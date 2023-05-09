from django.shortcuts import render,redirect,HttpResponse
from .models import *
from rest_framework . response import Response
from rest_framework . decorators import api_view
from .serializer import *
from rest_framework.decorators import api_view,authentication_classes,permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

# Create your views here.
def index_view(request):
    return render(request, 'resortapp/homepage.html')

def booking_view(request):
    print(request.method)
    if request.method == 'POST':
        uname = request.POST.get('Name')
        mobile= request.POST.get('mobile')
        email= request.POST.get('email_id')
        days = request.POST.get('days')
        adhar= request.POST.get('adhar_no')
        date = request.POST.get('booking_date')
        status = request.POST.get('status')
        noofpersons= request.POST.get('no_of_persons')
        roomtype = request.POST.get('room_type')

        book=Booking(Name=uname,mobile=mobile,email_id=email,days=days,adhar_no=adhar,booking_date=date,status=status,no_of_persons=noofpersons,room_type=roomtype)
        book.save()
        return redirect('/resortapp/display/')



    return render(request, 'resortapp/booking.html')

def display_view(request):
    data = Booking.objects.all()
    context ={'data': data}
    return render(request, 'resortapp/display.html', context)

def update_view(request,booking_id):
    data = Booking.objects.get(pk=booking_id)
    context = {'data': data}

    if request.method == 'POST':
        uname = request.POST.get('Name')
        mobile= request.POST.get('mobile')
        email= request.POST.get('email_id')
        days = request.POST.get('days')
        adhar= request.POST.get('adhar_no')
        date = request.POST.get('booking_date')
        status = request.POST.get('status')
        noofpersons= request.POST.get('no_of_persons')
        roomtype = request.POST.get('room_type')

        # book=Booking(Name=uname,mobile=mobile,email_id=email,days=days,adhar_no=adhar,booking_date=date,status=status,no_of_persons=noofpersons,room_type=roomtype)

        data.Name = uname
        data.mobile = mobile
        data.email_id = email
        data.days = days
        data.adhar_no = adhar
        data.booking_date = date
        data.status = status
        data.no_of_persons = noofpersons
        data.room_type = roomtype
        data.save()

        return redirect('/resortapp/display/')




    return render(request, 'resortapp/update.html', context)


def delete_view(request, booking_id):
    data = Booking.objects.get(pk=booking_id)
    data.delete()
    return redirect('/resortapp/display/')

def photos(request):
    return render(request, 'resortapp/photos.html')

def about(request):
    return render(request, 'resortapp/about.html')


@api_view(['GET','POST'])
def hello(request):
    return Response({"rno":1,"name":"Jack"})

@api_view(['GET','POST'])
def getStudent(request):
    return Response({"rno":1,"name":"Harry","marks":90})


@api_view(['GET','POST'])
def getEmployee(request):
    return Response({"Eid":1,"name":"Tom","Salary":50000})


@api_view(['GET','POST'])
def getProduct(request):
    return Response({"Pid":1,"name":"car","Price":500000})


@api_view(['POST'])
def saveStudent(request):
    datafromclient=request.data
    Boys.objects.create(rno=datafromclient["rno"],marks=datafromclient["marks"])
    # Boys.objects.create(rno=1,marks=70)
    return Response("data stored in db")

@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def getInformation(request,rollnumber):
    informationfromdb=Info.objects.get(rno=rollnumber)
    # boysfromdb=>[rno=103 name=tom marks=90]
    # response=Response({"rno":informationfromdb.rno,"name":informationfromdb.name,"marks":informationfromdb.marks})
    infoSerializer=InfoSerializer(informationfromdb)
    response=Response(infoSerializer.data)
    return response

@api_view(['POST'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def saveInformation(request):
    datafromclient=request.data
    print(datafromclient) 
    # {"rno":1,"name":"jack",marks:90}
    # rnofromclient=datafromclient["rno"]
    # namefromclient=datafromclient["name"]
    # marksfromclient=datafromclient["marks"]

    # Info.objects.create(rno=rnofromclient,name=namefromclient,marks=marksfromclient)
    infoSerializer=InfoSerializer(data=datafromclient)

    if infoSerializer.is_valid():
        infoSerializer.save()

    return Response("data stored in db")



@api_view(['PUT'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def updateInformation(request):
    datafromclient=request.data
    print(datafromclient)
    # {"rno":3,"name":"abhi","marks":504}
    # there is already record of rno 3 we want to update

    informationfromdb=Info.objects.get(rno=datafromclient["rno"])
    serializer=InfoSerializer(informationfromdb,data=datafromclient,partial=False)
    if(serializer.is_valid()):
        serializer.save()

    return Response("data updated in db")


@api_view(['DELETE'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def deleteInformation(request,rollnumber):

    Info.objects.get(rno=rollnumber).delete()

    return Response("data deleted in db")

@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def getALLInformation(request):
    allinformationfromdb=Info.objects.all()
    serializer=InfoSerializer(allinformationfromdb,many=True)
    response=Response(serializer.data)
    return response

def homepage(request):
    return render(request, 'resortapp\home.html')


def addition(request):
     no1=request.GET['number1']
     no2=request.GET['number2']
     no3=int(no1)+int(no2)
     #return HttpResponse(no3)
     return render(request,'resortapp/home.html',{'answer':no3,'no1':no1,'no2':no2})


def substraction(request):
     no1=request.GET['number1']
     no2=request.GET['number2']
     no3=int(no1)-int(no2)
     #return HttpResponse(no3)
     return render(request,'resortapp/home.html',{'answer':no3,'no1':no1,'no2':no2})

def multiplication(request):
     no1=request.GET['number1']
     no2=request.GET['number2']
     no3=int(no1)*int(no2)
     #return HttpResponse(no3)
     return render(request,'resortapp/home.html',{'answer':no3,'no1':no1,'no2':no2})

def division(request):
     no1=request.GET['number1']
     no2=request.GET['number2']
     no3=int(no1)//int(no2)
     #return HttpResponse(no3)
     return render(request,'resortapp/home.html',{'answer':no3,'no1':no1,'no2':no2})



def setsession(request):
    request.session['sname']="akshay"
    return HttpResponse('attribute added in session object')

def getsession(request):
    try:
        studentname=request.session['sname']
        return HttpResponse(studentname)
    except:
        return HttpResponse('session expired')


def removesession(request):
    del request.session['sname']
    return HttpResponse('attribute removed')