from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import ArticleForm, CommentForm, PostSearchForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse


# Create your views here.


def index(request, category_slug=None):
    articles = Article.objects.order_by("-pk")
    articles_hits = Article.objects.order_by("-hits")
    current_category = None
    categories = Category.objects.all()
    articles = Article.objects.filter(available_display=True)
    if category_slug:
        current_category = get_object_or_404(Category, slug=category_slug)
        articles = articles.filter(category=current_category)
    context = {
        "articles": articles,
        "articles_hits": articles_hits,
        "current_category": current_category,
        "categories": categories,
    }
    return render(request, "articles/index.html", context)


@login_required
def create(request):
    if request.method == "POST":
        # DB에 저장하는 로직
        article_form = ArticleForm(request.POST, request.FILES)
        # 유효성 검사
        if article_form.is_valid():
            article = article_form.save(commit=False)
            # 로그인한 유저 => 작성자네!
            article.user = request.user
            article.save()

            return redirect("articles:index")
    else:
        article_form = ArticleForm()
    context = {"article_form": article_form}
    return render(request, "articles/form.html", context=context)


def article_in_category(request, category_slug=None):
    current_category = None
    categories = Category.objects.all()
    articles = Article.objects.filter(available_display=True)
    if category_slug:
        current_category = get_object_or_404(Category, slug=category_slug)
        articles = articles.filter(category=current_category)
    context = {
        "articles": articles,
        "current_category": current_category,
        "categories": categories,
    }
    return render(request, "articles/list.html", context)


def detail(request, pk, article_slug):
    # 특정 글을 가져온다.
    article = get_object_or_404(Article, pk=pk, slug=article_slug)
    comment_form = CommentForm()

    # 조회수 측정
    article.hits += 1
    article.save()

    # template에 객체 전달
    context = {
        "article": article,
        # 역참조 (article에 포함된 comment data를 전부 불러온다.)
        "comments": article.comment_set.all(),
        "comment_form": comment_form,
    }
    return render(request, "articles/detail.html", context)


@login_required
def update(request, pk, article_slug):
    article = Article.objects.get(pk=pk, slug=article_slug)
    if request.user == article.user:
        if request.method == "POST":
            article_form = ArticleForm(request.POST, request.FILES, instance=article)
            if article_form.is_valid():
                article_form.save()
                return redirect("articles:detail", article.pk)
        else:
            article_form = ArticleForm(instance=article)
        context = {"article_form": article_form}
        return render(request, "articles/form.html", context)
    else:
        messages.warning(request, "작성자만 수정할 수 있습니다.")
        return redirect("articles:detail", article.pk, article_slug)


@login_required
def delete(request, pk, article_slug):
    Article.objects.get(pk=pk, slug=article_slug).delete()

    return redirect("articles:index")


@login_required
def comment_create(request, pk, article_slug):
    # 특정 게시물 가져오기
    article = Article.objects.get(pk=pk, slug=article_slug)
    # comment 폼 가져오기
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.article = article
        comment.user = request.user
        comment.save()
    return redirect("articles:detail", article.pk)


@login_required
def comment_update(request, pk, article_slug):
    if request.method == "POST":
        # 특정 게시물 가져오기
        article = Article.objects.get(pk=pk, slug=article_slug)
        comment_update = article.comment_set.all()
        # comment 폼 가져오기
    return redirect("articles:detail", article.pk)


@login_required
def comments_delete(request, article_pk, article_slug, comment_pk):
    if request.user.is_authenticated:
        comment = get_object_or_404(Comment, pk=comment_pk)
        if request.user == comment.user:
            comment.delete()
    return redirect("articles:detail", article_pk, article_slug)


@login_required
def like(request, pk, article_slug):
    article = get_object_or_404(Article, pk=pk, slug=article_slug)
    # 만약에 로그인한 유저가 이 글을 좋아요를 눌렀다면,
    # if article.like_users.filter(id=request.user.id).exists():
    if request.user in article.like_users.all():
        # 좋아요 삭제하고
        article.like_users.remove(request.user)
        is_liked = False
    else:
        # 좋아요 추가하고
        article.like_users.add(request.user)
        is_liked = True
    # 상세 페이지로 redirect
    context = {"isLiked": is_liked, "likeCount": article.like_users.count()}
    return JsonResponse(context)
