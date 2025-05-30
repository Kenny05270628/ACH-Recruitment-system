from django.db import models

# Create your models here.
# 第一轮面试结果
FIRST_INTERVIEW_RESULT_TYPE = ((u'建议复试', u'建议复试'), (u'待定', u'待定'), (u'放弃', u'放弃'))
# 候选人学历
DEGREE_TYPE = ((u'本科', u'本科'), (u'硕士', u'硕士'), (u'博士', u'博士'))
# HR终面打分
HR_SCORE_TYPE = (
    ('S', 'S（优秀）'),  # 存 'S'，显示 'S（优秀）'
    ('A', 'A（良好）'),
    ('B', 'B（合格）'),
    ('C', 'C（待改进）')
)

class Candidate(models.Model):
    # 基础信息
    user_id = models.IntegerField(unique=True, blank=True, null=True, verbose_name='应聘者ID')
    full_name = models.CharField(max_length=135, verbose_name='姓名')
    city = models.CharField(max_length=135, verbose_name='城市')
    phone = models.CharField(max_length=11, verbose_name='手机号码')
    email = models.EmailField(max_length=254, blank=True, verbose_name='电子邮箱')
    apply_position = models.CharField(max_length=135, blank=True, verbose_name='应聘职位')
    born_address = models.CharField(max_length=135, blank=True, verbose_name='生源地')
    gender = models.CharField(max_length=135, blank=True, verbose_name='性别')
    candidate_remark = models.CharField(max_length=135, blank=True, verbose_name='候选人信息备注')

    # 学校与学历信息
    bachelor_college = models.CharField(max_length=135, blank=True, verbose_name='本科院校')
    master_college = models.CharField(max_length=135, blank=True, verbose_name='硕士院校')
    doctor_college = models.CharField(max_length=135, blank=True, verbose_name='博士院校')
    major = models.CharField(max_length=135, blank=True, verbose_name='专业')
    degree = models.CharField(max_length=135, choices=DEGREE_TYPE, blank=True, verbose_name='学历')

    # 综合能力测评成绩，笔试测评成绩

    # 第一轮面试记录

    # 第二轮面试记录