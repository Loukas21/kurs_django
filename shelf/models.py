from django.db import models

# Create your models here.
class Author(models.Model):
	first_name = models.CharField(max_length=20)
	last_name = models.CharField(max_length=50)
	
	
class Publisher(models.Model):
	name = models.CharField(max_length=70)


class Book(models.Model):
	title = models.CharField(max_length=100)
	author = models.ForeignKey(Author) # jezeli klasa Author bylaby po klasie Book, to mozna napisac " 'Author' "
	isbn = models.CharField(max_length=17)
	publisher = models.ForeignKey(Publisher)
