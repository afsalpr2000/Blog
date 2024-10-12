from django.urls import path
from.views import Admin_Home, User_List, View_User, Blog_List, Blog_View, Reset_Password, Admin_Blog_Hide, Admin_Blog_Show, Block_User, Unblock_User, Admin_Comment_Hide, Admin_Comment_Show, Admin_Sign_Out



urlpatterns = [
    path('',Admin_Home, name = 'admin_home'),
    path('user_list/',User_List, name = 'user_list'),
    path('view_user/<int:profile_id>/',View_User, name = 'view_user'),
    path('blog_list/',Blog_List, name = 'blog_list'),
    path('blog_view/<int:blog_id>/',Blog_View, name = 'blog_view'),
    path('reset_password/',Reset_Password, name = 'reset_password'),
    path('hide_blog/<int:blog_id>/', Admin_Blog_Hide, name='admin_blog_hide'),
    path('show_blog/<int:blog_id>/', Admin_Blog_Show, name='admin_blog_show'),
    path('block_user/<int:profile_id>/', Block_User, name='block_user'),
    path('unblock_user/<int:profile_id>/', Unblock_User, name='unblock_user'),
    path('hide_comment/<int:comment_id>/',Admin_Comment_Hide, name='admin_comment_hide'),
    path('show_comment/<int:comment_id>/',Admin_Comment_Show, name='admin_comment_show'),
    path('admin_sign_out/', Admin_Sign_Out, name='admin_sign_out'),
]
