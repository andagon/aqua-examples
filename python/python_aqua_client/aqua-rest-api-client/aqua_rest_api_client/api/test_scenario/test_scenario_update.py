from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_argument_error import ApiArgumentError
from ...models.api_backend_not_available_error import ApiBackendNotAvailableError
from ...models.api_forbidden_error import ApiForbiddenError
from ...models.api_internal_error import ApiInternalError
from ...models.api_item_update_with_test_jobs import ApiItemUpdateWithTestJobs
from ...models.api_not_found_error import ApiNotFoundError
from ...models.api_unauthorized_error import ApiUnauthorizedError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: int,
    *,
    client: AuthenticatedClient,
    json_body: ApiItemUpdateWithTestJobs,
    explicit_lock: Union[Unset, None, bool] = False,
    apply_default_values: Union[Unset, None, bool] = True,
) -> Dict[str, Any]:
    url = "{}/api/TestScenario/{id}".format(client.base_url, id=id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["explicitLock"] = explicit_lock

    params["applyDefaultValues"] = apply_default_values

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    json_json_body = json_body.to_dict()

    return {
        "method": "put",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "json": json_json_body,
        "params": params,
    }


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[
    Union[
        Any,
        ApiArgumentError,
        ApiBackendNotAvailableError,
        ApiForbiddenError,
        ApiInternalError,
        ApiNotFoundError,
        ApiUnauthorizedError,
    ]
]:
    if response.status_code == HTTPStatus.NO_CONTENT:
        response_204 = cast(Any, None)
        return response_204
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
        Any,
        ApiArgumentError,
        ApiBackendNotAvailableError,
        ApiForbiddenError,
        ApiInternalError,
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
    id: int,
    *,
    client: AuthenticatedClient,
    json_body: ApiItemUpdateWithTestJobs,
    explicit_lock: Union[Unset, None, bool] = False,
    apply_default_values: Union[Unset, None, bool] = True,
) -> Response[
    Union[
        Any,
        ApiArgumentError,
        ApiBackendNotAvailableError,
        ApiForbiddenError,
        ApiInternalError,
        ApiNotFoundError,
        ApiUnauthorizedError,
    ]
]:
    """Update test scenario

     Update the test scenario with the specified *id*. The changes
                to perform are provided in the *ApiItemUpdate* object.

    Args:
        id (int):
        explicit_lock (Union[Unset, None, bool]):
        apply_default_values (Union[Unset, None, bool]):  Default: True.
        json_body (ApiItemUpdateWithTestJobs):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ApiArgumentError, ApiBackendNotAvailableError, ApiForbiddenError, ApiInternalError, ApiNotFoundError, ApiUnauthorizedError]]
    """

    kwargs = _get_kwargs(
        id=id,
        client=client,
        json_body=json_body,
        explicit_lock=explicit_lock,
        apply_default_values=apply_default_values,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: int,
    *,
    client: AuthenticatedClient,
    json_body: ApiItemUpdateWithTestJobs,
    explicit_lock: Union[Unset, None, bool] = False,
    apply_default_values: Union[Unset, None, bool] = True,
) -> Optional[
    Union[
        Any,
        ApiArgumentError,
        ApiBackendNotAvailableError,
        ApiForbiddenError,
        ApiInternalError,
        ApiNotFoundError,
        ApiUnauthorizedError,
    ]
]:
    """Update test scenario

     Update the test scenario with the specified *id*. The changes
                to perform are provided in the *ApiItemUpdate* object.

    Args:
        id (int):
        explicit_lock (Union[Unset, None, bool]):
        apply_default_values (Union[Unset, None, bool]):  Default: True.
        json_body (ApiItemUpdateWithTestJobs):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ApiArgumentError, ApiBackendNotAvailableError, ApiForbiddenError, ApiInternalError, ApiNotFoundError, ApiUnauthorizedError]]
    """

    return sync_detailed(
        id=id,
        client=client,
        json_body=json_body,
        explicit_lock=explicit_lock,
        apply_default_values=apply_default_values,
    ).parsed


async def asyncio_detailed(
    id: int,
    *,
    client: AuthenticatedClient,
    json_body: ApiItemUpdateWithTestJobs,
    explicit_lock: Union[Unset, None, bool] = False,
    apply_default_values: Union[Unset, None, bool] = True,
) -> Response[
    Union[
        Any,
        ApiArgumentError,
        ApiBackendNotAvailableError,
        ApiForbiddenError,
        ApiInternalError,
        ApiNotFoundError,
        ApiUnauthorizedError,
    ]
]:
    """Update test scenario

     Update the test scenario with the specified *id*. The changes
                to perform are provided in the *ApiItemUpdate* object.

    Args:
        id (int):
        explicit_lock (Union[Unset, None, bool]):
        apply_default_values (Union[Unset, None, bool]):  Default: True.
        json_body (ApiItemUpdateWithTestJobs):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ApiArgumentError, ApiBackendNotAvailableError, ApiForbiddenError, ApiInternalError, ApiNotFoundError, ApiUnauthorizedError]]
    """

    kwargs = _get_kwargs(
        id=id,
        client=client,
        json_body=json_body,
        explicit_lock=explicit_lock,
        apply_default_values=apply_default_values,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: int,
    *,
    client: AuthenticatedClient,
    json_body: ApiItemUpdateWithTestJobs,
    explicit_lock: Union[Unset, None, bool] = False,
    apply_default_values: Union[Unset, None, bool] = True,
) -> Optional[
    Union[
        Any,
        ApiArgumentError,
        ApiBackendNotAvailableError,
        ApiForbiddenError,
        ApiInternalError,
        ApiNotFoundError,
        ApiUnauthorizedError,
    ]
]:
    """Update test scenario

     Update the test scenario with the specified *id*. The changes
                to perform are provided in the *ApiItemUpdate* object.

    Args:
        id (int):
        explicit_lock (Union[Unset, None, bool]):
        apply_default_values (Union[Unset, None, bool]):  Default: True.
        json_body (ApiItemUpdateWithTestJobs):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ApiArgumentError, ApiBackendNotAvailableError, ApiForbiddenError, ApiInternalError, ApiNotFoundError, ApiUnauthorizedError]]
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            json_body=json_body,
            explicit_lock=explicit_lock,
            apply_default_values=apply_default_values,
        )
    ).parsed
