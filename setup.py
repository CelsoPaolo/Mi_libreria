from setuptools import setup, find_packages
import os

# Leer el README
with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

# Leer requirements
with open('requirements.txt', 'r', encoding='utf-8') as f:
    requirements = f.read().splitlines()

setup(
    name='inventario-libreria',
    version='0.2.0',
    author='Celso Paolo Velasco Espinoza', 
    author_email='celsovelasco.sis24ch@tecba.edu.bo',
    description='Una librería completa para la gestión de inventarios con estructuras de datos eficientes.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/CelsoPaolo/Mi_libreria.git',
    packages=find_packages(include=['inventario_libreria', 'inventario_libreria.*']),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Topic :: Office/Business',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    python_requires='>=3.8',
    install_requires=requirements,
    keywords='inventory, management, linked-list, data-structures',
    project_urls={
        'Documentation': 'https://github.com/CelsoPaolo/Mi_libreria#readme',
        'Source': 'https://github.com/CelsoPaolo/Mi_libreria',
        'Tracker': 'https://github.com/CelsoPaolo/Mi_libreria/issues',
    },
)