# GradAdmit

GradAdmit requires a Python Environment for Machine Learning and Deep Learning.

Follow this [link](https://machinelearningmastery.com/setup-python-environment-machine-learning-deep-learning-anaconda/).

TLDR;

Download [Anaconda Navigator](https://www.anaconda.com/distribution/).

* After installation, open Anaconda Prompt.
* Confirm **conda** is installed correctly, by typing: conda -V

You should see the following:
conda 4.6.7

* Confirm Python is installed correctly by typing: python -V

You should see the following:
Python 3.6.7

* Confirm your conda environment is up-to-date, type: 
conda update conda
conda update anaconda

* Confirm Anaconda SciPy environment is up-to-date, type: conda update scikit-learn

* Confirm your SciPy environment, type: python versions.py

You should see the following:
scipy: 1.2.1
numpy: 1.16.2
matplotlib: 3.0.3
pandas: 0.24.1
statsmodels: 0.9.0
sklearn: 0.20.2

**Copy and Paste** the following code for **versions.py**:
# scipy
import scipy
print('scipy: %s' % scipy.__version__)
# numpy
import numpy
print('numpy: %s' % numpy.__version__)
# matplotlib
import matplotlib
print('matplotlib: %s' % matplotlib.__version__)
# pandas
import pandas
print('pandas: %s' % pandas.__version__)
# statsmodels
import statsmodels
print('statsmodels: %s' % statsmodels.__version__)
# scikit-learn
import sklearn
print('sklearn: %s' % sklearn.__version__)
