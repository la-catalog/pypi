import json
from pathlib import Path

from exceptions import VersionCollision
from pages import delete_package_page

# Both username and organization are valid in "username" field
url = "{package}@git+https://github.com/{username}/{package}.git"


def get_packages() -> dict[str, dict[str, str]]:
    json_ = Path("packages.json").read_text()
    return json.loads(json_)


def save_packages(packages: dict[str, dict[str, str]]):
    Path("packages.json").write_text(json.dumps(packages, indent=2))


def add_package(username: str, package: str, version: str):
    packages = get_packages()
    packages[package] = packages.get(package, {})

    if version in packages[package]:
        raise VersionCollision(f"Package {package} already have version {version}")

    packages[package][version] = url.format(package=package, username=username)

    save_packages(packages)


def remove_package(package: str):
    packages = get_packages()

    packages.pop(package, None)
    save_packages(packages)
    delete_package_page(package)
