from http import HTTPStatus
from io import BytesIO
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_intial_type import ApiIntialType
from ...types import UNSET, File, Response, Unset


def _get_kwargs(
    user_id: int,
    *,
    client: AuthenticatedClient,
    initials: Union[Unset, None, ApiIntialType] = ApiIntialType.ALL,
) -> Dict[str, Any]:
    url = "{}/api/UserImage/{userId}/picture".format(client.base_url, userId=user_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    json_initials: Union[Unset, None, str] = UNSET
    if not isinstance(initials, Unset):
        json_initials = initials.value if initials else None

    params["initials"] = json_initials

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[Union[File, str]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = File(payload=BytesIO(response.content))

        return response_200
    if response.status_code == HTTPStatus.NOT_FOUND:
        response_404 = cast(str, response.text)
        return response_404
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        response_401 = cast(str, response.text)
        return response_401
    if response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR:
        response_500 = cast(str, response.text)
        return response_500
    if response.status_code == HTTPStatus.SERVICE_UNAVAILABLE:
        response_503 = cast(str, response.text)
        return response_503
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[Union[File, str]]:
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
    initials: Union[Unset, None, ApiIntialType] = ApiIntialType.ALL,
) -> Response[Union[File, str]]:
    """Get a user's profile pricture

     Get the profile picture for a particular user

    Args:
        user_id (int):
        initials (Union[Unset, None, ApiIntialType]): Identifies the type of the intial.
            This enum has the following values:
              - `All` Two letters as initials will be returned.
              - `Single` One letter as initial will be returned.
             Default: ApiIntialType.ALL.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[File, str]]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        client=client,
        initials=initials,
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
    initials: Union[Unset, None, ApiIntialType] = ApiIntialType.ALL,
) -> Optional[Union[File, str]]:
    """Get a user's profile pricture

     Get the profile picture for a particular user

    Args:
        user_id (int):
        initials (Union[Unset, None, ApiIntialType]): Identifies the type of the intial.
            This enum has the following values:
              - `All` Two letters as initials will be returned.
              - `Single` One letter as initial will be returned.
             Default: ApiIntialType.ALL.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[File, str]]
    """

    return sync_detailed(
        user_id=user_id,
        client=client,
        initials=initials,
    ).parsed


async def asyncio_detailed(
    user_id: int,
    *,
    client: AuthenticatedClient,
    initials: Union[Unset, None, ApiIntialType] = ApiIntialType.ALL,
) -> Response[Union[File, str]]:
    """Get a user's profile pricture

     Get the profile picture for a particular user

    Args:
        user_id (int):
        initials (Union[Unset, None, ApiIntialType]): Identifies the type of the intial.
            This enum has the following values:
              - `All` Two letters as initials will be returned.
              - `Single` One letter as initial will be returned.
             Default: ApiIntialType.ALL.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[File, str]]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        client=client,
        initials=initials,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    user_id: int,
    *,
    client: AuthenticatedClient,
    initials: Union[Unset, None, ApiIntialType] = ApiIntialType.ALL,
) -> Optional[Union[File, str]]:
    """Get a user's profile pricture

     Get the profile picture for a particular user

    Args:
        user_id (int):
        initials (Union[Unset, None, ApiIntialType]): Identifies the type of the intial.
            This enum has the following values:
              - `All` Two letters as initials will be returned.
              - `Single` One letter as initial will be returned.
             Default: ApiIntialType.ALL.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[File, str]]
    """

    return (
        await asyncio_detailed(
            user_id=user_id,
            client=client,
            initials=initials,
        )
    ).parsed
