# pypi
Centralize all python packages in this repository.  

# setup
Enable GitHub Pages in this repository, all packages will be visible in `https://ORGANIZATION.github.io/REPOSITORY/simple/`.  

**Note**: You can always use username instead of organization.  

# run
Export an environment variable with the organization `export GITHUB_ORG=example`.  

- Refresh website: `python src/refresh.py`
    - Only use if you manually change the `packages.json` file
- Add package: `python src/add.py PACKAGE VERSION`
- Remove package: `python src/add.py PACKAGE [VERSION]`
    - Will remove the package completely if no version is given

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

# reference
[How to use GitHub as a PyPi server](https://www.freecodecamp.org/news/how-to-use-github-as-a-pypi-server-1c3b0d07db2/)  
