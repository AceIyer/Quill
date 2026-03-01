#This file is responsilbe for making acedoc a multi-lingual tool 
#BUilding parsers for every lanuage acedoc will support
#Just going with the main ones for now 
'''
main langugaes i use right now is c++, python, js. 
Just building the maps for those originally then will expand later on 
'''

from pathlib import Path
from tree_sitter import Parser, Language
import tree_sitter_python as tspython
import tree_sitter_javascript as tsjs
import tree_sitter_cpp as tscpp

LANGUAGE_MAP = {
    ".py":tspython.language(),
    ".js":tsjs.language(),
    ".cpp":tscpp.language(),
    ".hpp":tscpp.language(),
    ".cc":tscpp.language()
}
