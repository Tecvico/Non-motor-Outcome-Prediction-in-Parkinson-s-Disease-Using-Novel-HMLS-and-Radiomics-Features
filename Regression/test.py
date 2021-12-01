import numpy as np
# from adaboost import adaboost
# from DecisionTree import DT
# from bagging import BaggingReg
# from ExtraTrees import ExtraTreesReg
# from GaussianProcess import GaussianProcessReg
# from HistGradientBoosting import histGradientBoosting
# from GradientBoosting import GradientBoosting
# from KernelRidge import KRidge
from KNN import knn
# from multiLayerPerceptron import MLP
# from PLSRegression import PLSReg
# from RandomForrest import  RF
# from SGDRegressor import SGDReg
# from svm_linear import svmLinear
# from svm_Sigmoid import svmSigmoid
# from svm_poly import svmpoly
# from svm_RBF import svmRbf
# from LinearRegression import LinearReg
# from Polynomial import PolynomialReg
# from TweedieRegressor import TweedieReg
# from ARDRegression import ARDReg 
# from BayesianRidge import BayesianRidgeReg
# from ElasticNet import ElasticNetReg
# from GammaRegressor import GammaReg
# from HuberRegressor import HuberReg
# from LARS import LarsReg
# from Lasso import LassoReg
# from LassoLARS import LassoLarsReg
# from LogisticRegression import LogisticReg
# from MultiTaskElasticNet import MultiTaskElasticNetReg
# from MultiTaskLasso import MultiTaskLassoReg
# from PassiveAggressiveRegressor import PassiveAggressiveReg
# from Perceptron import PerceptronReg
# from PLSRegression import PLSReg
# from PoissonRegressor import PoissonReg
# from RANSACRegressor import RANSACReg
# from Ridge import RidgeReg
# from TheilSenRegressor import TheilSenReg
from RegressionMetrics import RegressorMetrics
from sklearn.model_selection import train_test_split
import pandas as pd
from sklearn.metrics import mean_absolute_error
from sklearn.neighbors import KNeighborsRegressor
from sklearn.model_selection import cross_validate
import os

Listfiles = os.listdir('Data/')
Listfile = []


# mrmr
Listfile = Listfiles[0:1]

for i in Listfile:
    filename = i
    path = 'Data//'+filename
    X = pd.read_excel(path , sheet_name='Data' , engine='openpyxl' ,header=None)
    X = X.to_numpy()
    n_samples = X.shape[0]
    n_features = X.shape[1]

    Y = pd.read_excel(path, sheet_name='Output' , engine='openpyxl',header=None)
    Y = Y.to_numpy().flatten()
    numberOfFold = 5

    file = open("Results.txt", "w")
    file.close()

    # print('knn***************************')
    # knn(X,Y ,numberOfFold,file)

    n_neighbors= 1 
    leaf_size= 5 
    metric= 'manhattan' 
    algorithm= 'auto'
    model = KNeighborsRegressor(n_neighbors=n_neighbors , leaf_size=leaf_size , metric=metric , algorithm=algorithm)

    maxSplit = 10
    for spl in range(1, maxSplit+1):
        Nosplit = spl
        df_split_X = np.array_split(X, Nosplit)
        df_split_Y = np.array_split(Y, Nosplit)

        MAE = np.zeros(Nosplit)
        for j in range(0, Nosplit):
            # X_train, X_test, y_train, y_test = train_test_split(df_split_X[j], df_split_Y[j], test_size=0.30 , shuffle=True)
            # model.fit(X_train, y_train)
            # y_pred = model.predict(X_test)
            # MAE[j] = mean_absolute_error(y_test, y_pred)
            # print(MAE[j])


            r = RegressorMetrics()
            cv_results = cross_validate(model, df_split_X[j], df_split_Y[j], cv=5, scoring=r.scorer )
            # print('mean : ',np.mean(cv_results['test_MAE']))
            MAE[j] = np.mean(cv_results['test_MAE'])
            # # print(MAE[j])

        print('mean : ',np.mean(MAE))  
        print('std : ',np.std(MAE))  

        print('Nosplit : ',Nosplit,'************************\n')  

        # print(np.std(MAE))      