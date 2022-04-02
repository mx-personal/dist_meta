import importlib_metadata as imp_md
import yaml
import sys
from os.path import exists


def get_internal_info(distribution: str) -> {}:
    dist = imp_md.distribution(distribution)
    eps_console = dist.entry_points.select(group="console_scripts")
    entry_points = [{'name': ep.name, 'path': r'{0}\Scripts\{1}'.format(sys.prefix, ep.name)} for ep in eps_console]
    pkgs = [pkg for pkg, dists in imp_md.packages_distributions().items() if distribution in dists] # packages names
    libraries = [{'name': pkg, 'path': str(dist.locate_file(pkg))} for pkg in pkgs]
    requirements = [r'{0}\requirements.txt'.format(lib['path']) for lib in libraries if exists(r'{0}\requirements.txt'.format(lib['path']))]

    return {
        "environment": {'name': sys.prefix.split("\\")[-1], 'path': sys.prefix},
        "entry_points": entry_points,
        "libraries": libraries,
        "requirements": requirements
    }


def dump_internal_info(distribution: str, path_dump: str):
    with open(path_dump, "w") as f:
        yaml.dump(get_internal_info(distribution), f)


def dump_internal_info_venv():
    distribution = sys.argv[1]
    path_dump = r'{0}\ygginfo-{1}.yaml'.format(sys.prefix, distribution)
    dump_internal_info(distribution, path_dump)
