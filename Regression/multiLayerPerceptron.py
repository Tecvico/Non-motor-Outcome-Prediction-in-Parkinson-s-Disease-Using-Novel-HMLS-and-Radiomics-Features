import sys
from sklearn.model_selection import GridSearchCV

from sklearn.model_selection import cross_validate

from sklearn.neural_network import MLPRegressor
from RegressionMetrics import RegressorMetrics

def MLP(data, labels, nof,file , filename ):
    params = {
        'solver': ['lbfgs', 'sgd', 'adam'],
        'activation' : ['identity', 'logistic', 'tanh', 'relu'],
        'alpha': [0.00001 ,0.0001 , 0.001, 0.01 , 0.5 , 1],
        'learning_rate' : ['constant', 'invscaling', 'adaptive'],
        'momentum' : [0.5 ,0.9 , 0.95 , 0.99]
        # 'solver': ['adam'],
        # 'activation' : [ 'relu'],
        # 'alpha': [0.0001 , 0.001, 0.01],
        # 'momentum' : [0.9 , 0.99]
    }
    clf = GridSearchCV(MLPRegressor(), params, n_jobs=-1, cv=nof)
    clf.fit(data, labels)
    best_parameters = clf.best_params_
    sol = best_parameters['solver']
    act = best_parameters['activation']
    alph = best_parameters['alpha']
    lr = best_parameters['learning_rate']
    mom = best_parameters['momentum']


    model = MLPRegressor(solver=sol  ,activation=act , alpha=alph  , momentum = mom , learning_rate=lr )
    # cvs = cross_val_score(model, data, labels, cv=nof)
    # print(cvs)
    # print(cvs.mean() , "\t" , cvs.std())

    r = RegressorMetrics()
    r.set_predictorName("MLPRegressor")
    r.set_contin(False)
    r.set_DatasetName(filename)
    bestparameters = 'solver= ' +str(sol) + ' activation= '+str(act) + ' alpha= '+str(alph) + ' learning_rate= '+str(lr) + ' momentum' + str(mom)
    r.set_best(bestparameters)
    r.PrintbestParameters()

    cv_results = cross_validate(model, data, labels, cv=nof, scoring=r.scorer, return_train_score = True)
    r.Print("MLPRegressor")
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

