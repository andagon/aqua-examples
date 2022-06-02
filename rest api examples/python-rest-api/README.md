# aqua REST API Python Example

This example shows how to setup and use python to talk with the aqua REST-API.
It selects a project based on the name and creates a simple test case with test steps.

## Setup

- Install `poetry` and `openapi-python-client` modules
- Download the aqua swagger.json from https://aqua-server/aquaWebNG/Help
- We have an open defect that breaks some of the openapi generators, here is the workaround:
    - Edit the swagger.json and find `"securitySchemes"` and add a correct `tokenUrl` and `scope` to it:
    ```json
    "password": {
        "tokenUrl": "http://aqua-server/aquaWebNG/api/token",
        "scopes": {}
    }
    ```
- Generate aqua rest client: `openapi-python-client --path swagger.json`
  This creates an aqua-rest-api-client folder in your current work directory