from django.db import models
from django.core.exceptions import ValidationError

def validate_image_file(value):
    valid_extensions = ['.jpg', '.jpeg', '.png']
    extension = value.name.split('.')[-1].lower()
    if f".{extension}" not in valid_extensions:
        raise ValidationError('Only JPG, JPEG, and PNG files are allowed.')
# Create your models here.
class franchise(models.Model):
    franchise_id=models.CharField(max_length=1000,unique=True,null=True,blank=True)
    name=models.CharField(max_length=100)
    email=models.EmailField(null=True,blank=True)
    phone = models.CharField(max_length=15,null=True)  # Allow null and blank values
    pan=models.CharField(max_length=12,null=True,blank=True)
    aadhar=models.CharField(max_length=12)
    profession=models.CharField(max_length=30)
    city=models.CharField(max_length=30)
    agreeCheck=models.BooleanField(default=False)
    dsaPhoto=models.ImageField(validators=[validate_image_file],upload_to='dsa/')
    aadharFront=models.ImageField(validators=[validate_image_file],upload_to='dsa/')
    aadharBack=models.ImageField(validators=[validate_image_file],upload_to='dsa/')
    panCard=models.ImageField(validators=[validate_image_file],upload_to='dsa/')
    bankDocument=models.ImageField(validators=[validate_image_file],upload_to='dsa/')
    # New field to track approval status
    aproval_status = models.CharField(max_length=20, choices=[('pending', 'Pending'), ('approved', 'Approved'), ('rejected', 'Rejected')],default='pending')



    def __str__(self):
       return self.name