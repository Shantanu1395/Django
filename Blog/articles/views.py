from django.shortcuts import render,redirect
from .models import Article
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from . import forms
# Create your views here.
def articlelist(request):

    article_list=Article.objects.all().order_by('date')
    context = {
        "article_list":article_list
    }
    return render(request,"articlelist.html",context)

def article_detail(request,slug):
    article=Article.objects.get(slug=slug)
    return render(request,'article_detail.html',{'article':article})

@login_required(login_url='/accounts/login')
def article_create(request):
    form = forms.CreateArticle()
    if request.method=="POST":
        form = forms.CreateArticle(request.POST,request.FILES)
        
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect('myarticles:list')
    else:     
        form = forms.CreateArticle()
    return render(request,'article_create.html',{'form':form})