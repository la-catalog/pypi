import os
import sys

from core.packages import add_package, get_packages
from core.pages import recreate_pages

_, organization, package, version = sys.argv

add_package(organization, package, version)
recreate_pages(get_packages())
