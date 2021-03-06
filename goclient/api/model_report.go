/*
 * Container Security API
 *
 * # Authentication You must authenticate to the Qualys Cloud Platform using Qualys account credentials (user name and password) and get the JSON Web Token (JWT) before you can start using the Container Security APIs. Use the Qualys Authentication API to get the JWT.  **Example Authentication Curl Request**:  curl -X POST https://gateway/auth -H 'Content-Type: application/x-www-form-urlencoded' -d 'username=value1&password=passwordValue&token=true' where - gateway is the base URL to the Qualys API server where your account is located. - **username** and **password** are the credentials of the user account for which you want to fetch Container Security data. - **token** should be **true** - **Content-Type** should be **application/x-www-form-urlencoded** 
 *
 * API version: v1.3
 * Generated by: Swagger Codegen (https://github.com/swagger-api/swagger-codegen.git)
 */
package api

type Report struct {
	CreatedAt string `json:"createdAt,omitempty"`
	Description string `json:"description,omitempty"`
	FileFormat string `json:"fileFormat,omitempty"`
	ReportUuid string `json:"reportUuid,omitempty"`
	Filter string `json:"filter,omitempty"`
	// Provide parameter values in the format shown under Example Value.
	DisplayColumns []string `json:"displayColumns,omitempty"`
	ReportName string `json:"reportName,omitempty"`
	ReportType string `json:"reportType,omitempty"`
	Status string `json:"status,omitempty"`
	TemplateName string `json:"templateName,omitempty"`
}
