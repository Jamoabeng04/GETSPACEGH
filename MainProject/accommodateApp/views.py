from django.shortcuts import render , redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.contrib.auth import authenticate,login
from .models import Manager, Product,Category,PriceRange, ProductReview
from django.db.models import Q

# Create your views here.
def register(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        con_password = request.POST.get('con_password')

        user = User.objects.filter(username = username, email = email)

        if user.exists():
            messages.info(request, "Username or email is taken")
            return redirect('/register')
        
        if password==con_password:
            user = User.objects.create_user(first_name=first_name,last_name=last_name,email=email,username=username)
            user.set_password(password)
            user.save()
            return redirect('/log_in')
        else:
            messages.info(request, "Password doesn't match")
            return redirect("/register")
    return render(request, 'signUp.html')


def log_in(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not User.objects.filter(username=username,email=email).exists():
            messages.error(request, 'Invalid credentials')
            return redirect('/log_in') 
        
        user = authenticate(email=email,username=username,password=password)

        if user is None:
            messages.error(request,"please check your passwors")
            return redirect('/log_in')
        else:
            login(request,user)
            return redirect('/home')
    return render(request,'loginPage.html')



def home(request): 
    products = Product.objects.order_by('-created_at')
    context = {'products': products}
    return render(request,'homePage.html', context)


def loginToSignUp(request):
    return render(request,'signUp.html')


def signUpTologin(request):
    return render(request,'loginPage.html')


def productDetails(request, pk):
    products  = Product.objects.get(id=pk)
    rooms1 = products.rooms.all()
    amenities = products.amenities.all()

    if request.method == 'POST' and request.user.is_authenticated:
        stars = request.POST.get('rate')
        content = request.POST.get('content')

        review = ProductReview.objects.create(products=products,user=request.user,stars =stars,content=content)

    
    context = {'products': products, 'rooms1':rooms1, 'amenities':amenities}
    return render(request, 'details.html', context)




def search(request):
    query = request.GET.get('q')  
    products  = Product.objects.all()
    results = Product.objects.filter(Q(name__icontains = query)|Q(description__icontains = query)|Q(rate__icontains = query)|Q(price__icontains = query)) 
    context = {'results': results,'products': products, 'query':query}
    return render(request, 'searchResults.html',context)


def category(request, cid):
    try:
        category = Category.objects.get(name = cid)
        products = Product.objects.filter(category=category)
        context = {'products': products, 'category':category}
        return render(request, 'category.html',context)
    except:
        messages.success(request, "Oops that category does not exist yet")
        return redirect('/home')
    

def pricerange(request, prid): 
    try:
        pricerange = PriceRange.objects.get(name = prid)
        products = Product.objects.filter(pricerange=pricerange)
        context = {'products': products, 'pricerange':pricerange}
        return render(request, 'PriceRange.html',context)
    except:
        messages.success(request, "Oops that price range does not exist yet")
        return redirect('/home')
    
    