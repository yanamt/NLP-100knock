import pandas as pd

df1=pd.read_csv("col1.txt",header=None)
df2=pd.read_csv("col2.txt",header=None)
df=pd.concat([df1,df2],axis=1)
df.to_csv("join.txt",sep="\t",header=False,index=False)
