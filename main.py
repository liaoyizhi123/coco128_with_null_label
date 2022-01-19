import os
from pathlib import Path
import shutil


def copy_and_change_image_name(origin_dir, img_dir):
    cwd = Path.cwd()
    images = (cwd / origin_dir).glob('*.*')
    for i in images:
        img_name = i.name.split('.')[0]
        img_suffix = i.name.split('.')[1]

        new_name = cwd / img_dir / (img_name + f"_coco128_bg5.{img_suffix}")
        # os.rename(i, new_name)
        shutil.copy(i, new_name)

def get_blank_txt_label(img_dir, label_dir):
    cwd = Path.cwd()
    images = (cwd / img_dir).glob('*.*')
    for i in images:
        parent = i.parent
        img_name = i.name.split(".")[0]
        txt_save_path = cwd / label_dir / f"{img_name}.txt"
        Path(txt_save_path).touch()


def get_trainlist_txt(img_dir):
    cwd = Path.cwd()
    txt_path = Path(img_dir).parent / 'train.txt'
    images = (cwd / img_dir).glob('*.*')
    with open(txt_path, 'w') as f:
        for i in images:
            f.write(str(i)+'\n')



if __name__ == '__main__':

    flag = False

    if flag:
        origin_dir = "images_without_motorbike/images_ori"
        dest_dir = "images_without_motorbike/images"
        copy_and_change_image_name(origin_dir, dest_dir)
    else:
        img_dir = "images_without_motorbike/images"
        label_dir = "images_without_motorbike/labels"
        # get_blank_txt_label(img_dir, label_dir)
        get_trainlist_txt(img_dir)

