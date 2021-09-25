# {{classname}}

All URIs are relative to *https://gateway.qg2.apps.qualys.com/csapi/v1.3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**DeleteCsSensors**](SensorApi.md#DeleteCsSensors) | **Delete** /sensors | Delete sensors in your account
[**GetCsSensorDetails**](SensorApi.md#GetCsSensorDetails) | **Get** /sensors/{sensorId} | Show details of a sensor
[**GetCsSensorsList**](SensorApi.md#GetCsSensorsList) | **Get** /sensors | Show a list of sensors in your account.

# **DeleteCsSensors**
> string DeleteCsSensors(ctx, optional)
Delete sensors in your account

Provide one or more sensor Ids or filters in the format shown under Example Value

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
 **optional** | ***SensorApiDeleteCsSensorsOpts** | optional parameters | nil if no parameters

### Optional Parameters
Optional parameters are passed through a pointer to a SensorApiDeleteCsSensorsOpts struct
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sensorIds** | [**optional.Interface of []string**](string.md)| delete the sensors from uuid | 
 **filter** | **optional.String**| delete the sensors from filter | 

### Return type

**string**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **GetCsSensorDetails**
> Sensor GetCsSensorDetails(ctx, sensorId)
Show details of a sensor

Show details of a sensor

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
  **sensorId** | **string**| Specify the sensor ID of a specific sensor in the user’s scope | 

### Return type

[**Sensor**](Sensor.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **GetCsSensorsList**
> Sensors GetCsSensorsList(ctx, optional)
Show a list of sensors in your account.

Show a list of sensors in your account.

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
 **optional** | ***SensorApiGetCsSensorsListOpts** | optional parameters | nil if no parameters

### Optional Parameters
Optional parameters are passed through a pointer to a SensorApiGetCsSensorsListOpts struct
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **optional.String**| Filter the sensors list by providing a query using Qualys syntax. | 
 **pageNumber** | **optional.Int32**| The page to be returned. | [default to 1]
 **pageSize** | **optional.Int32**| The number of records per page to be included in the response. | [default to 50]
 **sort** | **optional.String**| Sort the results using a Qualys token. | 

### Return type

[**Sensors**](Sensors.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

