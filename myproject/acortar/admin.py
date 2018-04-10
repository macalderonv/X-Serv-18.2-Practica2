from django.contrib import admin

# Register your models here.
from acortar.models import ShortedUrl

admin.site.register(ShortedUrl)
