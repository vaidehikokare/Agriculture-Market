from django.shortcuts import render
from .models import Crop , Seeds ,Fer
from django.urls import reverse
from django.conf import settings
from django.shortcuts import render, get_object_or_404 
# from .forms import CropForm
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages 
from django.shortcuts import render, redirect 
def home(request):
    return render(request, 'home.html')
# Create your views here.
def sell(request):
    return render(request, 'sell.html')

def insert(request):
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

        return render(request,'sell.html')  # Redirect after saving

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
