from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib.auth import authenticate,login,logout
from .models import *


def index(request):
    data = Questions.objects.all()
    d = {'data': data}
    return render(request,'index.html',d)

def login(request):
    error=""
    if request.method == "POST":
        u = request.POST['uname']
        p = request.POST['pwd']
        user = auth.authenticate(username=u,password=p)
        try:
            if user.is_staff:
                auth.login(request,user)
                error = "no"
            elif user is not None:
                auth.login(request,user)
                return redirect('user_home')
                error = "not"
            else:
                error = "yes"
        except:
            error = "yes"
    d = {'error':error}
    return render(request,'login.html',d)

def admin_home(request):
    if not request.user.is_authenticated:
        return redirect('login')
    return render(request,'admin_home.html')

def logout(request):
    auth.logout(request)
    return redirect('/') 

def questions(request):
    data = Questions.objects.all()
    d = {'data': data}
    return render(request,'questions.html',d)

def signup(request):
    error = ""
    if request.method=='POST':
        f=request.POST['fname']
        l=request.POST['lname']
        e = request.POST['email']
        con = request.POST['contact']
        p = request.POST['pwd']
        gen = request.POST['gender']
        d=request.POST['dob']
        try:
            user=User.objects.create_user(first_name=f,last_name=l,username=e,password=p)
            Signup.objects.create(user=user,mobile=con,gender=gen,dob=d)
            error="no"
        except:
            error="yes"
    d={'error':error}
    return render(request,'signup.html',d)

def user_home(request):
    if not request.user.is_authenticated:
        return redirect('login')
    return render(request,'user_home.html')

def add_que_admin(request):
    if not request.user.is_authenticated:
        return redirect('login')
    error=""
    if request.method=='POST':
        t = request.POST['topic']
        q = request.POST['que']
        try:
            Questions.objects.create(que=q,topic=t)
            error="no"
        except:
            error="yes"
    d={'error':error}
    return render(request,'add_que_admin.html',d)

def add_que_user(request):
    if not request.user.is_authenticated:
        return redirect('login')
    error=""
    if request.method=='POST':
        t = request.POST['topic']
        q = request.POST['que']
        try:
            Questions.objects.create(que=q,topic=t)
            error="no"
        except:
            error="yes"
    d={'error':error}
    return render(request,'add_que_user.html',d)

def view_que_admin(request):
    if not request.user.is_authenticated:
        return redirect('login')
    data = Questions.objects.all()
    d = {'data':data}
    return render(request,'view_que_admin.html',d)

def view_que_user(request):
    data = Questions.objects.all()[::-1]
    hp = Helpful.objects.all()
    ur = request.user
    d = {'data':data,'data2':hp,'ur':ur}
    return render(request,'view_que_user.html',d)

def add_ans_user(request,pid):
    if not request.user.is_authenticated:
        return redirect('login')
    data = Questions.objects.get(id=pid)
    user = request.user
    if request.method == 'POST':
        a = request.POST['ans']
        t = request.POST['atopic']
        try:
            Questions.objects.create(ans=a,user=user,atopic=t,h=0,nh=0)
        except:
            pass
    d = {'data':data}
    return render(request,'add_ans_user.html',d)

def view_user(request):
    if not request.user.is_authenticated:
        return redirect('login')
    data = Signup.objects.all()
    d = {'data':data}
    return render(request,'view_user.html',d)

def delete_user(request,id):
    if not request.user.is_authenticated:
        return redirect('login')
    student = User.objects.get(id=id)
    student.delete()
    return redirect('view_user')

def delete_que(request,id):
    if not request.user.is_authenticated:
        return redirect('login')
    student = Questions.objects.get(id=id)
    student.delete()
    return redirect('view_que_admin')

def change_password(request):
    if not request.user.is_authenticated:
        return redirect('login')
    error=""
    if request.method=="POST":
        c = request.POST['currentpassword']
        n = request.POST['newpassword']
        try:
            u = User.objects.get(id=request.user.id)
            if u.check_password(c):
                u.set_password(n)
                u.save()
                error="no"
            else:
                error="not"
        except:
            error="yes"
    d = {'error':error}
    return render(request,'change_password.html',d)


def feedback(request):
    error=""
    if request.method=='POST':
        n = request.POST['fname']
        p = request.POST['fphone']
        e = request.POST['femail']
        c = request.POST['fcomment']
        try:
            Feedback.objects.create(feedback_name=n,feedback_contact=p,feedback_email=e,feedback_comment=c)
            error = "no"
        except:
            error="yes"
    d = {'error':error}
    return render(request,'feedback.html',d)

def view_feedback(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    data = Feedback.objects.all()
    d = {'data':data}
    return render(request,'view_feedback.html',d)

def delete_feedback(request,id):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    feedback = Feedback.objects.get(id=id)
    feedback.delete()
    return redirect('view_feedback')

def helpful(request,id):
    que = Questions.objects.get(id=id)
    hp = Helpful.objects.all()

    for i in hp:
        n = i.num
        n1 = i.numid
        print (id)
        if n1==id:
            try:
                i.numid = id
                i.num = n+1
                i.save()
                break
            except:
                pass
    else:
        Helpful.objects.create(numid=id, num=1)
            # break
    return redirect('view_que_user')

# def nothelpful(request):
#     num = 1

def write_blog(request):
    if not request.user.is_authenticated:
        return redirect('login')
    user = request.user
    if request.method == 'POST':
        t = request.POST['btopic']
        bc = request.POST['blog']
        try:
            Blog.objects.create(user=user,topic=t, blogc=bc)
        except:
            pass
    return render(request,'write_blog.html')

def view_blogs(request):
    data = Blog.objects.all()
    d = {'data':data}
    return render(request,'view_blogs.html',d)

def view_blog_admin(request):
    data = Blog.objects.all()
    d = {'data':data}
    return render(request,'view_blog_admin.html',d)

def delete_blog(request,id):
    if not request.user.is_authenticated:
        return redirect('login')
    blog = Blog.objects.get(id=id)
    blog.delete()
    return redirect('view_blog_admin')

def view_que_visitor(request):
    data = Questions.objects.all()[::-1]
    hp = Helpful.objects.all()
    d = {'data':data,'data2':hp}
    return render(request,'view_que_visitor.html',d)

def add(request,id):
    all = Questions.objects.all()
    for i in all:
        if i.id==id:
            try:
                i.h = i.h+1
                i.save()
                break
            except:
                pass
    return redirect('view_que_user')

def addd(request,id):
    all = Questions.objects.all()
    for i in all:
        if i.id==id:
            try:
                i.nh = i.nh+1
                i.save()
                break
            except:
                pass
    return redirect('view_que_user')


