from sklearn.model_selection import GridSearchCV
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_validate
from  RegressionMetrics  import RegressorMetrics 


def LogisticReg(data, labels, nof ,file , filename):
    params = {
        'penalty': ['l1', 'l2', 'elasticnet', 'none'],
        'C': [0.1, 0.5, 1, 5, 10, 50, 100],
        'solver' : ['newton-cg', 'lbfgs', 'liblinear', 'sag', 'saga']
    }
    clf = GridSearchCV(LogisticRegression(), params, n_jobs=-1, cv=nof)
    clf.fit(data, labels)
    best_parameters = clf.best_params_
    pn = best_parameters['penalty']
    c = best_parameters['C']
    so = best_parameters['solver']

    model = LogisticRegression(penalty=pn ,C=c ,solver=so)
    
    r = RegressorMetrics()
    r.set_predictorName("LogisticRegression")
    r.set_contin(False)
    r.set_DatasetName(filename)
    bestparameters = 'solver' +str(so)
    r.set_best(bestparameters)
    r.PrintbestParameters()

    cv_results = cross_validate(model, data, labels, cv=nof, scoring=r.scorer, return_train_score = True)
    r.Print("LogisticRegression")
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