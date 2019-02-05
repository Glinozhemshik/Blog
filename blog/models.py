from django.contrib.auth.models import User
from django.db import models


class Statya(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField("name stayi", max_length=280)
    text = models.TextField("text statyi")
    time = models.DateField(auto_now=True)
    picture = models.ImageField(upload_to="images/", blank=True)
    prosmotry = models.IntegerField(default=0)
    slug = models.SlugField()
