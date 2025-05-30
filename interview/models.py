from django.db import models

# Create your models here.
# 第一轮面试结果
FIRST_INTERVIEW_RESULT_TYPE = ((u'建议复试', u'建议复试'), (u'待定', u'待定'), (u'放弃', u'放弃'))
# 复试面试结果
INTERVIEW_RESULT_TYPE = ((u'建议录用', u'建议录用'), (u'待定', u'待定'), (u'放弃', u'放弃'))
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
    test_score_of_general_ability = models.DecimalField(decimal_places=1, null=True,
                                                        max_digits=3, blank=True,
                                                        verbose_name='综合能力测评成绩')
    paper_score = models.DecimalField(decimal_places=1, null=True, max_digits=3, blank=True,
                                      verbose_name='笔试成绩')

    # 第一轮面试记录
    first_score = models.DecimalField(decimal_places=1, null=True, max_digits=2, blank=True,
                                      verbose_name='初试分')
    first_learning_ability = models.DecimalField(decimal_places=1, null=True, max_digits=2, blank=True,
                                                 verbose_name='学习能力得分')
    first_professional_competency = models.DecimalField(decimal_places=1, null=True, max_digits=2, blank=True,
                                                        verbose_name='初试结果')
    first_advantage = models.TextField(max_length = 1024, blank=True, verbose_name='优势')
    first_disadvantage = models.TextField(max_length=1024, blank=True, verbose_name='顾虑及不足')
    first_result = models.CharField(max_length=256, choices=FIRST_INTERVIEW_RESULT_TYPE, blank=True,
                                    verbose_name='初试结果')
    first_recommend_department = models.CharField(max_length=256, blank=True, verbose_name='推荐部门')
    first_interviewer = models.CharField(max_length=256, blank=True, verbose_name='面试官')
    first_remark = models.CharField(max_length=135, blank=True, verbose_name='初试备注')

    # 第二轮面试记录
    second_score = models.DecimalField(decimal_places=1, null=True, max_digits=2, blank=True,
                                      verbose_name='初试分')
    second_learning_ability = models.DecimalField(decimal_places=1, null=True, max_digits=2, blank=True,
                                                 verbose_name='学习能力得分')
    second_professional_ability = models.DecimalField(decimal_places=1, null=True, max_digits=2, blank=True,
                                                  verbose_name='专业能力得分')
    second_pursuit_of_excellence_ability = models.DecimalField(decimal_places=1, null=True, max_digits=2, blank=True,
                                                  verbose_name='追求卓越得分')
    second_communication_ability = models.DecimalField(decimal_places=1, null=True, max_digits=2, blank=True,
                                                  verbose_name='沟通能力得分')
    second_anti_pressure_ability = models.DecimalField(decimal_places=1, null=True, max_digits=2, blank=True,
                                                  verbose_name='抗压能力得分')
    second_advantage = models.TextField(max_length=1024, blank=True, verbose_name='优势')
    second_disadvantage = models.TextField(max_length=1024, blank=True, verbose_name='顾虑及不足')
    second_result = models.CharField(max_length=256, choices=INTERVIEW_RESULT_TYPE, blank=True,
                                    verbose_name='专业复试结果')
    second_recommend_department = models.CharField(max_length=256, blank=True, verbose_name='建议方向或推荐部门')
    second_interviewer = models.CharField(max_length=256, blank=True, verbose_name='面试官')
    second_remark = models.CharField(max_length=135, blank=True, verbose_name='专业复试备注')

    # HR终面
    hr_score = models.CharField(max_length=10, choices=HR_SCORE_TYPE, blank=True, verbose_name='HR复试综合等级')
    hr_responsibility = models.CharField(max_length=10, choices=HR_SCORE_TYPE, blank=True, verbose_name='HR责任心')
    hr_communication_ability = models.CharField(max_length=10, choices=HR_SCORE_TYPE, blank=True, verbose_name='HR坦诚沟通')
    hr_logic_ability = models.CharField(max_length=10, choices=HR_SCORE_TYPE, blank=True, verbose_name='HR逻辑思维')
    hr_potential = models.CharField(max_length=10, choices=HR_SCORE_TYPE, blank=True, verbose_name='HR发展潜力')
    hr_stability = models.CharField(max_length=10, choices=HR_SCORE_TYPE, blank=True, verbose_name='HR稳定性')
    hr_advantage = models.TextField(max_length=1024, blank=True, verbose_name='优势')
    hr_disadvantage = models.TextField(max_length=1024, blank=True, verbose_name='顾虑及不足')
    hr_result = models.CharField(max_length=256, choices=INTERVIEW_RESULT_TYPE, blank=True,verbose_name='HR复试结果')
    hr_interviewer = models.CharField(max_length=256, blank=True, verbose_name='HR面试官')
    hr_remark = models.CharField(max_length=256, blank=True, verbose_name='HR复试备注')

    creator = models.CharField(max_length=256, blank=True, verbose_name='候选人数据的创建者')
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    modified_date = models.DateTimeField(auto_now=True, null=True, blank=True, verbose_name='更新时间')
    last_editor = models.CharField(max_length=256, blank=True, verbose_name='最后编辑者')

    class Meta:
        db_table = 'candidate'
        verbose_name = '应聘者'
        verbose_name_plural = verbose_name

    # 将对象转换为字符串
    def __str__(self):
        return self.full_name