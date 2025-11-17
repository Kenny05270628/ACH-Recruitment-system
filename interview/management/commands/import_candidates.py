import csv

from django.core.management import BaseCommand
from interview.models import Candidate

# python manage.py import_candidates --path file.csv
# python manage.py import_candidates --path "C:/Users/38164/Desktop/候选人信息test.csv"

class Command(BaseCommand):
    help = '从一个csv文件导入候选人数据到数据库'

    def add_arguments(self, parser):
        parser.add_argument('--path', type=str, help='包含候选人数据的CSV文件路径')

    def handle(self, *args, **kwargs):
        path = kwargs['path']
        if not path:
            self.stdout.write(self.style.ERROR('请提供CSV文件路径'))
            return

        with open(path, 'rt', encoding='gbk') as f:
            reader = csv.reader(f, dialect='excel', delimiter=',')
            for row in reader:
                print(row[0]) 
                print(row[1])  # 打印每行的第二个字段作为示例
                candidate = Candidate.objects.create(
                    full_name=row[0],
                    city=row[1],
                    phone=row[2],
                    bachelor_college=row[3],
                    major=row[4],
                    degree=row[5],
                    test_score_of_general_ability=row[6],
                    paper_score=row[7],
                )
                print(candidate)