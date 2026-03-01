#Responsible for extracting classes and functions/methods in js code


from tree_sitter import Parser, Language
import tree_sitter_javascript as tsjs

js_lang = Language(tsjs.language())
parser = Parser(js_lang)


code = b"""
/**
 * AST Test Suite
 * Target Nodes: VariableDeclaration, ClassDeclaration, 
 * IfStatement, ForStatement, and BinaryExpressions.
 */

const magicNumber = 42;
let status = "initialized";

class Robot {
  constructor(name) {
    this.name = name;
  }

  // Method with a Conditional and Template Literal
  identify(code) {
    if (code === magicNumber) {
      return `Access Granted to ${this.name}`;
    } else {
      return "Access Denied";
    }
  }
}

// Loop to test Sequence and Update Expressions
for (let i = 0; i < 3; i++) {
  const bot = new Robot(`Bot_${i}`);
  const result = bot.identify(i + 40);
  console.log(result);
}
"""

tree = parser.parse(code)
root = tree.root_node
#print(root)

def extract_classes(node, source_code):
    classes = [] # Collect the function names

    if node.type == "class_declaration":
        name_node = node.child_by_field_name("name")

        if name_node:
            className = source_code[name_node.start_byte : name_node.end_byte].decode("utf-8")
            classes.append(className)

    for child in node.children:
        classes.extend(extract_classes(child, source_code))
    
    return classes

def extract_functions(node, source_code):
    functions = [] # Collect the function names

    if node.type == "method_definition":
        name_node = node.child_by_field_name("name")

        if name_node:
            functionName = source_code[name_node.start_byte : name_node.end_byte].decode("utf-8")
            functions.append(functionName)

    for child in node.children:
        functions.extend(extract_functions(child, source_code))
    
    return functions

test = extract_classes(root, code)
test2 = extract_functions(root, code)
print(f"Classes : {test}")
print(f"Functions : {test2}")