# bert-chinese-classifier

本项目包含大约20000条新闻的训练和测试集。

训练生成fine-tuning模型后即可运行`test.py`进行单句分类测试，也可以运行`server.py`启动flask服务器测试。

预训练模型：https://storage.googleapis.com/bert_models/2018_11_03/chinese_L-12_H-768_A-12.zip


## JupyterNotebook使用

找到`前面的全部一梭子运行`这一个cell，运行前面的全部cell。

然后下面的cell依次运行即可。


## 开始训练

```bash
python train.py
```

## 测试

```bash
python test.py
```

## 测试服务器

```bash
python server.py
```

请求方式为：`http://127.0.0.1:8000?text=现在值得购买的中端手机，都有着出色的配置，性能强劲`


## config文件配置

* model_name：模型名称
* epochs：迭代epoch的数量
* checkpoint_every：间隔多少步保存一次模型
* eval_every：间隔多少步验证一次模型
* learning_rate：学习速率，推荐2e-5， 5e-5， 1e-4
* sequence_length：序列长度，单GPU时不要超过128
* batch_size：单GPU时不要超过32
* num_classes：文本分类的类别数量，若是二分类设置为1
* warmup_rate：训练时的预热比例，建议0.05， 0.1
* output_path：输出文件夹，用来存储label_to_index等文件
* bert_model_path：预训练模型文件夹路径
* train_data：训练数据路径
* eval_data：验证数据路径
* ckpt_model_path：checkpoint模型文件保存路径