---------------------------------------
Written by Dieter van der Westhuizen
2020 - 2023
dietervdwes@gmail.com
+27828612093
---------------------------------------

This script does 2 things from the TrakCare Storage Information window:
1. Gets the storage info from a list of episode numbers: "storage_sample.csv" OR
2. Gets the "Instrument Send/Test result data" from a list of episode numbers: "episode_numbers.csv".
3. Gets the above "Instrument Send/Test result data output files and isolates the lines which contain the words "Sample [x] loaded on C6000" into a single text file

---------------------------------------

Instructions for 1. Storage info:

1. Format your file: storage_samples.csv with your list of episodes of which you need the storage locations to.
2. Make sure that specimen_log.txt is empty (i.e. does not contain the data from a previous scrape).
3. Log into TrakCare and open the "Specimen Information" module.
4. Enter one episode and hit Tab.  Then tick the "Storage Data" tick box and click "Display"
5. Click Clear.
6. Open the Storage Positions.ahk script.
7. Hit "Storage"

The scraped storage positions will be written to "specimen_log.txt" in the same folder as the main script.
This file will need manual translation by from Excel by "Data" --> "Text to colums" to get it into a useable thing.

---------------------------------------

Instruction for 2. Machine data:

1. Format your file: "episode_numbers.csv" with your list of episodes of which you need the machine log data to.
2. Make sure that the directory "machine_data" is empty (i.e. does not contain the data from a previous scrape).
3. Log into TrakCare and open the "Specimen Information" module.
4. Enter one episode and hit Tab.  Then tick the "Storage Data" tick box and click "Display" - this is to prepare the window for the scrape.
5. Click Clear.
6. Open the Storage Positions.ahk script.
7. Click the button "Epis_Machine".

If all works well, it should iterate through the episodes one by one and save a data file with Episode number for each episode in the folder "machine_data" within the working directory.

-----------------------------------------

Instruction for  3. RegEx matching of file array to create a single file

NOTE: You need python installed on the PC and added to the System/User Path list for this to work (https://realpython.com/add-python-to-path/). 
This option (adding Python to path) can also be selected upon installation of Python.

1. Open a terminal window (Windows Key + R --> cmd or powershell --> Run) and cd "current_working_directory". Hit Enter. To get the directory, go to the folder containing the scripts and click the window address bar - copy the full path.
   OR 
   Hold Shift and Right click on a blank space in the folder where the scripts are and click "Open PowerShell window here". This should open PowerShell in the current folder already.
2. Type: "python REGEX_DJW.py" without the inverted commas and hit Enter.
3. The script should (hopefully) run successfully and output a file in the folder "new_machine_data" called "Cobus_output_file[date-time].txt".
