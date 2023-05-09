from django.db import models


# Create your models here.
class Booking(models.Model):

    room_types=(
        ('sr','standard'),
        ('dr','deluxe'),
        ('sdr','superdeluxe')

    )

    booking_id=models.AutoField(primary_key=True)
    Name=models.CharField(max_length=100)
    mobile=models.CharField(max_length=100)
    email_id=models.EmailField(max_length=100)
    days=models.IntegerField()
    adhar_no=models.CharField(max_length=100)
    booking_date=models.DateField(auto_now_add=True)
    status=models.CharField(max_length=100)
    no_of_persons=models.IntegerField()
    room_type=models.CharField(max_length=3,choices=room_types)

    def __str__(self):
        return self.Name

    

class Boys(models.Model):

   rno = models.IntegerField(primary_key=True)
   marks = models.IntegerField()
   
   class Meta:
      db_table = "boy"


class Info(models.Model):
    rno= models.IntegerField(primary_key=True)
    name=models.CharField(max_length=45)
    marks=models.IntegerField()

    class Meta:
        db_table="information"