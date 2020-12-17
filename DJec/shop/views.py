from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Product, Contact, Order, OrderUpdate
from django.db.models import Q, Min , Max
from math import ceil
import json
from django.views.decorators.csrf import csrf_exempt
from .PayTm import Checksum
import requests

# Create your views here.
MERCHANT_KEY = 'bKMfNxPPf_QdZppa';
with open('shopjson.json') as shop_json_data:
    shopdata = json.load(shop_json_data)['shopdata']

def index(request):
    # products = Product.objects.all()
    # print(shopdata)
    # n = len(products)
    # nSlide = n//4 + ceil((n/4)-(n//4))

    allprods = []
    subcategoryprod = Product.objects.values('subcategory','id')
    subcategoies = {item['subcategory'] for item in subcategoryprod}
    for subcats in subcategoies:
        prod = Product.objects.filter(subcategory=subcats)
        n = len(prod)
        nSlides = n//4 + ceil((n/4)-(n//4))
        allprods.append([prod,range(1,nSlides),nSlides])
    
    
    #params = {'no_of_slides':nSlide, 'product': products,'range':range(1,nSlide)}
    #allprods = [[products, range(1, nSlide), nSlide],
     #           [products, range(1, nSlide), nSlide]]
    params = {'allProds':allprods, 'shopdata':shopdata}
    return render(request,'shop/index.html',params)

def searchMatch(search,item):
    if search.lower() in item.product_name.lower() or search.lower() in item.desc.lower() or search.lower() in item.subcategory.lower():
        print(item.product_name)
        return True
    else:
        return False

def search(request):
        search = request.GET.get('search')
        price1 = request.GET.get('price1')
        price2 = request.GET.get('price2')

        allprods = []
        subcategoryprod=''
        #subcategoryprod = Product.objects.filter(Q(price__range=(price1,price2))|Q(product_name__icontains=search)|Q(desc__contains=search))
        if price1!='' and price2!='':
            subcategoryprod = Product.objects.filter(Q(price__range=(price1,price2))&Q(Q(desc__contains=search)|Q(product_name__icontains=search)))
        #subcategoryprod=Product.objects.annotate(search=SearchVector('product_name', 'subcategory'),).filter(search=search)
        print(subcategoryprod)
        #subcategoies = {item['subcategory'] for item in subcategoryprod}
        '''for subcats in subcategoies:
            prodtemp = Product.objects.filter(subcategory=subcats)
            prod = [item for item in prodtemp if searchMatch(search,item)]
            n = len(prod)
            nSlides = n//4 + ceil((n/4)-(n//4))
            if len(prod)!=0:
                allprods.append([prod,range(1,nSlides),nSlides])
        params = {'allProds':allprods, 'shopdata':shopdata}'''
        params = {'allProds':subcategoryprod}
        if len(subcategoryprod) == 0:
            params = {'msg':'OOPS!! Search Product Not Found'}
        return render(request,'shop/search.html',params)


def about(request):
    return render(request,'shop/about.html')
    #return HttpResponse("About Page")

def contact(request):
    if request.method=="POST":
        #print(request)
        name = request.POST.get('name') 
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        print(name,email,phone,desc)
        contact = Contact(name=name,email=email,phone=phone,desc=desc)
        contact.save()
    return render(request,'shop/contact.html')

def tracker(request):
    if request.method=="POST":
        orderno = request.POST.get('orderno')
        email = request.POST.get('email')
        try:
            order = Order.objects.filter(order_id=orderno,email=email)
            if len(order)>0:
                update = OrderUpdate.objects.filter(order_id=orderno)
                updates = []
                for item in update:
                    updates.append({'text':item.update_desc,'time':item.timestamp})
                    response = json.dumps({"status":"success","updates":updates,"itemsJson":order[0].items_json}, default=str)
                return HttpResponse(response)
            else:
                return HttpResponse('{"status":"no item"}')
        except Exception as e:
            return HttpResponse('{"status":"error"}')
    return render(request,'shop/tracker.html')

def productview(request,myid):
    myproducts_list = Product.objects.filter(id=myid)
    myproducts= {"myproducts":myproducts_list}
    return render(request,'shop/productview.html',myproducts)

def checkout(request):
    if request.method=='POST':
        items = request.POST.get('itemsJson')
        amount = request.POST.get('amount')
        name = request.POST.get('csname')
        email = request.POST.get('email')
        address1 = request.POST.get('address1')
        address2 = request.POST.get('address2')
        ph_no = request.POST.get('phno')
        city = request.POST.get('city')
        state = request.POST.get('state')
        zipcode=request.POST.get('zipcode')
        address = str(address1+' ')+str(address2)
        order = Order(items_json=items,amount=amount,name=name,email=email,address=address,phone=ph_no,city=city,state=state,zip_code=zipcode)
        order.save()
        update = OrderUpdate(order_id=order.order_id, update_desc="The Order Has Been Placed")
        update.save()
        thanks = True
        ids=order.order_id
        #return render(request,'shop/checkout.html',{'thanks':thanks, 'id':ids})
        data_dict = {
            'MID':'DIY12386817555501617',
            'ORDER_ID':str(ids),
            'TXN_AMOUNT':str(amount),
            'CUST_ID':email,
            'INDUSTRY_TYPE_ID':'Retail',
            'WEBSITE':'WEBSTAGING',
            'CHANNEL_ID':'WEB',
            'CALLBACK_URL':'http://127.0.0.1:8000/shop/handlerequest/',
        }
        param_dict = data_dict
        param_dict['CHECKSUMHASH'] =Checksum.generate_checksum(data_dict, MERCHANT_KEY)
        params = {'param_dict':param_dict}
        return render(request,'shop/paytm.html',params)
    return render(request,'shop/checkout.html')

@csrf_exempt
def handlerequest(request):
    form = request.POST
    response_dict = {}
    for i in form.keys():
        response_dict[i] = form[i]
        if i == 'CHECKSUMHASH':
            checksum = form[i]
    verify = Checksum.verify_checksum(response_dict, MERCHANT_KEY, checksum)
    print(verify)
    if verify:
        if response_dict['RESPCODE'] == '01':
            print('order successful')
        else:
            print('order unsuccessful'+response_dict['RESPMSG'])
    return render(request,'shop/paymentstatus.html',{'response':response_dict})

def login(request):
    return render(request,'shop/login.html')

'''from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    params ={'name':'ullash vaghela'}
    return render(request,"index.html",params)
    '''

def stx(request):
    url = requests.get('https://api.stackexchange.com/2.2/questions?order=desc&sort=activity&site=stackoverflow').text
    js_data_load = json.loads(url)
    params={'data':js_data_load}
    return render(request,'shop/stx.html',params)