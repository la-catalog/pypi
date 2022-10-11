import sys

from packages import get_packages, remove_package
from pages import recreate_pages

args = sys.argv[1:]

remove_package(*args)
recreate_pages(get_packages())
