

%%%First open FSLib_v6.2.1_2018 in past folder and run
clc;
clear;
close all;


files=dir('files\');
files(1:2)= [];

for jj=1 : size(files,1)
    
    filename = files(jj).name;
    savename = split(filename,'_');
    ss = savename{3}(1:end-5);
    
    f = ['files\' filename];
    
    try
        data = readtable(f,'ReadVariableNames',true , 'Sheet', 'Data' );
        %     target = readtable(f,'ReadVariableNames',true , 'Sheet', 'Out' );
        %     asasa = data.Properties.VariableNames;
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
    

    dirname='Reduced_Datasets';
    mkdir(dirname);
    
    dirname2= [dirname '/' ss] ;
    mkdir(dirname2);
    
    Num_features=89;
    
    POV = 0.95;
    K_neighber = 12;
    for mm=1:1
        [SRdata , nameFRA ] = Main_Feature_Reduction(x_no,mm,Num_features,K_neighber , POV , Y);
        
        reducedFilename = dirname2 + "/" +nameFRA+".xlsx" ;
        
   %            xlswrite(reducedFilename,SRdata,'Data')
%     xlswrite(reducedFilename,Y,'Output')
         writematrix(SRdata,reducedFilename,'Sheet', 'Data')
        
        writematrix(Y,reducedFilename,'Sheet', 'Output')
 
  
    end
    

    number_of_featureReduction = 16 ;
    if mod(jj,2) == 1
        Num_features=17;
    else
        Num_features=19;
    end
    
    

    
    POV = 0.95;
    K_neighber = 12;
    for mm=2:number_of_featureReduction
        [SRdata , nameFRA ] = Main_Feature_Reduction(x_no,mm,Num_features,K_neighber , POV , Y);
        
        reducedFilename = dirname2 + "/" +nameFRA+".xlsx" ;
        %     xlswrite(reducedFilename,SRdata,'Data')
        %     xlswrite(reducedFilename,Y,'Output')
        
%            xlswrite(reducedFilename,SRdata,'Data')
%     xlswrite(reducedFilename,Y,'Output')
         writematrix(SRdata,reducedFilename,'Sheet', 'Data')
        
        writematrix(Y,reducedFilename,'Sheet', 'Output')
   
    end
end

