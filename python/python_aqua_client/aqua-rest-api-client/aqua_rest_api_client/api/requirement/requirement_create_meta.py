from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_argument_error import ApiArgumentError
from ...models.api_backend_not_available_error import ApiBackendNotAvailableError
from ...models.api_forbidden_error import ApiForbiddenError
from ...models.api_internal_error import ApiInternalError
from ...models.api_item_create_meta import ApiItemCreateMeta
from ...models.api_unauthorized_error import ApiUnauthorizedError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: AuthenticatedClient,
    project_id: int,
    folder_id: int,
    status_to: Union[Unset, None, int] = UNSET,
) -> Dict[str, Any]:
    url = "{}/api/Requirement/CreateMeta".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["projectId"] = project_id

    params["folderId"] = folder_id

    params["statusTo"] = status_to

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
        ApiArgumentError,
        ApiBackendNotAvailableError,
        ApiForbiddenError,
        ApiInternalError,
        ApiItemCreateMeta,
        ApiUnauthorizedError,
    ]
]:
    if response.status_code == HTTPStatus.OK:
        response_200 = ApiItemCreateMeta.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = ApiArgumentError.from_dict(response.json())

        return response_400
    if response.status_code == HTTPStatus.FORBIDDEN:
        response_403 = ApiForbiddenError.from_dict(response.json())

        return response_403
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
        ApiItemCreateMeta,
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
    *,
    client: AuthenticatedClient,
    project_id: int,
    folder_id: int,
    status_to: Union[Unset, None, int] = UNSET,
) -> Response[
    Union[
        ApiArgumentError,
        ApiBackendNotAvailableError,
        ApiForbiddenError,
        ApiInternalError,
        ApiItemCreateMeta,
        ApiUnauthorizedError,
    ]
]:
    """Get fields metadata

     Get a basic information on the fields of a new requirement created in given project and folder.
                The information contains details about available fields and their characteristics.

    Args:
        project_id (int):
        folder_id (int):
        status_to (Union[Unset, None, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ApiArgumentError, ApiBackendNotAvailableError, ApiForbiddenError, ApiInternalError, ApiItemCreateMeta, ApiUnauthorizedError]]
    """

    kwargs = _get_kwargs(
        client=client,
        project_id=project_id,
        folder_id=folder_id,
        status_to=status_to,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    project_id: int,
    folder_id: int,
    status_to: Union[Unset, None, int] = UNSET,
) -> Optional[
    Union[
        ApiArgumentError,
        ApiBackendNotAvailableError,
        ApiForbiddenError,
        ApiInternalError,
        ApiItemCreateMeta,
        ApiUnauthorizedError,
    ]
]:
    """Get fields metadata

     Get a basic information on the fields of a new requirement created in given project and folder.
                The information contains details about available fields and their characteristics.

    Args:
        project_id (int):
        folder_id (int):
        status_to (Union[Unset, None, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ApiArgumentError, ApiBackendNotAvailableError, ApiForbiddenError, ApiInternalError, ApiItemCreateMeta, ApiUnauthorizedError]]
    """

    return sync_detailed(
        client=client,
        project_id=project_id,
        folder_id=folder_id,
        status_to=status_to,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    project_id: int,
    folder_id: int,
    status_to: Union[Unset, None, int] = UNSET,
) -> Response[
    Union[
        ApiArgumentError,
        ApiBackendNotAvailableError,
        ApiForbiddenError,
        ApiInternalError,
        ApiItemCreateMeta,
        ApiUnauthorizedError,
    ]
]:
    """Get fields metadata

     Get a basic information on the fields of a new requirement created in given project and folder.
                The information contains details about available fields and their characteristics.

    Args:
        project_id (int):
        folder_id (int):
        status_to (Union[Unset, None, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ApiArgumentError, ApiBackendNotAvailableError, ApiForbiddenError, ApiInternalError, ApiItemCreateMeta, ApiUnauthorizedError]]
    """

    kwargs = _get_kwargs(
        client=client,
        project_id=project_id,
        folder_id=folder_id,
        status_to=status_to,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    project_id: int,
    folder_id: int,
    status_to: Union[Unset, None, int] = UNSET,
) -> Optional[
    Union[
        ApiArgumentError,
        ApiBackendNotAvailableError,
        ApiForbiddenError,
        ApiInternalError,
        ApiItemCreateMeta,
        ApiUnauthorizedError,
    ]
]:
    """Get fields metadata

     Get a basic information on the fields of a new requirement created in given project and folder.
                The information contains details about available fields and their characteristics.

    Args:
        project_id (int):
        folder_id (int):
        status_to (Union[Unset, None, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ApiArgumentError, ApiBackendNotAvailableError, ApiForbiddenError, ApiInternalError, ApiItemCreateMeta, ApiUnauthorizedError]]
    """

    return (
        await asyncio_detailed(
            client=client,
            project_id=project_id,
            folder_id=folder_id,
            status_to=status_to,
        )
    ).parsed
