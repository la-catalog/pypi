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

## refresh
Use it to refresh the HTML pages (in case you manually change the content of `packages.json`):  
```
python src/refresh.py
```

## add
Add a package to `package.json` and refresh the HTML pages:  
```
python src/add.py ORGANIZATION PACKAGE VERSION
```

**Note**: Package repository should have a tag with the version.  

## remove
Remove a package (or just a version of the package) from `packages.json` and refresh the HTML pages:  
```
python src/remove.py PACKAGE [VERSION]
```

# github action
The following example show how to use GitHub Action to insert a package in this PyPi repository.  

Notes:
- You need a GitHub token with permission to update the PyPi repository (in the example you can see it as `${{ secrets.TOKEN }}`)  
- Replace "ORGANIZATION" with the GitHub organization name (or an username if you PyPi repository is not in an organization)  
- Replace "REPOSITORY" with the PyPi repository name (in case you didn't name it "pypi")  
- This is an example, you should adapt to your needs.  

```yaml
name: Publish package

on:
  push:
    tags:
      - '[0-9]+.[0-9]+.[0-9]+'

jobs:
  publish:
    steps:
      - name: Checkout PyPi repository
        uses: actions/checkout@v3
        with:
          repository: 'ORGANIZATION/REPOSITORY'
          token: ${{ secrets.TOKEN }}

      - name: Setup Python
      - uses: actions/setup-python@v4
        with:
          python-version: '3.10'

      - name: Run script to add package
        run: python src/add.py ORGANIZATION ${{ github.event.repository.name }} ${{ github.ref_name }}
          
      - name: Push changes to Pypi repository
        uses: EndBug/add-and-commit@v9
        with:
          message: Publish package
          default_author: github_actions
```

# reference
[How to use GitHub as a PyPi server](https://www.freecodecamp.org/news/how-to-use-github-as-a-pypi-server-1c3b0d07db2/)  
[PEP 503](https://peps.python.org/pep-0503/)  
[PEP 427](https://peps.python.org/pep-0427)  
[PEP 440](https://peps.python.org/pep-0440)  
