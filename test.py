from core.predictor import Predictor
from config import train_config

predictor = Predictor(train_config)
text = "现在值得购买的中端手机，都有着出色的配置，性能强劲"
res = predictor.predict(text)
print(res)