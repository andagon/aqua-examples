from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_backend_not_available_error import ApiBackendNotAvailableError
from ...models.api_forbidden_error import ApiForbiddenError
from ...models.api_internal_error import ApiInternalError
from ...models.api_not_found_error import ApiNotFoundError
from ...models.api_project_sub_folder import ApiProjectSubFolder
from ...models.api_unauthorized_error import ApiUnauthorizedError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    project_id: int,
    folder_id: int,
    *,
    client: AuthenticatedClient,
    include_permissions: Union[Unset, None, bool] = True,
    recursive: Union[Unset, None, bool] = False,
) -> Dict[str, Any]:
    url = "{}/api/Project/{projectId}/Folder/{folderId}/Subfolder".format(
        client.base_url, projectId=project_id, folderId=folder_id
    )

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["includePermissions"] = include_permissions

    params["recursive"] = recursive

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[
    Union[
        ApiBackendNotAvailableError,
        ApiForbiddenError,
        ApiInternalError,
        ApiNotFoundError,
        ApiUnauthorizedError,
        List["ApiProjectSubFolder"],
    ]
]:
    if response.status_code == HTTPStatus.OK:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = ApiProjectSubFolder.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
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
        ApiBackendNotAvailableError,
        ApiForbiddenError,
        ApiInternalError,
        ApiNotFoundError,
        ApiUnauthorizedError,
        List["ApiProjectSubFolder"],
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
    include_permissions: Union[Unset, None, bool] = True,
    recursive: Union[Unset, None, bool] = False,
) -> Response[
    Union[
        ApiBackendNotAvailableError,
        ApiForbiddenError,
        ApiInternalError,
        ApiNotFoundError,
        ApiUnauthorizedError,
        List["ApiProjectSubFolder"],
    ]
]:
    """Get subfolders

     Get subfolders of a folder or load all subfolders including child subfolders.

    Args:
        project_id (int):
        folder_id (int):
        include_permissions (Union[Unset, None, bool]):  Default: True.
        recursive (Union[Unset, None, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ApiBackendNotAvailableError, ApiForbiddenError, ApiInternalError, ApiNotFoundError, ApiUnauthorizedError, List['ApiProjectSubFolder']]]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        folder_id=folder_id,
        client=client,
        include_permissions=include_permissions,
        recursive=recursive,
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
    include_permissions: Union[Unset, None, bool] = True,
    recursive: Union[Unset, None, bool] = False,
) -> Optional[
    Union[
        ApiBackendNotAvailableError,
        ApiForbiddenError,
        ApiInternalError,
        ApiNotFoundError,
        ApiUnauthorizedError,
        List["ApiProjectSubFolder"],
    ]
]:
    """Get subfolders

     Get subfolders of a folder or load all subfolders including child subfolders.

    Args:
        project_id (int):
        folder_id (int):
        include_permissions (Union[Unset, None, bool]):  Default: True.
        recursive (Union[Unset, None, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ApiBackendNotAvailableError, ApiForbiddenError, ApiInternalError, ApiNotFoundError, ApiUnauthorizedError, List['ApiProjectSubFolder']]]
    """

    return sync_detailed(
        project_id=project_id,
        folder_id=folder_id,
        client=client,
        include_permissions=include_permissions,
        recursive=recursive,
    ).parsed


async def asyncio_detailed(
    project_id: int,
    folder_id: int,
    *,
    client: AuthenticatedClient,
    include_permissions: Union[Unset, None, bool] = True,
    recursive: Union[Unset, None, bool] = False,
) -> Response[
    Union[
        ApiBackendNotAvailableError,
        ApiForbiddenError,
        ApiInternalError,
        ApiNotFoundError,
        ApiUnauthorizedError,
        List["ApiProjectSubFolder"],
    ]
]:
    """Get subfolders

     Get subfolders of a folder or load all subfolders including child subfolders.

    Args:
        project_id (int):
        folder_id (int):
        include_permissions (Union[Unset, None, bool]):  Default: True.
        recursive (Union[Unset, None, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ApiBackendNotAvailableError, ApiForbiddenError, ApiInternalError, ApiNotFoundError, ApiUnauthorizedError, List['ApiProjectSubFolder']]]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        folder_id=folder_id,
        client=client,
        include_permissions=include_permissions,
        recursive=recursive,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_id: int,
    folder_id: int,
    *,
    client: AuthenticatedClient,
    include_permissions: Union[Unset, None, bool] = True,
    recursive: Union[Unset, None, bool] = False,
) -> Optional[
    Union[
        ApiBackendNotAvailableError,
        ApiForbiddenError,
        ApiInternalError,
        ApiNotFoundError,
        ApiUnauthorizedError,
        List["ApiProjectSubFolder"],
    ]
]:
    """Get subfolders

     Get subfolders of a folder or load all subfolders including child subfolders.

    Args:
        project_id (int):
        folder_id (int):
        include_permissions (Union[Unset, None, bool]):  Default: True.
        recursive (Union[Unset, None, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ApiBackendNotAvailableError, ApiForbiddenError, ApiInternalError, ApiNotFoundError, ApiUnauthorizedError, List['ApiProjectSubFolder']]]
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            folder_id=folder_id,
            client=client,
            include_permissions=include_permissions,
            recursive=recursive,
        )
    ).parsed
