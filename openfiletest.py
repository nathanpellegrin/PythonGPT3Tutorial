import openai


""" 
#original def inserted newline char '\n', which was fixed by adding '.replace('\n', '')'
def open_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as infile:
        return infile.read().replace('\n', '')
"""


def open_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as infile:
        return infile.read().replace('\n', '')


openai.api_key = open_file('openaiapikey.txt')

print(openai.api_key)

string_val = open_file('openaiapikey.txt')

print(string_val)

string2 = string_val.replace('\n', '')

print(string2)
