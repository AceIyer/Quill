# Checking to see if a device has git installed
import subprocess
import shutil
import platform

def check_git_installed():
    git_path = shutil.which("git")   # Checking for a git executable file in path
    if git_path:

        try:
            subprocess.check_output([
                "git", "--version"
            ],
            text = True,
            stderr = subprocess.DEVNULL
            )
            print(f" Git has been detected on your {platform.system()} device")
            return True
        except (subprocess.CalledProcessError, OSError):
            raise RuntimeError("Git was found but failed to execute")
            
    else:
        print(f"Git not found or installed on your {platform.system()} device. PLease install Git to use Quill ")

if __name__ == "__main__":
    check_git_installed()



# checking if git has been initialized in the project for quill to run

def check_git_initialized() -> bool:

    try: 
        subprocess.check_output(["git", "rev-parse", "--is-inside"],
                    
                    stderr = subprocess.DEVNULL           
        )
        return True
    except subprocess.CalledProcessError:
        print("Git has not been initilized , please exceute git init to get started with Quill")