
files = ["ResulACO" , "ResulDE" , "ResulPSO" , "ResulSA"];
for i=1 : size(files,2)
    nameFSA = files(1,i);
    PATH = 'Data\\'+nameFSA+'\\'+'Ranking.xlsx';
    ranking = readtable(PATH,'ReadVariableNames', false );
    ranking = table2array(ranking);
    PATH2 = 'Data\\'+nameFSA+'\\'+'ranking.mat';
    save(PATH2,'ranking')
    
end