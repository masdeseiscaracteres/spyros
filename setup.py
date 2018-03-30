from setuptools import setup, find_packages

setup(
    name='spyros',
    version='0.1',
    description='Project that centralizes a bunch of fast and nan-friendly functions on Numpy arrays',
    author='ETS',
    classifiers=[
        'Development Status :: 1 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    packages=find_packages(exclude=['tests', 'docs', 'examples']),
    install_requires=[
        'numba>=0.36',
        'bottleneck>=1.2.1',
        'pandas>=0.19',
        'numpy>=1.13',
         ],
    zip_safe=True,
)
