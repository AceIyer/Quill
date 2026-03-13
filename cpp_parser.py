#This should work as the parser for c++ code


def extract_structs(node, source_code):
    structs = []

    if node.type == "struct_specifier":
        name_node = node.child_by_field_name("name")

        if name_node:
            structName = source_code[name_node.start_byte : name_node.end_byte].decode("utf-8")
            structs.append(structName)

    for child in node.children:
        structs.extend(extract_structs(child, source_code))

    return structs

def extract_classes(node, source_code):
    classes = []

    if node.type == "class_specifier":
        name_node = node.child_by_field_name("name")

        if name_node:
            className = source_code[name_node.start_byte : name_node.end_byte].decode("utf-8")
            classes.append(className)
    
    for child in node.children:
        classes.extend(extract_classes(child, source_code))
    
    return classes

def extract_functions(node, source_code):
    functions = []

    if node.type == "function_declarator":
        name_node = node.child_by_field_name("declarator")

        if name_node:
            functionName = source_code[name_node.start_byte : name_node.end_byte].decode("utf-8")
            functions.append(functionName)
    
    for child in node.children:
        functions.extend(extract_functions(child, source_code))

    return functions


