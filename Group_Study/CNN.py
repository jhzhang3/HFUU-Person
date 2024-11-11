import numpy as np
import matplotlib.pyplot as plt

#cnn卷积学习来源：https://blog.csdn.net/rocling/article/details/103831994
#Alexnet经典论文讲解：https://www.bilibili.com/video/BV1aW4y1k74S?spm_id_from=333.788.videopod.sections&vd_source=b89c6189c2b2b434fe847c59699b0acb
#不同卷积核介绍：https://blog.csdn.net/mrliuzhao/article/details/106011640


#ImageFilter类是用于实现卷积操作
class ImageFilter:
    
    def __init__(self, image_path, kernel):    # 构造函数
        self.srcImg = plt.imread(image_path)    # 读取图片
        self.kernel = kernel                      # 卷积核
        self.k_size = kernel.shape[0]              # 卷积核大小
        self.dstImg = None                         # 卷积结果

    def generate_dst(self):                          # 生成卷积结果
        m, n, n_channel = self.srcImg.shape                 # 图片大小
        self.dstImg = np.zeros((m - self.k_size + 1, n - self.k_size + 1, n_channel))         # 卷积结果大小
        return self.dstImg                       

    def conv_2d(self):                              # 卷积
        self.generate_dst()                          # 生成卷积结果
        self._conv()                                 # 卷积操作
        return self.dstImg                            # 返回卷积结果

    def _conv(self):
        for i in range(self.dstImg.shape[0]):                        
            for j in range(self.dstImg.shape[1]):       
                for k in range(self.dstImg.shape[2]):                   
                    value = self._con_each(self.srcImg[i:i + self.k_size, j:j + self.k_size, k])         # 卷积操作
                    self.dstImg[i, j, k] = value

    def _con_each(self, src_block):                            # 卷积操作
        pixel_count = self.kernel.size                          # 卷积核大小
        pixel_sum = 0                                             # 卷积核和像素点乘积之和
        _src = src_block.flatten()                                 # 展开图片像素
        _kernel = self.kernel.flatten()                           # 展开卷积核

        for i in range(pixel_count):                            # 卷积操作
            pixel_sum += _src[i] * _kernel[i]                     # 卷积核和像素点乘积之和

        value = pixel_sum / pixel_count                           # 卷积结果
        value = max(0, min(value, 255))                         # 限制值在[0, 255]之间

        return value

    def test_conv(self):                              # 测试卷积
        plt.figure()                                 # 显示图片
        plt.subplot(121)                             # 显示原图
        plt.imshow(self.srcImg)                  

        dst = self.conv_2d()                         # 卷积操作
        plt.subplot(122)                             # 显示卷积结果
        plt.imshow(dst)                             # 显示卷积结果
        plt.show()                                   # 显示图片

#下面是关于卷积核的笔记
# 卷积核1:均值滤波和高斯滤波
'''
这两个滤波器有如下两个共同点:滤波器中元素之和为1.输出亮度与输入基本一致；均为低通滤波器，主要用于图像模糊/平滑处理、消除噪点；核越大，模糊程度越大；


均值滤波器:
kernel = np.ones((3, 3)) / 9
或者这样表达：
kernel = np.array([[1/ 9, 1/ 9, 1/ 9],
                   [1/ 9, 1/ 9, 1/ 9],
                   [1/ 9, 1/ 9, 1/ 9]]) 

                   
高斯滤波器虽然元素总和也为1,但每个位置的权重不一样，权重在行和列上的分布均服从高斯分布，故称高斯滤波器。
高斯分布的标准差越大,则模糊程度越大。一个3 *3 标准差为1的高斯滤波器如下所示                
高斯滤波器:
kernel = np.array([[1, 2, 1],
                   [2, 4, 2],
                   [1, 2, 1]]) / 16
或者这样表达：
kernel = np.array([[1/ 16, 2/ 16, 1/ 16],
                   [2/ 16, 4/ 16, 2/ 16],
                   [1/ 16, 2/ 16, 1/ 16]])
'''

#卷积核2：锐化滤波器
'''
锐化卷积核从名字就可以看出,主要作用就是对图片进行锐化操作,也就是让图像的边缘更加锐利。图像的边缘往往就是变化较大的地方,也就是图像的高频部分,
因此锐化卷积核就是一种高通滤波器。一个3*3的锐化卷积核如下所示:
锐化滤波器:
kernel = np.array([[-1, -1, -1],
                   [-1, 8, -1],
                   [-1, -1, -1]])
可见该卷积核就是计算中心位置像素与周围像素的差值，差值越大则表示该元素附近的变化越大（频率越大），输出值也就越大，因此是高频滤波器的一种.
'''

