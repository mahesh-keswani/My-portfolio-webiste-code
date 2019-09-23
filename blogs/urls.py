from django.urls import path
from . import views

urlpatterns = [
    path('', views.show_all_blogs, name='showallblogs'),
    path('<int:blog_id>/', views.details, name="details") , # This basically means localhost:8000/blog/1 that 1 will ne stored into blog_id variable
 ]
