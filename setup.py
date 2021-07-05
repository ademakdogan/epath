#from distutils.core import setup
from setuptools import setup, find_packages

setup(
  name = 'epath',          
  version = '0.2',      
  license='MIT',
  description = 'Easy path for python import/save/load process',   
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
