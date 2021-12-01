import sys
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import cross_validate
from sklearn.svm import SVR
from RegressionMetrics import RegressorMetrics
from numpy import arange
from timeit import default_timer as timer    

# from numba import jit, cuda , float32
# @jit(target ="cuda")  
# @cuda.jit                          
def gen(x):
    out = []
    out.append(x)
    while(x < 1):
        x = x * 10
        out.append(x)

    x = 2
    out.append(x)
    while(x <= 10000):
        x = x * 2
        out.append(x)

    return out    
# def float_range(start, stop, step):
#   while start < stop:
#     yield float(start)
#     start += decimal.Decimal(step)


# @jit(target ="cuda") 
# @cuda.jit                          
def svmRbf(data, labels, nof ,file , filename):
    start = timer() 
    out = gen(0.00000001)
    params = {
        # 'C': out,
        'C': [0.1, 0.5, 1, 5, 10, 20],
        'gamma': arange(0.1 , 10.0 , 0.1),
        'kernel': ['rbf']
    }
    clf = GridSearchCV(SVR(), params, n_jobs=-1, cv=nof)
    clf.fit(data, labels)
    best_parameters = clf.best_params_
    c = best_parameters['C']
    gamma = best_parameters['gamma']


    model = SVR(C=c,kernel='rbf' , gamma= gamma)
    # cvs = cross_val_score(model, data, labels, cv=nof)
    # print(cvs)
    # print(cvs.mean() , "\t" , cvs.std())
    r = RegressorMetrics()
    r.set_predictorName("SVR_rbf")
    r.set_contin(False)
    r.set_DatasetName(filename)
    bestparameters = 'C= ' +str(c) + ' gamma= '+str(gamma)
    r.set_best(bestparameters)
    r.PrintbestParameters()

    cv_results = cross_validate(model, data, labels, cv=nof, scoring=r.scorer, return_train_score = True)
    r.Print("SVR_rbf")
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
    print("time:", timer()-start)   



    # file.write(str(cv_results['test_MAE']))
    # file.write(str(cv_results['test_RMAE']))
    # file.write(str(cv_results['test_MSE']))
    # file.write(str(cv_results['test_RMSE']))
    # file.write(str(cv_results['test_RS']))
