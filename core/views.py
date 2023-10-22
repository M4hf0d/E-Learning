from django.shortcuts import render
from django.shortcuts import get_object_or_404,redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout

from .models import *
from users.models import User
from .forms import *

def index(request):
    context ={'Status':'working'}
    return render(request, "index.html", context)

def homepage(request):
    # users = User.objects.filter(teacher = False)
    users = User.objects.all()
    courses = Course.objects.all()
    context = {'users':users , 'events':courses}
    return render(request, "homepage.html" , context)  

def coursepage(request, pk):
    teacher = False
    user  = request.user
    course =  get_object_or_404(Course , pk=pk) 
    # we want to know if the user is registered or not
    registered = False
    try : 
        mycourses = Course.objects.filter(participants = user)
        if course in mycourses:
            registered = True
        submitted = Submission.objects.filter(event = course , participant = request.user).exists()
        sub = Submission.objects.get(event = course , participant = request.user)
        # registered= request.user.events.filter(id=event.id).exists() #better check if anon user breaks
    except :
        sub = ""
        submitted =False

    try : 
        teacher = user.teacher
    except :
        teacher = False
    context = {'event':course , 'registered':registered ,'submitted': submitted,"sub":sub,"teacher": teacher}
    return render(request, "event.html",context)
@login_required(login_url='login')    
def AssginementsView(request,pk):
    user = request.user
    Assignement =  get_object_or_404(Assignements , pk=pk)
    print( Submission.objects.filter(Assignement=Assignement))
    context = {'assignement':Assignement, "teacher": user.teacher}
    return  render(request, "assignements.html",context)

# @login_required(login_url='login')    
def CoursesView(request, pk):
    enrolled = False
    user = request.user
    mycourse = get_object_or_404(Course, pk=pk)
    cAssignements = mycourse.AssCourse.all().order_by('-created')
    if user.is_authenticated:
        Teacher = user.teacher
        enrolled = mycourse.participants.filter(id=user.id).exists()
        print(enrolled)

    else :
        user = None
        Teacher = None
    
    context = {'event':mycourse,'cass':cAssignements , 'enrolled':enrolled ,"teacher": Teacher}
    return render(request, "event.html",context)




@login_required(login_url='login')    
def project_submission(request,pk):
    myassignement = Assignements.objects.get(pk=pk)
    form = SubmissionForm()
    
    if request.method == 'POST':
        form = SubmissionForm(request.POST) #initial={'event':event, 'participant':request.user} dosnt get sent to server =(
        if form.is_valid():
            submission = form.save(commit=False)
            submission.participant=request.user #fill the user details implicitly
            submission.Course=myassignement.course
            submission.Assignment=myassignement
            form.save()
            return redirect('course_page',pk =myassignement.course.id)
    context = {'assignement': myassignement, 'form': form, 'course':myassignement.course}
    return render(request, "submit_form.html", context)    




from django.shortcuts import render, get_object_or_404
from .models import Course
from django.shortcuts import render, get_object_or_404
from .models import Course
@login_required(login_url='login')    
def enroll_course(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    course.participants.add(request.user)
    return redirect('course_page', pk=course_id )
