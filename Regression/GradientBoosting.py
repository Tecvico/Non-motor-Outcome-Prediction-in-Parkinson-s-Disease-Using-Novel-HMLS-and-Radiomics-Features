import sys
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import cross_validate
from sklearn.ensemble import GradientBoostingRegressor
from RegressionMetrics import RegressorMetrics



def GradientBoosting(data, labels, nof ,file , filename):
    params = {
        'loss' : ['ls', 'lad', 'huber', 'quantile'],
        'n_estimators' : [10,50,100,200,500],
        'criterion' : ['friedman_mse', 'mse', 'mae'],
        'max_features':['auto', 'sqrt', 'log2'],
        # 'max_depth' : [1,2,3,5,10],
    }
    clf = GridSearchCV(GradientBoostingRegressor(), params, n_jobs=-1, cv=nof)
    clf.fit(data, labels)
    best_parameters = clf.best_params_
    ls = best_parameters['loss']
    ne = best_parameters['n_estimators']
    cr = best_parameters['criterion']
    mf = best_parameters['max_features']
    # md = best_parameters['max_depth']

    
    model = GradientBoostingRegressor(loss = ls , n_estimators=ne , criterion=cr ,max_features=mf)

    # model = GradientBoostingRegressor(loss = ls , n_estimators=ne , criterion=cr ,max_features=mf , max_depth=md)
    r = RegressorMetrics()
    r.set_predictorName("GradientBoostingRegressor")
    r.set_contin(False)
    r.set_DatasetName(filename)
    bestparameters = 'loss= ' +str(ls) + ' n_estimators= '+str(ne) + ' criterion= '+str(cr) + ' max_features= '+str(mf)
    r.set_best(bestparameters)
    r.PrintbestParameters()

    cv_results = cross_validate(model, data, labels, cv=nof, scoring=r.scorer, return_train_score = True)
    r.Print("GradientBoostingRegressor")
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