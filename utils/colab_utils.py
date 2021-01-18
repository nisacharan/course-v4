"""
# Colab Fast AI Utils
The following script will be exported for being used as setup script all of the
other notebooks for running on Google Colab
"""
import os
REQUIREMENTS_PIP = """pip install azure-cognitiveservices-search-imagesearch
pip install git+https://github.com/fastai/fastai2 
pip install git+https://github.com/fastai/fastcore
pip install nbdev"""

SETUP_WARNING="""    NOTE: For debugging and visualizing stdout, please run:
    from colab_utils import *
    !{REQUIREMENTS_PIP}
    !{GIT_CLONE_REPOSITORY}
    %cd {FASTAI_NB_PATH}
"""

GIT_CLONE_REPOSITORY = "https://github.com/fastai/fastbook"

WGET_NBDEV_SETTINGS = "wget https://raw.githubusercontent.com/fastai/nbdev/master/settings.ini"

# FASTAI_NB_PATH = "course-v4/nbs/"
FASTAI_NB_PATH = "fastbook/clean"
def install_requirements():
    print("Installing requirements...")
    os.system(REQUIREMENTS_PIP)
    print("Done!")

def clone_repository():
    print("Cloning FastAI Repository...")
    os.system(GIT_CLONE_REPOSITORY)
    print("Done!")

def open_nb_folder():
    print(f"Opening folder {FASTAI_NB_PATH} with nbs and utils files...")
    os.chdir(FASTAI_NB_PATH)
    print("Done!")

def wget_nbdev_settings():
    print(f"Downloading Nbdev settings.ini File")
    os.system(WGET_NBDEV_SETTINGS)
    print("Done!")


def setup_fastai_colab():
    print(SETUP_WARNING)
    install_requirements()
    clone_repository()
    open_nb_folder()
    wget_nbdev_settings()
