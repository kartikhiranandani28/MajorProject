from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import CollegeRegistrationForm, UserRegistrationForm, SignInForm
from .models import College
from django.contrib.auth.decorators import login_required 

# View to handle college registration
@login_required
def register_college(request):
    if request.method == 'POST':
        form = CollegeRegistrationForm(request.POST)
        if form.is_valid():
            college_name = form.cleaned_data['college_name']
            college_type = form.cleaned_data['college_type']
            contact_no = form.cleaned_data['contact_no']
            courses = [
                form.cleaned_data[f'course_{i}'] for i in range(1, 11)
            ]
            
            # Create and save the college instance
            College.objects.create(
                user=request.user,  # Associate the college with the logged-in user
                college_name=college_name,
                college_type=college_type,
                contact_no=contact_no,
                courses=courses
            )
            return HttpResponse(f"Registered College: {college_name}, Type: {college_type}, Contact: {contact_no}, Courses: {', '.join(courses)}")
    else:
        form = CollegeRegistrationForm()

    # Pass form and courses to template
    courses_fields = [form[f'course_{i}'] for i in range(1, 11)]
    return render(request, 'collegeapp/register.html', {'form': form, 'courses_fields': courses_fields})

# Sign-in view
def sign_in(request):
    if request.method == 'POST':
        form = SignInForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('register_college')  # Redirect after login
    else:
        form = SignInForm()
    
    return render(request, 'collegeapp/sign_in.html', {'form': form})

# User registration view
def register_user(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = User.objects.create_user(username=username, password=password)
            user.save()
            messages.success(request, 'User registered successfully.')
            return redirect('register_college')  # Redirect to college registration
    else:
        form = UserRegistrationForm()

    return render(request, 'collegeapp/register_user.html', {'form': form}) 