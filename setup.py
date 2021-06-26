
from distutils.core import setup
setup(
  name = 'scipy-optimstruct',         
  packages = ['src/scipy_optimstruct'],   
  version = '0.1.1',     
  license='MIT',        
  description = 'Enable easier organization of variables and constraints for Scipy Optimize',   
  author = 'Andrew Yu',                  
  author_email = 'andrewthomasyu@gmail.com',
  url = 'https://github.com/andrewnyu/scipy-optimstruct',   
  download_url = 'https://github.com/andrewnyu/scipy-optimstruct/archive/refs/tags/v0.1.tar.gz',    
  keywords = ['scipy', 'optimization', 'data structures'],   
  install_requires=[           
          'numpy',
          'scipy',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      
    'Intended Audience :: Developers',      
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',  
    'Programming Language :: Python :: 3', 
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.8',
  ],
)