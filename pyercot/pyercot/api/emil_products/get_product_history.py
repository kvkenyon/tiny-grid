from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.exception import Exception_
from ...models.product_history import ProductHistory
from ...types import Response


def _get_kwargs(
    emil_id: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/archive/{emil_id}".format(
            emil_id=quote(str(emil_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Exception_ | ProductHistory | None:
    if response.status_code == 200:
        response_200 = ProductHistory.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = Exception_.from_dict(response.json())

        return response_400

    if response.status_code == 403:
        response_403 = Exception_.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = Exception_.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Exception_ | ProductHistory]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    emil_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Exception_ | ProductHistory]:
    """Available report archives for a specified EMIL product.

     Available report archives for a specified EMIL product.

    Args:
        emil_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Exception_ | ProductHistory]
    """

    kwargs = _get_kwargs(
        emil_id=emil_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    emil_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Exception_ | ProductHistory | None:
    """Available report archives for a specified EMIL product.

     Available report archives for a specified EMIL product.

    Args:
        emil_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Exception_ | ProductHistory
    """

    return sync_detailed(
        emil_id=emil_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    emil_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Exception_ | ProductHistory]:
    """Available report archives for a specified EMIL product.

     Available report archives for a specified EMIL product.

    Args:
        emil_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Exception_ | ProductHistory]
    """

    kwargs = _get_kwargs(
        emil_id=emil_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    emil_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Exception_ | ProductHistory | None:
    """Available report archives for a specified EMIL product.

     Available report archives for a specified EMIL product.

    Args:
        emil_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Exception_ | ProductHistory
    """

    return (
        await asyncio_detailed(
            emil_id=emil_id,
            client=client,
        )
    ).parsed
