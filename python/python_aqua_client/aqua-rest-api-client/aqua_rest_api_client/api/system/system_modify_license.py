from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_argument_error import ApiArgumentError
from ...models.api_backend_not_available_error import ApiBackendNotAvailableError
from ...models.api_internal_error import ApiInternalError
from ...models.api_not_found_error import ApiNotFoundError
from ...models.api_unauthorized_error import ApiUnauthorizedError
from ...models.api_user_license_assignment_patch_request import ApiUserLicenseAssignmentPatchRequest
from ...types import Response


def _get_kwargs(
    user_id: int,
    license_code: Optional[str],
    *,
    client: AuthenticatedClient,
    json_body: ApiUserLicenseAssignmentPatchRequest,
) -> Dict[str, Any]:
    url = "{}/api/System/User/{userId}/License/{licenseCode}".format(
        client.base_url, userId=user_id, licenseCode=license_code
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


def _parse_response(
    *, client: Client, response: httpx.Response
) -> Optional[
    Union[Any, ApiArgumentError, ApiBackendNotAvailableError, ApiInternalError, ApiNotFoundError, ApiUnauthorizedError]
]:
    if response.status_code == HTTPStatus.NO_CONTENT:
        response_204 = cast(Any, None)
        return response_204
    if response.status_code == HTTPStatus.NOT_FOUND:
        response_404 = ApiNotFoundError.from_dict(response.json())

        return response_404
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = ApiArgumentError.from_dict(response.json())

        return response_400
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
    Union[Any, ApiArgumentError, ApiBackendNotAvailableError, ApiInternalError, ApiNotFoundError, ApiUnauthorizedError]
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    user_id: int,
    license_code: Optional[str],
    *,
    client: AuthenticatedClient,
    json_body: ApiUserLicenseAssignmentPatchRequest,
) -> Response[
    Union[Any, ApiArgumentError, ApiBackendNotAvailableError, ApiInternalError, ApiNotFoundError, ApiUnauthorizedError]
]:
    """Modify license

     Modify license type for the user with the specified *userId*.

    Args:
        user_id (int):
        license_code (Optional[str]):
        json_body (ApiUserLicenseAssignmentPatchRequest): Represent the necessary information to
            change the license type.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ApiArgumentError, ApiBackendNotAvailableError, ApiInternalError, ApiNotFoundError, ApiUnauthorizedError]]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        license_code=license_code,
        client=client,
        json_body=json_body,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    user_id: int,
    license_code: Optional[str],
    *,
    client: AuthenticatedClient,
    json_body: ApiUserLicenseAssignmentPatchRequest,
) -> Optional[
    Union[Any, ApiArgumentError, ApiBackendNotAvailableError, ApiInternalError, ApiNotFoundError, ApiUnauthorizedError]
]:
    """Modify license

     Modify license type for the user with the specified *userId*.

    Args:
        user_id (int):
        license_code (Optional[str]):
        json_body (ApiUserLicenseAssignmentPatchRequest): Represent the necessary information to
            change the license type.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ApiArgumentError, ApiBackendNotAvailableError, ApiInternalError, ApiNotFoundError, ApiUnauthorizedError]]
    """

    return sync_detailed(
        user_id=user_id,
        license_code=license_code,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    user_id: int,
    license_code: Optional[str],
    *,
    client: AuthenticatedClient,
    json_body: ApiUserLicenseAssignmentPatchRequest,
) -> Response[
    Union[Any, ApiArgumentError, ApiBackendNotAvailableError, ApiInternalError, ApiNotFoundError, ApiUnauthorizedError]
]:
    """Modify license

     Modify license type for the user with the specified *userId*.

    Args:
        user_id (int):
        license_code (Optional[str]):
        json_body (ApiUserLicenseAssignmentPatchRequest): Represent the necessary information to
            change the license type.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ApiArgumentError, ApiBackendNotAvailableError, ApiInternalError, ApiNotFoundError, ApiUnauthorizedError]]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        license_code=license_code,
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    user_id: int,
    license_code: Optional[str],
    *,
    client: AuthenticatedClient,
    json_body: ApiUserLicenseAssignmentPatchRequest,
) -> Optional[
    Union[Any, ApiArgumentError, ApiBackendNotAvailableError, ApiInternalError, ApiNotFoundError, ApiUnauthorizedError]
]:
    """Modify license

     Modify license type for the user with the specified *userId*.

    Args:
        user_id (int):
        license_code (Optional[str]):
        json_body (ApiUserLicenseAssignmentPatchRequest): Represent the necessary information to
            change the license type.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ApiArgumentError, ApiBackendNotAvailableError, ApiInternalError, ApiNotFoundError, ApiUnauthorizedError]]
    """

    return (
        await asyncio_detailed(
            user_id=user_id,
            license_code=license_code,
            client=client,
            json_body=json_body,
        )
    ).parsed
