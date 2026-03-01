#This should work as the parser for c++ code

from tree_sitter import Parser, Language
import tree_sitter_cpp  as tscpp

cpp_lang = Language(tscpp.language())
parser = Parser(cpp_lang)


code = b"""
#include <iostream>
#include <string>

// Simple data structure
struct Config {
    int id;
    float velocity;
};

// Class with encapsulation and a method
class Robot {
private:
    std::string name;
public:
    Robot(std::string n) : name(n) {}
    
    void status() {
        std::cout << "Robot " << name << " is active." << std::endl;
    }
};

// Standalone function
int calculate(int a, int b) {
    return a + b;
}

int main() {
    Config cfg = {1, 9.8f};
    Robot bot("Gemini");
    
    bot.status();
    int result = calculate(10, 20);
    
    return 0;
}
"""

tree = parser.parse(code)
root = tree.root_node
#print(root)

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


test = extract_structs(root, code)
test2 = extract_classes(root, code)
test3 = extract_functions(root, code)
print(f"Structs : {test}")
print(f"Classes : {test2}")
print(f"Functions : {test3}")