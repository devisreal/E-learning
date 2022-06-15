from django.db import models
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator

# Create your models here.
class Profile(models.Model):
   user_types = [
      ('teacher', 'teacher'),
      ('student', 'student'),
      ('parent', 'parent'),
   ]
   user = models.OneToOneField(User, on_delete=models.CASCADE)
   bio = models.TextField(max_length=500, blank=True)
   profile_image = models.ImageField(
      default='default.jpg', 
      upload_to='profile_image', 
      blank=True,
      validators=[FileExtensionValidator(['jpg', 'png', 'jpeg'])]
   )
   date_created = models.DateTimeField(auto_now_add=True)
   user_type = models.CharField(max_length=10, choices=user_types, default='student')
   
   def __str__(self):
      return f"{self.user.username}'s Profile"