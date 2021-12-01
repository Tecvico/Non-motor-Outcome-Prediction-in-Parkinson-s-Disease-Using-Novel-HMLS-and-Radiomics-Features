function [model]=lassoglm_Selector_Func(x,y)

opts = statset('UseParallel',true);

% Poisson Regression
[B,S] = lassoglm(x,y,'poisson','DFmax',100,'CV',10,'Alpha',0.5,'Options',opts);
model = B(:,S.Index1SE)~=0;
x=x(:,model);
end
