

% filename = "RF_CLI_GBAV4";
% f = filename + ".xlsx";
% data = readtable(f,'ReadVariableNames',true , 'Sheet', 'Data' );
% target = readtable(f,'ReadVariableNames',true , 'Sheet', 'Out' );
%
% data = table2array(data);
% target = table2array(target);
%
%
%
% Num_features=33;

%%
clc
clear all

filesExcel=dir('files\');
filesExcel(1:2)= [];

for jj=1 : size(filesExcel,1)
    
    filename = filesExcel(jj).name;
    savename = split(filename,'_');
    ss = savename{3}(1:end-5);
         
    f = ['files\' filename];
    
    try
        data = readtable(f,'ReadVariableNames',true , 'Sheet', 'Data' );
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
    

    Rankingpath = ['Data/Result_'  ss] ;
    files=dir(Rankingpath);
    files(1:2)= [];
    
        if mod(jj,2) == 1
        Num_features=17;
    else
        Num_features=19;
        end
    
    
        
    aa = 1:Num_features;
    
    
    for i=1 : size(files,1)
        nameFSA = files(i).name;
        PATH = [Rankingpath,'\',nameFSA,'\Ranking.mat'];
        load(PATH)
        
        
        if (size(ranking,2) == 1)
            ranking = ranking.';
        end
        
        features = ranking(:,1:Num_features);
        features = sort(features);
        if isequal(aa,features) == 0
            selected_data = data(:,features);
            
%             dirname='Reduced_Datasets';
%             mkdir(dirname);

              dirname='Reduced_Datasets';
                mkdir(dirname);

                dirname2= [dirname '/' ss] ;
                mkdir(dirname2);

    
            reducedFilename = dirname2 + "/" +nameFSA+".xlsx" ;
            %         xlswrite(reducedFilename,selected_data,'Data')
            %         xlswrite(reducedFilename,target,'Output')
            
            
            x = string(1:size(selected_data,2));
            var = strcat('X', x);
            T = array2table(selected_data,...
                'VariableNames',var);
            AA = [T T2 T3];
            writetable(AA,reducedFilename,'Sheet', 'Data')
            
        end
    end
end

