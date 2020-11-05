from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include


app_name = 'core'

from .views import IndexView,item_detail, user_type,register,contact_us,profile,SignUpView,\
    StudentSignUpView,TeacherSignUpView,DonorSignUpView,PartnerSignUpView,PublicSignUpView, search, \
    item_detail_update, item_detail_delete, item_detail_create

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='index'),
    path('item_detail/<id>', item_detail, name='item_detail'),
    path('item_detail_create/', item_detail_create, name = 'item_detail_create'),
    path('item_detail_update/<id>/update/', item_detail_update, name='item_detail_update'),
    path('item_detail_delete/<id>/delete/', item_detail_delete, name='item_detail_delete'),
    path('profile/', profile, name='profile'),
   # path('search/', search, name ="search"),
    path('register/', register,name = 'register'),
    path('contact_us/', contact_us,name = 'contact_us'),

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
