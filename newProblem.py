import sys
import os

class Main:
    def __init__(self):
        if len(sys.argv) == 1:
            print(f"Error:\tUsage: {sys.argv[0].split('/')[-1]} [folderName]")
        else:
            name = sys.argv[1]
            os.mkdir(name)
            os.mkdir(f'{name}/p1')
            os.mkdir(f'{name}/p2')
            with open('template.txt', 'r') as t:
                text = t.read()
                t.close()
                with open(f'{name}/p1/main.py', 'w') as f:
                    f.write(text+f'\n\tprint(Solution("{name}/p1/input.txt").solve())')
                    f.close()
                with open(f'{name}/p2/main.py', 'w') as f:
                    f.write(text+f'\n\tprint(Solution("{name}/p2/input.txt").solve())')
                    f.close()
            
if __name__ == '__main__':
    Main()