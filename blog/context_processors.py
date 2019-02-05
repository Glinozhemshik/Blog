from blog.forms import Search


def search(request):
    search = Search()
    context = {"search": search}
    return context
