import json
import os
from tokenize import Number, String
from typing import List
from httpx import Client as HttpxClient
from aqua_rest_api_client import AuthenticatedClient
from aqua_rest_api_client.api.project import project_get_all
from aqua_rest_api_client.api.test_case import test_case_create
from aqua_rest_api_client.models.api_project_info import ApiProjectInfo
from aqua_rest_api_client.models.api_item_new_with_test_data_and_test_steps import (
    ApiItemNewWithTestDataAndTestSteps,
)
from aqua_rest_api_client.models.api_item_location_update import ApiItemLocationUpdate
from aqua_rest_api_client.models.api_field_update import ApiFieldUpdate
from aqua_rest_api_client.models.api_rich_text import ApiRichText
from aqua_rest_api_client.models.api_test_step_new import ApiTestStepNew

def get_access_token(
    aqua_base_url: String, aqua_user: String, aqua_password: String
) -> String:
    # Authenticate against aqua server. The token is 15min valid, refresh_token can be used to generate a new token.
    auth_client = HttpxClient(base_url=aqua_base_url)
    response = auth_client.post(
        url="api/token",
        data={
            "grant_type": "password",
            "username": aqua_user,
            "password": aqua_password,
        },
        headers={"Content-Type": "application/x-www-form-urlencoded"},
    )

    response = json.loads(response.content)

    return response["access_token"]


def get_project_by_name(client: AuthenticatedClient, name: String) -> ApiProjectInfo:
    projects: List[ApiProjectInfo] = project_get_all.sync_detailed(client=client).parsed
    return next(filter(lambda p: p.name == name, projects), None)


def create_test_case_with_steps(client: AuthenticatedClient, project_id: Number):
    new_test_case = ApiItemNewWithTestDataAndTestSteps(
        # FolderId 0 is the root folder.
        location=ApiItemLocationUpdate(project_id=project_id, folder_id=0),
        description=ApiRichText(html="REST API Python <br> Hello World!"),
        # Name is a required field.
        details=[ApiFieldUpdate(field_id="Name", value="New API TestCase")],
        test_steps=[
            ApiTestStepNew(
                index=1,
                name="A step",
                description=ApiRichText(plain_text="This is a test step"),
                expected_result=ApiRichText(plain_text="Expected result"),
            )
        ],
    )

    return test_case_create.sync_detailed(client=client, json_body=new_test_case)


def main():
    aqua_user = os.environ["aqua_user"]
    aqua_password = os.environ["aqua_password"]
    aqua_base_url = os.environ["aqua_base_url"]

    access_token = get_access_token(aqua_base_url, aqua_user, aqua_password)
    client = AuthenticatedClient(
        base_url=aqua_base_url, token=access_token
    )
    project = get_project_by_name(client, "start")
    new_test_case = create_test_case_with_steps(client, project.id)
    print(new_test_case)

if __name__ == "__main__":
    main()