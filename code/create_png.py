import gzip
import numpy as np
from tqdm import tqdm
import matplotlib.pyplot as plt

def get_images(path):
    with gzip.open(path, 'r') as f:
        # first 4 bytes is a magic number
        magic_number = int.from_bytes(f.read(4), 'big')
        # second 4 bytes is the number of images
        image_count = int.from_bytes(f.read(4), 'big')
        # third 4 bytes is the row count
        row_count = int.from_bytes(f.read(4), 'big')
        # fourth 4 bytes is the column count
        column_count = int.from_bytes(f.read(4), 'big')
        # rest is the image pixel data, each pixel is stored as an unsigned byte
        # pixel values are 0 to 255
        image_data = f.read()
        images = np.frombuffer(image_data, dtype=np.uint8)\
            .reshape((image_count, row_count, column_count))
    return images


def get_labels(path):
    with gzip.open(path, 'r') as f:
        # first 4 bytes is a magic number
        magic_number = int.from_bytes(f.read(4), 'big')
        # second 4 bytes is the number of labels
        label_count = int.from_bytes(f.read(4), 'big')
        # rest is the label data, each label is stored as unsigned byte
        # label values are 0 to 9
        label_data = f.read()
        labels = np.frombuffer(label_data, dtype=np.uint8)
        return labels

train_images = get_images('emnist_byclass/raw/emnist-byclass-train-images-idx3-ubyte.gz')
train_labels = get_labels('emnist_byclass/raw/emnist-byclass-train-labels-idx1-ubyte.gz')

test_images = get_images('emnist_byclass/raw/emnist-byclass-test-images-idx3-ubyte.gz')
test_labels = get_labels('emnist_byclass/raw/emnist-byclass-test-labels-idx1-ubyte.gz')

print("Saving Train Images")
for i in tqdm(range(train_images.shape[0])):
    plt.imsave("emnist_byclass/Processed/train_images/"+str(i)+".png", train_images[i], cmap="gray")
np.savetxt("emnist_byclass/Processed/train_labels", train_labels, fmt='%s')

print("Saving Test Images")
for i in tqdm(range(test_images.shape[0])):
    plt.imsave("emnist_byclass/Processed/test_images/"+str(i)+".png", test_images[i], cmap="gray")
np.savetxt("emnist_byclass/Processed/test_labels", test_labels, fmt='%s')

print("Done")
