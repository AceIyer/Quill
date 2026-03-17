#This is to enforce the rules of quill with git 
# To stick to its workflow for the best experience

from .git_check import check_git_initialized, check_git_installed
import typer


def quill_preflight_check():
    if not check_git_installed():
        typer.echo("Quill needs git to be installed")
        raise typer.Exit(code=1)

    if not check_git_initialized():
        typer.echo("Git is has not been initialized for this project")
        typer.echo("Run in project root : git init then quill init")
        raise typer.Exit(code=1)

    
    return True