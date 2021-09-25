# qualys_containersecurityapi
test


https://gateway.qg2.apps.qualys.com/apidocs/yaml/csapi-swagger-v1.3.yaml

swagger-codegen generate -i https://gateway.qg2.apps.qualys.com/apidocs/yaml/csapi-swagger-v1.3.yaml -l go -o /tmp/test/golang


swagger-codegen generate -i generate \
 -i  https://gateway.qg2.apps.qualys.com/apidocs/yaml/csapi-swagger-v1.3.yaml -l go \
 --git-user-id "kongyew" \
 --git-repo-id "qualys_containersecurityapi" \
 --release-note " integration demo" \
  --config ./swagger-config.json
 -o /Users/kchan/code/qualys_containersecurityapi/goclient

 swagger-codegen config-help -l go

CONFIG OPTIONS
	packageName
	    Go package name (convention: lowercase). (Default: swagger)

	hideGenerationTimestamp
	    Hides the generation timestamp when files are generated. (Default: true)

	packageVersion
	    Go package version. (Default: 1.0.0)

	withXml
	    whether to include support for application/xml content type and include XML annotations in the mo


        {"optionKey":"optionValue", "optionKey1":"optionValue1"}