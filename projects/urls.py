from django.urls import path
from . import views

urlpatterns = [
	path('', views.allprojects, name="allprojects"),
    path('<int:project_id>/', views.details, name="projectdetails") , # This basically means localhost:8000/projects/1 that 1 will ne stored into project_id variable
 ]