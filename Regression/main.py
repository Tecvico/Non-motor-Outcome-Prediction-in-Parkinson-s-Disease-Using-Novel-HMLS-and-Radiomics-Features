import numpy as np
from adaboost import adaboost
from DecisionTree import DT
from bagging import BaggingReg
from ExtraTrees import ExtraTreesReg
from GaussianProcess import GaussianProcessReg
from HistGradientBoosting import histGradientBoosting
from GradientBoosting import GradientBoosting
from KernelRidge import KRidge
from KNN import knn
from multiLayerPerceptron import MLP
from PLSRegression import PLSReg
from RandomForrest import  RF
from SGDRegressor import SGDReg
from svm_linear import svmLinear
from svm_Sigmoid import svmSigmoid
from svm_poly import svmpoly
from svm_RBF import svmRbf
from LinearRegression import LinearReg
from Polynomial import PolynomialReg
from TweedieRegressor import TweedieReg
from ARDRegression import ARDReg 
from BayesianRidge import BayesianRidgeReg
from ElasticNet import ElasticNetReg
from GammaRegressor import GammaReg
from HuberRegressor import HuberReg
from LARS import LarsReg
from Lasso import LassoReg
from LassoLARS import LassoLarsReg
from LogisticRegression import LogisticReg
from MultiTaskElasticNet import MultiTaskElasticNetReg
from MultiTaskLasso import MultiTaskLassoReg
from PassiveAggressiveRegressor import PassiveAggressiveReg
from Perceptron import PerceptronReg
from PLSRegression import PLSReg
from PoissonRegressor import PoissonReg
from RANSACRegressor import RANSACReg
from Ridge import RidgeReg
from TheilSenRegressor import TheilSenReg
import pandas as pd
from RegressionMetrics import RegressorMetrics
import os
from sklearn.utils import resample

Listfiles = os.listdir('Data/')
Listfile = []


# [0:29]   
# Listfile = Listfiles[0:29]
Listfile = Listfiles

for i in Listfile:
    filename = i
    path = 'Data//'+filename
    X2 = pd.read_excel(path , sheet_name='Data' , engine='openpyxl' ,header=None)
    X2 = X2.to_numpy()
    n_samples = X2.shape[0]
    n_features = X2.shape[1]

    Y2 = pd.read_excel(path, sheet_name='Output' , engine='openpyxl',header=None)
    Y2 = Y2.to_numpy().flatten()
    numberOfFold = 5

    file = open("Results.txt", "w")
    file.close()
    
    # X, Y = resample(X2, Y2 , replace=False,random_state=42 , stratify = Y2) 
    X, Y = resample(X2, Y2 , replace=False,random_state=42) 
    # X = X2.copy()
    # Y = Y2.copy()

    X, X_External, Y, Y_External = train_test_split(X, Y, test_size=0.20, random_state=42)

    dirName = "Best_Parameters"
    if not os.path.exists(dirName):
        os.mkdir(dirName) 
    dirName = "Predict"
    if not os.path.exists(dirName):
        os.mkdir(dirName) 
    dirName = "Results"
    if not os.path.exists(dirName):
        os.mkdir(dirName) 

    dirName = "External_Predict"
    if not os.path.exists(dirName):
        os.mkdir(dirName) 

    filename = filename.split('.')[0]
    
    dirName = "External_Predict//"+filename
    if not os.path.exists(dirName):
        os.mkdir(dirName)

    dirName = "Predict//"+filename
    if not os.path.exists(dirName):
        os.mkdir(dirName)

    dirName = "Best_Parameters//"+filename
    if not os.path.exists(dirName):
        os.mkdir(dirName)    
        
    adaboost(X,Y ,numberOfFold,file,filename)
    ARDReg(X,Y ,numberOfFold,file,filename)
    BaggingReg(X,Y ,numberOfFold,file,filename)
    BayesianRidgeReg(X,Y ,numberOfFold,file,filename)
    DT(X,Y ,numberOfFold,file,filename)
    ElasticNetReg(X,Y ,numberOfFold,file,filename)  
    ExtraTreesReg(X,Y ,numberOfFold,file,filename)
    # # # GammaReg(X,Y ,numberOfFold,file,filename)    #wrong
    GaussianProcessReg(X,Y ,numberOfFold,file,filename)
    GradientBoosting(X,Y ,numberOfFold,file,filename)
    PLSReg(X,Y ,numberOfFold,file,filename , min(n_samples, n_features) )
    histGradientBoosting(X,Y ,numberOfFold,file,filename)
    HuberReg(X,Y ,numberOfFold,file,filename)
    KRidge(X,Y ,numberOfFold,file,filename)
    knn(X,Y ,numberOfFold,file,filename , X_External, Y_External)
    # # LarsReg(X,Y ,numberOfFold,file,filename)
    LassoReg(X,Y ,numberOfFold,file,filename)
    LassoLarsReg(X,Y ,numberOfFold,file,filename)
    LinearReg(X,Y ,numberOfFold,file,filename)
    LogisticReg(X,Y ,numberOfFold,file,filename)   
    MLP(X,Y ,numberOfFold,file,filename)
    # # # MultiTaskElasticNetReg(X,Y ,numberOfFold,file,filename) #wrong
    # # # MultiTaskLassoReg(X,Y ,numberOfFold,file,filename)#wrong
    PassiveAggressiveReg(X,Y ,numberOfFold,file,filename)
    PerceptronReg(X,Y ,numberOfFold,file,filename)
    PoissonReg(X,Y ,numberOfFold,file,filename)
    # # PolynomialReg(X,Y ,numberOfFold,file,filename)
    RF(X,Y ,numberOfFold,file,filename)
    # # # RANSACReg(X,Y ,numberOfFold,file,filename) #wrong
    RidgeReg(X,Y ,numberOfFold,file,filename)
    SGDReg(X,Y ,numberOfFold,file,filename)
    svmLinear(X,Y ,numberOfFold,file,filename)
    svmpoly(X,Y ,numberOfFold,file,filename)
    svmRbf(X,Y ,numberOfFold,file,filename)
    svmSigmoid(X,Y ,numberOfFold,file,filename)
    TheilSenReg(X,Y ,numberOfFold,file,filename)
    TweedieReg(X,Y ,numberOfFold,file,filename)



    txtfile = 'Results//Result_'+filename + '.txt'
    with open('Results.txt','r') as firstfile, open(txtfile,'w') as secondfile:
        for line in firstfile:
            secondfile.write(line)



            