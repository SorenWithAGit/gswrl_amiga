import os
import glob
import argparse
from pathlib import Path
import shutil


def main(input_path: Path, output_path: Path, base_name: str):
    img_cnt = 1
    subfolders= [f.path for f in os.scandir(input_path) if f.is_dir()]
    for folder in subfolders:
        # print(folder)
        subsub = [f.path for f in os.scandir(folder) if f.is_dir()]
        for sub in subsub:
            files = glob.glob(str(sub) + '//' + '*.png', recursive = True)
            for file in files:
                os.makedirs(output_path, exist_ok = True)
                newname = str(base_name) + "{:05d}".format(img_cnt) + ".png"
                dest_path = os.path.join(output_path, newname)
                shutil.copy2(Path(file), dest_path)
                print("Writing: " + str(newname))
                img_cnt += 1

if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog = "name_image.py", 
                                    description = "Collect and Rename image files")
    parser.add_argument("--input_path",
                          type = Path,
                          required = True,
                          help = "File path to navigate subfolders and .pngs")
    parser.add_argument("--output_path",
                        type = Path,
                        required = True,
                        help = "Destination path for .pngs")
    parser.add_argument("--base_name",
                        type = str,
                        required = True,
                        help = "Leading file name")
    args = parser.parse_args()
    main(args.input_path, args.output_path, args.base_name)