Data Cleaners


excel_data_cleaner

This Python script cleans an Excel dataset by removing duplicate rows and filling in missing values.

What It Does
- Replaces missing numeric values with `0`
- Replaces missing text values with `"Missing"`
- Saves a cleaned version of the file as `cleaned_data.csv` on your Desktop

 Requirements
- Python 3
- pandas library



How to Run
1. Update the file path in the code where it says "Replace with the file path" with your actual file path.
2. Run the script in your terminal or editor.
3. The cleaned file will be saved  as `cleaned_data.csv`.



txt_data_cleaner.py

 Data Cleaner with Hashed Column

This Python script reads a data file, removes duplicates, fills in missing values, renames columns, and adds a hashed version of a chosen column (for example, to hide customer names or IDs).

What It Does


- Removes duplicate rows
- Replaces missing numeric values with `0`
- Replaces missing text values with `"Missing"`
- Renames columns for clarity
- Creates a new hashed column using SHA-256
- Exports the cleaned data as a CSV file

 Requirements
- Python 3
- pandas
- hashlib (standard Python library)


A cleaned file is saved to the file path you set.


Constructive suggestions welcome!