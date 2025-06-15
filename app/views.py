from django.shortcuts import render, redirect
from bs4 import BeautifulSoup
import requests
from django.core.mail import send_mail
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
    crops= Crop.objects.filter(contact_email=email)
    orders = Order.objects.filter(product_id__in=crops.values_list('id', flat=True))
    return render(request, "order.html", {"order": orders})
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
    buyer_email = order.buyer_email

    
    subject = "Order Confirmation - Your Order Has Been Accepted"
    message = f"""
    Dear {order.buyer_name},

    We are pleased to inform you that your order has been accepted. Thank you for choosing our platform for your purchase.

    Here are your order details:
    - Order ID: {order.id}
    - Product Name: {order.product_name}
    

    If you have any questions or need further assistance, feel free to contact our support team.

    Best regards,
    Your AgriTech
    9503101433
    """

    send_mail(
        subject=subject,
        message=message,
        from_email="kokarevaidehi2@gmail.com",
        recipient_list=[buyer_email],
        fail_silently=False,
    )
    order.delete()
    return HttpResponse({"message: Order accepted successfully."})

def reject_order(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    buyer_email = order.buyer_email
    print(buyer_email)
    order.delete()
    send_mail(
        subject="Order Rejected",
        message=f"Dear {order.buyer_name},\n\nUnfortunately, your order has been rejected. We apologize for any inconvenience.",
        from_email="kokarevaidehi2@gmail.com",
        recipient_list=[buyer_email],
        fail_silently=False,
    )
    return HttpResponse({"message : Order rejected successfully."})

def search_seeds(request):
    search_query = request.GET.get('search', '')  
    seeds = Seeds.objects.filter(seedName__istartswith=search_query)
    return render(request, 'seeds_s.html', {'seeds': seeds, 'search_query': search_query})


import requests
from datetime import datetime, timedelta
from bs4 import BeautifulSoup
import urllib.parse
from googlesearch import search

def get_city_agri_weather_news(city):
    query = f"{city} agriculture weather news"
    agri_news = []
    try:
        for url in search(query, num_results=5):
            try:
                res = requests.get(url, timeout=5)
                soup = BeautifulSoup(res.content, "html.parser")
                title = soup.title.string.strip() if soup.title else url
                agri_news.append({
                    "title": title,
                    "url": url
                })
            except:
                continue
    except Exception as e:
        agri_news.append({"title": f"Unable to fetch news: {str(e)}", "url": "#"})

    return agri_news

def agri_weather_view(request):
    weather_info = {}
    rain_spans = []
    agri_news = []

    if request.method == "POST":
        city = request.POST.get("city")

        # --- Weather Section ---
        try:
            geo_url = f"https://geocoding-api.open-meteo.com/v1/search?name={city}"
            geo_response = requests.get(geo_url, timeout=5).json()
            if "results" in geo_response and geo_response["results"]:
                lat = geo_response["results"][0]["latitude"]
                lon = geo_response["results"][0]["longitude"]

                weather_url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&hourly=precipitation_probability&current_weather=true&timezone=auto"
                weather_response = requests.get(weather_url, timeout=5).json()

                weather_info = {
                    "city": city.capitalize(),
                    "temperature": weather_response["current_weather"]["temperature"],
                    "windspeed": weather_response["current_weather"]["windspeed"],
                    "time": weather_response["current_weather"]["time"],
                }

                # Rain spans
                times = weather_response["hourly"]["time"]
                rains = weather_response["hourly"]["precipitation_probability"]
                rain_hours = [
                    datetime.fromisoformat(t) for t, r in zip(times, rains)
                    if datetime.fromisoformat(t).date() == datetime.now().date() and r >= 30
                ]
                if rain_hours:
                    start = rain_hours[0]
                    for i in range(1, len(rain_hours)):
                        if (rain_hours[i] - rain_hours[i - 1]) > timedelta(hours=1):
                            rain_spans.append((start.strftime('%I:%M %p'), rain_hours[i - 1].strftime('%I:%M %p')))
                            start = rain_hours[i]
                    rain_spans.append((start.strftime('%I:%M %p'), rain_hours[-1].strftime('%I:%M %p')))
            else:
                weather_info = {"error": "Could not find coordinates for the given city."}
        except Exception as e:
            weather_info = {"error": f"Error retrieving data: {e}"}

        # --- City Agriculture/Weather News ---
        agri_news = get_city_agri_weather_news(city)
       

    return render(request, "agri_weather.html", {
        "weather": weather_info,
        "rain_spans": rain_spans,
        "agri_news": agri_news,
    })
