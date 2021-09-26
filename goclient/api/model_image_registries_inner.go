/*
 * Container Security API
 *
 * # Authentication You must authenticate to the Qualys Cloud Platform using Qualys account credentials (user name and password) and get the JSON Web Token (JWT) before you can start using the Container Security APIs. Use the Qualys Authentication API to get the JWT.  **Example Authentication Curl Request**:  curl -X POST https://gateway/auth -H 'Content-Type: application/x-www-form-urlencoded' -d 'username=value1&password=passwordValue&token=true' where - gateway is the base URL to the Qualys API server where your account is located. - **username** and **password** are the credentials of the user account for which you want to fetch Container Security data. - **token** should be **true** - **Content-Type** should be **application/x-www-form-urlencoded** 
 *
 * API version: v1.3
 * Generated by: Swagger Codegen (https://github.com/swagger-api/swagger-codegen.git)
 */
package api

type ImageRegistriesInner struct {
	Registry string `json:"registry,omitempty"`
	RegistryUuid string `json:"registryUuid,omitempty"`
	Repo string `json:"repo,omitempty"`
	Tag string `json:"tag,omitempty"`
}
