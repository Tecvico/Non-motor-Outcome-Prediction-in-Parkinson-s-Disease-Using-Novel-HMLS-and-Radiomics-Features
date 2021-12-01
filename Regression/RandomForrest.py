import sys
from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import cross_validate
from RegressionMetrics import RegressorMetrics


def RF(data, labels, nof ,file , filename):
    params = {
        'max_depth': range(1, 51),
        'min_samples_split': range(2, 11)
    }
    clf = GridSearchCV(RandomForestRegressor(), params, n_jobs=-1, cv=nof)
    clf.fit(data, labels)
    best_parameters = clf.best_params_
    md = best_parameters['max_depth']
    mss = best_parameters['min_samples_split']

    model = RandomForestRegressor( max_depth=md , min_samples_split=mss)

    r = RegressorMetrics()
    r.set_predictorName("RandomForestRegressor")
    r.set_contin(False)
    r.set_DatasetName(filename)
    bestparameters = 'max_depth= ' +str(md) + ' min_samples_split= '+str(mss)
    r.set_best(bestparameters)
    r.PrintbestParameters()

    cv_results = cross_validate(model, data, labels, cv=nof, scoring=r.scorer, return_train_score = True)
    r.Print("RandomForestRegressor")
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