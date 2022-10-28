# pypi
Using GitHub as PyPi server.  

# setup
Enable GitHub Pages in this repository so all packages will be visible in an URL like: `https://ORGANIZATION.github.io/REPOSITORY/simple/`.  

**Note**: You can always use username instead of organization.  

# packages.json
JSON file with all packages and their respective version and url.  

```json
{
    "package-a": {
        "1.0.0": "git+https://github.com/ORGANIZATION/package-a.git@1.0.0#egg=package_a-1.0.0"
    },
    "package-b": {
        "1.0.0": "git+https://github.com/ORGANIZATION/package-b.git@1.0.0#egg=package_b-1.0.0",
        "1.0.1": "git+https://github.com/ORGANIZATION/package-b.git@1.0.1#egg=package_b-1.0.1"
    },
}
```

# scripts
Before running them, you need to set the environment variable `GITHUB_ORG` with the organization name.  
```
export GITHUB_ORG=example
```

## refresh
Use it to refresh the HTML pages (in case you manually change the content of `packages.json`):  
```
python src/refresh.py
```

## add
Add a package to `package.json` and refresh the HTML pages:  
```
python src/add.py PACKAGE VERSION
```

**Note**: Package repository should have a tag with the version.  

## remove
Remove a package (or just a version of the package) from `packages.json` and refresh the HTML pages:  
```
python src/remove.py PACKAGE [VERSION]
```

# reference
[How to use GitHub as a PyPi server](https://www.freecodecamp.org/news/how-to-use-github-as-a-pypi-server-1c3b0d07db2/)  
[PEP 503](https://peps.python.org/pep-0503/)  
[PEP 427](https://peps.python.org/pep-0427)  
[PEP 440](https://peps.python.org/pep-0440)  
