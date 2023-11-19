from django.contrib import admin
from .models import Folder, Note, User

# Register your models here.
admin.site.register(Folder)
admin.site.register(Note)
admin.site.register(User)