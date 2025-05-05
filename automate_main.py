#######################################################################
"""
automate_main.py
Module as named will automate main.py within the file_converter repo.
Accepts an --input_path and --output_path as arguments. 
Will open all binaries and create the .png files of each event.
"""
#######################################################################

import glob
import os 
import argparse
from pathlib import Path


def main(input_path: Path, out_path: Path) -> None:

    # collect file names from folder
    files = glob.glob(str(input_path) + "//" + "*.bin")
    print("Number of files: " + str(len(files)))

    # execute main.py on all files in folder
    file_count = 0
    for filepath in files:
        print(str(filepath) + "is being converted to pngs!")
        os.system("python main.py --file-name " + str(filepath) + " --output-path " + str(out_path)  + " --camera-name oak0 --view-name rgb --video-to-png")
        try:
            os.system("python main.py --file-name " + str(filepath) + " --output-path " + str(out_path)  + " --camera-name oak1 --view-name rgb --video-to-png")
        except:
            print("file does not contain oak1")
            pass
        file_count += 1
        print("Completed " + str(file_count) + " files out of " + str(len(files)) + "files")
        
    # convert continious record to .mp4    
    if len(files) == 1:
        for filepath in files:
            print(str(filepath) + "is being converted to .mp4!")
            os.system("python main.py --file-name " + str(filepath) + " --output-path " + str(out_path)  + " --camera-name oak0 --view-name rgb")
        try:
            os.system("python main.py --file-name " + str(filepath) + " --output-path " + str(out_path)  + " --camera-name oak1 --view-name rgb")
        except:
            print("file does not contain oak1")
            pass


if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog = "python automate_main.py",
                                     description = "Automate file converrter")
    parser.add_argument("--input_path", 
                        type = Path, 
                        required = True, 
                        help = "Path to bin folder"
    )
    parser.add_argument("--output_path",
                        type = Path,
                        required = True,
                        help = "Path output pngs will be stored"
    )
    args = parser.parse_args()
    main(args.input_path, args.out_path)
    