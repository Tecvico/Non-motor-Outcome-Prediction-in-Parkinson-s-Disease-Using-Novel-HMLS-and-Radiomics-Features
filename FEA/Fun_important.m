function [importantFeatures]=Fun_important(SUmation)

for e=1:7
            there_selection6=SUmation>=e;  %%%%% Have to discuss
               jjj6=find(there_selection6~=0);
         importantFeatures(e).arr=jjj6;


end