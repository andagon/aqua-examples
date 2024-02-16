from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_backend_not_available_error import ApiBackendNotAvailableError
from ...models.api_forbidden_error import ApiForbiddenError
from ...models.api_internal_error import ApiInternalError
from ...models.api_not_found_error import ApiNotFoundError
from ...models.api_sprint import ApiSprint
from ...models.api_sprints_include import ApiSprintsInclude
from ...models.api_unauthorized_error import ApiUnauthorizedError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: int,
    *,
    client: AuthenticatedClient,
    include_sprints: Union[Unset, None, ApiSprintsInclude] = ApiSprintsInclude.ALL,
) -> Dict[str, Any]:
    url = "{}/api/Project/{id}/Sprint".format(client.base_url, id=id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    json_include_sprints: Union[Unset, None, str] = UNSET
    if not isinstance(include_sprints, Unset):
        json_include_sprints = include_sprints.value if include_sprints else None

    params["includeSprints"] = json_include_sprints

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
        List["ApiSprint"],
    ]
]:
    if response.status_code == HTTPStatus.OK:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = ApiSprint.from_dict(response_200_item_data)

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
        List["ApiSprint"],
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
    include_sprints: Union[Unset, None, ApiSprintsInclude] = ApiSprintsInclude.ALL,
) -> Response[
    Union[
        ApiBackendNotAvailableError,
        ApiForbiddenError,
        ApiInternalError,
        ApiNotFoundError,
        ApiUnauthorizedError,
        List["ApiSprint"],
    ]
]:
    """Get sprints as list

     Get sprints for the project with given id, sprint statistics are not included.

    Args:
        id (int):
        include_sprints (Union[Unset, None, ApiSprintsInclude]):
            This enum has the following values:
              - `Active`
              - `All`
              - `Inactive`
             Default: ApiSprintsInclude.ALL.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ApiBackendNotAvailableError, ApiForbiddenError, ApiInternalError, ApiNotFoundError, ApiUnauthorizedError, List['ApiSprint']]]
    """

    kwargs = _get_kwargs(
        id=id,
        client=client,
        include_sprints=include_sprints,
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
    include_sprints: Union[Unset, None, ApiSprintsInclude] = ApiSprintsInclude.ALL,
) -> Optional[
    Union[
        ApiBackendNotAvailableError,
        ApiForbiddenError,
        ApiInternalError,
        ApiNotFoundError,
        ApiUnauthorizedError,
        List["ApiSprint"],
    ]
]:
    """Get sprints as list

     Get sprints for the project with given id, sprint statistics are not included.

    Args:
        id (int):
        include_sprints (Union[Unset, None, ApiSprintsInclude]):
            This enum has the following values:
              - `Active`
              - `All`
              - `Inactive`
             Default: ApiSprintsInclude.ALL.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ApiBackendNotAvailableError, ApiForbiddenError, ApiInternalError, ApiNotFoundError, ApiUnauthorizedError, List['ApiSprint']]]
    """

    return sync_detailed(
        id=id,
        client=client,
        include_sprints=include_sprints,
    ).parsed


async def asyncio_detailed(
    id: int,
    *,
    client: AuthenticatedClient,
    include_sprints: Union[Unset, None, ApiSprintsInclude] = ApiSprintsInclude.ALL,
) -> Response[
    Union[
        ApiBackendNotAvailableError,
        ApiForbiddenError,
        ApiInternalError,
        ApiNotFoundError,
        ApiUnauthorizedError,
        List["ApiSprint"],
    ]
]:
    """Get sprints as list

     Get sprints for the project with given id, sprint statistics are not included.

    Args:
        id (int):
        include_sprints (Union[Unset, None, ApiSprintsInclude]):
            This enum has the following values:
              - `Active`
              - `All`
              - `Inactive`
             Default: ApiSprintsInclude.ALL.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ApiBackendNotAvailableError, ApiForbiddenError, ApiInternalError, ApiNotFoundError, ApiUnauthorizedError, List['ApiSprint']]]
    """

    kwargs = _get_kwargs(
        id=id,
        client=client,
        include_sprints=include_sprints,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: int,
    *,
    client: AuthenticatedClient,
    include_sprints: Union[Unset, None, ApiSprintsInclude] = ApiSprintsInclude.ALL,
) -> Optional[
    Union[
        ApiBackendNotAvailableError,
        ApiForbiddenError,
        ApiInternalError,
        ApiNotFoundError,
        ApiUnauthorizedError,
        List["ApiSprint"],
    ]
]:
    """Get sprints as list

     Get sprints for the project with given id, sprint statistics are not included.

    Args:
        id (int):
        include_sprints (Union[Unset, None, ApiSprintsInclude]):
            This enum has the following values:
              - `Active`
              - `All`
              - `Inactive`
             Default: ApiSprintsInclude.ALL.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ApiBackendNotAvailableError, ApiForbiddenError, ApiInternalError, ApiNotFoundError, ApiUnauthorizedError, List['ApiSprint']]]
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            include_sprints=include_sprints,
        )
    ).parsed
