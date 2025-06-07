import os
import shutil
import pathlib

def stat_to_pub_copy(static,public):
    if not os.path.exists(public):
        os.mkdir(public)
    
    for item in os.listdir(static):    
        source_item = os.path.join(static,item)
        dest_item =  os.path.join(public,item)

        if os.path.isfile(source_item):
            new_addition = shutil.copy(source_item, dest_item)
            print (f'Adding {new_addition}')
        if os.path.isdir(source_item):
            os.mkdir(dest_item)
            stat_to_pub_copy(source_item,dest_item)

