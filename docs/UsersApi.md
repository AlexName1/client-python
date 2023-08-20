# swagger_client.UsersApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_count_api_v1_users_count_get**](UsersApi.md#get_count_api_v1_users_count_get) | **GET** /api/v1/users/count | Get Count
[**get_ids_api_v1_users_ids_get**](UsersApi.md#get_ids_api_v1_users_ids_get) | **GET** /api/v1/users/ids | Get Ids
[**get_items_api_v1_users_user_id_items_get**](UsersApi.md#get_items_api_v1_users_user_id_items_get) | **GET** /api/v1/users/{user_id}/items | Get Items
[**get_user_api_v1_users_user_id_one_get**](UsersApi.md#get_user_api_v1_users_user_id_one_get) | **GET** /api/v1/users/{user_id}/one | Get User
[**insert_or_nothing_api_v1_users_post**](UsersApi.md#insert_or_nothing_api_v1_users_post) | **POST** /api/v1/users | Insert Or Nothing
[**update_items_api_v1_users_user_id_items_put**](UsersApi.md#update_items_api_v1_users_user_id_items_put) | **PUT** /api/v1/users/{user_id}/items | Update Items
[**update_last_mess_api_v1_users_user_id_mess_put**](UsersApi.md#update_last_mess_api_v1_users_user_id_mess_put) | **PUT** /api/v1/users/{user_id}/mess | Update Last Mess

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

# **get_ids_api_v1_users_ids_get**
> list[object] get_ids_api_v1_users_ids_get(token)

Get Ids

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
    # Get Ids
    api_response = api_instance.get_ids_api_v1_users_ids_get(token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->get_ids_api_v1_users_ids_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**|  | 

### Return type

**list[object]**

### Authorization

[HTTPBasic](../README.md#HTTPBasic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_items_api_v1_users_user_id_items_get**
> list[object] get_items_api_v1_users_user_id_items_get(user_id, token)

Get Items

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
    # Get Items
    api_response = api_instance.get_items_api_v1_users_user_id_items_get(user_id, token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->get_items_api_v1_users_user_id_items_get: %s\n" % e)
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

# **get_user_api_v1_users_user_id_one_get**
> GetUser get_user_api_v1_users_user_id_one_get(user_id, token, first_name=first_name)

Get User

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
first_name = 'first_name_example' # str |  (optional)

try:
    # Get User
    api_response = api_instance.get_user_api_v1_users_user_id_one_get(user_id, token, first_name=first_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->get_user_api_v1_users_user_id_one_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**|  | 
 **token** | **str**|  | 
 **first_name** | **str**|  | [optional] 

### Return type

[**GetUser**](GetUser.md)

### Authorization

[HTTPBasic](../README.md#HTTPBasic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **insert_or_nothing_api_v1_users_post**
> object insert_or_nothing_api_v1_users_post(body, token)

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
api_instance = swagger_client.UsersApi(swagger_client.ApiClient(configuration))
body = swagger_client.InsertUser() # InsertUser | 
token = 'token_example' # str | 

try:
    # Insert Or Nothing
    api_response = api_instance.insert_or_nothing_api_v1_users_post(body, token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->insert_or_nothing_api_v1_users_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**InsertUser**](InsertUser.md)|  | 
 **token** | **str**|  | 

### Return type

**object**

### Authorization

[HTTPBasic](../README.md#HTTPBasic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_items_api_v1_users_user_id_items_put**
> object update_items_api_v1_users_user_id_items_put(body, token, user_id)

Update Items

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
    # Update Items
    api_response = api_instance.update_items_api_v1_users_user_id_items_put(body, token, user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->update_items_api_v1_users_user_id_items_put: %s\n" % e)
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

