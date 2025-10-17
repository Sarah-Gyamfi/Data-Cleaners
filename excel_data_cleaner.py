import pandas as pd


def data_cleaner():

    #df = pd.read_excel("Replace with the file path", sep=",")
    #df = pd.read_excel(Replace with the file path", sep="\\t")
    #df = pd.read_excel("C:Replace with the file path", sep="\\s+")
    df = pd.read_excel("Replace with the file path", sep=";")
    #df = pd.read_excel("Replace with the file path", sep=" ")

    print (df.head())
    print(df.info())
    print(df.dtypes)


    new_df=df.drop_duplicates().copy()


# this loop fills in the blanks. None for numbers. Missing for strings
    for column in new_df.columns:

       if new_df[column].dtype == "int64" or df[column].dtype == "float64":
            new_df[column] = df[column].fillna(0)  
       elif new_df[column].dtype == "object":
            new_df[column] = df[column].fillna("Missing")

    new_df.to_csv("Add_the_path_where_you_want_your_cleaned_datafile_to_end_up\\cleaned_data.csv", index=False)
    print("Cleaned File Saved To Desktop")

    return new_df

data_cleaner()


