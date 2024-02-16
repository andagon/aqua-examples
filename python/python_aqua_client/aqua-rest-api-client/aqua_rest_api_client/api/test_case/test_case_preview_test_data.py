from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_argument_error import ApiArgumentError
from ...models.api_backend_not_available_error import ApiBackendNotAvailableError
from ...models.api_internal_error import ApiInternalError
from ...models.api_test_data_preview import ApiTestDataPreview
from ...models.api_unauthorized_error import ApiUnauthorizedError
from ...types import Response


def _get_kwargs(
    *,
    client: AuthenticatedClient,
    json_body: ApiTestDataPreview,
) -> Dict[str, Any]:
    url = "{}/api/TestCase/TestData/Preview".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_json_body = json_body.to_dict()

    return {
        "method": "post",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "json": json_json_body,
    }


def _parse_response(
    *, client: Client, response: httpx.Response
) -> Optional[
    Union[ApiArgumentError, ApiBackendNotAvailableError, ApiInternalError, ApiTestDataPreview, ApiUnauthorizedError]
]:
    if response.status_code == HTTPStatus.OK:
        response_200 = ApiTestDataPreview.from_dict(response.json())

        return response_200
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
    Union[ApiArgumentError, ApiBackendNotAvailableError, ApiInternalError, ApiTestDataPreview, ApiUnauthorizedError]
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
    json_body: ApiTestDataPreview,
) -> Response[
    Union[ApiArgumentError, ApiBackendNotAvailableError, ApiInternalError, ApiTestDataPreview, ApiUnauthorizedError]
]:
    """Create test data preview

     Allows to perform a 'preview' of test data values.
                By preview we mean that all formulas are resolved to actual values (the same way as
    during actual execution).

    Args:
        json_body (ApiTestDataPreview): This model is used when generating a "preview" of test
            data i.e. request server to provide
            actual data for all formulas included in the data.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ApiArgumentError, ApiBackendNotAvailableError, ApiInternalError, ApiTestDataPreview, ApiUnauthorizedError]]
    """

    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    json_body: ApiTestDataPreview,
) -> Optional[
    Union[ApiArgumentError, ApiBackendNotAvailableError, ApiInternalError, ApiTestDataPreview, ApiUnauthorizedError]
]:
    """Create test data preview

     Allows to perform a 'preview' of test data values.
                By preview we mean that all formulas are resolved to actual values (the same way as
    during actual execution).

    Args:
        json_body (ApiTestDataPreview): This model is used when generating a "preview" of test
            data i.e. request server to provide
            actual data for all formulas included in the data.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ApiArgumentError, ApiBackendNotAvailableError, ApiInternalError, ApiTestDataPreview, ApiUnauthorizedError]]
    """

    return sync_detailed(
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    json_body: ApiTestDataPreview,
) -> Response[
    Union[ApiArgumentError, ApiBackendNotAvailableError, ApiInternalError, ApiTestDataPreview, ApiUnauthorizedError]
]:
    """Create test data preview

     Allows to perform a 'preview' of test data values.
                By preview we mean that all formulas are resolved to actual values (the same way as
    during actual execution).

    Args:
        json_body (ApiTestDataPreview): This model is used when generating a "preview" of test
            data i.e. request server to provide
            actual data for all formulas included in the data.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ApiArgumentError, ApiBackendNotAvailableError, ApiInternalError, ApiTestDataPreview, ApiUnauthorizedError]]
    """

    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    json_body: ApiTestDataPreview,
) -> Optional[
    Union[ApiArgumentError, ApiBackendNotAvailableError, ApiInternalError, ApiTestDataPreview, ApiUnauthorizedError]
]:
    """Create test data preview

     Allows to perform a 'preview' of test data values.
                By preview we mean that all formulas are resolved to actual values (the same way as
    during actual execution).

    Args:
        json_body (ApiTestDataPreview): This model is used when generating a "preview" of test
            data i.e. request server to provide
            actual data for all formulas included in the data.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ApiArgumentError, ApiBackendNotAvailableError, ApiInternalError, ApiTestDataPreview, ApiUnauthorizedError]]
    """

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
        )
    ).parsed
