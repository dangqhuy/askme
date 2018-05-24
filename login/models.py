from django.db import models
# Create your models here.
class User(models.Model):
	username = models.CharField(max_length = 50)
	password = models.CharField(max_length = 50)
	gmailaddress = models.EmailField(max_length = 254)
	fullname = models.CharField(max_length = 50)
	dateofbirth = models.DateTimeField('data published')
	gender = models.CharField(max_length = 10, blank = True, null = True)
	def __str__(self):
		return self.username

	
