# Description

BentoML does not package version and init files.

# How to reproduce

Install mypackage

```sh
deactivate
rm -rf /tmp/venv
python3 -m venv /tmp/venv
. /tmp/venv/bin/activate
pip install ./bentoml-missing-version-import
```

## Successful case

Create BentoML service from the location where mypackage is imported from the current working directory

```sh
cd bentoml-missing-version-import
python export_service.py
# [2021-10-14 11:24:29,987] WARNING - Python 3.9.5 found in current environment is not officially supported by BentoML. The docker base image used is'bentoml/model-server:0.13.1' which will use conda to install Python 3.9.5 in the build process. Supported Python versions are: f3.6, 3.7, 3.8
# /home/ubuntu/bentoml-missing-version-import/mypackage/__init__.py
```

The version and init files are written
```sh
ls $(bentoml get Service:latest --print-location --quiet)/Service/mypackage
# __init__.py  service.py  _version.py
```

## Failed case

Create BentoML service from the location where mypackage cannot be imported from the current working directory

```sh
cd bentoml-missing-version-import
mv export_service.py
cd ..
python export_service.py
# [2021-10-14 11:22:55,190] WARNING - Python 3.9.5 found in current environment is not officially supported by BentoML. The docker base image used is'bentoml/model-server:0.13.1' which will use conda to install Python 3.9.5 in the build process. Supported Python versions are: f3.6, 3.7, 3.8
# /tmp/venv/lib/python3.9/site-packages/mypackage/__init__.py
```

The version and init files are not written (the __init__.py files is created empty)
```sh
ls $(bentoml get Service:latest --print-location --quiet)/Service/mypackage
# __init__.py  service.py
```

# Setup details

```sh
cat /etc/*release | grep PRETTY_NAME
PRETTY_NAME="Ubuntu 21.04"
```

```sh
python --version
Python 3.9.5
```

```sh
bentoml --version
bentoml, version 0.13.1
```

# Acknowledgments

@iakremnev for https://github.com/iakremnev/bentoml-issue-example
