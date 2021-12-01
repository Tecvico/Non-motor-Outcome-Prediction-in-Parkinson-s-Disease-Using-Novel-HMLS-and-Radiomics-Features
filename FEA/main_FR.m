

%%%First open FSLib_v6.2.1_2018 in past folder and run
clc;
clear;
close all;



filename = 'F1_SEMI_TNMV4';
f = filename + ".xlsx";
try
    data = readtable(f,'ReadVariableNames',true , 'Sheet', 'Data' );  
%     target = readtable(f,'ReadVariableNames',true , 'Sheet', 'Output' ); 

    target = data(:,end);
    data = data(:,1:end-1);

catch
    disp(f);
end

data = table2array(data);
target = table2array(target);

x1=data;
Y=target;
x_no = x1;

%% 

dirname='Reduced_Datasets';
mkdir(dirname);

Num_features=89;

POV = 0.95;
K_neighber = 12;
for mm=1:1
    [SRdata , nameFRA ] = Main_Feature_Reduction(x_no,mm,Num_features,K_neighber , POV , Y);
   
    reducedFilename = dirname + "/" +nameFRA+".xlsx" ;

    xlswrite(reducedFilename,SRdata,'Data')
    xlswrite(reducedFilename,Y,'Output')

end

%% 

number_of_featureReduction = 16 ; 
Num_features=19;



%% 

dirname='Reduced_Datasets';
mkdir(dirname);

POV = 0.95;
K_neighber = 12;

for mm=2:number_of_featureReduction
    [SRdata , nameFRA ] = Main_Feature_Reduction(x_no,mm,Num_features,K_neighber , POV , Y);
   
    reducedFilename = dirname + "/" +nameFRA+".xlsx" ;
    xlswrite(reducedFilename,SRdata,'Data')
    xlswrite(reducedFilename,Y,'Output')
    
end

