# CPAR Dataset

## Introduction
#### CPAR Dataset consists of Devanagri(Hindi) Characters and Digits. This Dataset was collected by Mr. Rajiv Kumar.

## Quick Tour
CPAR contains 48 Characters and 9 Digits.

![alt rating_to_insight](https://github.com/gaganmanku96/CPAR/blob/master/assets/images/char.png)
![alt rating_to_insight](https://github.com/gaganmanku96/CPAR/blob/master/assets/images/digit.png)

## Installation
#### Using PIP via PyPI
```
$ pip install cpar
```
#### Manually via GIT
```
$ git clone git://github.com/gaganmanku96/cpar
$ cd cpar
$ python setup.py install
```

## Usage
#### Character Dataset
```
$ from cpar.char import load_data
$ (x_train, y_train), (x_test, y_test) = load_data()
```
#### Digit Dataset
```
$ from cpar.digit import load_data
$ (x_train, y_train), (x_test, y_test) = load_data()
```

## Citations
  1.  Kumar Rajiv, Amresh Kumar, and Pervez Ahmed. "A benchmark dataset for devnagari document recognition research." In 6th International Conference on Visualization, Imaging and Simulation (VIS'13), Lemesos, Cyprus, pp. 258-263. 2013.
  2. Kumar, Rajiv, and Kiran Kumar Ravulakollu. "HANDWRITTEN DEVNAGARI DIGIT RECOGNITION: BENCHMARKING ON NEW DATASET." Journal of theoretical & applied information technology 60, no. 3 (2014).
