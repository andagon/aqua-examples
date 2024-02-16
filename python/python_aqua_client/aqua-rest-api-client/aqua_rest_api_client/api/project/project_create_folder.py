from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_argument_error import ApiArgumentError
from ...models.api_backend_not_available_error import ApiBackendNotAvailableError
from ...models.api_forbidden_error import ApiForbiddenError
from ...models.api_internal_error import ApiInternalError
from ...models.api_long_operation_of_integer import ApiLongOperationOfInteger
from ...models.api_not_found_error import ApiNotFoundError
from ...models.api_project_folder_create import ApiProjectFolderCreate
from ...models.api_unauthorized_error import ApiUnauthorizedError
from ...types import Response


def _get_kwargs(
    project_id: int,
    folder_id: int,
    *,
    client: AuthenticatedClient,
    json_body: ApiProjectFolderCreate,
) -> Dict[str, Any]:
    url = "{}/api/Project/{projectId}/Folder/{folderId}/Subfolder".format(
        client.base_url, projectId=project_id, folderId=folder_id
    )

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_json_body = json_body.to_dict()

    return {
        "method": "post",
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
        ApiLongOperationOfInteger,
        ApiNotFoundError,
        ApiUnauthorizedError,
    ]
]:
    if response.status_code == HTTPStatus.OK:
        response_200 = ApiLongOperationOfInteger.from_dict(response.json())

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
        ApiLongOperationOfInteger,
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
    json_body: ApiProjectFolderCreate,
) -> Response[
    Union[
        ApiArgumentError,
        ApiBackendNotAvailableError,
        ApiForbiddenError,
        ApiInternalError,
        ApiLongOperationOfInteger,
        ApiNotFoundError,
        ApiUnauthorizedError,
    ]
]:
    """Create folder

     Create a new folder in given location (use folderId=0 to create a folder directly in the project's
    root).
                If SourceFolder is provided then new folder is created as a copy of existing folder (all
    the items are copied as well), recursively.
                Currently folder can be copied in scope of one project only (cross-project copy is not
    supported).
                Note: folder names are unique in given level. If you try to create a duplicate the
    proper error will be returned.

    Args:
        project_id (int):
        folder_id (int):
        json_body (ApiProjectFolderCreate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ApiArgumentError, ApiBackendNotAvailableError, ApiForbiddenError, ApiInternalError, ApiLongOperationOfInteger, ApiNotFoundError, ApiUnauthorizedError]]
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
    json_body: ApiProjectFolderCreate,
) -> Optional[
    Union[
        ApiArgumentError,
        ApiBackendNotAvailableError,
        ApiForbiddenError,
        ApiInternalError,
        ApiLongOperationOfInteger,
        ApiNotFoundError,
        ApiUnauthorizedError,
    ]
]:
    """Create folder

     Create a new folder in given location (use folderId=0 to create a folder directly in the project's
    root).
                If SourceFolder is provided then new folder is created as a copy of existing folder (all
    the items are copied as well), recursively.
                Currently folder can be copied in scope of one project only (cross-project copy is not
    supported).
                Note: folder names are unique in given level. If you try to create a duplicate the
    proper error will be returned.

    Args:
        project_id (int):
        folder_id (int):
        json_body (ApiProjectFolderCreate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ApiArgumentError, ApiBackendNotAvailableError, ApiForbiddenError, ApiInternalError, ApiLongOperationOfInteger, ApiNotFoundError, ApiUnauthorizedError]]
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
    json_body: ApiProjectFolderCreate,
) -> Response[
    Union[
        ApiArgumentError,
        ApiBackendNotAvailableError,
        ApiForbiddenError,
        ApiInternalError,
        ApiLongOperationOfInteger,
        ApiNotFoundError,
        ApiUnauthorizedError,
    ]
]:
    """Create folder

     Create a new folder in given location (use folderId=0 to create a folder directly in the project's
    root).
                If SourceFolder is provided then new folder is created as a copy of existing folder (all
    the items are copied as well), recursively.
                Currently folder can be copied in scope of one project only (cross-project copy is not
    supported).
                Note: folder names are unique in given level. If you try to create a duplicate the
    proper error will be returned.

    Args:
        project_id (int):
        folder_id (int):
        json_body (ApiProjectFolderCreate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ApiArgumentError, ApiBackendNotAvailableError, ApiForbiddenError, ApiInternalError, ApiLongOperationOfInteger, ApiNotFoundError, ApiUnauthorizedError]]
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
    json_body: ApiProjectFolderCreate,
) -> Optional[
    Union[
        ApiArgumentError,
        ApiBackendNotAvailableError,
        ApiForbiddenError,
        ApiInternalError,
        ApiLongOperationOfInteger,
        ApiNotFoundError,
        ApiUnauthorizedError,
    ]
]:
    """Create folder

     Create a new folder in given location (use folderId=0 to create a folder directly in the project's
    root).
                If SourceFolder is provided then new folder is created as a copy of existing folder (all
    the items are copied as well), recursively.
                Currently folder can be copied in scope of one project only (cross-project copy is not
    supported).
                Note: folder names are unique in given level. If you try to create a duplicate the
    proper error will be returned.

    Args:
        project_id (int):
        folder_id (int):
        json_body (ApiProjectFolderCreate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ApiArgumentError, ApiBackendNotAvailableError, ApiForbiddenError, ApiInternalError, ApiLongOperationOfInteger, ApiNotFoundError, ApiUnauthorizedError]]
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            folder_id=folder_id,
            client=client,
            json_body=json_body,
        )
    ).parsed
