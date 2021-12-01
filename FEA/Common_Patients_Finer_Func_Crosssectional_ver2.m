function  [Dataset0,Dataset1,target0,target1,T0,T1]= Common_Patients_Finer_Func_Crosssectional_ver2(data0,data1,output,O0,O1)

count=0;
for i=1:size(output,1)
    for j=1:size(data0,1)
        
        if (output(i,1)==data0(j,1))
            count=count+1;
            target0(count,:)=output(i,:);
            Dataset0(count,:)=data0(j,:);
            T0(count,:)=O0(j,:);
            
        end
        
    end
end

count=0;
for i=1:size(output,1)
    for j=1:size(data1,1)
        
        if (output(i,1)==data1(j,1))
            count=count+1;
            target1(count,:)=output(i,:);
            Dataset1(count,:)=data1(j,:);
            T1(count,:)=O1(j,:);
        end
        
    end
end


end