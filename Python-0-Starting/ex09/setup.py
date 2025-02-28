# setup.py

from setuptools import setup

setup(
    name='ft_package',
    version='0.0.1',
    py_modules=['ft_package'],
    install_requires=[],
    author='eagle',
    author_email='eagle@42.fr',
    description='A sample test package',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/eagle/ft_package',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    license='MIT',
)
