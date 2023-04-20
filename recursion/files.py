
import re
import os

def find_dir(indir:str, output:list):
    '''
    traverse directory
    '''
    if os.path.isdir(indir):
        output.append(indir)
        for sub_dir in os.listdir(indir):
            if not re.findall(r'^\.|^\_\_', sub_dir):
                next_dir = os.path.join(indir, sub_dir)
                find_dir(next_dir, output)

def find_files(indir:str, output:list):
    if os.path.isdir(indir):
        for name in os.listdir(indir):
            if not re.findall(r'^\.|^\_\_', name):
                path = os.path.join(indir, name)
                if os.path.isfile(path):
                    output.append(path)
                elif os.path.isdir(path):
                    find_files(path, output)

