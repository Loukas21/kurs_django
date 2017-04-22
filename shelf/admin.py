from django.contrib import admin
from .models import Author, Publisher, Book # . oznacza,że to w tej aplikacji

class AuthorAdmin(admin.ModelAdmin):#konwencja, AuthorAdmin dziedziczy po admin.ModelAdmin
	search_fields = ['last_name', 'first_name']
	ordering = ['last_name', 'first_name']
	
class BookAdmin(admin.ModelAdmin):
	search_fields = ['title']
	list_display = ['title', 'author', 'isbn', 'publisher']
	
admin.site.register(Book, BookAdmin)
admin.site.register(Author, AuthorAdmin) # w nawiasie model, klasa administrująca
# Register your models here
admin.site.register(Publisher)

