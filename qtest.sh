#!/usr/bin/env bash
# Kurzskript für vqax test
set -e  # stoppe bei Fehlern

export TOKENIZERS_PARALLELISM=false
export OMP_NUM_THREADS=4

python eUG.py \
  --task vqax \
  --test data/vqax/test_x1.json \
  --load_trained experiments/vqax_smoketest/vqax_trained \
  --output experiments/vqax_run1/eval \
  --BBPath data/fasterRCNN_features/mscoco_imgfeat
