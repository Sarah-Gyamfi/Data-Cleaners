Data Cleaners





Excel Data Cleaner



A simple Python tool that cleans Excel datasets by removing duplicates and filling in missing values. Great for data analysts who need to quickly prepare messy data for analysis.



What It Does



This tool takes your messy Excel file and:



* Removes duplicate rows - Keeps only unique records

* Fills missing numeric values - Replaces blanks with 0

* Fills missing text values - Replaces blanks with "Missing"

* Saves cleaned data and exports it as a CSV file to your chosen location.



Why use this tool?



Save time by quickly cleaning data instead of manually addressing hundreds of rows.



Consistency: Apply the same cleaning rules every time, reducing human error



Simplicity: No complex configuration required. Specify your file and run the script.



Perfect For: Any Excel file with missing or duplicate data



Requirements



* Python 3 (any recent version)

* pandas library







How to Use



Step 1: Download the script



Download excel_data_cleaner.py from the repository.



Step 2: Update File Paths



Open the script in any text editor and update these two lines:



input_path = r"C:\Users\YourName\Documents\messy_data.xlsx"  # Your Excel file location

output_dir = r"C:\Users\YourName\Documents\Cleaned"  # Where to save cleaned file





Tips for file paths:



* On Windows: Use r"C:\Users\..." (note the r before the quotes)

* On Mac/Linux: Use "/Users/yourname/Documents/..."

* The script will create the output folder if it doesn't exist.



Step 3: Run the Script



Open your terminal, navigate to where you saved the script, and run:



python excel_data_cleaner.py





Or:



python3 excel_data_cleaner.py





Step 4: Find Your Cleaned File



Look in your output folder for cleaned_data.csv; this is your cleaned dataset.



Example



Before cleaning:



Name       | Age  | Department

John Smith | 35   | Sales

Jane Doe   |      | Marketing

John Smith | 35   | Sales

Bob Jones  | 28   |





After cleaning:



Name       | Age | Department

John Smith | 35  | Sales

Jane Doe   | 0   | Marketing

Bob Jones  | 28  | Missing





What Gets Displayed



When you run the script, you'll see:



* First 5 rows of your data

* Information about data types and missing values

* Confirmation message when the cleaned file is saved



Troubleshooting



"pandas not found" error: Install pandas.



"File not found" error: Double-check your file path is correct.



Excel file won't open: Make sure the file isn't open in Excel when you run the script.



Permission error: Make sure you have write access to the output folder.



Contributing



Found a bug or have a feature suggestion? Feel free to open an issue or submit a pull request!



License



Free to use and modify for your data cleaning needs.



---



Made for data analysts who want to spend less time cleaning and more time analysing.



---

Text Data Cleaner with Column Hashing

A Python tool that cleans text-based data files (CSV, TSV, etc.) and adds privacy by hashing sensitive columns. Ideal if you need to anonymise customer information, IDs, or other sensitive data before sharing datasets.

What It Does

This tool processes your text data files and:

* Removes duplicate rows - Keeps only unique records
* Fills missing numeric values - Replaces blanks with 0
* Fills missing text values - Replaces blanks with "Missing"
* Renames columns - Standardises column names for clarity
* Hashes sensitive data - Creates anonymized versions of columns containing names, IDs, or other sensitive information using SHA-256 encryption.
* Exports cleaned data - Saves as a CSV file ready for analysis or sharing.

Why Use This?

Privacy Protection: Hash customer names, employee IDs, or other sensitive information before sharing data with teams or clients

GDPR & Compliance Ready: Remove personally identifiable information while keeping your data useful for analysis

Flexible Format Support: Works with CSV, TSV, space-separated, and other common text formats

Time Saver: Automate data cleaning and anonymisation in one step

Perfect For: Customer datasets, employee records, medical data, survey responses or any data containing sensitive information that needs anonymisation

Requirements

* Python 3 (any recent version)
* pandas library
* hashlib (included with Python, no installation needed)



How to Use

Step 1: Download the script

Download txt_data_cleaner.py from this repository.

Step 2: Configure Your File Format

Open the script in a text editor. At the top of the data_cleaner() function, uncomment the line that matches your file format:

