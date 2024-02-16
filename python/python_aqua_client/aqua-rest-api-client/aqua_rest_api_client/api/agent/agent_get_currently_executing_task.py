from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_backend_not_available_error import ApiBackendNotAvailableError
from ...models.api_currently_executed_step_info import ApiCurrentlyExecutedStepInfo
from ...models.api_internal_error import ApiInternalError
from ...models.api_unauthorized_error import ApiUnauthorizedError
from ...types import Response


def _get_kwargs(
    agent_id: int,
    *,
    client: AuthenticatedClient,
) -> Dict[str, Any]:
    url = "{}/api/Agent/{agentId}/CurrentlyExecuting".format(client.base_url, agentId=agent_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(
    *, client: Client, response: httpx.Response
) -> Optional[Union[ApiBackendNotAvailableError, ApiCurrentlyExecutedStepInfo, ApiInternalError, ApiUnauthorizedError]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = ApiCurrentlyExecutedStepInfo.from_dict(response.json())

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
) -> Response[Union[ApiBackendNotAvailableError, ApiCurrentlyExecutedStepInfo, ApiInternalError, ApiUnauthorizedError]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    agent_id: int,
    *,
    client: AuthenticatedClient,
) -> Response[Union[ApiBackendNotAvailableError, ApiCurrentlyExecutedStepInfo, ApiInternalError, ApiUnauthorizedError]]:
    """Get currently executing task

     Get the task which currently executed by the given agent.

    Args:
        agent_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ApiBackendNotAvailableError, ApiCurrentlyExecutedStepInfo, ApiInternalError, ApiUnauthorizedError]]
    """

    kwargs = _get_kwargs(
        agent_id=agent_id,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    agent_id: int,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[ApiBackendNotAvailableError, ApiCurrentlyExecutedStepInfo, ApiInternalError, ApiUnauthorizedError]]:
    """Get currently executing task

     Get the task which currently executed by the given agent.

    Args:
        agent_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ApiBackendNotAvailableError, ApiCurrentlyExecutedStepInfo, ApiInternalError, ApiUnauthorizedError]]
    """

    return sync_detailed(
        agent_id=agent_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    agent_id: int,
    *,
    client: AuthenticatedClient,
) -> Response[Union[ApiBackendNotAvailableError, ApiCurrentlyExecutedStepInfo, ApiInternalError, ApiUnauthorizedError]]:
    """Get currently executing task

     Get the task which currently executed by the given agent.

    Args:
        agent_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ApiBackendNotAvailableError, ApiCurrentlyExecutedStepInfo, ApiInternalError, ApiUnauthorizedError]]
    """

    kwargs = _get_kwargs(
        agent_id=agent_id,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    agent_id: int,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[ApiBackendNotAvailableError, ApiCurrentlyExecutedStepInfo, ApiInternalError, ApiUnauthorizedError]]:
    """Get currently executing task

     Get the task which currently executed by the given agent.

    Args:
        agent_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ApiBackendNotAvailableError, ApiCurrentlyExecutedStepInfo, ApiInternalError, ApiUnauthorizedError]]
    """

    return (
        await asyncio_detailed(
            agent_id=agent_id,
            client=client,
        )
    ).parsed
