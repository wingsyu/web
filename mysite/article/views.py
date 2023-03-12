from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def hello(request):
    return HttpResponse("Hello World!!!!")



# 导入数据模型Article
from .models import Article

def article_list(request):
    # 取出所有博客文章
    articles = Article.objects.all()
    # 需要传递给模板（templates）的对象
    context = { 'articles': articles }
    # render函数：载入模板，并返回context对象
    return render(request, 'article/list.html', context)


