# -*- coding: utf-8 -*-

from django.contrib import admin

from videos import forms
from videos import models


class VideoAdmin(admin.ModelAdmin):
    form = forms.VideoAdminForm
    list_display = ['title', 'video', 'description']

admin.site.register(models.Video, VideoAdmin)
