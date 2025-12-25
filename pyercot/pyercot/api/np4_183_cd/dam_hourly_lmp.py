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
    dst_flag: bool | Unset = UNSET,
    delivery_date_from: str | Unset = UNSET,
    delivery_date_to: str | Unset = UNSET,
    hour_ending: str | Unset = UNSET,
    bus_name: str | Unset = UNSET,
    lmp_from: float | Unset = UNSET,
    lmp_to: float | Unset = UNSET,
    page: int | Unset = UNSET,
    size: int | Unset = UNSET,
    sort: str | Unset = UNSET,
    dir_: str | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["DSTFlag"] = dst_flag

    params["deliveryDateFrom"] = delivery_date_from

    params["deliveryDateTo"] = delivery_date_to

    params["hourEnding"] = hour_ending

    params["busName"] = bus_name

    params["LMPFrom"] = lmp_from

    params["LMPTo"] = lmp_to

    params["page"] = page

    params["size"] = size

    params["sort"] = sort

    params["dir"] = dir_

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/np4-183-cd/dam_hourly_lmp",
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
    dst_flag: bool | Unset = UNSET,
    delivery_date_from: str | Unset = UNSET,
    delivery_date_to: str | Unset = UNSET,
    hour_ending: str | Unset = UNSET,
    bus_name: str | Unset = UNSET,
    lmp_from: float | Unset = UNSET,
    lmp_to: float | Unset = UNSET,
    page: int | Unset = UNSET,
    size: int | Unset = UNSET,
    sort: str | Unset = UNSET,
    dir_: str | Unset = UNSET,
) -> Response[Exception_ | Report]:
    """DAM Hourly LMPs

     DAM Hourly LMPs

    Args:
        dst_flag (bool | Unset):
        delivery_date_from (str | Unset):
        delivery_date_to (str | Unset):
        hour_ending (str | Unset):
        bus_name (str | Unset):
        lmp_from (float | Unset):
        lmp_to (float | Unset):
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
        dst_flag=dst_flag,
        delivery_date_from=delivery_date_from,
        delivery_date_to=delivery_date_to,
        hour_ending=hour_ending,
        bus_name=bus_name,
        lmp_from=lmp_from,
        lmp_to=lmp_to,
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
    dst_flag: bool | Unset = UNSET,
    delivery_date_from: str | Unset = UNSET,
    delivery_date_to: str | Unset = UNSET,
    hour_ending: str | Unset = UNSET,
    bus_name: str | Unset = UNSET,
    lmp_from: float | Unset = UNSET,
    lmp_to: float | Unset = UNSET,
    page: int | Unset = UNSET,
    size: int | Unset = UNSET,
    sort: str | Unset = UNSET,
    dir_: str | Unset = UNSET,
) -> Exception_ | Report | None:
    """DAM Hourly LMPs

     DAM Hourly LMPs

    Args:
        dst_flag (bool | Unset):
        delivery_date_from (str | Unset):
        delivery_date_to (str | Unset):
        hour_ending (str | Unset):
        bus_name (str | Unset):
        lmp_from (float | Unset):
        lmp_to (float | Unset):
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
        dst_flag=dst_flag,
        delivery_date_from=delivery_date_from,
        delivery_date_to=delivery_date_to,
        hour_ending=hour_ending,
        bus_name=bus_name,
        lmp_from=lmp_from,
        lmp_to=lmp_to,
        page=page,
        size=size,
        sort=sort,
        dir_=dir_,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    dst_flag: bool | Unset = UNSET,
    delivery_date_from: str | Unset = UNSET,
    delivery_date_to: str | Unset = UNSET,
    hour_ending: str | Unset = UNSET,
    bus_name: str | Unset = UNSET,
    lmp_from: float | Unset = UNSET,
    lmp_to: float | Unset = UNSET,
    page: int | Unset = UNSET,
    size: int | Unset = UNSET,
    sort: str | Unset = UNSET,
    dir_: str | Unset = UNSET,
) -> Response[Exception_ | Report]:
    """DAM Hourly LMPs

     DAM Hourly LMPs

    Args:
        dst_flag (bool | Unset):
        delivery_date_from (str | Unset):
        delivery_date_to (str | Unset):
        hour_ending (str | Unset):
        bus_name (str | Unset):
        lmp_from (float | Unset):
        lmp_to (float | Unset):
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
        dst_flag=dst_flag,
        delivery_date_from=delivery_date_from,
        delivery_date_to=delivery_date_to,
        hour_ending=hour_ending,
        bus_name=bus_name,
        lmp_from=lmp_from,
        lmp_to=lmp_to,
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
    dst_flag: bool | Unset = UNSET,
    delivery_date_from: str | Unset = UNSET,
    delivery_date_to: str | Unset = UNSET,
    hour_ending: str | Unset = UNSET,
    bus_name: str | Unset = UNSET,
    lmp_from: float | Unset = UNSET,
    lmp_to: float | Unset = UNSET,
    page: int | Unset = UNSET,
    size: int | Unset = UNSET,
    sort: str | Unset = UNSET,
    dir_: str | Unset = UNSET,
) -> Exception_ | Report | None:
    """DAM Hourly LMPs

     DAM Hourly LMPs

    Args:
        dst_flag (bool | Unset):
        delivery_date_from (str | Unset):
        delivery_date_to (str | Unset):
        hour_ending (str | Unset):
        bus_name (str | Unset):
        lmp_from (float | Unset):
        lmp_to (float | Unset):
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
            dst_flag=dst_flag,
            delivery_date_from=delivery_date_from,
            delivery_date_to=delivery_date_to,
            hour_ending=hour_ending,
            bus_name=bus_name,
            lmp_from=lmp_from,
            lmp_to=lmp_to,
            page=page,
            size=size,
            sort=sort,
            dir_=dir_,
        )
    ).parsed
