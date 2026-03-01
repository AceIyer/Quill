# This is responsible for installing the git hooks onto a users device

import subprocess
import pathlib as Path
import shutil
import platform


def get_hook_path():
    """
    Get where the .git/hooks path is in the repo
    """
    result = subprocess.run(["git", "rev-parse", "--git-path", "hooks"],
                            capture_output = True,
                            text = True,
                            check = True,
                            stderr = subprocess.DEVNULL
                            )
    return Path(result.stdout.strip())

def get_hook_script():
    """
    This should be responsible for getting the correct hook based on the OS .sh(Unix based) and .bat(Windows)
    """
    if platform.system() == "Windows":
        return "post-commit.bat"
    return "post-commit.sh"

def install_hook():
    """
    This function is responsible for installing the post-commit git hook onto the device
    """
    hooks_path = get_hook_path()
    script_name = get_hook_script()

    source = Path(__file__).parent/"hooks"/script_name
    destination = hooks_path/"post-commit"

    if destination.exists():
        print("Post-Commit hook already exits.")
        return
    
    shutil.copy(source, destination)

    if platform.system() != "Windows":
        destination.chmod(0o775)
    print("Quill git hook installed successfully.")