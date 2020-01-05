from django.shortcuts import render
from enquiryapp.models import EnquiryData
from enquiryapp.forms import EnquiryForm
from django.http.response import HttpResponse

# Create your views here.

def enquiryview(request):
    if request.method=="POST":
        eform=EnquiryForm(request.POST)
        if eform.is_valid():
            name=request.POST.get('name')
            mobile1=request.POST.get('mobile')
            email1=request.POST.get('email')
            courses1=eform.cleaned_data.get('courses')
            trainers1=eform.cleaned_data.get('trainers')
            branches1=eform.cleaned_data.get('branches')
            gender1=eform.cleaned_data.get('gender')
            start_date1=eform.cleaned_data.get('start_date')

            data=EnquiryData(
                name=name,
                mobile=mobile1,
                email=email1,
                courses=courses1,
                trainers=trainers1,
                branches=branches1,
                gender=gender1,
                start_date=start_date1
            )

            data.save()
            eform=EnquiryForm()
            return render(request,'enquiryfile.html',{'eform':eform})

        else:
            return HttpResponse('user missed values')



    else:
        eform=EnquiryForm()
        return render(request,'enquiryfile.html',{'eform':eform})