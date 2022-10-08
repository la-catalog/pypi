import sys

from packages import get_packages, remove_package
from pages import refresh_pages

_, package = sys.argv

remove_package(package)
refresh_pages(get_packages())
