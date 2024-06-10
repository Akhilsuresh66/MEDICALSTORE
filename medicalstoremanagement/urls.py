from django.contrib import admin
from django.urls import path,include
from medical import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.medical),
    path('home/',include('med_acc.urls')),
    path('signup/',views.signup_page,name='signup'),
    path('login/',views.login_page,name='login'),
    path('productsapi/', include('productsapi.urls')),
]