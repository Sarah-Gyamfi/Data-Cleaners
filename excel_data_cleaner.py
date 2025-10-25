import pandas as pd
import os




def data_cleaner():
    input_path= r"the path for raw data goes here"
    output_dir = r"the folder path where you want the cleaned data"
    output_path = os.path.join(output_dir, "cleaned_data.csv")

#If a folder doesn't exist this should create one. If it does it should just continue
    os.makedirs(output_dir, exist_ok=True)

    df = pd.read_excel(input_path)
 
    

    print (df.head())
    print(df.info())
    print(df.dtypes)


    new_df=df.drop_duplicates().copy()


# this loop fills in the blanks. None for numbers. Missing for strings
    for column in new_df.columns:

       if new_df[column].dtype == "int64" or new_df[column].dtype == "float64":
            new_df[column] = new_df[column].fillna(0)  
       elif new_df[column].dtype == "object":
            new_df[column] = new_df[column].fillna("Missing")

    new_df.to_csv(output_path, index=False)
    print("Cleaned File Saved To {output_path}")

    return new_df

data_cleaner()


