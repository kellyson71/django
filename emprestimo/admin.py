from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(emprestimo)
admin.site.register(leitor)
admin.site.register(blibliotecario)
admin.site.register(livro)
admin.site.register(categoria)