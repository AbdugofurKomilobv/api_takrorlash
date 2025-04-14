from django.db import models


from rest_framework import filters



from .auth_user import *


class Course(BaseModel):
    title = models.CharField(max_length=50)
    descriptiaons = models.CharField(max_length=500,null=True,blank=True)


    def __str__(self):
        return self.title
    



class Departaments(BaseModel):
    title = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    descriptiaons = models.CharField(max_length=500,null=True,blank=True)
    search_fields = ['user_phone','user__full_name']


    def __str__(self):
        return self.title
    


class Teacher(BaseModel):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    departaments = models.ManyToManyField(Departaments,related_name='worker')
    course = models.ManyToManyField(Course,related_name='worker')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    descriptiaons = models.CharField(max_length=500,blank=True,null=True)

    def __str__(self):
        return self.user.phone_number