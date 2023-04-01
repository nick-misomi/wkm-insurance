from django.contrib import admin

from .models import ContactForm, SubscribedUsers
# Register your models here.

admin.site.register(ContactForm)
admin.site.register(SubscribedUsers)