from django.shortcuts import render
from .models import UserProfile

def user_detail(request, user_id):
    user = UserProfile.objects.get(pk=user_id)
    return render(request, 'user_detail.html', {'user': user})

def all_users(request):
    users = UserProfile.objects.all()
    return render(request, 'user/all_user.html', {'users': users})
