from django import forms
from django.contrib import admin
from django.utils.safestring import mark_safe
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from .models import User, Message, Group, Channel, Reply, MessageHistory, Emoji, Like, Attachment


class MessageForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget)

    class Meta:
        model = User
        fields = '__all__'


class UserAdmin(admin.ModelAdmin):
    readonly_fields = ['avt', 'password']

    def avt(self, user):
        return mark_safe(
            '<img src="/static/{url}" width="120" alt="{alt}" />'.format(url=user.avatar.name, alt=user.first_name)
        )

    class Media:
        css = {
            'all': ('/static/css/style.css',)
        }


class MessageAdmin(admin.ModelAdmin):
    form = MessageForm
    list_display = ['id', 'content', 'sender', 'receiver', 'type', 'created_date']
    search_fields = ['content', 'sender__username', 'receiver__username']
    list_filter = ['sender', 'receiver', 'type', 'created_date']


class ChatChitAdminSite(admin.AdminSite):
    site_header = 'Chat Chit Application'


admin_site = ChatChitAdminSite('myapp')

# Register your models here.
admin_site.register(User, UserAdmin)
admin_site.register(Message, MessageAdmin)
admin_site.register(Group)
admin_site.register(Channel)
admin_site.register(Reply)
admin_site.register(MessageHistory)
admin_site.register(Emoji)
admin_site.register(Like)
admin_site.register(Attachment)
