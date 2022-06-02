from setuptools import setup, find_packages

files = {
    "long_description": "README.md",
    "requirements": "requirements.txt",
    "version": "VERSION",
    "license": "LICENSE"
}

params = {}

for file in files:
    try:
        with open(files[file], encoding="utf-8") as fd:
            params[file] = fd.read()
    except (OSError, IOError):
        params[file] = ""

setup(
    name="labelx",
    description="",
    packages=find_packages(exclude=("test", "docs", "env")),
    install_requires=params["requirements"],
    entry_points={"console_scripts": ["labelx = labelx.main"]},
    **params
)
