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