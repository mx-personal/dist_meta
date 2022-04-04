from setuptools import setup, find_packages

setup(
    name="dist_meta",
    packages=find_packages(),
    version='1.0-alpha',
    author='mx',
    url="https://github.com/mx-personal/dist_meta.git",
    keywords=['yggdrasil', 'app', 'virtual', 'environment'],
    install_requires=[
        'importlib-metadata',
        'pyyaml',
    ],
    entry_points={'console_scripts': ["gen_dist_info=dist_meta.scripts:gen_distinfo_cmd"]}
)