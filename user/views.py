from django.shortcuts import render, redirect 
from django.http import HttpResponse, HttpResponseRedirect
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
import datetime


def signup(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(
                request, f'Account created for {username} you can now login')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'user/signup.html', {'form': form})


@login_required
def profile_edit(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(
            request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, 'Your profile is succesfully updated')
            return redirect('home-page')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {'u_form': u_form,
               'p_form': p_form}
    return render(request, 'user/profileedit.html', context)



@login_required(login_url='subscription')
def subscription_view(request):    
    if request.method == 'POST':
        usr = request.user
        usr.profile.subscription = True
        validity =int(request.POST.get('validity'))
        usr.profile.subscription_validity =  datetime.timedelta(days=validity) + datetime.datetime.now() if datetime.datetime.now(datetime.timezone.utc) > usr.profile.subscription_validity else usr.profile.subscription_validity  + datetime.timedelta(days=validity)
        usr.profile.save()
        return HttpResponseRedirect('subscription')
    return render(request,'user/subscription.html')

@login_required
def profile(request):
    usr = request.user.profile
    context = {
       'sub':"Active" if  usr.is_subscribed() else 'No subscription',
       'days': usr.get_subscription_validity() if usr.is_subscribed() else 'None'
    }
    return render(request,'user/profile.html',context)


    