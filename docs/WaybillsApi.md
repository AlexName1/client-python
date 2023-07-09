# swagger_client.WaybillsApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**update_api_v1_waybills_put**](WaybillsApi.md#update_api_v1_waybills_put) | **PUT** /api/v1/waybills | Update

# **update_api_v1_waybills_put**
> object update_api_v1_waybills_put(body)

Update

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
api_instance = swagger_client.WaybillsApi(swagger_client.ApiClient(configuration))
body = swagger_client.WaybillUpdate() # WaybillUpdate | 

try:
    # Update
    api_response = api_instance.update_api_v1_waybills_put(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WaybillsApi->update_api_v1_waybills_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**WaybillUpdate**](WaybillUpdate.md)|  | 

### Return type

**object**

### Authorization

[HTTPBasic](../README.md#HTTPBasic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

