# this is for google colab mainly

# Mounting google drive to import files from drive
from google.colab import drive
drive.mount('/content/drive')



# Colab setup
!pip install -U -q PyDrive
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from google.colab import auth
from oauth2client.client import GoogleCredentials
# Authenticate and create the PyDrive client.
auth.authenticate_user()
gauth = GoogleAuth()
gauth.credentials = GoogleCredentials.get_application_default()
drive = GoogleDrive(gauth)

# initializing data directories - please give your local directory name in case you are running on local machine
DATA_DIR = '/content/drive/My Drive/Projects/ASHRAE/'
ROOT_DIR = '/content/'

# importing needed libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import lightgbm as lgb
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import KFold
import datetime
import gc
%pylab inline



