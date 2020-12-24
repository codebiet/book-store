from django.shortcuts import render,HttpResponse, redirect
from django.contrib import messages
from .models import Book, Order, OrderUpdate
from math import ceil
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def index(request):
    context={
        'variable':"this is sent"
    }
    
    allBooks = []
    catbooks = Book.objects.values('category', 'id')
    cats = {item['category'] for item in catbooks}
    for cat in cats:
        book = Book.objects.filter(category=cat)
        n = len(book)
        nSlides = n//4 + ceil((n/4)-(n//4))
        allBooks.append([book, range(1, nSlides), nSlides])
    params = {'allBooks': allBooks}
    return render(request,'index.html',params)

def about(request):
    return render(request,'about.html')

def bestseller(request):
    return render(request,'bestseller.html')

def contacts(request):
    return render(request,'contact.html')

def tracker(request):
    return render(request,'tracker.html')


def bookView(request, myid):
    book = Book.objects.filter(id=myid)
    return render(request,'bookView.html', {'book':book[0]})

def checkout(request):
    if request.method == "POST":
        # Get the post parameters
        items_json = request.POST.get('itemsjson','')
        name = request.POST.get('name','')
        email = request.POST.get('email','')
        address = request.POST.get('address1','') + "" + request.POST.get('address2','')
        city = request.POST.get('city','')
        state = request.POST.get('state','')
        zip_code = request.POST.get('zip_code','')
        phone = request.POST.get('phone','')

        order = Order(items_json='items_json', name='name', email='email', address='address', city='city', state='state', zip_code='zip_code', phone='phone')
        order.save()
        update = OrderUpdate(order_id=order.order_id, update_desc="The order has been placed")
        update.save()
        thank = True
        id = order.order_id
        return render(request,'checkout.html', {'thank' : thank, 'id':id})
    return render(request,'checkout.html')

def me(request):
    return HttpResponse("i am very good person")

def handleSignup(request):
    if request.method == 'POST':
        # Get the post parameters
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        mobile = request.POST['mobile']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        #Create for errorneous inputs
        if len(username) > 10:
            messages.error(request, "Username must be under 10 characters")
            return redirect('home')

        if not username.isalnum():
            messages.error(request, "Username should only contain letters and numbers")
            return redirect('home')    

        if pass1 != pass2:
            messages.error(request, "Password do not ,match")
            return redirect('home')

        #Create the user 
        myuser = User.objects.create_user(username, email, pass1)
        myuser.mobile_number = mobile
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        messages.success(request, "Your account has been successfully created")
        return redirect('home')

    else:
        return HttpResponse('404 . Not Found')

def handleLogin(request):
    if request.method == 'POST':
        # Get the post parameters
        loginusername = request.POST['loginusername']
        loginpassword = request.POST['loginpassword']

        user = authenticate(username=loginusername, password=loginpassword)

        if user is not None:
            login(request, user)
            messages.success(request,"Successfully Logged In")
            return redirect('home')
        else:
            messages.error(request,"Invalid Credentials, Please try again")
            return redirect('home')

    return HttpResponse('404 - Not found')

def handleLogout(request):
    logout(request)
    messages.success(request,"Successfully Logged out")
    return redirect('home')

    