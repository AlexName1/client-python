# swagger_client.BotsApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_bot_api_v1_bots_token_get**](BotsApi.md#get_bot_api_v1_bots_token_get) | **GET** /api/v1/bots/{token} | Get Bot
[**get_bots_api_v1_bots_get**](BotsApi.md#get_bots_api_v1_bots_get) | **GET** /api/v1/bots | Get Bots
[**get_tokens_multibot_api_v1_bots_multibot_tokens_get**](BotsApi.md#get_tokens_multibot_api_v1_bots_multibot_tokens_get) | **GET** /api/v1/bots/multibot/tokens | Get Tokens Multibot
[**insert_or_nothing_api_v1_bots_post**](BotsApi.md#insert_or_nothing_api_v1_bots_post) | **POST** /api/v1/bots | Insert Or Nothing

# **get_bot_api_v1_bots_token_get**
> BotBaseDb get_bot_api_v1_bots_token_get(token)

Get Bot

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
api_instance = swagger_client.BotsApi(swagger_client.ApiClient(configuration))
token = 'token_example' # str | 

try:
    # Get Bot
    api_response = api_instance.get_bot_api_v1_bots_token_get(token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BotsApi->get_bot_api_v1_bots_token_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**|  | 

### Return type

[**BotBaseDb**](BotBaseDb.md)

### Authorization

[HTTPBasic](../README.md#HTTPBasic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_bots_api_v1_bots_get**
> list[BotBaseDb] get_bots_api_v1_bots_get()

Get Bots

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
api_instance = swagger_client.BotsApi(swagger_client.ApiClient(configuration))

try:
    # Get Bots
    api_response = api_instance.get_bots_api_v1_bots_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BotsApi->get_bots_api_v1_bots_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[BotBaseDb]**](BotBaseDb.md)

### Authorization

[HTTPBasic](../README.md#HTTPBasic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tokens_multibot_api_v1_bots_multibot_tokens_get**
> list[object] get_tokens_multibot_api_v1_bots_multibot_tokens_get()

Get Tokens Multibot

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
api_instance = swagger_client.BotsApi(swagger_client.ApiClient(configuration))

try:
    # Get Tokens Multibot
    api_response = api_instance.get_tokens_multibot_api_v1_bots_multibot_tokens_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BotsApi->get_tokens_multibot_api_v1_bots_multibot_tokens_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**list[object]**

### Authorization

[HTTPBasic](../README.md#HTTPBasic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **insert_or_nothing_api_v1_bots_post**
> object insert_or_nothing_api_v1_bots_post(body)

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
api_instance = swagger_client.BotsApi(swagger_client.ApiClient(configuration))
body = swagger_client.BotBase() # BotBase | 

try:
    # Insert Or Nothing
    api_response = api_instance.insert_or_nothing_api_v1_bots_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BotsApi->insert_or_nothing_api_v1_bots_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**BotBase**](BotBase.md)|  | 

### Return type

**object**

### Authorization

[HTTPBasic](../README.md#HTTPBasic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

