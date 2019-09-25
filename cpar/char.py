import gzip
import os
from urllib.request import urlretrieve

import numpy as np
from tqdm import tqdm

BASE_URL = "https://cpar.s3.amazonaws.com/"


def download_from_s3(file_name):
   
  download_url = BASE_URL + file_name
  save_path = os.path.join('data', file_name)
  urlretrieve(download_url, save_path)


def load_data(path=None):
    """Loads the cpar-char dataset.
    # Returns
        Tuple of Numpy arrays: `(x_train, y_train), (x_test, y_test)`.
    """
    files = ['char_train-labels-idx1-ubyte.gz', 'char_train-images-idx3-ubyte.gz', 
             'char_test-labels-idx1-ubyte.gz', 'char_test-images-idx3-ubyte.gz']
  
    paths = []
    if path is None:
      if os.path.isdir('data') is not True:
        os.mkdir('data')
      for fname in tqdm(files):
          if os.path.exists(os.path.join('data', fname)) is False:
            download_from_s3(fname)
          paths.append(fname)

    with gzip.open(os.path.join('data', paths[0]), 'rb') as lbpath:
        y_train = np.frombuffer(lbpath.read(), np.uint8, offset=8)

    with gzip.open(os.path.join('data', paths[1]), 'rb') as imgpath:
        x_train = np.frombuffer(imgpath.read(), np.uint8,
                                offset=16).reshape(len(y_train), 28, 28)

    with gzip.open(os.path.join('data', paths[2]), 'rb') as lbpath:
        y_test = np.frombuffer(lbpath.read(), np.uint8, offset=8)

    with gzip.open(os.path.join('data', paths[3]), 'rb') as imgpath:
        x_test = np.frombuffer(imgpath.read(), np.uint8,
                               offset=16).reshape(len(y_test), 28, 28)

    return (x_train, y_train), (x_test, y_test)
