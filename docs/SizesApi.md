# swagger_client.SizesApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_size_by_id_api_v1_sizes_size_id_get**](SizesApi.md#get_size_by_id_api_v1_sizes_size_id_get) | **GET** /api/v1/sizes/{size_id} | Get Size By Id
[**get_sizes_api_v1_sizes_get**](SizesApi.md#get_sizes_api_v1_sizes_get) | **GET** /api/v1/sizes | Get Sizes
[**insert_or_nothing_api_v1_sizes_post**](SizesApi.md#insert_or_nothing_api_v1_sizes_post) | **POST** /api/v1/sizes | Insert Or Nothing

# **get_size_by_id_api_v1_sizes_size_id_get**
> str get_size_by_id_api_v1_sizes_size_id_get(size_id)

Get Size By Id

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
api_instance = swagger_client.SizesApi(swagger_client.ApiClient(configuration))
size_id = 56 # int | 

try:
    # Get Size By Id
    api_response = api_instance.get_size_by_id_api_v1_sizes_size_id_get(size_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SizesApi->get_size_by_id_api_v1_sizes_size_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **size_id** | **int**|  | 

### Return type

**str**

### Authorization

[HTTPBasic](../README.md#HTTPBasic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sizes_api_v1_sizes_get**
> list[SizeBaseDb] get_sizes_api_v1_sizes_get(category=category)

Get Sizes

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
api_instance = swagger_client.SizesApi(swagger_client.ApiClient(configuration))
category = '' # str |  (optional)

try:
    # Get Sizes
    api_response = api_instance.get_sizes_api_v1_sizes_get(category=category)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SizesApi->get_sizes_api_v1_sizes_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **category** | **str**|  | [optional] 

### Return type

[**list[SizeBaseDb]**](SizeBaseDb.md)

### Authorization

[HTTPBasic](../README.md#HTTPBasic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **insert_or_nothing_api_v1_sizes_post**
> object insert_or_nothing_api_v1_sizes_post(body)

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
api_instance = swagger_client.SizesApi(swagger_client.ApiClient(configuration))
body = NULL # object | 

try:
    # Insert Or Nothing
    api_response = api_instance.insert_or_nothing_api_v1_sizes_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SizesApi->insert_or_nothing_api_v1_sizes_post: %s\n" % e)
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

