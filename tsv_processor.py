import pandas as pd

def clean_tsv_file(file_path, output_file_path):
    # Load the TSV file into a DataFrame
    df = pd.read_csv(file_path, sep='\t')

    # Drop rows with any empty fields
    df.dropna(inplace=True)

    # Save the cleaned DataFrame back to a TSV file
    df.to_csv(output_file_path, sep='\t', index=False)

d = input()
name = input()
# Specify the path to your TSV file and the output file path
file_path = 'datasets/{}/{}_old.tsv'.format(d, name)
output_file_path = 'datasets/{}/{}.tsv'.format(d, name)

# Call the function with the file paths
clean_tsv_file(file_path, output_file_path)
clean_tsv_file(file_path, output_file_path)
