# {{classname}}

All URIs are relative to *https://gateway.qg2.apps.qualys.com/csapi/v1.3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**DeleteCsContainers**](ContainerApi.md#DeleteCsContainers) | **Delete** /containers | Delete containers in your account
[**GetContainerDetailsUsingGET**](ContainerApi.md#GetContainerDetailsUsingGET) | **Get** /containers/{containerSha} | show details of a container
[**GetContainerListWithDetails**](ContainerApi.md#GetContainerListWithDetails) | **Get** /containers/list | Containers Bulk API
[**GetContainerPolicyComplianceDetailsUsingGET**](ContainerApi.md#GetContainerPolicyComplianceDetailsUsingGET) | **Get** /containers/{containerSha}/compliance | show policy compliance details of a container
[**GetContainerSoftwareUsingGET**](ContainerApi.md#GetContainerSoftwareUsingGET) | **Get** /containers/{containerSha}/software | Show software installed on a container
[**GetContainerVulnCountUsingGET**](ContainerApi.md#GetContainerVulnCountUsingGET) | **Get** /containers/{containerSha}/vuln/count | Show vulnerability count for a container
[**GetContainerVulnUsingGET**](ContainerApi.md#GetContainerVulnUsingGET) | **Get** /containers/{containerSha}/vuln | Show vulnerability details for a container
[**GetCsContainersDataUsingGET**](ContainerApi.md#GetCsContainersDataUsingGET) | **Get** /containers | Show a list of containers in your account

# **DeleteCsContainers**
> string DeleteCsContainers(ctx, optional)
Delete containers in your account

Provide one or more container Ids or filters in the format shown under Example Value.

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
 **optional** | ***ContainerApiDeleteCsContainersOpts** | optional parameters | nil if no parameters

### Optional Parameters
Optional parameters are passed through a pointer to a ContainerApiDeleteCsContainersOpts struct
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **containerIds** | [**optional.Interface of []string**](string.md)| delete the containers from uuid | 
 **filter** | **optional.String**| delete the containers from filter | 

### Return type

**string**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **GetContainerDetailsUsingGET**
> ContainerDetails GetContainerDetailsUsingGET(ctx, containerSha)
show details of a container

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
  **containerSha** | **string**| Specify the SHA value of a Container in the user’s scope. | 

### Return type

[**ContainerDetails**](ContainerDetails.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **GetContainerListWithDetails**
> BulkContainerDetailsList GetContainerListWithDetails(ctx, optional)
Containers Bulk API

Returns response with given number of Container records according to filter along with next page filter query.

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
 **optional** | ***ContainerApiGetContainerListWithDetailsOpts** | optional parameters | nil if no parameters

### Optional Parameters
Optional parameters are passed through a pointer to a ContainerApiGetContainerListWithDetailsOpts struct
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **optional.String**| Filter the containers list by providing a query using Qualys syntax. | 
 **paginationQuery** | **optional.String**| The next page filter query. | 
 **limit** | **optional.Int32**| The number of records per page to be included in the response. | [default to 50]

### Return type

[**BulkContainerDetailsList**](BulkContainerDetailsList.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **GetContainerPolicyComplianceDetailsUsingGET**
> PolicyComplianceDetails GetContainerPolicyComplianceDetailsUsingGET(ctx, containerSha)
show policy compliance details of a container

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
  **containerSha** | **string**| Specify the SHA value of a Container in the user’s scope. | 

### Return type

[**PolicyComplianceDetails**](PolicyComplianceDetails.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **GetContainerSoftwareUsingGET**
> ContainerSoftware GetContainerSoftwareUsingGET(ctx, containerSha, optional)
Show software installed on a container

Show software installed on a container

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
  **containerSha** | **string**| Specify the SHA value of a Container in the user’s scope. | 
 **optional** | ***ContainerApiGetContainerSoftwareUsingGETOpts** | optional parameters | nil if no parameters

### Optional Parameters
Optional parameters are passed through a pointer to a ContainerApiGetContainerSoftwareUsingGETOpts struct
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **filter** | **optional.String**| Filter the containers list by providing a query using Qualys syntax. | 
 **sort** | **optional.String**| Sort the results using a Qualys token. For example created:desc | [default to created:desc]
 **isDrift** | **optional.Bool**|  | [default to false]

### Return type

[**ContainerSoftware**](ContainerSoftware.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **GetContainerVulnCountUsingGET**
> interface{} GetContainerVulnCountUsingGET(ctx, containerSha)
Show vulnerability count for a container

Show vulnerability count for a container

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
  **containerSha** | **string**| Specify the SHA value of a Container in the user’s scope. | 

### Return type

[**interface{}**](interface{}.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **GetContainerVulnUsingGET**
> ContainerVuln GetContainerVulnUsingGET(ctx, containerSha, optional)
Show vulnerability details for a container

Show vulnerability details for a container

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
  **containerSha** | **string**| Specify the SHA value of a Container in the user’s scope. | 
 **optional** | ***ContainerApiGetContainerVulnUsingGETOpts** | optional parameters | nil if no parameters

### Optional Parameters
Optional parameters are passed through a pointer to a ContainerApiGetContainerVulnUsingGETOpts struct
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **filter** | **optional.String**| Filter the container vulnerability details by providing a query using Qualys syntax. | 
 **type_** | **optional.String**|  | [default to ALL]
 **isDrift** | **optional.Bool**|  | [default to false]

### Return type

[**ContainerVuln**](ContainerVuln.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **GetCsContainersDataUsingGET**
> Containers GetCsContainersDataUsingGET(ctx, optional)
Show a list of containers in your account

Show a list of containers in your account

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
 **optional** | ***ContainerApiGetCsContainersDataUsingGETOpts** | optional parameters | nil if no parameters

### Optional Parameters
Optional parameters are passed through a pointer to a ContainerApiGetCsContainersDataUsingGETOpts struct
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **optional.String**| Filter the containers list by providing a query using Qualys syntax. | 
 **pageNumber** | **optional.Int32**| The page to be returned. | [default to 1]
 **pageSize** | **optional.Int32**| The number of records per page to be included in the response. | [default to 50]
 **sort** | **optional.String**| Sort the results using a Qualys token. | [default to created:desc]

### Return type

[**Containers**](Containers.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

