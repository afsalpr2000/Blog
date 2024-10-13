from django.conf import settings
from django.urls import path
from.views import Home, Login, Registration, Forgot_Password, Reset_Password, otp, error_page
from django.conf.urls.static import static

app_name = 'sitevisitor'

urlpatterns = [
    path('',Home, name = 'home'),
    path('login/',Login, name = 'login'),
    path('registration/',Registration, name = 'registration'),
    path('forgot_password/',Forgot_Password, name = 'forgot_password'),
    path('reset_password/',Reset_Password, name = 'reset_password'),
    path('otp/',otp, name = 'otp'),
    path('404/',error_page, name='error_page')

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)