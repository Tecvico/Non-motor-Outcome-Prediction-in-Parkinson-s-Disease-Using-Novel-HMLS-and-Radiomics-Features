import sys
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import RandomizedSearchCV
from sklearn.model_selection import cross_validate
from sklearn.neighbors import KNeighborsRegressor
from RegressionMetrics import RegressorMetrics

def knn(data, labels, nof ,file , filename ,X_External, Y_External):
    params = {
        'n_neighbors': range(1, 51),
        'leaf_size': range(5, 65, 5),
        "metric": ["euclidean", "manhattan", "cityblock" , "minkowski"],
        'algorithm' : ['auto', 'ball_tree', 'kd_tree', 'brute']
    }
    clf = GridSearchCV(KNeighborsRegressor(), params, n_jobs=-1, cv=nof)
    clf.fit(data, labels)
    best_parameters = clf.best_params_
    nn = best_parameters['n_neighbors']
    ls = best_parameters['leaf_size']
    me = best_parameters['metric']
    alg = best_parameters['algorithm']

    # clf = RandomizedSearchCV(KNeighborsRegressor(), params, n_jobs=-1, cv=nof)
    # clf.fit(data, labels)
    # best_parameters = clf.best_params_
    # nn = best_parameters['n_neighbors']
    # ls = best_parameters['leaf_size']
    # me = best_parameters['metric']

    # print('n_neighbors= ' +str(nn) + ' leaf_size= '+str(ls) + ' metric= '+str(me) + ' algorithm= '+str(alg))
    model = KNeighborsRegressor(n_neighbors=nn , leaf_size=ls , metric=me , algorithm=alg)
    # model = KNeighborsRegressor(n_neighbors=1 , leaf_size=5 , metric='manhattan' , algorithm='auto')

    # cvs = cross_val_score(model, data, labels, cv=nof)
    # print(cvs)
    # print(cvs.mean() , "\t" , cvs.std())
    r = RegressorMetrics()
    r.set_predictorName("KNeighborsRegressor")
    r.set_contin(False)
    r.set_DatasetName(filename)
    bestparameters = 'n_neighbors= ' +str(nn) + ' leaf_size= '+str(ls) + ' metric= '+str(me) + ' algorithm= '+str(alg)
    r.set_best(bestparameters)
    r.PrintbestParameters()

    cv_results = cross_validate(model, data, labels, cv=nof, scoring=r.scorer, return_train_score = True)
    r.Print("KNeighborsRegressor")
    r.Print("test")
    # print(cv_results['test_MAE'])
    r.PrintResults("MAE" , cv_results['test_MAE'])
    r.PrintResults("RMAE" , cv_results['test_RMAE'])
    r.PrintResults("MSE" , cv_results['test_MSE'])
    r.PrintResults("RMSE" , cv_results['test_RMSE'])
    r.PrintResults("RS" , cv_results['test_RS'])
    r.Print("train")
    # print(cv_results['train_MAE'])
    r.PrintResults("MAE" , cv_results['train_MAE'])
    r.PrintResults("RMAE" , cv_results['train_RMAE'])
    r.PrintResults("MSE" , cv_results['train_MSE'])
    r.PrintResults("RMSE" , cv_results['train_RMSE'])
    r.PrintResults("RS" , cv_results['train_RS'])
    

    exResult = r.Externalscorer(model,X_External, Y_External)
    r.Print("External_test")
    # print(cv_results['train_MAE'])
    r.PrintResults("MAE" , cv_results['MAE'])
    r.PrintResults("RMAE" , cv_results['RMAE'])
    r.PrintResults("MSE" , cv_results['MSE'])
    r.PrintResults("RMSE" , cv_results['RMSE'])
    r.PrintResults("RS" , cv_results['RS'])