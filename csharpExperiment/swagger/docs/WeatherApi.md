# IO.Swagger.Api.WeatherApi

All URIs are relative to *https://api.met.no/weatherapi/locationforecast/2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**GetStatus**](WeatherApi.md#getstatus) | **GET** /status | 


<a name="getstatus"></a>
# **GetStatus**
> void GetStatus ()



### Example
```csharp
using System;
using System.Diagnostics;
using IO.Swagger.Api;
using IO.Swagger.Client;
using IO.Swagger.Model;

namespace Example
{
    public class GetStatusExample
    {
        public void main()
        {
            var apiInstance = new WeatherApi();

            try
            {
                apiInstance.GetStatus();
            }
            catch (Exception e)
            {
                Debug.Print("Exception when calling WeatherApi.GetStatus: " + e.Message );
            }
        }
    }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

