download-dependencies:
	wget https://repo1.maven.org/maven2/io/swagger/codegen/v3/swagger-codegen-cli/3.0.25/swagger-codegen-cli-3.0.25.jar -O swagger-codegen-cli.jar

generate: download-dependencies
	java -jar swagger-codegen-cli.jar generate -i example.yaml -l go -o codegen/bitbucket/pkg/bitbucketssh -DpackageName=bitbucketssh