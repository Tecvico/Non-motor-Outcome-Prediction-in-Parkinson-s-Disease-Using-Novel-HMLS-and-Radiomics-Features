from sklearn.metrics import mean_squared_error
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import r2_score
import numpy as np
from numpy import mean
from numpy import std


class RegressorMetrics :
    def __init__(self, predictorName = '' , contin = False , DatasetName = '',best = ''):
        self.predictorName = predictorName
        self.contin = contin
        self.DatasetName = DatasetName
        self.best = best

    # getter method
    def get_best(self):
        return self._best
      
    # setter method
    def set_best(self, x):
        self._best = x

     # getter method
    def get_DatasetName(self):
        return self._DatasetName
      
    # setter method
    def set_DatasetName(self, x):
        self._DatasetName = x


    # getter method
    def get_predictorName(self):
        return self._predictorName
      
    # setter method
    def set_predictorName(self, x):
        self._predictorName = x


    # getter method
    def get_contin(self):
        return self._contin
      
    # setter method
    def set_contin(self, x):
        self._contin = x

    def scorer(self,clf, X, y):
        y_pred = clf.predict(X)
        

        AlgName = self.get_predictorName()
        FEA_FSA = self.get_DatasetName()
        filename = 'Predict//' + FEA_FSA +'//'+ AlgName + '.txt'
        file = open(filename, "a")

       
        c = 0 
        if self.get_contin() == False:
            for i in y:
                out = str(y[c])+ "\t" +str(y_pred[c]) + "\n"
                file.write(out)
                c= c+1
            self.set_contin(True)
        else:
            self.set_contin(False)

        file.close()  
    
        # result = np.sum(np.absolute(np.array(y_pred) - np.array(y)))
        # file = open("yp.txt", "a")
        # out = str(result) + '  ' + str(result/len(y_pred)) + '\n'
        # file.write(out)
        # file.close()

        MAE = mean_absolute_error(y, y_pred)
        RMAE = np.sqrt(mean_absolute_error(y, y_pred))
        MSE = mean_squared_error(y, y_pred)
        RMSE = np.sqrt(mean_squared_error(y, y_pred))
        RS = r2_score(y, y_pred)
        
        return {'MAE': MAE , 'RMAE': RMAE ,'MSE': MSE ,'RMSE': RMSE ,'RS': RS }

    def PrintResults(self , MetricName,res):
        Avg = mean(res)
        Std = std(res)
        out = MetricName + "\tmean : " + str(Avg)  +  "\tstd : "  +  str(Std) + "\n"
        print(MetricName,"\tmean : ",Avg , "\tstd : " , Std)
        file = open("Results.txt", "a")
        file.write(out)
        file.close()
    def Print(self , Name):
        out = Name + " : \n"
        print("\n"+Name+" : ")
        file = open("Results.txt", "a")
        file.write(out)
        file.close()   

    def PrintbestParameters(self):
        AlgName = self.get_predictorName()
        FEA_FSA = self.get_DatasetName()
        best = self.get_best()
        filename = 'Best_Parameters//' + FEA_FSA +'//'+ AlgName + '.txt'
        file = open(filename, "a")      
        file.write(best)
        file.close()  


    def Externalscorer(self,clf, X, y):
        y_pred = clf.predict(X)
        
        AlgName = self.get_predictorName()
        FEA_FSA = self.get_DatasetName()
        filename = 'External_Predict//' + FEA_FSA +'//'+ AlgName + '.txt'
        file = open(filename, "a")

       
        c = 0 
        for i in y:
            out = str(y[c])+ "\t" +str(y_pred[c]) + "\n"
            file.write(out)
            c= c+1
        file.close()  
    
        MAE = mean_absolute_error(y, y_pred)
        RMAE = np.sqrt(mean_absolute_error(y, y_pred))
        MSE = mean_squared_error(y, y_pred)
        RMSE = np.sqrt(mean_squared_error(y, y_pred))
        RS = r2_score(y, y_pred)
        
        return {'MAE': MAE , 'RMAE': RMAE ,'MSE': MSE ,'RMSE': RMSE ,'RS': RS }    