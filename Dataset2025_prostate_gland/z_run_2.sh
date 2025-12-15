#!/bin/bash

# 1. data path
export NNUNET_BASE="/home/hongyezeng/repos/nnUNet/DATASET"
export nnUNet_raw="$NNUNET_BASE/nnUNet_raw"
export nnUNet_preprocessed="$NNUNET_BASE/nnUNet_preprocessed"
export nnUNet_results="$NNUNET_BASE/nnUNet_results"


# # 3. training


DATASET_ID=2025
CONFIG=3d_fullres

for FOLD in {3..4}; do
    LOGFILE="logs/train_fold${FOLD}.log"
    echo ">>> Starting fold ${FOLD}, log: ${LOGFILE}"
    CUDA_VISIBLE_DEVICES=4 nnUNetv2_train ${DATASET_ID} ${CONFIG} ${FOLD} > ${LOGFILE} 2>&1
done
