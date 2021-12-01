
function [X , Name_of_Fe_Redu] = Main_Feature_Reduction(data,Num_of_Fe_Redu,Num_features,k , POV , target)

Y = data ; 
%%%%%https://lvdmaaten.github.io/drtoolbox/

switch Num_of_Fe_Redu
    
    case 1
Y = pca(data, POV);
% Y = pca(data, Num_features);

    Name_of_Fe_Redu = 'pca';
    case 2
%     Y= kernel_pca(data, POV);%%%[mappedX, mapping] = kernel_pca(X, no_dims
 Y= kernel_pca(data, Num_features);%%%[mappedX, mapping] = kernel_pca(X, no_dims
       Name_of_Fe_Redu = 'kernel_pca';

%      case 3
%  [PC, net] = nlpca(data',20);%%%%MAX is 20 features
%  Y = (nlpca_get_components(net,data'))';

   
    case 3
Y = tsne(data,[],Num_features);
       Name_of_Fe_Redu = 'tsne';

    case 4
Y=fa(data,Num_features);
       Name_of_Fe_Redu = 'fa';

    case 5
Y=sammon(data,Num_features);
       Name_of_Fe_Redu = 'sammon';

    case 6
 Y=isomap(data,Num_features,k); %%%%[mappedX, mapping] = isomap(X, no_dims, k); that K is number of neighbor 
           Name_of_Fe_Redu = 'isomap';

    case 7
 Y = landmark_isomap(data, Num_features, k, 0.1); %%%%%%  [mappedX, mapping] = landmark_isomap(X, no_dims, k, percentage);
               Name_of_Fe_Redu = 'landmark_isomap';

    case 8
%   Y = laplacian_eigen(data, Num_features,k, 1, []);%   [mappedX, mapping] = laplacian_eigen(X, no_dims, k, sigma, eig_impl)
                    Name_of_Fe_Redu = 'laplacian_eigen';

    case 9
Y = lle(data, Num_features, k,[]); %%%%mappedX = lle(X, no_dims, k, eig_impl)
                   Name_of_Fe_Redu = 'lle';

%     case 10
% [centers,U] = fcm(data,Num_features);
%    Y = U';
%     case 12
% Y = ltsa(data, Num_features, k,1);%%%mappedX = ltsa(X, no_dims, k, eig_impl)
    
    case 10
Y = mds(data, Num_features);%%%%%mappedX = mds(X, no_dims);
                       Name_of_Fe_Redu = 'mds';

    case 11
Y = diffusion_maps(data, Num_features, 1, 1); %%%%mappedX = diffusion_maps(X, no_dims, alpha, sigma)&sigma is the variance of the Gaussian & The variable alpha
% determines the operator that is applied on the graph (default = 1)
                       Name_of_Fe_Redu = 'diffusion_maps';

    case 12
Y = spe(data, Num_features, 'Local', k);%   Y = spe(X, no_dims, 'Global')%   Y = spe(X, no_dims, 'Local', k)
                       Name_of_Fe_Redu = 'spe';
    
%     case 15
% Y = spe(data, 10, 'Global', k);%   Y = spe(X, no_dims, 'Global')%   Y = spe(X, no_dims, 'Local', k)

    case 13
 Y = gplvm(data, Num_features, 1);%%% Y = gplvm(X, no_dims, sigma)
                           Name_of_Fe_Redu = 'gplvm';

    case 14
 Y = sne(data, Num_features, 30);%%%  mappedX = sne(X, no_dims, perplexity)
                              Name_of_Fe_Redu = 'sne';

    case 15
 Y= sym_sne(data, Num_features, 30);%%%mappedX = sym_sne(X, no_dims, perplexity);
                                 Name_of_Fe_Redu = 'sym_sne';

    case 16
result= train_autoencoder(data',Num_features);
Subresult=result(1);
out=cell2mat(Subresult);
Y=out.W;
                          Name_of_Fe_Redu = 'autoencoder';
     case 17
%  Y= ProbPCA(data, Num_features, 30);
    Name_of_Fe_Redu = 'Probabilistic_PCA';

           case 18
 Y= lda(data,target ,  Num_features);
     Name_of_Fe_Redu = 'LDA';
case 19
%  Y= HessianLLE(data, Num_features, 30);
     Name_of_Fe_Redu = 'HessianLLE';
case 20
 Y= ltsa(data, Num_features, k);
         Name_of_Fe_Redu = 'LTSA';
case 21
%  Y= CCA(data,target ,  Num_features, 30);
                                 Name_of_Fe_Redu = 'Conformal_Eigenmaps';
case 22
%  Y= mvu(data, Num_features, 30);
                                 Name_of_Fe_Redu = 'Maximum_Variance_Unfolding';
case 23
 Y= lmvu(data, Num_features, k);
                                 Name_of_Fe_Redu = 'LandmarkMVU';
case 24
 Y= fastmvu(data, Num_features, k);
                                 Name_of_Fe_Redu = 'FastMVU';
case 25
%  Y= KernelLDA(data, Num_features, 30);
                                 Name_of_Fe_Redu = 'KernelLDA';
case 26
 Y= npe(data, Num_features, k);
             Name_of_Fe_Redu = 'NPE';
case 27
 Y= lpp(data, Num_features, k);
             Name_of_Fe_Redu = 'LPP';
case 28
 Y= lltsa(data, Num_features, k);
     Name_of_Fe_Redu = 'LLTSA';
case 29
 Y= llc(data,k ,  Num_features);
         Name_of_Fe_Redu = 'LLC';
case 30
%  Y= ManifoldChart(data, Num_features, 30);
     Name_of_Fe_Redu = 'ManifoldChart';
case 31
 Y= cfa(data, Num_features);
    Name_of_Fe_Redu = 'CFA';
case 32
 Y= nca(data,target ,  Num_features);
      Name_of_Fe_Redu = 'NCA';
case 33
 Y= mcml(data,target ,  Num_features);
       Name_of_Fe_Redu = 'MCML';
case 34
 Y= lmnn(data, target);
       Name_of_Fe_Redu = 'LMNN';
                      
                                 
end
X=Y;
end
