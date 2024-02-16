from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_argument_error import ApiArgumentError
from ...models.api_backend_not_available_error import ApiBackendNotAvailableError
from ...models.api_internal_error import ApiInternalError
from ...models.api_unauthorized_error import ApiUnauthorizedError
from ...models.api_user_new import ApiUserNew
from ...models.api_user_new_reponse import ApiUserNewReponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: AuthenticatedClient,
    json_body: ApiUserNew,
    send_notification: Union[Unset, None, bool] = True,
) -> Dict[str, Any]:
    url = "{}/api/System/User".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["sendNotification"] = send_notification

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    json_json_body = json_body.to_dict()

    return {
        "method": "post",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "json": json_json_body,
        "params": params,
    }


def _parse_response(
    *, client: Client, response: httpx.Response
) -> Optional[
    Union[ApiArgumentError, ApiBackendNotAvailableError, ApiInternalError, ApiUnauthorizedError, ApiUserNewReponse]
]:
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = ApiArgumentError.from_dict(response.json())

        return response_400
    if response.status_code == HTTPStatus.OK:
        response_200 = ApiUserNewReponse.from_dict(response.json())

        return response_200
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
) -> Response[
    Union[ApiArgumentError, ApiBackendNotAvailableError, ApiInternalError, ApiUnauthorizedError, ApiUserNewReponse]
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
    json_body: ApiUserNew,
    send_notification: Union[Unset, None, bool] = True,
) -> Response[
    Union[ApiArgumentError, ApiBackendNotAvailableError, ApiInternalError, ApiUnauthorizedError, ApiUserNewReponse]
]:
    """Create user

     Create a new user with the given data.

    Args:
        send_notification (Union[Unset, None, bool]):  Default: True.
        json_body (ApiUserNew): Represents the necessary information to create a user.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ApiArgumentError, ApiBackendNotAvailableError, ApiInternalError, ApiUnauthorizedError, ApiUserNewReponse]]
    """

    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
        send_notification=send_notification,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    json_body: ApiUserNew,
    send_notification: Union[Unset, None, bool] = True,
) -> Optional[
    Union[ApiArgumentError, ApiBackendNotAvailableError, ApiInternalError, ApiUnauthorizedError, ApiUserNewReponse]
]:
    """Create user

     Create a new user with the given data.

    Args:
        send_notification (Union[Unset, None, bool]):  Default: True.
        json_body (ApiUserNew): Represents the necessary information to create a user.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ApiArgumentError, ApiBackendNotAvailableError, ApiInternalError, ApiUnauthorizedError, ApiUserNewReponse]]
    """

    return sync_detailed(
        client=client,
        json_body=json_body,
        send_notification=send_notification,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    json_body: ApiUserNew,
    send_notification: Union[Unset, None, bool] = True,
) -> Response[
    Union[ApiArgumentError, ApiBackendNotAvailableError, ApiInternalError, ApiUnauthorizedError, ApiUserNewReponse]
]:
    """Create user

     Create a new user with the given data.

    Args:
        send_notification (Union[Unset, None, bool]):  Default: True.
        json_body (ApiUserNew): Represents the necessary information to create a user.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ApiArgumentError, ApiBackendNotAvailableError, ApiInternalError, ApiUnauthorizedError, ApiUserNewReponse]]
    """

    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
        send_notification=send_notification,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    json_body: ApiUserNew,
    send_notification: Union[Unset, None, bool] = True,
) -> Optional[
    Union[ApiArgumentError, ApiBackendNotAvailableError, ApiInternalError, ApiUnauthorizedError, ApiUserNewReponse]
]:
    """Create user

     Create a new user with the given data.

    Args:
        send_notification (Union[Unset, None, bool]):  Default: True.
        json_body (ApiUserNew): Represents the necessary information to create a user.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ApiArgumentError, ApiBackendNotAvailableError, ApiInternalError, ApiUnauthorizedError, ApiUserNewReponse]]
    """

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
            send_notification=send_notification,
        )
    ).parsed
