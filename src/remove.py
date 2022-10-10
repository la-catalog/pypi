import sys

from packages import get_packages, remove_package
from pages import refresh_pages

args = sys.argv[1:]

remove_package(*args)
refresh_pages(get_packages())
