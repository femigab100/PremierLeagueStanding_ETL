import os

def load_to_csv(df, file_path="output/PLStanding.csv"):

    #Load transformed DataFrame into a CSV file.
    os.makedirs("output", exist_ok=True)
    df.to_csv(file_path, index=False)
    print(f"Data successfully loaded into {file_path}")
