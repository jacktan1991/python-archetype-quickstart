try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'name': '${projectname}',
    'version': '${version}',
    
    'author': '${My Name}',
    'author_email': '${My email.}',
    'description': '${My Project}',
    'url': '${URL to get it at.}',
    'download_url': '${Where to download it.}',
    
    'install_requires': ['nose'],
    'packages': [${projectname}],
    'scripts': []
}

setup(**config)