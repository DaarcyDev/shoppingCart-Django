from django.shortcuts import render, HttpResponse

# Create your views here.
def tienda(request):
    # return HttpResponse("HOLA")
    return render(request, "tienda.html")