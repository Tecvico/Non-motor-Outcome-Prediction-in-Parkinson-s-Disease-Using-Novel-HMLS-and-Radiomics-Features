import sys
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import cross_validate
from sklearn.ensemble import ExtraTreesRegressor
from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn.gaussian_process.kernels import RBF , ConstantKernel , WhiteKernel , Matern  , RationalQuadratic
from  RegressionMetrics  import RegressorMetrics 

def GaussianProcessReg(data, labels, nof ,file , filename):
    kernel = [RBF() , ConstantKernel() , WhiteKernel() , Matern() , RationalQuadratic() , None]
    params = {
        'kernel' : kernel 
    }
    clf = GridSearchCV(GaussianProcessRegressor(), params, n_jobs=-1, cv=nof)
    clf.fit(data, labels)
    best_parameters = clf.best_params_
    ke = best_parameters['kernel']

    model = GaussianProcessRegressor( kernel = ke)
   
    r = RegressorMetrics()
    r.set_predictorName("GaussianProcessRegressor")
    r.set_contin(False)
    r.set_DatasetName(filename)
    bestparameters = 'kernel= ' +str(ke)
    r.set_best(bestparameters)
    r.PrintbestParameters()

    cv_results = cross_validate(model, data, labels, cv=nof, scoring=r.scorer, return_train_score = True)
    r.Print("GaussianProcessRegressor")
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


#  r = RegressorMetrics()
#     cv_results = cross_validate(model, data, labels, cv=nof, scoring= r.scorer)
#     r.PrintResults("MAE" , cv_results['test_MAE'])
#     r.PrintResults("RMAE" , cv_results['test_RMAE'])
#     r.PrintResults("MSE" , cv_results['test_MSE'])
#     r.PrintResults("RMSE" , cv_results['test_RMSE'])
#     r.PrintResults("RS" , cv_results['test_RS'])


#     from  RegressionMetrics  import RegressorMetrics 
