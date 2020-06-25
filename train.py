from core.trainer import Trainer
from config import train_config


# 开始训练
def run_trainer(config: dict):
    trainer = Trainer(config)
    trainer.train()


# 生成训练的分类标签数据
def gen_train_data(config: dict):
    trainer = Trainer(config)
    trainer.load_data()


if __name__ == '__main__':
    run_trainer(train_config)
    # gen_train_data(train_config)
