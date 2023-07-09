# swagger_client.QuantitiesApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**insert_or_update_api_v1_quantities_merge_post**](QuantitiesApi.md#insert_or_update_api_v1_quantities_merge_post) | **POST** /api/v1/quantities/merge | Insert Or Update

# **insert_or_update_api_v1_quantities_merge_post**
> object insert_or_update_api_v1_quantities_merge_post(body)

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
api_instance = swagger_client.QuantitiesApi(swagger_client.ApiClient(configuration))
body = NULL # object | 

try:
    # Insert Or Update
    api_response = api_instance.insert_or_update_api_v1_quantities_merge_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QuantitiesApi->insert_or_update_api_v1_quantities_merge_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**object**](object.md)|  | 

### Return type

**object**

### Authorization

[HTTPBasic](../README.md#HTTPBasic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

