from ..models import *


class Day(BaseModel):
    title = models.CharField(max_length=50)
    descriptions = models.CharField(max_length=500,null=True,blank=True)


    def __str__(self):
        return self.title
    


class Rooms(BaseModel):
    title = models.CharField(max_length=50)
    descriptions = models.CharField(max_length=500,blank=True,null=True)


    def __str__(self):
        return self.title
    



class TableType(BaseModel):
    title = models.CharField(max_length=50)
    descriptions = models.CharField(max_length=500,blank=True,null=True)


    def __str__(self):
        return self.title
    



class Table(BaseModel):
    start_time = models.TimeField()
    end_time = models.TimeField()
    
   



    def __str__(self):
        return 
