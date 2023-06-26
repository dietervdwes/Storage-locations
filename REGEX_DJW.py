#!/usr/bin/env python
# coding: utf-8

# In[2]:


import os
import glob
import re
import datetime

def process_file(file_path, output_folder):
    # Read the contents of the file
    with open(file_path, 'r') as file:
        content = file.read()

    # Define the regex pattern to match the desired line structure
    # pattern1 = r'\d{2}/\d{2}/\d{4} \d{2}:\d{2}\s+Type : IR\s+Sample \w+ loaded on RSA Pro'
    # matches1 = re.findall(pattern1, content)

    pattern2 = r'\d{2}/\d{2}/\d{4} \d{2}:\d{2}\s+Type : IR\s+Sample \w+ loaded on C6000'
    matches2 = re.findall(pattern2, content)

    # If there are matches, write the last match into a new file
    # if matches1:
    #     last_sample_line1 = matches1[-1] + "\n"
    #     output_file_path = os.path.join(output_folder, 'Cobas_output_file.txt')
    #     with open(output_file_path, 'a') as output_file:
    #         output_file.write(last_sample_line1)
    
    #Get the date into a variable
    date_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S").replace(":","-").replace(" ","_")
    if matches2:
        last_sample_line2 = matches2[-1] + "\n"
        output_file_path = os.path.join(output_folder, f'Cobas_output_file{date_time}.txt')
        with open(output_file_path, 'a') as output_file:
            output_file.write(last_sample_line2)

def process_all_files(input_folder, output_folder):
    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Get a list of all .txt files in the input folder
    files = glob.glob(os.path.join(input_folder, "*.txt"))

    # Process each file in the input folder
    for file_path in files:
        process_file(file_path, output_folder)

if __name__ == "__main__":
    base_path = os.getcwd()
    input_folder = os.path.join(base_path, "machine_data")  # Replace with the path to your input folder
    output_folder = os.path.join(base_path, "new_machine_data")  # Replace with the path to your desired output folder
    # Create the directory, if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    if not os.path.exists(input_folder):
        os.makedirs(input_folder)
    process_all_files(input_folder, output_folder)


# In[ ]:




