function  [DataMRI_time_New,DataMRI_Cross_New]= Common_Patients_Finer_Func_timeless(DataMRI_time,DataMRI_Cross)

count=0;
for i=1:size(DataMRI_Cross,1)
    for j=1:size(DataMRI_time,1)
        
if (DataMRI_Cross(i,1)==DataMRI_time(j,1) && DataMRI_Cross(i,2)==DataMRI_time(j,2))
count=count+1;
DataMRI_Cross_New(count,:)=DataMRI_Cross(i,:);
DataMRI_time_New(count,:)=DataMRI_time(j,:);
end

    end
end
end