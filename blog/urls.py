from django.urls import path
from . import views


urlpatterns = [
    path('create_post/', views.create_post, name='create_post'),
    path('home/', views.home, name='home'),
    path('post/<int:pk>/', views.post_details, name= 'post_details'),
    path('', views.login_custom, name='login'),
    path('logout/', views.logout, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('post/delete/<int:pk>/', views.delete_post, name='delete_post'),

]