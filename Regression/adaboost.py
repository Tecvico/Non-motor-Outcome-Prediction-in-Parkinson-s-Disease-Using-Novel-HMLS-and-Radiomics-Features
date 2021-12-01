from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import RandomizedSearchCV
from sklearn.model_selection import cross_validate
from sklearn.ensemble import AdaBoostRegressor , RandomForestRegressor , ExtraTreesRegressor
from sklearn.svm import SVR
from sklearn.tree import DecisionTreeRegressor
from  RegressionMetrics  import RegressorMetrics 

def adaboost(data, labels, nof ,file , filename):
    # base_models = [
    #     ExtraTreesRegressor(criterion='mae'),  
    #     RandomForestRegressor(),
    #     SVR(kernel='rbf'),
    #     DecisionTreeRegressor()]  
    base_models = [
        SVR(kernel='rbf'),
        DecisionTreeRegressor()]  
    params = {
        'base_estimator': base_models,
        'n_estimators' : [10,20,50,100,200,400],
        'loss' : ['linear', 'square', 'exponential']
    }
    clf = GridSearchCV(AdaBoostRegressor(), params, n_jobs=-1, cv=nof)
    clf.fit(data, labels)
    best_parameters = clf.best_params_

    bs = best_parameters['base_estimator']
    ne = best_parameters['n_estimators']
    loss = best_parameters['loss']
    # print('base_estimator= ' +str(bs) + ' n_estimators= '+str(ne) + ' loss= '+str(loss))
    model = AdaBoostRegressor(base_estimator=bs , n_estimators= ne , loss = loss)

    r = RegressorMetrics()
    r.set_predictorName("AdaBoostRegressor")
    r.set_contin(False)
    r.set_DatasetName(filename)

    bestparameters = 'base_estimator= ' +str(bs) + ' n_estimators= '+str(ne) + ' loss= '+str(loss)
    r.set_best(bestparameters)
    r.PrintbestParameters()  
      
    cv_results = cross_validate(model, data, labels, cv=nof, scoring= r.scorer, return_train_score = True)
    
    r.Print("AdaBoostRegressor")
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



    # params = {
    #     'base_estimator': [ SVR() , DecisionTreeRegressor()],
    #     'n_estimators' : range(1 , 10000),
    #     'loss' : ['linear', 'square', 'exponential']
    # }
    # clf = RandomizedSearchCV(AdaBoostRegressor(), params, n_jobs=-1, cv=nof)
    # clf.fit(data, labels)
    # best_parameters = clf.best_params_


    # bs = best_parameters['base_estimator']
    # ne = best_parameters['n_estimators']
    # loss = best_parameters['loss']
    # model = AdaBoostRegressor(base_estimator=bs , n_estimators= ne , loss = loss)

    # r = RegressorMetrics()
    # cv_results = cross_validate(model, data, labels, cv=nof, scoring= r.scorer)
    # r.PrintResults("MAE" , cv_results['test_MAE'])
    # r.PrintResults("RMAE" , cv_results['test_RMAE'])
    # r.PrintResults("MSE" , cv_results['test_MSE'])
    # r.PrintResults("RMSE" , cv_results['test_RMSE'])
    # r.PrintResults("RS" , cv_results['test_RS'])