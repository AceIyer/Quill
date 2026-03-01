# This is responsible for getting the modified files from project and the users commit hash for documentation identification


import subprocess

def check_modified_files():

    try: 
        files_check = subprocess.check_output(["git", "show", "--name-only", "<commit_hash>"],
                                 text = True,
                                 stderr=subprocess.DEVNULL
                                 
                                 )
        return(files_check)
    except subprocess.CalledProcessError as e:
        raise RuntimeError(e)
    


    