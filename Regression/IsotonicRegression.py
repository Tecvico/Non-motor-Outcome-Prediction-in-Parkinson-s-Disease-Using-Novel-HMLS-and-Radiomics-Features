import sys
from sklearn.model_selection import GridSearchCV

from sklearn.model_selection import cross_validate

from sklearn.isotonic import IsotonicRegression
from RegressionMetrics  import RegressorMetrics 

def IsoReg(data, labels, nof ,file , filename):
    params = {
        # 'y_min': [sys.maxsize],
        # 'y_max': [-sys.maxsize-1],
        'out_of_bounds' : ['nan', 'clip', 'raise']
    }
    clf = GridSearchCV(IsotonicRegression(), params, n_jobs=-1, cv=nof)
    clf.fit(data, labels)
    best_parameters = clf.best_params_
    out_of_bounds = best_parameters['out_of_bounds']
    model = IsotonicRegression(out_of_bounds=out_of_bounds)

    r = RegressorMetrics()
    r.set_predictorName("KNeighborsRegressor")
    r.set_contin(False)
    r.set_DatasetName(filename)
    bestparameters = 'n_neighbors= ' +str(nn) + ' leaf_size= '+str(ls) + ' metric= '+str(me) + ' algorithm= '+str(alg)
    r.set_best(bestparameters)
    r.PrintbestParameters()

    cv_results = cross_validate(model, data, labels, cv=nof, scoring=r.scorer)
    r.PrintResults("MAE" , cv_results['test_MAE'])
    r.PrintResults("RMAE" , cv_results['test_RMAE'])
    r.PrintResults("MSE" , cv_results['test_MSE'])
    r.PrintResults("RMSE" , cv_results['test_RMSE'])
    r.PrintResults("RS" , cv_results['test_RS'])