from django.shortcuts import render, redirect, get_object_or_404
from .models import Resolution, Progress, Recommendation
from .forms import ResolutionForm
from django.contrib.auth import login
from django.contrib.auth.models import User
from .forms import UserRegistrationForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.contrib import messages
from .forms import ProgressForm

def home(request):

    resolutions = Resolution.objects.filter(user=request.user)
    query = request.GET.get('query')
    if query:
        resolutions = resolutions.filter(title__icontains=query)
def SearchForm(request, resolutions):
    search_form = SearchForm()
    return render(request, 'resolutions/home.html', {'resolutions': resolutions, 'search_form': search_form})

def add_resolution(request):
    if request.method == 'POST':
        form = ResolutionForm(request.POST)
        if form.is_valid():
            resolution = form.save(commit=False)
            resolution.user = request.user
            resolution.save()
            return redirect('resolution_list')  
        form = ResolutionForm()
    return render(request, 'resolutions/add_resolution.html', {'form': form})

def recommend_resolutions(user):
    preferences = Resolution.objects.filter(user=user).values_list('title', flat=True)
    all_recommendations = [
        "Exercise regularly",
        "Read more books",
        "Learn a new skill",
        "Save more money",
        "Spend more time with family"
    ]
    recommended = [rec for rec in all_recommendations if rec not in preferences]
    return Resolution.objects.filter(user=user)



@login_required
def get_recommendations(request):
    recommendations = recommend_resolutions(request.user)
    return render(request, 'resolutions/recommendations.html', {'recommendations': recommendations})


def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            user = user_form.save()
            login(request, user)
            return redirect('home')
    else:
        user_form = UserRegistrationForm()
    return render(request, 'registration/register.html', {'user_form': user_form})

@login_required
def home(request):
    resolutions = Resolution.objects.filter(user=request.user)
    return render(request, 'resolutions/home.html', {'resolutions': resolutions})


@login_required
def add_resolution(request):
    print("Request Method:", request.method)
    if request.method == 'POST':
        form = ResolutionForm(request.POST)
        print("Form POST data:", form.data)
        if form.is_valid():
            print("Form is valid")
            resolution = form.save(commit=False)
            resolution.user = request.user
            resolution.save()
            messages.success(request, 'Resolution added successfully!')
            return redirect('home')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = ResolutionForm()
    return render(request, 'resolutions/add_resolution.html', {'form': form})

@login_required
def toggle_completed(request, resolution_id):
    resolution = Resolution.objects.get(id=resolution_id, user=request.user)
    resolution.completed = not resolution.completed
    resolution.save()
    return redirect('home')

@login_required
def profile(request):
    return render(request, 'resolutions/profile.html')

@login_required
def resolution_list(request):
    resolutions = Resolution.objects.filter(user=request.user)
    return render(request, 'resolutions/resolution_list.html', {'resolutions': resolutions})

@login_required
def resolution_detail(request, pk):
    resolution = get_object_or_404(Resolution, pk=pk)
    progress_list = Progress.objects.filter(resolution=resolution)
    return render(request, 'resolutions/resolution_detail.html', {
        'resolution': resolution,
        'progress_list': progress_list
    })

@login_required
def add_progress(request, resolution_id):
    resolution = get_object_or_404(Resolution, id=resolution_id)
    if request.method == 'POST':
        form = ProgressForm(request.POST)
        if form.is_valid():
            progress = form.save(commit=False)
            progress.resolution = resolution
            progress.save()
            return redirect('resolution_detail', pk=resolution_id)
    else:
        form = ProgressForm()
    return render(request, 'resolutions/add_progress.html', {'form': form})

@login_required
def progress_view(request):
    resolutions = Resolution.objects.filter(user=request.user)
    return render(request, 'resolutions/progress.html', {'resolutions': resolutions})