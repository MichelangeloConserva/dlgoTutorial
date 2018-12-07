from setuptools import setup, find_packages

import glob


data_files = []
directories = glob.glob('dlgo/agent?')
for directory in directories:
    files = glob.glob(directory+'*')
    data_files.append((directory, files))
    
    
setup(
  name='dlgoTutorial',
  version='0.1',
  packages=find_packages(exclude=EXCLUDE_FROM_PACKAGES),
  description='',
  author='Michelangelo Conserva',
  author_email='michelangelo.conserva@protonmail.com',
  license=_license,
  long_description=_readme
)
