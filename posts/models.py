from django.db import models
import uuid


def rename_and_path(instance, filename):
    extension = filename.split('.')[-1]
    og_filename = filename.split('.')[0]
    new_filename = "posts/%s.%s" % (instance.title, extension)

    return new_filename


class Post(models.Model):
    id = models.UUIDField(default=uuid.uuid4,
                          primary_key=True, editable=False, unique=True)
    created = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(
        default="posts/default.jpeg", null=True, blank=True, upload_to=rename_and_path)
    title = models.CharField(max_length=200, blank=True, null=True)
    summary = models.TextField(blank=True, null=True)
    updated = models.DateTimeField(null=True, blank=True)
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    # author
    parent = models.ForeignKey(
        'Post', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.title
