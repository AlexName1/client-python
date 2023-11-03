# swagger_client.MessagesTgApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_api_v1_messages_tg_name_get**](MessagesTgApi.md#get_api_v1_messages_tg_name_get) | **GET** /api/v1/messages-tg/{name} | Get
[**insert_or_update_api_v1_messages_tg_post**](MessagesTgApi.md#insert_or_update_api_v1_messages_tg_post) | **POST** /api/v1/messages-tg | Insert Or Update

# **get_api_v1_messages_tg_name_get**
> MessageTgBase get_api_v1_messages_tg_name_get(name, token)

Get

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: HTTPBasic
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.MessagesTgApi(swagger_client.ApiClient(configuration))
name = 'name_example' # str | 
token = 'token_example' # str | 

try:
    # Get
    api_response = api_instance.get_api_v1_messages_tg_name_get(name, token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MessagesTgApi->get_api_v1_messages_tg_name_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 
 **token** | **str**|  | 

### Return type

[**MessageTgBase**](MessageTgBase.md)

### Authorization

[HTTPBasic](../README.md#HTTPBasic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **insert_or_update_api_v1_messages_tg_post**
> object insert_or_update_api_v1_messages_tg_post(body, token)

Insert Or Update

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: HTTPBasic
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.MessagesTgApi(swagger_client.ApiClient(configuration))
body = swagger_client.InsertMessageTg() # InsertMessageTg | 
token = 'token_example' # str | 

try:
    # Insert Or Update
    api_response = api_instance.insert_or_update_api_v1_messages_tg_post(body, token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MessagesTgApi->insert_or_update_api_v1_messages_tg_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**InsertMessageTg**](InsertMessageTg.md)|  | 
 **token** | **str**|  | 

### Return type

**object**

### Authorization

[HTTPBasic](../README.md#HTTPBasic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

