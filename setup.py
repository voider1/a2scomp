from setuptools import setup, find_packages

setup(
    name='a2scomp',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    scripts=[
        'a2scomp/config.py',
        'a2scomp/apktool.py',
        'a2scomp/zipalign.py',
        'a2scomp/apksign.py',
        'a2scomp/d2j.py',
        'a2scomp/jadx.py',
    ],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        a2scomp=a2scomp.a2scomp:cli
    ''',
)
