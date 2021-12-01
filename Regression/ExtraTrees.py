import sys
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import cross_validate
from sklearn.ensemble import ExtraTreesRegressor
from  RegressionMetrics  import RegressorMetrics 


def ExtraTreesReg(data, labels, nof ,file , filename):
    params = {
        'criterion' : ['mse', 'mae'] ,
        'max_features' : ['auto', 'sqrt', 'log2' ],
        'n_estimators' : [10,20,50,100,200],
        'max_depth' : [3,5,10,20,50,100,None]
    }
    clf = GridSearchCV(ExtraTreesRegressor(), params, n_jobs=-1, cv=nof)
    clf.fit(data, labels)
    best_parameters = clf.best_params_
    mf = best_parameters['max_features']
    ne = best_parameters['n_estimators']
    cr = best_parameters['criterion']
    md = best_parameters['max_depth']


    model = ExtraTreesRegressor( n_estimators= ne , max_features=mf , criterion=cr , max_depth=md)
    r = RegressorMetrics()
    r.set_predictorName("ExtraTreesRegressor")
    r.set_contin(False)
    r.set_DatasetName(filename)
    bestparameters = 'max_features= ' +str(mf) + ' n_estimators= '+str(ne) + ' criterion= '+str(cr) + ' max_depth= '+str(md)
    r.set_best(bestparameters)
    r.PrintbestParameters()

    cv_results = cross_validate(model, data, labels, cv=nof, scoring=r.scorer, return_train_score = True)
    r.Print("ExtraTreesRegressor")
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
