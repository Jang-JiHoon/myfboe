from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    """
    Default custom user model for myfboe.
    If adding fields that need to be filled at user signup,
    check forms.SignupForm and forms.SocialSignupForms accordingly.
    """

    #: First and last name do not cover name patterns around the globe
    
    GENDER_CHOICES=[
        ('M','Male'),
        ('F', 'Female'),
        ('C', 'Custom'),
    ]
    """
    Default custom user model for djangogram.
    If adding fields that need to be filled at user signup,
    check forms.SignupForm and forms.SocialSignupForms accordingly.
    """

    #: First and last name do not cover name patterns around the globe
    name = models.CharField(_("Name of User"), blank=True, max_length=255)
    user_name = models.CharField( blank=True, max_length=255)
    profile_photo = models.ImageField(blank=True)
    website = models.URLField(blank=True)
    bio = models.TextField(blank=True)
    email = models.CharField(max_length=255, blank=True)
    phone_number  = models.CharField(max_length=255, blank=True)
    gender = models.CharField(max_length=255, choices  = GENDER_CHOICES,  blank=True)
    follwers = models.ManyToManyField("self")
    following = models.ManyToManyField("self")

    def get_absolute_url(self):
        """Get url for user's detail view.

        Returns:
            str: URL for user detail.

        """
        return reverse("users:detail", kwargs={"username": self.username})
    def get_absolute_url(self):
        """Get url for user's detail view.

        Returns:
            str: URL for user detail.

        """
        return reverse("users:detail", kwargs={"username": self.username})
class Person(models.Model):
    #  STATUS_CHOICES=[
    #     ('N','New'),
    #     ('L', 'Later'),
    #     ('F', 'Finished'),
    # ]
    #  status = models.CharField(max_length=1, choices=STATUS_CHOICES)
     name = models.CharField(_("name"), blank=False, max_length=255)
     email_name = models.CharField(_("email_name"), blank=False, max_length=255)
     message_name = models.CharField(_("message_name"), blank=False, max_length=255)


class Meeting(models.Model):
     status = models.name = models.CharField(
         choices=(
             ('검토완료','검토완료'),
             ('검토대기','검토대기'),

         ),
         default='검토대기', max_length=32, verbose_name='상태'
     )
     company = models.CharField(_("company"), blank=False, max_length=255)
     industry = models.CharField(_("industry"), blank=False, max_length=255)
     firstname = models.CharField(_("firstname"), blank=False, max_length=255)
     lastname = models.CharField(_("lastname"), blank=False, max_length=255)
     jobtitle = models.CharField(_("jobtitle"), blank=False, max_length=255)
     email= models.CharField(_("email"), blank=False, max_length=255)
    #  MM = models.CharField(_("MM"), blank=False, max_length=255)
    #  DD = models.CharField(_("DD"), blank=False, max_length=255)
    #  YYYY = models.CharField(_("YYYY"), blank=False, max_length=255)
     message = models.CharField(_("message"), blank=False, max_length=255)