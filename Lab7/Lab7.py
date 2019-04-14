import numpy as np
import matplotlib.pyplot as plt
import pandas as pd 
from sklearn.svm import SVC
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.model_selection import train_test_split 
import warnings
warnings.filterwarnings('ignore')

def linear_svm():
    # download data set: https://drive.google.com/file/d/13nw-uRXPY8XIZQxKRNZ3yYlho-CYm_Qt/view
    # info: https://archive.ics.uci.edu/ml/datasets/banknote+authentication

    # load data
    bankdata = pd.read_csv(r"bill_authentication.csv")  

    # see the data
    bankdata.shape  

    # see head
    bankdata.head()  

    # data processing
    X = bankdata.drop('Class', axis=1)  
    y = bankdata['Class']  

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.20)  

    # train the SVM
    svclassifier = SVC(kernel='linear')  
    svclassifier.fit(X_train, y_train)  

    # predictions
    y_pred = svclassifier.predict(X_test)  
     
    # Evaluate model  
    print(confusion_matrix(y_test,y_pred))  
    print(classification_report(y_test,y_pred))  


# Iris dataset  https://archive.ics.uci.edu/ml/datasets/iris4
def import_iris():
    url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"

    # Assign colum names to the dataset
    colnames = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'Class']

    # Read dataset to pandas dataframe
    irisdata = pd.read_csv(url, names=colnames) 

    # process
    X = irisdata.drop('Class', axis=1)  
    y = irisdata['Class']  

    # train 
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.20)
    return X_train,X_test,y_train,y_test

def polynomial_kernel(X_train,X_test,y_train,y_test):
    # TODO
    # NOTE: use 8-degree in the degree hyperparameter. 
    # Trains, predicts and evaluates the model
    svclassifier = SVC(kernel='poly',degree=8)
    svclassifier.fit(X_train,y_train)
    y_pred = svclassifier.predict(X_test)
    print("POLYNOMIAL KERNEL")
    print(confusion_matrix(y_test,y_pred))
    print(classification_report(y_test,y_pred))
    print("________________________________________________________________")


def gaussian_kernel(X_train,X_test,y_train,y_test):
    # TODO
    # Trains, predicts and evaluates the model
    svclassifier = SVC(kernel='rbf')
    svclassifier.fit(X_train,y_train)
    y_pred = svclassifier.predict(X_test)
    print("GAUSSIAN KERNEL")
    print(confusion_matrix(y_test,y_pred))
    print(classification_report(y_test,y_pred))
    print("_________________________________________________________________")


def sigmoid_kernel(X_train,X_test,y_train,y_test):
    # TODO
    # Trains, predicts and evaluates the model
    svclassifier = SVC(kernel='sigmoid')
    svclassifier.fit(X_train,y_train)
    y_pred = svclassifier.predict(X_test)
    print("SIGMOID KERNEL")
    print(confusion_matrix(y_test,y_pred))
    print(classification_report(y_test,y_pred))
    print("__________________________________________________________________")

def test():
    X_train,X_test,y_train,y_test = import_iris()
    polynomial_kernel(X_train,X_test,y_train,y_test)
    gaussian_kernel(X_train,X_test,y_train,y_test)
    sigmoid_kernel(X_train,X_test,y_train,y_test)
    # NOTE: 3-point extra credit for plotting three kernel models.

test()
