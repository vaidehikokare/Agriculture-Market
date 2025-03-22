from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import render
from .models import Crop , Seeds ,Fer , sell_register , Buy_register ,Order
from django.urls import reverse
from django.conf import settings
from django.shortcuts import render, get_object_or_404 
# from .forms import CropForm
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages 
from django.shortcuts import render, redirect 
from django.http import JsonResponse
def home(request):
    return render(request, 'home.html')
# Create your views here.
def sell(request):
    return render(request, 'sell.html')

def insert(request,user_id):
    id=user_id
    user=sell_register.objects.get(id=id)
    if request.method == 'POST':
        crop_name = request.POST.get('crop_name')
        crop_type = request.POST.get('crop_type')
        quantity = request.POST.get('quantity')
        price = request.POST.get('price')
        contact_name = request.POST.get('contact_name')
        contact_email = request.POST.get('contact_email')
        contact_phone = request.POST.get('contact_phone')
        description = request.POST.get('description')
        photo = request.FILES.get('photo')  # Handle file uploads
        state = request.POST.get('state')
        district = request.POST.get('district')
        street_address = request.POST.get('street_address')

        # Create a new Crop instance
        crop_instance = Crop(
            crop_name=crop_name,
            crop_type=crop_type,
            quantity=quantity,
            price=price,
            contact_name=contact_name,
            contact_email=contact_email,
            contact_phone=contact_phone,
            photo=photo,
            description=description,
            state=state,
            district=district,
            street_address=street_address
        )
        crop_instance.save()

        return render(request, 'sell.html', {'user': user})


    return render(request, 'sell.html') 

def insert1(request):
    if request.method == 'POST':
        seedName = request.POST.get('seedName')
        seedType = request.POST.get('seedType')
        quantity = request.POST.get('quantity')
        price = request.POST.get('price')
        contactName = request.POST.get('contactName')
        contactEmail = request.POST.get('contactEmail')
        contactPhone = request.POST.get('contactPhone')
        description = request.POST.get('description')
        photo = request.FILES.get('photo')  # Handle file upload
        inputState = request.POST.get('inputState')
        inputDistrict = request.POST.get('inputDistrict')
        streetAddress = request.POST.get('streetAddress')

        # Create a new Seeds instance
        seeds_instance = Seeds(
            seedName=seedName,
            seedType=seedType,
            quantity=quantity,
            price=price,
            contactName=contactName,
            contactEmail=contactEmail,
            contactPhone=contactPhone,
            description=description,
            photo=photo,
            inputState=inputState,
            inputDistrict=inputDistrict,
            streetAddress=streetAddress
        )

        # Save the Seeds instance to the database
        seeds_instance.save()

        # Redirect after successful form submission
        return redirect('seeds')  # Replace 'seeds' with the appropriate URL name

    # If the request method is GET, render the insert seeds form
    return render(request, 'insert_seeds.html')

def seeds(request):
     return render(request, 'seeds.html')

def fer(request):
      return render(request, 'fer.html')

def insert2(request):
    if request.method == 'POST':
        fertilizerName= request.POST.get('fertilizerName')
        fertilizerType = request.POST.get('fertilizerType')
        quantity = request.POST.get('quantity')
        price = request.POST.get('price')
        contactName = request.POST.get('contactName')
        contactEmail = request.POST.get('contactEmail')
        contactPhone = request.POST.get('contactPhone')
        description = request.POST.get('description')
        photo = request.FILES.get('photo')  # Handle file uploads
        inputState = request.POST.get('inputState')
        inputDistrict = request.POST.get('inputDistrict')
        streetAddress = request.POST.get('streetAddress')

        # Create a new Crop instance
        crop_instance = Fer(
            fertilizerName=fertilizerName,
            fertilizerType=fertilizerType,
            quantity=quantity,
            price=price,
           contactName=contactName,
            contactEmail=contactEmail,
            contactPhone=contactPhone,
            photo=photo,
            description=description,
            inputState=inputState,
            inputDistrict=inputDistrict,
            streetAddress=streetAddress
        )
        crop_instance.save()

        return redirect('fer')  # Redirect after saving

    return render(request, 'fer.html')
from django.shortcuts import render
from .models import Crop

def buy(request):
     crops = Crop.objects.all()  # Fetch all records from the Crop table
     return render(request, 'buy.html', {'crops': crops})
def seeds_buy(request):
     crops = Seeds.objects.all()  # Fetch all records from the Crop table
     return render(request, 'Seeds_buy.html', {'crops': crops})

def crop_buy(request):
     crops = Crop.objects.all()  # Fetch all records from the Crop table
     return render(request, 'crop_buy.html', {'crops': crops})
def fer_buy(request):
     crops = Fer.objects.all()  # Fetch all records from the Crop table
     return render(request, 'fer_buy.html', {'crops': crops})
def search(request):
    search_query = request.GET.get('search', '')  # Retrieve the search query from the URL
    
    # Filter crops by name that start with the search query (case-insensitive)
    crops = Crop.objects.filter(crop_name__istartswith=search_query)
    
    # Render the template and pass the crops as context
    return render(request, 'crop_s.html', {'crops': crops, 'search_query': search_query})
def crop_detail(request, crop_id):
    crop = get_object_or_404(Crop, id=crop_id)
    return render(request, 'crop_detail.html', {'crop': crop})
