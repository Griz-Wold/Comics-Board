from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth.decorators import login_required

def create_account(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'create_account.html', {'form': form})

@login_required
def account(request):
        username = request.user.username
        email = request.user.email
        avatar = request.user.avatar
        return render(request, 'account.html', {'username': username, 'email': email, 'avatar': avatar})