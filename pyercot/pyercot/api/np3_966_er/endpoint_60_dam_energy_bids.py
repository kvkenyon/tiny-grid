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
    energy_only_bid_mw_1_from: float | Unset = UNSET,
    energy_only_bid_mw_1_to: float | Unset = UNSET,
    energy_only_bid_price_1_from: float | Unset = UNSET,
    energy_only_bid_price_1_to: float | Unset = UNSET,
    energy_only_bid_mw_2_from: float | Unset = UNSET,
    energy_only_bid_mw_2_to: float | Unset = UNSET,
    energy_only_bid_price_2_from: float | Unset = UNSET,
    energy_only_bid_price_2_to: float | Unset = UNSET,
    energy_only_bid_mw_3_from: float | Unset = UNSET,
    energy_only_bid_mw_3_to: float | Unset = UNSET,
    energy_only_bid_price_3_from: float | Unset = UNSET,
    energy_only_bid_price_3_to: float | Unset = UNSET,
    energy_only_bid_mw_4_from: float | Unset = UNSET,
    energy_only_bid_mw_4_to: float | Unset = UNSET,
    energy_only_bid_price_4_from: float | Unset = UNSET,
    energy_only_bid_price_4_to: float | Unset = UNSET,
    energy_only_bid_mw_5_from: float | Unset = UNSET,
    energy_only_bid_mw_5_to: float | Unset = UNSET,
    energy_only_bid_price_5_from: float | Unset = UNSET,
    energy_only_bid_price_5_to: float | Unset = UNSET,
    energy_only_bid_mw_6_from: float | Unset = UNSET,
    energy_only_bid_mw_6_to: float | Unset = UNSET,
    energy_only_bid_price_6_from: float | Unset = UNSET,
    energy_only_bid_price_6_to: float | Unset = UNSET,
    energy_only_bid_mw_7_from: float | Unset = UNSET,
    energy_only_bid_mw_7_to: float | Unset = UNSET,
    energy_only_bid_price_7_from: float | Unset = UNSET,
    energy_only_bid_price_7_to: float | Unset = UNSET,
    energy_only_bid_mw_8_from: float | Unset = UNSET,
    energy_only_bid_mw_8_to: float | Unset = UNSET,
    energy_only_bid_price_8_from: float | Unset = UNSET,
    energy_only_bid_price_8_to: float | Unset = UNSET,
    energy_only_bid_mw_9_from: float | Unset = UNSET,
    energy_only_bid_mw_9_to: float | Unset = UNSET,
    energy_only_bid_price_9_from: float | Unset = UNSET,
    energy_only_bid_price_9_to: float | Unset = UNSET,
    energy_only_bid_mw_10_from: float | Unset = UNSET,
    energy_only_bid_mw_10_to: float | Unset = UNSET,
    energy_only_bid_price_10_from: float | Unset = UNSET,
    energy_only_bid_price_10_to: float | Unset = UNSET,
    bid_id_from: float | Unset = UNSET,
    bid_id_to: float | Unset = UNSET,
    multi_hour_block: bool | Unset = UNSET,
    block_curve: bool | Unset = UNSET,
    delivery_date_from: str | Unset = UNSET,
    delivery_date_to: str | Unset = UNSET,
    hour_ending_from: str | Unset = UNSET,
    hour_ending_to: str | Unset = UNSET,
    settlement_point_name: str | Unset = UNSET,
    qse_name: str | Unset = UNSET,
    page: int | Unset = UNSET,
    size: int | Unset = UNSET,
    sort: str | Unset = UNSET,
    dir_: str | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["energyOnlyBidMw1From"] = energy_only_bid_mw_1_from

    params["energyOnlyBidMw1To"] = energy_only_bid_mw_1_to

    params["energyOnlyBidPrice1From"] = energy_only_bid_price_1_from

    params["energyOnlyBidPrice1To"] = energy_only_bid_price_1_to

    params["energyOnlyBidMw2From"] = energy_only_bid_mw_2_from

    params["energyOnlyBidMw2To"] = energy_only_bid_mw_2_to

    params["energyOnlyBidPrice2From"] = energy_only_bid_price_2_from

    params["energyOnlyBidPrice2To"] = energy_only_bid_price_2_to

    params["energyOnlyBidMw3From"] = energy_only_bid_mw_3_from

    params["energyOnlyBidMw3To"] = energy_only_bid_mw_3_to

    params["energyOnlyBidPrice3From"] = energy_only_bid_price_3_from

    params["energyOnlyBidPrice3To"] = energy_only_bid_price_3_to

    params["energyOnlyBidMw4From"] = energy_only_bid_mw_4_from

    params["energyOnlyBidMw4To"] = energy_only_bid_mw_4_to

    params["energyOnlyBidPrice4From"] = energy_only_bid_price_4_from

    params["energyOnlyBidPrice4To"] = energy_only_bid_price_4_to

    params["energyOnlyBidMw5From"] = energy_only_bid_mw_5_from

    params["energyOnlyBidMw5To"] = energy_only_bid_mw_5_to

    params["energyOnlyBidPrice5From"] = energy_only_bid_price_5_from

    params["energyOnlyBidPrice5To"] = energy_only_bid_price_5_to

    params["energyOnlyBidMw6From"] = energy_only_bid_mw_6_from

    params["energyOnlyBidMw6To"] = energy_only_bid_mw_6_to

    params["energyOnlyBidPrice6From"] = energy_only_bid_price_6_from

    params["energyOnlyBidPrice6To"] = energy_only_bid_price_6_to

    params["energyOnlyBidMw7From"] = energy_only_bid_mw_7_from

    params["energyOnlyBidMw7To"] = energy_only_bid_mw_7_to

    params["energyOnlyBidPrice7From"] = energy_only_bid_price_7_from

    params["energyOnlyBidPrice7To"] = energy_only_bid_price_7_to

    params["energyOnlyBidMw8From"] = energy_only_bid_mw_8_from

    params["energyOnlyBidMw8To"] = energy_only_bid_mw_8_to

    params["energyOnlyBidPrice8From"] = energy_only_bid_price_8_from

    params["energyOnlyBidPrice8To"] = energy_only_bid_price_8_to

    params["energyOnlyBidMw9From"] = energy_only_bid_mw_9_from

    params["energyOnlyBidMw9To"] = energy_only_bid_mw_9_to

    params["energyOnlyBidPrice9From"] = energy_only_bid_price_9_from

    params["energyOnlyBidPrice9To"] = energy_only_bid_price_9_to

    params["energyOnlyBidMw10From"] = energy_only_bid_mw_10_from

    params["energyOnlyBidMw10To"] = energy_only_bid_mw_10_to

    params["energyOnlyBidPrice10From"] = energy_only_bid_price_10_from

    params["energyOnlyBidPrice10To"] = energy_only_bid_price_10_to

    params["bidIdFrom"] = bid_id_from

    params["bidIdTo"] = bid_id_to

    params["multiHourBlock"] = multi_hour_block

    params["blockCurve"] = block_curve

    params["deliveryDateFrom"] = delivery_date_from

    params["deliveryDateTo"] = delivery_date_to

    params["hourEndingFrom"] = hour_ending_from

    params["hourEndingTo"] = hour_ending_to

    params["settlementPointName"] = settlement_point_name

    params["qseName"] = qse_name

    params["page"] = page

    params["size"] = size

    params["sort"] = sort

    params["dir"] = dir_

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/np3-966-er/60_dam_energy_bids",
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
    energy_only_bid_mw_1_from: float | Unset = UNSET,
    energy_only_bid_mw_1_to: float | Unset = UNSET,
    energy_only_bid_price_1_from: float | Unset = UNSET,
    energy_only_bid_price_1_to: float | Unset = UNSET,
    energy_only_bid_mw_2_from: float | Unset = UNSET,
    energy_only_bid_mw_2_to: float | Unset = UNSET,
    energy_only_bid_price_2_from: float | Unset = UNSET,
    energy_only_bid_price_2_to: float | Unset = UNSET,
    energy_only_bid_mw_3_from: float | Unset = UNSET,
    energy_only_bid_mw_3_to: float | Unset = UNSET,
    energy_only_bid_price_3_from: float | Unset = UNSET,
    energy_only_bid_price_3_to: float | Unset = UNSET,
    energy_only_bid_mw_4_from: float | Unset = UNSET,
    energy_only_bid_mw_4_to: float | Unset = UNSET,
    energy_only_bid_price_4_from: float | Unset = UNSET,
    energy_only_bid_price_4_to: float | Unset = UNSET,
    energy_only_bid_mw_5_from: float | Unset = UNSET,
    energy_only_bid_mw_5_to: float | Unset = UNSET,
    energy_only_bid_price_5_from: float | Unset = UNSET,
    energy_only_bid_price_5_to: float | Unset = UNSET,
    energy_only_bid_mw_6_from: float | Unset = UNSET,
    energy_only_bid_mw_6_to: float | Unset = UNSET,
    energy_only_bid_price_6_from: float | Unset = UNSET,
    energy_only_bid_price_6_to: float | Unset = UNSET,
    energy_only_bid_mw_7_from: float | Unset = UNSET,
    energy_only_bid_mw_7_to: float | Unset = UNSET,
    energy_only_bid_price_7_from: float | Unset = UNSET,
    energy_only_bid_price_7_to: float | Unset = UNSET,
    energy_only_bid_mw_8_from: float | Unset = UNSET,
    energy_only_bid_mw_8_to: float | Unset = UNSET,
    energy_only_bid_price_8_from: float | Unset = UNSET,
    energy_only_bid_price_8_to: float | Unset = UNSET,
    energy_only_bid_mw_9_from: float | Unset = UNSET,
    energy_only_bid_mw_9_to: float | Unset = UNSET,
    energy_only_bid_price_9_from: float | Unset = UNSET,
    energy_only_bid_price_9_to: float | Unset = UNSET,
    energy_only_bid_mw_10_from: float | Unset = UNSET,
    energy_only_bid_mw_10_to: float | Unset = UNSET,
    energy_only_bid_price_10_from: float | Unset = UNSET,
    energy_only_bid_price_10_to: float | Unset = UNSET,
    bid_id_from: float | Unset = UNSET,
    bid_id_to: float | Unset = UNSET,
    multi_hour_block: bool | Unset = UNSET,
    block_curve: bool | Unset = UNSET,
    delivery_date_from: str | Unset = UNSET,
    delivery_date_to: str | Unset = UNSET,
    hour_ending_from: str | Unset = UNSET,
    hour_ending_to: str | Unset = UNSET,
    settlement_point_name: str | Unset = UNSET,
    qse_name: str | Unset = UNSET,
    page: int | Unset = UNSET,
    size: int | Unset = UNSET,
    sort: str | Unset = UNSET,
    dir_: str | Unset = UNSET,
) -> Response[Exception_ | Report]:
    """60 Day DAM Energy Bids

     60 Day DAM Energy Bids

    Args:
        energy_only_bid_mw_1_from (float | Unset):
        energy_only_bid_mw_1_to (float | Unset):
        energy_only_bid_price_1_from (float | Unset):
        energy_only_bid_price_1_to (float | Unset):
        energy_only_bid_mw_2_from (float | Unset):
        energy_only_bid_mw_2_to (float | Unset):
        energy_only_bid_price_2_from (float | Unset):
        energy_only_bid_price_2_to (float | Unset):
        energy_only_bid_mw_3_from (float | Unset):
        energy_only_bid_mw_3_to (float | Unset):
        energy_only_bid_price_3_from (float | Unset):
        energy_only_bid_price_3_to (float | Unset):
        energy_only_bid_mw_4_from (float | Unset):
        energy_only_bid_mw_4_to (float | Unset):
        energy_only_bid_price_4_from (float | Unset):
        energy_only_bid_price_4_to (float | Unset):
        energy_only_bid_mw_5_from (float | Unset):
        energy_only_bid_mw_5_to (float | Unset):
        energy_only_bid_price_5_from (float | Unset):
        energy_only_bid_price_5_to (float | Unset):
        energy_only_bid_mw_6_from (float | Unset):
        energy_only_bid_mw_6_to (float | Unset):
        energy_only_bid_price_6_from (float | Unset):
        energy_only_bid_price_6_to (float | Unset):
        energy_only_bid_mw_7_from (float | Unset):
        energy_only_bid_mw_7_to (float | Unset):
        energy_only_bid_price_7_from (float | Unset):
        energy_only_bid_price_7_to (float | Unset):
        energy_only_bid_mw_8_from (float | Unset):
        energy_only_bid_mw_8_to (float | Unset):
        energy_only_bid_price_8_from (float | Unset):
        energy_only_bid_price_8_to (float | Unset):
        energy_only_bid_mw_9_from (float | Unset):
        energy_only_bid_mw_9_to (float | Unset):
        energy_only_bid_price_9_from (float | Unset):
        energy_only_bid_price_9_to (float | Unset):
        energy_only_bid_mw_10_from (float | Unset):
        energy_only_bid_mw_10_to (float | Unset):
        energy_only_bid_price_10_from (float | Unset):
        energy_only_bid_price_10_to (float | Unset):
        bid_id_from (float | Unset):
        bid_id_to (float | Unset):
        multi_hour_block (bool | Unset):
        block_curve (bool | Unset):
        delivery_date_from (str | Unset):
        delivery_date_to (str | Unset):
        hour_ending_from (str | Unset):
        hour_ending_to (str | Unset):
        settlement_point_name (str | Unset):
        qse_name (str | Unset):
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
        energy_only_bid_mw_1_from=energy_only_bid_mw_1_from,
        energy_only_bid_mw_1_to=energy_only_bid_mw_1_to,
        energy_only_bid_price_1_from=energy_only_bid_price_1_from,
        energy_only_bid_price_1_to=energy_only_bid_price_1_to,
        energy_only_bid_mw_2_from=energy_only_bid_mw_2_from,
        energy_only_bid_mw_2_to=energy_only_bid_mw_2_to,
        energy_only_bid_price_2_from=energy_only_bid_price_2_from,
        energy_only_bid_price_2_to=energy_only_bid_price_2_to,
        energy_only_bid_mw_3_from=energy_only_bid_mw_3_from,
        energy_only_bid_mw_3_to=energy_only_bid_mw_3_to,
        energy_only_bid_price_3_from=energy_only_bid_price_3_from,
        energy_only_bid_price_3_to=energy_only_bid_price_3_to,
        energy_only_bid_mw_4_from=energy_only_bid_mw_4_from,
        energy_only_bid_mw_4_to=energy_only_bid_mw_4_to,
        energy_only_bid_price_4_from=energy_only_bid_price_4_from,
        energy_only_bid_price_4_to=energy_only_bid_price_4_to,
        energy_only_bid_mw_5_from=energy_only_bid_mw_5_from,
        energy_only_bid_mw_5_to=energy_only_bid_mw_5_to,
        energy_only_bid_price_5_from=energy_only_bid_price_5_from,
        energy_only_bid_price_5_to=energy_only_bid_price_5_to,
        energy_only_bid_mw_6_from=energy_only_bid_mw_6_from,
        energy_only_bid_mw_6_to=energy_only_bid_mw_6_to,
        energy_only_bid_price_6_from=energy_only_bid_price_6_from,
        energy_only_bid_price_6_to=energy_only_bid_price_6_to,
        energy_only_bid_mw_7_from=energy_only_bid_mw_7_from,
        energy_only_bid_mw_7_to=energy_only_bid_mw_7_to,
        energy_only_bid_price_7_from=energy_only_bid_price_7_from,
        energy_only_bid_price_7_to=energy_only_bid_price_7_to,
        energy_only_bid_mw_8_from=energy_only_bid_mw_8_from,
        energy_only_bid_mw_8_to=energy_only_bid_mw_8_to,
        energy_only_bid_price_8_from=energy_only_bid_price_8_from,
        energy_only_bid_price_8_to=energy_only_bid_price_8_to,
        energy_only_bid_mw_9_from=energy_only_bid_mw_9_from,
        energy_only_bid_mw_9_to=energy_only_bid_mw_9_to,
        energy_only_bid_price_9_from=energy_only_bid_price_9_from,
        energy_only_bid_price_9_to=energy_only_bid_price_9_to,
        energy_only_bid_mw_10_from=energy_only_bid_mw_10_from,
        energy_only_bid_mw_10_to=energy_only_bid_mw_10_to,
        energy_only_bid_price_10_from=energy_only_bid_price_10_from,
        energy_only_bid_price_10_to=energy_only_bid_price_10_to,
        bid_id_from=bid_id_from,
        bid_id_to=bid_id_to,
        multi_hour_block=multi_hour_block,
        block_curve=block_curve,
        delivery_date_from=delivery_date_from,
        delivery_date_to=delivery_date_to,
        hour_ending_from=hour_ending_from,
        hour_ending_to=hour_ending_to,
        settlement_point_name=settlement_point_name,
        qse_name=qse_name,
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
    energy_only_bid_mw_1_from: float | Unset = UNSET,
    energy_only_bid_mw_1_to: float | Unset = UNSET,
    energy_only_bid_price_1_from: float | Unset = UNSET,
    energy_only_bid_price_1_to: float | Unset = UNSET,
    energy_only_bid_mw_2_from: float | Unset = UNSET,
    energy_only_bid_mw_2_to: float | Unset = UNSET,
    energy_only_bid_price_2_from: float | Unset = UNSET,
    energy_only_bid_price_2_to: float | Unset = UNSET,
    energy_only_bid_mw_3_from: float | Unset = UNSET,
    energy_only_bid_mw_3_to: float | Unset = UNSET,
    energy_only_bid_price_3_from: float | Unset = UNSET,
    energy_only_bid_price_3_to: float | Unset = UNSET,
    energy_only_bid_mw_4_from: float | Unset = UNSET,
    energy_only_bid_mw_4_to: float | Unset = UNSET,
    energy_only_bid_price_4_from: float | Unset = UNSET,
    energy_only_bid_price_4_to: float | Unset = UNSET,
    energy_only_bid_mw_5_from: float | Unset = UNSET,
    energy_only_bid_mw_5_to: float | Unset = UNSET,
    energy_only_bid_price_5_from: float | Unset = UNSET,
    energy_only_bid_price_5_to: float | Unset = UNSET,
    energy_only_bid_mw_6_from: float | Unset = UNSET,
    energy_only_bid_mw_6_to: float | Unset = UNSET,
    energy_only_bid_price_6_from: float | Unset = UNSET,
    energy_only_bid_price_6_to: float | Unset = UNSET,
    energy_only_bid_mw_7_from: float | Unset = UNSET,
    energy_only_bid_mw_7_to: float | Unset = UNSET,
    energy_only_bid_price_7_from: float | Unset = UNSET,
    energy_only_bid_price_7_to: float | Unset = UNSET,
    energy_only_bid_mw_8_from: float | Unset = UNSET,
    energy_only_bid_mw_8_to: float | Unset = UNSET,
    energy_only_bid_price_8_from: float | Unset = UNSET,
    energy_only_bid_price_8_to: float | Unset = UNSET,
    energy_only_bid_mw_9_from: float | Unset = UNSET,
    energy_only_bid_mw_9_to: float | Unset = UNSET,
    energy_only_bid_price_9_from: float | Unset = UNSET,
    energy_only_bid_price_9_to: float | Unset = UNSET,
    energy_only_bid_mw_10_from: float | Unset = UNSET,
    energy_only_bid_mw_10_to: float | Unset = UNSET,
    energy_only_bid_price_10_from: float | Unset = UNSET,
    energy_only_bid_price_10_to: float | Unset = UNSET,
    bid_id_from: float | Unset = UNSET,
    bid_id_to: float | Unset = UNSET,
    multi_hour_block: bool | Unset = UNSET,
    block_curve: bool | Unset = UNSET,
    delivery_date_from: str | Unset = UNSET,
    delivery_date_to: str | Unset = UNSET,
    hour_ending_from: str | Unset = UNSET,
    hour_ending_to: str | Unset = UNSET,
    settlement_point_name: str | Unset = UNSET,
    qse_name: str | Unset = UNSET,
    page: int | Unset = UNSET,
    size: int | Unset = UNSET,
    sort: str | Unset = UNSET,
    dir_: str | Unset = UNSET,
) -> Exception_ | Report | None:
    """60 Day DAM Energy Bids

     60 Day DAM Energy Bids

    Args:
        energy_only_bid_mw_1_from (float | Unset):
        energy_only_bid_mw_1_to (float | Unset):
        energy_only_bid_price_1_from (float | Unset):
        energy_only_bid_price_1_to (float | Unset):
        energy_only_bid_mw_2_from (float | Unset):
        energy_only_bid_mw_2_to (float | Unset):
        energy_only_bid_price_2_from (float | Unset):
        energy_only_bid_price_2_to (float | Unset):
        energy_only_bid_mw_3_from (float | Unset):
        energy_only_bid_mw_3_to (float | Unset):
        energy_only_bid_price_3_from (float | Unset):
        energy_only_bid_price_3_to (float | Unset):
        energy_only_bid_mw_4_from (float | Unset):
        energy_only_bid_mw_4_to (float | Unset):
        energy_only_bid_price_4_from (float | Unset):
        energy_only_bid_price_4_to (float | Unset):
        energy_only_bid_mw_5_from (float | Unset):
        energy_only_bid_mw_5_to (float | Unset):
        energy_only_bid_price_5_from (float | Unset):
        energy_only_bid_price_5_to (float | Unset):
        energy_only_bid_mw_6_from (float | Unset):
        energy_only_bid_mw_6_to (float | Unset):
        energy_only_bid_price_6_from (float | Unset):
        energy_only_bid_price_6_to (float | Unset):
        energy_only_bid_mw_7_from (float | Unset):
        energy_only_bid_mw_7_to (float | Unset):
        energy_only_bid_price_7_from (float | Unset):
        energy_only_bid_price_7_to (float | Unset):
        energy_only_bid_mw_8_from (float | Unset):
        energy_only_bid_mw_8_to (float | Unset):
        energy_only_bid_price_8_from (float | Unset):
        energy_only_bid_price_8_to (float | Unset):
        energy_only_bid_mw_9_from (float | Unset):
        energy_only_bid_mw_9_to (float | Unset):
        energy_only_bid_price_9_from (float | Unset):
        energy_only_bid_price_9_to (float | Unset):
        energy_only_bid_mw_10_from (float | Unset):
        energy_only_bid_mw_10_to (float | Unset):
        energy_only_bid_price_10_from (float | Unset):
        energy_only_bid_price_10_to (float | Unset):
        bid_id_from (float | Unset):
        bid_id_to (float | Unset):
        multi_hour_block (bool | Unset):
        block_curve (bool | Unset):
        delivery_date_from (str | Unset):
        delivery_date_to (str | Unset):
        hour_ending_from (str | Unset):
        hour_ending_to (str | Unset):
        settlement_point_name (str | Unset):
        qse_name (str | Unset):
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
        energy_only_bid_mw_1_from=energy_only_bid_mw_1_from,
        energy_only_bid_mw_1_to=energy_only_bid_mw_1_to,
        energy_only_bid_price_1_from=energy_only_bid_price_1_from,
        energy_only_bid_price_1_to=energy_only_bid_price_1_to,
        energy_only_bid_mw_2_from=energy_only_bid_mw_2_from,
        energy_only_bid_mw_2_to=energy_only_bid_mw_2_to,
        energy_only_bid_price_2_from=energy_only_bid_price_2_from,
        energy_only_bid_price_2_to=energy_only_bid_price_2_to,
        energy_only_bid_mw_3_from=energy_only_bid_mw_3_from,
        energy_only_bid_mw_3_to=energy_only_bid_mw_3_to,
        energy_only_bid_price_3_from=energy_only_bid_price_3_from,
        energy_only_bid_price_3_to=energy_only_bid_price_3_to,
        energy_only_bid_mw_4_from=energy_only_bid_mw_4_from,
        energy_only_bid_mw_4_to=energy_only_bid_mw_4_to,
        energy_only_bid_price_4_from=energy_only_bid_price_4_from,
        energy_only_bid_price_4_to=energy_only_bid_price_4_to,
        energy_only_bid_mw_5_from=energy_only_bid_mw_5_from,
        energy_only_bid_mw_5_to=energy_only_bid_mw_5_to,
        energy_only_bid_price_5_from=energy_only_bid_price_5_from,
        energy_only_bid_price_5_to=energy_only_bid_price_5_to,
        energy_only_bid_mw_6_from=energy_only_bid_mw_6_from,
        energy_only_bid_mw_6_to=energy_only_bid_mw_6_to,
        energy_only_bid_price_6_from=energy_only_bid_price_6_from,
        energy_only_bid_price_6_to=energy_only_bid_price_6_to,
        energy_only_bid_mw_7_from=energy_only_bid_mw_7_from,
        energy_only_bid_mw_7_to=energy_only_bid_mw_7_to,
        energy_only_bid_price_7_from=energy_only_bid_price_7_from,
        energy_only_bid_price_7_to=energy_only_bid_price_7_to,
        energy_only_bid_mw_8_from=energy_only_bid_mw_8_from,
        energy_only_bid_mw_8_to=energy_only_bid_mw_8_to,
        energy_only_bid_price_8_from=energy_only_bid_price_8_from,
        energy_only_bid_price_8_to=energy_only_bid_price_8_to,
        energy_only_bid_mw_9_from=energy_only_bid_mw_9_from,
        energy_only_bid_mw_9_to=energy_only_bid_mw_9_to,
        energy_only_bid_price_9_from=energy_only_bid_price_9_from,
        energy_only_bid_price_9_to=energy_only_bid_price_9_to,
        energy_only_bid_mw_10_from=energy_only_bid_mw_10_from,
        energy_only_bid_mw_10_to=energy_only_bid_mw_10_to,
        energy_only_bid_price_10_from=energy_only_bid_price_10_from,
        energy_only_bid_price_10_to=energy_only_bid_price_10_to,
        bid_id_from=bid_id_from,
        bid_id_to=bid_id_to,
        multi_hour_block=multi_hour_block,
        block_curve=block_curve,
        delivery_date_from=delivery_date_from,
        delivery_date_to=delivery_date_to,
        hour_ending_from=hour_ending_from,
        hour_ending_to=hour_ending_to,
        settlement_point_name=settlement_point_name,
        qse_name=qse_name,
        page=page,
        size=size,
        sort=sort,
        dir_=dir_,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    energy_only_bid_mw_1_from: float | Unset = UNSET,
    energy_only_bid_mw_1_to: float | Unset = UNSET,
    energy_only_bid_price_1_from: float | Unset = UNSET,
    energy_only_bid_price_1_to: float | Unset = UNSET,
    energy_only_bid_mw_2_from: float | Unset = UNSET,
    energy_only_bid_mw_2_to: float | Unset = UNSET,
    energy_only_bid_price_2_from: float | Unset = UNSET,
    energy_only_bid_price_2_to: float | Unset = UNSET,
    energy_only_bid_mw_3_from: float | Unset = UNSET,
    energy_only_bid_mw_3_to: float | Unset = UNSET,
    energy_only_bid_price_3_from: float | Unset = UNSET,
    energy_only_bid_price_3_to: float | Unset = UNSET,
    energy_only_bid_mw_4_from: float | Unset = UNSET,
    energy_only_bid_mw_4_to: float | Unset = UNSET,
    energy_only_bid_price_4_from: float | Unset = UNSET,
    energy_only_bid_price_4_to: float | Unset = UNSET,
    energy_only_bid_mw_5_from: float | Unset = UNSET,
    energy_only_bid_mw_5_to: float | Unset = UNSET,
    energy_only_bid_price_5_from: float | Unset = UNSET,
    energy_only_bid_price_5_to: float | Unset = UNSET,
    energy_only_bid_mw_6_from: float | Unset = UNSET,
    energy_only_bid_mw_6_to: float | Unset = UNSET,
    energy_only_bid_price_6_from: float | Unset = UNSET,
    energy_only_bid_price_6_to: float | Unset = UNSET,
    energy_only_bid_mw_7_from: float | Unset = UNSET,
    energy_only_bid_mw_7_to: float | Unset = UNSET,
    energy_only_bid_price_7_from: float | Unset = UNSET,
    energy_only_bid_price_7_to: float | Unset = UNSET,
    energy_only_bid_mw_8_from: float | Unset = UNSET,
    energy_only_bid_mw_8_to: float | Unset = UNSET,
    energy_only_bid_price_8_from: float | Unset = UNSET,
    energy_only_bid_price_8_to: float | Unset = UNSET,
    energy_only_bid_mw_9_from: float | Unset = UNSET,
    energy_only_bid_mw_9_to: float | Unset = UNSET,
    energy_only_bid_price_9_from: float | Unset = UNSET,
    energy_only_bid_price_9_to: float | Unset = UNSET,
    energy_only_bid_mw_10_from: float | Unset = UNSET,
    energy_only_bid_mw_10_to: float | Unset = UNSET,
    energy_only_bid_price_10_from: float | Unset = UNSET,
    energy_only_bid_price_10_to: float | Unset = UNSET,
    bid_id_from: float | Unset = UNSET,
    bid_id_to: float | Unset = UNSET,
    multi_hour_block: bool | Unset = UNSET,
    block_curve: bool | Unset = UNSET,
    delivery_date_from: str | Unset = UNSET,
    delivery_date_to: str | Unset = UNSET,
    hour_ending_from: str | Unset = UNSET,
    hour_ending_to: str | Unset = UNSET,
    settlement_point_name: str | Unset = UNSET,
    qse_name: str | Unset = UNSET,
    page: int | Unset = UNSET,
    size: int | Unset = UNSET,
    sort: str | Unset = UNSET,
    dir_: str | Unset = UNSET,
) -> Response[Exception_ | Report]:
    """60 Day DAM Energy Bids

     60 Day DAM Energy Bids

    Args:
        energy_only_bid_mw_1_from (float | Unset):
        energy_only_bid_mw_1_to (float | Unset):
        energy_only_bid_price_1_from (float | Unset):
        energy_only_bid_price_1_to (float | Unset):
        energy_only_bid_mw_2_from (float | Unset):
        energy_only_bid_mw_2_to (float | Unset):
        energy_only_bid_price_2_from (float | Unset):
        energy_only_bid_price_2_to (float | Unset):
        energy_only_bid_mw_3_from (float | Unset):
        energy_only_bid_mw_3_to (float | Unset):
        energy_only_bid_price_3_from (float | Unset):
        energy_only_bid_price_3_to (float | Unset):
        energy_only_bid_mw_4_from (float | Unset):
        energy_only_bid_mw_4_to (float | Unset):
        energy_only_bid_price_4_from (float | Unset):
        energy_only_bid_price_4_to (float | Unset):
        energy_only_bid_mw_5_from (float | Unset):
        energy_only_bid_mw_5_to (float | Unset):
        energy_only_bid_price_5_from (float | Unset):
        energy_only_bid_price_5_to (float | Unset):
        energy_only_bid_mw_6_from (float | Unset):
        energy_only_bid_mw_6_to (float | Unset):
        energy_only_bid_price_6_from (float | Unset):
        energy_only_bid_price_6_to (float | Unset):
        energy_only_bid_mw_7_from (float | Unset):
        energy_only_bid_mw_7_to (float | Unset):
        energy_only_bid_price_7_from (float | Unset):
        energy_only_bid_price_7_to (float | Unset):
        energy_only_bid_mw_8_from (float | Unset):
        energy_only_bid_mw_8_to (float | Unset):
        energy_only_bid_price_8_from (float | Unset):
        energy_only_bid_price_8_to (float | Unset):
        energy_only_bid_mw_9_from (float | Unset):
        energy_only_bid_mw_9_to (float | Unset):
        energy_only_bid_price_9_from (float | Unset):
        energy_only_bid_price_9_to (float | Unset):
        energy_only_bid_mw_10_from (float | Unset):
        energy_only_bid_mw_10_to (float | Unset):
        energy_only_bid_price_10_from (float | Unset):
        energy_only_bid_price_10_to (float | Unset):
        bid_id_from (float | Unset):
        bid_id_to (float | Unset):
        multi_hour_block (bool | Unset):
        block_curve (bool | Unset):
        delivery_date_from (str | Unset):
        delivery_date_to (str | Unset):
        hour_ending_from (str | Unset):
        hour_ending_to (str | Unset):
        settlement_point_name (str | Unset):
        qse_name (str | Unset):
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
        energy_only_bid_mw_1_from=energy_only_bid_mw_1_from,
        energy_only_bid_mw_1_to=energy_only_bid_mw_1_to,
        energy_only_bid_price_1_from=energy_only_bid_price_1_from,
        energy_only_bid_price_1_to=energy_only_bid_price_1_to,
        energy_only_bid_mw_2_from=energy_only_bid_mw_2_from,
        energy_only_bid_mw_2_to=energy_only_bid_mw_2_to,
        energy_only_bid_price_2_from=energy_only_bid_price_2_from,
        energy_only_bid_price_2_to=energy_only_bid_price_2_to,
        energy_only_bid_mw_3_from=energy_only_bid_mw_3_from,
        energy_only_bid_mw_3_to=energy_only_bid_mw_3_to,
        energy_only_bid_price_3_from=energy_only_bid_price_3_from,
        energy_only_bid_price_3_to=energy_only_bid_price_3_to,
        energy_only_bid_mw_4_from=energy_only_bid_mw_4_from,
        energy_only_bid_mw_4_to=energy_only_bid_mw_4_to,
        energy_only_bid_price_4_from=energy_only_bid_price_4_from,
        energy_only_bid_price_4_to=energy_only_bid_price_4_to,
        energy_only_bid_mw_5_from=energy_only_bid_mw_5_from,
        energy_only_bid_mw_5_to=energy_only_bid_mw_5_to,
        energy_only_bid_price_5_from=energy_only_bid_price_5_from,
        energy_only_bid_price_5_to=energy_only_bid_price_5_to,
        energy_only_bid_mw_6_from=energy_only_bid_mw_6_from,
        energy_only_bid_mw_6_to=energy_only_bid_mw_6_to,
        energy_only_bid_price_6_from=energy_only_bid_price_6_from,
        energy_only_bid_price_6_to=energy_only_bid_price_6_to,
        energy_only_bid_mw_7_from=energy_only_bid_mw_7_from,
        energy_only_bid_mw_7_to=energy_only_bid_mw_7_to,
        energy_only_bid_price_7_from=energy_only_bid_price_7_from,
        energy_only_bid_price_7_to=energy_only_bid_price_7_to,
        energy_only_bid_mw_8_from=energy_only_bid_mw_8_from,
        energy_only_bid_mw_8_to=energy_only_bid_mw_8_to,
        energy_only_bid_price_8_from=energy_only_bid_price_8_from,
        energy_only_bid_price_8_to=energy_only_bid_price_8_to,
        energy_only_bid_mw_9_from=energy_only_bid_mw_9_from,
        energy_only_bid_mw_9_to=energy_only_bid_mw_9_to,
        energy_only_bid_price_9_from=energy_only_bid_price_9_from,
        energy_only_bid_price_9_to=energy_only_bid_price_9_to,
        energy_only_bid_mw_10_from=energy_only_bid_mw_10_from,
        energy_only_bid_mw_10_to=energy_only_bid_mw_10_to,
        energy_only_bid_price_10_from=energy_only_bid_price_10_from,
        energy_only_bid_price_10_to=energy_only_bid_price_10_to,
        bid_id_from=bid_id_from,
        bid_id_to=bid_id_to,
        multi_hour_block=multi_hour_block,
        block_curve=block_curve,
        delivery_date_from=delivery_date_from,
        delivery_date_to=delivery_date_to,
        hour_ending_from=hour_ending_from,
        hour_ending_to=hour_ending_to,
        settlement_point_name=settlement_point_name,
        qse_name=qse_name,
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
    energy_only_bid_mw_1_from: float | Unset = UNSET,
    energy_only_bid_mw_1_to: float | Unset = UNSET,
    energy_only_bid_price_1_from: float | Unset = UNSET,
    energy_only_bid_price_1_to: float | Unset = UNSET,
    energy_only_bid_mw_2_from: float | Unset = UNSET,
    energy_only_bid_mw_2_to: float | Unset = UNSET,
    energy_only_bid_price_2_from: float | Unset = UNSET,
    energy_only_bid_price_2_to: float | Unset = UNSET,
    energy_only_bid_mw_3_from: float | Unset = UNSET,
    energy_only_bid_mw_3_to: float | Unset = UNSET,
    energy_only_bid_price_3_from: float | Unset = UNSET,
    energy_only_bid_price_3_to: float | Unset = UNSET,
    energy_only_bid_mw_4_from: float | Unset = UNSET,
    energy_only_bid_mw_4_to: float | Unset = UNSET,
    energy_only_bid_price_4_from: float | Unset = UNSET,
    energy_only_bid_price_4_to: float | Unset = UNSET,
    energy_only_bid_mw_5_from: float | Unset = UNSET,
    energy_only_bid_mw_5_to: float | Unset = UNSET,
    energy_only_bid_price_5_from: float | Unset = UNSET,
    energy_only_bid_price_5_to: float | Unset = UNSET,
    energy_only_bid_mw_6_from: float | Unset = UNSET,
    energy_only_bid_mw_6_to: float | Unset = UNSET,
    energy_only_bid_price_6_from: float | Unset = UNSET,
    energy_only_bid_price_6_to: float | Unset = UNSET,
    energy_only_bid_mw_7_from: float | Unset = UNSET,
    energy_only_bid_mw_7_to: float | Unset = UNSET,
    energy_only_bid_price_7_from: float | Unset = UNSET,
    energy_only_bid_price_7_to: float | Unset = UNSET,
    energy_only_bid_mw_8_from: float | Unset = UNSET,
    energy_only_bid_mw_8_to: float | Unset = UNSET,
    energy_only_bid_price_8_from: float | Unset = UNSET,
    energy_only_bid_price_8_to: float | Unset = UNSET,
    energy_only_bid_mw_9_from: float | Unset = UNSET,
    energy_only_bid_mw_9_to: float | Unset = UNSET,
    energy_only_bid_price_9_from: float | Unset = UNSET,
    energy_only_bid_price_9_to: float | Unset = UNSET,
    energy_only_bid_mw_10_from: float | Unset = UNSET,
    energy_only_bid_mw_10_to: float | Unset = UNSET,
    energy_only_bid_price_10_from: float | Unset = UNSET,
    energy_only_bid_price_10_to: float | Unset = UNSET,
    bid_id_from: float | Unset = UNSET,
    bid_id_to: float | Unset = UNSET,
    multi_hour_block: bool | Unset = UNSET,
    block_curve: bool | Unset = UNSET,
    delivery_date_from: str | Unset = UNSET,
    delivery_date_to: str | Unset = UNSET,
    hour_ending_from: str | Unset = UNSET,
    hour_ending_to: str | Unset = UNSET,
    settlement_point_name: str | Unset = UNSET,
    qse_name: str | Unset = UNSET,
    page: int | Unset = UNSET,
    size: int | Unset = UNSET,
    sort: str | Unset = UNSET,
    dir_: str | Unset = UNSET,
) -> Exception_ | Report | None:
    """60 Day DAM Energy Bids

     60 Day DAM Energy Bids

    Args:
        energy_only_bid_mw_1_from (float | Unset):
        energy_only_bid_mw_1_to (float | Unset):
        energy_only_bid_price_1_from (float | Unset):
        energy_only_bid_price_1_to (float | Unset):
        energy_only_bid_mw_2_from (float | Unset):
        energy_only_bid_mw_2_to (float | Unset):
        energy_only_bid_price_2_from (float | Unset):
        energy_only_bid_price_2_to (float | Unset):
        energy_only_bid_mw_3_from (float | Unset):
        energy_only_bid_mw_3_to (float | Unset):
        energy_only_bid_price_3_from (float | Unset):
        energy_only_bid_price_3_to (float | Unset):
        energy_only_bid_mw_4_from (float | Unset):
        energy_only_bid_mw_4_to (float | Unset):
        energy_only_bid_price_4_from (float | Unset):
        energy_only_bid_price_4_to (float | Unset):
        energy_only_bid_mw_5_from (float | Unset):
        energy_only_bid_mw_5_to (float | Unset):
        energy_only_bid_price_5_from (float | Unset):
        energy_only_bid_price_5_to (float | Unset):
        energy_only_bid_mw_6_from (float | Unset):
        energy_only_bid_mw_6_to (float | Unset):
        energy_only_bid_price_6_from (float | Unset):
        energy_only_bid_price_6_to (float | Unset):
        energy_only_bid_mw_7_from (float | Unset):
        energy_only_bid_mw_7_to (float | Unset):
        energy_only_bid_price_7_from (float | Unset):
        energy_only_bid_price_7_to (float | Unset):
        energy_only_bid_mw_8_from (float | Unset):
        energy_only_bid_mw_8_to (float | Unset):
        energy_only_bid_price_8_from (float | Unset):
        energy_only_bid_price_8_to (float | Unset):
        energy_only_bid_mw_9_from (float | Unset):
        energy_only_bid_mw_9_to (float | Unset):
        energy_only_bid_price_9_from (float | Unset):
        energy_only_bid_price_9_to (float | Unset):
        energy_only_bid_mw_10_from (float | Unset):
        energy_only_bid_mw_10_to (float | Unset):
        energy_only_bid_price_10_from (float | Unset):
        energy_only_bid_price_10_to (float | Unset):
        bid_id_from (float | Unset):
        bid_id_to (float | Unset):
        multi_hour_block (bool | Unset):
        block_curve (bool | Unset):
        delivery_date_from (str | Unset):
        delivery_date_to (str | Unset):
        hour_ending_from (str | Unset):
        hour_ending_to (str | Unset):
        settlement_point_name (str | Unset):
        qse_name (str | Unset):
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
            energy_only_bid_mw_1_from=energy_only_bid_mw_1_from,
            energy_only_bid_mw_1_to=energy_only_bid_mw_1_to,
            energy_only_bid_price_1_from=energy_only_bid_price_1_from,
            energy_only_bid_price_1_to=energy_only_bid_price_1_to,
            energy_only_bid_mw_2_from=energy_only_bid_mw_2_from,
            energy_only_bid_mw_2_to=energy_only_bid_mw_2_to,
            energy_only_bid_price_2_from=energy_only_bid_price_2_from,
            energy_only_bid_price_2_to=energy_only_bid_price_2_to,
            energy_only_bid_mw_3_from=energy_only_bid_mw_3_from,
            energy_only_bid_mw_3_to=energy_only_bid_mw_3_to,
            energy_only_bid_price_3_from=energy_only_bid_price_3_from,
            energy_only_bid_price_3_to=energy_only_bid_price_3_to,
            energy_only_bid_mw_4_from=energy_only_bid_mw_4_from,
            energy_only_bid_mw_4_to=energy_only_bid_mw_4_to,
            energy_only_bid_price_4_from=energy_only_bid_price_4_from,
            energy_only_bid_price_4_to=energy_only_bid_price_4_to,
            energy_only_bid_mw_5_from=energy_only_bid_mw_5_from,
            energy_only_bid_mw_5_to=energy_only_bid_mw_5_to,
            energy_only_bid_price_5_from=energy_only_bid_price_5_from,
            energy_only_bid_price_5_to=energy_only_bid_price_5_to,
            energy_only_bid_mw_6_from=energy_only_bid_mw_6_from,
            energy_only_bid_mw_6_to=energy_only_bid_mw_6_to,
            energy_only_bid_price_6_from=energy_only_bid_price_6_from,
            energy_only_bid_price_6_to=energy_only_bid_price_6_to,
            energy_only_bid_mw_7_from=energy_only_bid_mw_7_from,
            energy_only_bid_mw_7_to=energy_only_bid_mw_7_to,
            energy_only_bid_price_7_from=energy_only_bid_price_7_from,
            energy_only_bid_price_7_to=energy_only_bid_price_7_to,
            energy_only_bid_mw_8_from=energy_only_bid_mw_8_from,
            energy_only_bid_mw_8_to=energy_only_bid_mw_8_to,
            energy_only_bid_price_8_from=energy_only_bid_price_8_from,
            energy_only_bid_price_8_to=energy_only_bid_price_8_to,
            energy_only_bid_mw_9_from=energy_only_bid_mw_9_from,
            energy_only_bid_mw_9_to=energy_only_bid_mw_9_to,
            energy_only_bid_price_9_from=energy_only_bid_price_9_from,
            energy_only_bid_price_9_to=energy_only_bid_price_9_to,
            energy_only_bid_mw_10_from=energy_only_bid_mw_10_from,
            energy_only_bid_mw_10_to=energy_only_bid_mw_10_to,
            energy_only_bid_price_10_from=energy_only_bid_price_10_from,
            energy_only_bid_price_10_to=energy_only_bid_price_10_to,
            bid_id_from=bid_id_from,
            bid_id_to=bid_id_to,
            multi_hour_block=multi_hour_block,
            block_curve=block_curve,
            delivery_date_from=delivery_date_from,
            delivery_date_to=delivery_date_to,
            hour_ending_from=hour_ending_from,
            hour_ending_to=hour_ending_to,
            settlement_point_name=settlement_point_name,
            qse_name=qse_name,
            page=page,
            size=size,
            sort=sort,
            dir_=dir_,
        )
    ).parsed
