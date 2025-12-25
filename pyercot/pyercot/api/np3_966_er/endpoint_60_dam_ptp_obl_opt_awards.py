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
    hour_ending_from: str | Unset = UNSET,
    hour_ending_to: str | Unset = UNSET,
    qse_name: str | Unset = UNSET,
    settlement_point_source: str | Unset = UNSET,
    settlement_point_sink: str | Unset = UNSET,
    mw_from: float | Unset = UNSET,
    mw_to: float | Unset = UNSET,
    price_from: float | Unset = UNSET,
    price_to: float | Unset = UNSET,
    offer_id: str | Unset = UNSET,
    crr_id: str | Unset = UNSET,
    page: int | Unset = UNSET,
    size: int | Unset = UNSET,
    sort: str | Unset = UNSET,
    dir_: str | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["deliveryDateFrom"] = delivery_date_from

    params["deliveryDateTo"] = delivery_date_to

    params["hourEndingFrom"] = hour_ending_from

    params["hourEndingTo"] = hour_ending_to

    params["qseName"] = qse_name

    params["settlementPointSource"] = settlement_point_source

    params["settlementPointSink"] = settlement_point_sink

    params["MWFrom"] = mw_from

    params["MWTo"] = mw_to

    params["priceFrom"] = price_from

    params["priceTo"] = price_to

    params["offerId"] = offer_id

    params["CRRId"] = crr_id

    params["page"] = page

    params["size"] = size

    params["sort"] = sort

    params["dir"] = dir_

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/np3-966-er/60_dam_ptp_obl_opt_awards",
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
    hour_ending_from: str | Unset = UNSET,
    hour_ending_to: str | Unset = UNSET,
    qse_name: str | Unset = UNSET,
    settlement_point_source: str | Unset = UNSET,
    settlement_point_sink: str | Unset = UNSET,
    mw_from: float | Unset = UNSET,
    mw_to: float | Unset = UNSET,
    price_from: float | Unset = UNSET,
    price_to: float | Unset = UNSET,
    offer_id: str | Unset = UNSET,
    crr_id: str | Unset = UNSET,
    page: int | Unset = UNSET,
    size: int | Unset = UNSET,
    sort: str | Unset = UNSET,
    dir_: str | Unset = UNSET,
) -> Response[Exception_ | Report]:
    """60 Day DAM PTP Obligation Option Awards

     60 Day DAM PTP Obligation Option Awards

    Args:
        delivery_date_from (str | Unset):
        delivery_date_to (str | Unset):
        hour_ending_from (str | Unset):
        hour_ending_to (str | Unset):
        qse_name (str | Unset):
        settlement_point_source (str | Unset):
        settlement_point_sink (str | Unset):
        mw_from (float | Unset):
        mw_to (float | Unset):
        price_from (float | Unset):
        price_to (float | Unset):
        offer_id (str | Unset):
        crr_id (str | Unset):
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
        hour_ending_from=hour_ending_from,
        hour_ending_to=hour_ending_to,
        qse_name=qse_name,
        settlement_point_source=settlement_point_source,
        settlement_point_sink=settlement_point_sink,
        mw_from=mw_from,
        mw_to=mw_to,
        price_from=price_from,
        price_to=price_to,
        offer_id=offer_id,
        crr_id=crr_id,
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
    hour_ending_from: str | Unset = UNSET,
    hour_ending_to: str | Unset = UNSET,
    qse_name: str | Unset = UNSET,
    settlement_point_source: str | Unset = UNSET,
    settlement_point_sink: str | Unset = UNSET,
    mw_from: float | Unset = UNSET,
    mw_to: float | Unset = UNSET,
    price_from: float | Unset = UNSET,
    price_to: float | Unset = UNSET,
    offer_id: str | Unset = UNSET,
    crr_id: str | Unset = UNSET,
    page: int | Unset = UNSET,
    size: int | Unset = UNSET,
    sort: str | Unset = UNSET,
    dir_: str | Unset = UNSET,
) -> Exception_ | Report | None:
    """60 Day DAM PTP Obligation Option Awards

     60 Day DAM PTP Obligation Option Awards

    Args:
        delivery_date_from (str | Unset):
        delivery_date_to (str | Unset):
        hour_ending_from (str | Unset):
        hour_ending_to (str | Unset):
        qse_name (str | Unset):
        settlement_point_source (str | Unset):
        settlement_point_sink (str | Unset):
        mw_from (float | Unset):
        mw_to (float | Unset):
        price_from (float | Unset):
        price_to (float | Unset):
        offer_id (str | Unset):
        crr_id (str | Unset):
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
        hour_ending_from=hour_ending_from,
        hour_ending_to=hour_ending_to,
        qse_name=qse_name,
        settlement_point_source=settlement_point_source,
        settlement_point_sink=settlement_point_sink,
        mw_from=mw_from,
        mw_to=mw_to,
        price_from=price_from,
        price_to=price_to,
        offer_id=offer_id,
        crr_id=crr_id,
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
    hour_ending_from: str | Unset = UNSET,
    hour_ending_to: str | Unset = UNSET,
    qse_name: str | Unset = UNSET,
    settlement_point_source: str | Unset = UNSET,
    settlement_point_sink: str | Unset = UNSET,
    mw_from: float | Unset = UNSET,
    mw_to: float | Unset = UNSET,
    price_from: float | Unset = UNSET,
    price_to: float | Unset = UNSET,
    offer_id: str | Unset = UNSET,
    crr_id: str | Unset = UNSET,
    page: int | Unset = UNSET,
    size: int | Unset = UNSET,
    sort: str | Unset = UNSET,
    dir_: str | Unset = UNSET,
) -> Response[Exception_ | Report]:
    """60 Day DAM PTP Obligation Option Awards

     60 Day DAM PTP Obligation Option Awards

    Args:
        delivery_date_from (str | Unset):
        delivery_date_to (str | Unset):
        hour_ending_from (str | Unset):
        hour_ending_to (str | Unset):
        qse_name (str | Unset):
        settlement_point_source (str | Unset):
        settlement_point_sink (str | Unset):
        mw_from (float | Unset):
        mw_to (float | Unset):
        price_from (float | Unset):
        price_to (float | Unset):
        offer_id (str | Unset):
        crr_id (str | Unset):
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
        hour_ending_from=hour_ending_from,
        hour_ending_to=hour_ending_to,
        qse_name=qse_name,
        settlement_point_source=settlement_point_source,
        settlement_point_sink=settlement_point_sink,
        mw_from=mw_from,
        mw_to=mw_to,
        price_from=price_from,
        price_to=price_to,
        offer_id=offer_id,
        crr_id=crr_id,
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
    hour_ending_from: str | Unset = UNSET,
    hour_ending_to: str | Unset = UNSET,
    qse_name: str | Unset = UNSET,
    settlement_point_source: str | Unset = UNSET,
    settlement_point_sink: str | Unset = UNSET,
    mw_from: float | Unset = UNSET,
    mw_to: float | Unset = UNSET,
    price_from: float | Unset = UNSET,
    price_to: float | Unset = UNSET,
    offer_id: str | Unset = UNSET,
    crr_id: str | Unset = UNSET,
    page: int | Unset = UNSET,
    size: int | Unset = UNSET,
    sort: str | Unset = UNSET,
    dir_: str | Unset = UNSET,
) -> Exception_ | Report | None:
    """60 Day DAM PTP Obligation Option Awards

     60 Day DAM PTP Obligation Option Awards

    Args:
        delivery_date_from (str | Unset):
        delivery_date_to (str | Unset):
        hour_ending_from (str | Unset):
        hour_ending_to (str | Unset):
        qse_name (str | Unset):
        settlement_point_source (str | Unset):
        settlement_point_sink (str | Unset):
        mw_from (float | Unset):
        mw_to (float | Unset):
        price_from (float | Unset):
        price_to (float | Unset):
        offer_id (str | Unset):
        crr_id (str | Unset):
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
            hour_ending_from=hour_ending_from,
            hour_ending_to=hour_ending_to,
            qse_name=qse_name,
            settlement_point_source=settlement_point_source,
            settlement_point_sink=settlement_point_sink,
            mw_from=mw_from,
            mw_to=mw_to,
            price_from=price_from,
            price_to=price_to,
            offer_id=offer_id,
            crr_id=crr_id,
            page=page,
            size=size,
            sort=sort,
            dir_=dir_,
        )
    ).parsed
