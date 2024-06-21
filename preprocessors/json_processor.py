import pandas as pd
import json
import re
import os

def process_json_files(file_paths, d, name):
    # List to hold all utterances from all files
    all_utterances = []

    # Regular expression to remove text in the format (something)/(something else)
    pattern = re.compile(r'\(.*?\/.*?\)|\{.*?\}')

    # List all files in the given directory
    json_files = [f for f in os.listdir(directory) if f.endswith('.json')]

    # Loop through each file name in the list
    for file_name in json_files:
        file_path = os.path.join(directory, file_name)  # Full path to the file
        
        try:
            # Load JSON data from file
            with open(file_path, 'r', encoding='utf-8') as file:
                data = json.load(file)
                # utterances = data.get("utterance", [])
                transcription = data.get("transcription", [])
                utterances = transcription.get("sentences", [])

                # Extract and process data from each utterance
                for utterance in utterances:
                    # Clean both standard_form and dialect_form by removing the pattern
                    # standard_form = re.sub(pattern, '', utterance.get("standard_form", "")).strip()
                    # dialect_form = re.sub(pattern, '', utterance.get("dialect_form", "")).strip()
                    standard_form = utterance.get("standard", "").strip()
                    dialect_form = utterance.get("dialect", "").strip()

                    utterance_data = {
                        "standard_form": standard_form,
                        "dialect_form": dialect_form
                    }
                    all_utterances.append(utterance_data)
                    
        except json.JSONDecodeError:
            print("Error reading file: {}".format(file_name))
            continue

    # Convert list of dictionaries to DataFrame
    df = pd.DataFrame(all_utterances)

    # Save DataFrame to TSV
    df.to_csv('datasets/{}/{}.tsv'.format(d, name), sep='\t', index=False)

d = input()
name = input()
# Specify the directory containing JSON files
directory = 'datasets/{}/{}/'.format(d, name)

# Call the function with the directory
process_json_files(directory, d, name)
