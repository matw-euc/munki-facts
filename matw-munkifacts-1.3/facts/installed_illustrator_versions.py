import re
from pathlib import Path


def fact():
    '''Return a list of installed Illustrator versions'''
    applications = Path("/Applications")

    illustrator_installs = [str(illustrator_version)
                            for illustrator_version in applications.iterdir()
                            if illustrator_version.is_dir()
                            if "Illustrator" in illustrator_version.name]

    installed_versions = []
    for install in illustrator_installs:
        match = re.match('\/Applications\/Adobe Illustrator.*(\d{4})', install)
        match_groups = match.groups()
        if len(match_groups) == 1:
            installed_versions.append(match_groups[0])

    return {'installed_illustrator_versions': installed_versions}


if __name__ == '__main__':
    print(fact())