from django.shortcuts import render , redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.contrib.auth import authenticate,login
from .models import Manager, Product,Category,PriceRange, ProductReview,Agents
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

def AgentRegister(request):
    if request.method == 'POST':
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        whatsapp = request.POST.get('whatsapp')
        phone = request.POST.get('whatsapp')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        con_password = request.POST.get('con_password')

        user = User.objects.filter(username = username, email = email)

        if user.exists():
            messages.info(request, "Username or email is taken")
            return redirect('/AgentRegister')
        
        if password==con_password:
            user = User.objects.create_user(email=email,username=username,is_staff=True)
            user.set_password(password)
            user.is_staff = True
            user.save()
            agent = Agents.objects.create(user=user,is_staff=True,firstname =firstname,lastname=lastname,whatsapp=whatsapp,phone=phone)
            return redirect('/log_in')
        else:
            messages.info(request, "Password doesn't match")
            return redirect("/AgentRegister")
    return render(request, 'AgentSignUp.html')


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
            messages.error(request, 'Invalid credentials')
            return redirect('/log_in')

        login(request, user)

  
        if user.is_staff:  
            return redirect('/agent_dashboard')
        else:
            return redirect('/home')

    return render(request, 'loginPage.html')



def home(request): 
    products = Product.objects.order_by('-created_at')
    context = {'products': products}
    return render(request,'homePage.html', context)

def agent_dashboard(request):
    return render(request,'agent_dashboard.html')

def loginToSignUp(request):
    return render(request,'signUp.html')


def signUpTologin(request):
    return render(request,'loginPage.html')

def toAgentSignUp(request):
    return render(request,'AgentSignUp.html')

def productDetails(request, pk):
    products  = Product.objects.get(id=pk)
    rooms1 = products.rooms.all()
    amenities = products.amenities.all()

    if request.method == 'POST' and request.user.is_authenticated:
        stars = request.POST.get('rate')
        content = request.POST.get('content')

        review = ProductReview.objects.create(products=products,user=request.user,stars =stars,content=content)
        return redirect('productDetails', pk=pk)

    
    context = {'products': products, 'rooms1':rooms1, 'amenities':amenities}
    return render(request, 'details.html', context)




def search(request):
    query = request.GET.get('q')  
    products  = Product.objects.all()
    results = Product.objects.filter(Q(name__icontains = query)|Q(description__icontains = query)|Q(rate__icontains = query)|Q(price__icontains = query)|Q(vicinity__icontains = query)) 
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
    
    