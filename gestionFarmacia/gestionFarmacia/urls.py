"""
URL configuration for gestionFarmacia project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from usuarios import views as usuarios_views
from inventario import views as inventario_views, views
from pedidos import views as pedidos_views
from gestionFarmacia import views as main_views  # Importar vistas generales

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main_views.home, name='home'),  # Página de inicio
    path('clientes/', usuarios_views.lista_clientes, name='lista_clientes'),
    path('empleados/', usuarios_views.lista_empleados, name='lista_empleados'),
    path('sucursales/', inventario_views.lista_sucursales, name='lista_sucursales'),
    path('pedidos/<int:pedido_id>/', pedidos_views.detalle_pedido, name='detalle_pedido'),
    path('pedidos/', pedidos_views.lista_pedidos, name='lista_pedidos'),
    path('productos/', views.lista_productos, name='lista_productos'),

]

