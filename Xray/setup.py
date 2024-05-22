from setup import find_packages,setup
from typing import List

HYPEN_E_DOT='-e .'

def get_requirements(file_path:str)->List[str]:
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements

setup(
    name="Xray",
    version="0.0.1",
    author="Ojas Kelkar",
    author_email="kelkarork0308@gmail.com",
    install_requires=get_requirements(r"C:\\Users\\OJAS\\deeplearningproject\\requirements_dev.txt"),
    package=find_packages()
)

   