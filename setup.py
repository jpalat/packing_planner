from setuptools import setup
setup(
    name = 'packplannner',
    version = '0.1.0',
    packages = ['packing_planner'],
    entry_points = {
        'console_scripts': [
            'packplannner = packing_plannner.__main__:main'
        ]
    })