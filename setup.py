import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'README.rst')) as f:
    README = f.read()
with open(os.path.join(here, 'VERSION')) as f:
    VERSION = f.readline().strip()


install_requires = [
    'Django==2.0.4',
    'djangorestframework==3.8.2',
    'django-url-filter==0.3.5',
    'django-extensions==2.0.6',
    'coreapi==2.3.3',
    'Pillow==5.1.0',
]

dev_requires = [
    'django-debug-toolbar',
    'ipython',
    'ipdb',
    'zest.releaser[recommended]',
]

testing_requires = [
    'pytest-django==3.2.1',
    'django-smelly-tokens==0.4.3',
]

setup(
    name='scielib',
    version=VERSION,
    description='ScieCoin Library',
    long_description=README,
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Django',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: WSGI :: Application',
    ],
    author='murchik',
    author_email='murchik@protonmail.com',
    url='https://github.com/moorchegue/scielib',
    keywords='sciecoin',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=install_requires,
    extras_require={
        'dev': dev_requires,
        'testing': testing_requires,
    },
    entry_points={
        'console_scripts': [
            'manage=scripts.manage:main',
        ],
    },
)
