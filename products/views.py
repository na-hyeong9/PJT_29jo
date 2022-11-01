from django.shortcuts import render

# Create your views here.
def detail(request, product_pk):
    return render(request, "products/detail.html")