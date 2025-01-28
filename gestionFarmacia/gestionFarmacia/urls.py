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
from inventario import views as inventario_views
from pedidos import views as pedidos_views
from gestionFarmacia import views as main_views
from django.contrib.auth import views as auth_views

urlpatterns = [

    path('admin/', admin.site.urls),


    path('', main_views.home, name='home'),


    path('clientes/', usuarios_views.lista_clientes, name='lista_clientes'),
    path('empleados/', usuarios_views.lista_empleados, name='lista_empleados'),
    path('dashboard/', usuarios_views.dashboard, name='dashboard'),
    path('perfil/', usuarios_views.perfil, name='perfil'),
    path('registro/', usuarios_views.registro, name='registro'),


    path('sucursales/', inventario_views.lista_sucursales, name='lista_sucursales'),
    path('productos/', inventario_views.lista_productos, name='lista_productos'),
    path('inventario/', inventario_views.consultar_inventario, name='consultar_inventario'),
    path('inventario/sucursal/<int:sucursal_id>/', inventario_views.consultar_inventario_por_sucursal, name='consultar_inventario_por_sucursal'),
    path('transferir/<int:sucursal_id>/', inventario_views.transferir_producto, name='transferir_producto'),


    path('pedidos/', pedidos_views.lista_pedidos, name='lista_pedidos'),
    path('pedidos/<int:pedido_id>/', pedidos_views.detalle_pedido, name='detalle_pedido'),
    path('pedidos/<int:pedido_id>/confirmar/', pedidos_views.confirmar_pedido, name='confirmar_pedido'),
    path('pedidos/crear/', pedidos_views.crear_pedido, name='crear_pedido'),
    path('pedidos/mis_pedidos/', pedidos_views.mis_pedidos, name='mis_pedidos'),


    path('login/', auth_views.LoginView.as_view(template_name='usuarios/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/login/'), name='logout'),
]
