import os
import tempfile

import pandas as pd

dirpath = tempfile.TemporaryDirectory()
print(str(dirpath))
dirpath.cleanup()

def run():
    # create a temporary working directory
    dirpath = tempfile.TemporaryDirectory()
    print(str(dirpath))
    dirpath.cleanup()

    # list and print all foldes and files in /data and /feature-store
    print('/data')
    for root, subdirectories, files in os.walk('/data'):
        for subdirectory in subdirectories:
            print(os.path.join(root, subdirectory))
        for file in files:
            print(os.path.join(root, file))

    print('/feature-store')
    for root, subdirectories, files in os.walk('/data'):
        for subdirectory in subdirectories:
            print(os.path.join(root, subdirectory))
        for file in files:
            print(os.path.join(root, file))

    print("done!")

if __name__ == "__main__":
    run()