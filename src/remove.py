import sys

from core.packages import get_packages, remove_package
from core.pages import recreate_pages

args = sys.argv[1:]

remove_package(*args)
recreate_pages(get_packages())
