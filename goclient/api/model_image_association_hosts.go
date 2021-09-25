/*
 * Container Security API
 *
 * # Authentication You must authenticate to the Qualys Cloud Platform using Qualys account credentials (user name and password) and get the JSON Web Token (JWT) before you can start using the Container Security APIs. Use the Qualys Authentication API to get the JWT.  **Example Authentication Curl Request**:  curl -X POST https://gateway/auth -H 'Content-Type: application/x-www-form-urlencoded' -d 'username=value1&password=passwordValue&token=true' where - gateway is the base URL to the Qualys API server where your account is located. - **username** and **password** are the credentials of the user account for which you want to fetch Container Security data. - **token** should be **true** - **Content-Type** should be **application/x-www-form-urlencoded** 
 *
 * API version: v1.3
 * Generated by: Swagger Codegen (https://github.com/swagger-api/swagger-codegen.git)
 */
package qualys

type ImageAssociationHosts struct {
	CreatedContainerCount int32 `json:"createdContainerCount,omitempty"`
	CreatedContainerCountForAssociatedImage int32 `json:"createdContainerCountForAssociatedImage,omitempty"`
	Hostname string `json:"hostname,omitempty"`
	IpAddress string `json:"ipAddress,omitempty"`
	PausedContainerCount int32 `json:"pausedContainerCount,omitempty"`
	PausedContainerCountForAssociatedImage int32 `json:"pausedContainerCountForAssociatedImage,omitempty"`
	RunningContainerCount int32 `json:"runningContainerCount,omitempty"`
	RunningContainerCountForAssociatedImage int32 `json:"runningContainerCountForAssociatedImage,omitempty"`
	SensorUuid string `json:"sensorUuid,omitempty"`
	StoppedContainerCount int32 `json:"stoppedContainerCount,omitempty"`
	StoppedContainerCountForAssociatedImage int32 `json:"stoppedContainerCountForAssociatedImage,omitempty"`
	Uuid string `json:"uuid,omitempty"`
}