#!/bin/bash

# 1. data path
export NNUNET_BASE="/home/hongyezeng/repos/nnUNet/DATASET"
export nnUNet_raw="$NNUNET_BASE/nnUNet_raw"
export nnUNet_preprocessed="$NNUNET_BASE/nnUNet_preprocessed"
export nnUNet_results="$NNUNET_BASE/nnUNet_results"

# 2. preprocess
# nnUNetv2_plan_and_preprocess -d 2025 --verify_dataset_integrity  

# # 3. training


DATASET_ID=2025
CONFIG=3d_fullres

for FOLD in {0..4}; do
    LOGFILE="logs/train_fold${FOLD}.log"
    echo ">>> Starting fold ${FOLD}, log: ${LOGFILE}"
    CUDA_VISIBLE_DEVICES=3 nnUNetv2_train ${DATASET_ID} ${CONFIG} ${FOLD} > ${LOGFILE} 2>&1
done


# FOLD=0
# LOGFILE="logs/train_fold${FOLD}.log"
# GPU=${GPUS[$FOLD]}
# echo ">>> Starting fold ${FOLD} on GPU ${GPU}, log: ${LOGFILE}"
# CUDA_VISIBLE_DEVICES=${GPU} nnUNetv2_train ${DATASET_ID} ${CONFIG} ${FOLD} > ${LOGFILE} 2>&1

# for FOLD in {0..2}; do
#     GPU=${GPUS[$FOLD]}
#     LOGFILE="logs/train_fold${FOLD}.log"
#     echo ">>> Starting fold ${FOLD} on GPU ${GPU}, log: ${LOGFILE}"
#     CUDA_VISIBLE_DEVICES=${GPU} nnUNetv2_train ${DATASET_ID} ${CONFIG} ${FOLD} > ${LOGFILE} 2>&1 &
# done

# wait
# echo "All folds have been started."
