import urllib.request
import gzip
import os
import shutil

# MNIST dataset URLs (from alternative working source)
urls = [
    'https://ossci-datasets.s3.amazonaws.com/mnist/train-images-idx3-ubyte.gz',
    'https://ossci-datasets.s3.amazonaws.com/mnist/train-labels-idx1-ubyte.gz',
    'https://ossci-datasets.s3.amazonaws.com/mnist/t10k-images-idx3-ubyte.gz',
    'https://ossci-datasets.s3.amazonaws.com/mnist/t10k-labels-idx1-ubyte.gz'
]

# Target folders
folders = [
    '1. K Nearest Neighbors/MNIST_Dataset_Loader/dataset/',
    '2. SVM/MNIST_Dataset_Loader/dataset/',
    '3. Random Forest Classifier/MNIST_Dataset_Loader/dataset/'
]

def download_and_extract(url, folder):
    filename = url.split('/')[-1]
    extracted = filename.replace('.gz', '')
    filepath = os.path.join(folder, filename)
    extractpath = os.path.join(folder, extracted)

    # Skip if already exists
    if os.path.exists(extractpath):
        print(f'Already exists: {extractpath}')
        return

    print(f'Downloading {filename}...')
    urllib.request.urlretrieve(url, filepath)

    print(f'Extracting {filename}...')
    with gzip.open(filepath, 'rb') as f_in:
        with open(extractpath, 'wb') as f_out:
            shutil.copyfileobj(f_in, f_out)

    # Remove the .gz file after extraction
    os.remove(filepath)
    print(f'Done: {extracted}\n')

# Create folders if they don't exist
for folder in folders:
    os.makedirs(folder, exist_ok=True)

# Download into each folder
for folder in folders:
    print(f'\n--- Downloading into {folder} ---')
    for url in urls:
        download_and_extract(url, folder)

print('\nAll datasets downloaded successfully!')
print('You can now run knn.py, svm.py, and RFC.py')