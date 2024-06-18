from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm


# Create your views here.
def sign_up(request):
    if request.method=='POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog-index')
    else:
        form=UserCreationForm()

    context={
        'form':form
    }
    return render(request, 'users/sign_up.html', context)

def profile(request):
    return render(request, 'users/profile.html')

def logout(request):
    return render(request, 'users/logout.html')