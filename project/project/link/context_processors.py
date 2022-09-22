from .models import Link, column_list


def links_column1(request):
    """
    Con questa funzione definisco la lista dei link
    """
    item = Link.objects.filter(column=column_list[0][0])
    context = {"links_column1": item}

    return context


def links_column2(request):
    """
    Con questa funzione definisco la lista dei link
    """
    item = Link.objects.filter(column=column_list[1][0])
    context = {"links_column2": item}

    return context


def links_column3(request):
    """
    Con questa funzione definisco la lista dei link
    """
    item = Link.objects.filter(column=column_list[2][0])
    context = {"links_column3": item}

    return context
