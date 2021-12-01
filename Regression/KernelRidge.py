import sys
from sklearn.model_selection import GridSearchCV
import numpy as np
from sklearn.model_selection import cross_validate
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import KFold
from sklearn import preprocessing
from sklearn.model_selection import KFold
from scipy.optimize import differential_evolution
from sklearn.kernel_ridge import KernelRidge 
from RegressionMetrics  import RegressorMetrics 

# def KRR_function(hyperparams,X,y):
#     # Assign hyper-parameters
#     alpha_value,gamma_value = hyperparams
#     # Split data into test and train: random state fixed for reproducibility
#     kf = KFold(n_splits=5)
#     y_pred_total = []
#     y_test_total = []
#     # kf-fold cross-validation loop
#     for train_index, test_index in kf.split(X):
#         X_train, X_test = X[train_index], X[test_index]
#         y_train, y_test = y[train_index], y[test_index]

#         # Fit KRR with (X_train_scaled, y_train), and predict X_test_scaled
#         KRR = KernelRidge(kernel='rbf',alpha=alpha_value,gamma=gamma_value)
#         y_pred = KRR.fit(X_train, y_train).predict(X_test)
#         # Append y_pred and y_test values of this k-fold step to list with total values
#         y_pred_total.append(y_pred)
#         y_test_total.append(y_test)
#     # Flatten lists with test and predicted values
#     y_pred_total = [item for sublist in y_pred_total for item in sublist]
#     y_test_total = [item for sublist in y_test_total for item in sublist]
#     # Calculate error metric of test and predicted values: rmse
#     mae = mean_absolute_error(y_test_total, y_pred_total)
#     #print('alpha: %.6f . gamma: %.6f . rmse: %.6f' %(alpha_value,gamma_value,rmse)) # Uncomment to print intermediate results
#     return mae

def KRidge(data, labels, nof ,file , filename):
    params = {
        'kernel': ['rbf' , 'linear' , 'poly']
    }
    clf = GridSearchCV(KernelRidge(), params, n_jobs=-1, cv=nof)
    clf.fit(data, labels)
    best_parameters = clf.best_params_
    KE = best_parameters['kernel']


    model = KernelRidge(kernel=KE)
    # cvs = cross_val_score(model, data, labels, cv=nof)
    # print(cvs)
    # print(cvs.mean() , "\t" , cvs.std())

    r = RegressorMetrics()
    r.set_predictorName("KernelRidge")
    r.set_contin(False)
    r.set_DatasetName(filename)
    bestparameters = 'kernel= ' +str(KE)
    r.set_best(bestparameters)
    r.PrintbestParameters()

    cv_results = cross_validate(model, data, labels, cv=nof, scoring=r.scorer, return_train_score = True)
    r.Print("KernelRidge")
    r.Print("test")
    r.PrintResults("MAE" , cv_results['test_MAE'])
    r.PrintResults("RMAE" , cv_results['test_RMAE'])
    r.PrintResults("MSE" , cv_results['test_MSE'])
    r.PrintResults("RMSE" , cv_results['test_RMSE'])
    r.PrintResults("RS" , cv_results['test_RS'])
    r.Print("train")
    r.PrintResults("MAE" , cv_results['train_MAE'])
    r.PrintResults("RMAE" , cv_results['train_RMAE'])
    r.PrintResults("MSE" , cv_results['train_MSE'])
    r.PrintResults("RMSE" , cv_results['train_RMSE'])
    r.PrintResults("RS" , cv_results['train_RS'])

    
    # file.write(str(cv_results['test_MAE']))
    # file.write(str(cv_results['test_RMAE']))
    # file.write(str(cv_results['test_MSE']))
    # file.write(str(cv_results['test_RMSE']))
    # file.write(str(cv_results['test_RS']))
    


    # KRR_alpha_lim = (0.00001,100.0)
    # KRR_gamma_lim = (0.00001,20.0)
    # boundaries = [KRR_alpha_lim] + [KRR_gamma_lim]
    # extra_variables = (data, labels)
    # solver = differential_evolution(KRR_function,boundaries,args=extra_variables,strategy='best1bin',
    #                                 popsize=15,mutation=0.5,recombination=0.7,tol=0.01)
    # best_hyperparams = solver.x
    # best_mae = solver.fun
    # print("Converged hyperparameters: alpha= %.6f, gamma= %.6f" %(best_hyperparams[0],best_hyperparams[1]))    
    # print("Minimum mae: %.6f" %(best_mae))