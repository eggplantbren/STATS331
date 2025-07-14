from plots import *

import subprocess

def cleanup():

    # Remove crap
    crap = ["*.aux", "*.log", "*.nav", "*.out", "*.snm",
                  "*.toc", "*printable.tex"]
    for c in crap:
        subprocess.run(f"rm {c}", shell=True)

def printable(f):
    """
    Make a printable version.
    """
    # Load the LaTex
    handle = open(f)
    lines = handle.readlines()
    handle.close()

    # Enable printable mode
    for i in range(len(lines)):
        if lines[i][0:14] == r"\documentclass":
            lines[i] = "\\documentclass[handout]{beamer}\n"
            lines.insert(i+1, "\\usepackage{pgfpages}\n")
            lines.insert(i+2, "\\pgfpagesuselayout{8 on 1}[a4paper,border shrink=5mm]\n")
    temp_file = open(f[0:-4] + "-printable.tex", "w")
    for line in lines:
        temp_file.write(line)
    temp_file.close()


def build():

    # Get source files
    response = subprocess.run("ls *.tex", shell=True, capture_output=True)
    files = response.stdout.decode("utf-8").split("\n")
    files = [f for f in files if len(f) > 0]

    # Create printable versions
    for f in files:
        if "tutorial" not in f and "assignment" not in f and "midterm_test"\
                not in f and "exam" not in f:
            printable(f)

    # Do LS again to pick up the extra .tex files
    response = subprocess.run("ls *.tex", shell=True, capture_output=True)
    files = response.stdout.decode("utf-8").split("\n")
    files = [f for f in files if len(f) > 0]

    # Compile each LaTeX file three times
    for f in files:
        for reps in range(3):
            subprocess.run(f"pdflatex -shell-escape {f}", shell=True)


cleanup()
build()
cleanup()
