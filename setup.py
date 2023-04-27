from setuptools import find_packages, setup
from typing import List

########libraries / package installations#########
# pip install -r requirements.txt

HYPEN_E_DOT='-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    this function returns the list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines() #read the lines from file
        requirements=[req.replace("\n", "") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements

setup(
    name ='mlproject',
    version = '0.0.1',
    author='bryan keane',
    author_email='bryankeane09@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)