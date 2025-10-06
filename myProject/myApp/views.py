from django.shortcuts import render,redirect
from myApp.models import *

def homePage(request):
    
    
    return render(request,"homePage.html")


def doctorPage(request):
    
    if request.method=="POST":
        name=request.POST.get("name")
        specialty=request.POST.get("specialty")
        Departmet_id=request.POST.get("Departmet_id")
        phone=request.POST.get("phone")
        email=request.POST.get("email")
        
        departmentName=DepartmentModel.objects.get(id=Departmet_id)
        
        data=DoctorModel(
            DoctorName=name,
            Specialization=specialty,
            phone=phone,
            email=email,
            department=departmentName
        )
        
        data.save()
        
        return redirect("doctorPage")
    
    doctors=DoctorModel.objects.all()
    departments=DepartmentModel.objects.all()
    
    context={
        'doctors':doctors,
        'departments':departments
    }
    
    return render(request,"doctorPage.html",context)



def DoctordeletePage(request,id):
    
    data= DoctorModel.objects.get(id=id).delete()
    
    return redirect("doctorPage")
    


def DoctoreditPage(request,id):
    departments=DepartmentModel.objects.all()
    doctor=DoctorModel.objects.get(id=id)
    if request.method=="POST":
        name=request.POST.get("name")
        specialty=request.POST.get("specialty")
        Departmet_id=request.POST.get("Departmet_id")
        phone=request.POST.get("phone")
        email=request.POST.get("email")
        departmentName=DepartmentModel.objects.get(id=Departmet_id)
        
        data=DoctorModel(
            id=id,
            DoctorName=name,
            Specialization=specialty,
            phone=phone,
            email=email,
            department=departmentName
        )
        data.save()
        return redirect("doctorPage")
    context={
        'departments':departments,
        'doctor':doctor,
    }
    return render(request,"DoctoreditPage.html",context)


def patientPage(request):
    
    doctors=DoctorModel.objects.all()
    patients=PatientModel.objects.all()
    
    
    if request.method=="POST":
        PatientName=request.POST.get("PatientName")
        doctor_id=request.POST.get("doctor_id")
        doctor_name=DoctorModel.objects.get(id=doctor_id)
        address=request.POST.get("address")
    
        email=request.POST.get("email")
        gender=request.POST.get("gender")
        age=request.POST.get("age")
        
        data=PatientModel(
            doctor=doctor_name,
            Address=address,
            email=email,
            Age=age,
            Gender=gender,
            PatientName=PatientName
        )
        data.save()
        return redirect("patientPage")
    
    context={
        'doctors':doctors,
        'patients':patients
    }
    
    
    return render(request,"patientPage.html",context)

def appointmentPage(request):
    
    
    return render(request,"appointmentPage.html")


def departmentPage(request):
    
    
    return render(request,"departmentPage.html")