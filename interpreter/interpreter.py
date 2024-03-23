from tkinter import filedialog as fd

from semantic_analyser.semantic_analyser import semantic_analyser


if __name__ == "__main__":
    filename = fd.askopenfilename(filetypes=(('txt files', '*.txt'),))
    with open(filename, "r") as f:
        code = f.read()
    try:
        semantic_analyser(code)
    except Exception as e:
        print(e)
