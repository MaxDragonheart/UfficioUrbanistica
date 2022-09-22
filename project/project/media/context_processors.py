from .models import FileUpload


def highlighted_media(request):
    """
    Con questa funzione definisco la lista dei media evidenziati
    """
    item = FileUpload.objects.filter(highlighted=True)
    context = {"highlighted_media": item}

    return context
