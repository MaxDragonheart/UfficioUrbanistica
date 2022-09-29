from itertools import chain

from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render, get_object_or_404

from .models import OGCLayer, WebGISProject, Categories


# def wms_list(request):
#     """[Function view](https://docs.djangoproject.com/en/4.0/topics/http/views/) that deliver the list
#     of objects from OGCLayer Model.
#     Args:
#         request:
#     Returns:
#         JSON
#     """
#     list = OGCLayer.objects.all()
#
#     context = {
#         "name": "Elenco dei layer",
#         "list": list
#     }
#     template = "wms/wms_list.html"
#     return render(request, template, context)


def single_wms(request, slug_post):
    """[Function view](https://docs.djangoproject.com/en/4.0/topics/http/views/) that deliver the list
    of contents related to a single object from OGCLayer Model.
    Args:
        request:
        slug_post: String.
    Returns:
        JSON
    """
    object = get_object_or_404(OGCLayer, slug_post=slug_post)

    context = {
        "single_object": object,
    }
    template = "wms/single_wms.html"
    return render(request, template, context)


# def webgis_list(request):
#     """[Function view](https://docs.djangoproject.com/en/4.0/topics/http/views/) that deliver the list
#     of objects from WebGISProject Model.
#     Args:
#         request:
#     Returns:
#         JSON
#     """
#     list = WebGISProject.objects.all()
#     context = {
#         "name": "Elenco dei WebGIS",
#         "list": list
#     }
#     template = "webgis/webgis_list.html"
#     return render(request, template, context)


def single_webgis(request, slug_post):
    """[Function view](https://docs.djangoproject.com/en/4.0/topics/http/views/) that deliver the list
    of contents related to a single object from WebGISProject Model.
    Args:
        request:
        slug: String.
    Returns:
        JSON
    """
    object = get_object_or_404(WebGISProject, slug_post=slug_post)

    context = {
        "single_object": object,
    }
    template = "webgis/single_webgis.html"
    return render(request, template, context)


def opengeodata(request):
    wms = OGCLayer.objects.all()
    webgis = WebGISProject.objects.all()

    item_list = list(chain(wms, webgis))

    paginator = Paginator(item_list, 10)
    page = request.GET.get("pagina")
    objects = paginator.get_page(page)

    context = {
        "objects": objects,
    }
    template = "opengeodata.html"
    return render(request, template, context)


def search(request):
    template = "opengeodata.html"

    if "q" in request.GET:
        querystring = request.GET.get("q")
        wms = OGCLayer.objects.filter(
                                Q(title__icontains=querystring) |
                                Q(description__icontains=querystring) |
                                Q(contents__icontains=querystring)
                            )
        webgis = WebGISProject.objects.filter(
                                Q(title__icontains=querystring) |
                                Q(description__icontains=querystring) |
                                Q(contents__icontains=querystring)
                            )

        objects = list(chain(wms, webgis))

        # paginator = Paginator(item_list, 2)
        # page = request.GET.get("pagina")
        # objects = paginator.get_page(page)

        context = {
            "objects": objects,
        }
        return render(request, template, context)
    else:
        return render(request, template)


def single_category(request, slug_category):
    """
    Con questa funzione visualizzo la singola categoria
    """
    category = get_object_or_404(Categories, slug_category=slug_category)
    wms = OGCLayer.objects.filter(categories=category)
    webgis = WebGISProject.objects.filter(categories=category)

    context = {
            "category": category,
            "objects": list(chain(wms, webgis)),
            }

    return render(request, "opengeodata.html", context)
