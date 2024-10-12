from django.shortcuts import render,get_object_or_404, redirect
from adminpanel.models import Profile,Blog,Comment,User
from .forms import RegistrationForm, LoginForm, ProfileForm, BlogForm, CommentForm,CustomPasswordChangeForm
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache


# Create your views here.
@login_required(login_url='/404/')
@never_cache
def User_Home(request):
    blogs = Blog.objects.filter(status='published')
    profile = Profile.objects.get(user=request.user)
    return render(request,'userpanel/user_home.html',{'blogs': blogs,'profile':profile})

@login_required(login_url='/404/')
@never_cache
def Add_Blog(request):
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.author = request.user
            form.save()
            messages.success(request,'Blog Added Successfully!!!')
            return redirect('userpanel:user_home')
    else:
        form = BlogForm()
    return render(request,'userpanel/add_blog.html',{'form':form})

@login_required(login_url='/404/')
@never_cache
def Edit_Blog(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES, instance=blog)
        if form.is_valid():
            form.save()
            messages.success(request,'Blog Edited Successfully!!!')
            return redirect('userpanel:my_blog')
    else:
        form = BlogForm(instance=blog)
    return render(request,'userpanel/edit_blog.html',{'form': form})

@login_required(login_url='/404/')
@never_cache
def delete_blog(request,blog_id):
    blog = get_object_or_404(Blog, id=blog_id)
    if request.method == 'POST':
        blog.delete()
        messages.success(request, "Blog deleted successfully!")
        return redirect('userpanel:my_blog')

    return render(request,'userpanel/delete_blog.html',{'blog':blog})

@login_required(login_url='/404/')
@never_cache
def Blog_List(request):
    blogs = Blog.objects.filter(status='published')
    return render(request,'userpanel/blog_list.html',{'blogs': blogs})

@login_required(login_url='/404/')
@never_cache
def My_Blog(request):
    draft_posts = Blog.objects.filter(status='draft', author=request.user)
    published_posts = Blog.objects.filter(status='published', author=request.user)
    context = {
        'draft_posts': draft_posts,
        'published_posts': published_posts,
    }
    return render(request, 'userpanel/my_blog.html', context)


@login_required(login_url='/404/')
@never_cache
#BLOG VIEW and COMMENT SECTION
def View_Blog(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)
    comments = Comment.objects.filter( blog=blog,status='visible')
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.blog = blog
            comment.save()
            messages.success(request,'Comment added successfully')
            return redirect('userpanel:view_blog', blog_id=blog_id)
        else:
            messages.error(request,'Failed to Comment')
    else:
        form = CommentForm()
    return render(request,'userpanel/view_blog.html',{'form':form , 'blog':blog , 'comments':comments})


@login_required(login_url='/404/')
@never_cache
def Edit_Comment(request, comment_id, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)
    comment = get_object_or_404(Comment, id=comment_id)
    if request.method =='POST':
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            messages.success(request,'Comment Edited Successfully!!')
            return redirect('userpanel:view_blog', blog_id=blog_id)
    else:
        form = CommentForm(instance=comment)
    return render(request,'userpanel/edit_comment.html',{'form':form,'comment':comment,'blog':blog})

@login_required(login_url='/404/')
@never_cache
def delete_comment(request,comment_id, blog_id):
    comment = get_object_or_404(Comment, id = comment_id)
    blog = get_object_or_404(Blog, id=blog_id)
    if request.method == 'POST':
        blog_id = comment.blog.id
        comment.delete()
        messages.success(request, "Comment deleted successfully!")
        return redirect('userpanel:view_blog', blog_id=blog_id)

    return render(request,'userpanel/delete_comment.html',{'comment':comment,'blog':blog})

@login_required(login_url='/404/')
@never_cache
def View_Profile(request, profile_id):
    user = request.user
    profile = get_object_or_404(Profile, id=profile_id)
    blogs = Blog.objects.filter(author_id=profile_id)
    is_owner = request.user == profile.user
    return render(request,'userpanel/view_profile.html',{'profile':profile,'blogs':blogs,'is_owner':is_owner})


@login_required(login_url='/404/')
@never_cache
def Edit_Profile(request, profile_id):
    profile = get_object_or_404(Profile, id=profile_id, user=request.user)

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()

            user = request.user
            user.email = request.POST.get('email', user.email)
            user.save()

            messages.success(request, 'Profile Updated Successfully')
            return redirect('userpanel:view_profile', profile_id=profile_id)
        else:
            messages.error(request, 'Failed to Update Profile')
    else:
        form = ProfileForm(instance=profile)
    context = {
        'form': form,
        'username': request.user.username,
        'email': request.user.email,
    }
    
    return render(request, 'userpanel/edit_profile.html',context)


@login_required(login_url='/404/')
@never_cache
def Reset_Password(request, id=Profile.user):
    if request.method == 'POST':
        form = CustomPasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important to keep the user logged in
            messages.success(request, 'Your password was successfully updated!')
            return redirect('userpanel:user_home')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = CustomPasswordChangeForm(request.user)
    
    return render(request, 'userpanel/reset_password.html', {'form': form})

@login_required(login_url='/404/')
@never_cache
def sign_out(request):
    # Log out the user and redirect to the home page
    logout(request)
    return redirect('sitevisitor:home')