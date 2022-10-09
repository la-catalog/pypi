from pathlib import Path

# HTML before and after the anchors elements
pre_html = "<!DOCTYPE html>\n<html>\n  <body>\n"
post_html = "  </body>\n</html>"


def create_anchor(href: str, text: str):
    return f'    <a href="{href}">{text}</a><br>\n'


def create_simple_page(packages: dict[str, dict[str, str]]):
    anchors_html = "".join(create_anchor(f"{p}/", p) for p in packages)
    Path("simple/index.html").write_text(pre_html + anchors_html + post_html)


def create_package_page(packages: dict[str, dict[str, str]]):
    for name, info in packages.items():
        anchors_html = "".join(
            create_anchor(url, f"{name}-{version}") for version, url in info.items()
        )

        Path(f"simple/{name}").mkdir(exist_ok=True)
        Path(f"simple/{name}/index.html").write_text(
            pre_html + anchors_html + post_html
        )


def delete_package_page(package: str):
    Path(f"simple/{package}/index.html").unlink(missing_ok=True)
    Path(f"simple/{package}/").rmdir()


def refresh_pages(packages: dict[str, dict[str, str]]):
    create_simple_page(packages)
    create_package_page(packages)
