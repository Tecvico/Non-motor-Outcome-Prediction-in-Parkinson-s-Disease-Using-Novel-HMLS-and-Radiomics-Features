import sys
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import cross_validate
from sklearn.ensemble import BaggingRegressor
from sklearn.svm import SVR
from sklearn.tree import DecisionTreeRegressor
from  RegressionMetrics  import RegressorMetrics 

def BaggingReg(data, labels, nof ,file , filename):
    params = {
        'base_estimator': [ SVR() , DecisionTreeRegressor()],
        'n_estimators' : [3,5,10,20]
    }
    clf = GridSearchCV(BaggingRegressor(), params, n_jobs=-1, cv=nof)
    clf.fit(data, labels)
    best_parameters = clf.best_params_
    bs = best_parameters['base_estimator']
    ne = best_parameters['n_estimators']

    model = BaggingRegressor(base_estimator=bs , n_estimators= ne)
    r = RegressorMetrics()
    r.set_predictorName("BaggingRegressor")
    r.set_contin(False)
    r.set_DatasetName(filename)
    bestparameters = 'base_estimator= ' +str(bs) + ' n_estimators= '+str(ne)
    r.set_best(bestparameters)
    r.PrintbestParameters()

    cv_results = cross_validate(model, data, labels, cv=nof, scoring=r.scorer, return_train_score = True)
    r.Print("BaggingRegressor")
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