# For comma-separated (CSV):
df = pd.read_csv("Replace with the file path", sep=",")

# For tab-separated (TSV):
# df = pd.read_csv("Replace with the file path", sep="\t")

# For space-separated:
# df = pd.read_csv("Replace with the file path", sep="\s+")

# For semicolon-separated:
# df = pd.read_csv("Replace with the file path", sep=";")


Remove the # from the line you want to use, and add # to the others.

Step 3: Update Your File Paths and Settings

Update these parts of the script:

# 1. Input file path
df = pd.read_csv("C:/Users/YourName/Documents/raw_data.csv", sep=",")

# 2. Your column names (in order as they appear in your file)
column_names = ["CustomerID", "Name", "Email", "Purchase", "Date"]

# 3. Which column to hash (must match one of the names above)
new_df["HASHED_NAME"] = df["Name"].apply(lambda name: hashlib.sha256(str(name).encode("utf-8")).hexdigest())

# 4. Drop the original unhashed column
new_df = new_df.drop(columns=["Name"])

# 5. Output file path
new_df.to_csv("C:/Users/YourName/Documents/Cleaned/cleaned_data.csv", index=False)


Important Notes:

* Column names will be converted to UPPERCASE automatically.
* The hashed column name (e.g., "HASHED_NAME") can be anything you want
* Make sure the column you're hashing exists in your column_names list.

Step 4: Run the Script

Open your terminal, navigate to where you saved the script and run:

python txt_data_cleaner.py


Or:

python3 txt_data_cleaner.py


Step 5: Find Your Cleaned File

Your anonymized, cleaned dataset will be saved as cleaned_data.csv in your specified location.

Example

Before cleaning:

CustomerID | Name          | Email              | Purchase
1001       | Alice Johnson | alice@email.com    | 50.00
1002       | Bob Smith     |                    | 
1001       | Alice Johnson | alice@email.com    | 50.00
1003       |               | charlie@email.com  | 75.50


After cleaning:

CUSTOMERID | HASHED_NAME                                                      | EMAIL              | PURCHASE
1001       | 8f4e7c2a1b3d9e5f6a0c8d7b4e1f2a3c5d6e7f8a9b0c1d2e3f4a5b6c7d8e9f | alice@email.com    | 50.00
1002       | 3a2b1c0d9e8f7a6b5c4d3e2f1a0b9c8d7e6f5a4b3c2d1e0f9a8b7c6d5e4f3a2b | Missing            | 0
1003       | Missing                                                          | charlie@email.com  | 75.50


Notice:

* Duplicate row removed.
* Names replaced with irreversible hashed values.
* Missing values filled in.
* Column names standardized to uppercase.

Understanding Hashing

What is hashing? Hashing converts text into a unique fingerprint that cannot be reversed. The same input always produces the same hash, which is useful for:

* Matching records without exposing real identities
* Protecting customer privacy
* Meeting data protection regulations

Important: Once hashed, you cannot recover the original value. Keep a secure copy of the original data if you might need it later.

What Gets Displayed

When you run the script, you'll see:

* First 5 rows of your original data
* Data type information
* Confirmation message when the cleaned file is saved

Troubleshooting

"pandas not found" error: Install pandas using pip install pandas.

"File not found" error: Check your input file path is correct.

"KeyError" on column name: Make sure the column you're trying to hash matches exactly with your column_names list

Encoding errors: If your file has special characters, try adding encoding='utf-8' to the read_csv line:

df = pd.read_csv("your_path", sep=",", encoding='utf-8')


Mixed separators in file: If your file uses inconsistent separators, clean it first or use sep=None with the engine='python' parameter

Privacy Note

This tool uses SHA-256 hashing, which is one-way encryption. However, for maximum security when handling sensitive data:

* Store original data securely and separately.
* Limit access to unhashed data.
* Follow your organization's data protection policies.
* Consider additional security measures for highly sensitive data.

Contributing

Have suggestions or found a bug? Open an issue or submit a pull request!

License

Free to use and modify for your data cleaning and privacy protection needs.

---

Built for data analysts who need to protect privacy while maintaining data utility.