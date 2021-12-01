function   [table_newa,table1] =Uniform_Func_Arash(Data_Se1,Data_Se2)

% table=zeros(3,3);
% for i=1:3
%     Data_Se1(i).arr=Data1(Data1(:,2)==i,:);
% end
%
% for j=1:3
%     Data_Se2(j).arr=Data2(Data2(:,2)==j,:);
% end

for k=1:size(Data_Se1,2)
    for kk=1:size(Data_Se2,2)
        count=0;
        temp1=Data_Se1(k).arr;
        temp2=Data_Se2(kk).arr;
        
        for s=1:size(temp1,1)
            for ss=1:size(temp2,1)
                
                if temp1(s,1)==temp2(ss,1) && temp1(s,2)==temp2(ss,2)
                    count=count+1;
                end
                
            end
        end
        
        count_per=count/size(temp1,1);
        table(k,kk)=count_per;
        
        
    end
end

tableneww=zeros(3,3);
table1=table.*10^3;
for i=1:3
    for j=1:3
        table1(i,j)=table1(i,j)+((i-1)*3)+j;
    end
end



p=perms([1 2 3]);
out=[0 0 0];
lastsum=0;
for i=1:size(p,1)
    temp=sum([table1(p(i,1),1) table1(p(i,2),2) table1(p(i,3),3)]);
    if temp>lastsum
        out=p(i,:);
        lastsum=temp;
    end
end

table_newa=zeros(3,3);
for hj=1:3
    table_newa(out(hj),hj)=table1(out(hj),hj)/1000;
end

for o=1:3
    for oo=1:3
        
        if table_newa(o,oo)>1
            table_newa(o,oo)=1;
        end
    end
end



end

% SUMtableclm=sum(tabl);
% [pc,ppc]=find (SUMtableclm==0);
% SUMtablerow=sum(tabl');
% [pr,ppr]=find (SUMtablerow==0);
% tabl(ppr,ppc)=table_ad(ppr,ppc);

% Cross=[];
% for j=1:3
%    [a b]= find(tabl==max(tabl(j,:)));
%    newpiar= Data_Se1(j).arr(:,1);
%    if tabl(a,b)>0.3
%    IDXnewar=b(1,1)*ones(size(newpiar,1),1);
%    IDXnew=[newpiar IDXnewar];
%    Cross=[Cross ;IDXnew];
%    else
%    IDXnewar=4*ones(size(newpiar,1),1);
%    IDXnew=[newpiar IDXnewar];
%    Cross=[Cross ;IDXnew];
% end
