import os
import glob
input_folder="\smaple-docs"
for input_files in glob.glob(os.path.join(input_folder,"*.pdf")):
    print(input_files)