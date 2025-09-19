import os
from glob import glob
import numpy as np
from sklearn.model_selection import KFold,StratifiedKFold
import time  
import cv2
import keras
from keras.callbacks import CSVLogger, LearningRateScheduler, ModelCheckpoint
from keras.layers import *
from keras.models import Model, load_model
from keras.optimizers import Adam
from albumentations import *
from keras import backend as K
from skimage.feature import peak_local_max
from scipy import ndimage as ndi
from skimage.segmentation import watershed
import skimage.morphology
from skimage.io import imsave
from skimage.morphology import remove_small_objects
import tqdm
from random import shuffle 
import matplotlib.pyplot as plt
import pandas as pd
print('Chicken')