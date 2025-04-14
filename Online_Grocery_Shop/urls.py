"""Online_Grocery_Shop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from grocery.views import *
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path
from grocery import views
from grocery.views import Add_Cart 
from grocery.views import Booking_order

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',Home,name="home"),
    path('signup',views.Signup,name="signup"),
	path('about/',views.About,name='about'),
	path('contact/',views.Contact,name='contact'),
    path('login',views.Login,name="login"),
    path('logout',views.Logout,name="logout"),
    path('view_user',views.View_user,name="view_user"),
    path('add_product',views.Add_Product,name="add_product"),
    path('view_feedback', views.View_feedback, name='view_feedback'),
    path('view_product/<int:pid>/', views.View_prodcut, name='view_product'),
    path('admin_view_product', views.Admin_View_product, name='admin_view_product'),
    path('login_admin',views.Admin_Login,name="login_admin"),
    path('admin_viewBooking', views.Admin_View_Booking, name='admin_viewBooking'),
    path('view_categary/', views.View_Categary, name='view_categary'),
    path('add_categary', views.Add_Categary, name='add_categary'),
    path('add_cart/<int:pid>/',views.Add_Cart, name='add_cart'),
    path('delete_product/<int:pid>/', views.delete_product, name='delete_product'),
    path('delete_user/<int:pid>/', views.delete_user, name='delete_user'),
    path('delete_feedback/<int:pid>/', views.delete_feedback, name='delete_feedback'),
    path('cart',views.view_cart, name='cart'),
    path('payment/<str:total>/', views.payment, name='payment'),
    path('delete_booking/<str:pid>/<int:bid>/', views.delete_booking, name='delete_booking'),
    path('delete_admin_booking/<str:pid>/<int:bid>/', views.delete_admin_booking, name='delete_admin_booking'),
    path('booking_detail/<str:pid>/<int:bid>/', views.booking_detail, name='booking_detail'),
    path('admin_booking_detail/<str:pid>/<int:bid>/<int:uid>/', views.admin_booking_detail, name='admin_booking_detail'),
    path('Edit_status/(?P<str:pid>)/(?P<bid>[0-9]+)', Edit_status, name='Edit_status'),
    path('remove_cart/<int:pid>/', views.remove_cart, name='remove_cart'),
    path('booking/<str:pid>/', views.Booking_order, name='booking'),
    path('view_booking', views.View_Booking, name='view_booking'),
    path('profile', views.profile, name='profile'),
    path('edit_profile', views.Edit_profile, name='edit_profile'),
    path('delete_category/<int:pid>/',views.delete_category, name='delete_category'),
    path('admin_home', views.Admin_Home, name='admin_home'),
    path('change_password', views.Change_Password, name="change_password"),
    path('send_feedback/<int:pid>/', views.send_Feedback, name='send_feedback'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
