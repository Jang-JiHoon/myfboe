from django.shortcuts import render
from .forms import ContactUsForm, MeetingForm
from django.urls import reverse
from django.http import HttpResponseRedirect
from .models import Person, Meeting
from django.contrib.auth import authenticate, login
from django.contrib import messages



def main(request):
    if request.method == 'GET': 
        return render(request, "users/main.html")

def contactus(request):
    if request.method=='GET':
        form = ContactUsForm()

        return render(request,'users/contactus.html',{'form':form})

    elif request.method == 'POST':
        form = ContactUsForm(request.POST)

        if form.is_valid():
            

            obj = Person(email_name = form.cleaned_data['email_name'],
            name = form.cleaned_data['name'],
            message_name = form.cleaned_data['message_name']
            )
            obj.save()
            
            # if user is not None:
            #     login(request, user)
            #     return HttpResponseRedirect(reverse('posts:index'))
        else:
            messages.error(request,"Error")
            return render(request,'users/contactus.html',{'form':form})
     
        return render(request, "users/commit.html")  


def meeting(request):
    if request.method=='GET':
        form = MeetingForm()

        return render(request,'users/meeting.html',{'form':form})

    elif request.method == 'POST':
        form = MeetingForm(request.POST)

        if form.is_valid():
            

            obj = Meeting( 
            company = form.cleaned_data['company'],
            industry = form.cleaned_data['industry'],
            firstname = form.cleaned_data['firstname'],
            lastname = form.cleaned_data['lastname'],
            jobtitle = form.cleaned_data['jobtitle'],
            email = form.cleaned_data['email'],
            MM = form.cleaned_data['MM'],
            DD = form.cleaned_data['DD'],
            YYYY = form.cleaned_data['YYYY'],
            message = form.cleaned_data['message'],
            
            )
            obj.save()
            
            # if user is not None:
            #     login(request, user)
            #     return HttpResponseRedirect(reverse('posts:index'))
        else:
            messages.error(request,"Error")
            return render(request,'users/meeting.html',{'form':form})
     
        return render(request, "users/commit.html")     


def commit(request):
    return render(request, "users/main.html")