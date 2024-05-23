from django.contrib.auth.models import AbstractUser
from django.db import models
from ckeditor.fields import RichTextField


# Create your models here.

class User(AbstractUser):
    avatar = models.ImageField(upload_to='chatchits/%Y/%m', default=None)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.username


class BaseModel(models.Model):
    class Meta:
        abstract = True

    created_date = models.DateTimeField(auto_now_add=True)


class Message(BaseModel):  # Tin nhan
    content = RichTextField()  # Noi dung tin nhan

    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name="sent_messages")  # Nguoi gui
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name="received_messages")  # Nguoi nhan
    type = models.CharField(max_length=255)  # Loai tin nhan (van ban, hinh anh, tep)

    def __str__(self):
        return f"{self.sender} -> {self.receiver}: {self.content[:20]}"


class Channel(BaseModel):  # Kenh
    name = models.CharField(max_length=255)
    description = models.TextField()
    creator = models.ForeignKey(User, related_name="creator_channel", on_delete=models.CASCADE)
    type = models.CharField(max_length=255)  # Loại kênh (công khai, riêng tư)
    members = models.ManyToManyField(User, related_name="members_channel")  # Thành viên kênh

    def __str__(self):
        return self.name


class Group(BaseModel):  # Nhom
    name = models.CharField(max_length=255)
    description = models.TextField()
    creator = models.ForeignKey(User, related_name="creator_group", on_delete=models.CASCADE)
    members = models.ManyToManyField(User, related_name="members_group")

    def __str__(self):
        return self.name


class Like(BaseModel):  # Thich tin nhan
    user = models.ForeignKey(User, related_name='likes', on_delete=models.CASCADE)  # Người thích
    message = models.ForeignKey(Message, related_name='likes', on_delete=models.CASCADE)  # Tin nhắn được thích

    def __str__(self):
        return f"{self.user} liked {self.message}"


class Reply(BaseModel):
    content = models.TextField()
    author = models.ForeignKey(User, related_name='reply', on_delete=models.CASCADE)
    message = models.ForeignKey(Message, related_name='reply', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.author} replied to {self.message}: {self.content[:20]}"


class Attachment(BaseModel):
    name = models.CharField(max_length=255)
    file = models.FileField()
    message = models.ForeignKey(Message, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Emoji(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField()

    def __str__(self):
        return self.name


class MessageHistory(BaseModel):
    message = models.ForeignKey(Message, on_delete=models.CASCADE)
    action = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.action} on {self.message}"
