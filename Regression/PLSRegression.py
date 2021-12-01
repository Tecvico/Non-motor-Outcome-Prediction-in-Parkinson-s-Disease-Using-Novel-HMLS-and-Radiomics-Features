import sys
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import cross_validate
from sklearn.cross_decomposition import PLSRegression
from RegressionMetrics import RegressorMetrics

def PLSReg(data, labels, nof ,file , filename, minimum):
    params = {
        'scale': [False , True],
        'max_iter' : [100 , 500 , 1000],
        'n_components' : range(1,2,minimum),
    }
    clf = GridSearchCV(PLSRegression(), params, n_jobs=-1, cv=nof)
    clf.fit(data, labels)
    best_parameters = clf.best_params_
    sc = best_parameters['scale']
    mi = best_parameters['max_iter']
    nc = best_parameters['n_components']

    model = PLSRegression( n_components=nc ,scale=sc ,max_iter=mi )
    # cvs = cross_val_score(model, data, labels, cv=nof)
    # print(cvs)
    # print(cvs.mean() , "\t" , cvs.std())
    r = RegressorMetrics()
    r.set_predictorName("PLSRegression")
    r.set_contin(False)
    r.set_DatasetName(filename)
    bestparameters = 'scale= ' +str(sc) + ' max_iter= '+str(mi) + ' n_components= '+str(nc)
    r.set_best(bestparameters)
    r.PrintbestParameters()

    cv_results = cross_validate(model, data, labels, cv=nof, scoring=r.scorer, return_train_score = True)
    r.Print("PLSRegression")
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

