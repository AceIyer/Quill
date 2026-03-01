#Just a simple file to help me understand parsers

from tree_sitter import Parser, Language
import tree_sitter_python as tspython


python_lang = Language(tspython.language())
parser = Parser(python_lang)

code = b"""
class Math_Stuff:
    def add(a, b):
        return a + b

    def subtract(c, d):
        return a - b
"""

tree = parser.parse(code)
root = tree.root_node
print(root)


# Learning how to extract functions
def extract_functions(node, source_code):
    functions = [] # Collect the function names

    if node.type == "function_definition":
        name_node = node.child_by_field_name("name")

        if name_node:
            functionName = source_code[name_node.start_byte : name_node.end_byte].decode("utf-8")
            functions.append(functionName)

    for child in node.children:
        functions.extend(extract_functions(child, source_code))
    
    return functions

test = extract_functions(root, code)
print(f"Functions Detected : {test}")

def extract_classes(node, source_code):
    classes = [] # Collect the function names

    if node.type == "class_definition":
        name_node = node.child_by_field_name("name")

        if name_node:
            className = source_code[name_node.start_byte : name_node.end_byte].decode("utf-8")
            classes.append(className)

    for child in node.children:
        classes.extend(extract_classes(child, source_code))
    
    return classes

t2 = extract_classes(root, code)
print(f"Classes detected : {t2}")



