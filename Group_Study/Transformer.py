<<<<<<< HEAD
'''
VIT论文讲解：https://www.bilibili.com/video/BV15P4y137jb?spm_id_from=333.788.videopod.sections&vd_source=b89c6189c2b2b434fe847c59699b0acb
vit代码：https://www.bilibili.com/video/BV1Xwc6eoEBa?spm_id_from=333.788.videopod.sections&vd_source=b89c6189c2b2b434fe847c59699b0acb
vit，detr，rt-detr代码：https://www.bilibili.com/video/BV1xm4y1b7Pw?spm_id_from=333.788.player.switch&vd_source=b89c6189c2b2b434fe847c59699b0acb

qkv讲解
q: query，主动计算与其他token相似度，Q1与k1,k2,k3……之间的相似度
k: key，被动计算与其他token相似度
v: value，当前token的重要程度

公式：
Attention(Q,K,V)=softmax(QK^T/√d_k)V
单头注意力机制：初始token会与一个W相乘，得到qkv，然后再进行Attention计算Q1与k1,k2,k3……之间的点积，除以√d_k的平方根，（除以模型的维度），再归一化，再与V相乘，得到Q1的注意力权重。
例如w=[2,5,7],他的维度就是3
多头注意力机制的话，初始token会与不同的W相乘，得到不同的Qkv，然后再进行Attention计算。
维度的话：d_k=d_v=d_model/h，h是头的个数（W的个数），d_model是模型的维度。

'''
=======
>>>>>>> ca1a2f833dce82b7e83876e1224fcefa05d56069


