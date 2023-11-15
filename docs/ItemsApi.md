# swagger_client.ItemsApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_all_api_v1_items_get**](ItemsApi.md#get_all_api_v1_items_get) | **GET** /api/v1/items | Get All
[**get_brands_and_counts_api_v1_items_category_brands_counts_get**](ItemsApi.md#get_brands_and_counts_api_v1_items_category_brands_counts_get) | **GET** /api/v1/items/{category}/brands-counts | Get Brands And Counts
[**get_item_api_v1_items_code_token_one_get**](ItemsApi.md#get_item_api_v1_items_code_token_one_get) | **GET** /api/v1/items/{code}/{token}/one | Get Item
[**get_item_new_api_v1_items_code_token_one_new_get**](ItemsApi.md#get_item_new_api_v1_items_code_token_one_new_get) | **GET** /api/v1/items/{code}/{token}/one_new | Get Item New
[**get_item_selectinload_size_api_v1_items_code_token_load_size_get**](ItemsApi.md#get_item_selectinload_size_api_v1_items_code_token_load_size_get) | **GET** /api/v1/items/{code}/{token}/load-size | Get Item Selectinload Size
[**get_items_action_new_codes_api_v1_items_token_all_new_codes_get**](ItemsApi.md#get_items_action_new_codes_api_v1_items_token_all_new_codes_get) | **GET** /api/v1/items/{token}/all_new_codes | Get Items Action New Codes
[**get_items_codes_api_v1_items_category_brand_codes_get**](ItemsApi.md#get_items_codes_api_v1_items_category_brand_codes_get) | **GET** /api/v1/items/{category}/{brand}/codes | Get Items Codes
[**get_models_and_counts_api_v1_items_category_brand_models_counts_get**](ItemsApi.md#get_models_and_counts_api_v1_items_category_brand_models_counts_get) | **GET** /api/v1/items/{category}/{brand}/models-counts | Get Models And Counts
[**get_models_api_v1_items_category_brand_models_get**](ItemsApi.md#get_models_api_v1_items_category_brand_models_get) | **GET** /api/v1/items/{category}/{brand}/models | Get Models

# **get_all_api_v1_items_get**
> list[ItemBaseDb] get_all_api_v1_items_get(token)

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
api_instance = swagger_client.ItemsApi(swagger_client.ApiClient(configuration))
token = 'token_example' # str | 

try:
    # Get All
    api_response = api_instance.get_all_api_v1_items_get(token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ItemsApi->get_all_api_v1_items_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**|  | 

### Return type

[**list[ItemBaseDb]**](ItemBaseDb.md)

### Authorization

[HTTPBasic](../README.md#HTTPBasic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_brands_and_counts_api_v1_items_category_brands_counts_get**
> list[BrandCount] get_brands_and_counts_api_v1_items_category_brands_counts_get(category)

Get Brands And Counts

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
api_instance = swagger_client.ItemsApi(swagger_client.ApiClient(configuration))
category = 'category_example' # str | 

try:
    # Get Brands And Counts
    api_response = api_instance.get_brands_and_counts_api_v1_items_category_brands_counts_get(category)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ItemsApi->get_brands_and_counts_api_v1_items_category_brands_counts_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **category** | **str**|  | 

### Return type

[**list[BrandCount]**](BrandCount.md)

### Authorization

[HTTPBasic](../README.md#HTTPBasic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_item_api_v1_items_code_token_one_get**
> ItemBaseDb get_item_api_v1_items_code_token_one_get(code, token, active=active, size_id=size_id)

Get Item

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
api_instance = swagger_client.ItemsApi(swagger_client.ApiClient(configuration))
code = 'code_example' # str | 
token = 'token_example' # str | 
active = false # bool |  (optional) (default to false)
size_id = 56 # int |  (optional)

try:
    # Get Item
    api_response = api_instance.get_item_api_v1_items_code_token_one_get(code, token, active=active, size_id=size_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ItemsApi->get_item_api_v1_items_code_token_one_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | **str**|  | 
 **token** | **str**|  | 
 **active** | **bool**|  | [optional] [default to false]
 **size_id** | **int**|  | [optional] 

### Return type

[**ItemBaseDb**](ItemBaseDb.md)

### Authorization

[HTTPBasic](../README.md#HTTPBasic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_item_new_api_v1_items_code_token_one_new_get**
> ItemBaseDb get_item_new_api_v1_items_code_token_one_new_get(code, token, dimension=dimension, category=category, centimeter=centimeter)

Get Item New

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
api_instance = swagger_client.ItemsApi(swagger_client.ApiClient(configuration))
code = 'code_example' # str | 
token = 'token_example' # str | 
dimension = false # bool |  (optional) (default to false)
category = false # bool |  (optional) (default to false)
centimeter = false # bool |  (optional) (default to false)

try:
    # Get Item New
    api_response = api_instance.get_item_new_api_v1_items_code_token_one_new_get(code, token, dimension=dimension, category=category, centimeter=centimeter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ItemsApi->get_item_new_api_v1_items_code_token_one_new_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | **str**|  | 
 **token** | **str**|  | 
 **dimension** | **bool**|  | [optional] [default to false]
 **category** | **bool**|  | [optional] [default to false]
 **centimeter** | **bool**|  | [optional] [default to false]

### Return type

[**ItemBaseDb**](ItemBaseDb.md)

### Authorization

[HTTPBasic](../README.md#HTTPBasic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_item_selectinload_size_api_v1_items_code_token_load_size_get**
> ItemBaseDb get_item_selectinload_size_api_v1_items_code_token_load_size_get(code, token, like=like, sneaker=sneaker)

Get Item Selectinload Size

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
api_instance = swagger_client.ItemsApi(swagger_client.ApiClient(configuration))
code = 'code_example' # str | 
token = 'token_example' # str | 
like = false # bool |  (optional) (default to false)
sneaker = false # bool |  (optional) (default to false)

try:
    # Get Item Selectinload Size
    api_response = api_instance.get_item_selectinload_size_api_v1_items_code_token_load_size_get(code, token, like=like, sneaker=sneaker)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ItemsApi->get_item_selectinload_size_api_v1_items_code_token_load_size_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | **str**|  | 
 **token** | **str**|  | 
 **like** | **bool**|  | [optional] [default to false]
 **sneaker** | **bool**|  | [optional] [default to false]

### Return type

[**ItemBaseDb**](ItemBaseDb.md)

### Authorization

[HTTPBasic](../README.md#HTTPBasic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_items_action_new_codes_api_v1_items_token_all_new_codes_get**
> list[str] get_items_action_new_codes_api_v1_items_token_all_new_codes_get(token, action, category=category, size=size, color=color, season=season, sneaker=sneaker)

Get Items Action New Codes

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
api_instance = swagger_client.ItemsApi(swagger_client.ApiClient(configuration))
token = 'token_example' # str | 
action = 'action_example' # str | 
category = 'category_example' # str |  (optional)
size = 56 # int |  (optional)
color = 'color_example' # str |  (optional)
season = 'season_example' # str |  (optional)
sneaker = false # bool |  (optional) (default to false)

try:
    # Get Items Action New Codes
    api_response = api_instance.get_items_action_new_codes_api_v1_items_token_all_new_codes_get(token, action, category=category, size=size, color=color, season=season, sneaker=sneaker)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ItemsApi->get_items_action_new_codes_api_v1_items_token_all_new_codes_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**|  | 
 **action** | **str**|  | 
 **category** | **str**|  | [optional] 
 **size** | **int**|  | [optional] 
 **color** | **str**|  | [optional] 
 **season** | **str**|  | [optional] 
 **sneaker** | **bool**|  | [optional] [default to false]

### Return type

**list[str]**

### Authorization

[HTTPBasic](../README.md#HTTPBasic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_items_codes_api_v1_items_category_brand_codes_get**
> list[object] get_items_codes_api_v1_items_category_brand_codes_get(category, brand, model=model)

Get Items Codes

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
api_instance = swagger_client.ItemsApi(swagger_client.ApiClient(configuration))
category = 'category_example' # str | 
brand = 'brand_example' # str | 
model = 'model_example' # str |  (optional)

try:
    # Get Items Codes
    api_response = api_instance.get_items_codes_api_v1_items_category_brand_codes_get(category, brand, model=model)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ItemsApi->get_items_codes_api_v1_items_category_brand_codes_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **category** | **str**|  | 
 **brand** | **str**|  | 
 **model** | **str**|  | [optional] 

### Return type

**list[object]**

### Authorization

[HTTPBasic](../README.md#HTTPBasic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_models_and_counts_api_v1_items_category_brand_models_counts_get**
> list[ModelCount] get_models_and_counts_api_v1_items_category_brand_models_counts_get(category, brand)

Get Models And Counts

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
api_instance = swagger_client.ItemsApi(swagger_client.ApiClient(configuration))
category = 'category_example' # str | 
brand = 'brand_example' # str | 

try:
    # Get Models And Counts
    api_response = api_instance.get_models_and_counts_api_v1_items_category_brand_models_counts_get(category, brand)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ItemsApi->get_models_and_counts_api_v1_items_category_brand_models_counts_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **category** | **str**|  | 
 **brand** | **str**|  | 

### Return type

[**list[ModelCount]**](ModelCount.md)

### Authorization

[HTTPBasic](../README.md#HTTPBasic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_models_api_v1_items_category_brand_models_get**
> object get_models_api_v1_items_category_brand_models_get(category, brand)

Get Models

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
api_instance = swagger_client.ItemsApi(swagger_client.ApiClient(configuration))
category = 'category_example' # str | 
brand = 'brand_example' # str | 

try:
    # Get Models
    api_response = api_instance.get_models_api_v1_items_category_brand_models_get(category, brand)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ItemsApi->get_models_api_v1_items_category_brand_models_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **category** | **str**|  | 
 **brand** | **str**|  | 

### Return type

**object**

### Authorization

[HTTPBasic](../README.md#HTTPBasic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

