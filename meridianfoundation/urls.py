from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

app_name = 'core'

from .views import index,user_type,register,contact_us,profile,SignUpView,StudentSignUpView,TeacherSignUpView,DonorSignUpView,PartnerSignUpView,PublicSignUpView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index,name = 'index'),
    path('profile/', profile, name='profile'),
    path('accounts/', include('allauth.urls')),
    path('register/', register,name = 'register'),
    path('contact_us/', contact_us,name = 'contact_us'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('accounts/signup/',SignUpView.as_view(), name='signup'),
    path('accounts/signup/student/', StudentSignUpView.as_view(), name='student'),
    path('accounts/signup/teacher/', TeacherSignUpView.as_view(), name='teacher'),
    path('accounts/signup/donor/', DonorSignUpView.as_view(), name='donor'),
    path('accounts/signup/partner/', PartnerSignUpView.as_view(), name='partner'),
    path('accounts/signup/public/', PublicSignUpView.as_view(), name='public'),


]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
