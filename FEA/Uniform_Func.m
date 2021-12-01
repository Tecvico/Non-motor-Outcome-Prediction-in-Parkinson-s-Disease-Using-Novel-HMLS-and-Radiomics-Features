function   [table_newa,table1] =Uniform_Func(Data_Se1,Data_Se2)

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

% table
tableneww=zeros(3,3);
table1=table.*10^3;
for i=1:3
    for j=1:3
        table1(i,j)=table1(i,j)+((i-1)*3)+j;
    end
end


table_ad=table1;
tabl=zeros(3,3);
hh1=max(table_ad);
hh=hh1;
[a b]= find(table_ad==max(table_ad));
ar=zeros(3,1);
br=zeros(3,1);
% for k=1:3
%     [am bm]= find (hh1==(max(hh1)));
%     ar(k,1)=a(bm);
%     br(k,1)=b(bm);
%
%     hh1(am,bm)=0;
%     end

for mo=1:2
    
    
    for lk=1:3
        [aa bb]= find(table_ad(:,lk)==max(table_ad(:,lk)));
        a(lk,1)=aa(1);
        b(lk,1)=lk;
    end
    
     table_ad1=table_ad;
    ar=zeros(3,1);
    br=zeros(3,1);
    hh1=max(table_ad1);
    hh=hh1;
   
    for ku=1:3
        [am bm]= find (table_ad1==(max(max(table_ad1))));
        ar(ku,1)=am(1,1);
        br(ku,1)=bm(1,1);
        table_ad1(am(1,1),:)=0;
        table_ad1(:,bm(1,1))=0;
    end
    

    table_newa=zeros(3,3);
for hj=1:3
    table_newa(ar(hj),br(hj))=table_ad(ar(hj),br(hj));
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
end