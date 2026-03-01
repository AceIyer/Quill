# This file is responsible for allowing Quill to run within your repo

import typer
from docflow.ui import run_tui
from preflight import check_git_initialized, check_git_installed
from create_quill_dir import create_quill_dir
from install_git_hook import install_hook

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

    run_tui()

if __name__ == "__main__":
    app()