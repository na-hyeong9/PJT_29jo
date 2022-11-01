import statistics
from django.shortcuts import render
from .models import Product
from .models import Review

# Create your views here.

def detail(request, product_pk):
    products = Product.objects.all()
    reviews = Review.objects.all()
    values_ = reviews.values('grade_1', 'grade_2', 'grade_3', 'grade_4')

        # annotate
        
        # for value in values:
        #     avg_score = statistics.mean(list(value.values()))
        #     break
        # review.grade_1 = avg_score
        # review.save()
  
    context = {
        "products" : products,
        "reviews" : reviews,
    }
    return render(request, "products/detail.html", context)