
filename = "Timeless_Version5";
f = filename + ".xlsx";
data = readtable(f,'ReadVariableNames',true , 'Sheet', 'Timeless' );  
target = readtable(f,'ReadVariableNames',true , 'Sheet', 'Output' ); 

Num_features=92;

%% 

% files = ["cfs" ,"fsasl","fsv","L0","laplacian" , "lasso","llcfs","mrmr" ,"relieff" ,"UDFS","ufsol" ];
files = ["mrmr" ];

for i=1 : size(files,2)
    nameFSA = files(1,i);
    PATH = 'Data\\'+nameFSA+'\\'+'Ranking.mat';
    load(PATH)
  
    if (size(ranking,2) == 1)
        ranking = ranking.';
    end
    
    features = ranking(:,1:Num_features);
    features = sort(features);
    selected_data = data(:,features);
    
    var = selected_data.Properties.VariableNames;

end

