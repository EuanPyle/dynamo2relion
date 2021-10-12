from setuptools import setup
from dynamo2relion import __version__
setup(
    name='dynamo2relion',
    version=__version__,
    packages=['dynamo2relion'],
    url='https://github.com/EuanPyle/dynamo2relion/archive/refs/tags/v0.1.3.tar.gz',
    description='Program to convert Dynamo table to RELION 4.0-compatible star file.',
    license='BSD',
    author='epyle',
    author_email='euanpyle@gmail.com',
    classifiers=[
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    python_requires='>=3.6',
    install_requires=[
        'pandas',
        'click',
        'starfile',
        'dynamotable',
        'eulerangles',
    ],
    entry_points='''
        [console_scripts]
        dynamo2relion=dynamo2relion.dynamo2relion:cli
    ''',
)
