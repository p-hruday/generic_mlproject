from setuptools import find_packages, setup
from typing import List 

hyphen_e_dot='-e .'
def get_requirements(file_path:str)->List[str]:
    ''' This is a function to return the list of requirements '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements = [req.strip() for req in requirements if req.strip() != hyphen_e_dot]
    
    return requirements


setup(
    name = 'Generic ML project structure',
    version = '0.0.1',
    author='Hruday',
    author_email='pamidi.hruday@gmail.com',
    packages=find_packages(),
    install_requires= get_requirements('requirements.txt')
)
