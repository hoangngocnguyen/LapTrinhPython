# Create a directory and move a file from one directory to another
# using low-level OS functions.

import os
from pathlib import Path


def using_os_function():
    # Check to see if a directory named "test1" exists under the current
    # directory. If not, create it:
    desc_dir = os.path.join(os.getcwd(), "test1")
    if not os.path.exists(desc_dir):
        os.mkdir(desc_dir)

    # Construct source and destination paths:
    src_file = os.path.join(os.getcwd(), "sample_data", "README.md")
    dest_file = os.path.join(os.getcwd(), "test1", "README.md")


    # Move the file from its original location to the destination:
    os.rename(src_file, dest_file)


def using_pathlib():
    # Check to see if the "test1" subdirectory exists. If not, create it:
    dest_dir = Path("test1/")
    print("hi", dest_dir)
    if not dest_dir.exists():
        dest_dir.mkdir()

    # Construct source and destination paths:
    src_file = Path("./sample_data/README.md")
    dest_file = dest_dir / "README.md"

    # Move the file from its original location to the destination:
    src_file.rename(dest_file)

using_pathlib()