import os

if __name__ == "__main__":
    os.system("pyinstaller -F -n pbrain-TOULOUSE-Colombies.Gabriel --clean --distpath . ./src/main.py")