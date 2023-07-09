# swagger_client.UsersApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_all_ids_users_api_v1_users_ids_get**](UsersApi.md#get_all_ids_users_api_v1_users_ids_get) | **GET** /api/v1/users/ids | Get All Ids Users
[**get_all_users_api_v1_users_get**](UsersApi.md#get_all_users_api_v1_users_get) | **GET** /api/v1/users | Get All Users
[**get_user_api_v1_users_user_id_get**](UsersApi.md#get_user_api_v1_users_user_id_get) | **GET** /api/v1/users/{user_id} | Get User
[**get_user_client_api_v1_users_clients_user_id_get**](UsersApi.md#get_user_client_api_v1_users_clients_user_id_get) | **GET** /api/v1/users/clients/{user_id} | Get User Client
[**get_user_codes_api_v1_users_user_id_codes_get**](UsersApi.md#get_user_codes_api_v1_users_user_id_codes_get) | **GET** /api/v1/users/{user_id}/codes | Get User Codes
[**update_last_mess_api_v1_users_user_id_mess_put**](UsersApi.md#update_last_mess_api_v1_users_user_id_mess_put) | **PUT** /api/v1/users/{user_id}/mess | Update Last Mess
[**update_user_items_api_v1_users_user_id_items_put**](UsersApi.md#update_user_items_api_v1_users_user_id_items_put) | **PUT** /api/v1/users/{user_id}/items | Update User Items

# **get_all_ids_users_api_v1_users_ids_get**
> object get_all_ids_users_api_v1_users_ids_get()

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

try:
    # Get All Ids Users
    api_response = api_instance.get_all_ids_users_api_v1_users_ids_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->get_all_ids_users_api_v1_users_ids_get: %s\n" % e)
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

# **get_all_users_api_v1_users_get**
> list[UserBase] get_all_users_api_v1_users_get()

Get All Users

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

try:
    # Get All Users
    api_response = api_instance.get_all_users_api_v1_users_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->get_all_users_api_v1_users_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[UserBase]**](UserBase.md)

### Authorization

[HTTPBasic](../README.md#HTTPBasic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_api_v1_users_user_id_get**
> object get_user_api_v1_users_user_id_get(user_id, first_name)

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
first_name = 'first_name_example' # str | 

try:
    # Get User
    api_response = api_instance.get_user_api_v1_users_user_id_get(user_id, first_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->get_user_api_v1_users_user_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**|  | 
 **first_name** | **str**|  | 

### Return type

**object**

### Authorization

[HTTPBasic](../README.md#HTTPBasic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_client_api_v1_users_clients_user_id_get**
> object get_user_client_api_v1_users_clients_user_id_get(user_id)

Get User Client

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

try:
    # Get User Client
    api_response = api_instance.get_user_client_api_v1_users_clients_user_id_get(user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->get_user_client_api_v1_users_clients_user_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**|  | 

### Return type

**object**

### Authorization

[HTTPBasic](../README.md#HTTPBasic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_codes_api_v1_users_user_id_codes_get**
> object get_user_codes_api_v1_users_user_id_codes_get(user_id)

Get User Codes

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

try:
    # Get User Codes
    api_response = api_instance.get_user_codes_api_v1_users_user_id_codes_get(user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->get_user_codes_api_v1_users_user_id_codes_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**|  | 

### Return type

**object**

### Authorization

[HTTPBasic](../README.md#HTTPBasic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_last_mess_api_v1_users_user_id_mess_put**
> object update_last_mess_api_v1_users_user_id_mess_put(user_id, message_id)

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
user_id = 56 # int | 
message_id = 56 # int | 

try:
    # Update Last Mess
    api_response = api_instance.update_last_mess_api_v1_users_user_id_mess_put(user_id, message_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->update_last_mess_api_v1_users_user_id_mess_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**|  | 
 **message_id** | **int**|  | 

### Return type

**object**

### Authorization

[HTTPBasic](../README.md#HTTPBasic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_user_items_api_v1_users_user_id_items_put**
> object update_user_items_api_v1_users_user_id_items_put(body, user_id)

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
body = NULL # object | 
user_id = 56 # int | 

try:
    # Update User Items
    api_response = api_instance.update_user_items_api_v1_users_user_id_items_put(body, user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->update_user_items_api_v1_users_user_id_items_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**object**](object.md)|  | 
 **user_id** | **int**|  | 

### Return type

**object**

### Authorization

[HTTPBasic](../README.md#HTTPBasic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

