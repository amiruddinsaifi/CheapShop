from django.shortcuts import render
from math import ceil
from django.http import HttpResponse
from . models import Product,Contect
# Create your views here.
def index(request):
    # products=Product.objects.all()
    # print(products)
    # n=len(products)
    # nSlides=(n//4+ceil((n/4)-n//4))
    # params={'no_of_Slides':nSlides,'range':range(nSlides),'product':products}
    # allprods=[[products,range(1,nSlides),nSlides],
    #          [products,range(1,nSlides),nSlides],
    #           [products,range(1,nSlides),nSlides]]
    allprods=[]
    prodcats=Product.objects.values('category','id')
    cats={item['category'] for item in prodcats}
    for cat in cats:
        prod=Product.objects.filter(category=cat)
        n = len(prod)
        nSlides=(n//4+ceil((n/4)-n//4))
        allprods.append([prod,range(1,nSlides),nSlides])

    params={'allprods':allprods}
    return render(request, 'shop/index.html',params)
def about(request):
    return render(request, 'shop/about.html')
def contect(request):
    if request.method=="POST":
        print("request")
        name=request.POST.get('name','')
        email=request.POST.get('email','')
        phone=request.POST.get('phone','')
        desc=request.POST.get('desc','')
        print(name,email,phone,desc)
        contect=Contect(name=name,email=email,phone=phone,desc=desc)
        contect.save()
    return render(request, 'shop/contect.html')
def tracker(request):
    return render(request, 'shop/tracker.html')
def search(request):
    return render(request, 'shop/search.html')
def prodView(request,myid):
    product=Product.objects.filter(id=myid)
    print(product)
    return render(request, 'shop/prodView.html',{'product':product[0]})
def checkout(request):
    return render(request, 'shop/checkout.html')
