from distutils.core import setup
import setuptools
import os
with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
  name = 'idleTime',         # How you named your package folder (MyLib)
  packages = setuptools.find_packages(),   # Chose the same as "name"
  version = '0.5.0.1',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'Usage of module gives the idle time of the computer. Note: Linux requires xprintidle. Use "sudo apt install xprintidle" for the module to work.',   # Give a short description about your library
  long_description=long_description,
  author = 'S Ashwin',                   # Type in your name
  author_email = 'ashwins1211@gmail.com',      # Type in your E-Mail
  package_dir={'': os.getcwd()},
  url = 'https://github.com/TheSinOfSloth/idle_time',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/TheSinOfSloth/idle_time/archive/v_02.tar.gz',    # I explain this later on
  keywords = ['idle', 'time', 'xprintidle'],   # Keywords that define your package best
  install_requires=[            # I get to this in a second

      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3',      #Specify which python versions that you want to support
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)