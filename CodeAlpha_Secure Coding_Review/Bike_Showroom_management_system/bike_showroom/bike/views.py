
"""from django.shortcuts import render
from .models import Bike

def home(request):
    bikes = Bike.objects.all()  # Fetch all bikes from DB
    context = {
        'bikes': bikes
    }
    return render(request,   'home.html', context)"""
"""

# bike/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Bike
from django.contrib.auth.decorators import login_required

# ----- Public Views -----

def index(request):
    return render(request, 'bike/index.html')

def showroom(request):
    # list all bikes to users
    bikes = Bike.objects.all()
    return render(request, 'bike/showroom.html', {'bikes': bikes})

def bikedetails(request, id):
    bike = get_object_or_404(Bike, id=id)
    return render(request, 'bike/bikedetails.html', {'bike': bike})

# ----- Admin CRUD Views -----

@login_required
def bike_form(request):
    # show a blank form to add a bike
    return render(request, 'bike/bikeform.html')

@login_required
def insert_bike(request):
    if request.method == 'POST':
        b = Bike(
            name=request.POST['name'],
            brand=request.POST['brand'],
            price=request.POST['price'],
            description=request.POST['description'],
            image=request.FILES['image']
        )
        b.save()
        return redirect('show_bikes')
    return redirect('bike_form')

@login_required
def show_bikes(request):
    bikes = Bike.objects.all()
    return render(request, 'bike/showbikes.html', {'bikes': bikes})

@login_required
def delete_bike(request, id):
    bike = get_object_or_404(Bike, id=id)
    bike.delete()
    return redirect('show_bikes')

@login_required
def update_bike(request, id):
    bike = get_object_or_404(Bike, id=id)
    if request.method == 'POST':
        bike.name        = request.POST['name']
        bike.brand       = request.POST['brand']
        bike.price       = request.POST['price']
        bike.description = request.POST['description']
        if 'image' in request.FILES:
            bike.image = request.FILES['image']
        bike.save()
        return redirect('show_bikes')
    return render(request, 'bike/updatebike.html', {'bike': bike})
"""
# bike/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout

from django.contrib import messages
from django.urls import reverse
from .models import Bike, Booking, ContactMessage, AdminProfile
from django.contrib.auth.models import User
from .forms import BookingForm, ContactForm, AdminSignupForm, BikeForm  # we'll define these later

# ─── Public Pages ──────────────────────────────────────────────────────────

def home(request):
    """Show all bikes on homepage."""
    bikes = Bike.objects.all()
    return render(request, 'home.html', {'bikes': bikes})

def about(request):
    return render(request, 'about.html')

def services(request):
    return render(request, 'services.html')

def contact(request):
    """Display & process the contact form."""
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()  # saves ContactMessage
            messages.success(request, "Message sent!")
            return redirect('contact')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})

def book(request):
    """Display & handle booking form."""
    if not request.user.is_authenticated:
        messages.error(request, "Please log in to book a bike.")
        return redirect('login')
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.save()
            messages.success(request, "Bike booked successfully!")
            return redirect('book')
    else:
        form = BookingForm()
    return render(request, 'book.html', {'form': form})

# ─── Authentication ────────────────────────────────────────────────────────

# views.py

"""def register(request):
    if request.method == 'POST':
        form = AdminSignupForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Registration successful. Please log in.")
            return redirect('login')
    else:
        form = AdminSignupForm()
    return render(request, 'login.html', {'form': form})  # Same file"""
def register(request):
    if request.method == 'POST':
        name = request.POST.get('fullname')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if password1 != password2:
            messages.error(request, "Passwords do not match.")
            return redirect('login')

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already registered.")
            return redirect('login')

        username = email.split('@')[0]  # make username from email
        user = User.objects.create_user(
            username=username,
            email=email,
            password=password1,
        )
        user.first_name = name
        user.save()

        messages.success(request, "Registered successfully. Please log in.")
        return redirect('login')

    return render(request, 'login.html')


"""def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('profile')
        messages.error(request, "Invalid credentials.")
        return redirect('login')
    return render(request, 'login.html')  # Same file"""

def user_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            messages.error(request, "Email not registered.")
            return redirect('login')

        user = authenticate(request, username=user.username, password=password)
        if user:
            login(request, user)
            return redirect('profile')
        else:
            messages.error(request, "Invalid password.")
            return redirect('login')

    return render(request, 'login.html')

def user_logout(request):
    logout(request)
    return redirect('home')

def profile(request):
    if not request.user.is_authenticated:
        return redirect('login')
    return render(request, 'profile.html')

# ─── Admin Panel Views ────────────────────────────────────────────────────

def admin_dashboard(request):
    """Very basic analytics."""
    if not request.user.is_staff:
        return redirect('admin_login')
    total_bikes    = Bike.objects.count()
    total_bookings = Booking.objects.count()
    total_users    = User.objects.count()
    return render(request, 'bike/admin/dashboard.html', {
        'total_bikes': total_bikes,
        'total_bookings': total_bookings,
        'total_users': total_users,
    })
def admin_login(request):
    """Separate admin login (could reuse user_login with staff check)."""
    if request.method == 'POST':
        u = request.POST['username']
        p = request.POST['password']
        user = authenticate(request, username=u, password=p)
        if user and user.is_staff:
            login(request, user)
            return redirect('admin_dashboard')
        messages.error(request, "Invalid admin credentials.")
    return render(request, 'bike/admin/login.html')

def admin_logout(request):
    logout(request)
    return redirect('admin_login')

# ─── Bike CRUD for Admin ──────────────────────────────────────────────────

def bike_create(request):
    if not request.user.is_staff:
        return redirect('admin_login')
    if request.method == 'POST':
        form = BikeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('bike_list')
    else:
        form = BikeForm()
    return render(request, 'bike/admin/bike_form.html', {'form': form})

def bike_list(request):
    if not request.user.is_staff:
        return redirect('admin_login')
    bikes = Bike.objects.all()
    return render(request, 'bike/admin/bike_list.html', {'bikes': bikes})

def bike_update(request, pk):
    if not request.user.is_staff:
        return redirect('admin_login')
    bike = get_object_or_404(Bike, pk=pk)
    if request.method == 'POST':
        form = BikeForm(request.POST, request.FILES, instance=bike)
        if form.is_valid():
            form.save()
            return redirect('bike_list')
    else:
        form = BikeForm(instance=bike)
    return render(request, 'bike/admin/bike_form.html', {'form': form, 'bike': bike})

def bike_delete(request, pk):
    if not request.user.is_staff:
        return redirect('admin_login')
    bike = get_object_or_404(Bike, pk=pk)
    if request.method == 'POST':
        bike.delete()
        return redirect('bike_list')
    return render(request, 'bike/admin/bike_confirm_delete.html', {'bike': bike})
