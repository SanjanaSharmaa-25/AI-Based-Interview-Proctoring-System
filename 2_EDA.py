import os
import cv2
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
data_dir = r"D:\train"
classes = os.listdir(data_dir)
IMG_SIZE = 48

def load_and_preprocess_data(data_dir, classes):
    images = []
    labels = []
    for label_index, emotion in enumerate(classes):
        folder_path = os.path.join(data_dir, emotion)
        for file_name in os.listdir(folder_path):
            img_path = os.path.join(folder_path, file_name)
            img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
            if img is None:
                continue
            img = cv2.resize(img, (IMG_SIZE, IMG_SIZE))
            img = img / 255.0
            images.append(img)
            labels.append(label_index)
    images = np.array(images)
    labels = np.array(labels)
    return images, labels

X_train, y_train = load_and_preprocess_data("data/train", classes)
X_train = X_train.reshape(-1, IMG_SIZE, IMG_SIZE, 1)

X_test, y_test = load_and_preprocess_data("data/test", classes)
X_test = X_test.reshape(-1, IMG_SIZE, IMG_SIZE, 1)

print("X_train shape:", X_train.shape)
print("X_test shape:", X_test.shape)



X_train_final, X_val, y_train_final, y_val = train_test_split(
    X_train, y_train,
    test_size=0.1,
    random_state=42,
    stratify=y_train
)

print("Training set shape:", X_train_final.shape)
print("Validation set shape:", X_val.shape)
