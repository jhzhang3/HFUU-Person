'''
DETR论文解析：https://blog.csdn.net/m0_48086806/article/details/132155312?ops_request_misc=%257B%2522request%255Fid%2522%253A%252242e572880ae8aeb87bd18bfacd29330b%2522%252C%2522scm%2522%253A%252220140713.130102334..%2522%257D&request_id=42e572880ae8aeb87bd18bfacd29330b&biz_id=0&utm_medium=distribute.pc_search_result.none-task-blog-2~all~top_positive~default-1-132155312-null-null.142^v102^pc_search_result_base7&utm_term=detr&spm=1018.2226.3001.4187
CSDN论文解析：https://blog.csdn.net/java1314777/article/details/134629701
B站：https://www.bilibili.com/video/BV1ux421X7EL/?spm_id_from=333.337.search-card.all.click&vd_source=b89c6189c2b2b434fe847c59699b0acb
实战复现：https://www.bilibili.com/video/BV11rcXeUEKU/?spm_id_from=333.337.top_right_bar_window_history.content.click&vd_source=b89c6189c2b2b434fe847c59699b0acb


推理命令：
python .\tools\infer.py -c D:\DeskTop\rtdetr_pytorch\configs\rtdetr\rtdetr_r18vd_6x_coco.yml -r D:\DeskTop\rtdetr_pytorch\model\rtdetr_r18vd_dec3_6x_coco_from_paddle.pth -f D:\DeskTop\rtdetr_pytorch\example\1.jpg 

训练命令：从当前checkpoint0071.pth开始训练
python tools/train.py -c configs/rtdetr/rtdetr_r18vd_6x_coco.yml -r ./output/rtdetr_r18vd_6x_coco/checkpoint0071.pth
'''