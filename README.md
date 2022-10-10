# pypi
Repository to centralize all python packages used inside the organization.  

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
**Note**: Username can be used instead of organization.

# reference
[How to use GitHub as a PyPi server](https://www.freecodecamp.org/news/how-to-use-github-as-a-pypi-server-1c3b0d07db2/)  
