from django.shortcuts import render, redirect

from django.contrib.auth.models import User
from .models import myUser
from django.contrib.auth import authenticate, login, logout

from django.contrib import messages
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from . models import products, Cart, CartItem



# Create your views here.

def home(request):
    new_products = products.objects.filter(launch='new')
    categories = products.objects.values('category').distinct()
    brands = products.objects.values('brand').distinct()

    total_quantity = 0
    if request.user.is_authenticated:
        user_cart, created = Cart.objects.get_or_create(user=request.user)
        cart_items = user_cart.items.all()
        total_quantity = sum(item.quantity for item in cart_items)


    return render(request, 'index.html', {'new_products': new_products, 'total_quantity':total_quantity, 'categories': categories, 'brands':brands})




def product_detail(request, pk):
    product = get_object_or_404(products, pk=pk)
    categories = products.objects.values('category').distinct()
    brands = products.objects.values('brand').distinct()

    total_quantity = 0
    if request.user.is_authenticated:
        user_cart, created = Cart.objects.get_or_create(user=request.user)
        cart_items = user_cart.items.all()
        total_quantity = sum(item.quantity for item in cart_items)

    if request.method == 'POST':
        if not request.user.is_authenticated:
            messages.info(request, "Please log in to add items to your cart.")
            return redirect('login')
        user_cart, created = Cart.objects.get_or_create(user=request.user)

        # Check if the product is already in the cart
        cart_item, item_created = CartItem.objects.get_or_create(
            user=request.user,
            product=product
        )

        if not item_created:
            cart_item.quantity += 1
            cart_item.save()

        user_cart.items.add(cart_item)
        messages.success(request, f"{product.name} has been added to your cart.")

    context = {
        'product': product,
        'total_quantity':total_quantity,
        'categories': categories,
        'brands':brands
    }
    return render(request, 'product_detail.html', context)

def user_signup(request):
    categories = products.objects.values('category').distinct()
    brands = products.objects.values('brand').distinct()

    total_quantity = 0
    if request.user.is_authenticated:
        user_cart, created = Cart.objects.get_or_create(user=request.user)
        cart_items = user_cart.items.all()
        total_quantity = sum(item.quantity for item in cart_items)


    if request.method == 'POST':
        ufirstname = request.POST['firstname']
        ulastname = request.POST['lastname']
        uemail = request.POST['email']
        unumber = request.POST['number']
        upassword_1 = request.POST['pswd1']
        upassword_2 = request.POST['pswd2']



        if upassword_1 == upassword_2:
            if User.objects.filter(email=uemail).exists():
                messages.info(request, "Email Already Exists")
                return redirect('signup')
            elif myUser.objects.filter(number=unumber).exists():
                messages.info(request, "Mobile number alredy exists")
                return redirect('signup')
            else:
                user = User.objects.create_user(username=uemail, email=uemail, password=upassword_1, first_name = ufirstname, last_name= ulastname)
                my_user = myUser.objects.create(user=user, number = unumber)
                user.save()
                my_user.save()
                messages.info(request, "User Created")
                return redirect('login')
        else:
            messages.info(request, "Passwords do not match")
            return redirect('signup')
    return render(request, "signup.html",{'total_quantity':total_quantity, 'categories': categories, 'brands':brands})

@login_required
def view_cart(request):
    categories = products.objects.values('category').distinct()
    brands = products.objects.values('brand').distinct()

    total_quantity = 0
    if request.user.is_authenticated:
        user_cart, created = Cart.objects.get_or_create(user=request.user)
        cart_items = user_cart.items.all()
        total_quantity = sum(item.quantity for item in cart_items)

   
    user_cart, created = Cart.objects.get_or_create(user=request.user)
    cart_items = user_cart.items.all()
    

    if request.method == 'POST':
        product_id = request.POST.get('product_id')
        cart_item = get_object_or_404(CartItem, id=product_id, user=request.user)

        if request.POST.get('action') == 'remove':
            cart_item.delete()
            messages.success(request, f"{cart_item.product.name} has been removed from your cart.")
        elif request.POST.get('action') == 'decrease':
            if cart_item.quantity > 1:
                cart_item.quantity -= 1
                cart_item.save()
                messages.success(request, f"{cart_item.product.name} quantity decreased.")
            else:
                cart_item.delete()
                messages.success(request, f"{cart_item.product.name} has been removed from your cart.")
        elif request.POST.get('action') == 'increase':
            cart_item.quantity += 1
            cart_item.save()
            messages.success(request, f"{cart_item.product.name} quantity increased.")

        return redirect('view_cart')

    total_price = sum(item.product.price * item.quantity for item in cart_items)
    
    context = {
        'cart_items': cart_items,
        'total_price': total_price,
        'total_quantity':total_quantity,
        'categories': categories,
        'brands':brands
         
    }

    return render(request, 'cart.html', context)


   
def user_login(request):
    categories = products.objects.values('category').distinct()
    brands = products.objects.values('brand').distinct()

    total_quantity = 0
    if request.user.is_authenticated:
        user_cart, created = Cart.objects.get_or_create(user=request.user)
        cart_items = user_cart.items.all()
        total_quantity = sum(item.quantity for item in cart_items)
    


    if request.method == "POST":

        name = request.POST['login_email']
        password = request.POST['loginpswd']


        user = authenticate(request, username = name, password = password)
        if user is not None:
            login(request, user)
            full_name = f"{user.first_name} {user.last_name}" if user.first_name and user.last_name else user.username
            messages.info(request, f"You are logged in as {full_name}.")
            return redirect("/")
        else:
            messages.info(request, "User Not Found")
            
            return redirect('login')
    else:
        
        return render(request, "login.html",{'total_quantity':total_quantity, 'categories': categories, 'brands':brands} )
    
def user_logout(request):
    logout(request)
    return redirect('/')

def custom_404(request, exception):
    return render(request, '404.html', status=404)

# views.py



def product_list(request, filter_type, filter_value):
    categories = products.objects.values('category').distinct()
    brands = products.objects.values('brand').distinct()

    total_quantity = 0
    if request.user.is_authenticated:
        user_cart, created = Cart.objects.get_or_create(user=request.user)
        cart_items = user_cart.items.all()
        total_quantity = sum(item.quantity for item in cart_items)
    
    brand_image_url = None  # Initialize the variable outside the conditional block

    if filter_type == 'category':
        filtered_products = products.objects.filter(category=filter_value)
    elif filter_type == 'brand':
        filtered_products = products.objects.filter(brand=filter_value)
        # Get the brand image URL only if there are filtered products
        brand_image_url = products.objects.filter(brand=filter_value).first().brand_image.url if filtered_products else None
    elif filter_type == 'price':
        # Assuming price is stored as a field in your Product model
        price_range = filter_value.split('-')
        min_price, max_price = int(price_range[0]), int(price_range[1])
        filtered_products = products.objects.filter(price__range=(min_price, max_price))
    else:
        # Handle other filter types or provide a default case
        filtered_products = []

    context = {'filtered_products': filtered_products,
                'brand_image_url': brand_image_url,
                'total_quantity':total_quantity,
               'categories': categories,
                'brands':brands

                }
    return render(request, 'product_list.html', context)

def order(request):
    return render(request, "order.html")