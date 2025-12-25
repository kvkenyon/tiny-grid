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
    delivery_date_from: str | Unset = UNSET,
    delivery_date_to: str | Unset = UNSET,
    delivery_hour_from: int | Unset = UNSET,
    delivery_hour_to: int | Unset = UNSET,
    delivery_interval_from: int | Unset = UNSET,
    delivery_interval_to: int | Unset = UNSET,
    settlement_point: str | Unset = UNSET,
    settlement_point_type: str | Unset = UNSET,
    settlement_point_price_from: float | Unset = UNSET,
    settlement_point_price_to: float | Unset = UNSET,
    dst_flag: bool | Unset = UNSET,
    page: int | Unset = UNSET,
    size: int | Unset = UNSET,
    sort: str | Unset = UNSET,
    dir_: str | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["deliveryDateFrom"] = delivery_date_from

    params["deliveryDateTo"] = delivery_date_to

    params["deliveryHourFrom"] = delivery_hour_from

    params["deliveryHourTo"] = delivery_hour_to

    params["deliveryIntervalFrom"] = delivery_interval_from

    params["deliveryIntervalTo"] = delivery_interval_to

    params["settlementPoint"] = settlement_point

    params["settlementPointType"] = settlement_point_type

    params["settlementPointPriceFrom"] = settlement_point_price_from

    params["settlementPointPriceTo"] = settlement_point_price_to

    params["DSTFlag"] = dst_flag

    params["page"] = page

    params["size"] = size

    params["sort"] = sort

    params["dir"] = dir_

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/np6-905-cd/spp_node_zone_hub",
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
    delivery_date_from: str | Unset = UNSET,
    delivery_date_to: str | Unset = UNSET,
    delivery_hour_from: int | Unset = UNSET,
    delivery_hour_to: int | Unset = UNSET,
    delivery_interval_from: int | Unset = UNSET,
    delivery_interval_to: int | Unset = UNSET,
    settlement_point: str | Unset = UNSET,
    settlement_point_type: str | Unset = UNSET,
    settlement_point_price_from: float | Unset = UNSET,
    settlement_point_price_to: float | Unset = UNSET,
    dst_flag: bool | Unset = UNSET,
    page: int | Unset = UNSET,
    size: int | Unset = UNSET,
    sort: str | Unset = UNSET,
    dir_: str | Unset = UNSET,
) -> Response[Exception_ | Report]:
    """Settlement Point Prices at Resource Nodes, Hubs and Load Zones

     Settlement Point Prices at Resource Nodes, Hubs and Load Zones

    Args:
        delivery_date_from (str | Unset):
        delivery_date_to (str | Unset):
        delivery_hour_from (int | Unset):
        delivery_hour_to (int | Unset):
        delivery_interval_from (int | Unset):
        delivery_interval_to (int | Unset):
        settlement_point (str | Unset):
        settlement_point_type (str | Unset):
        settlement_point_price_from (float | Unset):
        settlement_point_price_to (float | Unset):
        dst_flag (bool | Unset):
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
        delivery_date_from=delivery_date_from,
        delivery_date_to=delivery_date_to,
        delivery_hour_from=delivery_hour_from,
        delivery_hour_to=delivery_hour_to,
        delivery_interval_from=delivery_interval_from,
        delivery_interval_to=delivery_interval_to,
        settlement_point=settlement_point,
        settlement_point_type=settlement_point_type,
        settlement_point_price_from=settlement_point_price_from,
        settlement_point_price_to=settlement_point_price_to,
        dst_flag=dst_flag,
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
    delivery_date_from: str | Unset = UNSET,
    delivery_date_to: str | Unset = UNSET,
    delivery_hour_from: int | Unset = UNSET,
    delivery_hour_to: int | Unset = UNSET,
    delivery_interval_from: int | Unset = UNSET,
    delivery_interval_to: int | Unset = UNSET,
    settlement_point: str | Unset = UNSET,
    settlement_point_type: str | Unset = UNSET,
    settlement_point_price_from: float | Unset = UNSET,
    settlement_point_price_to: float | Unset = UNSET,
    dst_flag: bool | Unset = UNSET,
    page: int | Unset = UNSET,
    size: int | Unset = UNSET,
    sort: str | Unset = UNSET,
    dir_: str | Unset = UNSET,
) -> Exception_ | Report | None:
    """Settlement Point Prices at Resource Nodes, Hubs and Load Zones

     Settlement Point Prices at Resource Nodes, Hubs and Load Zones

    Args:
        delivery_date_from (str | Unset):
        delivery_date_to (str | Unset):
        delivery_hour_from (int | Unset):
        delivery_hour_to (int | Unset):
        delivery_interval_from (int | Unset):
        delivery_interval_to (int | Unset):
        settlement_point (str | Unset):
        settlement_point_type (str | Unset):
        settlement_point_price_from (float | Unset):
        settlement_point_price_to (float | Unset):
        dst_flag (bool | Unset):
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
        delivery_date_from=delivery_date_from,
        delivery_date_to=delivery_date_to,
        delivery_hour_from=delivery_hour_from,
        delivery_hour_to=delivery_hour_to,
        delivery_interval_from=delivery_interval_from,
        delivery_interval_to=delivery_interval_to,
        settlement_point=settlement_point,
        settlement_point_type=settlement_point_type,
        settlement_point_price_from=settlement_point_price_from,
        settlement_point_price_to=settlement_point_price_to,
        dst_flag=dst_flag,
        page=page,
        size=size,
        sort=sort,
        dir_=dir_,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    delivery_date_from: str | Unset = UNSET,
    delivery_date_to: str | Unset = UNSET,
    delivery_hour_from: int | Unset = UNSET,
    delivery_hour_to: int | Unset = UNSET,
    delivery_interval_from: int | Unset = UNSET,
    delivery_interval_to: int | Unset = UNSET,
    settlement_point: str | Unset = UNSET,
    settlement_point_type: str | Unset = UNSET,
    settlement_point_price_from: float | Unset = UNSET,
    settlement_point_price_to: float | Unset = UNSET,
    dst_flag: bool | Unset = UNSET,
    page: int | Unset = UNSET,
    size: int | Unset = UNSET,
    sort: str | Unset = UNSET,
    dir_: str | Unset = UNSET,
) -> Response[Exception_ | Report]:
    """Settlement Point Prices at Resource Nodes, Hubs and Load Zones

     Settlement Point Prices at Resource Nodes, Hubs and Load Zones

    Args:
        delivery_date_from (str | Unset):
        delivery_date_to (str | Unset):
        delivery_hour_from (int | Unset):
        delivery_hour_to (int | Unset):
        delivery_interval_from (int | Unset):
        delivery_interval_to (int | Unset):
        settlement_point (str | Unset):
        settlement_point_type (str | Unset):
        settlement_point_price_from (float | Unset):
        settlement_point_price_to (float | Unset):
        dst_flag (bool | Unset):
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
        delivery_date_from=delivery_date_from,
        delivery_date_to=delivery_date_to,
        delivery_hour_from=delivery_hour_from,
        delivery_hour_to=delivery_hour_to,
        delivery_interval_from=delivery_interval_from,
        delivery_interval_to=delivery_interval_to,
        settlement_point=settlement_point,
        settlement_point_type=settlement_point_type,
        settlement_point_price_from=settlement_point_price_from,
        settlement_point_price_to=settlement_point_price_to,
        dst_flag=dst_flag,
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
    delivery_date_from: str | Unset = UNSET,
    delivery_date_to: str | Unset = UNSET,
    delivery_hour_from: int | Unset = UNSET,
    delivery_hour_to: int | Unset = UNSET,
    delivery_interval_from: int | Unset = UNSET,
    delivery_interval_to: int | Unset = UNSET,
    settlement_point: str | Unset = UNSET,
    settlement_point_type: str | Unset = UNSET,
    settlement_point_price_from: float | Unset = UNSET,
    settlement_point_price_to: float | Unset = UNSET,
    dst_flag: bool | Unset = UNSET,
    page: int | Unset = UNSET,
    size: int | Unset = UNSET,
    sort: str | Unset = UNSET,
    dir_: str | Unset = UNSET,
) -> Exception_ | Report | None:
    """Settlement Point Prices at Resource Nodes, Hubs and Load Zones

     Settlement Point Prices at Resource Nodes, Hubs and Load Zones

    Args:
        delivery_date_from (str | Unset):
        delivery_date_to (str | Unset):
        delivery_hour_from (int | Unset):
        delivery_hour_to (int | Unset):
        delivery_interval_from (int | Unset):
        delivery_interval_to (int | Unset):
        settlement_point (str | Unset):
        settlement_point_type (str | Unset):
        settlement_point_price_from (float | Unset):
        settlement_point_price_to (float | Unset):
        dst_flag (bool | Unset):
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
            delivery_date_from=delivery_date_from,
            delivery_date_to=delivery_date_to,
            delivery_hour_from=delivery_hour_from,
            delivery_hour_to=delivery_hour_to,
            delivery_interval_from=delivery_interval_from,
            delivery_interval_to=delivery_interval_to,
            settlement_point=settlement_point,
            settlement_point_type=settlement_point_type,
            settlement_point_price_from=settlement_point_price_from,
            settlement_point_price_to=settlement_point_price_to,
            dst_flag=dst_flag,
            page=page,
            size=size,
            sort=sort,
            dir_=dir_,
        )
    ).parsed
