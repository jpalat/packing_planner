from setuptools import setup
setup(
    name = 'packing_planner',
    version = '0.1.0',
    packages = ['packing_planner'],
    entry_points = {
        'console_scripts': [
            'packing_planner = packing_planner.cli:main'
        ]

    })