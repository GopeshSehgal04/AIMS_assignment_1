# ORIGINAL INCODING

import pandas as pd
import numpy as np
data={"Currency":['Yen','Dollar','Rupee','euro','pound']}
df=pd.DataFrame(data)

order=['Dollar','euro','pound','Rupee','Yen']

mapping={}
for i in range(len(order)):
    mapping[order[i]]=i+1

for i in range(len(df)):
    current_value=df.loc[i,"Currency"]
    df.loc[i,"Currency"]=mapping[current_value]

print("Encoded Data:\n", df)

# ONE-HOT-ENCODING

data={"States":['Uttar_Pradesh','Goa','Madhya_pradesh','Rajasthan','Kerala','Goa','Uttar_Pradesh','Punjab']}

df=pd.DataFrame(data)

def one_hot(df, column):
    categories = df[column].unique()
    for States in categories:
        df[States] = np.where(df[column] == States, 1, 0)
    df = df.drop(column, axis=1)
    return df

df_OHE = one_hot(df, 'States')

print("One-Hot Encoding:\n", df_OHE)

# IMPUTATION

data = {"Grades":[7,9,6,8,5,np.nan,5,7,8,9,2, np.nan,3,8,np.nan]}

df= pd.DataFrame(data)
mean_value= df["Grades"].mean()

def mean_imputation(df):
    for i in range(len(df)):
        if np.isnan(df.loc[i, "Grades"]):
             df.loc[i, "Grades"] = mean_value
    return df

print("Imputed data: \n" ,mean_imputation(df))