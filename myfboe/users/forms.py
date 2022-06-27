from allauth.account.forms import SignupForm
from allauth.socialaccount.forms import SignupForm as SocialSignupForm
from django.contrib.auth import forms as admin_forms
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from django import forms as django_forms
from django import forms
from .models import Person, Meeting

User = get_user_model()


class UserAdminChangeForm(admin_forms.UserChangeForm):
    class Meta(admin_forms.UserChangeForm.Meta):
        model = User


class UserAdminCreationForm(admin_forms.UserCreationForm):
    """
    Form for User Creation in the Admin Area.
    To change user signup, see UserSignupForm and UserSocialSignupForm.
    """

    class Meta(admin_forms.UserCreationForm.Meta):
        model = User

        error_messages = {
            "username": {"unique": _("This username has already been taken.")}
        }


class SignupForm(SignupForm):
    """
    Form that will be rendered on a user sign up section/screen.
    Default fields will be added automatically.
    Check UserSocialSignupForm for accounts created from social.
    """


class UserSocialSignupForm(SocialSignupForm):
    """
    Renders the form when user has signed up using social accounts.
    Default fields will be added automatically.
    See UserSignupForm otherwise.
    """
class ContactUsForm(django_forms.ModelForm):
    class Meta:
        model = Person
        fields = ['email_name', 'name', 'message_name']

        # labels = {
        #     'email' : '이메일',
        #     'name' : '성명',
        #     'username' : '사용자 이름', 
        #     'password' : '비밀번호',
        # }

        widgets = {
            'email_name' : django_forms.TextInput(attrs={'placeholder' : '이메일 주소'}),
            'name' : django_forms.TextInput(attrs={'placeholder' : '성명'}),
            'message_name' : django_forms.TextInput(attrs={'placeholder' : '사용자 이름'}),
            # 'password' : django_forms.PasswordInput(attrs={'placeholder' : '비밀번호'}),
        }

class MeetingForm(django_forms.ModelForm):
    class Meta:
        model = Meeting
        fields = ['company','industry','firstname','lastname','jobtitle','email','message']
        # 'MM','DD','YYYY',
        widgets = {
            'company': django_forms.TextInput(attrs={'placeholder' : 'company'}),
            'industry': django_forms.TextInput(attrs={'placeholder' : 'industry'}),
            'firstname': django_forms.TextInput(attrs={'placeholder' : 'firstname'}),
            'lastname': django_forms.TextInput(attrs={'placeholder' : 'lastname'}),
            'jobtitle': django_forms.TextInput(attrs={'placeholder' : 'jobtitle'}),
            'email': django_forms.TextInput(attrs={'placeholder' : 'email'}),
            # 'MM': django_forms.TextInput(attrs={'placeholder' : 'MM'}),
            # 'DD': django_forms.TextInput(attrs={'placeholder' : 'DD'}),
            # 'YYYY': django_forms.TextInput(attrs={'placeholder' : 'YYYY'}),
            'message': django_forms.TextInput(attrs={'placeholder' : 'message'}),
        }


    
    # def save(self, commit=True):

    #     user = super().save(commit=False)
    #     # user.set_password(self.cleaned_data["password"])
    #     if commit:
    #         user.save()
    #     return user
  
