import os
import argparse
from pathlib import Path


def main(input_path: Path, base_name: str) -> None:
    for count, filename in enumerate(os.listdir(input_path)):
        if filename.lower().endswith((".png")):
            old_path = os.path.join(input_path, filename)
            new_name = (str(base_name) + "{:05d}".format(count + 1) + ".png")
            new_file_path = os.path.join(input_path, new_name)
            print("renamed: " + str(new_name))
            os.rename(old_path, new_file_path)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog = "name_image.py", 
                                    description = "Collect and Rename image files")
    parser.add_argument("--input_path",
                          type = Path,
                          required = True,
                          help = "File path to navigate subfolders and .pngs")
    parser.add_argument("--base_name",
                        type = str,
                        required = True,
                        help = "Leading file name")
    args = parser.parse_args()
    main(args.input_path, args.base_name)