from django.shortcuts import render, HttpResponse, redirect
from carritoApp.models import Producto
from carritoApp.carrito import Carrito

# Create your views here.
def tienda(request):
    producto = Producto.objects.all()
    return render(request, "tienda.html",{
        'productos':producto
    })

def agregar_producto(request,producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.agregar(producto)
    return redirect("tienda")

def eliminar(request, producto_id):
    carrito = Carrito(request)
    producto = producto.objects.get(id=producto_id)
    carrito.eliminar(producto)
    return redirect("tienda")

def restar(request,producto_id):
    carrito = Carrito(request)
    producto = producto.objects.get(id=producto_id)
    carrito.retar(producto)
    return redirect("tienda")

def limpiar(request):
    carrito = Carrito(request)
    carrito.limpiar()
    return redirect("tienda")