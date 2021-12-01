import sys
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import cross_validate
from sklearn.experimental import enable_hist_gradient_boosting
from sklearn.ensemble import HistGradientBoostingRegressor
from RegressionMetrics  import RegressorMetrics 

def histGradientBoosting(data, labels, nof,file , filename ):
    params = {
        'loss' : ['least_squares', 'least_absolute_deviation', 'poisson'],
        # 'max_iter' : [50,100,200],
        # 'early_stopping' : ['auto' , False , True],
    }
    clf = GridSearchCV(HistGradientBoostingRegressor(), params, n_jobs=-1, cv=nof)
    clf.fit(data, labels)
    best_parameters = clf.best_params_
    ls = best_parameters['loss']
    # mi = best_parameters['max_iter']
    # es = best_parameters['early_stopping']
    model = HistGradientBoostingRegressor(loss = ls)

    # model = HistGradientBoostingRegressor(loss = ls , max_iter=mi , early_stopping = es)
    r = RegressorMetrics()
    r.set_predictorName("HistGradientBoostingRegressor")
    r.set_contin(False)
    r.set_DatasetName(filename)
    bestparameters = 'loss= ' +str(ls)
    r.set_best(bestparameters)
    r.PrintbestParameters()

    cv_results = cross_validate(model, data, labels, cv=nof, scoring=r.scorer, return_train_score = True)
    r.Print("HistGradientBoostingRegressor")
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