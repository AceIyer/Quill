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
    if platform.system() == "Windows":
        destination = hooks_path / "post-commit.bat"
    else:
        destination = hooks_path / "post-commit"

    if destination.exists():
        # Maybe offer to overwrite if you update Quill later!
        print("Post-Commit hook already exists.")
        return
    
    shutil.copy(source, destination)

    if platform.system() != "Windows":
        # Ensure it is executable
        destination.chmod(0o775)
        
    print(f"Quill git hook installed successfully as {destination.name}")