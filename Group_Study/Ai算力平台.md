# Ai算力平台
## 1.1大文件传输
首先下载mobaxterm，安装好，点击session,使用sftp连接，输入Remote host为浪潮的ip地址，（点击网页，看网址，像是：172.17.120.160，ip地址可能会变化，具体的实际为准），Username就是登录浪潮的账号（像我就是学号），然后点击OK
之后要输入密码，这个密码在网页内：左侧数据管理-文件管理-复制密码
网址：https://blog.csdn.net/m0_45894743/article/details/131756499?ops_request_misc=&request_id=&biz_id=102&utm_term=Aistation%E4%B8%8A%E4%BC%A0%E6%95%B0%E6%8D%AE&utm_medium=distribute.pc_search_result.none-task-blog-2~all~sobaiduweb~default-0-131756499.142^v102^pc_search_result_base7&spm=1018.2226.3001.4187

## 1.2windows向乌班图传输文件
首先下载mobaxterm，安装好，点击session,使用sftp连接，输入Remote host为乌班图的ip地址，（bash:"hostname -I" ：172.25.161.166，查看ip地址），Username就是登录乌班图的账号（meng），然后点击OK,密码就是登录乌班图用户密码。



# Linux学习
## 1.1修改文件权限
每个文件的属性由左边第一部分的10个字符来确定，其中第一个字符表示文件类型，后面9个字符表示文件权限。-表示没有权限，d表示目录，l表示链接文件，-表示普通文件。权限分为三组用户：文件所有者、文件所在组、其他用户。分别有rwx三个权限。   
- 例如：drwxr-xr-x 2 root root 4096 2021-08-10 16:20 test.txt
- r 表示可读权限    （4）
- w 表示可写权限    （2）
- x 表示可执行权限  （1）

```
chmod 777 test.txt   # 给test.txt文件所有权限
chmod 755 test.txt   # 给test.txt文件文件所有者（读写执行），文件所在组（读、执行），其他用户（读、执行）
chmod 644 test.txt   # 给test.txt文件文件所有者（读写），文件所在组（读），其他用户（读）
```

## 1.2删除文件
- -f ：就是 force 的意思，忽略不存在的文件，不会出现警告信息；
- -i ：互动模式，在删除前会询问使用者是否动作
- -r ：递归删除啊！最常用在目录的删除了！这是非常危险的选项！！！
```
sudo rm -rf test.txt   # sudo代表管理员权限，-r表示递归删除，-f表示强制删除
```

## 1.3磁盘挂载
```
sudo mkdir /mnt/data   # 创建挂载目录，在mut目录下新建一个data目录
sudo mount /dev/sda1 /mnt/data   # 挂载sda1盘到/mnt/data目录下
```
上面已经挂载好了，但是属于手动挂载，每次开关机都得重新输入命令，现在来设置下开机自动挂载。
编辑/etc/fstab文件，添加如下内容：
```
sudo vim /etc/fstab  
uuid=xxxxxx   /mnt/data ext4 defaults 0 0   
```
使用vim编辑器，打开fstab文件，按i进入编辑模式。这里的uuid是sda1盘的uuid，/mnt/data是挂载目录，ext4表示文件系统类型，defaults表示挂载参数，0 0表示不检查文件系统。按Esc键退出编辑模式，输入“:wq！”保存并退出。
- :w：保存文件。
- :q：退出 Vim 编辑器。
- :wq：保存文件并退出 Vim 编辑器。
- :q!：强制退出Vim编辑器，不保存修改。

## 1.4apt命令
apt（Advanced Packaging Tool）是一个在 Debian 和 Ubuntu 中的 Shell 前端软件包管理器。apt 命令提供了查找、安装、升级、删除某一个、一组甚至全部软件包的命令，而且命令简洁而又好记。apt 命令执行需要超级管理员权限(root)。

```
sudo apt-get install xxx   # 安装软件
sudo apt-get remove xxx   # 卸载软件

#deb软件安装
sudo dpkg -i xxx.deb   # 安装deb包
sudo dpkg -r xxx   # 卸载deb包

```

解压相关文件包的命令，常用的命令地址：
- tar：用来压缩和解压文件。
- https://www.runoob.com/linux/linux-comm-tar.html

## 1.5杀死端口占用
```
sudo pkill -9 -f "torchrun.*7777"  # 杀死进程,知道端口占用的为torchrun,端口号7777
```

## 1.6显存爆满但没有相关进程
第一步：查看显存占用情况
```
nvidia-smi

可能会出现如下情况显存爆满但没有相关进程

(yolo) root@5h5bg5eknf4d6-0:/24085404033# nvidia-smi
Mon Jul  7 06:03:16 2025       
+-----------------------------------------------------------------------------------------+
| NVIDIA-SMI 550.127.08             Driver Version: 550.127.08     CUDA Version: 12.4     |
|-----------------------------------------+------------------------+----------------------+
| GPU  Name                 Persistence-M | Bus-Id          Disp.A | Volatile Uncorr. ECC |
| Fan  Temp   Perf          Pwr:Usage/Cap |           Memory-Usage | GPU-Util  Compute M. |
|                                         |                        |               MIG M. |
|=========================================+========================+======================|
|   0  NVIDIA A100-SXM4-80GB          On  |   00000000:92:00.0 Off |                    0 |
| N/A   33C    P0             85W /  400W |   80887MiB /  81920MiB |      0%      Default |
|                                         |                        |             Disabled |
+-----------------------------------------+------------------------+----------------------+
                                                                                         
+-----------------------------------------------------------------------------------------+
| Processes:                                                                              |
|  GPU   GI   CI        PID   Type   Process name                              GPU Memory |
|        ID   ID                                                               Usage      |
|=========================================================================================|
+---------------------------------------------------------
```
步骤一：查看当前用户名
```
whoami
```
步骤二：查看当前用户进程
```
ps -u root #查看当前用户进程
ps -u root | grep python #查看全部python进程
```
步骤三：杀死相关进程
```
kill -9 12345 12347 #杀死进程号为12345和12347的进程
pkill -9 python #杀死全部python进程
```