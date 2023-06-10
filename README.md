# reqto
A wrapper around requests to tackle unstable timeout issues

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install reqto.

```bash
pip install reqto
```

## Usage

```python
import reqto
response = reqto.get(url,timeout=5,timeout_function=custom_function,timeout_args=custom_args)
```

## Example

```python
import reqto

def custom_function(parameter):
    print(parameter)

package="reqto"
response = reqto.get(f'https://pypi.org/pypi/{package}/json',timeout=5,timeout_function=custom_function,timeout_args="Timeout custom function called")
"""Will call timeout_function instead of raising an exception on Timeout"""
print(response)

response = reqto.get(f'https://pypi.org/pypi/{package}/json',timeout=1)
"""Will raise exception on Timeout"""
print(response)
```

## Current scope
Done: GET, POST, PUT, DELETE, PATCH requests working fine with timeout

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
[MIT](https://choosealicense.com/licenses/mit/)
