# This file is responsible for allowing Quill to run within your repo

import typer

from Git_check import check_git_initialized, check_git_installed
from create_quill_dir import create_quill_dir
from install_git_hook import install_hook
from preflight import quill_preflight_check
from write import get_modified_files, pipeline, write_to_Docs

app = typer.Typer(help = "Ace Doc - This is a tool that works with your git flow to keep documentation consistent")

@app.command() 
def init():
    # This should allow for users to run either quill or ace run to initialize Ace Doc in repo
    """
    Type in quill init to initilaze Ace Doc within your git repo. 
    """
    typer.echo("Initializing Quill ....")
    # TODO:
    check_git_installed()
    check_git_initialized()
    create_quill_dir()
    install_hook()
    typer.echo("Quill initialization completed.")

@app.command()
def run():
    """
    - Start running Quill in your repo.
    - If you're having trouble with quill run try quill init first to initialize quill into your git workflow.
    """
    #Building execution structure
    if quill_preflight_check():
        typer.echo("Quill is checking last commit....")
        #get files modified
        files = get_modified_files()
        # Extract and write
        extracted_data = pipeline(files)
        write_to_Docs(extracted_data)


if __name__ == "__main__":
    app()