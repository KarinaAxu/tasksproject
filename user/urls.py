from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('login/', views.login_page, name='login'),
    path('register/', views.register_page, name='register'),
    path('logout/', views.logout, name='logout'),
    path('settings/', views.profile_page, name='settings_page'),
    path('forgot_password/', views.forgot_password, name='forgot_password'),
    path('reset-password/<slug:token>', views.reset_password, name='reset_password'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
