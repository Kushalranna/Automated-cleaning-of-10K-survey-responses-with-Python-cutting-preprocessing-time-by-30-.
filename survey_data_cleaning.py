import pandas as pd
df = pd.read_csv("survey_data.csv")

print("Before Cleaning:")
print(df.head())


df = df.fillna({
    'Name': 'Unknown',
    'Age': df['Age'].median(),
    'Response': 'No Response'
})


df['Name'] = df['Name'].str.strip().str.title()
df['Email'] = df['Email'].str.lower()


df['Response_Date'] = pd.to_datetime(df['Response_Date'], errors='coerce')


df = df.drop_duplicates()


df.to_csv("survey_data_cleaned.csv", index=False)
df.to_excel("survey_data_cleaned.xlsx", index=False)

print("After Cleaning:")
print(df.head())
print("\n Data cleaned and exported successfully!")
