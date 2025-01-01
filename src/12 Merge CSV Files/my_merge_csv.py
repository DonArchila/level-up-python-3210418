# merge list of csv files in a directory into a single csv file 
import os
import pandas as pd

def merge_csv(file_list, output_file):
# Initialize an empty list to hold DataFrames
    df_list = []

    # Get the directory of the current script
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # Read and append each CSV file to the list
    for file in file_list:
        file_path = os.path.join(script_dir, file)
        df_temp = pd.read_csv(file_path)
        df_list.append(df_temp)
    
    # Concatenate all DataFrames in the list
    df = pd.concat(df_list, ignore_index=True)
    
    # Write the merged data frame to a new file
    output_path = os.path.join(script_dir, output_file)
    df.to_csv(output_path, index=False)

if __name__ == "__main__":
    # List of CSV files to merge
    files = ['class1.csv', 'class2.csv']
    
    # Output file name
    output_file = "all_students.csv"
    
    # Merge the CSV files
    merge_csv(files, output_file)