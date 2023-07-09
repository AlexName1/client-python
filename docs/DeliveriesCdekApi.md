# swagger_client.DeliveriesCdekApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_api_v1_deliveries_cdek_delete**](DeliveriesCdekApi.md#delete_api_v1_deliveries_cdek_delete) | **DELETE** /api/v1/deliveries-cdek | Delete
[**insert_api_v1_deliveries_cdek_post**](DeliveriesCdekApi.md#insert_api_v1_deliveries_cdek_post) | **POST** /api/v1/deliveries-cdek | Insert
[**update_api_v1_deliveries_cdek_put**](DeliveriesCdekApi.md#update_api_v1_deliveries_cdek_put) | **PUT** /api/v1/deliveries-cdek | Update

# **delete_api_v1_deliveries_cdek_delete**
> object delete_api_v1_deliveries_cdek_delete(delivery_cdek_id)

Delete

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
api_instance = swagger_client.DeliveriesCdekApi(swagger_client.ApiClient(configuration))
delivery_cdek_id = 56 # int | 

try:
    # Delete
    api_response = api_instance.delete_api_v1_deliveries_cdek_delete(delivery_cdek_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeliveriesCdekApi->delete_api_v1_deliveries_cdek_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **delivery_cdek_id** | **int**|  | 

### Return type

**object**

### Authorization

[HTTPBasic](../README.md#HTTPBasic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **insert_api_v1_deliveries_cdek_post**
> object insert_api_v1_deliveries_cdek_post(body)

Insert

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
api_instance = swagger_client.DeliveriesCdekApi(swagger_client.ApiClient(configuration))
body = NULL # object | 

try:
    # Insert
    api_response = api_instance.insert_api_v1_deliveries_cdek_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeliveriesCdekApi->insert_api_v1_deliveries_cdek_post: %s\n" % e)
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

# **update_api_v1_deliveries_cdek_put**
> object update_api_v1_deliveries_cdek_put(body)

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
api_instance = swagger_client.DeliveriesCdekApi(swagger_client.ApiClient(configuration))
body = swagger_client.DeliveryCdekUpdate() # DeliveryCdekUpdate | 

try:
    # Update
    api_response = api_instance.update_api_v1_deliveries_cdek_put(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeliveriesCdekApi->update_api_v1_deliveries_cdek_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DeliveryCdekUpdate**](DeliveryCdekUpdate.md)|  | 

### Return type

**object**

### Authorization

[HTTPBasic](../README.md#HTTPBasic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

