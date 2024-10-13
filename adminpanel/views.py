from django.shortcuts import render,get_object_or_404, redirect
from adminpanel.models import Profile,Blog,Comment,User
from userpanel.forms import RegistrationForm, LoginForm, ProfileForm, BlogForm, CommentForm,CustomPasswordChangeForm
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache


# Create your views here.

#Home page to display total count of users and blogs
@login_required(login_url='/404/')
@never_cache
def Admin_Home(request):

    total_users = Profile.objects.count()
    total_blogs = Blog.objects.count()

    context = {
        'total_users': total_users,
        'total_blogs': total_blogs,
    }
    return render(request,'adminpanel/admin_home.html',context)


#User list 
@login_required(login_url='/404/')
@never_cache
def User_List(request):
    profiles = Profile.objects.all()
    return render(request,'adminpanel/user_list.html',{'profiles':profiles})


#
@login_required(login_url='/404/')
@never_cache
def View_User(request, profile_id):
    profile = get_object_or_404(Profile, id=profile_id)
    return render(request,'adminpanel/view_user.html',{'profile':profile})

@login_required(login_url='/404/')
@never_cache
def Blog_List(request):
    blogs = Blog.objects.all()
    return render(request,'adminpanel/blog_list.html',{'blogs': blogs})

@login_required(login_url='/404/')
@never_cache
def Blog_View(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)
    comments = Comment.objects.filter( blog=blog)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.blog = blog
            comment.save()
            messages.success(request,'Comment added successfully')
            return redirect('adminpanel:blog_view', blog_id=blog_id)
        else:
            messages.error(request,'Failed to Comment')
    else:
        form = CommentForm()
    return render(request,'adminpanel/blog_view.html',{'form':form , 'blog':blog , 'comments':comments})

@login_required(login_url='/404/')
@never_cache
def Reset_Password(request, id=Profile.user):
    if request.method == 'POST':
        form = CustomPasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important to keep the user logged in
            messages.success(request, 'Your password was successfully updated!')
            return redirect('admin_home')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = CustomPasswordChangeForm(request.user)
    return render(request,'adminpanel/reset_password.html',{'form':form})

@login_required(login_url='/404/')
@never_cache
def Admin_Blog_Hide(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)
    
    blog.status = 'hidden'
    blog.save()
    messages.success(request, 'Blog Has Been Hidden Successfully')
    return redirect('blog_list')

@login_required(login_url='/404/')
@never_cache
def Admin_Blog_Show(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)

    blog = get_object_or_404(Blog, id=blog_id)

    # Check if the author of the blog is blocked
    if blog.author.profile.is_blocked:
        messages.error(request, 'This user is blocked. Unblock the user before making their blog visible.')
        return redirect('blog_list')

    blog.status = 'published'
    blog.save()
    messages.success(request, 'Blog has been made visible successfully.')
    return redirect('blog_list')

@login_required(login_url='/404/')
@never_cache
def Block_User(request, profile_id):
    
    user_profile = get_object_or_404(Profile, id=profile_id)
    user_profile.is_blocked = True
    user_profile.save()
    user_profile.user.is_active = False  # Deactivate the user account.
    user_profile.user.save()

    # Hide all blogs of the blocked user.
    Blog.objects.filter(author=user_profile.user).update(status='hidden')

    # Hide all comments of the blocked user.
    Comment.objects.filter(author=user_profile.user).update(status='hidden')

    messages.success(request, f'User {user_profile.user.username} has been blocked successfully.')
    return redirect('user_list')

@login_required(login_url='/404/')
@never_cache
def Unblock_User(request, profile_id):
    
    user_profile = get_object_or_404(Profile, id=profile_id)
    user_profile.is_blocked = False
    user_profile.save()
    user_profile.user.is_active = True  # Reactivate the user account.
    user_profile.user.save()

    # Set all blogs to draft for review.
    Blog.objects.filter(author=user_profile.user).update(status='draft')

    # Optionally, set comments to visible or keep them hidden until reviewed.
    Comment.objects.filter(author=user_profile.user).update(status='draft')  # Adjust as needed

    messages.success(request, f'User {user_profile.user.username} has been unblocked successfully.')
    return redirect('user_list')

@login_required(login_url='/404/')
@never_cache
def Admin_Comment_Hide(request, comment_id):
    
    comment = get_object_or_404(Comment, id=comment_id)
    comment.status = 'hidden'
    comment.save()
    messages.success(request, 'Comment has been hidden successfully.')
    return redirect('blog_view', blog_id=comment.blog.id)

@login_required(login_url='/404/')
@never_cache
def Admin_Comment_Show(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)

    # Check if the author of the comment is blocked
    if comment.author.profile.is_blocked:
        messages.error(request, 'This user is blocked. Unblock the user before making their comment visible.')
        return redirect('blog_view', blog_id=comment.blog.id)

    comment.status = 'visible'
    comment.save()
    messages.success(request, 'Comment has been made visible successfully.')
    return redirect('blog_view', blog_id=comment.blog.id)

@login_required(login_url='/404/')
@never_cache
def Admin_Sign_Out(request):
    logout(request)
    return redirect('admin_login')