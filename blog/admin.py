from django.contrib import admin

from .models import Post # yani un post ke tuye model tarif kardam, noghte ghabl az model yani modeli ke hamin dir ast 

admin.site.register(Post)
