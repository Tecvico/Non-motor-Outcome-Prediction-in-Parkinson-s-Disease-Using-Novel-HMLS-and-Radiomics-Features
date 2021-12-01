import sys
from sklearn.model_selection import GridSearchCV

from sklearn.model_selection import cross_validate

from sklearn.linear_model import SGDRegressor
from RegressionMetrics import RegressorMetrics


def SGDReg(data, labels, nof ,file , filename):
    params = {
        'loss' : [ 'squared_loss', 'huber', 'epsilon_insensitive' , 'squared_epsilon_insensitive'],
        'penalty' : ['l2', 'l1', 'elasticnet'],
        # 'max_iter' : [100 , 500 ,1000],
        'learning_rate': ['constant' , 'optimal' , 'invscaling' , 'adaptive'],
    }
    clf = GridSearchCV(SGDRegressor(), params, n_jobs=-1, cv=nof)
    clf.fit(data, labels)
    best_parameters = clf.best_params_
    ls = best_parameters['loss']
    pe = best_parameters['penalty']
    # mi = best_parameters['max_iter']
    lr = best_parameters['learning_rate']
    model = SGDRegressor(loss=ls , penalty=pe ,learning_rate=lr)

    # model = SGDRegressor(loss=ls , penalty=pe ,max_iter=mi,learning_rate=lr)
    r = RegressorMetrics()
    r.set_predictorName("SGDRegressor")
    r.set_contin(False)
    r.set_DatasetName(filename)
    bestparameters = 'loss= ' +str(ls) + ' penalty= '+str(pe) + ' learning_rate= '+str(lr)
    r.set_best(bestparameters)
    r.PrintbestParameters()

    cv_results = cross_validate(model, data, labels, cv=nof, scoring=r.scorer, return_train_score = True)
    r.Print("SGDRegressor")
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
