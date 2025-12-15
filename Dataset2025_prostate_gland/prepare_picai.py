import os
import glob
import SimpleITK as sitk
import shutil as shuil
from tqdm import tqdm


# image_folder = "/home/hongyezeng/repos/picai_baseline/input/images"
# label_folder = "/home/hongyezeng/repos/picai_baseline/input/picai_labels/anatomical_delineations/whole_gland/AI/Bosma22b"


# output_folder = "/home/hongyezeng/repos/nnUNet/DATASET/nnUNet_raw/Dataset222_prostate_seg"  # 设置输出文件夹
# img_save_folder = os.path.join(output_folder, "imagesTr")
# os.makedirs(img_save_folder, exist_ok=True)
# label_save_folder = os.path.join(output_folder, "labelsTr")
# os.makedirs(label_save_folder, exist_ok=True)

# def convert_mha_to_nii(mha_path, nii_path):
#     """将 .mha 文件转换为 .nii.gz 文件"""
#     try:
#         # 读取 .mha 文件
#         image = sitk.ReadImage(mha_path)
#         # 写入 .nii.gz 文件
#         sitk.WriteImage(image, nii_path)
#         return True
#     except Exception as e:
#         print(f"转换失败: {mha_path}, 错误: {e}")
#         return False

# # 搜索 .mha 文件并转换
# for subject_id in tqdm(os.listdir(image_folder)):
#     subject_path = os.path.join(image_folder, subject_id)
#     if os.path.isdir(subject_path):
#         # 搜索特定的 .mha 文件
#         t2w_files = glob.glob(os.path.join(subject_path, "*_t2w.mha"))
#         adc_files = glob.glob(os.path.join(subject_path, "*_adc.mha"))
#         hbv_files = glob.glob(os.path.join(subject_path, "*_hbv.mha"))

#         # 转换 T2W 文件
#         for t2w_file in t2w_files:
#             output_name = f"{subject_id}_0000.nii.gz"
#             output_path = os.path.join(img_save_folder, output_name)
#             convert_mha_to_nii(t2w_file, output_path)
        
#         # 转换 HBV 文件
#         for hbv_file in hbv_files:
#             output_name = f"{subject_id}_0001.nii.gz"
#             output_path = os.path.join(img_save_folder, output_name)
#             convert_mha_to_nii(hbv_file, output_path)
        
#         # 转换 ADC 文件
#         for adc_file in adc_files:
#             output_name = f"{subject_id}_0002.nii.gz"
#             output_path = os.path.join(img_save_folder, output_name)
#             convert_mha_to_nii(adc_file, output_path)

#         # 在标签文件夹中搜索以 subject_id 开头的文件
#         label_files = glob.glob(os.path.join(label_folder, f"{subject_id}*.nii.gz"))[0]
#         output_path = os.path.join(label_save_folder, f"{subject_id}.nii.gz")
#         shuil.copy(label_files, output_path)

# # # #       # # #  # # #  # # #  # # #  # # #   

# image_folder = "DATASET/nnUNet_raw/Dataset2222_prostate_seg_3channels/imagesTr"
# label_folder = "DATASET/nnUNet_raw/Dataset2222_prostate_seg_3channels/labelsTr"
# output_folder = "/home/hongyezeng/repos/nnUNet/DATASET/nnUNet_raw/Dataset2025_prostate_gland"  # 设置输出文件夹
# img_save_folder = os.path.join(output_folder, "imagesTr")
# label_save_folder = os.path.join(output_folder, "labelsTr")
# os.makedirs(img_save_folder, exist_ok=True)
# os.makedirs(label_save_folder, exist_ok=True)

# i = 0
# for file_name in tqdm(os.listdir(image_folder)):
#     subject_id = file_name.split("_")[0]

#     if file_name.endswith("_0000.nii.gz"):  # only t2w
#         img_path = os.path.join(image_folder, file_name)

#         label_path = os.path.join(label_folder, f"{subject_id}.nii.gz")
#         label = sitk.ReadImage(label_path)
#         img = sitk.ReadImage(img_path)

#         if img.GetSize() != label.GetSize():
#             print(f"Size mismatch for subject {file_name}: image size {img.GetSize()}, label size {label.GetSize()}")
#         else:
#             modality = file_name.split("_")[-1].replace(".nii.gz", "")
#             img_save_path = os.path.join(img_save_folder, f"{i:04}_{modality}.nii.gz")
#             label_save_path =  os.path.join(label_save_folder, f"{i:04}.nii.gz")
#             i += 1

#             shuil.copy(img_path, img_save_path)
#             if not os.path.exists(label_save_path):
#                 shuil.copy(label_path, label_save_path)
