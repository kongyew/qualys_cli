# {{classname}}

All URIs are relative to *https://gateway.qg2.apps.qualys.com/csapi/v1.3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**GetCsControlsDataUsingGET**](ControlApi.md#GetCsControlsDataUsingGET) | **Get** /controls/{controlId} | Show details of control
[**GetCsControlsList**](ControlApi.md#GetCsControlsList) | **Get** /controls | Show list of controls

# **GetCsControlsDataUsingGET**
> PcControl GetCsControlsDataUsingGET(ctx, controlId)
Show details of control

Show details of control

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
  **controlId** | **string**| Specify ID of control | 

### Return type

[**PcControl**](PcControl.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **GetCsControlsList**
> PcControls GetCsControlsList(ctx, optional)
Show list of controls

Show list of controls

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
 **optional** | ***ControlApiGetCsControlsListOpts** | optional parameters | nil if no parameters

### Optional Parameters
Optional parameters are passed through a pointer to a ControlApiGetCsControlsListOpts struct
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **optional.String**| Filter the containers list by providing a query using Qualys syntax. | 
 **pageNumber** | **optional.Int32**| The page to be returned. | [default to 1]
 **pageSize** | **optional.Int32**| The number of records per page to be included in the response. | [default to 50]
 **sort** | **optional.String**| Sort the results using a Qualys token. | 

### Return type

[**PcControls**](PcControls.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

