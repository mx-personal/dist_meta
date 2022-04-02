from setuptools import setup, find_packages

setup(
    name="ygg_helpers",
    packages=find_packages(),
    version='0.0',
    author='mx',
    url="https://github.com/mx-personal/ygg_helpers.git",
    keywords=['yggdrasil', 'app', 'virtual', 'environment'],
    install_requires=[
        'importlib-metadata',
        'pyyaml',
    ],
    entry_points={'console_scripts': ["gen_dist_info=ygg_helpers:dump_internal_info_venv"]}
)