from django.shortcuts import render
from .models import Article

# Create your views here.
def articles(request):
    articles = Article.objects.all().order_by('date')
    return render(request,'blog/articles.html',{'articles':articles})

def article_detail(request, slug):
   article=Article.objects.get(slug=slug)
   return render(request,'blog/article_detail.html',{'article':article})
