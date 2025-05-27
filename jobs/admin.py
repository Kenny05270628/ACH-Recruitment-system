from django.contrib import admin
from jobs.models import Job

# Register your models here.
class JobAdmin(admin.ModelAdmin):
    # exclude配置表示：在admin的表单编辑页面中隐藏这些字段，用户不能手动输入或修改它们。
    exclude = ('creator', 'created_date', 'modified_date')
    list_display = ('job_name', 'job_type', 'job_city', 'creator', 'created_date', 'modified_date')

    def save_model(self, request, obj, form, change):
        obj.creator = request.user
        super().save_model(request, obj, form, change)

    pass

admin.site.register(Job, JobAdmin)