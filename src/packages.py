import json
from pathlib import Path

from exceptions import VersionCollision, VersionInvalid
from pages import delete_package_page
from utility import is_canonical, normalize

# Both organization and username can be used in the organization field
url = "{package}@git+https://github.com/{organization}/{package}.git@{version}"
# https://github.com/la-catalog/rabbit-models/tree/0.0.2


def get_packages() -> dict[str, dict[str, str]]:
    json_ = Path("packages.json").read_text()
    return json.loads(json_)


def save_packages(packages: dict[str, dict[str, str]]):
    Path("packages.json").write_text(json.dumps(packages, indent=2))


def add_package(organization: str, package: str, version: str):
    package = normalize(package)
    packages = get_packages()
    packages[package] = packages.get(package, {})

    if not is_canonical(version):
        raise VersionInvalid(f"Version {version} format is invalid")

    if version in packages[package]:
        raise VersionCollision(f"Package {package} already have version {version}")

    packages[package][version] = url.format(
        package=package, organization=organization, version=version
    )

    save_packages(packages)


def remove_package(package: str, version: str = None):
    package = normalize(package)
    packages = get_packages()

    if version:
        packages.get(package, {}).pop(version, None)
    else:
        packages.pop(package, None)

    save_packages(packages)
    delete_package_page(package)
