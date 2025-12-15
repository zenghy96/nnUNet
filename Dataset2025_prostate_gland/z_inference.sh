#!/bin/bash

# 1. data path
export NNUNET_BASE="/home/hongyezeng/repos/nnUNet/DATASET"
export nnUNet_raw="$NNUNET_BASE/nnUNet_raw"
export nnUNet_preprocessed="$NNUNET_BASE/nnUNet_preprocessed"
export nnUNet_results="$NNUNET_BASE/nnUNet_results"

nnUNetv2_predict \
    -i DATASET/nnUNet_raw/Dataset2025_prostate_gland/imagesTs \
    -o ./output \
    -d 2025 \
    -c 3d_fullres \
    -f 0 \
    -device cuda