#!/usr/bin/env bash
# Kurzskript für vqax Training
set -e  # stoppe bei Fehlern

export TOKENIZERS_PARALLELISM=false
export OMP_NUM_THREADS=4

python eUG.py \
  --task vqax \
  --train data/vqax/train_x.json \
  --valid data/vqax/val_x.json \
  --BBPath data/fasterRCNN_features/mscoco_imgfeat \
  --output experiments/vqax_smoketest \
  --batchSize 8 --numWorkers 8 --epochs 1 --save_steps 2000
