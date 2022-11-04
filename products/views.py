import statistics
from django.shortcuts import render, redirect, get_object_or_404, resolve_url
from .models import Product, Review
from .forms import ReviewCreationForm
from django.db.models import Avg
from django.contrib.auth import get_user_model

# Create your views here.

def detail(request, product_pk):
    product = get_object_or_404(Product, pk=product_pk)
    reviews = Review.objects.all()
    grade_all = reviews.aggregate(Avg('grade_durability'), Avg('grade_price'), Avg('grade_design'), Avg('grade_practicality'))
    grade_avg = reviews.aggregate(Avg('grade_avg'))
    # 키 -값 쌍으로
  
    context = {
        "product" : product,
        "reviews" : reviews,
        "grade_all" : grade_all,
        "grade_avg" : grade_avg,
    }
    return render(request, "products/detail.html", context)

def reviews_create(request, product_pk):
    if request.method == "POST":
        product = Product.objects.get(pk=product_pk)
        # if request.method == "POST":
        #     print(request)
            # forms = ReviewCreationForm(request.POST, request.FILES)
            # if forms.is_valid():
                # review = forms.save(commit=False)
                # print(review)
        user = request.user
        content = request.POST.get('content')
        review_image = request.FILES.get('image')
        grade_1 = request.POST.get('grade_durability')
        grade_2 = request.POST.get('grade_price')
        grade_3 = request.POST.get('grade_design')
        grade_4 = request.POST.get('grade_practicality')
        avg_list = list(map(float, [grade_1, grade_2, grade_3, grade_4]))
        avg_score = statistics.mean(avg_list)
        
        review = Review()
        review.content = content
        review.product = product
        review.user = user
        review.review_image = review_image
        review.grade_durability = grade_1
        review.grade_price = grade_2
        review.grade_design = grade_3
        review.grade_practicality = grade_4
        review.grade_avg = avg_score
        review.save()
            # 변수명에 어떤 필드인지 직관적으로 알 수 있도록
        return redirect('{}#review_{}'.format(resolve_url('products:detail', product_pk), review.id))
        
    else:
        forms = ReviewCreationForm()
    context = {
        "forms" : forms,
    }
    return render(request, "products/create.html", context)

def reviews_update(request, product_pk, review_pk):
        review = Review.objects.get(pk=review_pk)
        if request.method == "POST":
            forms = ReviewCreationForm(request.POST, request.FILES, instance=review)
            if forms.is_valid():
                forms.save()
                return redirect('{}#review_{}'.format(resolve_url('products:detail', product_pk), review.id))
        
        else:
            forms = ReviewCreationForm(instance=review)
        context = {
            "forms" : forms,
        }
        return render(request, "products/update.html", context)
    
def reviews_delete(request, product_pk, review_pk):
    review = Review.objects.get(pk=review_pk)
    review.delete()
    return redirect("products:detail", product_pk)

def reviews_likes(request, product_pk, review_pk):
    review = get_object_or_404(Review, pk=review_pk)

    if request.user in review.review_likes.all(): 
        # 좋아요 삭제하고
        review.review_likes.remove(request.user)
    else:
        # 좋아요 추가하고 
        review.review_likes.add(request.user)
    # 상세 페이지로 redirect
    return redirect("products:detail", product_pk)