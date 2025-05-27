from django.http import HttpResponse, Http404
from django.shortcuts import render
from django.template import loader

# Create your views here.

from jobs.models import Job
from jobs.models import JobTypes, Cities


# 函数视图
def joblist(request):
    # 获取排序后的职位列表
    job_list = Job.objects.order_by('job_type')
    template = loader.get_template('joblist.html')
    context = {'job_list': job_list}

    # 添加中文标签
    for job in job_list:
        job.job_type = JobTypes[job.job_type][1]
        job.city_name = Cities[job.job_city][1]
        # print(job)

    # 渲染模板
    return HttpResponse(template.render(context))


def job_detail(request, job_id):
    try:
        job = Job.objects.get(pk=job_id)
        job.city_name = Cities[job.job_city][1]
    except Job.DoesNotExist:
        raise Http404("Job does not exist")

    return render(request, 'job.html', {'job': job})
