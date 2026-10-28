#Processing the data for CNN model training
import os
import cv2
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

# Define image size (matches CNN input requirement)
IMG_SIZE = 48

def load_and_preprocess_data(data_dir, classes):
    images = []
    labels = []
    
    for label_index, emotion in enumerate(classes):
        folder_path = os.path.join(data_dir, emotion)
        
        for file_name in os.listdir(folder_path):
            img_path = os.path.join(folder_path, file_name)
            
            # Load image in grayscale
            img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
            
            # Skip corrupt/unreadable files
            if img is None:
                continue
            
            # Resize to fixed size (safety check, already 48x48 in this dataset)
            img = cv2.resize(img, (IMG_SIZE, IMG_SIZE))
            
            # Normalize pixel values to range 0-1
            img = img / 255.0
            
            images.append(img)
            labels.append(label_index)
    
    # Convert lists to NumPy arrays
    images = np.array(images)
    labels = np.array(labels)
    
    return images, labels

classes = os.listdir("D:/SUBJECTS/datascience/Project/data/train")
X_train, y_train = load_and_preprocess_data("D:/SUBJECTS/datascience/Project/data/train", classes)

print("X_train shape:", X_train.shape)
print("y_train shape:", y_train.shape)


#-------- Add channel dimension for CNN compatibility--------------
X_train = X_train.reshape(-1, IMG_SIZE, IMG_SIZE, 1)

print("New X_train shape:", X_train.shape)

#------for test data same
X_test, y_test = load_and_preprocess_data("data/test", classes)
X_test = X_test.reshape(-1, IMG_SIZE, IMG_SIZE, 1)

print("X_test shape:", X_test.shape)
print("y_test shape:", y_test.shape)

#----verify one preprocessed image-----
import matplotlib.pyplot as plt

# Check one preprocessed image
plt.imshow(X_train[0].reshape(48, 48), cmap="gray")
plt.title(f"Label: {classes[y_train[0]]}")
plt.axis("off")
plt.show()

print("Pixel value range after normalization:", X_train[0].min(), "to", X_train[0].max())

#--------------Train_Validation_Test Split-------------

from sklearn.model_selection import train_test_split

# Split training data into training (90%) and validation (10%) sets
X_train_final, X_val, y_train_final, y_val = train_test_split(
    X_train, y_train,
    test_size=0.1,
    random_state=42,
    stratify=y_train
)

print("Training set shape:", X_train_final.shape)
print("Validation set shape:", X_val.shape)

#--------------Verify Class Distribution Check-------------
import numpy as np

print("Original class distribution:")
unique, counts = np.unique(y_train, return_counts=True)
print(dict(zip(unique, counts)))

print("\nTraining set class distribution:")
unique, counts = np.unique(y_train_final, return_counts=True)
print(dict(zip(unique, counts)))

print("\nValidation set class distribution:")
unique, counts = np.unique(y_val, return_counts=True)
print(dict(zip(unique, counts)))