def sell_login(request):
    return render(request, 'sell_login.html')
def sell_signup(request):
    return render(request, 'sell_signup.html')
def sell_register_view(request):
    if request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")

        print(f"Received Data - First Name: {first_name}, Last Name: {last_name}, Username: {username}, Email: {email}")

        if password != confirm_password:
            messages.error(request, "Passwords do not match!")
            return redirect("sell_signup")

        if sell_register.objects.filter(username=username).exists():
            messages.error(request, "Username already taken!")
            return redirect("sell_signup")

        if sell_register.objects.filter(email=email).exists():
            messages.error(request, "Email already registered!")
            return redirect("sell_signup")

        # Save user data to the custom model
        user = sell_register(
            first_name=first_name,
            last_name=last_name,
            username=username,
            email=email,
            password=make_password(password),  # Hash password before saving
        )
        user.save()

        print("User successfully saved to database.")

        messages.success(request, "Registration successful! Please login.")
        return redirect("sell_login")

    return render(request, "sell_signup.html")
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.hashers import check_password
from .models import sell_register  # Ensure you are importing the correct model

def sell_login1(request):
    if request.method == "POST":  # ✅ Fix request method check
        username = request.POST.get('username')
        password = request.POST.get('password')

    
        user = sell_register.objects.filter(username=username).first()

        if user is None:
            messages.error(request, "Username does not exist")
            return redirect('sell_login')

       
        if not check_password(password, user.password):
            messages.error(request, "Incorrect Password")
            return redirect('sell_login')
        messages.success(request, "Login Successful")
        return render(request, 'sell.html', {'user': user})


    return render(request, 'sell.html')  

def buy_login(request):
    return render(request, 'buy_login.html')
def buy_signup(request):
    return render(request, 'buy_signup.html')
def buy_register_view(request):
    if request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")

        print(f"Received Data - First Name: {first_name}, Last Name: {last_name}, Username: {username}, Email: {email}")

        if password != confirm_password:
            messages.error(request, "Passwords do not match!")
            return redirect("buy_signup")

        if Buy_register.objects.filter(username=username).exists():
            messages.error(request, "Username already taken!")
            return redirect("buy_signup")

        if Buy_register.objects.filter(email=email).exists():
            messages.error(request, "Email already registered!")
            return redirect("buy_signup")

        # Save user data to the custom model
        user =Buy_register(
            first_name=first_name,
            last_name=last_name,
            username=username,
            email=email,
            password=make_password(password),  # Hash password before saving
        )
        user.save()

        print("User successfully saved to database.")

        messages.success(request, "Registration successful! Please login.")
        return redirect("buy_login")

    return render(request, "buy_signup.html")

def buy_login1(request):
    if request.method == "POST":  # ✅ Fix request method check
        username = request.POST.get('username')
        password = request.POST.get('password')

    
        user = Buy_register.objects.filter(username=username).first()

        if user is None:
            messages.error(request, "Username does not exist")
            return redirect('buy_login')

       
        if not check_password(password, user.password):
            messages.error(request, "Incorrect Password")
            return redirect('buy_login')

        messages.success(request, "Login Successful")
        return redirect('buy')  

    return render(request, 'buy.html')  

def crop_display(request):
    email = request.GET.get('email')  
    crops = Crop.objects.filter(contact_email=email) 
    return render(request, 'crop_display.html', {'crops': crops}) 

def view_details_crop(request, crop_id):
    crop = get_object_or_404(Crop, id=crop_id)
    return render(request, 'view_details_crop.html', {'crop': crop})
def crop_delete(request, crop_id):
    crop=get_object_or_404(Crop, id=crop_id)
    email=crop.contact_email
    crop.delete()
    return redirect(f'/crop_display/?email={email}')

def buy_product(request ,crop_id):
    crop = get_object_or_404(Crop, id=crop_id)  
    return render(request, 'buy_product.html', {'crop': crop}) 


def confirm_order(request, crop_id):
    crop = get_object_or_404(Crop, id=crop_id)  

    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        quantity = request.POST.get("quantity")

        # Save order in the database with product details
        Order.objects.create(
            product_type="crop",  
            product_id=crop.id,  
            product_name=crop.crop_name,  
            buyer_name=name,
            buyer_email=email,
            buyer_phone=phone,
            quantity=quantity
        )

        messages.success(request, f"Your order for {crop.crop_name} has been confirmed!")
        return redirect("confirm_order", crop_id=crop_id)

    return render(request, "buy_product.html", {"crop": crop})  # Corrected dictionary key

def orders(request):
    email = request.GET.get('email')  
    order = Order.objects.filter(buyer_email =email) 
    return render(request, "order.html", {"order": order})
def order_action(request, order_id, action):
    order = get_object_or_404(Order, id=order_id)

    if action == "accept":
        order.status = "Accepted"
    elif action == "reject":
        order.status = "Rejected"
    else:
        return JsonResponse({"status": "error", "message": "Invalid action"})

    order.save()
    return HttpResponse({"status": "success", "message": f"Order {action}ed successfully!"})

def accept_order(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    order.delete()
    return HttpResponse({"message: Order accepted successfully."})

def reject_order(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    order.delete()
    return HttpResponse({"message : Order rejected successfully."})