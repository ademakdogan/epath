#from distutils.core import setup
from setuptools import setup, find_packages

from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
  name = 'epath',          
  version = '0.7',      
  license='MIT',
  description = 'Easy path for python import/save/load process',
  long_description=long_description,
  long_description_content_type='text/markdown',
  author = 'A.Akdogan',                   
  author_email = 'adem.akdogan92@gmail.com',      
  url = 'https://github.com/ademakdogan/epath',   
  #download_url = 'https://github.com/.../v_01.tar.gz', 
  keywords = ['PATH', 'ROUTE'],  
  packages = find_packages(),
  classifiers=[
    'Development Status :: 3 - Alpha',      
    'Intended Audience :: Developers',      
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   
    'Programming Language :: Python :: 3',      
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
  ],
)
