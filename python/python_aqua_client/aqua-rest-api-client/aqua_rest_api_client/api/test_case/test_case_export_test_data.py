from http import HTTPStatus
from io import BytesIO
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_test_data_file_format import ApiTestDataFileFormat
from ...types import UNSET, File, Response, Unset


def _get_kwargs(
    id: int,
    *,
    client: AuthenticatedClient,
    file_format: Union[ApiTestDataFileFormat, None, Unset] = UNSET,
) -> Dict[str, Any]:
    url = "{}/api/TestCase/{id}/TestData/Transfer".format(client.base_url, id=id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    json_file_format: Union[None, Unset, str]
    if isinstance(file_format, Unset):
        json_file_format = UNSET
    elif file_format is None:
        json_file_format = None

    else:
        json_file_format = UNSET
        if not isinstance(file_format, Unset):
            json_file_format = file_format.value if file_format else None

    params["fileFormat"] = json_file_format

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
    if response.status_code == HTTPStatus.FORBIDDEN:
        response_403 = cast(str, response.text)
        return response_403
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
    id: int,
    *,
    client: AuthenticatedClient,
    file_format: Union[ApiTestDataFileFormat, None, Unset] = UNSET,
) -> Response[Union[File, str]]:
    """Export test data

     Export the test data of this test case in the specified file format and allows
                to download the resulting file.

    Args:
        id (int):
        file_format (Union[ApiTestDataFileFormat, None, Unset]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[File, str]]
    """

    kwargs = _get_kwargs(
        id=id,
        client=client,
        file_format=file_format,
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
    file_format: Union[ApiTestDataFileFormat, None, Unset] = UNSET,
) -> Optional[Union[File, str]]:
    """Export test data

     Export the test data of this test case in the specified file format and allows
                to download the resulting file.

    Args:
        id (int):
        file_format (Union[ApiTestDataFileFormat, None, Unset]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[File, str]]
    """

    return sync_detailed(
        id=id,
        client=client,
        file_format=file_format,
    ).parsed


async def asyncio_detailed(
    id: int,
    *,
    client: AuthenticatedClient,
    file_format: Union[ApiTestDataFileFormat, None, Unset] = UNSET,
) -> Response[Union[File, str]]:
    """Export test data

     Export the test data of this test case in the specified file format and allows
                to download the resulting file.

    Args:
        id (int):
        file_format (Union[ApiTestDataFileFormat, None, Unset]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[File, str]]
    """

    kwargs = _get_kwargs(
        id=id,
        client=client,
        file_format=file_format,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: int,
    *,
    client: AuthenticatedClient,
    file_format: Union[ApiTestDataFileFormat, None, Unset] = UNSET,
) -> Optional[Union[File, str]]:
    """Export test data

     Export the test data of this test case in the specified file format and allows
                to download the resulting file.

    Args:
        id (int):
        file_format (Union[ApiTestDataFileFormat, None, Unset]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[File, str]]
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            file_format=file_format,
        )
    ).parsed
