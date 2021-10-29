from django.db import models
import uuid


def rename_and_path(instance, filename):
    extension = filename.split('.')[-1]
    og_filename = filename.split('.')[0]
    new_filename = "users/%s.%s" % (instance.title, extension)

    return new_filename


class Profile(models.Model):

    id = models.UUIDField(default=uuid.uuid4,
                          primary_key=True, editable=False, unique=True)
    created = models.DateTimeField(auto_now_add=True)
    email = models.CharField(max_length=200)
    userName = models.CharField(max_length=200, blank=True, null=True)
    mobile = models.CharField(max_length=200, blank=True, null=True)
    firstName = models.CharField(max_length=200, blank=True, null=True)
    lastName = models.CharField(max_length=200, blank=True, null=True)
    image = models.ImageField(
        default="users/default.jpeg", null=True, blank=True, upload_to=rename_and_path)
