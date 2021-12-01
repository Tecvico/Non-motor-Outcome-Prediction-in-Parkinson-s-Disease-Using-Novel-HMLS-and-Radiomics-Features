function   [res] = Table_percent(TemptB_in_A,IDXs_GB_train)

for j=1:size(TemptB_in_A,2)
    for jj=1:size(IDXs_GB_train,2)
        Temptdata1=TemptB_in_A(j).arr;
        Temptdata2=IDXs_GB_train(jj).arr;
        count1=0;
        for k=1:size(Temptdata1,1)
            
            for kk=1:size(Temptdata2,1)
                if Temptdata1(k,1)==Temptdata2(kk,1)&& Temptdata1(k,2)==Temptdata2(kk,2)
                    count1=count1+1;
                end
            end
        end
        tableXY(j,jj)=count1/size(Temptdata2,1);
    end
    Temptdata1=[];
    Temptdata2=[];
    count1=0;
end

res=tableXY;

end