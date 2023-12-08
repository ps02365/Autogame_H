import os
import shutil

def copy_file_to_train_folder():
    current_dir = os.getcwd()
    label_folder_name = 'labels'
    image_folder_name = 'positive'
    for path in os.listdir(label_folder_name):
        if path == 'classes.txt':
            continue
        filename, file_extension = os.path.splitext(path)
        image_filename = f"{filename}.jpg"
        if os.path.exists(os.path.join(image_folder_name, image_filename)):
            yolov7_train_images_path = os.path.join(current_dir, "yolov7\\data\\train\\images", image_filename)
            yolov7_train_labels_path = os.path.join(current_dir, 'yolov7\\data\\train\\labels', path)
            origin_label = os.path.join(current_dir, label_folder_name,path)
            origin_image = os.path.join(current_dir, image_folder_name, image_filename)
            shutil.copy(origin_label, yolov7_train_labels_path)
            shutil.copy(origin_image, yolov7_train_images_path)
copy_file_to_train_folder()
# def check_missing_file_not_labeled():
#     current_dir = os.getcwd()
#     label_folder_name = 'labels'
#     image_folder_name = 'positive'
#     for path in os.listdir(image_folder_name):
#         if 