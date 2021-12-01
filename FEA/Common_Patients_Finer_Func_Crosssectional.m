function  [Dataset0,Dataset1,target,out0,out1]= Common_Patients_Finer_Func_Crosssectional(data0,data1,output,Ot0,Ot1)

count=0;
R0=zeros(size(data0,1),1);
R1=zeros(size(data1,1),1);
R4=zeros(size(output,1),1);
for i=1:size(output,1)
    for j=1:size(data0,1)
        
        if (output(i,1)==data0(j,1))
            count=count+1;
            Labeled(count,1)=output(i,1);
        end
        
    end
end

count1=0;
for k=1:size(Labeled,1)
    for kk=1:size(data1,1)
        
        if (Labeled(k,1)==data1(kk,1))
            count1=count1+1;
            Labeledt(count1,1)=Labeled(k,1);
        end
        
    end
end




count=0;
for O0=1:size(Labeledt,1)
    for OO0=1:size(data0,1)
        
        if (Labeledt(O0,1)==data0(OO0,1))
            count=count+1;
            Dataset0(count,:)=data0(OO0,:);
              out0(count,:)=Ot0(OO0,:);
        end
    end
end



count=0;
for O0=1:size(Labeledt,1)
    for OO0=1:size(data1,1)
        
        if (Labeledt(O0,1)==data1(OO0,1))
            count=count+1;
            Dataset1(count,:)=data1(OO0,:);
            out1(count,:)=Ot1(OO0,:);
        end
    end
end



count=0;
for O0=1:size(Labeledt,1)
    for OO0=1:size(output,1)
        
        if (Labeledt(O0,1)==output(OO0,1))
            count=count+1;
            target(count,:)=output(OO0,:);
        end
    end
end

end