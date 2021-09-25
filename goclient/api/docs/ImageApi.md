# {{classname}}

All URIs are relative to *https://gateway.qg2.apps.qualys.com/csapi/v1.3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**DeleteCsImages**](ImageApi.md#DeleteCsImages) | **Delete** /images | Delete images in your account
[**GetCsImagesDataUsingGET**](ImageApi.md#GetCsImagesDataUsingGET) | **Get** /images | Show a list of images in your account
[**GetImageAssociationUsingGET**](ImageApi.md#GetImageAssociationUsingGET) | **Get** /images/{imageSha}/association | show associations of an image
[**GetImageDetailsUsingGET**](ImageApi.md#GetImageDetailsUsingGET) | **Get** /images/{imageSha} | show details of an image
[**GetImageListWithDetails**](ImageApi.md#GetImageListWithDetails) | **Get** /images/list | Images Bulk API
[**GetImagePolicyComplianceDetailsUsingGET**](ImageApi.md#GetImagePolicyComplianceDetailsUsingGET) | **Get** /images/{imageSha}/compliance | show policy compliance details of an image
[**GetImageRegistriesUsingGET**](ImageApi.md#GetImageRegistriesUsingGET) | **Get** /images/{imageSha}/associatedRegistries | Get associated registries with Image
[**GetImageSoftwareUsingGET**](ImageApi.md#GetImageSoftwareUsingGET) | **Get** /images/{imageSha}/software | Show software installed on an image
[**GetImageVulnCountUsingGET**](ImageApi.md#GetImageVulnCountUsingGET) | **Get** /images/{imageSha}/vuln/count | Show vulnerability count for an image
[**GetImageVulnUsingGET**](ImageApi.md#GetImageVulnUsingGET) | **Get** /images/{imageSha}/vuln | Show vulnerability details for an image
[**InstrumenteImage**](ImageApi.md#InstrumenteImage) | **Post** /images/{imageSha}/instrument | Instrumenting the image identified by image id

# **DeleteCsImages**
> string DeleteCsImages(ctx, optional)
Delete images in your account

Provide one or more image Ids or filters in the format shown under Example Value.

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
 **optional** | ***ImageApiDeleteCsImagesOpts** | optional parameters | nil if no parameters

### Optional Parameters
Optional parameters are passed through a pointer to a ImageApiDeleteCsImagesOpts struct
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **imageIds** | [**optional.Interface of []string**](string.md)| delete the images from uuid | 
 **filter** | **optional.String**| delete the images from filter | 

### Return type

**string**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **GetCsImagesDataUsingGET**
> Images GetCsImagesDataUsingGET(ctx, optional)
Show a list of images in your account

Show a list of images in your account

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
 **optional** | ***ImageApiGetCsImagesDataUsingGETOpts** | optional parameters | nil if no parameters

### Optional Parameters
Optional parameters are passed through a pointer to a ImageApiGetCsImagesDataUsingGETOpts struct
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **optional.String**| Filter the images list by providing a query using Qualys syntax. | 
 **pageNumber** | **optional.Int32**| The page to be returned. | [default to 1]
 **pageSize** | **optional.Int32**| The number of records per page to be included in the response. | [default to 50]
 **sort** | **optional.String**| Sort the results using a Qualys token. | [default to created:desc]

### Return type

[**Images**](Images.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **GetImageAssociationUsingGET**
> ImageAssociation GetImageAssociationUsingGET(ctx, imageSha, optional)
show associations of an image

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
  **imageSha** | **string**| Specify the SHA value of an Image in the user’s scope. | 
 **optional** | ***ImageApiGetImageAssociationUsingGETOpts** | optional parameters | nil if no parameters

### Optional Parameters
Optional parameters are passed through a pointer to a ImageApiGetImageAssociationUsingGETOpts struct
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **filter** | **optional.String**|  | 
 **type_** | **optional.String**|  | 

### Return type

[**ImageAssociation**](ImageAssociation.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **GetImageDetailsUsingGET**
> ImageDetails GetImageDetailsUsingGET(ctx, imageSha)
show details of an image

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
  **imageSha** | **string**| Specify the SHA value of an Image in the user’s scope. | 

### Return type

[**ImageDetails**](ImageDetails.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **GetImageListWithDetails**
> BulkImageDetailsList GetImageListWithDetails(ctx, optional)
Images Bulk API

Returns response with given number of Image records according to filter along with next page filter query.

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
 **optional** | ***ImageApiGetImageListWithDetailsOpts** | optional parameters | nil if no parameters

### Optional Parameters
Optional parameters are passed through a pointer to a ImageApiGetImageListWithDetailsOpts struct
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **optional.String**| Filter the containers list by providing a query using Qualys syntax. | 
 **paginationQuery** | **optional.String**| The next page filter query. | 
 **limit** | **optional.Int32**| The number of records per page to be included in the response. | [default to 50]

### Return type

[**BulkImageDetailsList**](BulkImageDetailsList.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **GetImagePolicyComplianceDetailsUsingGET**
> PolicyComplianceDetails GetImagePolicyComplianceDetailsUsingGET(ctx, imageSha)
show policy compliance details of an image

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
  **imageSha** | **string**| Specify the SHA value of an Image in the user’s scope. | 

### Return type

[**PolicyComplianceDetails**](PolicyComplianceDetails.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **GetImageRegistriesUsingGET**
> []ImageRegistriesInner GetImageRegistriesUsingGET(ctx, imageSha)
Get associated registries with Image

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
  **imageSha** | **string**| Specify the SHA value of an Image in the user’s scope. | 

### Return type

[**[]ImageRegistriesInner**](array.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **GetImageSoftwareUsingGET**
> ImageSoftware GetImageSoftwareUsingGET(ctx, imageSha, optional)
Show software installed on an image

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
  **imageSha** | **string**| Specify the SHA value of an Image in the user’s scope. | 
 **optional** | ***ImageApiGetImageSoftwareUsingGETOpts** | optional parameters | nil if no parameters

### Optional Parameters
Optional parameters are passed through a pointer to a ImageApiGetImageSoftwareUsingGETOpts struct
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **filter** | **optional.String**| Filter the image vulnerability details by providing a query using Qualys syntax. | 
 **sort** | **optional.String**| Sort the results using a Qualys token. | 

### Return type

[**ImageSoftware**](ImageSoftware.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **GetImageVulnCountUsingGET**
> interface{} GetImageVulnCountUsingGET(ctx, imageSha)
Show vulnerability count for an image

Show vulnerability count for an image

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
  **imageSha** | **string**| Specify the SHA value of an Image in the user’s scope. | 

### Return type

[**interface{}**](interface{}.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **GetImageVulnUsingGET**
> ImageVulnerability GetImageVulnUsingGET(ctx, imageSha, optional)
Show vulnerability details for an image

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
  **imageSha** | **string**| Specify the SHA value of an Image in the user’s scope. | 
 **optional** | ***ImageApiGetImageVulnUsingGETOpts** | optional parameters | nil if no parameters

### Optional Parameters
Optional parameters are passed through a pointer to a ImageApiGetImageVulnUsingGETOpts struct
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **filter** | **optional.String**| Filter the image vulnerability details by providing a query using Qualys syntax. | 
 **type_** | **optional.String**| Specify the type of information to be fetched: Summary, Details, All | [default to ALL]
 **sort** | **optional.String**| Sort the results using a Qualys token. | [default to qid:asc]

### Return type

[**ImageVulnerability**](ImageVulnerability.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **InstrumenteImage**
> string InstrumenteImage(ctx, body, imageSha)
Instrumenting the image identified by image id

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
  **body** | [**InstrumentRequest**](InstrumentRequest.md)| Provide parameter values in the format shown under Example Value. | 
  **imageSha** | **string**| Specify the SHA value of an Image in the user’s scope. | 

### Return type

**string**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

