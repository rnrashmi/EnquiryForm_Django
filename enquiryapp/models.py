from django.db import models

# Create your models here.
from multiselectfield import MultiSelectField

class EnquiryData(models.Model):
    name=models.CharField(max_length=100)
    mobile=models.BigIntegerField()
    email=models.EmailField()
    COURSE_CHOICES=(
        ('PYTHON','Python'),
        ('DJANGO','Django'),
        ('UI','ui')
    )

    courses=MultiSelectField(choices=COURSE_CHOICES,max_length=200)

    TRAINER_CHOICES=(
        ('SAI','sai'),
        ('SATYA','satya'),
        ('ROHIT','rohit')
    )
    trainers=MultiSelectField(choices=TRAINER_CHOICES,max_length=200)

    BRANCHES_CHOICES=(
        ('HYD','Hyd'),
        ('BANG','Bang')
    )

    branches=MultiSelectField(choices=BRANCHES_CHOICES,max_length=200)


    gender=models.CharField(max_length=100)
    start_date=models.DateField(max_length=100)