#卷积核3:一阶微分算子
'''
图像中物体的边缘往往就是变化较为剧烈的部分（高频部分），对于一个函数来说，变化越剧烈的地方，对应的导数的绝对值也就越大。图像就是一种二元函数,
f(x, y)表示( x , y )处像素的值，因此导数除了大小，还有方向。那么求图像在某方向上的一阶导数（或称图像的梯度），也就可以反映出图像在该处的变化程度，
变化程度越快，在该方向的垂直方向可能就存在物体的边缘。
一阶微分算子可以计算出某个方向上物体的边缘，但往往对噪声较为敏感，且边缘检测敏感度依赖于物体的大小。
'''
#3.1:Prewitt算子
'''
Prewitt算子就是对图像进行差分来近似对图像的某个部分求一阶导数。由于导数还具有方向性，因此同样大小的Prewitt算子还有8种不同的类型，
目的在于求上、下、左、右、左上、左下、右上、右下8个方向上的梯度。其中求向右梯度的3*3的Prewitt算子如下所示:

Prewitt算子:
kernel = np.array([[-1, 0, 1],
                   [-1, 0, 1],
                   [-1, 0, 1]])

可见该算子的核是一个3*3的矩阵,分别对应于x方向和y方向的梯度,通过计算梯度的大小,可以检测出图像的边缘。
x方向的梯度表示图像在水平方向的变化,y方向的梯度表示图像在竖直方向的变化。通过计算x方向和y方向的梯度,可以得到图像的边缘。
'''

#3.2:Sobel算子
'''
Sobel算子则是Prewitt算子的改进版，对中间的元素适当进行了加权，Sobel算子之于Prewitt算子类似于高斯滤波之于均值滤波。
同样Prewitt算子，Sobel算子一样考虑方向,计算向上梯度的3*3Sobel算子如下所示：

向上梯度的Sobel算子:
kernel = np.array([[1, 2, 1],              
                   [0, 0, 0],
                   [-1, -2, -1]])

向左梯度的Sobel算子:
kernel = np.array([[2, 1, 0],              
                   [1, 0, -1],
                   [0, -1, -2]])

可见该算子的核是一个3*3的矩阵,分别对应于x方向和y方向的梯度,通过计算梯度的大小,可以检测出图像的边缘。
x方向的梯度表示图像在水平方向的变化,y方向的梯度表示图像在竖直方向的变化。通过计算x方向和y方向的梯度,可以得到图像的边缘。

Sobel算子是一种边缘检测算子,它是一种高通滤波器,可以检测出图像的边缘。Sobel算子的核如下所示:
'''

#卷积核4：二阶微分算子
'''
上一小节介绍的Prewitt算子和Sobel算子都是近似对图像进行一阶导数的计算，只能提取出某个具体方向的边缘。
由微积分的知识可知，一个函数的二阶导数为0时，代表此处的一阶导数取得极值，对应地也就表明原函数在此处的变化最大。
因此往往还可以根据图像的二阶导数过零点的位置，来预测图像中变化最剧烈的地方，也许对应物体的边缘。
与一阶微分算子不同，这些二阶微分算子对边缘的计算具有旋转不变性，也就是可以检测出各个方向上的边缘。
'''

#4.1:Laplace算子
'''
Laplace算子分为两种，分别考虑4-邻接（D4）和8-邻接（D8）两种邻域的二阶微分。

D4算子的核如下所示:
D4算子:
kernel = np.array([[0, 1, 0],
                   [1, -4, 1],
                   [0, 1, 0]])


                   
8-邻接的3*3Laplace算子则考虑到斜对角方向上的梯度
D8算子:
kernel = np.array([[1, 1, 1],
                   [1, -8, 1],
                   [1, 1, 1]])

可以看出D8 Laplace算子与锐化卷积核类似，锐化卷积核计算的是中心像素减去周围像素的差值（中心权重为正，周边权重为负）；
而Laplace算子则是周围像素之和减去中心像素的差值（中心权重为负，周边权重为正）。

'''
#4.2:LoG算子
'''
Laplace算子对噪声依然很敏感。因此常常先使用高斯滤波器对图像进行平滑操作，再使用Laplace算子计算二阶微分。
二者结合称为LoG算子（Laplacian of Gaussian），该算子可以更加稳定地计算图像的二阶微分。常用的5*5的LoG算子如下所示:
LoG算子:
kernel = np.array([[0, 0, 1, 0, 0],              
                   [0, 1, 2, 1, 0],
                   [1, 2, -16, 2, 1],
                   [0, 1, 2, 1, 0],
                   [0, 0, 1, 0, 0]])

LoG算子的核是一个5*5的矩阵,分别对应于x方向和y方向的梯度,通过计算梯度的大小,可以检测出图像的边缘。

'''



# 使用示例
image_path = 'D:/DeskTop/Images/lena.png'   

test_kernel = np.array([[-1, -1, -1],         
                        [-1, 9, -1],
                        [-1, -1, -1]])         # 锐化卷积核

image_filter = ImageFilter(image_path, test_kernel)      
image_filter.test_conv()   






