from django.shortcuts import render

# Create your views here.
def catalog(request):
    return render(request, "Shop/catalog.html")