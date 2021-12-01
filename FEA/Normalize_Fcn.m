function xN = Normalize_Fcn(x,Mean,Std)

% xN = (x - MinX) / (MaxX - MinX) * 2 - 1;
 xN = (x-Mean)./(Std);


% datatotal1=xlsread('Feature490.xlsx','Sheet1');


end