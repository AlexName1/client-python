# swagger_client.BasketsApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_one_basket_api_v1_baskets_basket_id_delete**](BasketsApi.md#delete_one_basket_api_v1_baskets_basket_id_delete) | **DELETE** /api/v1/baskets/{basket_id} | Delete One Basket
[**delete_user_basket_api_v1_baskets_users_bots_user_bot_id_delete**](BasketsApi.md#delete_user_basket_api_v1_baskets_users_bots_user_bot_id_delete) | **DELETE** /api/v1/baskets/users_bots/{user_bot_id} | Delete User Basket
[**get_basket_api_v1_baskets_get**](BasketsApi.md#get_basket_api_v1_baskets_get) | **GET** /api/v1/baskets | Get Basket
[**get_count_basket_api_v1_baskets_all_count_get**](BasketsApi.md#get_count_basket_api_v1_baskets_all_count_get) | **GET** /api/v1/baskets/all/count | Get Count Basket
[**get_list_id_basket_api_v1_baskets_all_list_id_get**](BasketsApi.md#get_list_id_basket_api_v1_baskets_all_list_id_get) | **GET** /api/v1/baskets/all/list_id | Get List Id Basket
[**get_one_basket_api_v1_baskets_basket_id_get**](BasketsApi.md#get_one_basket_api_v1_baskets_basket_id_get) | **GET** /api/v1/baskets/{basket_id} | Get One Basket
[**insert_api_v1_baskets_post**](BasketsApi.md#insert_api_v1_baskets_post) | **POST** /api/v1/baskets | Insert

# **delete_one_basket_api_v1_baskets_basket_id_delete**
> object delete_one_basket_api_v1_baskets_basket_id_delete(basket_id)

Delete One Basket

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
api_instance = swagger_client.BasketsApi(swagger_client.ApiClient(configuration))
basket_id = 56 # int | 

try:
    # Delete One Basket
    api_response = api_instance.delete_one_basket_api_v1_baskets_basket_id_delete(basket_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BasketsApi->delete_one_basket_api_v1_baskets_basket_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **basket_id** | **int**|  | 

### Return type

**object**

### Authorization

[HTTPBasic](../README.md#HTTPBasic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_user_basket_api_v1_baskets_users_bots_user_bot_id_delete**
> object delete_user_basket_api_v1_baskets_users_bots_user_bot_id_delete(user_bot_id)

Delete User Basket

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
api_instance = swagger_client.BasketsApi(swagger_client.ApiClient(configuration))
user_bot_id = 56 # int | 

try:
    # Delete User Basket
    api_response = api_instance.delete_user_basket_api_v1_baskets_users_bots_user_bot_id_delete(user_bot_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BasketsApi->delete_user_basket_api_v1_baskets_users_bots_user_bot_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_bot_id** | **int**|  | 

### Return type

**object**

### Authorization

[HTTPBasic](../README.md#HTTPBasic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_basket_api_v1_baskets_get**
> list[BasketBaseDb] get_basket_api_v1_baskets_get(user_id, token, item)

Get Basket

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
api_instance = swagger_client.BasketsApi(swagger_client.ApiClient(configuration))
user_id = 56 # int | 
token = 'token_example' # str | 
item = true # bool | 

try:
    # Get Basket
    api_response = api_instance.get_basket_api_v1_baskets_get(user_id, token, item)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BasketsApi->get_basket_api_v1_baskets_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**|  | 
 **token** | **str**|  | 
 **item** | **bool**|  | 

### Return type

[**list[BasketBaseDb]**](BasketBaseDb.md)

### Authorization

[HTTPBasic](../README.md#HTTPBasic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_count_basket_api_v1_baskets_all_count_get**
> int get_count_basket_api_v1_baskets_all_count_get(user_id, token)

Get Count Basket

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
api_instance = swagger_client.BasketsApi(swagger_client.ApiClient(configuration))
user_id = 56 # int | 
token = 'token_example' # str | 

try:
    # Get Count Basket
    api_response = api_instance.get_count_basket_api_v1_baskets_all_count_get(user_id, token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BasketsApi->get_count_basket_api_v1_baskets_all_count_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**|  | 
 **token** | **str**|  | 

### Return type

**int**

### Authorization

[HTTPBasic](../README.md#HTTPBasic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_list_id_basket_api_v1_baskets_all_list_id_get**
> list[int] get_list_id_basket_api_v1_baskets_all_list_id_get(user_id, token)

Get List Id Basket

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
api_instance = swagger_client.BasketsApi(swagger_client.ApiClient(configuration))
user_id = 56 # int | 
token = 'token_example' # str | 

try:
    # Get List Id Basket
    api_response = api_instance.get_list_id_basket_api_v1_baskets_all_list_id_get(user_id, token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BasketsApi->get_list_id_basket_api_v1_baskets_all_list_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**|  | 
 **token** | **str**|  | 

### Return type

**list[int]**

### Authorization

[HTTPBasic](../README.md#HTTPBasic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_one_basket_api_v1_baskets_basket_id_get**
> BasketBaseDb get_one_basket_api_v1_baskets_basket_id_get(basket_id, token)

Get One Basket

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
api_instance = swagger_client.BasketsApi(swagger_client.ApiClient(configuration))
basket_id = 56 # int | 
token = 'token_example' # str | 

try:
    # Get One Basket
    api_response = api_instance.get_one_basket_api_v1_baskets_basket_id_get(basket_id, token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BasketsApi->get_one_basket_api_v1_baskets_basket_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **basket_id** | **int**|  | 
 **token** | **str**|  | 

### Return type

[**BasketBaseDb**](BasketBaseDb.md)

### Authorization

[HTTPBasic](../README.md#HTTPBasic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **insert_api_v1_baskets_post**
> object insert_api_v1_baskets_post(body)

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
api_instance = swagger_client.BasketsApi(swagger_client.ApiClient(configuration))
body = swagger_client.InsertBasket() # InsertBasket | 

try:
    # Insert
    api_response = api_instance.insert_api_v1_baskets_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BasketsApi->insert_api_v1_baskets_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**InsertBasket**](InsertBasket.md)|  | 

### Return type

**object**

### Authorization

[HTTPBasic](../README.md#HTTPBasic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

