from django.urls import path
from . import views

urlpatterns = [
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('logout', views.logout, name='logout'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('dashboard-dueno/', views.dashboard_dueno, name='dashboard_dueno'),
    path('crear-propiedad/', views.crear_propiedad, name='crear_propiedad'),
    path('editar-propiedad/<int:propiedad_id>/', views.editar_propiedad, name='editar_propiedad'),
    path('eliminar-propiedad/<int:propiedad_id>/', views.eliminar_propiedad, name='eliminar_propiedad'),
    path('publicar-propiedad/<int:propiedad_id>/', views.publicar_propiedad, name='publicar_propiedad'),

]
