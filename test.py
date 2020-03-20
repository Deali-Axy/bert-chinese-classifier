from ipywidgets import interact
from core.predictor import Predictor
from config import train_config

predictor = Predictor(train_config)
text = "王一博被问：是否愿意为了肖战与全世界为敌？王一博的反应太真实"
res = predictor.predict(text)
interact(lambda x: f'分类结果：{x}', x=res)

