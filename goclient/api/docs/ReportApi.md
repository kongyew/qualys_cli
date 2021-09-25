# {{classname}}

All URIs are relative to *https://gateway.qg2.apps.qualys.com/csapi/v1.3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**CreateReportRequest**](ReportApi.md#CreateReportRequest) | **Post** /reports | Create Report request
[**DeleteCsReports**](ReportApi.md#DeleteCsReports) | **Delete** /reports | Delete Reports in your account
[**GetCsReportDownload**](ReportApi.md#GetCsReportDownload) | **Get** /reports/{reportUuid}/download | Show a details of a Report.
[**GetCsReportsList**](ReportApi.md#GetCsReportsList) | **Get** /reports | Show a list of reports in your account.

# **CreateReportRequest**
> string CreateReportRequest(ctx, body)
Create Report request

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
  **body** | [**ReportRequest**](ReportRequest.md)| Provide parameter values in the format shown under Example Value. displayColumns can have following values if your template is &lt;table&gt; &lt;tr&gt; &lt;th&gt;CS_IMAGE_VULNERABILITY&lt;/th&gt; &lt;td&gt;repo, imageId, sha, uuid, created, updated,  qid, title, severity, cveids, vendorReference, cvssBase, cvssTemporal, cvss3Base, cvss3Temporal, threat, impact, solution, exploitability, associatedMalwares, category, software, result&lt;/td&gt; &lt;/tr&gt; &lt;tr&gt; &lt;th&gt;CS_CONTAINER_VULNERABILITY&lt;/th&gt; &lt;td&gt; name, containerId, uuid, imageId, created, hostName, hostIp, state, stateChanged, updated,  qid, title, severity, cveids, vendorReference, cvssBase, cvssTemporal, cvss3Base, cvss3Temporal, threat, impact, solution, exploitability, associatedMalwares, category, software, result&lt;/td&gt; &lt;/tr&gt; &lt;/table&gt; &lt;BR&gt; | 

### Return type

**string**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **DeleteCsReports**
> ReportsDeleteSucccess DeleteCsReports(ctx, reportUuids)
Delete Reports in your account

Delete Reports in your account

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
  **reportUuids** | [**[]string**](string.md)| delete the reports from uuid | 

### Return type

[**ReportsDeleteSucccess**](ReportsDeleteSucccess.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **GetCsReportDownload**
> interface{} GetCsReportDownload(ctx, reportUuid)
Show a details of a Report.

Show a details of a Report.

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
  **reportUuid** | **string**| Specify the report UUID of a specific report in the user’s scope | 

### Return type

[**interface{}**](interface{}.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **GetCsReportsList**
> Reports GetCsReportsList(ctx, optional)
Show a list of reports in your account.

Show a list of reports in your account.

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
 **optional** | ***ReportApiGetCsReportsListOpts** | optional parameters | nil if no parameters

### Optional Parameters
Optional parameters are passed through a pointer to a ReportApiGetCsReportsListOpts struct
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **optional.String**| Filter the reports list by providing a query using Qualys syntax.Only reportName is supported in filter query. | 
 **pageNumber** | **optional.Int32**| The page to be returned. | [default to 1]
 **pageSize** | **optional.Int32**| The number of records per page to be included in the response. | [default to 50]
 **sort** | **optional.String**| Supported values are reportName/ status. | [default to status:desc]

### Return type

[**Reports**](Reports.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

