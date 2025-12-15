import os
import glob
import SimpleITK as sitk
import shutil as shuil
from tqdm import tqdm

mri_root = "/home/hongyezeng/data/all_prostate_mri"
save_folder = "/home/hongyezeng/repos/nnUNet/DATASET/nnUNet_raw/Dataset2025_prostate_gland/imagesTs"
os.makedirs(save_folder, exist_ok=True)

for root, folder, files in os.walk(mri_root):
    for file in files:
        if file == "T2.nii.gz":
            source_path = os.path.join(root, file)
            mrn = root.split("/")[-2]
            accession = root.split("/")[-1]
            save_name = f"{mrn}_{accession}_0000.nii.gz"
            dst_path = os.path.join(save_folder, save_name)
            shuil.copy(source_path, dst_path)