from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from .models import Resume, Video
from django.contrib import messages
from django.contrib.auth.models import User
from .utils import get_resume_id
import datetime

# Create your views here.
@login_required
def home(request):
    return render(request, 'main/home.html')


def about(request):        
    return render(request, 'main/about.html')

def preview(request,username,resumeid):
    user = User.objects.filter(username = username).first()
    if not user.profile.is_subscribed():
        return render(request, 'user/notsubscribed.html')
    context = {
        'vidoes' : Video.objects.filter(user = user),
        "resume" : Resume.objects.filter(resumeid = resumeid).first(),  
        'video_check': True if Video.objects.filter(user = user) else False,
        'resume_check': True if Resume.objects.filter(resumeid = resumeid)  else False,
    }
    return render(request, 'main/preview.html',context)

@login_required
def resume(request):
    if request.method == 'POST':
        file = request.FILES.get('file-uploader')
        if hasattr(request.user , 'resume'):
            user_resume = Resume.objects.get(user=request.user)
            user_resume.file = file 
            user_resume.resumeid = get_resume_id()
            print(user_resume.resumeid)
            user_resume.save()
            messages.success(request,'resume updated')
        else: 
            instance = Resume(user = request.user , active = False, file = file , resumeid = get_resume_id())
            instance.save()
        return HttpResponseRedirect(reverse('resume'))
    return render(request, 'main/resume.html')

@login_required
def video(request):
    if request.method == 'POST':
        video = request.FILES.get('video-uploader')
        title = request.POST['video-title']
        instance = Video(user = request.user, title = title, file = video)
        instance.save()
        return HttpResponseRedirect(reverse('video'))
    return render(request, 'main/video.html')

@login_required
def delete_video(request,id):
    video_to_be_deleted = Video.objects.get(id = id)
    video_to_be_deleted.delete()
    return HttpResponseRedirect(reverse('video'))