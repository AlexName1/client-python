# swagger_client.StocksApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_stock_by_stock_id_api_v1_stocks_user_stock_id_get**](StocksApi.md#get_stock_by_stock_id_api_v1_stocks_user_stock_id_get) | **GET** /api/v1/stocks/user/{stock_id} | Get Stock By Stock Id
[**get_stock_without_load_by_stock_id_api_v1_stocks_stock_id_get**](StocksApi.md#get_stock_without_load_by_stock_id_api_v1_stocks_stock_id_get) | **GET** /api/v1/stocks/{stock_id} | Get Stock Without Load By Stock Id
[**get_stocks_by_order_code_api_v1_stocks_code_size_get**](StocksApi.md#get_stocks_by_order_code_api_v1_stocks_code_size_get) | **GET** /api/v1/stocks/{code}/{size} | Get Stocks By Order Code

# **get_stock_by_stock_id_api_v1_stocks_user_stock_id_get**
> object get_stock_by_stock_id_api_v1_stocks_user_stock_id_get(stock_id)

Get Stock By Stock Id

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
api_instance = swagger_client.StocksApi(swagger_client.ApiClient(configuration))
stock_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 

try:
    # Get Stock By Stock Id
    api_response = api_instance.get_stock_by_stock_id_api_v1_stocks_user_stock_id_get(stock_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StocksApi->get_stock_by_stock_id_api_v1_stocks_user_stock_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stock_id** | [**str**](.md)|  | 

### Return type

**object**

### Authorization

[HTTPBasic](../README.md#HTTPBasic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_stock_without_load_by_stock_id_api_v1_stocks_stock_id_get**
> Stock get_stock_without_load_by_stock_id_api_v1_stocks_stock_id_get(stock_id)

Get Stock Without Load By Stock Id

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
api_instance = swagger_client.StocksApi(swagger_client.ApiClient(configuration))
stock_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 

try:
    # Get Stock Without Load By Stock Id
    api_response = api_instance.get_stock_without_load_by_stock_id_api_v1_stocks_stock_id_get(stock_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StocksApi->get_stock_without_load_by_stock_id_api_v1_stocks_stock_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stock_id** | [**str**](.md)|  | 

### Return type

[**Stock**](Stock.md)

### Authorization

[HTTPBasic](../README.md#HTTPBasic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_stocks_by_order_code_api_v1_stocks_code_size_get**
> list[Stock] get_stocks_by_order_code_api_v1_stocks_code_size_get(code, size)

Get Stocks By Order Code

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
api_instance = swagger_client.StocksApi(swagger_client.ApiClient(configuration))
code = 'code_example' # str | 
size = 'size_example' # str | 

try:
    # Get Stocks By Order Code
    api_response = api_instance.get_stocks_by_order_code_api_v1_stocks_code_size_get(code, size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StocksApi->get_stocks_by_order_code_api_v1_stocks_code_size_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | **str**|  | 
 **size** | **str**|  | 

### Return type

[**list[Stock]**](Stock.md)

### Authorization

[HTTPBasic](../README.md#HTTPBasic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

