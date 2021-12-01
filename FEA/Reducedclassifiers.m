function[Table_reliability_Test]=classifiers(X,Y,No_of_folds,d)
addpath('../Classification_task')
i=1;
p=1;
o=1;
dd=1;
                    switch d
                        case 1
                            [TestResult,TrainResult]=Decision_TreeClassifiyer(X,Y,No_of_folds,i,p,o);
                            Table_reliability_Test(dd,o)=mean(TestResult.Accurtest);
                            Table_reliability_Train(dd,o)=mean(TrainResult.Accurtrain);
                            
                        case 2
                            [TestResult,TrainResult]=MultiLabel_SVM(X,Y,No_of_folds,i,p,o);
                            Table_reliability_Test(dd,o)=mean(TestResult.Accurtest);
                            Table_reliability_Train(dd,o)=mean(TrainResult.Accurtrain);
                            
%                         case 3
%                             [TestResult,TrainResult]=Naive_Bayes(X,Y,No_of_folds,i,p,o);
%                             Table_reliability_Test(dd,o)=mean(TestResult.Accurtest);
%                             Table_reliability_Train(dd,o)=mean(TrainResult.Accurtrain);
                            
                        case 3
                            [TestResult,TrainResult]=SetKNN(X,Y,No_of_folds,i,p,o);
                            Table_reliability_Test(dd,o)=mean(TestResult.Accurtest);
                            Table_reliability_Train(dd,o)=mean(TrainResult.Accurtrain);
%                             
                        case 4
                            [TestResult,TrainResult]=Ensemble(X,Y,No_of_folds,i,p,o);
                            Table_reliability_Test(dd,o)=mean(TestResult.Accurtest);
                            Table_reliability_Train(dd,o)=mean(TrainResult.Accurtrain);
                            
%                         case 4
%                             [TestResult,TrainResult]=ClassificationDiscriminant_class(X,Y,No_of_folds,i,p,o);
%                             Table_reliability_Test(dd,o)=mean(TestResult.Accurtest);
%                             Table_reliability_Train(dd,o)=mean(TrainResult.Accurtrain);
                            
                        case 5
                            [TestResult,TrainResult]=NEWPPN(X,Y,No_of_folds,i,p,o);
                            Table_reliability_Test(dd,o)=mean(TestResult.Accurtest);
                            Table_reliability_Train(dd,o)=mean(TrainResult.Accurtrain);
                            
                        case 6
                            [TestResult,TrainResult]=ClassificationECOC_class(X,Y,No_of_folds,i,p,o);
                            Table_reliability_Test(dd,o)=mean(TestResult.Accurtest);
                            Table_reliability_Train(dd,o)=mean(TrainResult.Accurtrain);
                            
                        case 7
                            [TestResult,TrainResult]=MLP(X,Y,No_of_folds,i,p,o)
                            Table_reliability_Test(dd,o)=mean(TestResult.Accurtest);
                            Table_reliability_Train(dd,o)=mean(TrainResult.Accurtrain);
                            
                        case 8
                            [TestResult,TrainResult]=SetRF(X,Y,No_of_folds,i,p,o);
                            Table_reliability_Test(dd,o)=mean(TestResult.Accurtest);
                            Table_reliability_Train(dd,o)=mean(TrainResult.Accurtrain);
                            
%                         case 9
%                             [TestResult,TrainResult]=RNN(X,Y,No_of_folds,i,p,o);
%                             Table_reliability_Test(dd,o)=mean(TestResult.Accurtest);
%                             Table_reliability_Train(dd,o)=mean(TrainResult.Accurtrain);
                            
%                         case 10
%                             [TestResult,TrainResult]= SetRBF(X,Y,No_of_folds,i,p,o);
%                             Table_reliability_Test(dd,o)=mean(TestResult.Accurtest);
%                             Table_reliability_Train(dd,o)=mean(TrainResult.Accurtrain);
%                             
%                         case 11
%                             [TestResult,TrainResult]=SetLolimat(X,Y,No_of_folds,i,p,o);
%                             Table_reliability_Test(dd,o)=mean(TestResult.Accurtest);
%                             Table_reliability_Train(dd,o)=mean(TrainResult.Accurtrain);
                            
                        case 9
                            [TestResult,TrainResult]=GaussianMLClassifier3(X,Y,No_of_folds,i,p,o);
                            Table_reliability_Test(dd,o)=mean(TestResult.Accurtest);
                            Table_reliability_Train(dd,o)=mean(TrainResult.Accurtrain);
                            
%                         case 13
%                             [TestResult,TrainResult]=GaussianMLClassifier2(X,Y,No_of_folds,i,p,o);
%                             Table_reliability_Test(dd,o)=mean(TestResult.Accurtest);
%                             Table_reliability_Train(dd,o)=mean(TrainResult.Accurtrain);
                            
%                         case 14
%                             [TestResult,TrainResult]=GaussianMLClassifier1(X,Y,No_of_folds,i,p,o);
%                             Table_reliability_Test(dd,o)=mean(TestResult.Accurtest);
%                             Table_reliability_Train(dd,o)=mean(TrainResult.Accurtrain);
                            
                       % case 17
                            % [TestResult,TrainResult]=SetANFISS(X(:,2:5),Y,i,No_of_folds,q,p,o);
                            % Table_reliability_Test(dd,o)=mean(TestResult.Accurtest);
                            %Table_reliability_Train(dd,o)=mean(TrainResult.Accurtrain);
                            %
%                         case 13
%                             [TestResult,TrainResult]=Fit_linear_regression_model(X,Y,No_of_folds,i,p,o);
%                             Table_reliability_Test(dd,o)=mean(TestResult.Accurtest);
%                             Table_reliability_Train(dd,o)=mean(TrainResult.Accurtrain);
%                             
%                         case 14
%                             [TestResult,TrainResult]=Gaussian_Reg(X,Y,No_of_folds,i,p,o);
%                             Table_reliability_Test(dd,o)=mean(TestResult.Accurtest);
%                             Table_reliability_Train(dd,o)=mean(TrainResult.Accurtrain);
                            

                            
                    end  %%%for switch

                end