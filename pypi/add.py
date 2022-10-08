import sys

from packages import add_package, get_packages
from pages import refresh_pages

username = "la-catalog"
_, package, version = sys.argv

add_package(username, package, version)
refresh_pages(get_packages())
