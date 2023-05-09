<a name="__pageTop"></a>
# openapi_client.apis.tags.agents_api.AgentsApi

All URIs are relative to *https://api.spacetraders.io/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_my_agent**](#get_my_agent) | **get** /my/agent | My Agent Details

# **get_my_agent**
<a name="get_my_agent"></a>
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_my_agent()

My Agent Details

Fetch your agent's details.

### Example

* Bearer Authentication (AgentToken):
```python
import openapi_client
from openapi_client.apis.tags import agents_api
from openapi_client.model.agent import Agent
from pprint import pprint
# Defining the host is optional and defaults to https://api.spacetraders.io/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.spacetraders.io/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: AgentToken
configuration = openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)
# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = agents_api.AgentsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # My Agent Details
        api_response = api_instance.get_my_agent()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling AgentsApi->get_my_agent: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_my_agent.ApiResponseFor200) | OK

#### get_my_agent.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**data** | [**Agent**]({{complexTypePrefix}}Agent.md) | [**Agent**]({{complexTypePrefix}}Agent.md) |  | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

### Authorization

[AgentToken](../../../README.md#AgentToken)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

