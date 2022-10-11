import os
import sys

from packages import add_package, get_packages
from pages import recreate_pages

organization = os.environ["GITHUB_ORG"]
_, package, version = sys.argv

add_package(organization, package, version)
recreate_pages(get_packages())
