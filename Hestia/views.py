from django.shortcuts import render, redirect
from django.contrib.auth import  logout, authenticate
from django.contrib.auth import login as auth_login
from .models import *
from django.contrib.auth.models import User
from django.contrib import messages
import logging
from django.views import generic
# Create your views here.

from django.contrib.auth.decorators import login_required

logger = logging.getLogger(__name__)

def index(request):
    return render(request,'Hestia/landing.html')

def open_listings(request):
    return render(request,'Hestia/listings.html')

def open_sublet_form(request):
    if request.user.is_authenticated:
        return render(request,'Hestia/list.html')
    else:
        return render(request,'Hestia/signin.html')

def about_us(request):
    return render(request,'Hestia/about.html')

def login(request):
    return render(request,'Hestia/signin.html')

def dashboard(request):
    return render(request,'Hestia/yourListing.html')

def sign_up(request):
    return render(request,'Hestia/signup.html')

def profile(request):
    return render(request,'Hestia/profile.html')

def settings(request):
    return render(request,'Hestia/settings.html')

def contact(request):
    return render(request,'Hestia/contact.html')

def terms(request):
    return render(request,'Hestia/termsandconditions.html')

def delete(request):
    return render(request,'Hestia/delete.html')

def yourListings(request):
    context = {}
    if request.method == 'GET':
        current_user = Client.objects.get(user=request.user)
        properties = Property.objects.filter(client = current_user)
        context['properties'] = properties
        context['is_empty'] = not properties.exists()
        return render(request, 'Hestia/yourListing.html', context)
    
def yourCart(request):
    context = {}
    if request.method == 'GET':
        current_user = Client.objects.get(user=request.user)
        properties = Cart.objects.filter(user = current_user)
        context['properties'] = properties
        context['is_empty'] = not properties.exists()
        return render(request, 'Hestia/Cart.html', context)


def login_request(request):
    context = {}
    # Handles POST request
    if request.method == "POST":
        # Get username and password from request.POST dictionary
        username = request.POST['username']
        password = request.POST['psw']
        # Try to check if provide credential can be authenticated
        user = authenticate(username=username, password=password)
        if user is not None:
            # If user is valid, call login method to login current user
            auth_login(request, user)
            return redirect('Hestia:index')
        else:
            # If not, return to login page again
            return render(request, 'Hestia/signin.html', context)
    else:
        return render(request, 'Hestia/sigin.html', context)

#Logut
def logout_request(request):
    logout(request)
    return redirect("Hestia:index")
    
def register_request(request):
    context = {}
    if request.method == 'GET':
        return render(request,'Hestia/signin.html')
    elif request.method == 'POST':
        username = request.POST['username']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        uniemail = request.POST['uniemail']
        university = request.POST['institute']
        phonenumber = request.POST['phonenumber']
        password = request.POST['psw']
        already_exists = False
        try:
            User.objects.get(username=username)
            already_exists = True
        except:
             logger.debug("{} is new user".format(username))
        
        if not already_exists:
            user = User.objects.create_user(username=username,first_name=firstname,
                                            last_name=lastname,email=email, password=password)
            
            newuser = Client(user=user,email=email,uni_email=uniemail,university=university,
                             phone_number=phonenumber)
            newuser.save()
            auth_login(request, user)
            return redirect('Hestia:dashboard')
        else:
            return render(request, 'Hestia/signin.html', context) 

def sublet_request(request):
    curr = request.user
    if request.method == 'POST':
        street1 = request.POST['street1']
        street2 = request.POST['street2']
        zip = request.POST['zip']
        province = request.POST['province']
        city = request.POST['city']
        university = request.POST['university']
        apartment = request.POST['apartment']
        rooms = request.POST['rooms']
        price = request.POST['price']
        start = request.POST['start']
        duration = request.POST['duration']
        description = request.POST['description']
        current_user = Client.objects.get(user=curr)
        cover_image = request.FILES.getlist('cover_image')
        images = request.FILES.getlist('images')
        furnished = request.POST['furnished']
        bathrooms = request.POST['bathrooms']
        new_property = Property(street1=street1, street2=street2,
                                zip_code=zip, province=province, city=city,apartment=apartment,
                                university=university,rooms=rooms,price=price,
                                date=start,duration=duration,client=current_user, 
                                description=description, cover_image = cover_image[0],bathrooms = bathrooms, furnished = furnished,)
        image_list = [new_property.image_01,new_property.image_02,new_property.image_03,new_property.image_04,new_property.image_05]
            
        i=0
        for image in images:
           image_list[i] = image
           i+=1 
            
            
        new_property.save()

        return render(request,'Hestia/dashboard.html')
    else:
        return render(request,'Hestia/list.html')

#ListView

def HestListView(request):
    context = {}
    if request.method == 'GET':
        properties = Property.objects.all()
        context['properties'] = properties
        context['is_empty'] = not properties.exists()
        return render(request, 'Hestia/listings.html', context)
    

def remove_prop(request, prop_id):
    prop = Property.objects.get(prop_id=prop_id)
    prop.delete()
    return render(request,'Hestia/yourListing.html')

def remove_item(request, item_id):
    prop = Cart.objects.get(item_id=item_id)
    prop.delete()
    return render(request,'Hestia/Cart.html')

@login_required
def delete_account(request):
    current_user = request.user
    if request.method == 'POST':
        current_user.delete()
        logout(request)
        return render(request,'Hestia/landing.html')
    else:
        return render(request,'Hestia/delete.html')
    
def detailView(request, prop_id):
    context = {}
    prop = Property.objects.get(prop_id=prop_id)
    context['prop'] = prop
    return render(request, 'Hestia/individualListing.html', context)

def add_to_Cart(request, prop_id):
    curr = request.user
    if request.user.is_authenticated:
        new_user = Client.objects.get(user=curr)
        prop = Property.objects.get(prop_id=prop_id)
        Cart.objects.get_or_create(user=new_user, property=prop)
        return detailView(request, prop_id)
    else:
        return render(request, 'Hestia/signin.html')

def Filter(request):
    context = {}
    if request.method == 'POST':
        properties = Property.objects.all()
        city = request.POST['city']
        minprice = request.POST['min-price']
        maxprice = request.POST['max-price']
        rooms = request.POST['rooms']
        try:
            minprice = float(minprice)
        except ValueError:
            minprice = 0

        try:
            maxprice = float(maxprice)
        except ValueError:
            maxprice = 1000000

        try:
            rooms = int(rooms)
        except ValueError:
            rooms = 1
        if minprice:
            properties = properties.filter(price__gte=minprice)
    
        if maxprice:
            properties = properties.filter(price__lte=maxprice)
    
        if city:
            properties = properties.filter(city__icontains=city)
    
        if rooms: 
            properties = properties.filter(rooms__gte=rooms)
        context['properties'] = properties
        
    return render(request, 'Hestia/listings.html', context)

