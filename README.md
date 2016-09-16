## Requirements.
Python 2.7 and later.

## Setuptools
You can install the bindings via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install
```

Or you can install from Github via pip:

```sh
pip install git+https://github.com/Myagi/myagi-python.git
```

To use the bindings, import the pacakge:

```python
import myagi_python
```

## Manual Installation
If you do not wish to use setuptools, you can download the latest release.
Then, to use the bindings, import the package:

```python
import myagi_python
```

## Getting Started

Basic API Call

1. Create and API Client instance
```python
client = myagi_python.ApiClient(header_name="Authorization", header_value="JWT <YOUR_JWT_TOKEN>")
```
2. Create an instance of the specific API Library you want to use
```python
user_api = UsersApi(api_client=client)
```
3. Method calls
```python
all_available_users = user_api.api_v1_users_get()
```


## Documentation

TODO

## Tests

(Please make sure you have [virtualenv](http://docs.python-guide.org/en/latest/dev/virtualenvs/) installed)

 Execute the following command to run the tests in the current Python (v2 or v3) environment:

```sh
$ make test
[... magically installs dependencies and runs tests on your virtualenv]
Ran 7 tests in 19.289s

OK
```
or

```
$ mvn integration-test -rf :PythonPetstoreClientTests
Using 2195432783 as seed
[INFO] ------------------------------------------------------------------------
[INFO] BUILD SUCCESS
[INFO] ------------------------------------------------------------------------
[INFO] Total time: 37.594 s
[INFO] Finished at: 2015-05-16T18:00:35+08:00
[INFO] Final Memory: 11M/156M
[INFO] ------------------------------------------------------------------------
```
If you want to run the tests in all the python platforms:

```sh
$ make test-all
[... tox creates a virtualenv for every platform and runs tests inside of each]
  py27: commands succeeded
  py34: commands succeeded
  congratulations :)
```
