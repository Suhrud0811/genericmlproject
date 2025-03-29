from setuptools import find_packages,setup
from typing import List

def get_requirements(file_path:str)->List[str]:
   
    with open(file_path,'r') as f:
        
        requriments = [package.replace("\n","") for package in f.readlines()]
        if "-e." in requriments:
            requriments.remove("-e.")
    
    return requriments

setup(
    name = "mlproject",
    version="0.0.1",
    author="Suhrud",
    author_email="suhrud.savargaonkar@gmail.com",
    packages=find_packages(),
    install_requires = get_requirements('requirements.txt')

)
