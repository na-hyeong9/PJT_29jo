from django.shortcuts import render, redirect
from products.models import Product
from accounts.models import User
from .models import CartItem
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
# Create your views here.

def _cart_id(request):
    cart = request.session.session_key
  
    if not cart:
        cart = request.session.create()
        
    return cart

@login_required
def add_cart(request, product_id):
	# 상품을 담기 위해 해당 상품 객체를 product 변수에 할당
    product = Product.objects.get(pk=product_id)

    try:
    	# 장바구니는 user 를 FK 로 참조하기 때문에 save() 를 하기 위해 user 가 누구인지도 알아야 함
        cart = CartItem.objects.get(product__id=product.pk, user__id=request.user.pk)
        if cart:
            if cart.product.title == product.title:
                cart.quantity += 1
                cart.save()
    except CartItem.DoesNotExist:
        user = User.objects.get(pk=request.user.pk)
        cart = CartItem(
            user=user,
            product=product,
            quantity=1,
        )
        cart.save()
    return redirect('articles:index')

@login_required
def my_cart(request):
    """
    각 유저의 장바구니 공간
    """
    cart_item = CartItem.objects.filter(user__id=request.user.pk)
    # 장바구니에 담긴 상품의 총 합계 가격
    total_price = 0
    # for loop 를 순회하여 각 상품 * 수량을 total_price 에 담는다
    for each_total in cart_item:
        total_price += each_total.product.price * each_total.quantity
    if cart_item is not None:
        context = {
        	# 없으면 없는대로 빈 conext 를 템플릿 변수에서 사용
            'cart_item': cart_item,
            'total_price': total_price,
        }
        return render(request, 'cart/cart.html', context)
    return redirect('product:cart')

# def minus_cart_item(request, -):
#     cart_item = CartItem.objects.filter(product__id=-)
#     product = Product.objects.get(pk=-)
#     try:
#         for item in cart_item:
#             if item.product.name == product.name:
#                 if item.quantity > 1:
#                     item.quantity -= 1
#                     item.save()
#                 return redirect('product:my-cart')
#             else:
#                 return redirect('product:my-cart')
#     except CartItem.DoesNotExist:
#         raise Http404