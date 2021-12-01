

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
        deathname = data.Properties.VariableNames(end-1);
        targetname = data.Properties.VariableNames(end);
        target = data(:,end);
        death = data(:,end-1);
        
        data = data(:,1:end-2);
        
        
    catch
        disp(f);
    end
    death = table2array(death);
    data = table2array(data);
    target = table2array(target);
    
    x1=data;
    Y=target;
    x_no = x1;
    
    T2 = array2table(death,...
        'VariableNames',{deathname{1}});
    
    T3 = array2table(Y,...
        'VariableNames',{targetname{1}});
    
    
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
        
        
        x = string(1:size(SRdata,2));
        var = strcat('X', x);
        
        T = array2table(SRdata,...
            'VariableNames',var);
        
        
        
        AA = [T T2 T3];
        
        %     xlswrite(reducedFilename,AA,'Data')
        writetable(AA,reducedFilename,'Sheet', 'Data')
        
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
        
        
        x = string(1:size(SRdata,2));
        var = strcat('X', x);
        T = array2table(SRdata,...
            'VariableNames',var);
        AA = [T T2 T3];
        writetable(AA,reducedFilename,'Sheet', 'Data')
        
    end
end

