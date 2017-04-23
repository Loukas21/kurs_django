from __future__ import unicode_literals, absolute_import, print_function # import z przyszlosci musi byc na poczatku kodu
from django.utils.encoding import python_2_unicode_compatible

from six.moves import range #biblioteka pozwala na dzialanie aplikacji zarowno na python 2 i 3

from django.db import models

# Create your models here.
@python_2_unicode_compatible
class Author(models.Model):
	first_name = models.CharField(max_length=20)
	last_name = models.CharField(max_length=50)
	def __str__(self):
		return "{first_name} {last_name}".format(first_name=self.first_name,last_name=self.last_name)

@python_2_unicode_compatible	
class Publisher(models.Model):
	name = models.CharField(max_length=70)
	def __str__(self):
		return self.name
	
@python_2_unicode_compatible
class Book(models.Model):
	title = models.CharField(max_length=100)
	author = models.ForeignKey(Author) # jezeli klasa Author bylaby po klasie Book, to mozna napisac " 'Author' "
	isbn = models.CharField(max_length=17)
	publisher = models.ForeignKey(Publisher)
	def __str__(self):
		return self.title

#metoda wyswietlajaca reprezentacje napisową danego obiektu
