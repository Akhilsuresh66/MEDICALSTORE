from django.urls import path
from . import views

urlpatterns = [
    path('signup',views.signup,name='signup_api'),
    path('login', views.login, name='login_api'),
    path('create', views.create_Medicine, name='createproductapi'),
    path('list', views.list_Medicine, name='retrieveproductapi'),
    path('<int:pk>/update', views.update_Medicine, name='updateproductapi'),
    path('<int:pk>/delete', views.delete_Medicine, name='deleteproductapi'),
    path('search', views.searchmedicine_api, name='search_medicine_api'),

]
