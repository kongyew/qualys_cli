# {{classname}}

All URIs are relative to *https://gateway.qg2.apps.qualys.com/csapi/v1.3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**CancelCsRegistrySchedule**](RegistryApi.md#CancelCsRegistrySchedule) | **Post** /registry/{registryId}/schedule/{scheduleId}/cancel | Cancel registry schedule in your account.
[**CreateCsAcrConnector**](RegistryApi.md#CreateCsAcrConnector) | **Post** /registry/acr/connector | Create new ACR connector
[**CreateCsAwsConnector**](RegistryApi.md#CreateCsAwsConnector) | **Post** /registry/aws/connector | Create new AWS connector
[**CreateCsGcpConnector**](RegistryApi.md#CreateCsGcpConnector) | **Post** /registry/gcp/connector | Create new GCP connector
[**CreateCsRegistry**](RegistryApi.md#CreateCsRegistry) | **Post** /registry | Create a new registry
[**CreateCsRegistrySchedule**](RegistryApi.md#CreateCsRegistrySchedule) | **Post** /registry/{registryId}/schedule | Create a new Registry scan schedule
[**DeleteCsRegistries**](RegistryApi.md#DeleteCsRegistries) | **Delete** /registry | Delete multiple registries in your account
[**DeleteCsRegistry**](RegistryApi.md#DeleteCsRegistry) | **Delete** /registry/{registryId} | Delete registry in you account
[**DeleteCsRegistrySchedule**](RegistryApi.md#DeleteCsRegistrySchedule) | **Delete** /registry/{registryId}/schedule/{scheduleId} | Delete registry schedule in your account
[**DeleteCsRegistrySchedules**](RegistryApi.md#DeleteCsRegistrySchedules) | **Delete** /registry/{registryId}/schedule | Delete multiple registry schedules in your account
[**GetCsAcrConnectorsByAwsAccountIdUsingGET**](RegistryApi.md#GetCsAcrConnectorsByAwsAccountIdUsingGET) | **Get** /registry/acr/connector/{connectorId} | Show ACR connector details
[**GetCsAcrConnectorsListUsingGET**](RegistryApi.md#GetCsAcrConnectorsListUsingGET) | **Get** /registry/acr/connectors | Show list of ACR connectors in your account
[**GetCsAwsAccountIdUsingGET**](RegistryApi.md#GetCsAwsAccountIdUsingGET) | **Get** /registry/aws-base | Fetch AWS account ID and external ID for your account
[**GetCsAwsConnectorsByAwsAccountIdUsingGET**](RegistryApi.md#GetCsAwsConnectorsByAwsAccountIdUsingGET) | **Get** /registry/aws/connectors/{accountId} | Show list of AWS connectors for an AWS account ID
[**GetCsAwsConnectorsListUsingGET**](RegistryApi.md#GetCsAwsConnectorsListUsingGET) | **Get** /registry/aws/connectors | Show list of AWS connectors in your account
[**GetCsGcpConnectorsByGcpConnectorIdUsingGET**](RegistryApi.md#GetCsGcpConnectorsByGcpConnectorIdUsingGET) | **Get** /registry/gcp/connector/{connectorId} | Get GCP connector by connectorId
[**GetCsGcpConnectorsListUsingGET**](RegistryApi.md#GetCsGcpConnectorsListUsingGET) | **Get** /registry/gcp/connectors | Show list of GCP connectors in your account
[**GetCsRegistriesDataUsingGET**](RegistryApi.md#GetCsRegistriesDataUsingGET) | **Get** /registry | Show a list of registries in your account
[**GetCsRegistryDetails**](RegistryApi.md#GetCsRegistryDetails) | **Get** /registry/{registryId} | Show details of a registry
[**GetCsRegistryRepositories**](RegistryApi.md#GetCsRegistryRepositories) | **Get** /registry/{registryId}/repository | Show a list of repositories in a registry
[**GetCsRegistrySchedules**](RegistryApi.md#GetCsRegistrySchedules) | **Get** /registry/{registryId}/schedule | Show a list of schedules created for a registry
[**UpdateCsRegistry**](RegistryApi.md#UpdateCsRegistry) | **Put** /registry/{registryId} | Update exiting registry in your account
[**UpdateCsRegistrySchedule**](RegistryApi.md#UpdateCsRegistrySchedule) | **Put** /registry/{registryId}/schedule/{scheduleId} | Update existing registry schedule in your account
[**ValidateCsRegistry**](RegistryApi.md#ValidateCsRegistry) | **Post** /registry/validate | Validate information for new registry

# **CancelCsRegistrySchedule**
> string CancelCsRegistrySchedule(ctx, registryId, scheduleId)
Cancel registry schedule in your account.

Cancel registry schedule in your account.

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
  **registryId** | **string**| Provide the ID/UUID of the registry you want to cancel the schedule for. | 
  **scheduleId** | **string**| Provide the ID/UUID of the schedule you want to cancel. You can only cancel schedules which are in the state: Created, Queued, Paused, Running, BaselineQueued or BasinelineRunning | 

### Return type

**string**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **CreateCsAcrConnector**
> string CreateCsAcrConnector(ctx, body)
Create new ACR connector

Create new ACR connector

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
  **body** | [**AcrConnectorRequest**](AcrConnectorRequest.md)| Provide parameter values in the format shown under Example Value. | 

### Return type

**string**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **CreateCsAwsConnector**
> string CreateCsAwsConnector(ctx, body)
Create new AWS connector

Create new AWS connector

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
  **body** | [**AwsConnectorRequest**](AwsConnectorRequest.md)| Provide parameter values in the format shown under Example Value. | 

### Return type

**string**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **CreateCsGcpConnector**
> string CreateCsGcpConnector(ctx, serviceAccountJson, name, optional)
Create new GCP connector

Create new GCP connector

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
  **serviceAccountJson** | ***os.File*****os.File**|  | 
  **name** | **string**| Provide the name for the connector | 
 **optional** | ***RegistryApiCreateCsGcpConnectorOpts** | optional parameters | nil if no parameters

### Optional Parameters
Optional parameters are passed through a pointer to a RegistryApiCreateCsGcpConnectorOpts struct
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


 **description** | **optional.**| Provide the description for the connector | 
 **connectorId** | **optional.**| Provide the connector id for the connector | 

### Return type

**string**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **CreateCsRegistry**
> string CreateCsRegistry(ctx, body)
Create a new registry

Create a new registry

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
  **body** | [**RegistryRequest**](RegistryRequest.md)| Provide parameter values in the format shown under Example Value. Parameters accountId, arn, and region are required when the registryType is AWS ECR and you want to create a new AWS connector. Specify the ARN if you want to use an existing AWS connector, or if you want to create a new connector. All parameters are required other than dockerHubOrgName which is optional. | 

### Return type

**string**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **CreateCsRegistrySchedule**
> string CreateCsRegistrySchedule(ctx, body, registryId)
Create a new Registry scan schedule

Create a new Registry scan schedule

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
  **body** | [**ScheduleRequest**](ScheduleRequest.md)| Provide parameter values in the format shown under Example Value. Specify &quot;onDemand&quot;: true if you want to scan immediately. Otherwise, Automatic scan will be triggered everyday at a set time. For days, specify 1 to 7 days / 14 (for last two weeks). For schedule, specify time in UTC, e.g., 19:30. | 
  **registryId** | **string**| Provide the ID of the registry for which you want to scan. | 

### Return type

**string**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **DeleteCsRegistries**
> string DeleteCsRegistries(ctx, )
Delete multiple registries in your account

Delete multiple registries in your account

### Required Parameters
This endpoint does not need any parameter.

### Return type

**string**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **DeleteCsRegistry**
> string DeleteCsRegistry(ctx, registryId)
Delete registry in you account

Delete registry in you account

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
  **registryId** | **string**| Provide the ID/UUID of the registry you want to delete. Note: You cannot delete a registry whose schedules are in “Running” state. | 

### Return type

**string**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **DeleteCsRegistrySchedule**
> string DeleteCsRegistrySchedule(ctx, registryId, scheduleId)
Delete registry schedule in your account

Delete registry schedule in your account

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
  **registryId** | **string**| Provide the ID of the registry you want to delete. | 
  **scheduleId** | **string**| Provide the ID/UUID of the schedule you want to delete. Note: You cannot delete a schedule which is in “Running” state. | 

### Return type

**string**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **DeleteCsRegistrySchedules**
> string DeleteCsRegistrySchedules(ctx, registryId)
Delete multiple registry schedules in your account

Delete multiple registry schedules in your account

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
  **registryId** | **string**| Provide the ID of the registry for which you want to delete. | 

### Return type

**string**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **GetCsAcrConnectorsByAwsAccountIdUsingGET**
> AcrConnector GetCsAcrConnectorsByAwsAccountIdUsingGET(ctx, connectorId)
Show ACR connector details

Show ACR connector details

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
  **connectorId** | **string**| Provide the ACR connector Id to get connector details. | 

### Return type

[**AcrConnector**](AcrConnector.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **GetCsAcrConnectorsListUsingGET**
> []AcrConnector GetCsAcrConnectorsListUsingGET(ctx, )
Show list of ACR connectors in your account

Show list of ACR connectors in your account

### Required Parameters
This endpoint does not need any parameter.

### Return type

[**[]AcrConnector**](AcrConnector.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **GetCsAwsAccountIdUsingGET**
> AwsAccount GetCsAwsAccountIdUsingGET(ctx, )
Fetch AWS account ID and external ID for your account

Fetch AWS account ID and external ID for your account

### Required Parameters
This endpoint does not need any parameter.

### Return type

[**AwsAccount**](AwsAccount.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **GetCsAwsConnectorsByAwsAccountIdUsingGET**
> []AwsConnector GetCsAwsConnectorsByAwsAccountIdUsingGET(ctx, accountId)
Show list of AWS connectors for an AWS account ID

Show list of AWS connectors for an AWS account ID

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
  **accountId** | **string**| Provide the AWS account Id to get a list of connectors. | 

### Return type

[**[]AwsConnector**](AwsConnector.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **GetCsAwsConnectorsListUsingGET**
> AwsConnector GetCsAwsConnectorsListUsingGET(ctx, )
Show list of AWS connectors in your account

Show list of AWS connectors in your account

### Required Parameters
This endpoint does not need any parameter.

### Return type

[**AwsConnector**](AwsConnector.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **GetCsGcpConnectorsByGcpConnectorIdUsingGET**
> GcpConnector GetCsGcpConnectorsByGcpConnectorIdUsingGET(ctx, connectorId)
Get GCP connector by connectorId

Get GCP connector by connectorId

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
  **connectorId** | **string**| Provide the GCP connector Id to get connector details. | 

### Return type

[**GcpConnector**](GcpConnector.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **GetCsGcpConnectorsListUsingGET**
> []GcpConnector GetCsGcpConnectorsListUsingGET(ctx, )
Show list of GCP connectors in your account

Show list of GCP connectors in your account

### Required Parameters
This endpoint does not need any parameter.

### Return type

[**[]GcpConnector**](GcpConnector.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **GetCsRegistriesDataUsingGET**
> Registries GetCsRegistriesDataUsingGET(ctx, optional)
Show a list of registries in your account

Show a list of registries in your account

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
 **optional** | ***RegistryApiGetCsRegistriesDataUsingGETOpts** | optional parameters | nil if no parameters

### Optional Parameters
Optional parameters are passed through a pointer to a RegistryApiGetCsRegistriesDataUsingGETOpts struct
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **optional.String**| Filter the registries list by providing a query using Qualys syntax. | 
 **pageNumber** | **optional.Int32**| The page to be returned. | [default to 1]
 **pageSize** | **optional.Int32**| The number of records per page to be included in the response. | [default to 50]
 **sort** | **optional.String**| Sort the results using a Qualys token. | 

### Return type

[**Registries**](Registries.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **GetCsRegistryDetails**
> RegistryDetails GetCsRegistryDetails(ctx, registryId)
Show details of a registry

Show details of a registry

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
  **registryId** | **string**| Provide the ID/UUID of the registry you want to fetch the details. | 

### Return type

[**RegistryDetails**](RegistryDetails.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **GetCsRegistryRepositories**
> Repositories GetCsRegistryRepositories(ctx, registryId, optional)
Show a list of repositories in a registry

Show a list of repositories in a registry

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
  **registryId** | **string**| Provide the ID of the registry for which you want to list the repositories. | 
 **optional** | ***RegistryApiGetCsRegistryRepositoriesOpts** | optional parameters | nil if no parameters

### Optional Parameters
Optional parameters are passed through a pointer to a RegistryApiGetCsRegistryRepositoriesOpts struct
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **filter** | **optional.String**| Filter the repository list by providing a query using Qualys syntax. | 
 **pageNumber** | **optional.Int32**| The page to be returned. | [default to 1]
 **pageSize** | **optional.Int32**| The number of records per page to be included in the response. | [default to 50]
 **sort** | **optional.String**| Sort the results using a Qualys token. | 

### Return type

[**Repositories**](Repositories.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **GetCsRegistrySchedules**
> Schedules GetCsRegistrySchedules(ctx, registryId, optional)
Show a list of schedules created for a registry

Show a list of schedules created for a registry

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
  **registryId** | **string**| Provide the ID of the registry for which you want to list the schedules. | 
 **optional** | ***RegistryApiGetCsRegistrySchedulesOpts** | optional parameters | nil if no parameters

### Optional Parameters
Optional parameters are passed through a pointer to a RegistryApiGetCsRegistrySchedulesOpts struct
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **filter** | **optional.String**| Filter the schedules list by providing a query using Qualys syntax. | 
 **pageNumber** | **optional.Int32**| The page to be returned. | [default to 1]
 **pageSize** | **optional.Int32**| The number of records per page to be included in the response. | [default to 50]
 **sort** | **optional.String**| Sort the results using a Qualys token. | 

### Return type

[**Schedules**](Schedules.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **UpdateCsRegistry**
> string UpdateCsRegistry(ctx, body, registryId)
Update exiting registry in your account

Update exiting registry in your account

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
  **body** | [**RegistryRequest**](RegistryRequest.md)| Provide parameter values in the format shown under Example Value. registryType and registryUri are required even though they are not updatable. | 
  **registryId** | **string**| Provide the ID/UUID of the registry you want to update. | 

### Return type

**string**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **UpdateCsRegistrySchedule**
> string UpdateCsRegistrySchedule(ctx, body, registryId, scheduleId)
Update existing registry schedule in your account

Update existing registry schedule in your account

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
  **body** | [**ScheduleRequest**](ScheduleRequest.md)| Provide parameter values in the format shown under Example Value. Specify &quot;onDemand&quot;: true if you want to scan immediately. Otherwise, Automatic scan will be triggered everyday at a set time. For days, specify 1 to 7 days / 14 (for last two weeks). For schedule, specify time in UTC, e.g., 19:30. | 
  **registryId** | **string**| Provide the ID of the registry you want to update. | 
  **scheduleId** | **string**| Provide the ID/UUID of the schedule you want to update. | 

### Return type

**string**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ValidateCsRegistry**
> bool ValidateCsRegistry(ctx, body)
Validate information for new registry

Validate information for new registry

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
  **body** | [**RegistryRequest**](RegistryRequest.md)| Validate parameters for a registry you intend to create. Provide parameter values in the format shown under Example Value. Parameters accountId, arn, and region are required when the registryType is AWS ECR and you want to create a new AWS connector. Specify the ARN if you want to use an existing AWS connector, or if you want to create a new connector. All parameters are required other than dockerHubOrgName which is optional. | 

### Return type

**bool**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

