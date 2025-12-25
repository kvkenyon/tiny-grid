from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.exception import Exception_
from ...models.report import Report
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    interval_value_from: float | Unset = UNSET,
    interval_value_to: float | Unset = UNSET,
    interval_time_from: str | Unset = UNSET,
    interval_time_to: str | Unset = UNSET,
    interval_number_from: int | Unset = UNSET,
    interval_number_to: int | Unset = UNSET,
    resource_code: str | Unset = UNSET,
    page: int | Unset = UNSET,
    size: int | Unset = UNSET,
    sort: str | Unset = UNSET,
    dir_: str | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["intervalValueFrom"] = interval_value_from

    params["intervalValueTo"] = interval_value_to

    params["intervalTimeFrom"] = interval_time_from

    params["intervalTimeTo"] = interval_time_to

    params["intervalNumberFrom"] = interval_number_from

    params["intervalNumberTo"] = interval_number_to

    params["resourceCode"] = resource_code

    params["page"] = page

    params["size"] = size

    params["sort"] = sort

    params["dir"] = dir_

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/np3-965-er/60_sced_smne_gen_res",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Exception_ | Report | None:
    if response.status_code == 200:
        response_200 = Report.from_dict(response.json())

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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Exception_ | Report]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    interval_value_from: float | Unset = UNSET,
    interval_value_to: float | Unset = UNSET,
    interval_time_from: str | Unset = UNSET,
    interval_time_to: str | Unset = UNSET,
    interval_number_from: int | Unset = UNSET,
    interval_number_to: int | Unset = UNSET,
    resource_code: str | Unset = UNSET,
    page: int | Unset = UNSET,
    size: int | Unset = UNSET,
    sort: str | Unset = UNSET,
    dir_: str | Unset = UNSET,
) -> Response[Exception_ | Report]:
    """60 Day SCED Settlement Metered Net Energy for Generation Resources

     60 Day SCED Settlement Metered Net Energy for Generation Resources

    Args:
        interval_value_from (float | Unset):
        interval_value_to (float | Unset):
        interval_time_from (str | Unset):
        interval_time_to (str | Unset):
        interval_number_from (int | Unset):
        interval_number_to (int | Unset):
        resource_code (str | Unset):
        page (int | Unset):
        size (int | Unset):
        sort (str | Unset):
        dir_ (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Exception_ | Report]
    """

    kwargs = _get_kwargs(
        interval_value_from=interval_value_from,
        interval_value_to=interval_value_to,
        interval_time_from=interval_time_from,
        interval_time_to=interval_time_to,
        interval_number_from=interval_number_from,
        interval_number_to=interval_number_to,
        resource_code=resource_code,
        page=page,
        size=size,
        sort=sort,
        dir_=dir_,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    interval_value_from: float | Unset = UNSET,
    interval_value_to: float | Unset = UNSET,
    interval_time_from: str | Unset = UNSET,
    interval_time_to: str | Unset = UNSET,
    interval_number_from: int | Unset = UNSET,
    interval_number_to: int | Unset = UNSET,
    resource_code: str | Unset = UNSET,
    page: int | Unset = UNSET,
    size: int | Unset = UNSET,
    sort: str | Unset = UNSET,
    dir_: str | Unset = UNSET,
) -> Exception_ | Report | None:
    """60 Day SCED Settlement Metered Net Energy for Generation Resources

     60 Day SCED Settlement Metered Net Energy for Generation Resources

    Args:
        interval_value_from (float | Unset):
        interval_value_to (float | Unset):
        interval_time_from (str | Unset):
        interval_time_to (str | Unset):
        interval_number_from (int | Unset):
        interval_number_to (int | Unset):
        resource_code (str | Unset):
        page (int | Unset):
        size (int | Unset):
        sort (str | Unset):
        dir_ (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Exception_ | Report
    """

    return sync_detailed(
        client=client,
        interval_value_from=interval_value_from,
        interval_value_to=interval_value_to,
        interval_time_from=interval_time_from,
        interval_time_to=interval_time_to,
        interval_number_from=interval_number_from,
        interval_number_to=interval_number_to,
        resource_code=resource_code,
        page=page,
        size=size,
        sort=sort,
        dir_=dir_,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    interval_value_from: float | Unset = UNSET,
    interval_value_to: float | Unset = UNSET,
    interval_time_from: str | Unset = UNSET,
    interval_time_to: str | Unset = UNSET,
    interval_number_from: int | Unset = UNSET,
    interval_number_to: int | Unset = UNSET,
    resource_code: str | Unset = UNSET,
    page: int | Unset = UNSET,
    size: int | Unset = UNSET,
    sort: str | Unset = UNSET,
    dir_: str | Unset = UNSET,
) -> Response[Exception_ | Report]:
    """60 Day SCED Settlement Metered Net Energy for Generation Resources

     60 Day SCED Settlement Metered Net Energy for Generation Resources

    Args:
        interval_value_from (float | Unset):
        interval_value_to (float | Unset):
        interval_time_from (str | Unset):
        interval_time_to (str | Unset):
        interval_number_from (int | Unset):
        interval_number_to (int | Unset):
        resource_code (str | Unset):
        page (int | Unset):
        size (int | Unset):
        sort (str | Unset):
        dir_ (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Exception_ | Report]
    """

    kwargs = _get_kwargs(
        interval_value_from=interval_value_from,
        interval_value_to=interval_value_to,
        interval_time_from=interval_time_from,
        interval_time_to=interval_time_to,
        interval_number_from=interval_number_from,
        interval_number_to=interval_number_to,
        resource_code=resource_code,
        page=page,
        size=size,
        sort=sort,
        dir_=dir_,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    interval_value_from: float | Unset = UNSET,
    interval_value_to: float | Unset = UNSET,
    interval_time_from: str | Unset = UNSET,
    interval_time_to: str | Unset = UNSET,
    interval_number_from: int | Unset = UNSET,
    interval_number_to: int | Unset = UNSET,
    resource_code: str | Unset = UNSET,
    page: int | Unset = UNSET,
    size: int | Unset = UNSET,
    sort: str | Unset = UNSET,
    dir_: str | Unset = UNSET,
) -> Exception_ | Report | None:
    """60 Day SCED Settlement Metered Net Energy for Generation Resources

     60 Day SCED Settlement Metered Net Energy for Generation Resources

    Args:
        interval_value_from (float | Unset):
        interval_value_to (float | Unset):
        interval_time_from (str | Unset):
        interval_time_to (str | Unset):
        interval_number_from (int | Unset):
        interval_number_to (int | Unset):
        resource_code (str | Unset):
        page (int | Unset):
        size (int | Unset):
        sort (str | Unset):
        dir_ (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Exception_ | Report
    """

    return (
        await asyncio_detailed(
            client=client,
            interval_value_from=interval_value_from,
            interval_value_to=interval_value_to,
            interval_time_from=interval_time_from,
            interval_time_to=interval_time_to,
            interval_number_from=interval_number_from,
            interval_number_to=interval_number_to,
            resource_code=resource_code,
            page=page,
            size=size,
            sort=sort,
            dir_=dir_,
        )
    ).parsed
