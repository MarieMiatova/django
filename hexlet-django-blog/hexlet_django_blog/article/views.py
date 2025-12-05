from django.views import View
from django.shortcuts import render


class ArticleIndexView(View):
    def get(self, request, *args, **kwargs):
        return render(
            request,
            "articles/index.html",
            context={
                "app_name": "hexlet_django_blog.article"
            }
        )