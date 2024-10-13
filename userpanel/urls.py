from django.urls import path
from.views import User_Home, Add_Blog, Blog_List, My_Blog, View_Blog, Edit_Blog, View_Profile, Edit_Profile, Reset_Password, Edit_Comment, delete_comment, delete_blog, sign_out
from django.conf import settings
from django.conf.urls.static import static


app_name = 'userpanel'

urlpatterns = [
    path('user_home/',User_Home, name = 'user_home'),
    path('add_blog/',Add_Blog, name = 'add_blog'),
    path('blog_list/',Blog_List, name = 'blog_list'),
    path('my_blog/',My_Blog, name = 'my_blog'),
    path('view_blog/<int:blog_id>/',View_Blog, name = 'view_blog'),
    path('edit_blog/<int:blog_id>/',Edit_Blog, name = 'edit_blog'),
    path('delete_blog/<int:blog_id>/', delete_blog, name="delete_blog"),
    path('view_profile/<int:profile_id>/',View_Profile, name = 'view_profile'),
    path('edit_profile/<int:profile_id>/',Edit_Profile, name = 'edit_profile'),
    path('reset_password/',Reset_Password, name = 'reset_password'),
    path('edit_comment/<int:comment_id>/<int:blog_id>/',Edit_Comment, name = 'edit_comment'),
    path('delete_comment/<int:comment_id>/<int:blog_id>/', delete_comment, name="delete_comment"),
    path('sign_out/', sign_out, name='sign_out'),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)