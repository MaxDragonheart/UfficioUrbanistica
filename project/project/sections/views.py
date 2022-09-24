from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from django.db.models.functions import Now
from django.core.paginator import Paginator

from .models import Section, SectionPost

post_filter = SectionPost.objects.filter(draft=False, publishing_date__lte=Now())


def tmp_homepage(request):
    """
    Home page temporanea
    :param request:
    :return:
    """
    template = "index_tmp.html"
    return render(request, template)


def homepage(request):
    """
    Con questa funzione definisco la lista delle categorie
    """
    category_list = Section.objects.all()
    context = {"category_list": category_list}
    template = "index.html"
    return render(request, template, context)


def single_category(request, slug_category):
    """
    Con questa funzione definisco la lista dei post della singola categoria
    """
    category = get_object_or_404(Section, slug_category=slug_category)
    if request.user.is_staff:
        post_list = SectionPost.objects.filter(category=category)
        highlighted = post_list.filter(highlighted=True)[:1]
    else:
        post_list = post_filter.filter(category=category)
        highlighted = post_list.filter(highlighted=True)[:1]

    context = {
            "category": category,
            "post_list": post_list,
            "highlighted": highlighted,
            }
    return render(request, "single_category.html", context)


def all_posts(request):
    """
    Con questa funzione ottengo l'elenco di tutte le pubblicazioni
    """
    if request.user.is_staff:
        articles = SectionPost.objects.all()
    else:
        articles = post_filter

    paginator = Paginator(articles, 10)
    page = request.GET.get("pagina")
    post_list = paginator.get_page(page)

    context = {
        "post_list": post_list,
    }
    template = "all_posts.html"
    return render(request, template, context)


def single_post(request, slug_post, slug_category):
    """
    Con questa funzione visualizzo il singolo post
    """
    if request.user.is_staff:
        article = get_object_or_404(SectionPost, slug_post=slug_post)
    else:
        article = get_object_or_404(post_filter, slug_post=slug_post)
    category = get_object_or_404(Section, slug_category=slug_category)
    category_article = SectionPost.objects.filter(category=category)
    context = {
            "category": category,
            "article": article,
            "category_article": category_article
            }
    return render(request, "single_post.html", context)


def search(request):
    template = "search_article.html"

    if "q" in request.GET:
        querystring = request.GET.get("q")
        post_list = post_filter.filter(
                                Q(title__icontains=querystring) |
                                Q(description__icontains=querystring) |
                                Q(contents__icontains=querystring) |
                                Q(category__category_name__icontains=querystring)
                            )

        context = {"post_list": post_list}
        return render(request, template, context)
    else:
        return render(request, template)
