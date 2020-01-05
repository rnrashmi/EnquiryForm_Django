from django import forms
from multiselectfield import MultiSelectFormField

class EnquiryForm(forms.Form):
    name=forms.CharField(
        label='Enter Your Name',
        widget=forms.TextInput(
            attrs={
                'placeholder':'your name',
                   'class':'form-control'
            }
        )


    )

    mobile=forms.IntegerField(
        label='Enter Your Mobile Number',
        widget=forms.NumberInput(
            attrs={'placeholder': 'your Mobile',
                   'class': 'form-control'}
        )

    )

    email=forms.EmailField(
        label='Enter Your Email',
        widget=forms.EmailInput(
            attrs={'placeholder': 'your Email',
                   'class': 'form-control'}
        )

    )

    COURSE_CHOICES=(
        ('PYTHON','Python'),
        ('DJANGO','Django'),
        ('UI','ui')
    )

    courses=MultiSelectFormField(choices=COURSE_CHOICES,label='select required courses:')

    TRAINER_CHOICES =(

    ('SAI','sai'),
    ('SATYA','Satya'),
    ('ROHIT','Rohit')
    )

    trainers=MultiSelectFormField(choices=TRAINER_CHOICES,label='select required Trainer:')


    BRANCH_CHOICES =(
         ('HYD','Hyd'),
         ('BANG','Bang'))


    branches=MultiSelectFormField(choices=BRANCH_CHOICES,label='Select preferred branch')

    GENDER_CHOICES=(
        ('MALE','Male'),
        ('FEMALE','Female')

    )


    gender=forms.ChoiceField(
      widget=forms.RadioSelect(),choices=GENDER_CHOICES,
       label='Select your Gender'
    )
    y=range(2019,2050)
    start_date=forms.DateField(
        widget=forms.SelectDateWidget(years=y)

    )