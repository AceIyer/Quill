#This is responsible for creating the .quill/project_documentation.md dir in the project repo

import subprocess
from pathlib import Path

def get_repo_root():
    """
    This is responsible for getting the main root of the project so that the .quill dir can get created there get_repo_root
    """

    try: 
        result = subprocess.run(
            ["git", "rev-parse", "--show-toplevel"],
            capture_output = True,
            text = True,
            check=True,
            
        )
        return Path(result.stdout.strip())
    except subprocess.CalledProcessError:
        return Path(".")

def create_quill_dir():
    """
    Responsible for craeting the .quill dir and the project-doc.md where all the documentation is written
    """

    root = get_repo_root()
    quill_dir = root /".quill"
    quill_dir.mkdir(exist_ok = True)

    doc_file = quill_dir / "project_documentation.md"
    if not doc_file.exists():
        doc_file.write_text("# Poject Documentation\n\n")



if __name__ == "__main__":
    create_quill_dir()