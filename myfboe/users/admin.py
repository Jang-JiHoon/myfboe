from django.contrib import admin
from django.contrib.auth import admin as auth_admin
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from .models import Person, Meeting
from .forms import ContactUsForm, MeetingForm
from django.utils.html import format_html

from myfboe.users.forms import UserAdminChangeForm, UserAdminCreationForm, ContactUsForm

# User = get_user_model()
# #admin.site.register(Person)

# @admin.register(User)
# class UserAdmin(auth_admin.UserAdmin):

#     form = UserAdminChangeForm
#     add_form = UserAdminCreationForm
#     fieldsets = (
#         #(None, {"fields": ("username", "password")}),
#         (_("Personal info"), {"fields": ("name", "email")}),
#         # (
#         #     _("Permissions"),
#         #     {
#         #         "fields": (
#         #             "is_active",
#         #             "is_staff",
#         #             "is_superuser",
#         #             "groups",
#         #             "user_permissions",
#         #         ),
#         #     },
#         # ),
#         # (_("Important dates"), {"fields": ("last_login", "date_joined")}),
#     )
#     list_display = ["username", "name", "is_superuser"]
#     search_fields = ["name"]

@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):

    # def configuration(self, request, queryset):


    form = ContactUsForm
    fieldsets = (
        # (None, {"fields": "name"}),
        (_("name"), {"fields": ("email_name","message_name")}),
        # (
        #     _("Permissions"),
        #     {
        #         "fields": (
        #             "is_active",
        #             "is_staff",
        #             "is_superuser",
        #             "groups",
        #             "user_permissions",
        #         ),
        #     },
        # ),
        # (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
    list_display = ["name", "email_name", "message_name"]
    search_fields = ["name"]
    actions = ['configuation']

@admin.register(Meeting)
class MeetingAdmin(admin.ModelAdmin):

    form = MeetingForm
    fieldsets = (
        (_("Personal info"), {"fields": ('company','industry','firstname','lastname','jobtitle','email','message','status')}),
    )
    list_filter = ('status',)
    list_display = ['company','industry','styled_status']
    search_fields = ['company']
    actions = ['configuration']

    def styled_status(self, obj):
        if obj.status == '검토대기':
            return format_html(f'<span style="color:red">{obj.status}</span>')
        if obj.status == '검토완료':
            return format_html(f'<span style="color:green">{obj.status}</span>')
        return format_html(f'<span>{obj.status}</span>')           
    styled_status.short_description = '상태'