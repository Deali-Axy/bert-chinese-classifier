from core.trainer import Trainer
from config import train_config


def run_trainer(config: dict):
    trainer = Trainer(config)
    trainer.train()


run_trainer(train_config)
