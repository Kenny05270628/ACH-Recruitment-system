from django.contrib import admin

from .models import Question

# 告诉管理页面，问题 Question 对象需要被管理
admin.site.register(Question)

