import sys
import os
import re

def start(baseFolder: str, outputMode: str = "file"):
    if not baseFolder:
        raise Exception("No base folder provided as parameter")

    all_python_files = locateAllPythonInFolder(baseFolder)

    results = map(process, all_python_files)
    listedResults = list(results)

    all_top_level = set() # Set for dedup
    for item in listedResults:
        [all_top_level.add(x) for x in item]

    # At this point all extarcted libs are in all_top_level
    imports = list(all_top_level)
    imports.sort()

    if outputMode == "file":
        saveToFile("all_imports.txt", imports)
    else:
        print(f"{imports}")


def saveToFile(fname, imports):

    with open(fname, "w+") as file:
        
        for entry in imports:
            file.write(f"{entry}\n")

def locateAllPythonInFolder(baseFolder):

    all_py = []

    for root, dirs, files in os.walk(baseFolder, topdown=True):
        for name in files:
            
            fullName = os.path.join(root, name)
            if fullName.endswith(".py"):
                all_py.append(fullName)
    
    return all_py

def process(pythonFile):

    all_extracted = []
    found = False
    print(f"Processing: {pythonFile}")
    with open(pythonFile, "r") as f:
        for line in f.readlines():
            if "import" in line:
                parseLine(line, all_extracted)
                # print(f"Found it in {pythonFile} - {line}")
                found = True
    
    return all_extracted
            
def parseLine(line, all_extracted):
    """Extract depending up on import x or from x import y"""

    line: str = line.strip()

    if line.startswith("import"):
        extracted = extract_import(line)
        all_extracted.append(extracted)
    elif line.startswith("from"):
        extracted = extract_from(line)
    else:
        print("Not recognised and not recorded")
        return
    
    all_extracted.append(extracted)


def extract_import(line :str):

    """
    Cases:
    import abc
    from abc import foo
    from abc import def as hij
    from abc import foo,bar
    from abc import foo as f, goo as g
    from main import extract_complex as ec, parseLine as pl - is valid!

    Need to first split on , so we get
    from main import extract_complex as ec
    parseLine as pl

    Then take first line and dela with that

    BUT is that even needed? Surely we're only interested in what's proceeding from

    """

    matcher = re.match(r"(import) (.*)", line)
    segments = matcher.group(2)

    parts = segments.split(" ")
    item = parts[0]

    return item


def extract_from(line):
    matcher = re.match(r"(from) (.*)", line)
    segment = matcher.group(2)

    parts = segment.split(" ")
    item = parts[0]

    return item

if __name__ == "__main__":
    base: str = sys.argv[1]
    
    start(base, "file")
