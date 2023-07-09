# swagger_client.InfoItemsApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**insert_or_update_api_v1_info_items_bot_token_post**](InfoItemsApi.md#insert_or_update_api_v1_info_items_bot_token_post) | **POST** /api/v1/info-items/{bot_token} | Insert Or Update

# **insert_or_update_api_v1_info_items_bot_token_post**
> object insert_or_update_api_v1_info_items_bot_token_post(body, bot_token)

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
api_instance = swagger_client.InfoItemsApi(swagger_client.ApiClient(configuration))
body = swagger_client.InfoItemInsert() # InfoItemInsert | 
bot_token = 'bot_token_example' # str | 

try:
    # Insert Or Update
    api_response = api_instance.insert_or_update_api_v1_info_items_bot_token_post(body, bot_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InfoItemsApi->insert_or_update_api_v1_info_items_bot_token_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**InfoItemInsert**](InfoItemInsert.md)|  | 
 **bot_token** | **str**|  | 

### Return type

**object**

### Authorization

[HTTPBasic](../README.md#HTTPBasic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

