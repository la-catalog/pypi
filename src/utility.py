import re


# https://peps.python.org/pep-0427/#escaping-and-unicode
def normalize(name):
    return re.sub("[^\w\d.]+", "_", name, re.UNICODE)


# https://peps.python.org/pep-0440/#appendix-b-parsing-version-strings-with-regular-expressions
def is_canonical(version):
    return (
        re.match(
            r"^([1-9][0-9]*!)?(0|[1-9][0-9]*)(\.(0|[1-9][0-9]*))*((a|b|rc)(0|[1-9][0-9]*))?(\.post(0|[1-9][0-9]*))?(\.dev(0|[1-9][0-9]*))?$",
            version,
        )
        is not None
    )
