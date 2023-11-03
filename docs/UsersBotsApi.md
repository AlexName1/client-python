# swagger_client.UsersBotsApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_only_user_bot_api_v1_users_bots_user_id_only_get**](UsersBotsApi.md#get_only_user_bot_api_v1_users_bots_user_id_only_get) | **GET** /api/v1/users_bots/{user_id}/only | Get Only User Bot
[**get_user_bot_api_v1_users_bots_user_id_get**](UsersBotsApi.md#get_user_bot_api_v1_users_bots_user_id_get) | **GET** /api/v1/users_bots/{user_id} | Get User Bot
[**get_user_bot_start_api_v1_users_bots_user_id_start_get**](UsersBotsApi.md#get_user_bot_start_api_v1_users_bots_user_id_start_get) | **GET** /api/v1/users_bots/{user_id}/start | Get User Bot Start
[**get_user_client_bot_api_v1_users_bots_user_id_client_get**](UsersBotsApi.md#get_user_client_bot_api_v1_users_bots_user_id_client_get) | **GET** /api/v1/users_bots/{user_id}/client | Get User Client Bot

# **get_only_user_bot_api_v1_users_bots_user_id_only_get**
> UserBotBaseDb get_only_user_bot_api_v1_users_bots_user_id_only_get(user_id, token, partner=partner, user=user, stock=stock)

Get Only User Bot

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
api_instance = swagger_client.UsersBotsApi(swagger_client.ApiClient(configuration))
user_id = 56 # int | 
token = 'token_example' # str | 
partner = true # bool |  (optional)
user = true # bool |  (optional)
stock = true # bool |  (optional)

try:
    # Get Only User Bot
    api_response = api_instance.get_only_user_bot_api_v1_users_bots_user_id_only_get(user_id, token, partner=partner, user=user, stock=stock)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersBotsApi->get_only_user_bot_api_v1_users_bots_user_id_only_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**|  | 
 **token** | **str**|  | 
 **partner** | **bool**|  | [optional] 
 **user** | **bool**|  | [optional] 
 **stock** | **bool**|  | [optional] 

### Return type

[**UserBotBaseDb**](UserBotBaseDb.md)

### Authorization

[HTTPBasic](../README.md#HTTPBasic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_bot_api_v1_users_bots_user_id_get**
> UserBotBaseDb get_user_bot_api_v1_users_bots_user_id_get(user_id, token, first_name, username=username)

Get User Bot

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
api_instance = swagger_client.UsersBotsApi(swagger_client.ApiClient(configuration))
user_id = 56 # int | 
token = 'token_example' # str | 
first_name = 'first_name_example' # str | 
username = 'username_example' # str |  (optional)

try:
    # Get User Bot
    api_response = api_instance.get_user_bot_api_v1_users_bots_user_id_get(user_id, token, first_name, username=username)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersBotsApi->get_user_bot_api_v1_users_bots_user_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**|  | 
 **token** | **str**|  | 
 **first_name** | **str**|  | 
 **username** | **str**|  | [optional] 

### Return type

[**UserBotBaseDb**](UserBotBaseDb.md)

### Authorization

[HTTPBasic](../README.md#HTTPBasic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_bot_start_api_v1_users_bots_user_id_start_get**
> UserBotBaseDbStart get_user_bot_start_api_v1_users_bots_user_id_start_get(user_id, token, first_name, username=username, subscribe_channel=subscribe_channel)

Get User Bot Start

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
api_instance = swagger_client.UsersBotsApi(swagger_client.ApiClient(configuration))
user_id = 56 # int | 
token = 'token_example' # str | 
first_name = 'first_name_example' # str | 
username = 'username_example' # str |  (optional)
subscribe_channel = true # bool |  (optional)

try:
    # Get User Bot Start
    api_response = api_instance.get_user_bot_start_api_v1_users_bots_user_id_start_get(user_id, token, first_name, username=username, subscribe_channel=subscribe_channel)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersBotsApi->get_user_bot_start_api_v1_users_bots_user_id_start_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**|  | 
 **token** | **str**|  | 
 **first_name** | **str**|  | 
 **username** | **str**|  | [optional] 
 **subscribe_channel** | **bool**|  | [optional] 

### Return type

[**UserBotBaseDbStart**](UserBotBaseDbStart.md)

### Authorization

[HTTPBasic](../README.md#HTTPBasic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_client_bot_api_v1_users_bots_user_id_client_get**
> UserBotBaseDb get_user_client_bot_api_v1_users_bots_user_id_client_get(user_id, token)

Get User Client Bot

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
api_instance = swagger_client.UsersBotsApi(swagger_client.ApiClient(configuration))
user_id = 56 # int | 
token = 'token_example' # str | 

try:
    # Get User Client Bot
    api_response = api_instance.get_user_client_bot_api_v1_users_bots_user_id_client_get(user_id, token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersBotsApi->get_user_client_bot_api_v1_users_bots_user_id_client_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**|  | 
 **token** | **str**|  | 

### Return type

[**UserBotBaseDb**](UserBotBaseDb.md)

### Authorization

[HTTPBasic](../README.md#HTTPBasic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

