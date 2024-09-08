# 实习内容
## 1. Postman测试(增删改查)
四项请求都需要Header
这些信息是部署前端获得的，通过F12查询看到Headers
### 1.1增(post)
增加数据的时候在Bodyl里面的raw里面选择json，然后在下面输入数据，点击Send即可,需要输入的数据格式为json格式。
### 1.2删(delete)
删除的时候根据id进行删除
### 1.3改(put)
修改的时候根据id进行修改，然后在Body里面的raw里面选择json，然后在下面输入数据，点击Send即可,需要输入的数据格式为json格式。
### 1.4查(get)
查询的时候根据id进行查询

## 2.前端环境启动
### 2.1安装node.js
下载安装node.js，安装完成后，打开命令行，输入npm -v，查看是否安装成功。
### 2.2cmd启动项目
npm未安装执行一下命令，在项目目录下打开cmd命令行，输入  
注意：一定是要在项目下打开cmd命令行，输入以下命令！！！！ 
```
npm install #（安装npm）
yarn install #（安装yarn）
yarn dev #（运行环境）
``` 
或启动项目，项目启动成功后，会自动打开浏览器，输入http://localhost:8080/ 即可访问项目。  
注：要求先打开后端项目,再启动前端项目。
### 2.3输入cookie
部署企业级项目时候，可能存在登录问题，需要到门户网站中查找cookie，F12查看应用程序，再查看cookie，寻找到相关网页的cookie value，复制到前端网页同样的地方，即可进行访问本地部署的前端页面。

## 3.pycharm里面使用git
csdn文章地址：
https://blog.csdn.net/bfz_50/article/details/120941200
### 3.1下拉git项目
pycharm中Files-Settings-Version Control-Git-test，自动识别电脑中git地址，并测试是否可用，结果是返回git版本。  
点击git-clone，填写url 点击clone，项目拉取完成。 
也可以在终端输入命令(在terminal中输入)：
```
git clone url ()
``` 
### 3.2创建/切换分支
1：没有分支，新建分支  
在master分支下,右键选择New BRANCH from master，输入分支名，点击Create Branch。
(该分支将会基于master创建, 如果在打开其他分支下新建分支, 就会基于该分支进行创建)

2：有分支，创建新分支   
在master分支下，右键选择checkout，选择要切换的分支，点击切换。对应指令:
```
git checkout master
```

### 3.3提交代码
在pycharm中，点击git-commit，填写commit message，点击commit and push，提交代码。

## 4.前端部署问题
### 4.1下载下来的前端被锁住了
下载下来的前端项目，在某些情况下，会被锁住，无法进行修改，解决方法：  
删除两个文件包package-lock.json和yarn.lock,之后重新运行npm install，yarn dev进行启动
### 4.2环境地址配置
部分文件依旧打不开，需要在vue.config.js中配置代理环境地址，如下： 
```
proxy = {
      '/api': {
        target: 'http://10.5.164.78:9090/'
        //target: 'http://localhost:9090/'
      },
      '/core': {
        target: 'http://localhost:3000/'
      }
    }
``` 
修改以后，问题即可解决。


# 技术栈
前端：html、css、javascript、vue

后端：java、python  
web框架：springboot(java)、django(python)  
数据库：mysql、oracle、sql server、mongodb  
版本管理：git  
服务器：linux、windows   
测试工具：postman
部署工具：docker 
```
HTML 定义了网页的内容
CSS 描述了网页的布局
JavaScript 控制了网页的行为
```

# 总结

1：说话要有逻辑，分点列出回答，需要对已有问题进行总结概括，总结提炼出重要内容。了解具体的需求远比怎么去做更为重要，技术不会不用担心，可以慢慢去学习，但要确保思维方向的正确性。

