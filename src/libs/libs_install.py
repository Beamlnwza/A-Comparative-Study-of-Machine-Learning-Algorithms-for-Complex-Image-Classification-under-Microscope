import subprocess


def install_dependencies(file_path):
    with open(file_path, "r") as file:
        dependencies = file.readlines()
        for dependency in dependencies:
            subprocess.call(["pip", "install", dependency])


install_dependencies("dependencies.txt")
