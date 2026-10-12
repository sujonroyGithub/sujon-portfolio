from django.contrib import admin
from .models import Profile, Skill, Service, Project, Experience, ContactMessage

admin.site.register(Profile)
admin.site.register(Skill)
admin.site.register(Service)
admin.site.register(Project)
admin.site.register(Experience)


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'created_at')
    readonly_fields = ('created_at',)
