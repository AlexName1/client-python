# swagger_client.InfoItemsApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**insert_or_update_api_v1_info_items_token_post**](InfoItemsApi.md#insert_or_update_api_v1_info_items_token_post) | **POST** /api/v1/info-items/{token} | Insert Or Update
[**update_api_v1_info_items_token_put**](InfoItemsApi.md#update_api_v1_info_items_token_put) | **PUT** /api/v1/info-items/{token} | Update
[**update_new_api_v1_info_items_token_new_put**](InfoItemsApi.md#update_new_api_v1_info_items_token_new_put) | **PUT** /api/v1/info-items/{token}/new | Update New

# **insert_or_update_api_v1_info_items_token_post**
> object insert_or_update_api_v1_info_items_token_post(body, token)

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
token = 'token_example' # str | 

try:
    # Insert Or Update
    api_response = api_instance.insert_or_update_api_v1_info_items_token_post(body, token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InfoItemsApi->insert_or_update_api_v1_info_items_token_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**InfoItemInsert**](InfoItemInsert.md)|  | 
 **token** | **str**|  | 

### Return type

**object**

### Authorization

[HTTPBasic](../README.md#HTTPBasic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_api_v1_info_items_token_put**
> object update_api_v1_info_items_token_put(body, token)

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
api_instance = swagger_client.InfoItemsApi(swagger_client.ApiClient(configuration))
body = swagger_client.InfoItemUpdate() # InfoItemUpdate | 
token = 'token_example' # str | 

try:
    # Update
    api_response = api_instance.update_api_v1_info_items_token_put(body, token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InfoItemsApi->update_api_v1_info_items_token_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**InfoItemUpdate**](InfoItemUpdate.md)|  | 
 **token** | **str**|  | 

### Return type

**object**

### Authorization

[HTTPBasic](../README.md#HTTPBasic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_new_api_v1_info_items_token_new_put**
> object update_new_api_v1_info_items_token_new_put(body, token)

Update New

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
body = swagger_client.InfoItemUpdateNew() # InfoItemUpdateNew | 
token = 'token_example' # str | 

try:
    # Update New
    api_response = api_instance.update_new_api_v1_info_items_token_new_put(body, token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InfoItemsApi->update_new_api_v1_info_items_token_new_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**InfoItemUpdateNew**](InfoItemUpdateNew.md)|  | 
 **token** | **str**|  | 

### Return type

**object**

### Authorization

[HTTPBasic](../README.md#HTTPBasic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

