# swagger_client.UsersApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_all_ids_users_api_v1_users_ids_get**](UsersApi.md#get_all_ids_users_api_v1_users_ids_get) | **GET** /api/v1/users/ids | Get All Ids Users
[**get_count_api_v1_users_count_get**](UsersApi.md#get_count_api_v1_users_count_get) | **GET** /api/v1/users/count | Get Count
[**get_user_items_api_v1_users_user_id_items_get**](UsersApi.md#get_user_items_api_v1_users_user_id_items_get) | **GET** /api/v1/users/{user_id}/items | Get User Items
[**update_last_mess_api_v1_users_user_id_mess_put**](UsersApi.md#update_last_mess_api_v1_users_user_id_mess_put) | **PUT** /api/v1/users/{user_id}/mess | Update Last Mess
[**update_user_items_api_v1_users_user_id_items_put**](UsersApi.md#update_user_items_api_v1_users_user_id_items_put) | **PUT** /api/v1/users/{user_id}/items | Update User Items

# **get_all_ids_users_api_v1_users_ids_get**
> list[int] get_all_ids_users_api_v1_users_ids_get(token)

Get All Ids Users

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
api_instance = swagger_client.UsersApi(swagger_client.ApiClient(configuration))
token = 'token_example' # str | 

try:
    # Get All Ids Users
    api_response = api_instance.get_all_ids_users_api_v1_users_ids_get(token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->get_all_ids_users_api_v1_users_ids_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**|  | 

### Return type

**list[int]**

### Authorization

[HTTPBasic](../README.md#HTTPBasic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_count_api_v1_users_count_get**
> int get_count_api_v1_users_count_get(token)

Get Count

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
api_instance = swagger_client.UsersApi(swagger_client.ApiClient(configuration))
token = 'token_example' # str | 

try:
    # Get Count
    api_response = api_instance.get_count_api_v1_users_count_get(token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->get_count_api_v1_users_count_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**|  | 

### Return type

**int**

### Authorization

[HTTPBasic](../README.md#HTTPBasic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_items_api_v1_users_user_id_items_get**
> list[object] get_user_items_api_v1_users_user_id_items_get(user_id, token)

Get User Items

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
api_instance = swagger_client.UsersApi(swagger_client.ApiClient(configuration))
user_id = 56 # int | 
token = 'token_example' # str | 

try:
    # Get User Items
    api_response = api_instance.get_user_items_api_v1_users_user_id_items_get(user_id, token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->get_user_items_api_v1_users_user_id_items_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**|  | 
 **token** | **str**|  | 

### Return type

**list[object]**

### Authorization

[HTTPBasic](../README.md#HTTPBasic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_last_mess_api_v1_users_user_id_mess_put**
> object update_last_mess_api_v1_users_user_id_mess_put(body, token, user_id)

Update Last Mess

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
api_instance = swagger_client.UsersApi(swagger_client.ApiClient(configuration))
body = swagger_client.UpdateUserMess() # UpdateUserMess | 
token = 'token_example' # str | 
user_id = 56 # int | 

try:
    # Update Last Mess
    api_response = api_instance.update_last_mess_api_v1_users_user_id_mess_put(body, token, user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->update_last_mess_api_v1_users_user_id_mess_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateUserMess**](UpdateUserMess.md)|  | 
 **token** | **str**|  | 
 **user_id** | **int**|  | 

### Return type

**object**

### Authorization

[HTTPBasic](../README.md#HTTPBasic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_user_items_api_v1_users_user_id_items_put**
> object update_user_items_api_v1_users_user_id_items_put(body, token, user_id)

Update User Items

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
api_instance = swagger_client.UsersApi(swagger_client.ApiClient(configuration))
body = swagger_client.UpdateUserItems() # UpdateUserItems | 
token = 'token_example' # str | 
user_id = 56 # int | 

try:
    # Update User Items
    api_response = api_instance.update_user_items_api_v1_users_user_id_items_put(body, token, user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->update_user_items_api_v1_users_user_id_items_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateUserItems**](UpdateUserItems.md)|  | 
 **token** | **str**|  | 
 **user_id** | **int**|  | 

### Return type

**object**

### Authorization

[HTTPBasic](../README.md#HTTPBasic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

