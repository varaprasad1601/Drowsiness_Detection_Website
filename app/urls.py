from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('train',views.train,name='train'),
    path('user_register',views.user_register,name='user_register'),
    path('company',views.company,name='company'),
    path('check_company',views.check_company,name='check_company'),
    path('app_api',views.app_api,name='app_api'),
    path('company_api',views.company_api,name='company_api'),
]