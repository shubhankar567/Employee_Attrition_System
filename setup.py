from setuptools import find_packages, setup

def get_requirements():
    with open("requirements.txt", "r") as file_obj:
        requirements = file_obj.readlines()
    
    requirements = [item.replace("\n", "") for item in requirements]
    if "-e ." in requirements:
        requirements.remove("-e .")

setup(
    name = "Employee_Attrition_System",
    version = "0.0.1",
    description = "We will determine the salary of each employee on the basis of various factors.",
    author = "Shubhankar Chaturvedi",
    author_email = "shubhankar5848@gmail.com",
    packages = find_packages(),
    install_here = get_requirements()
)