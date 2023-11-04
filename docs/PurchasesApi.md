# swagger_client.PurchasesApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_purchase_api_v1_purchases_purchase_id_delete**](PurchasesApi.md#delete_purchase_api_v1_purchases_purchase_id_delete) | **DELETE** /api/v1/purchases/{purchase_id} | Delete Purchase
[**get_active_orders_api_v1_purchases_token_active_get**](PurchasesApi.md#get_active_orders_api_v1_purchases_token_active_get) | **GET** /api/v1/purchases/{token}/active | Get Active Orders
[**get_all_api_v1_purchases_get**](PurchasesApi.md#get_all_api_v1_purchases_get) | **GET** /api/v1/purchases | Get All
[**get_count_api_v1_purchases_token_status_count_get**](PurchasesApi.md#get_count_api_v1_purchases_token_status_count_get) | **GET** /api/v1/purchases/{token}/{status}/count | Get Count
[**get_order_by_id_api_v1_purchases_order_id_token_one_get**](PurchasesApi.md#get_order_by_id_api_v1_purchases_order_id_token_one_get) | **GET** /api/v1/purchases/{order_id}/{token}/one | Get Order By Id
[**get_purchase_by_id_api_v1_purchases_purchase_id_get**](PurchasesApi.md#get_purchase_by_id_api_v1_purchases_purchase_id_get) | **GET** /api/v1/purchases/{purchase_id} | Get Purchase By Id
[**get_user_orders_api_v1_purchases_token_users_user_id_get**](PurchasesApi.md#get_user_orders_api_v1_purchases_token_users_user_id_get) | **GET** /api/v1/purchases/{token}/users/{user_id} | Get User Orders
[**insert_new_api_v1_purchases_token_new_post**](PurchasesApi.md#insert_new_api_v1_purchases_token_new_post) | **POST** /api/v1/purchases/{token}/new | Insert New
[**update_api_v1_purchases_token_put**](PurchasesApi.md#update_api_v1_purchases_token_put) | **PUT** /api/v1/purchases/{token} | Update
[**update_only_api_v1_purchases_put**](PurchasesApi.md#update_only_api_v1_purchases_put) | **PUT** /api/v1/purchases | Update Only

# **delete_purchase_api_v1_purchases_purchase_id_delete**
> object delete_purchase_api_v1_purchases_purchase_id_delete(purchase_id)

Delete Purchase

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
api_instance = swagger_client.PurchasesApi(swagger_client.ApiClient(configuration))
purchase_id = 56 # int | 

try:
    # Delete Purchase
    api_response = api_instance.delete_purchase_api_v1_purchases_purchase_id_delete(purchase_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PurchasesApi->delete_purchase_api_v1_purchases_purchase_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **purchase_id** | **int**|  | 

### Return type

**object**

### Authorization

[HTTPBasic](../README.md#HTTPBasic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_active_orders_api_v1_purchases_token_active_get**
> list[PurchaseBaseDb] get_active_orders_api_v1_purchases_token_active_get(token, ds=ds)

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
api_instance = swagger_client.PurchasesApi(swagger_client.ApiClient(configuration))
token = 'token_example' # str | 
ds = false # bool |  (optional) (default to false)

try:
    # Get Active Orders
    api_response = api_instance.get_active_orders_api_v1_purchases_token_active_get(token, ds=ds)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PurchasesApi->get_active_orders_api_v1_purchases_token_active_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**|  | 
 **ds** | **bool**|  | [optional] [default to false]

### Return type

[**list[PurchaseBaseDb]**](PurchaseBaseDb.md)

### Authorization

[HTTPBasic](../README.md#HTTPBasic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_api_v1_purchases_get**
> list[PurchaseBaseDb] get_all_api_v1_purchases_get(token)

Get All

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
api_instance = swagger_client.PurchasesApi(swagger_client.ApiClient(configuration))
token = 'token_example' # str | 

try:
    # Get All
    api_response = api_instance.get_all_api_v1_purchases_get(token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PurchasesApi->get_all_api_v1_purchases_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**|  | 

### Return type

[**list[PurchaseBaseDb]**](PurchaseBaseDb.md)

### Authorization

[HTTPBasic](../README.md#HTTPBasic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_count_api_v1_purchases_token_status_count_get**
> int get_count_api_v1_purchases_token_status_count_get(token, status)

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
api_instance = swagger_client.PurchasesApi(swagger_client.ApiClient(configuration))
token = 'token_example' # str | 
status = 56 # int | 

try:
    # Get Count
    api_response = api_instance.get_count_api_v1_purchases_token_status_count_get(token, status)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PurchasesApi->get_count_api_v1_purchases_token_status_count_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**|  | 
 **status** | **int**|  | 

### Return type

**int**

### Authorization

[HTTPBasic](../README.md#HTTPBasic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_order_by_id_api_v1_purchases_order_id_token_one_get**
> PurchaseBaseDb get_order_by_id_api_v1_purchases_order_id_token_one_get(order_id, token)

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
api_instance = swagger_client.PurchasesApi(swagger_client.ApiClient(configuration))
order_id = 56 # int | 
token = 'token_example' # str | 

try:
    # Get Order By Id
    api_response = api_instance.get_order_by_id_api_v1_purchases_order_id_token_one_get(order_id, token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PurchasesApi->get_order_by_id_api_v1_purchases_order_id_token_one_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_id** | **int**|  | 
 **token** | **str**|  | 

### Return type

[**PurchaseBaseDb**](PurchaseBaseDb.md)

### Authorization

[HTTPBasic](../README.md#HTTPBasic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_purchase_by_id_api_v1_purchases_purchase_id_get**
> PurchaseBaseDb get_purchase_by_id_api_v1_purchases_purchase_id_get(purchase_id, token, delivery_cdek=delivery_cdek, waybill=waybill, stock=stock, user_stock=user_stock)

Get Purchase By Id

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
api_instance = swagger_client.PurchasesApi(swagger_client.ApiClient(configuration))
purchase_id = 56 # int | 
token = 'token_example' # str | 
delivery_cdek = true # bool |  (optional)
waybill = true # bool |  (optional)
stock = true # bool |  (optional)
user_stock = true # bool |  (optional)

try:
    # Get Purchase By Id
    api_response = api_instance.get_purchase_by_id_api_v1_purchases_purchase_id_get(purchase_id, token, delivery_cdek=delivery_cdek, waybill=waybill, stock=stock, user_stock=user_stock)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PurchasesApi->get_purchase_by_id_api_v1_purchases_purchase_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **purchase_id** | **int**|  | 
 **token** | **str**|  | 
 **delivery_cdek** | **bool**|  | [optional] 
 **waybill** | **bool**|  | [optional] 
 **stock** | **bool**|  | [optional] 
 **user_stock** | **bool**|  | [optional] 

### Return type

[**PurchaseBaseDb**](PurchaseBaseDb.md)

### Authorization

[HTTPBasic](../README.md#HTTPBasic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_orders_api_v1_purchases_token_users_user_id_get**
> list[PurchaseBaseDb] get_user_orders_api_v1_purchases_token_users_user_id_get(token, user_id, status=status)

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
api_instance = swagger_client.PurchasesApi(swagger_client.ApiClient(configuration))
token = 'token_example' # str | 
user_id = 56 # int | 
status = 3 # int |  (optional) (default to 3)

try:
    # Get User Orders
    api_response = api_instance.get_user_orders_api_v1_purchases_token_users_user_id_get(token, user_id, status=status)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PurchasesApi->get_user_orders_api_v1_purchases_token_users_user_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**|  | 
 **user_id** | **int**|  | 
 **status** | **int**|  | [optional] [default to 3]

### Return type

[**list[PurchaseBaseDb]**](PurchaseBaseDb.md)

### Authorization

[HTTPBasic](../README.md#HTTPBasic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **insert_new_api_v1_purchases_token_new_post**
> int insert_new_api_v1_purchases_token_new_post(body, user_id, token, partner=partner)

Insert New

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
api_instance = swagger_client.PurchasesApi(swagger_client.ApiClient(configuration))
body = swagger_client.InsertPurchase() # InsertPurchase | 
user_id = 56 # int | 
token = 'token_example' # str | 
partner = false # bool |  (optional) (default to false)

try:
    # Insert New
    api_response = api_instance.insert_new_api_v1_purchases_token_new_post(body, user_id, token, partner=partner)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PurchasesApi->insert_new_api_v1_purchases_token_new_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**InsertPurchase**](InsertPurchase.md)|  | 
 **user_id** | **int**|  | 
 **token** | **str**|  | 
 **partner** | **bool**|  | [optional] [default to false]

### Return type

**int**

### Authorization

[HTTPBasic](../README.md#HTTPBasic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_api_v1_purchases_token_put**
> PurchaseBaseDb update_api_v1_purchases_token_put(body, token)

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
api_instance = swagger_client.PurchasesApi(swagger_client.ApiClient(configuration))
body = swagger_client.PurchaseUpdate() # PurchaseUpdate | 
token = 'token_example' # str | 

try:
    # Update
    api_response = api_instance.update_api_v1_purchases_token_put(body, token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PurchasesApi->update_api_v1_purchases_token_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PurchaseUpdate**](PurchaseUpdate.md)|  | 
 **token** | **str**|  | 

### Return type

[**PurchaseBaseDb**](PurchaseBaseDb.md)

### Authorization

[HTTPBasic](../README.md#HTTPBasic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_only_api_v1_purchases_put**
> object update_only_api_v1_purchases_put(body)

Update Only

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
api_instance = swagger_client.PurchasesApi(swagger_client.ApiClient(configuration))
body = swagger_client.UpdatePurchase() # UpdatePurchase | 

try:
    # Update Only
    api_response = api_instance.update_only_api_v1_purchases_put(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PurchasesApi->update_only_api_v1_purchases_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdatePurchase**](UpdatePurchase.md)|  | 

### Return type

**object**

### Authorization

[HTTPBasic](../README.md#HTTPBasic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

