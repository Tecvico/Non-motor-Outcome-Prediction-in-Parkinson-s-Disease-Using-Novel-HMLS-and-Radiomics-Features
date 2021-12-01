from sklearn.model_selection import GridSearchCV
from sklearn.linear_model import TweedieRegressor
from sklearn.model_selection import cross_validate
from  RegressionMetrics  import RegressorMetrics 


def TweedieReg(data, labels, nof ,file , filename):
    params = {
        'alpha': [0 , 0.001 , 0.005 , 0.01 , 0.05 , 0.1 , 0.5 ,0.9 ,1],
        'power': [0 ,1 ,2 ,3 ,4 ,5],
        'link' : ['auto', 'identity', 'log']
    }
    clf = GridSearchCV(TweedieRegressor(), params, n_jobs=-1, cv=nof)
    clf.fit(data, labels)
    best_parameters = clf.best_params_
    al = best_parameters['alpha']
    po = best_parameters['power']
    li = best_parameters['link']

    model = TweedieRegressor( power=po , alpha=al , link=li)
    
    r = RegressorMetrics()
    r.set_predictorName("TweedieRegressor")
    r.set_contin(False)
    r.set_DatasetName(filename)
    bestparameters = 'alpha= ' +str(al) + ' power= '+str(po) + ' link= '+str(li)
    r.set_best(bestparameters)
    r.PrintbestParameters()

    cv_results = cross_validate(model, data, labels, cv=nof, scoring=r.scorer, return_train_score = True)
    r.Print("TweedieRegressor")
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