from django.shortcuts import render
from django.http import HttpResponse
from  .models import Article,ArtType

# Create your views here.
def index(request):
    return render(request,'products/base.html')

def home(request):
    return render(request,'products/home.html')

def contact(request):
    return render(request,'products/contactus.html')

def about(request):
    return render(request,'products/aboutus.html')


def product_by_name(request):
    q= Article.objects.all()
    output = ','.join([a.article_name for a in q])
    return HttpResponse(output)

def product_details(request,ptype):
    q = ArtType.objects.get(type=ptype)
    type_id = q.id
    details = Article.objects.filter(article_type = type_id)

    return render(request,'products/detail.html',{'details':details,'ptype':ptype})

def products(request):
    return render(request,'products/detail.html')

def gallery(request):
    images = Article.objects.values('article_image')
    return render(request,'products/gallery.html',{'image_list': images})