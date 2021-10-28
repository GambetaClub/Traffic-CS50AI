import cv2
import numpy as np
import os
import os.path
import sys
import tensorflow as tf

from sklearn.model_selection import train_test_split
from tensorflow.python.autograph.pyct.parser import MAX_SIZE

EPOCHS = 10
IMG_WIDTH = 30
IMG_HEIGHT = 30
NUM_CATEGORIES = 43
TEST_SIZE = 0.4


def main():

    # Check command-line arguments
    if len(sys.argv) not in [2, 3]:
        sys.exit("Usage: python traffic.py data_directory [model.h5]")

    # Get image arrays and labels for all image files
    images, labels = load_data(sys.argv[1])

    # Split data into training and testing sets
    labels = tf.keras.utils.to_categorical(labels)
    x_train, x_test, y_train, y_test = train_test_split(
        np.array(images), np.array(labels), test_size=TEST_SIZE
    )

    if len(sys.argv) == 3:
        # Get saved trained neural network
        filename = sys.argv[2]
        model = tf.keras.models.load_model(filename)
    else:
        # Get a new compiled neural network
        model = get_model()

    # Fit model on training data
    model.fit(x_train, y_train, epochs=EPOCHS)

    # Evaluate neural network performance
    model.evaluate(x_test,  y_test, verbose=2)

    # Save model to file
    if len(sys.argv) == 3:
        filename = sys.argv[2]
        model.save(filename)
        print(f"Model saved to {filename}.")


def load_data(data_dir):
    """
    Load image data from directory `data_dir`.

    Assume `data_dir` has one directory named after each category, numbered
    0 through NUM_CATEGORIES - 1. Inside each category directory will be some
    number of image files.

    Return tuple `(images, labels)`. `images` should be a list of all
    of the images in the data directory, where each image is formatted as a
    numpy ndarray with dimensions IMG_WIDTH x IMG_HEIGHT x 3. `labels` should
    be a list of integer labels, representing the categories for each of the
    corresponding `images`.
    """
    images = list()
    labels = list()
    
    for root, dirs, files in os.walk(data_dir):
        for filename in files:
            if filename.startswith('.'):
                continue
            filepath = root + os.sep + filename
            img = cv2.imread(filepath)
            img = cv2.resize(img, (IMG_WIDTH, IMG_HEIGHT))

            images.append(img)
            labels.append(root[(len(data_dir)+1):])

    return (images, labels)
    


def get_model():
    """
    Returns a compiled convolutional neural network model. Assume that the
    `input_shape` of the first layer is `(IMG_WIDTH, IMG_HEIGHT, 3)`.
    The output layer should have `NUM_CATEGORIES` units, one for each category.
    """
    model = tf.keras.models.Sequential([
        
        # Convolutional layer. Learn filters using a 3x3 kernel
        tf.keras.layers.Conv2D(
            36, (3,3), activation="relu", input_shape=(IMG_WIDTH, IMG_HEIGHT, 3)
        ),

        # Max-pooling layer, using 2x2 pool size 
        tf.keras.layers.MaxPooling2D(pool_size=(2,2)),

        # Convolutional layer. Learn filters using a 3x3 kernel
        tf.keras.layers.Conv2D(
            36, (3,3), activation="relu", input_shape=(IMG_WIDTH, IMG_HEIGHT, 3)
        ),

        # Max-pooling layer, using 2x2 pool size 
        tf.keras.layers.MaxPooling2D(pool_size=(2,2)),

        # Flatten units
        tf.keras.layers.Flatten(),

        # Add a hidden layer with dropout 
        tf.keras.layers.Dense(128, activation="relu"),
        tf.keras.layers.Dropout(0.4),

        # Add output layer with output units for all 43 signs
        tf.keras.layers.Dense(NUM_CATEGORIES, activation="softmax")
    ])

    model.compile(
        optimizer="adam",
        loss="categorical_crossentropy",
        metrics=["accuracy"]
    )
    
    return model


if __name__ == "__main__":
    main()
