function [model]=lassoSelect(x, y)

opts = statset('UseParallel',true);
% Linear Regression
[B,S] = lasso(x,y,'DFmax',100,'CV',10,'Alpha',0.5,'Options',opts);

model = B(:,S.Index1SE)~=0;
% x=x(:,model);
end
