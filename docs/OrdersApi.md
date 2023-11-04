# swagger_client.OrdersApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_order_api_v1_orders_order_id_delete**](OrdersApi.md#delete_order_api_v1_orders_order_id_delete) | **DELETE** /api/v1/orders/{order_id} | Delete Order
[**get_active_orders_api_v1_orders_get**](OrdersApi.md#get_active_orders_api_v1_orders_get) | **GET** /api/v1/orders | Get Active Orders
[**get_count_orders_api_v1_orders_count_get**](OrdersApi.md#get_count_orders_api_v1_orders_count_get) | **GET** /api/v1/orders/count | Get Count Orders
[**get_count_orders_by_user_id_api_v1_orders_users_user_id_count_get**](OrdersApi.md#get_count_orders_by_user_id_api_v1_orders_users_user_id_count_get) | **GET** /api/v1/orders/users/{user_id}/count | Get Count Orders By User Id
[**get_order_by_id_api_v1_orders_order_id_get**](OrdersApi.md#get_order_by_id_api_v1_orders_order_id_get) | **GET** /api/v1/orders/{order_id} | Get Order By Id
[**get_user_orders_api_v1_orders_users_user_id_get**](OrdersApi.md#get_user_orders_api_v1_orders_users_user_id_get) | **GET** /api/v1/orders/users/{user_id} | Get User Orders
[**insert_order_api_v1_orders_post**](OrdersApi.md#insert_order_api_v1_orders_post) | **POST** /api/v1/orders | Insert Order

# **delete_order_api_v1_orders_order_id_delete**
> object delete_order_api_v1_orders_order_id_delete(order_id)

Delete Order

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
api_instance = swagger_client.OrdersApi(swagger_client.ApiClient(configuration))
order_id = 56 # int | 

try:
    # Delete Order
    api_response = api_instance.delete_order_api_v1_orders_order_id_delete(order_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrdersApi->delete_order_api_v1_orders_order_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_id** | **int**|  | 

### Return type

**object**

### Authorization

[HTTPBasic](../README.md#HTTPBasic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_active_orders_api_v1_orders_get**
> list[OrderBaseDb] get_active_orders_api_v1_orders_get(dropshipping, token, user_id=user_id)

Get Active Orders

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
api_instance = swagger_client.OrdersApi(swagger_client.ApiClient(configuration))
dropshipping = true # bool | 
token = 'token_example' # str | 
user_id = 56 # int |  (optional)

try:
    # Get Active Orders
    api_response = api_instance.get_active_orders_api_v1_orders_get(dropshipping, token, user_id=user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrdersApi->get_active_orders_api_v1_orders_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dropshipping** | **bool**|  | 
 **token** | **str**|  | 
 **user_id** | **int**|  | [optional] 

### Return type

[**list[OrderBaseDb]**](OrderBaseDb.md)

### Authorization

[HTTPBasic](../README.md#HTTPBasic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_count_orders_api_v1_orders_count_get**
> int get_count_orders_api_v1_orders_count_get(status, token)

Get Count Orders

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
api_instance = swagger_client.OrdersApi(swagger_client.ApiClient(configuration))
status = 56 # int | 
token = 'token_example' # str | 

try:
    # Get Count Orders
    api_response = api_instance.get_count_orders_api_v1_orders_count_get(status, token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrdersApi->get_count_orders_api_v1_orders_count_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **status** | **int**|  | 
 **token** | **str**|  | 

### Return type

**int**

### Authorization

[HTTPBasic](../README.md#HTTPBasic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_count_orders_by_user_id_api_v1_orders_users_user_id_count_get**
> int get_count_orders_by_user_id_api_v1_orders_users_user_id_count_get(user_id, status, token)

Get Count Orders By User Id

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
api_instance = swagger_client.OrdersApi(swagger_client.ApiClient(configuration))
user_id = 56 # int | 
status = 56 # int | 
token = 'token_example' # str | 

try:
    # Get Count Orders By User Id
    api_response = api_instance.get_count_orders_by_user_id_api_v1_orders_users_user_id_count_get(user_id, status, token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrdersApi->get_count_orders_by_user_id_api_v1_orders_users_user_id_count_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**|  | 
 **status** | **int**|  | 
 **token** | **str**|  | 

### Return type

**int**

### Authorization

[HTTPBasic](../README.md#HTTPBasic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_order_by_id_api_v1_orders_order_id_get**
> OrderBaseDb get_order_by_id_api_v1_orders_order_id_get(order_id, purchases=purchases, item=item, size=size, user_bot=user_bot, partner=partner, order_by_purchases=order_by_purchases)

Get Order By Id

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
api_instance = swagger_client.OrdersApi(swagger_client.ApiClient(configuration))
order_id = 56 # int | 
purchases = true # bool |  (optional)
item = true # bool |  (optional)
size = true # bool |  (optional)
user_bot = true # bool |  (optional)
partner = true # bool |  (optional)
order_by_purchases = true # bool |  (optional)

try:
    # Get Order By Id
    api_response = api_instance.get_order_by_id_api_v1_orders_order_id_get(order_id, purchases=purchases, item=item, size=size, user_bot=user_bot, partner=partner, order_by_purchases=order_by_purchases)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrdersApi->get_order_by_id_api_v1_orders_order_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_id** | **int**|  | 
 **purchases** | **bool**|  | [optional] 
 **item** | **bool**|  | [optional] 
 **size** | **bool**|  | [optional] 
 **user_bot** | **bool**|  | [optional] 
 **partner** | **bool**|  | [optional] 
 **order_by_purchases** | **bool**|  | [optional] 

### Return type

[**OrderBaseDb**](OrderBaseDb.md)

### Authorization

[HTTPBasic](../README.md#HTTPBasic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_orders_api_v1_orders_users_user_id_get**
> list[OrderBaseDb] get_user_orders_api_v1_orders_users_user_id_get(user_id, purchase_status, token)

Get User Orders

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
api_instance = swagger_client.OrdersApi(swagger_client.ApiClient(configuration))
user_id = 56 # int | 
purchase_status = 56 # int | 
token = 'token_example' # str | 

try:
    # Get User Orders
    api_response = api_instance.get_user_orders_api_v1_orders_users_user_id_get(user_id, purchase_status, token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrdersApi->get_user_orders_api_v1_orders_users_user_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**|  | 
 **purchase_status** | **int**|  | 
 **token** | **str**|  | 

### Return type

[**list[OrderBaseDb]**](OrderBaseDb.md)

### Authorization

[HTTPBasic](../README.md#HTTPBasic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **insert_order_api_v1_orders_post**
> OrderBaseDb insert_order_api_v1_orders_post(body, token)

Insert Order

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
api_instance = swagger_client.OrdersApi(swagger_client.ApiClient(configuration))
body = swagger_client.InsertOrder() # InsertOrder | 
token = 'token_example' # str | 

try:
    # Insert Order
    api_response = api_instance.insert_order_api_v1_orders_post(body, token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrdersApi->insert_order_api_v1_orders_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**InsertOrder**](InsertOrder.md)|  | 
 **token** | **str**|  | 

### Return type

[**OrderBaseDb**](OrderBaseDb.md)

### Authorization

[HTTPBasic](../README.md#HTTPBasic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

