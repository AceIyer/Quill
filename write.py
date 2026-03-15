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
from rich.console import Console
import json
import re  # regex

# Calling my parsers
import python_parser, cpp_parser, js_parser


console = Console()

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
     console.print("Quill Code Summary : " , style = f"bold italic underline {indicolite}", justify = "center")

     for item in data_list:
          console.print(f"\nFile : {item['file']}", style = "green")

          if item['classes']:
        # Added (L{c['line']}) to show the line number in the terminal
            class_names = [f"{c['name']} (L{c['line']})" for c in item['classes'] ]
            console.print(f"  [bold green]Classes:[/bold green]   {', '.join(class_names)}")

          if item['functions']:
            
            function_names = [f"{f['name']} (L{f['line']})" for f in item['functions']]
            console.print(f"  [bold white]Functions: [/bold white]{', '.join(function_names)}")

          if item.get('structs'):
            struct_names = [f"{s['name']} (L{s['line']})" for s in item['structs']]
            console.print(f"  [bold magenta]Structs: [/bold magenta]   {', '.join(struct_names)}")

def reference_system(dev_notes, extracted_data):
    """
    This is responsible for allowing the user to use @ to link where this block of lives in teh system i
    in the project-doc.md file , creates a link to the file and block of code
    """
    refs = re.findall(r"@(\w+)", dev_notes)

    for ref in refs:
        # Find the matching data in your extracted list
        for file_entry in extracted_data:
            # Check functions, classes, and structs
            all_items = file_entry['functions'] + file_entry['classes'] + file_entry.get('structs', [])
            
            match = next((item for item in all_items if item['name'] == ref), None)
            
            if match:
                file_path = file_entry['file']
                line = match['line']
                # Replace @add with a Markdown link to that file and line
                link = f"[**{ref}**]({file_path}#L{line})"
                dev_notes = dev_notes.replace(f"@{ref}", link)
                
    return dev_notes





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
    print("=> Add a quick note?")
    print("--Use @ to link important functions, classes or structs.")
    print("-- Press Ctrl + D or type DONE to save and exit.")
    dev_notes = []
    while True:
        try:
            line = input()
            if line.strip().upper() == "DONE":
                break
            dev_notes.append(line)
        except EOFError: # this should trigger Ctrl+D for a user to save and exit
            break
    
    #this should combine the strings of the dev notes nicely
    raw_notes = "\n".join(dev_notes)

    #now apply my reference code
    final_notes = reference_system(dev_notes, data_list)

    timestamp = get_current_time()
    os.makedirs(".quill", exist_ok=True)
    
    #md
    with open(".quill/project_documentation.md", "a", encoding="utf-8") as md_file:
        md_file.write(f"\n---\n## {timestamp}\n")
        md_file.write(f"**Dev Notes:** {final_notes}\n\n")
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