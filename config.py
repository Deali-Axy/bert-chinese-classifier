train_config={
  "model_name": "classifier",
  "epochs": 10,
  "checkpoint_every": 10,
  "eval_every": 10,
  "learning_rate": 5e-5,
  "sequence_length": 128,
  "batch_size": 32,
  "num_classes": 20,
  "warmup_rate": 0.1,
  "output_path": "output/",
  "bert_model_path": "bert_model/chinese_L-12_H-768_A-12",
  "train_data": "data/train.txt",
  "eval_data": "data/test.txt",
  "ckpt_model_path": "ckpt_model/"
}