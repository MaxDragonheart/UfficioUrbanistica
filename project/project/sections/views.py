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

def single_category(request, slug_category):
    """
    Con questa funzione definisco la lista dei post della singola categoria
    """
    category = get_object_or_404(Section, slug_category=slug_category)
    if request.user.is_staff:
        blogpost_full = SectionPost.objects.filter(category=category)
    else:
        blogpost_full = post_filter.filter(category=category)

    paginator = Paginator(blogpost_full, 10)
    page = request.GET.get("pagina")
    post_list = paginator.get_page(page)

    context = {
            "category": category,
            "post_list": post_list,
            }
    return render(request, "single_category.html", context)
