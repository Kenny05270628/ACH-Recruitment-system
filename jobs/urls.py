# jobs/urls.py
from django.urls import re_path
from jobs import views

urlpatterns = [
    # 使用正则匹配 joblist/
    re_path(r'^$', views.joblist, name='joblist'),
    re_path(r'^(?P<job_id>\d+)/$', views.job_detail, name='job_detail'),
]