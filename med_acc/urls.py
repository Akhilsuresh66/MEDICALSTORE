from . import views
from django.urls import path

urlpatterns = [
        path('',views.home,name='home'),
        path('create/',views.create_medicine,name='addmedicine'),
        path('edit/<int:pk>/',views.update_med,name='editmedicine'),
        path('delete/<int:pk>/',views.del_medicine,name='dltmedicine'),
        path('search/',views.search_medicine,name='searchmedicine'),
        path('logout/',views.user_logout,name='logoutuser'),


    ]