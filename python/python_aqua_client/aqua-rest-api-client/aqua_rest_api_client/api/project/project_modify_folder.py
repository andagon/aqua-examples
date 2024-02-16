from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_argument_error import ApiArgumentError
from ...models.api_backend_not_available_error import ApiBackendNotAvailableError
from ...models.api_forbidden_error import ApiForbiddenError
from ...models.api_internal_error import ApiInternalError
from ...models.api_long_operation_of_boolean import ApiLongOperationOfBoolean
from ...models.api_not_found_error import ApiNotFoundError
from ...models.api_project_folder_patch_operation import ApiProjectFolderPatchOperation
from ...models.api_unauthorized_error import ApiUnauthorizedError
from ...types import Response


def _get_kwargs(
    project_id: int,
    folder_id: int,
    *,
    client: AuthenticatedClient,
    json_body: ApiProjectFolderPatchOperation,
) -> Dict[str, Any]:
    url = "{}/api/Project/{projectId}/Folder/{folderId}".format(
        client.base_url, projectId=project_id, folderId=folder_id
    )

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_json_body = json_body.to_dict()

    return {
        "method": "patch",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "json": json_json_body,
    }


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[
    Union[
        ApiArgumentError,
        ApiBackendNotAvailableError,
        ApiForbiddenError,
        ApiInternalError,
        ApiLongOperationOfBoolean,
        ApiNotFoundError,
        ApiUnauthorizedError,
    ]
]:
    if response.status_code == HTTPStatus.OK:
        response_200 = ApiLongOperationOfBoolean.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = ApiArgumentError.from_dict(response.json())

        return response_400
    if response.status_code == HTTPStatus.FORBIDDEN:
        response_403 = ApiForbiddenError.from_dict(response.json())

        return response_403
    if response.status_code == HTTPStatus.NOT_FOUND:
        response_404 = ApiNotFoundError.from_dict(response.json())

        return response_404
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        response_401 = ApiUnauthorizedError.from_dict(response.json())

        return response_401
    if response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR:
        response_500 = ApiInternalError.from_dict(response.json())

        return response_500
    if response.status_code == HTTPStatus.SERVICE_UNAVAILABLE:
        response_503 = ApiBackendNotAvailableError.from_dict(response.json())

        return response_503
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[
    Union[
        ApiArgumentError,
        ApiBackendNotAvailableError,
        ApiForbiddenError,
        ApiInternalError,
        ApiLongOperationOfBoolean,
        ApiNotFoundError,
        ApiUnauthorizedError,
    ]
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    project_id: int,
    folder_id: int,
    *,
    client: AuthenticatedClient,
    json_body: ApiProjectFolderPatchOperation,
) -> Response[
    Union[
        ApiArgumentError,
        ApiBackendNotAvailableError,
        ApiForbiddenError,
        ApiInternalError,
        ApiLongOperationOfBoolean,
        ApiNotFoundError,
        ApiUnauthorizedError,
    ]
]:
    """Modify folder

     Modifiy folder with the given *folderId*.

    Args:
        project_id (int):
        folder_id (int):
        json_body (ApiProjectFolderPatchOperation): Represents data required to execute folder-
            modify operation.
            There are multiple folder modify operations supported - see
            ApiProjectFolderPatchOperationType.
            Depending on the type the actual properties can differ. See subclasses for details.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ApiArgumentError, ApiBackendNotAvailableError, ApiForbiddenError, ApiInternalError, ApiLongOperationOfBoolean, ApiNotFoundError, ApiUnauthorizedError]]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        folder_id=folder_id,
        client=client,
        json_body=json_body,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    project_id: int,
    folder_id: int,
    *,
    client: AuthenticatedClient,
    json_body: ApiProjectFolderPatchOperation,
) -> Optional[
    Union[
        ApiArgumentError,
        ApiBackendNotAvailableError,
        ApiForbiddenError,
        ApiInternalError,
        ApiLongOperationOfBoolean,
        ApiNotFoundError,
        ApiUnauthorizedError,
    ]
]:
    """Modify folder

     Modifiy folder with the given *folderId*.

    Args:
        project_id (int):
        folder_id (int):
        json_body (ApiProjectFolderPatchOperation): Represents data required to execute folder-
            modify operation.
            There are multiple folder modify operations supported - see
            ApiProjectFolderPatchOperationType.
            Depending on the type the actual properties can differ. See subclasses for details.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ApiArgumentError, ApiBackendNotAvailableError, ApiForbiddenError, ApiInternalError, ApiLongOperationOfBoolean, ApiNotFoundError, ApiUnauthorizedError]]
    """

    return sync_detailed(
        project_id=project_id,
        folder_id=folder_id,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    project_id: int,
    folder_id: int,
    *,
    client: AuthenticatedClient,
    json_body: ApiProjectFolderPatchOperation,
) -> Response[
    Union[
        ApiArgumentError,
        ApiBackendNotAvailableError,
        ApiForbiddenError,
        ApiInternalError,
        ApiLongOperationOfBoolean,
        ApiNotFoundError,
        ApiUnauthorizedError,
    ]
]:
    """Modify folder

     Modifiy folder with the given *folderId*.

    Args:
        project_id (int):
        folder_id (int):
        json_body (ApiProjectFolderPatchOperation): Represents data required to execute folder-
            modify operation.
            There are multiple folder modify operations supported - see
            ApiProjectFolderPatchOperationType.
            Depending on the type the actual properties can differ. See subclasses for details.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ApiArgumentError, ApiBackendNotAvailableError, ApiForbiddenError, ApiInternalError, ApiLongOperationOfBoolean, ApiNotFoundError, ApiUnauthorizedError]]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        folder_id=folder_id,
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_id: int,
    folder_id: int,
    *,
    client: AuthenticatedClient,
    json_body: ApiProjectFolderPatchOperation,
) -> Optional[
    Union[
        ApiArgumentError,
        ApiBackendNotAvailableError,
        ApiForbiddenError,
        ApiInternalError,
        ApiLongOperationOfBoolean,
        ApiNotFoundError,
        ApiUnauthorizedError,
    ]
]:
    """Modify folder

     Modifiy folder with the given *folderId*.

    Args:
        project_id (int):
        folder_id (int):
        json_body (ApiProjectFolderPatchOperation): Represents data required to execute folder-
            modify operation.
            There are multiple folder modify operations supported - see
            ApiProjectFolderPatchOperationType.
            Depending on the type the actual properties can differ. See subclasses for details.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ApiArgumentError, ApiBackendNotAvailableError, ApiForbiddenError, ApiInternalError, ApiLongOperationOfBoolean, ApiNotFoundError, ApiUnauthorizedError]]
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            folder_id=folder_id,
            client=client,
            json_body=json_body,
        )
    ).parsed
