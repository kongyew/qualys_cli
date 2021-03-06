/*
 * Container Security API
 *
 * # Authentication You must authenticate to the Qualys Cloud Platform using Qualys account credentials (user name and password) and get the JSON Web Token (JWT) before you can start using the Container Security APIs. Use the Qualys Authentication API to get the JWT.  **Example Authentication Curl Request**:  curl -X POST https://gateway/auth -H 'Content-Type: application/x-www-form-urlencoded' -d 'username=value1&password=passwordValue&token=true' where - gateway is the base URL to the Qualys API server where your account is located. - **username** and **password** are the credentials of the user account for which you want to fetch Container Security data. - **token** should be **true** - **Content-Type** should be **application/x-www-form-urlencoded** 
 *
 * API version: v1.3
 * Generated by: Swagger Codegen (https://github.com/swagger-api/swagger-codegen.git)
 */
package api

type ImageDetails struct {
	Created string `json:"created,omitempty"`
	Updated string `json:"updated,omitempty"`
	Author string `json:"author,omitempty"`
	Repo []Repo `json:"repo,omitempty"`
	RepoDigests []RepoDigest `json:"repoDigests,omitempty"`
	Label []BulkContainerDetailsLabel `json:"label,omitempty"`
	Uuid string `json:"uuid,omitempty"`
	Sha string `json:"sha,omitempty"`
	OperatingSystem string `json:"operatingSystem,omitempty"`
	CustomerUuid string `json:"customerUuid,omitempty"`
	DockerVersion string `json:"dockerVersion,omitempty"`
	Size int32 `json:"size,omitempty"`
	Layers []Layer `json:"layers,omitempty"`
	Host []Host `json:"host,omitempty"`
	Architecture string `json:"architecture,omitempty"`
	ImageId string `json:"imageId,omitempty"`
	RegistryUuid []string `json:"registryUuid,omitempty"`
	Source []string `json:"source,omitempty"`
	TotalVulnCount int32 `json:"totalVulnCount,omitempty"`
	Users []string `json:"users,omitempty"`
	InstrumentationState string `json:"instrumentationState,omitempty"`
	InstrumentedFrom string `json:"instrumentedFrom,omitempty"`
	IsDockerHubOfficial bool `json:"isDockerHubOfficial,omitempty"`
	IsInstrumented bool `json:"isInstrumented,omitempty"`
	ScanType string `json:"scanType,omitempty"`
	ScanErrorCode string `json:"scanErrorCode,omitempty"`
	ScanStatus string `json:"scanStatus,omitempty"`
	LastFoundOnHost *Host `json:"lastFoundOnHost,omitempty"`
}
