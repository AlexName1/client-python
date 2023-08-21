# swagger_client.SchedulersApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_api_v1_schedulers_scheduler_id_delete**](SchedulersApi.md#delete_api_v1_schedulers_scheduler_id_delete) | **DELETE** /api/v1/schedulers/{scheduler_id} | Delete
[**get_api_v1_schedulers_get**](SchedulersApi.md#get_api_v1_schedulers_get) | **GET** /api/v1/schedulers | Get
[**insert_api_v1_schedulers_post**](SchedulersApi.md#insert_api_v1_schedulers_post) | **POST** /api/v1/schedulers | Insert

# **delete_api_v1_schedulers_scheduler_id_delete**
> object delete_api_v1_schedulers_scheduler_id_delete(scheduler_id)

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
api_instance = swagger_client.SchedulersApi(swagger_client.ApiClient(configuration))
scheduler_id = 56 # int | 

try:
    # Delete
    api_response = api_instance.delete_api_v1_schedulers_scheduler_id_delete(scheduler_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SchedulersApi->delete_api_v1_schedulers_scheduler_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scheduler_id** | **int**|  | 

### Return type

**object**

### Authorization

[HTTPBasic](../README.md#HTTPBasic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_api_v1_schedulers_get**
> list[GetScheduler] get_api_v1_schedulers_get(token)

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
api_instance = swagger_client.SchedulersApi(swagger_client.ApiClient(configuration))
token = 'token_example' # str | 

try:
    # Get
    api_response = api_instance.get_api_v1_schedulers_get(token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SchedulersApi->get_api_v1_schedulers_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**|  | 

### Return type

[**list[GetScheduler]**](GetScheduler.md)

### Authorization

[HTTPBasic](../README.md#HTTPBasic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **insert_api_v1_schedulers_post**
> int insert_api_v1_schedulers_post(body)

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
api_instance = swagger_client.SchedulersApi(swagger_client.ApiClient(configuration))
body = swagger_client.InsertScheduler() # InsertScheduler | 

try:
    # Insert
    api_response = api_instance.insert_api_v1_schedulers_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SchedulersApi->insert_api_v1_schedulers_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**InsertScheduler**](InsertScheduler.md)|  | 

### Return type

**int**

### Authorization

[HTTPBasic](../README.md#HTTPBasic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

