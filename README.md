### Recruitment System

It is a recruitment system developed by Django.

+ 最外层的 mysite/ 根目录只是你项目的容器， Django 不关心它的名字，你可以将它重命名为任何你喜欢的名字。
+ manage.py: 一个让你用各种方式管理 Django 项目的命令行工具。
+ 里面一层的 mysite/ 目录包含你的项目，它是一个纯 Python 包。它的名字就是当你引用它内部任何东西时需要用到的 Python 包名。 (比如 mysite.urls).
+ mysite/__init__.py：一个空文件，告诉 Python 这个目录应该被认为是一个 Python 包。
+ mysite/settings.py：Django 项目的配置文件。
+ mysite/urls.py：Django 项目的 URL 声明，就像你网站的“目录”。
+ mysite/wsgi.py：作为你的项目的运行在 WSGI 兼容的Web服务器上的入口。

```python
python manage.py runserver
```



Django中核心的数据库迁移命令

```python
# 生成生成迁移脚本文件
python manage.py makemigrations
# 应用迁移到数据库
python manage.py migrate
```