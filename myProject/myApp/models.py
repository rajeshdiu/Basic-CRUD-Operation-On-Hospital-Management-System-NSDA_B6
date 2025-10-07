from django.db import models


class DepartmentModel(models.Model):
    DepartmentName=models.CharField(max_length=100,null=True)
    DepartmentDescription=models.TextField(max_length=100,null=True)
    
    def __str__(self):
        return self.DepartmentName
    
    

class DoctorModel(models.Model):
    DoctorName=models.CharField(max_length=100,null=True)
    Specialization=models.CharField(max_length=100,null=True)
    phone=models.CharField(max_length=100,null=True)
    email=models.EmailField(max_length=100,null=True)
    department=models.ForeignKey(DepartmentModel,max_length=100,null=True,on_delete=models.CASCADE,related_name="my_department")
    doctor_image=models.ImageField(null=True,upload_to="Media/Doctor_Picture")
    
    def __str__(self):
        return self.DoctorName+"-"+self.department.DepartmentName
    
class PatientModel(models.Model):
    PatientName=models.CharField(max_length=100,null=True)
    Age=models.CharField(max_length=100,null=True)
    Gender=models.CharField(max_length=100,null=True)
    email=models.EmailField(max_length=100,null=True)
    Address=models.TextField(max_length=100,null=True)
    doctor=models.ForeignKey(DoctorModel,max_length=100,null=True,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.PatientName
    
    
class AppointmentModel(models.Model):
    patient=models.ForeignKey(PatientModel,max_length=100,null=True,on_delete=models.CASCADE)
    doctor=models.ForeignKey(DoctorModel,max_length=100,null=True,on_delete=models.CASCADE)
    appointment_date= models.DateTimeField(null=True)
    status = models.CharField(max_length=100,null=True,default='Pending')
    
    
    def __str__(self):
        return self.patient.PatientName
    