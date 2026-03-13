#Responsible for writing down the documentation into the file
#This page is also responsible for collecting all modified files using git then determine the correct parser
#Maybe make a seperate file like or folder like Project_Documenation/Docs.md or .txt
# this is the final page where it all comes together like a master-piece 

from datetime import datetime
import os 
import subprocess
from tree_sitter import Parser, Language
import tree_sitter_cpp as tscpp
import tree_sitter_javascript as tsjs
import tree_sitter_python as tspy
from rich import print
import json

# Calling my parsers
import python_parser, cpp_parser, js_parser

def get_current_time():
    """
    This should allow for quill to get the local time of every user
    """
    current_datetime_local = datetime.now()
    date_string = current_datetime_local.strftime("%Y-%m-%d %H:%M:%S")

    return date_string


def get_modified_files():
    """
    This function gets all the modified files that the dev worked on in the project so far 
    """
    modified_files = subprocess.check_output(['git', 'diff', '--name-only', 'HEAD~1', 'HEAD'], stderr = subprocess.DEVNULL)
    files = modified_files.decode('utf-8').splitlines()

    return files

def pipeline(files):
    '''
    This is a mapping dictionary to map the correct file to parsing logic and it handles the 
    extraction of functions, classes and structs i got from the code 
    '''
    Language_Map = {
        '.py' : Language(tspy.language()),
        '.cpp' : Language(tscpp.language()),
        '.hpp' : Language(tscpp.language()),
        '.js' : Language(tsjs.language())
    }

    #storing all info
    all_extracted_info = []

    for file_path in files:
            ext = os.path.splitext(file_path)[1]
            if ext in Language_Map:
                lang = Language_Map[ext]
                parser = Parser(lang)

                #creating a dictionary for this file
                file_info = {"file": file_path, "functions": [], "classes": [], "structs": []}

                if os.path.exists(file_path):
                     with open(file_path, "rb") as f:
                          source_code = f.read()     # reads the source code as bytes since tree sitter need bytes
                     tree = parser.parse(source_code)
                     root = tree.root_node
                    
                     if ext == ".py":
                          file_info["functions"] = python_parser.extract_functions(root, source_code)
                          file_info["classes"] = python_parser.extract_classes(root, source_code)
                          
                     
                     elif ext == ".cpp" or ext == ".hpp" :
                          file_info["structs"] = cpp_parser.extract_structs(root, source_code)
                          file_info["functions"] = cpp_parser.extract_functions(root, source_code)
                          file_info["classes"] = cpp_parser.extract_classes(root, source_code)
                          
                     
                     elif ext == ".js":
                          file_info["classes"] = js_parser.extract_classes(root, source_code)
                          file_info["functions"] = js_parser.extract_functions(root, source_code)
                          
                     all_extracted_info.append(file_info)
    return all_extracted_info


def code_summary(data_list):
     """
     After the commit to get this should appear to the dev showing them all their modified files
     and all the added functions, classes and in cpp structs
     """
     indicolite = "#267D97" # Colour code of indicolit i could find
     print("Quill Code Summary : " , style = f"bold italic underline {indicolite}", justify = "center")

     for item in data_list:
          print(f"\nFile : {item['file']}", style = "green")

          if item['classes']:
            print(f"  [bold green]Classes:[/bold green]   {', '.join(item['classes'])}")
          if item['functions']:
            print(f"  [bold white]Functions: [/bold white]{', '.join(item['functions'])}")
          if item.get('structs'):
            print(f"  [bold purple]Structs: [/bold purple]   {', '.join(item['structs'])}")



def write_to_Docs(data_list):
    """
    This is responsible for writing all the information in to the project doc and index.json
    in the .quill file in the dir
    """
    if not data_list:
        return "No files we're modified."
    
    #What quill found
    code_summary(data_list)

    #notes from dev
    print("Describe the changes for the knowledge base.")
    dev_notes = input("Insert Documentation : ")
    print("Lets hope the next dev doesn't break anything.")

    timestamp = get_current_time()
    os.makedirs(".quill", exist_ok=True)
    
    #md
    with open(".quill/project_documentation.md", "a", encoding="utf-8") as md_file:
        md_file.write(f"\n---\n## {timestamp}\n")
        md_file.write(f"**Dev Notes:** {dev_notes}\n\n")
        for item in data_list:
            md_file.write(f"### `{item['file']}`\n")
            if item['classes']: md_file.write(f"- Classes: {', '.join(item['classes'])}\n")
            if item['functions']: md_file.write(f"- Functions: {', '.join(item['functions'])}\n")
            md_file.write("\n")

    #json
    #No idea why im doing a json, but professional stuff uses .json to track
    json_path = ".quill/index.json"
    history = []
    if os.path.exists(json_path):
        with open(json_path, "r") as jf:
            try: history = json.load(jf)
            except: history = []

    history.append({
        "timestamp": timestamp,
        "note": dev_notes,
        "files_modified": data_list
    })

    with open(json_path, "w") as jf:
        json.dump(history, jf, indent=4)