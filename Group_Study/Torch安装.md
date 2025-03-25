这次安装可谓是历经艰难万苦，装上了GPU版本的pytorch,有显卡才可以装gpu版本，否则只能装cpu版本。
# 1.识别cuda版本
首先，我们需要确认自己的cud版本，在cmd中输入：
```
nvidia-smi
```
第一行就会显示cuda版本，如我的显示：CUDA Version: 11.7 

# 2.安装pytorch
有两种安装方法，第一种去官网找命令安装，可以安装conda或者pip的命令；第二种就是找到命令行中所需要whl文件，下载到本地进行安装。第一种由于系统环境问题，下载速度不一定可以，容易导致下载中断，不一定下载下来，对于其他的包，可以切换成其他如清华镜像源下载。但是在这里，使用清华镜像源虽然看似安装上GPU版本的pytorch了，但实际是给我们安装上的cpu版本的pytorch，所以尽量使用源网址安装。

国内镜像地址：
阿里云
http://mirrors.aliyun.com/pypi/simple/

中国科技大学
https://pypi.mirrors.ustc.edu.cn/simple/

豆瓣(douban)
http://pypi.douban.com/simple/

清华大学
https://pypi.tuna.tsinghua.edu.cn/simple/

中国科学技术大学
http://pypi.mirrors.ustc.edu.cn/simple/

安装的时候就用如下命令：

```
pip install torch==1.10.2 -i https://pypi.tuna.tsinghua.edu.cn/simple
```
 
## 2.1 官网安装
pytorch官网为：https://pytorch.org/get-started/locally/ 这个页面一般展示当前最近版本对应的安装包，要是查看之前的cuda版本可以点击页面中的：Previous CUDA Versions。对应地址为：https://pytorch.org/get-started/previous-versions/    

从中找到对应cuda版本的命令行，前面标注cpu为cpu版本，gpu的有conda命令行和pip命令行。这里展示的是pip的命令行，我的如下：

```
pip install torch==1.13.0+cu117 torchvision==0.14.0+cu117 torchaudio==0.13.0 --extra-index-url https://download.pytorch.org/whl/cu117
```
对应的torch版本为1.13.0，torchvision版本为0.14.0，torchaudio版本为0.13.0。要是网速可以，可以直接命令行安装上。
## 2.2 本地安装
对应为上面的安装方法失效了，可以尝试本地安装。
刚刚的命令行中：https://download.pytorch.org/whl/cu117 ，从这个网站下载torch等三个的whl文件，里面的文件很多，我们要找到对应的。下载速度很慢建议买个vpn节点，不然2.1G下载太长时间了。我的是这个：torch-1.13.0+cu117-cp38-cp38-win_amd64.whl，其中cu117,对应cuda版本11.7，cp38,对应python版本3.8，win_amd64,对应系统版本64位。cpu版本会标识带上cpu，gpu版本则不会。

下载完成后，我们要在切入到虚拟环境中，不然本地环境不一定对应python的版本，比如本地直接输入python，查看的版本为3.12，是conda自带的python，而虚拟环境中的python才是3.8版本，才可以安装上面的包。cmd输入如下命令：

```
activate zjhml    # 切换到虚拟环境
pip install D:\Download\torch-1.13.0+cu117-cp38-cp38-win_amd64.whl  # 安装whl文件
```

# 3.验证安装
验证安装是否成功，可以输入：

```
python
import torch
print(torch.cuda.is_available())
```
结果为True，说明安装成功，至此结束。




