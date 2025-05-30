from django.contrib import admin

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
        "hr_score", "hr_result", "last_editor"
    )

    fieldsets = (
        (None, {'fields': ("user_id", "full_name", "city", "phone", "email", "apply_position", "born_address", "gender", "candidate_remark", "bachelor_college", "master_college", "doctor_college", "major", "degree", "last_editor")}),
        ('第一轮面试记录', {'fields': ("first_score", "first_learning_ability", "first_professional_competency", "first_advantage", "first_disadvantage", "first_result", "first_recommend_department", "first_interviewer", "first_remark")}),
        ('第二轮专业复试记录',{'fields': ("second_score", "second_learning_ability", "second_professional_ability", "second_pursuit_of_excellence_ability", "second_communication_ability", "second_anti_pressure_ability", "second_advantage", "second_disadvantage", "second_result", "second_recommend_department", "second_interviewer", "second_remark")}),
        ('HR复试记录',{'fields': ("hr_score", "hr_responsibility", "hr_communication_ability", "hr_logic_ability", "hr_potential", "hr_stability", "hr_advantage", "hr_disadvantage", "hr_result", "hr_interviewer", "hr_remark")}),
    )

admin.site.register(Candidate, CandidateAdmin)