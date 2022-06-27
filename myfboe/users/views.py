from django.shortcuts import render
from .forms import ContactUsForm, MeetingForm
from django.urls import reverse
from django.http import HttpResponseRedirect
from .models import Person, Meeting
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.core.mail import EmailMessage
from django.core.mail.message import EmailMessage
from django.core.mail import  EmailMultiAlternatives,BadHeaderError
from django.template.loader import render_to_string
from django.template import loader



import threading
from threading import Thread


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


class EmailThread(threading.Thread):

    def __init__(self, subject, body, from_email, recipient_list, fail_silently, html):

        self.subject = subject

        self.body = body

        self.recipient_list = recipient_list

        self.from_email = from_email

        self.fail_silently = fail_silently

        self.html = html

        threading.Thread.__init__(self)



    def run(self):

        msg = EmailMultiAlternatives(self.subject, self.body, self.from_email, self.recipient_list)



        if self.html:

            msg.attach_alternative(self.html, 'text/html')

        msg.send(self.fail_silently)





def send_email(subject, body, from_email, recipient_list, fail_silently=False, html=False, *args, **kwargs):

    EmailThread(subject, body, from_email, recipient_list, fail_silently, html).start()

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
            # MM = form.cleaned_data['MM'],
            # DD = form.cleaned_data['DD'],
            # YYYY = form.cleaned_data['YYYY'],
            message = form.cleaned_data['message'],
            
            )
            
            obj.save()
            #Meet = MeetingForm(Meeting.objects.all())
            
            # Meet = field.name
            Meet = loader.render_to_string('users/test.html',{
            "company": request.POST['company'],
            "industry": request.POST['industry'],
            "firstname": request.POST['firstname'],
            "lastname": request.POST['lastname'],
            "jobtitle": request.POST['jobtitle'],
            "email": request.POST['email'],
            # "MM": request.POST['MM'],
            # "DD": request.POST['DD'],
            # "YYYY": request.POST['YYYY'],
            "message": request.POST['message'],

            
            })
           
            
            # if user is not None:
            #     login(request, user)
            #     return HttpResponseRedirect(reverse('posts:index'))
        else:
            messages.error(request,"Error")
            return render(request,'users/meeting.html',{'form':form})

        try:
                send_email("새로운 미팅 알림",Meet, "smtp.gmail.com",["ulsan@fboeit.com"])
                
        except BadHeaderError:
                return HttpResponse("Invalid header found.")
     
        return render(request, "users/commit.html")     


def commit(request):
    return render(request, "users/main.html")

