"""Database Models for Lizard and Comments on the website"""
from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django_quill.fields import QuillField
from django.core.validators import MinValueValidator

DIET = ((0, "Not defined"), (1, "Omnivorous"), (2, "Herbivorous"),
          (3, "Insectivorous")

class Lizard(models.Model):
    """Lizard Database Model
       MinValueValidator, see README Credit 1
    """
     title = models.CharField(
        max_length=100,
        unique=True
    )
    slug = models.SlugField(max_length=100, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='lizard_post')
        description = models.TextField()
    image = CloudinaryField('image', default='default')
    created_on = models.DateField(auto_now_add=True)
    max_size = models.IntegerField(validators=[MinValueValidator(1)])
    lifespan = models.IntegerField(validators=[MinValueValidator(1)])
    price_from = models.IntegerField(validators=[MinValueValidator(1)])
    price_to = models.IntegerField(validators=[MinValueValidator(1)])
    diet = models.IntegerField(choices=DIET, default=0)
    diet_list = QuillField(default="Write lizards favourite food here")
   

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title


