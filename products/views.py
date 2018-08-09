from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect

from .forms import ContactForm
from  .models import Article,ArtType

from django.contrib import messages
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

def product_enquiry(request,ptype,pid):
    spec_product = Article.objects.get(id = pid)

    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            phone = form.cleaned_data['phone']
            message = 'Message received from: ' + str(phone)+'\n' + str(spec_product.article_name)+ '\n'+form.cleaned_data['message'] + '\n'
            try:
                send_mail(subject, message, from_email, ['shruti.karva@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            messages.success(request, 'Message sent. You will be contacted soon. Meanwhile have a look at other designs.')
            return redirect('../')

    return render(request,'products/enquiry.html',{'prod':spec_product,'ptype':ptype,'form':form})

def products(request):
    return render(request,'products/detail.html')

def gallery(request):
    images = Article.objects.values('article_image')
    return render(request,'products/gallery.html',{'image_list': images})

