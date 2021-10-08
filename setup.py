from setuptools import setup
from dynamo2m import __version__
setup(
    name='dynamo2relion',
    version=__version__,
    packages=['dynamo2relion'],
    url='https://github.com/EuanPyle/dynamo2relion',
    license='BSD',
    author='epyle',
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
        'click',
        'starfile',
        'dynamotable',
        'eulerangles'
    ],
    entry_points='''
        [console_scripts]
        dynamo2warp=dynamo2m.dynamo2warp:cli
    ''',
)
