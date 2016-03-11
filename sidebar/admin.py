from django.contrib import admin

from sidebar.models import Slider, Link

admin.site.register([Slider, Link])
