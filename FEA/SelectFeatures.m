

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

files=dir('Data\');
files(1:2)= [];
aa = 1:Num_features; 


for i=1 : size(files,1)
    nameFSA = files(i).name;
    PATH = ['Data\',nameFSA,'\Ranking.mat'];
    load(PATH);
      
    if (size(ranking,2) == 1)
        ranking = ranking.';
    end
    
    features = ranking(:,1:Num_features);
    features = sort(features);
    if isequal(aa,features) == 0
        selected_data = data(:,features);

        dirname='Reduced_Datasets';
        mkdir(dirname);

        reducedFilename = dirname + "/" +nameFSA+".xlsx" ;
        xlswrite(reducedFilename,selected_data,'Data')
        xlswrite(reducedFilename,target,'Output')
    
    end
end

