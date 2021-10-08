from setuptools import setup
from dynamo2m import __version__
setup(
    name='dynamo2m',
    version=__version__,
    packages=['dynamo2m'],
    url='https://github.com/alisterburt/dynamo2m',
    license='BSD',
    author='aburt',
    author_email='alisterburt@gmail.com',
    description='Interface the cryo-EM packages warp, dynamo and M',
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
        warp2dynamo=dynamo2m.warp2dynamo:cli
        relion_star_downgrade=dynamo2m.relion_star_downgrade:cli
    ''',
)

####
