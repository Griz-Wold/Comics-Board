from django.db import models
from django.core.validators import MinValueValidator
from accounts.models import PicturaUser

class Posting(models.Model):
    account = models.ForeignKey(PicturaUser, on_delete=models.CASCADE, null=False, blank=False)
    title = models.CharField(max_length=50, null=False, blank=False)
    description = models.TextField(max_length=200, null=True, blank=True)
    price = models.IntegerField(validators=[MinValueValidator(0)])
    pub_date = models.DateField(auto_now_add=True)
    image = models.ImageField(upload_to='images/', default='images/default.png')

    def __str__(self):
        return self.title