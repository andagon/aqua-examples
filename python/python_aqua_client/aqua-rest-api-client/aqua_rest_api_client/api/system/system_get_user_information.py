from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_backend_not_available_error import ApiBackendNotAvailableError
from ...models.api_internal_error import ApiInternalError
from ...models.api_not_found_error import ApiNotFoundError
from ...models.api_unauthorized_error import ApiUnauthorizedError
from ...models.api_user import ApiUser
from ...types import UNSET, Response, Unset


def _get_kwargs(
    user_id: int,
    *,
    client: AuthenticatedClient,
    include_projects: Union[Unset, None, bool] = False,
    include_licenses: Union[Unset, None, bool] = False,
) -> Dict[str, Any]:
    url = "{}/api/System/User/{userId}".format(client.base_url, userId=user_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["includeProjects"] = include_projects

    params["includeLicenses"] = include_licenses

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(
    *, client: Client, response: httpx.Response
) -> Optional[Union[ApiBackendNotAvailableError, ApiInternalError, ApiNotFoundError, ApiUnauthorizedError, ApiUser]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = ApiUser.from_dict(response.json())

        return response_200
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


def _build_response(
    *, client: Client, response: httpx.Response
) -> Response[Union[ApiBackendNotAvailableError, ApiInternalError, ApiNotFoundError, ApiUnauthorizedError, ApiUser]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    user_id: int,
    *,
    client: AuthenticatedClient,
    include_projects: Union[Unset, None, bool] = False,
    include_licenses: Union[Unset, None, bool] = False,
) -> Response[Union[ApiBackendNotAvailableError, ApiInternalError, ApiNotFoundError, ApiUnauthorizedError, ApiUser]]:
    """Get user

     Get the user with the specified *userId*.

    Args:
        user_id (int):
        include_projects (Union[Unset, None, bool]):
        include_licenses (Union[Unset, None, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ApiBackendNotAvailableError, ApiInternalError, ApiNotFoundError, ApiUnauthorizedError, ApiUser]]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        client=client,
        include_projects=include_projects,
        include_licenses=include_licenses,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    user_id: int,
    *,
    client: AuthenticatedClient,
    include_projects: Union[Unset, None, bool] = False,
    include_licenses: Union[Unset, None, bool] = False,
) -> Optional[Union[ApiBackendNotAvailableError, ApiInternalError, ApiNotFoundError, ApiUnauthorizedError, ApiUser]]:
    """Get user

     Get the user with the specified *userId*.

    Args:
        user_id (int):
        include_projects (Union[Unset, None, bool]):
        include_licenses (Union[Unset, None, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ApiBackendNotAvailableError, ApiInternalError, ApiNotFoundError, ApiUnauthorizedError, ApiUser]]
    """

    return sync_detailed(
        user_id=user_id,
        client=client,
        include_projects=include_projects,
        include_licenses=include_licenses,
    ).parsed


async def asyncio_detailed(
    user_id: int,
    *,
    client: AuthenticatedClient,
    include_projects: Union[Unset, None, bool] = False,
    include_licenses: Union[Unset, None, bool] = False,
) -> Response[Union[ApiBackendNotAvailableError, ApiInternalError, ApiNotFoundError, ApiUnauthorizedError, ApiUser]]:
    """Get user

     Get the user with the specified *userId*.

    Args:
        user_id (int):
        include_projects (Union[Unset, None, bool]):
        include_licenses (Union[Unset, None, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ApiBackendNotAvailableError, ApiInternalError, ApiNotFoundError, ApiUnauthorizedError, ApiUser]]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        client=client,
        include_projects=include_projects,
        include_licenses=include_licenses,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    user_id: int,
    *,
    client: AuthenticatedClient,
    include_projects: Union[Unset, None, bool] = False,
    include_licenses: Union[Unset, None, bool] = False,
) -> Optional[Union[ApiBackendNotAvailableError, ApiInternalError, ApiNotFoundError, ApiUnauthorizedError, ApiUser]]:
    """Get user

     Get the user with the specified *userId*.

    Args:
        user_id (int):
        include_projects (Union[Unset, None, bool]):
        include_licenses (Union[Unset, None, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ApiBackendNotAvailableError, ApiInternalError, ApiNotFoundError, ApiUnauthorizedError, ApiUser]]
    """

    return (
        await asyncio_detailed(
            user_id=user_id,
            client=client,
            include_projects=include_projects,
            include_licenses=include_licenses,
        )
    ).parsed
