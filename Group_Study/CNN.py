import numpy as np
import matplotlib.pyplot as plt

#cnn卷积学习来源：https://blog.csdn.net/rocling/article/details/103831994
#Alexnet经典论文讲解：https://www.bilibili.com/video/BV1aW4y1k74S?spm_id_from=333.788.videopod.sections&vd_source=b89c6189c2b2b434fe847c59699b0acb
#不同卷积核介绍：https://blog.csdn.net/mrliuzhao/article/details/106011640

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

# 使用示例
image_path = 'D:/DeskTop/Images/lena.png'   

test_kernel = np.array([[-1, -1, -1],         
                        [-1, 9, -1],
                        [-1, -1, -1]])         # 锐化卷积核

image_filter = ImageFilter(image_path, test_kernel)      
image_filter.test_conv()   






