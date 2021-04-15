from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from .models import Student, Recruiter, Job

# from django.contrib.auth import authenticate


# home page
def home(request):
    return render(request, 'job/home.html')

# contact  page
def contact(request):
    return render(request, 'job/contact.html')

# admin_login page  
def admin_login(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            u = request.POST['username']
            p = request.POST['password']
            user = authenticate(username=u, password=p)
            if user is not None:
                # user1 =User.objects.get(user=user)
                if user.is_staff:
                    login(request,user)
                    messages.success(request, 'Admin Succesfully Logged In')
                    return HttpResponseRedirect('/admin_profile/')
                else:
                    messages.info(request,'You are not a staff, you cannot login..!!')
                    return HttpResponseRedirect('/admin_login')
            else:
                messages.info(request,'Pleace enter correct username & password')
                return HttpResponseRedirect('/admin_login')
        else:
            return render(request, 'job/admin_login.html')

    else:
        return HttpResponseRedirect('/admin_profile/')
        



# user_login or (student_login) page  
def user_login(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            u = request.POST['username']
            p = request.POST['password']
            user = authenticate(username=u, password=p)
            if user is not None:
                user1 =Student.objects.get(user=user)
                login(request,user)
                messages.success(request, 'Student Succesfully Logged In')
                return HttpResponseRedirect('/student_profile/')
            else:
                messages.info(request,'Pleace enter correcet username & password..pleace try again!!')
                return HttpResponseRedirect('/user_login')
        else:
            return render(request, 'job/user_login.html')

    else:
        return HttpResponseRedirect('/student_profile/')
        


# recruiter_login  page  
def recruiter_login(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            u = request.POST['username']
            p = request.POST['password']
            user = authenticate(username=u, password=p)
            if user is not None:
                user1 =Recruiter.objects.get(user=user)
                if user1.user_type == 'recruiter' and user1.status != 'pending' and user1.status != 'Reject':
                    login(request,user)
                    messages.success(request, 'Recruiter Succesfully Logged In')
                    return HttpResponseRedirect('/recruiter_profile/')
                else:
                    messages.info(request, 'Your status pending pleace try after sometime..')
                    return HttpResponseRedirect('/recruiter_login')
            else:
                messages.info(request,'Pleace enter correct username & password')
                return HttpResponseRedirect('/recruiter_login')
        else:
            return render(request, 'job/recruiter_login.html')
            

    else:
        return HttpResponseRedirect('/recruiter_profile/')

        


# signupforms
# student_signup page
def student_signup(request):
    
    if request.method == 'POST':
        u = request.POST['username']
        f = request.POST['first_name']
        l = request.POST['last_name']
        e = request.POST['email']
        c = request.POST['contact']
        gen = request.POST['gender']
        pwd = request.POST['password1']
        cpwd = request.POST['password2']
        
        if pwd == cpwd:
            user = User.objects.create_user(first_name=f, last_name=l, username=u, email=e, password=pwd)

            user1 = Student.objects.create(user=user,contact=c, gender=gen, user_type='student')

            messages.success(request, 'Account Created Succesfully..!!')
            return HttpResponseRedirect('/student_signup/')
        else:
            messages.info(request,'Password not matching.Try again..') 
            return HttpResponseRedirect('/student_signup/')
    else:
        return render(request,'job/student_signup.html')


# recruiter_signup page
def recruiter_signup(request):
    
    if request.method == 'POST':
        u = request.POST['username']
        f = request.POST['first_name']
        l = request.POST['last_name']
        comp = request.POST['company']
        e = request.POST['email']
        c = request.POST['contact']
        gen = request.POST['gender']
        pwd = request.POST['password1']
        cpwd = request.POST['password2']
        
        if pwd == cpwd:
            user = User.objects.create_user(first_name=f, last_name=l, username=u, email=e, password=pwd)

            user1 = Recruiter.objects.create(user=user,contact=c, gender=gen, company=comp ,user_type='recruiter',status='pending')

            messages.success(request, 'Recruiter Account Created Succesfully..!!')
            return HttpResponseRedirect('/recruiter_signup/')
        else:
            messages.info(request,'Password not matching.Try again..') 
            return HttpResponseRedirect('/recruiter_signup/')
    else:
        return render(request,'job/recruiter_signup.html')





# student_profile
def student_profile(request):
    if request.user.is_authenticated:
        return render(request, 'job/student_profile.html')
    else:
        return HttpResponseRedirect('/user_login')


# recruiter_profile
def recruiter_profile(request):
    if request.user.is_authenticated:
        return render(request, 'job/recruiter_profile.html')
    else:
        return HttpResponseRedirect('/recruiter_login')
        
# admin_profile
def admin_profile(request):
    if request.user.is_authenticated:
        return render(request, 'job/admin_profile.html')
    else:
        return HttpResponseRedirect('/admin_login')

# recruiter_pending
def recruiter_pending(request):
    if request.user.is_authenticated:
        recruiter_data = Recruiter.objects.filter(status='pending')
        return render(request, 'job/recruiter_pending.html',{'recruiter_data': recruiter_data})
    else:
        return HttpResponseRedirect('/admin_login')

#  recruiter_accept
def recruiter_accept(request):
    if request.user.is_authenticated:
        recruiter_data = Recruiter.objects.filter(status='Accept')
        return render(request, 'job/recruiter_accept.html',{'recruiter_data': recruiter_data})
    else:
        return HttpResponseRedirect('/admin_login')

# recruiter_reject
def recruiter_reject(request):
    if request.user.is_authenticated:
        recruiter_data = Recruiter.objects.filter(status='Reject')
        return render(request, 'job/recruiter_reject.html',{'recruiter_data': recruiter_data})
    else:
        return HttpResponseRedirect('/admin_login')


#  recruiter_all
def recruiter_all(request):
    if request.user.is_authenticated:
        recruiter_data = Recruiter.objects.all()
        return render(request, 'job/recruiter_all.html',{'recruiter_data': recruiter_data})
    else:
        return HttpResponseRedirect('/admin_login')


# view_users page
def view_users(request):
    if request.user.is_authenticated:
        
        student_data = Student.objects.all()
        return render(request, 'job/view_users.html',{'student_data':student_data})
    else:
        return HttpResponseRedirect('/admin_login')

# user_delete 
def user_delete(request,id):
    if request.user.is_authenticated:
        student = User.objects.get(id=id)
        student.delete()
        return HttpResponseRedirect('/view_users')
    else:
        return HttpResponseRedirect('/admin_login')
 

# recruiter_delete
def recruiter_delete(request,id):
    if request.user.is_authenticated:
        recruiter = User.objects.get(id=id)
        recruiter.delete()
        return HttpResponseRedirect('/recruiter_all')
    else:
        return HttpResponseRedirect('/admin_login')

# change_status view
def change_status(request,id):
    if request.user.is_authenticated:
        recruiter = Recruiter.objects.get(id=id)
        if request.method == 'POST':
            s = request.POST['status']
            recruiter.status = s
            recruiter.save()
            messages.success(request, 'Status updated succesfully.')
            return HttpResponseRedirect('/recruiter_all/')
        else:
            return render(request,'job/change_status.html',{'recruiter':recruiter})
    else:
        return HttpResponseRedirect('/admin_login')
        
# addjob view
def addjob(request):
    if request.method == 'POST':
        sd = request.POST['start_date']
        ed = request.POST['end_date']
        t = request.POST['title']
        l = request.POST['location']
        exp = request.POST['experience']
        s = request.POST['salary']
        des = request.POST['description']
        
        user = request.user
        recruiter = Recruiter.objects.get(user=user)
        job = Job.objects.create(recruiter=recruiter,start_date=sd,end_date=ed,title=t,location=l,experience=exp,
        salary=s,description=des)
        
        messages.success(request,'Job added successfully..!!')
        return HttpResponseRedirect('/joblist/')
    else: 
        return render(request,'job/addjob.html')
        
# joblist view
def joblist(request):
    user = request.user
    recruiter = Recruiter.objects.get(user=user)
    job=Job.objects.filter(recruiter=recruiter)
    return render(request,'job/joblist.html',{'job':job})

# student_logout
def all_logout(request):
    if request.user.is_authenticated:
        logout(request)
        return HttpResponseRedirect('/')