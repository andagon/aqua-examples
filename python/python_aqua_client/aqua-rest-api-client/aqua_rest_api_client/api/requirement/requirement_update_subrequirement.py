from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_argument_error import ApiArgumentError
from ...models.api_backend_not_available_error import ApiBackendNotAvailableError
from ...models.api_forbidden_error import ApiForbiddenError
from ...models.api_internal_error import ApiInternalError
from ...models.api_not_found_error import ApiNotFoundError
from ...models.api_subrequirement import ApiSubrequirement
from ...models.api_subrequirement_update import ApiSubrequirementUpdate
from ...models.api_unauthorized_error import ApiUnauthorizedError
from ...types import Response


def _get_kwargs(
    id: int,
    subrequirement_id: int,
    *,
    client: AuthenticatedClient,
    json_body: ApiSubrequirementUpdate,
) -> Dict[str, Any]:
    url = "{}/api/Requirement/{id}/Subrequirement/{subrequirementId}".format(
        client.base_url, id=id, subrequirementId=subrequirement_id
    )

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_json_body = json_body.to_dict()

    return {
        "method": "put",
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
        ApiNotFoundError,
        ApiSubrequirement,
        ApiUnauthorizedError,
    ]
]:
    if response.status_code == HTTPStatus.OK:
        response_200 = ApiSubrequirement.from_dict(response.json())

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
        ApiNotFoundError,
        ApiSubrequirement,
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
    subrequirement_id: int,
    *,
    client: AuthenticatedClient,
    json_body: ApiSubrequirementUpdate,
) -> Response[
    Union[
        ApiArgumentError,
        ApiBackendNotAvailableError,
        ApiForbiddenError,
        ApiInternalError,
        ApiNotFoundError,
        ApiSubrequirement,
        ApiUnauthorizedError,
    ]
]:
    """Update subrequirement

     Update the subrequirement with *subrequirementId* in the
                requirement with *id*. Currently, this call only allows to change
                the position of the subrequirement in the parent requirement. You can only
                change first-level subrequirements. To change the parent of a subrequirement,
                you can just create the subrequirement at the new parent. The create will take
                care of detaching the subrequirement from its old parent.

    Args:
        id (int):
        subrequirement_id (int):
        json_body (ApiSubrequirementUpdate): The information to update in a given sub requirement.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ApiArgumentError, ApiBackendNotAvailableError, ApiForbiddenError, ApiInternalError, ApiNotFoundError, ApiSubrequirement, ApiUnauthorizedError]]
    """

    kwargs = _get_kwargs(
        id=id,
        subrequirement_id=subrequirement_id,
        client=client,
        json_body=json_body,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: int,
    subrequirement_id: int,
    *,
    client: AuthenticatedClient,
    json_body: ApiSubrequirementUpdate,
) -> Optional[
    Union[
        ApiArgumentError,
        ApiBackendNotAvailableError,
        ApiForbiddenError,
        ApiInternalError,
        ApiNotFoundError,
        ApiSubrequirement,
        ApiUnauthorizedError,
    ]
]:
    """Update subrequirement

     Update the subrequirement with *subrequirementId* in the
                requirement with *id*. Currently, this call only allows to change
                the position of the subrequirement in the parent requirement. You can only
                change first-level subrequirements. To change the parent of a subrequirement,
                you can just create the subrequirement at the new parent. The create will take
                care of detaching the subrequirement from its old parent.

    Args:
        id (int):
        subrequirement_id (int):
        json_body (ApiSubrequirementUpdate): The information to update in a given sub requirement.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ApiArgumentError, ApiBackendNotAvailableError, ApiForbiddenError, ApiInternalError, ApiNotFoundError, ApiSubrequirement, ApiUnauthorizedError]]
    """

    return sync_detailed(
        id=id,
        subrequirement_id=subrequirement_id,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    id: int,
    subrequirement_id: int,
    *,
    client: AuthenticatedClient,
    json_body: ApiSubrequirementUpdate,
) -> Response[
    Union[
        ApiArgumentError,
        ApiBackendNotAvailableError,
        ApiForbiddenError,
        ApiInternalError,
        ApiNotFoundError,
        ApiSubrequirement,
        ApiUnauthorizedError,
    ]
]:
    """Update subrequirement

     Update the subrequirement with *subrequirementId* in the
                requirement with *id*. Currently, this call only allows to change
                the position of the subrequirement in the parent requirement. You can only
                change first-level subrequirements. To change the parent of a subrequirement,
                you can just create the subrequirement at the new parent. The create will take
                care of detaching the subrequirement from its old parent.

    Args:
        id (int):
        subrequirement_id (int):
        json_body (ApiSubrequirementUpdate): The information to update in a given sub requirement.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ApiArgumentError, ApiBackendNotAvailableError, ApiForbiddenError, ApiInternalError, ApiNotFoundError, ApiSubrequirement, ApiUnauthorizedError]]
    """

    kwargs = _get_kwargs(
        id=id,
        subrequirement_id=subrequirement_id,
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: int,
    subrequirement_id: int,
    *,
    client: AuthenticatedClient,
    json_body: ApiSubrequirementUpdate,
) -> Optional[
    Union[
        ApiArgumentError,
        ApiBackendNotAvailableError,
        ApiForbiddenError,
        ApiInternalError,
        ApiNotFoundError,
        ApiSubrequirement,
        ApiUnauthorizedError,
    ]
]:
    """Update subrequirement

     Update the subrequirement with *subrequirementId* in the
                requirement with *id*. Currently, this call only allows to change
                the position of the subrequirement in the parent requirement. You can only
                change first-level subrequirements. To change the parent of a subrequirement,
                you can just create the subrequirement at the new parent. The create will take
                care of detaching the subrequirement from its old parent.

    Args:
        id (int):
        subrequirement_id (int):
        json_body (ApiSubrequirementUpdate): The information to update in a given sub requirement.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ApiArgumentError, ApiBackendNotAvailableError, ApiForbiddenError, ApiInternalError, ApiNotFoundError, ApiSubrequirement, ApiUnauthorizedError]]
    """

    return (
        await asyncio_detailed(
            id=id,
            subrequirement_id=subrequirement_id,
            client=client,
            json_body=json_body,
        )
    ).parsed
