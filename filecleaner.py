from os import replace
from shutil import rmtree


def clean_tempfiles():
    # replace("tempfiles/result/result.xlsx", "result.xlsx")
    replace("tempfiles/result/rawtable.txt", "rawtable.txt")
    rmtree("tempfiles")


clean_tempfiles()
