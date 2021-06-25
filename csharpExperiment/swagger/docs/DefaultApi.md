# IO.Swagger.Api.DefaultApi

All URIs are relative to *https://api.met.no/weatherapi/locationforecast/2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**CompactGet**](DefaultApi.md#compactget) | **GET** /compact | 


<a name="compactget"></a>
# **CompactGet**
> void CompactGet (int? altitude = null, string lat = null, string lon = null)



### Example
```csharp
using System;
using System.Diagnostics;
using IO.Swagger.Api;
using IO.Swagger.Client;
using IO.Swagger.Model;

namespace Example
{
    public class CompactGetExample
    {
        public void main()
        {
            var apiInstance = new DefaultApi();
            var altitude = 56;  // int? |  (optional)  (default to 0)
            var lat = lat_example;  // string |  (optional) 
            var lon = lon_example;  // string |  (optional) 

            try
            {
                apiInstance.CompactGet(altitude, lat, lon);
            }
            catch (Exception e)
            {
                Debug.Print("Exception when calling DefaultApi.CompactGet: " + e.Message );
            }
        }
    }
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **altitude** | **int?**|  | [optional] [default to 0]
 **lat** | **string**|  | [optional] 
 **lon** | **string**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

