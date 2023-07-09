# swagger_client.CategoriesApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_categories_name_api_v1_categories_get**](CategoriesApi.md#get_categories_name_api_v1_categories_get) | **GET** /api/v1/categories | Get Categories Name
[**insert_or_nothing_api_v1_categories_post**](CategoriesApi.md#insert_or_nothing_api_v1_categories_post) | **POST** /api/v1/categories | Insert Or Nothing

# **get_categories_name_api_v1_categories_get**
> object get_categories_name_api_v1_categories_get()

Get Categories Name

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
api_instance = swagger_client.CategoriesApi(swagger_client.ApiClient(configuration))

try:
    # Get Categories Name
    api_response = api_instance.get_categories_name_api_v1_categories_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CategoriesApi->get_categories_name_api_v1_categories_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**object**

### Authorization

[HTTPBasic](../README.md#HTTPBasic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **insert_or_nothing_api_v1_categories_post**
> object insert_or_nothing_api_v1_categories_post(body)

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
api_instance = swagger_client.CategoriesApi(swagger_client.ApiClient(configuration))
body = NULL # list[object] | 

try:
    # Insert Or Nothing
    api_response = api_instance.insert_or_nothing_api_v1_categories_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CategoriesApi->insert_or_nothing_api_v1_categories_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[object]**](object.md)|  | 

### Return type

**object**

### Authorization

[HTTPBasic](../README.md#HTTPBasic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

