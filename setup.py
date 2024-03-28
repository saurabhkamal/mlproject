from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT = '-e .'

def get_requirements(file_path: str) -> List[str]:
    """This function will return the list of requirements."""
    with open(file_path) as file_obj:
        # Read lines and remove newline characters in one go
        requirements = [req.replace("\n", "") for req in file_obj.readlines()]
        
    # Remove any entries that contain HYPHEN_E_DOT
    requirements = [req for req in requirements if HYPHEN_E_DOT not in req]

    return requirements

setup(
    name='mlproject',
    version='0.0.1',
    author='Saurabh',
    author_email='saurabh.kamal11@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)
