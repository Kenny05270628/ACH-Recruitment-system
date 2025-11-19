from django.contrib import admin
from datetime import datetime
from interview.models import Candidate
# Register your models here.

# 自定义Admin站点标题
admin.site.site_header = '企业招聘管理系统'  # 左上角主标题
admin.site.site_title = '招聘系统后台'     # 浏览器标签页标题
admin.site.index_title = '数据管理'       # 首页的副标题

class CandidateAdmin(admin.ModelAdmin):
    exclude = ('creator', 'created_date', 'modified_date')

    list_display = (
        "full_name", "city", "bachelor_college", "master_college", "doctor_college",
        "first_score", "first_result", "first_interviewer",
        "second_score", "second_result", "second_interviewer",
        "hr_score", "hr_result", "hr_interviewer" ,"last_editor"
    )

    # 筛选条件
    list_filter = ("city", "first_result", "second_result", "hr_result", "first_interviewer", "second_interviewer", "hr_interviewer")

    # 查询字段
    search_fields = ("full_name", "phone", "email", "bachelor_college")

    ordering = ("hr_result", "second_result", "first_result")

    fieldsets = (
        (None, {'fields': ("user_id", "full_name", "city", "phone", "email", "apply_position", "born_address", "gender", "candidate_remark", "bachelor_college", "master_college", "doctor_college", "major", "degree", "last_editor")}),
        ('第一轮面试', {'fields': ("first_score", "first_learning_ability", "first_professional_competency", "first_advantage", "first_disadvantage", "first_result", "first_recommend_department", "first_interviewer", "first_remark")}),
        ('第二轮面试（专业复试）',{'fields': ("second_score", "second_learning_ability", "second_professional_ability", "second_pursuit_of_excellence_ability", "second_communication_ability", "second_anti_pressure_ability", "second_advantage", "second_disadvantage", "second_result", "second_recommend_department", "second_interviewer", "second_remark")}),
        ('HR复试',{'fields': ("hr_score", "hr_responsibility", "hr_communication_ability", "hr_logic_ability", "hr_potential", "hr_stability", "hr_advantage", "hr_disadvantage", "hr_result", "hr_interviewer", "hr_remark")}),
    )

    def save_model(self, request, obj, form, change):
        obj.last_editor = request.user.username
        if not obj.creator: 
            obj.creator = request.user.username
        obj.modified_date = datetime.now()
        obj.save()
        

admin.site.register(Candidate, CandidateAdmin)