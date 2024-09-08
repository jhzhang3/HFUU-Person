# 1:dagnjo新建一个项目
## 1.1安装django
pip安装django：
```python 
pip install Django  
```
查看版本：
```
python3 -m django --version
```
## 1.2创建项目
使用django-admin来创建HelloWorld项目：
```
django-admin startproject HelloWorld
```  
目录结构：
```
|-- HelloWorld
|   |-- __init__.py  
|   |-- asgi.py
|   |-- settings.py (配置文件)
|   |-- urls.py
|   `-- wsgi.py
`-- manage.py (项目管理脚本/项目启动)
```
```
新建一个文件，在文件里面使用cmd，输入以下命令：
1、创建项目
django-admin startproject HelloWorld
2、创建虚拟环境
python -m venv dj_base
3、激活虚拟环境
dj_base\Scripts\activate
4、安装django
pip install django
```

## 1.3创建应用
在HelloWorld目录下创建应用：
```
python manage.py startapp app01  
``` 
目录结构：
```
|-- HelloWorld
|   |-- __init__.py  
|   |-- asgi.py
|   |-- settings.py (配置文件)
|   |-- urls.py
|   `-- wsgi.py
|   |-- app01
|       |-- __init__.py
|       |-- admin.py (模型管理)
|       |-- apps.py (应用配置)
|       |-- migrations
|       |   `-- __init__.py
|       |-- models.py (模型)
|       |-- tests.py (测试)
|       `-- views.py (视图)
`-- manage.py (项目管理脚本/项目启动)
```
## 1.4配置数据库、app路径
在HelloWorld目录下的settings.py文件中，配置数据库路径：
```python
DATABASES = { 
    'default': 
    { 
        'ENGINE': 'django.db.backends.mysql',    # 数据库引擎
        'NAME': 'runoob', # 数据库名称
        'HOST': '127.0.0.1', # 数据库地址，本机 ip 地址 127.0.0.1 
        'PORT': 3306, # 端口 
        'USER': 'root',  # 数据库用户名
        'PASSWORD': '123456', # 数据库密码
    }  
}
```
在 settings.py 中找到INSTALLED_APPS这一项，如下
```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'app01',  # 上面为已有的应用,添加此项
]
```

## 1.5创建模型
在app01目录下创建models.py文件，定义模型：
```python
from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    email = models.EmailField()
#以上相当于是建表
```
建表后需要执行以下命令：
```
python manage.py makemigrations app01  
# 生成迁移文件
python manage.py migrate app01
# 创建表结构
```

## 1.6更新url
前后端分离时候，常常在app01目录下中其他如resource文件定义函数方法,在HelloWorld目录下的urls.py文件中，配置url：
```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path(r'^admin/', admin.site.urls),
    url(r'^app01/', include('app01.urls')),  # 新增app01的url配置
]
```
app01软件下的urls.py文件中，配置url  
sd的示例： 

