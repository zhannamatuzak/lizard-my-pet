"""Database Models for Lizard and Comments on the website"""
from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.core.validators import MinValueValidator

DIET = ((0, "Not defined"), (1, "Omnivorous"), (2, "Herbivorous"),
          (3, "Insectivorous"))
STATUS = ((0, "Draft"), (1, "Published"))

class Lizard(models.Model):
    """Lizard Database Model
       MinValueValidator, see README Credit 1
    """
    title = models.CharField(max_length=100, unique=True)
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
    diet_list = models.TextField()
    status = models.IntegerField(choices=STATUS, default=0)
   

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

class Experience(models.Model):
    """
    Experiences database model
    """
    post = models.ForeignKey(
        Lizard, on_delete=models.CASCADE, related_name="experiences")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    pet_name = models.CharField(max_length=80, blank=True)
    size = models.IntegerField(validators=[MinValueValidator(1)], blank=True)
    body = models.TextField()
    created_on = models.DateField(auto_now_add=True)
    likes = models.ManyToManyField(
        User, related_name='post_like', blank=True)
    
    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return f"Experience {self.body} by {self.user}"

    def number_of_likes(self):
        return self.likes.count()