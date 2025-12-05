# 后端
## 1 conda常用指令
```
conda env list # 查看已有环境
conda create -n ml python=3.7 # 创建名为ml的python3.7环境
conda activate ml # 激活ml环境
conda deactivate # 退出当前环境
conda remove -n ml --all # 删除ml环境
```

## 2 django
## 2.1 启动一个django项目
```
django-admin startproject ml # 创建django项目
cd ml # 进入项目目录
python manage.py runserver # 启动服务器
python manage.py startapp polls # 创建一个polls应用
```
一个project包含一个或多个app，一个app包含多个models、views、urls、templates等文件。
## 2.2 url与视图函数映射
![映射关系，前面默认加了/，只需要加入后面具体访问地址url](Py_developer_images/1.png)
![url两种传参方式](Py_developer_images/2.png)

## 2.3 路由path函数
![路由path函数](Py_developer_images/3.png)
![路由模块化](Py_developer_images/4.png)
```
path('movies/',include("movies.urls")) # 导入movies模块的urls.py文件
```
## 2.4 模板渲染
![模板视图在views.py中定义，模板文件在templates目录下](Py_developer_images/5.png) 
![模板查找路径配置](Py_developer_images/6.png) 
![视图渲染](Py_developer_images/7.png)

## 2.5 数据库
数据库配置主要是在settings.py文件中进行配置，主要包括数据库类型、数据库名称、用户名、密码、主机地址、端口号等信息。
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'polls',
        'USER': 'root',
        'PASSWORD': '123456',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

## 2.6 ORM
![映射模型到数据库中](Py_developer_images/8.png)
![上述步骤2](Py_developer_images/9.png)
![上述步骤3,添加app](Py_developer_images/10.png)

增删改查：
![增查，借助于视图](Py_developer_images/11.png)
![可以设置排序，顺序以及倒序](Py_developer_images/13.png)
![改，删](Py_developer_images/12.png)


## 2.7 数据写入
用来写后端代码。后端必然需要和数据库打交道，在Django中对于数据库模型一般写在models.py文件中。当写好之后，需要在setting文件中配置引入'book'，见图10 
![](Py_developer_images/10.png)
执行如下命令：
```
python manage.py makemigrations
python manage.py migrate
```
makemigrations的作用是Django会去检查创建或修改数据库，如果不合法会给出提示。当第一次执行该操作，会在app下面创建migrations目录，并创建0001_inital.py文件，文件中记录了当前的建表、依赖等信息。执行完makemigrations只是生成了对应的sql语句，还并没真正将改动迁移到数据库中。需要执行migrate才能将改动迁移到数据库，完成建表、修改字段等操作。所以综上所述，makemigrations生成ddl（数据库模式定义语言），migrate真正地去执行ddl。

## 2.8 Mate配置
可以设置数据表名，否则使用默认的表名“book_book”,前面book为app名，Book为模型名。还可以设置数据展示的顺序，配置一下ordering
![配置Mate](Py_developer_images/14.png)