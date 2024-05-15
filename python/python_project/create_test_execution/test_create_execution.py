import json
import os
from unittest import TestCase
from httpx import Client as HttpxClient
from aqua_rest_api_client import AuthenticatedClient
from aqua_rest_api_client.api.test_execution import test_execution_create
from aqua_rest_api_client.models import (
    ApiTestExecutionNew, ApiTestStepExecutionNew, ApiRichText,
    ApiTestStepExecutionUpdateStatus, ApiFieldValueTimeSpan, TimeUnit
)
import requests


def get_access_token(
    aqua_base_url: str, aqua_user: str, aqua_password: str
) -> str:
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


def create_aqua_execution_with_aqua_lib(client: AuthenticatedClient, test_case_id: int) -> None:
    execution = ApiTestExecutionNew(
        test_case_id=test_case_id,
        test_case_name="name of the test case",
        execution_duration=ApiFieldValueTimeSpan(value=20, unit=TimeUnit.HOUR, field_value_type="TimeSpan"),
        steps=[
            ApiTestStepExecutionNew(
                index=1,
                actual_results=ApiRichText(
                    incompatible_rich_text_features=False,
                    plain_text="some result in plain text as passed"
                ),
                status=ApiTestStepExecutionUpdateStatus.PASS
            ),
                        ApiTestStepExecutionNew(
                index=2,
                actual_results=ApiRichText(
                    incompatible_rich_text_features=False,
                    html="<h1>header 1</h1><p>some result in html text as failed</p>"
                ),
                status=ApiTestStepExecutionUpdateStatus.FAILED
            )
        ]
    )
    result = test_execution_create.sync(client=client, json_body=[execution])
    print(result)

def create_aqua_execution_with_requests(aqua_base_url: str, access_token: str, test_case_id: int, results: list) -> None:
    headers = {
        "Authorization": f"Bearer {access_token}"
    }

    steps = []
    for index, result in enumerate(results):
        status = "Pass" if result["status"] == 1 else "Failed"
        step = {
                    "Index": index + 1,
                    "ActualResults": {
                        "PlainText": f"some result in plain text as {status}, {result['message']}",
                        "IncompatibleRichTextFeatures": False
                    },
                    "Status": status
                }
        steps.append(step)
    
    object_body = [
        {
            "TestCaseId": test_case_id,
            "TestCaseName": "Name of the test case, ideally this was read beforehand from the test case",
            "ExecutionDuration": {
                "Value": 20.56,
                "Unit": "Hour",
                "FieldValueType": "TimeSpan"
            },
            "Steps": steps
        }
    ]

    response = requests.post(f"{aqua_base_url}/api/TestExecution", json=object_body, headers=headers)
    if response.ok:
        print("Upload complete")
        print(response.content)
    else:
        print("Something went wrong")
        print(response.content)


def send_results(results: list):
    aqua_user = os.environ["aqua_user"] # provide user name
    aqua_password = os.environ["aqua_password"] # provide password
    aqua_base_url = os.environ["aqua_base_url"] # provide aqua url with the folder e.g.: https://domain:port/aquaWebNG

    access_token = get_access_token(aqua_base_url, aqua_user, aqua_password)
    client = AuthenticatedClient(
        base_url=aqua_base_url, token=access_token
    )
    # create_aqua_execution_with_aqua_lib(client, 15733)
    
    create_aqua_execution_with_requests(aqua_base_url, access_token, 15733, results)


class TestExecution(TestCase):

    def test_execution_creation(self):
        self.step_results = []
        # Arrange
        result = "expected value"
        # Act
        # Assert
        
        try: self.assertEqual("expected value", result)
        except AssertionError as e: self.step_results.append({"status": 0, "message": str(e)})
        else: self.step_results.append({"status": 1, "message": ""})

        try: self.assertEqual("expected value1", result)
        except AssertionError as e: self.step_results.append({"status": 0, "message": str(e)})
        else: self.step_results.append({"status": 1, "message": ""})

        # post 
        send_results(self.step_results)
