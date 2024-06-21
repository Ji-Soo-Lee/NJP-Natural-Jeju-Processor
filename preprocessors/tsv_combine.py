import pandas as pd

def combine_tsv_files(file_paths, output_file_path):
    # Initialize an empty list to hold the DataFrames
    dfs = []

    # Loop through the list of file paths and read each file into a DataFrame
    for file_path in file_paths:
        df = pd.read_csv(file_path, sep='\t')
        dfs.append(df)

    # Concatenate all DataFrames into a single DataFrame
    combined_df = pd.concat(dfs, ignore_index=True)

    # Save the combined DataFrame to a TSV file
    combined_df.to_csv(output_file_path, sep='\t', index=False)

d = input()
name = input()
# List of TSV file paths to combine
file_paths = [
    'datasets/{}/{}_1.tsv'.format(d, name),
    'datasets/{}/{}_2.tsv'.format(d, name),
    'datasets/{}/{}_3.tsv'.format(d, name)
]

# Specify the path for the output combined TSV file
output_file_path = 'datasets/{}/{}_old.tsv'.format(d, name)

# Call the function with the file paths and output file path
combine_tsv_files(file_paths, output_file_path)
