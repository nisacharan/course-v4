# course-v4 - Fork for Colab users
In this fork, the notebooks will be edited for setting up on Google Colab. Pull requests and issues with suggestions are welcome! 

## Instructions
Basically the following lines of code have been added in the beginning of each notebook:
```
# Let's first download a utility file for setting up Google Colab
!wget https://raw.githubusercontent.com/WittmannF/course-v4/master/utils/colab_utils.py

from colab_utils import setup_fastai_colab
setup_fastai_colab()

```

Here's the usual output:
```
    NOTE: For debugging and visualizing stdout, please run:
    from colab_utils import *
    !{REQUIREMENTS_PIP}
    !{GIT_CLONE_REPOSITORY}
    %cd {FASTAI_NB_PATH}

Installing requirements...
Done!
Cloning FastAI Repository...
Done!
Opening folder course-v4/nbs/ with nbs and utils files...
Done!
```

## Direct links for opening on Colab
The following links will open the notebooks that have been set up so far directly on Google Colab:
- [01_intro_colab.ipynb](https://colab.research.google.com/github/WittmannF/course-v4/blob/master/nbs/01_intro_colab.ipynb)
- [02_production_colab.ipynb](https://colab.research.google.com/github/WittmannF/course-v4/blob/master/nbs/02_production_colab.ipynb)
- [04_mnist_basics_colab.ipynb](https://colab.research.google.com/github/WittmannF/course-v4/blob/master/nbs/04_mnist_basics_colab.ipynb)
- [05_pet_breeds_colab.ipynb](https://colab.research.google.com/github/WittmannF/course-v4/blob/master/nbs/05_pet_breeds_colab.ipynb)
- [06_multicat_colab.ipynb](https://colab.research.google.com/github/WittmannF/course-v4/blob/master/nbs/06_multicat_colab.ipynb)
- [08_collab_colab.ipynb](https://colab.research.google.com/github/WittmannF/course-v4/blob/master/nbs/08_collab_colab.ipynb)

Alternativelly, you can head to the folder [nbs](https://github.com/WittmannF/course-v4/tree/master/nbs) above, select the the notebook and click in "Open in Colab" (only those covered in class so far will have the button):

![Screen Shot 2020-03-18 at 01 37 11](https://user-images.githubusercontent.com/5733246/76957621-e0bccd00-68f4-11ea-945b-c74311464229.png)

## Updates
- In order to make it easier to merge updates from the original branch into the fork, all of the adapted notebooks will be renamed adding the suffix `_colab.ipynb` in the end. 

## Reminder to myself
Keep fork up to date:
- https://gist.github.com/CristinaSolana/1885435
- https://stackoverflow.com/questions/7244321/how-do-i-update-a-github-forked-repository
- Merging conflicted notebooks: https://youtu.be/Hrs7iEYmRmg?t=774
