from sklearn.model_selection import GridSearchCV
from sklearn.preprocessing import PolynomialFeatures
from sklearn.model_selection import cross_validate
from  RegressionMetrics  import RegressorMetrics 
from sklearn.linear_model import Ridge
from sklearn.pipeline import make_pipeline

def PolynomialReg(data, labels, nof ,file , filename):
    return 0 
    # params = {
    #     'degree': [2 , 3 , 4 ,5 , 6 ,7]
    # }
    # clf = GridSearchCV(PolynomialFeatures(), params, n_jobs=-1, cv=nof)
    # clf.fit(data, labels)
    # best_parameters = clf.best_params_
    # de = best_parameters['degree']

    # model = PolynomialFeatures(degree=de)


    # degree =  [2 , 3 , 4 ,5 , 6 ,7]

    # for d in degree:
    #     model = make_pipeline(PolynomialFeatures(d), Ridge())
    #     model.fit(data, labels)
    #     y_plot = model.predict(data)
        # r = RegressorMetrics()
        # cv_results = cross_validate(model, data, labels, cv=nof, scoring=r.scorer)
        # print(d)
        # r.PrintResults("MAE" , cv_results['test_MAE'])
        # r.PrintResults("RMAE" , cv_results['test_RMAE'])
        # r.PrintResults("MSE" , cv_results['test_MSE'])
        # r.PrintResults("RMSE" , cv_results['test_RMSE'])
        # r.PrintResults("RS" , cv_results['test_RS'])


    
    # r = RegressorMetrics()
    # cv_results = cross_validate(model, data, labels, cv=nof, scoring=r.scorer, return_train_score = True)
    # r.Print("PolynomialFeatures")
    # r.Print("train")
    # r.PrintResults("MAE" , cv_results['test_MAE'])
    # r.PrintResults("RMAE" , cv_results['test_RMAE'])
    # r.PrintResults("MSE" , cv_results['test_MSE'])
    # r.PrintResults("RMSE" , cv_results['test_RMSE'])
    # r.PrintResults("RS" , cv_results['test_RS'])
    # r.Print("test")
    # r.PrintResults("MAE" , cv_results['train_MAE'])
    # r.PrintResults("RMAE" , cv_results['train_RMAE'])
    # r.PrintResults("MSE" , cv_results['train_MSE'])
    # r.PrintResults("RMSE" , cv_results['train_RMSE'])
    # r.PrintResults("RS" , cv_results['train_RS'])

    
    # file.write(str(cv_results['test_MAE']))
    # file.write(str(cv_results['test_RMAE']))
    # file.write(str(cv_results['test_MSE']))
    # file.write(str(cv_results['test_RMSE']))
    # file.write(str(cv_results['test_RS']))