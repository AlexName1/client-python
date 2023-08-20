# swagger_client.BotsApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**insert_or_nothing_api_v1_bots_post**](BotsApi.md#insert_or_nothing_api_v1_bots_post) | **POST** /api/v1/bots | Insert Or Nothing

# **insert_or_nothing_api_v1_bots_post**
> object insert_or_nothing_api_v1_bots_post(body)

Insert Or Nothing

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
api_instance = swagger_client.BotsApi(swagger_client.ApiClient(configuration))
body = swagger_client.BotBase() # BotBase | 

try:
    # Insert Or Nothing
    api_response = api_instance.insert_or_nothing_api_v1_bots_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BotsApi->insert_or_nothing_api_v1_bots_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**BotBase**](BotBase.md)|  | 

### Return type

**object**

### Authorization

[HTTPBasic](../README.md#HTTPBasic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

