# CYK Algorithm Implementation
This project implements the Cocke-Younger-Kasami (CYK) algorithm for parsing context-free grammars in Python.

## Description
The CYK algorithm is a bottom-up parsing algorithm that can check if a given string can be generated from a context-free grammar. It employs dynamic programming to efficiently parse the input.

This implementation takes as input:
- The number of grammar rules
- The grammar rules in the format "A -> BC" 
- An input string

It outputs whether the string can be generated from the grammar using the CYK algorithm. If so, it prints the parse in a table showing which grammar rules could generate substrings.

## Input Format
- First line: Number of grammar rules
- Following lines: Grammar rules (A -> BC)
    - Terminals: Lowercase letters
    - Non-terminals: Uppercase letters
- Last line: Input string

## Output Format
If the input string can be parsed by the grammar rules using CYK:
- YES
- Table showing the grammar rules that can generate substrings

If the input cannot be parsed:
- NO

## Example Usage
See the examples provided in [examples.md](examples.md)

## Dependencies
- Python 3

## Credits
CYK algorithm by:
- John Cocke 
- Daniel Younger  
- Tadao Kasami

Implementation by:
- Seyyed Ali Ayati