```python
from tastypie.api import Api
from django.conf.urls import url, include
from gcloud.workflow_management import api
from gcloud.workflow_management.resources import (
    TestResource,
    Management_TemplateResource
)
v3_api = Api(api_name='v3')
v3_api.register(TestResource())
v3_api.register(Management_TemplateResource())

urlpatterns = [
    url(r'', include(v3_api.urls)),
    url(r'^v3/test_workflow/$', api.test_workflow),
    url(r'^v3/test_post/', api.test_post),
    url(r'^v3/test_get_django/', api.test_get),
]
```
目录结构如下：
```
servicedesk_backend-servicedesk_release
└─ 📁servicedesk_backend
   ├─ 📁config
   │  ├─ 📁__pycache__
   │  │  ├─ 📄dev.cpython-37.pyc
   │  │  ├─ 📄log_utils.cpython-37.pyc
   │  │  ├─ 📄redis.cpython-37.pyc
   │  │  ├─ 📄settings.cpython-37.pyc
   │  │  ├─ 📄urls.cpython-37.pyc
   │  │  ├─ 📄wsgi.cpython-37.pyc
   │  │  └─ 📄__init__.cpython-37.pyc
   │  ├─ 📄dev.py
   │  ├─ 📄log_utils.py
   │  ├─ 📄redis.py
   │  ├─ 📄sentinel.py
   │  ├─ 📄settings.py
   │  ├─ 📄urls.py
   │  ├─ 📄wsgi.py
   │  └─ 📄__init__.py
   ├─ 📁gcloud
   │  ├─ 📁workflow
   │  │  ├─ 📁migrations
   │  │  │  ├─ 📁__pycache__
   │  │  │  │  └─ 📄__init__.cpython-37.pyc
   │  │  │  └─ 📄__init__.py
   │  │  ├─ 📁models
   │  │  │  ├─ 📁__pycache__
   │  │  │  │  ├─ 📄template.cpython-37.pyc
   │  │  │  │  └─ 📄__init__.cpython-37.pyc
   │  │  │  ├─ 📄field.py
   │  │  │  ├─ 📄node.py
   │  │  │  ├─ 📄template.py
   │  │  │  ├─ 📄workflow.py
   │  │  │  └─ 📄__init__.py
   │  │  ├─ 📁__pycache__
   │  │  │  ├─ 📄api.cpython-37.pyc
   │  │  │  ├─ 📄resources.cpython-37.pyc
   │  │  │  ├─ 📄urls.cpython-37.pyc
   │  │  │  └─ 📄__init__.cpython-37.pyc
   │  │  ├─ 📄api.py
   │  │  ├─ 📄resources.py
   │  │  ├─ 📄urls.py
   │  │  └─ 📄__init__.py
   │  ├─ 📁workflow_management
   │  │  ├─ 📁migrations
   │  │  │  ├─ 📁__pycache__
   │  │  │  │  ├─ 📄0001_initial.cpython-36.pyc
   │  │  │  │  ├─ 📄0001_initial.cpython-37.pyc
   │  │  │  │  ├─ 📄0002_auto_20240806_1722.cpython-36.pyc
   │  │  │  │  ├─ 📄0002_auto_20240806_1722.cpython-37.pyc
   │  │  │  │  ├─ 📄0003_auto_20240808_1400.cpython-36.pyc
   │  │  │  │  ├─ 📄0003_auto_20240808_1400.cpython-37.pyc
   │  │  │  │  ├─ 📄__init__.cpython-36.pyc
   │  │  │  │  └─ 📄__init__.cpython-37.pyc
   │  │  │  ├─ 📄0001_initial.py
   │  │  │  ├─ 📄0002_auto_20240806_1722.py
   │  │  │  ├─ 📄0003_auto_20240808_1400.py
   │  │  │  └─ 📄__init__.py
   │  │  ├─ 📁__pycache__
   │  │  │  ├─ 📄api.cpython-36.pyc
   │  │  │  ├─ 📄api.cpython-37.pyc
   │  │  │  ├─ 📄models.cpython-36.pyc
   │  │  │  ├─ 📄models.cpython-37.pyc
   │  │  │  ├─ 📄resources.cpython-36.pyc
   │  │  │  ├─ 📄resources.cpython-37.pyc
   │  │  │  ├─ 📄urls.cpython-36.pyc
   │  │  │  ├─ 📄urls.cpython-37.pyc
   │  │  │  ├─ 📄__init__.cpython-36.pyc
   │  │  │  └─ 📄__init__.cpython-37.pyc
   │  │  ├─ 📄api.py
   │  │  ├─ 📄apps.py
   │  │  ├─ 📄models.py
   │  │  ├─ 📄resources.py
   │  │  ├─ 📄tests.py
   │  │  ├─ 📄urls.py
   │  │  └─ 📄__init__.py
   │  ├─ 📁__pycache__
   │  │  ├─ 📄exceptions.cpython-37.pyc
   │  │  ├─ 📄utils.cpython-37.pyc
   │  │  └─ 📄__init__.cpython-37.pyc
   │  ├─ 📄exceptions.py
   │  ├─ 📄utils.py
   │  └─ 📄__init__.py
   ├─ 📁__pycache__
   │  └─ 📄manage.cpython-37.pyc
   ├─ 📄.gitignore
   ├─ 📄changelog.md
   ├─ 📄cookbook.sh
   ├─ 📄Dockerfile
   ├─ 📄flowdetail_test.py
   ├─ 📄get-pip.py
   ├─ 📄init_pipeline_field.py
   ├─ 📄init_template_field.py
   ├─ 📄manage.py
   ├─ 📄README.md
   ├─ 📄requirements.txt
   ├─ 📄start.sh
   ├─ 📄supervisor-uwsgi.ini
   ├─ 📄supervisord.conf
   └─ 📄uwsgi.ini
```