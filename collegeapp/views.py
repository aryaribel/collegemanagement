from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from collegeapp.models import CourseModel,StudentModel,TeacherModel
# Create your views here.
def home(request):
    return render(request,'home.html')
def signup(request):
    courses=CourseModel.objects.all()
    context={'courses':courses}
    return render(request,'signup.html',context) 
def loginpage(request):
    return render(request,'login.html') 
# Create your views here.
# def signup(request):
#     return render(request,'signup.html')
def usercreate(request):
    if request.method=='POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        address=request.POST['address']
        age=request.POST['age']
        gender=request.POST['gender']
        phone=request.POST['phone']
        select=request.POST['course']
        course=CourseModel.objects.get(id=select)
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        cpassword=request.POST['cpassword']
        photo=request.FILES.get('file')

        if password==cpassword:  #  password matching......
            if User.objects.filter(username=username).exists(): #check Username Already Exists..
                messages.info(request, 'This username already exists!!!!!!')
                #print("Username already Taken..")
                return redirect('signup')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'this email already exists!!!!')

            else:
                user=User.objects.create_user(
                    first_name=first_name,
                    last_name=last_name,
                    email=email,
                    username=username,
                    password=password)
                user.save()
                #messages.info(request, 'SuccessFully completed.......')
                print("Successed...")

                data=User.objects.get(id=user.id)
                teacher_data=TeacherModel(t_address=address,t_age=age,t_gender=gender,t_email=email,t_phone=phone,t_image=photo,course=course,teacher=data)
                teacher_data.save()
                messages.success(request,'welcome....'+data.first_name)
                return redirect('loginpage')
        else:
            messages.info(request, 'Password doesnt match!!!!!!!')
            print("Password is not Matching.. ") 
            return redirect('signup')   
        return redirect('signin')
    else:
        return render(request,'signup.html')
# @login_required(login_url='loginpage')
def signin(request):
    if request.method == 'POST':
        username = request.POST['username'] 
        password = request.POST['password'] 
        user = auth.authenticate(username=username,password=password) 
        if user is not None:
            if user.is_staff:
                auth.login(request,user)    
                return redirect('admin_home_page') 
            else:
                # login(request,user)   
                auth.login(request,user) 
                return redirect('showdetails',user.id)          
        else:
             return redirect('loginpage')      
    return redirect('loginpage')  

def admin_home_page(request):
    return render(request,'adminhome.html') 
def teacher_home_page(request):
    return render(request,'teacherhome.html')

def CoursePage(request):
    return render(request,'addcourse.html')
def AddCourse(request):
    if request.method == 'POST':
        coursename=request.POST['coursename']
        coursefees=request.POST['coursefees']
        data = CourseModel(crs_name=coursename,crs_fee=coursefees)
        data.save()
        # messages.info(request, 'New User Added')
        return redirect('admin_home_page')

def StudentPage(request):
    courses=CourseModel.objects.all()
    context={'courses':courses}
    return render(request,'addstudent.html',context)
def AddStudent(request):
    if request.method=='POST':
        stdname=request.POST['stdname']
        stdaddress=request.POST['stdaddress']
        gender=request.POST['gender']
        phone=request.POST['phone']
        email=request.POST['email']

        joindate=request.POST['joindate']
        select=request.POST['course']
        course=CourseModel.objects.get(id=select)
        image=request.FILES.get('file')
        data = StudentModel(s_name=stdname,s_address=stdaddress,s_gender=gender,s_phone=phone,s_email=email,joindate=joindate,s_image=image,course=course)
        data.save()
        return redirect('admin_home_page')

def StudentDetails(request):
    student_detail = StudentModel.objects.all()
    return render(request,'studentdetail.html',{'student':student_detail})
def logout(request):
	auth.logout(request)
	return redirect('loginpage')
def deletepage(request,pk):
    studentval=StudentModel.objects.get(id=pk)  
    return render(request,'studentdetail.html',{'student':studentval})
def delete_student(request,pk):
    studentval=StudentModel.objects.get(id=pk)  
    studentval.delete()
    return redirect('StudentDetails')   


def teacherdetails(request):
    teacher=TeacherModel.objects.all()
    return render(request,'teacherdetail.html',{'teacher':teacher})

def s_details(request,pk):
    if request.method=='POST':
        teacher = TeacherModel.objects.get(id=pk)
        teacher.first_name = request.POST.get('first_name')
        teacher.last_name = request.POST.get('last_name')
        teacher.address = request.POST.get('address')
        teacher.age = request.POST.get('age')
        teacher.gender = request.POST.get('gender')
        teacher.phone = request.POST.get('phone')
        teacher.email = request.POST.get('email')
        teacher.course = request.POST.get('course')
        teacher.image=request.FILES.get('file')
        teacher.save()
        return redirect('teacherdetails')
    return render(request,'teacherdetail.html',)
def deleteteacherpage(request,pk):
    teacherval=TeacherModel.objects.get(id=pk)  
    return render(request,'teacherdetail.html',{'teacher':teacherval})
def delete_teacher(request,pk):
    teacherval=TeacherModel.objects.get(id=pk)  
    teacherval.delete()
    return redirect('teacherdetails')

def showdetails(request,pk):
    courses=CourseModel.objects.all()
    teachers =TeacherModel.objects.get(teacher=pk)
    return render(request,'viewteacher.html',{'teacher':teachers,'courses':courses})

def remove_image(request,pk):
    teachers =TeacherModel.objects.get(id=pk)
    teachers.t_image=''
    teachers.save()
    return render(request,'viewteacher.html',{'teacher':teachers})

def updatedetails(request,pk):
    teacherval=TeacherModel.objects.get(id=pk)  
    return render(request,'viewteacher.html',{'teacher':teacherval})

def update_details(request,pk):

    if request.method=='POST':    
        teacher = TeacherModel.objects.get(teacher=pk)
        user=User.objects.get(id=pk)
        old=teacher.t_image
        new=request.FILES.get('file')
        if old !=None and new==None:
            teacher.t_image=old
        else:
            teacher.t_image=new
        user.first_name = request.POST.get('first_name')
        user.last_name = request.POST.get('last_name')
        user.save()
        teacher.t_phone = request.POST.get('phone')
        teacher.t_email = request.POST.get('email')
        teacher.t_age = request.POST.get('age')
        teacher.t_gender = request.POST.get('gender') 
        # select=request.POST['course']
        # course=CourseModel.objects.get(id=select)
        # teacher.course = course             
        teacher.course.crs_name = request.POST.get('course')
        teacher.t_address = request.POST.get('address')

        teacher.save()
        return redirect('showdetails',request.user.id)
    return render(request, 'viewteacher.html')        
