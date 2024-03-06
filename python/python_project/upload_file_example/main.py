import json
import os
from httpx import Client as HttpxClient
from aqua_rest_api_client import AuthenticatedClient
from aqua_rest_api_client.api.file import file_upload_file
from aqua_rest_api_client.models import FileUploadFileMultipartData
from aqua_rest_api_client.types import File
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


def upload_file_text_like_file(client: AuthenticatedClient, file_path: str) -> None:
    with open(file_path,"r") as file:
        data = file.read()

        file_to_upload = File(file_name=file.name, payload=data)
        multipart_data = FileUploadFileMultipartData(file=[file_to_upload])
        result = file_upload_file.sync(client=client, file_name=file.name, multipart_data=multipart_data)
        print(result)


def upload_binary_file(aqua_base_url: str, access_token: str, file_path: str) -> None:
    with open(file_path,"rb") as file:
        headers = {
            "Authorization": f"Bearer {access_token}"
        }
        response = requests.post(f"{aqua_base_url}/api/File?fileName={file.name}", data=file.raw, headers=headers)
        if response.ok:
            print("Upload complete")
            print(response.content)
        else:
            print("Something went wrong")
            print(response.content)


def main():
    aqua_user = os.environ["aqua_user"] # provide user name
    aqua_password = os.environ["aqua_password"] # provide password
    aqua_base_url = os.environ["aqua_base_url"] # provide aqua url with the folder e.g.: https://domain:port/aquaWebNG

    access_token = get_access_token(aqua_base_url, aqua_user, aqua_password)
    client = AuthenticatedClient(
        base_url=aqua_base_url, token=access_token
    )

    upload_file_text_like_file(client, "test.txt")
    
    upload_binary_file(aqua_base_url, access_token, "test.zip")

if __name__ == "__main__":
   main()