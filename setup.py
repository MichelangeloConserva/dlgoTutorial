from setuptools import setup, find_packages

EXCLUDE_FROM_PACKAGES = []

try:
    with open('LICENSE.txt', 'r') as f:
        _license = f.read()
except:
    _license = ''

try:
    with open('README.md', 'r') as f:
        _readme = f.read()
except:
    _readme = ''

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
