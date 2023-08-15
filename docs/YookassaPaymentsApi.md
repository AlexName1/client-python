# swagger_client.YookassaPaymentsApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**insert_api_v1_yookassa_payments_post**](YookassaPaymentsApi.md#insert_api_v1_yookassa_payments_post) | **POST** /api/v1/yookassa-payments | Insert

# **insert_api_v1_yookassa_payments_post**
> int insert_api_v1_yookassa_payments_post(body)

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
api_instance = swagger_client.YookassaPaymentsApi(swagger_client.ApiClient(configuration))
body = swagger_client.YookassaPaymentInsert() # YookassaPaymentInsert | 

try:
    # Insert
    api_response = api_instance.insert_api_v1_yookassa_payments_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling YookassaPaymentsApi->insert_api_v1_yookassa_payments_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**YookassaPaymentInsert**](YookassaPaymentInsert.md)|  | 

### Return type

**int**

### Authorization

[HTTPBasic](../README.md#HTTPBasic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

