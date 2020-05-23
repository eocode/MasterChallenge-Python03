# Resolve the problem!!
import re

def run():
    # Start coding here
    with open('encoded.txt', 'r', encoding='utf-8') as f:
        text = f.read()
        x = re.findall('[a-zA-Z0-9]',text)
        print(' '.join([str(elem) for elem in x]))
        

if __name__ == '__main__':
    run()
