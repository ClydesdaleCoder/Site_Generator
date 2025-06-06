import os
import shutil
import pathlib

def stat_to_pub_copy(static,public):
    if os.path.exists(public):
        public = shutil.rmtree(public)
    for s in static:    
        if os.path.isfile(s):
            shutil.copy(s,pathlib.path(public))
        if os.path.isdir(s):
            new_dir= os.mkdir(s)
            public = os.path.join(public,new_dir)
            return stat_to_pub_copy(static,public)


