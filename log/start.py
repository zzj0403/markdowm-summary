import os, sys
from src.run import run

path = os.path.dirname(__file__)
sys.path.append(path)
if __name__ == '__main__':
    run()
