from django.shortcuts import render,HttpResponseRedirect,reverse
from .models import *
from random import randint
from .util import *
# Create your views here.

def RegisterPage(request):
    return render(request,"app/register.html")

def SucessPage(request):
    return render(request,"app/sucess.html")


def ShowPage(request):
    return render(request,"app/showdata.html")


def JSPage(request):
    return render(request,"app/js.html")
def RegisterUser(request):
    try:
        if request.POST['role']=='doctor':
            role = request.POST['role']
            firstname = request.POST['firstname']
            lastname = request.POST['lastname']
            password = request.POST['password']
            confirmpassword = request.POST['confirmpassword']
            gender = request.POST['gender']
            email = request.POST['email']
            speciality = request.POST['speciality']
            dateofbirth = request.POST['birthdate']
            city = request.POST['city']
            mobile = (request.POST['phone'])
            profile_pic = request.FILES['image']

            user = User.objects.filter(email=email)
            if user:
                message = 'This email already exists'
                return render(request, 'app/register.html', {'message': message})
            else:
                if password == confirmpassword:
                    otp = randint(10000,99999)
                    newuser = User.objects.create(email=email,password=password,role=role,otp=otp)
                    newdoctor = Doctor.objects.create(user_id=newuser,firstname=firstname,
                     lastname=lastname,profile_pic=profile_pic,
                        gender=gender, speciality=speciality, city=city, mobile=mobile, birthdate=dateofbirth)
                    email_subject = "Doctor Verification"
                    sendmail(email_subject,'mailtemplate',email,{'name':firstname,'otp':otp})
                    return HttpResponseRedirect(reverse('showdetails'))
                else:
                     message = 'Password Does not match'
                     return render(request, 'app/register.html', {'message': message})
        else:
             message = 'Paitent coming soon'
             return render(request, 'app/register.html', {'message': message})



    except User.DoesNotExist:
         message = 'Server Error'
         return render(request, 'app/register.html', {'message': message})

def show_details(request):
    all_doctor = Doctor.objects.all()
    return render(request,"app/showdata.html",{'all_doctor':all_doctor})