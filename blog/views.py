from django.shortcuts import render
from blog.models import *
from django.views.generic import View
from django.db.models import Q


class StatyaView(View):
    def get(self, request):
        s = Statya.objects.all()
        context = {"statya": s}
        return render(request, "blog/list.html", context)


class SlugFilter(View):
    def get(self, request, slug):
        f = Statya.objects.filter(slug=slug)
        allstatyas = Statya.objects.get(slug=slug)
        allstatyas.prosmotry += 1
        allstatyas.save()
        context = {"single": f,
                   "ragnarek": allstatyas}
        return render(request, "blog/single.html", context)


class SearchView(View):

    def post(self, request, *args, **kwargs):
        query = self.request.POST.get('q')
        founded = Statya.objects.filter(Q(title__icontains=query) | Q(text__icontains=query))
        return render(request, "blog/search.html", {"founded": founded})
