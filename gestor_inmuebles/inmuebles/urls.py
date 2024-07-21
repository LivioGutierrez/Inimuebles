from django.urls import path
from inmuebles import views

urlpatterns = [
    path('',views.index,name='index'),
    path('agregarinmueble/', views.agregar_inmueble, name='agregar_inmueble'),
    path('registrar/', views.RegistroView.as_view(), name='register'),
    path('login/', views.LoginView.as_view(), name='login'),
]