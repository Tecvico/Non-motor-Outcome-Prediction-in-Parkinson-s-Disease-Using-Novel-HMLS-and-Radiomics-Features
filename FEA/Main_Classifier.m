

%%%First open FSLib_v6.2.1_2018 in past folder and run
clc;
clear;
close all;

% files = ["ILFS" , "mrmr" , "RelifA" , "laplacian" , "UDFS" , "llcfs","cfs" , "FSASL" , "UFSOL","Lasso", "autoencoder" ,"diffusion_maps" ,"fa" ,"gplvm" ,"isomap" ,"kernel_pca" ,"landmark_isomap","lle" , "mds" ,"pca" ,"sammon" ,"sne" ,"spe" ,"sym_sne" ,"tsne" ];
files = ["Lasso"];

NUM_File=size(files,2);

   distype=1; %%%Euclidean distance=1,Pearson correlation=2};
    Num_Evalua=1;
    neighbour=15;
    
NumFolds=5;
NumberOfClassifications=12;
Num_features=83;
    Table_reliability_Test=zeros(NumberOfClassifications,NUM_File);
    Table_reliability_Train=zeros(NumberOfClassifications,NUM_File);
  
for i=1:NUM_File
    o = i ;
    name = files(1,i);
    filename = 'Dataset\\'+name;
f = filename + ".xlsx";
try
    data = readtable(f,'ReadVariableNames',false , 'Sheet', 'Data' );  
    target = readtable(f,'ReadVariableNames',false , 'Sheet', 'Output' ); 
    %
catch
    disp(f);
end
data = table2array(data);
target = table2array(target);

x1=data;
Y=target;
x_no = x1;

SRdata = x_no;

    for oo=1:NumberOfClassifications
%         try
            [TestResult,TestSTD,trnResult,trnSTD]=classifiers(SRdata,Y,NumFolds,oo,i);
            table_acc(i,oo)=TestResult;
            table_STD(i,oo)=TestSTD;
            table_acc_trn(i,oo)=trnResult;
            table_STD_trn(i,oo)=trnSTD;
            TableACC_allSR(i).arr=table_acc;
            TableSTD_allSR(i).arr=table_STD;
            TableACC_allSR_trn(i).arr=table_acc_trn;
            TableSTD_allSR_trn(i).arr=table_STD_trn;
            
%         catch
%         end
        
    end
    
    %% 
    
    dirname='Timeless_Result_Classifiers_5folds_1';
    mkdir(dirname);
    ffname1=strcat(dirname,'/TableACC_allSR.mat');
    ffname2=strcat(dirname,'/TableSTD_allSR.mat');
    ffname3=strcat(dirname,'/TableACC_allSR_trn.mat');
    ffname4=strcat(dirname,'/TableSTD_allSR_trn.mat');
%     save TableACC_allSR
%     save TableSTD_allSR
%     save TableACC_allSR_trn
%     save TableSTD_allSR_trn
    save(ffname1);
    save(ffname2);
    save(ffname3);
    save(ffname4);
    
    clc;
    
    
end


