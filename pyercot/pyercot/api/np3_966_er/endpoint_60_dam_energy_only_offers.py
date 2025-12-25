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
    settlement_point_name: str | Unset = UNSET,
    qse_name: str | Unset = UNSET,
    energy_only_offer_mw1_from: float | Unset = UNSET,
    energy_only_offer_mw1_to: float | Unset = UNSET,
    energy_only_offer_price_1_from: float | Unset = UNSET,
    energy_only_offer_price_1_to: float | Unset = UNSET,
    energy_only_offer_mw2_from: float | Unset = UNSET,
    energy_only_offer_mw2_to: float | Unset = UNSET,
    energy_only_offer_price_2_from: float | Unset = UNSET,
    energy_only_offer_price_2_to: float | Unset = UNSET,
    energy_only_offer_mw3_from: float | Unset = UNSET,
    energy_only_offer_mw3_to: float | Unset = UNSET,
    energy_only_offer_price_3_from: float | Unset = UNSET,
    energy_only_offer_price_3_to: float | Unset = UNSET,
    energy_only_offer_mw4_from: float | Unset = UNSET,
    energy_only_offer_mw4_to: float | Unset = UNSET,
    energy_only_offer_price_4_from: float | Unset = UNSET,
    energy_only_offer_price_4_to: float | Unset = UNSET,
    energy_only_offer_mw5_from: float | Unset = UNSET,
    energy_only_offer_mw5_to: float | Unset = UNSET,
    energy_only_offer_price_5_from: float | Unset = UNSET,
    energy_only_offer_price_5_to: float | Unset = UNSET,
    energy_only_offer_mw6_from: float | Unset = UNSET,
    energy_only_offer_mw6_to: float | Unset = UNSET,
    energy_only_offer_price_6_from: float | Unset = UNSET,
    energy_only_offer_price_6_to: float | Unset = UNSET,
    energy_only_offer_mw7_from: float | Unset = UNSET,
    energy_only_offer_mw7_to: float | Unset = UNSET,
    energy_only_offer_price_7_from: float | Unset = UNSET,
    energy_only_offer_price_7_to: float | Unset = UNSET,
    energy_only_offer_mw8_from: float | Unset = UNSET,
    energy_only_offer_mw8_to: float | Unset = UNSET,
    energy_only_offer_price_8_from: float | Unset = UNSET,
    energy_only_offer_price_8_to: float | Unset = UNSET,
    energy_only_offer_mw9_from: float | Unset = UNSET,
    energy_only_offer_mw9_to: float | Unset = UNSET,
    energy_only_offer_price_9_from: float | Unset = UNSET,
    energy_only_offer_price_9_to: float | Unset = UNSET,
    energy_only_offer_mw10_from: float | Unset = UNSET,
    energy_only_offer_mw10_to: float | Unset = UNSET,
    energy_only_offer_price_10_from: float | Unset = UNSET,
    energy_only_offer_price_10_to: float | Unset = UNSET,
    offer_id_from: float | Unset = UNSET,
    offer_id_to: float | Unset = UNSET,
    multi_hour_block: bool | Unset = UNSET,
    block_curve: bool | Unset = UNSET,
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

    params["settlementPointName"] = settlement_point_name

    params["qseName"] = qse_name

    params["energyOnlyOfferMW1From"] = energy_only_offer_mw1_from

    params["energyOnlyOfferMW1To"] = energy_only_offer_mw1_to

    params["energyOnlyOfferPrice1From"] = energy_only_offer_price_1_from

    params["energyOnlyOfferPrice1To"] = energy_only_offer_price_1_to

    params["energyOnlyOfferMW2From"] = energy_only_offer_mw2_from

    params["energyOnlyOfferMW2To"] = energy_only_offer_mw2_to

    params["energyOnlyOfferPrice2From"] = energy_only_offer_price_2_from

    params["energyOnlyOfferPrice2To"] = energy_only_offer_price_2_to

    params["energyOnlyOfferMW3From"] = energy_only_offer_mw3_from

    params["energyOnlyOfferMW3To"] = energy_only_offer_mw3_to

    params["energyOnlyOfferPrice3From"] = energy_only_offer_price_3_from

    params["energyOnlyOfferPrice3To"] = energy_only_offer_price_3_to

    params["energyOnlyOfferMW4From"] = energy_only_offer_mw4_from

    params["energyOnlyOfferMW4To"] = energy_only_offer_mw4_to

    params["energyOnlyOfferPrice4From"] = energy_only_offer_price_4_from

    params["energyOnlyOfferPrice4To"] = energy_only_offer_price_4_to

    params["energyOnlyOfferMW5From"] = energy_only_offer_mw5_from

    params["energyOnlyOfferMW5To"] = energy_only_offer_mw5_to

    params["energyOnlyOfferPrice5From"] = energy_only_offer_price_5_from

    params["energyOnlyOfferPrice5To"] = energy_only_offer_price_5_to

    params["energyOnlyOfferMW6From"] = energy_only_offer_mw6_from

    params["energyOnlyOfferMW6To"] = energy_only_offer_mw6_to

    params["energyOnlyOfferPrice6From"] = energy_only_offer_price_6_from

    params["energyOnlyOfferPrice6To"] = energy_only_offer_price_6_to

    params["energyOnlyOfferMW7From"] = energy_only_offer_mw7_from

    params["energyOnlyOfferMW7To"] = energy_only_offer_mw7_to

    params["energyOnlyOfferPrice7From"] = energy_only_offer_price_7_from

    params["energyOnlyOfferPrice7To"] = energy_only_offer_price_7_to

    params["energyOnlyOfferMW8From"] = energy_only_offer_mw8_from

    params["energyOnlyOfferMW8To"] = energy_only_offer_mw8_to

    params["energyOnlyOfferPrice8From"] = energy_only_offer_price_8_from

    params["energyOnlyOfferPrice8To"] = energy_only_offer_price_8_to

    params["energyOnlyOfferMW9From"] = energy_only_offer_mw9_from

    params["energyOnlyOfferMW9To"] = energy_only_offer_mw9_to

    params["energyOnlyOfferPrice9From"] = energy_only_offer_price_9_from

    params["energyOnlyOfferPrice9To"] = energy_only_offer_price_9_to

    params["energyOnlyOfferMW10From"] = energy_only_offer_mw10_from

    params["energyOnlyOfferMW10To"] = energy_only_offer_mw10_to

    params["energyOnlyOfferPrice10From"] = energy_only_offer_price_10_from

    params["energyOnlyOfferPrice10To"] = energy_only_offer_price_10_to

    params["offerIdFrom"] = offer_id_from

    params["offerIdTo"] = offer_id_to

    params["multiHourBlock"] = multi_hour_block

    params["blockCurve"] = block_curve

    params["page"] = page

    params["size"] = size

    params["sort"] = sort

    params["dir"] = dir_

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/np3-966-er/60_dam_energy_only_offers",
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
    settlement_point_name: str | Unset = UNSET,
    qse_name: str | Unset = UNSET,
    energy_only_offer_mw1_from: float | Unset = UNSET,
    energy_only_offer_mw1_to: float | Unset = UNSET,
    energy_only_offer_price_1_from: float | Unset = UNSET,
    energy_only_offer_price_1_to: float | Unset = UNSET,
    energy_only_offer_mw2_from: float | Unset = UNSET,
    energy_only_offer_mw2_to: float | Unset = UNSET,
    energy_only_offer_price_2_from: float | Unset = UNSET,
    energy_only_offer_price_2_to: float | Unset = UNSET,
    energy_only_offer_mw3_from: float | Unset = UNSET,
    energy_only_offer_mw3_to: float | Unset = UNSET,
    energy_only_offer_price_3_from: float | Unset = UNSET,
    energy_only_offer_price_3_to: float | Unset = UNSET,
    energy_only_offer_mw4_from: float | Unset = UNSET,
    energy_only_offer_mw4_to: float | Unset = UNSET,
    energy_only_offer_price_4_from: float | Unset = UNSET,
    energy_only_offer_price_4_to: float | Unset = UNSET,
    energy_only_offer_mw5_from: float | Unset = UNSET,
    energy_only_offer_mw5_to: float | Unset = UNSET,
    energy_only_offer_price_5_from: float | Unset = UNSET,
    energy_only_offer_price_5_to: float | Unset = UNSET,
    energy_only_offer_mw6_from: float | Unset = UNSET,
    energy_only_offer_mw6_to: float | Unset = UNSET,
    energy_only_offer_price_6_from: float | Unset = UNSET,
    energy_only_offer_price_6_to: float | Unset = UNSET,
    energy_only_offer_mw7_from: float | Unset = UNSET,
    energy_only_offer_mw7_to: float | Unset = UNSET,
    energy_only_offer_price_7_from: float | Unset = UNSET,
    energy_only_offer_price_7_to: float | Unset = UNSET,
    energy_only_offer_mw8_from: float | Unset = UNSET,
    energy_only_offer_mw8_to: float | Unset = UNSET,
    energy_only_offer_price_8_from: float | Unset = UNSET,
    energy_only_offer_price_8_to: float | Unset = UNSET,
    energy_only_offer_mw9_from: float | Unset = UNSET,
    energy_only_offer_mw9_to: float | Unset = UNSET,
    energy_only_offer_price_9_from: float | Unset = UNSET,
    energy_only_offer_price_9_to: float | Unset = UNSET,
    energy_only_offer_mw10_from: float | Unset = UNSET,
    energy_only_offer_mw10_to: float | Unset = UNSET,
    energy_only_offer_price_10_from: float | Unset = UNSET,
    energy_only_offer_price_10_to: float | Unset = UNSET,
    offer_id_from: float | Unset = UNSET,
    offer_id_to: float | Unset = UNSET,
    multi_hour_block: bool | Unset = UNSET,
    block_curve: bool | Unset = UNSET,
    page: int | Unset = UNSET,
    size: int | Unset = UNSET,
    sort: str | Unset = UNSET,
    dir_: str | Unset = UNSET,
) -> Response[Exception_ | Report]:
    """60 Day DAM Energy Only Offers

     60 Day DAM Energy Only Offers

    Args:
        delivery_date_from (str | Unset):
        delivery_date_to (str | Unset):
        hour_ending_from (str | Unset):
        hour_ending_to (str | Unset):
        settlement_point_name (str | Unset):
        qse_name (str | Unset):
        energy_only_offer_mw1_from (float | Unset):
        energy_only_offer_mw1_to (float | Unset):
        energy_only_offer_price_1_from (float | Unset):
        energy_only_offer_price_1_to (float | Unset):
        energy_only_offer_mw2_from (float | Unset):
        energy_only_offer_mw2_to (float | Unset):
        energy_only_offer_price_2_from (float | Unset):
        energy_only_offer_price_2_to (float | Unset):
        energy_only_offer_mw3_from (float | Unset):
        energy_only_offer_mw3_to (float | Unset):
        energy_only_offer_price_3_from (float | Unset):
        energy_only_offer_price_3_to (float | Unset):
        energy_only_offer_mw4_from (float | Unset):
        energy_only_offer_mw4_to (float | Unset):
        energy_only_offer_price_4_from (float | Unset):
        energy_only_offer_price_4_to (float | Unset):
        energy_only_offer_mw5_from (float | Unset):
        energy_only_offer_mw5_to (float | Unset):
        energy_only_offer_price_5_from (float | Unset):
        energy_only_offer_price_5_to (float | Unset):
        energy_only_offer_mw6_from (float | Unset):
        energy_only_offer_mw6_to (float | Unset):
        energy_only_offer_price_6_from (float | Unset):
        energy_only_offer_price_6_to (float | Unset):
        energy_only_offer_mw7_from (float | Unset):
        energy_only_offer_mw7_to (float | Unset):
        energy_only_offer_price_7_from (float | Unset):
        energy_only_offer_price_7_to (float | Unset):
        energy_only_offer_mw8_from (float | Unset):
        energy_only_offer_mw8_to (float | Unset):
        energy_only_offer_price_8_from (float | Unset):
        energy_only_offer_price_8_to (float | Unset):
        energy_only_offer_mw9_from (float | Unset):
        energy_only_offer_mw9_to (float | Unset):
        energy_only_offer_price_9_from (float | Unset):
        energy_only_offer_price_9_to (float | Unset):
        energy_only_offer_mw10_from (float | Unset):
        energy_only_offer_mw10_to (float | Unset):
        energy_only_offer_price_10_from (float | Unset):
        energy_only_offer_price_10_to (float | Unset):
        offer_id_from (float | Unset):
        offer_id_to (float | Unset):
        multi_hour_block (bool | Unset):
        block_curve (bool | Unset):
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
        settlement_point_name=settlement_point_name,
        qse_name=qse_name,
        energy_only_offer_mw1_from=energy_only_offer_mw1_from,
        energy_only_offer_mw1_to=energy_only_offer_mw1_to,
        energy_only_offer_price_1_from=energy_only_offer_price_1_from,
        energy_only_offer_price_1_to=energy_only_offer_price_1_to,
        energy_only_offer_mw2_from=energy_only_offer_mw2_from,
        energy_only_offer_mw2_to=energy_only_offer_mw2_to,
        energy_only_offer_price_2_from=energy_only_offer_price_2_from,
        energy_only_offer_price_2_to=energy_only_offer_price_2_to,
        energy_only_offer_mw3_from=energy_only_offer_mw3_from,
        energy_only_offer_mw3_to=energy_only_offer_mw3_to,
        energy_only_offer_price_3_from=energy_only_offer_price_3_from,
        energy_only_offer_price_3_to=energy_only_offer_price_3_to,
        energy_only_offer_mw4_from=energy_only_offer_mw4_from,
        energy_only_offer_mw4_to=energy_only_offer_mw4_to,
        energy_only_offer_price_4_from=energy_only_offer_price_4_from,
        energy_only_offer_price_4_to=energy_only_offer_price_4_to,
        energy_only_offer_mw5_from=energy_only_offer_mw5_from,
        energy_only_offer_mw5_to=energy_only_offer_mw5_to,
        energy_only_offer_price_5_from=energy_only_offer_price_5_from,
        energy_only_offer_price_5_to=energy_only_offer_price_5_to,
        energy_only_offer_mw6_from=energy_only_offer_mw6_from,
        energy_only_offer_mw6_to=energy_only_offer_mw6_to,
        energy_only_offer_price_6_from=energy_only_offer_price_6_from,
        energy_only_offer_price_6_to=energy_only_offer_price_6_to,
        energy_only_offer_mw7_from=energy_only_offer_mw7_from,
        energy_only_offer_mw7_to=energy_only_offer_mw7_to,
        energy_only_offer_price_7_from=energy_only_offer_price_7_from,
        energy_only_offer_price_7_to=energy_only_offer_price_7_to,
        energy_only_offer_mw8_from=energy_only_offer_mw8_from,
        energy_only_offer_mw8_to=energy_only_offer_mw8_to,
        energy_only_offer_price_8_from=energy_only_offer_price_8_from,
        energy_only_offer_price_8_to=energy_only_offer_price_8_to,
        energy_only_offer_mw9_from=energy_only_offer_mw9_from,
        energy_only_offer_mw9_to=energy_only_offer_mw9_to,
        energy_only_offer_price_9_from=energy_only_offer_price_9_from,
        energy_only_offer_price_9_to=energy_only_offer_price_9_to,
        energy_only_offer_mw10_from=energy_only_offer_mw10_from,
        energy_only_offer_mw10_to=energy_only_offer_mw10_to,
        energy_only_offer_price_10_from=energy_only_offer_price_10_from,
        energy_only_offer_price_10_to=energy_only_offer_price_10_to,
        offer_id_from=offer_id_from,
        offer_id_to=offer_id_to,
        multi_hour_block=multi_hour_block,
        block_curve=block_curve,
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
    settlement_point_name: str | Unset = UNSET,
    qse_name: str | Unset = UNSET,
    energy_only_offer_mw1_from: float | Unset = UNSET,
    energy_only_offer_mw1_to: float | Unset = UNSET,
    energy_only_offer_price_1_from: float | Unset = UNSET,
    energy_only_offer_price_1_to: float | Unset = UNSET,
    energy_only_offer_mw2_from: float | Unset = UNSET,
    energy_only_offer_mw2_to: float | Unset = UNSET,
    energy_only_offer_price_2_from: float | Unset = UNSET,
    energy_only_offer_price_2_to: float | Unset = UNSET,
    energy_only_offer_mw3_from: float | Unset = UNSET,
    energy_only_offer_mw3_to: float | Unset = UNSET,
    energy_only_offer_price_3_from: float | Unset = UNSET,
    energy_only_offer_price_3_to: float | Unset = UNSET,
    energy_only_offer_mw4_from: float | Unset = UNSET,
    energy_only_offer_mw4_to: float | Unset = UNSET,
    energy_only_offer_price_4_from: float | Unset = UNSET,
    energy_only_offer_price_4_to: float | Unset = UNSET,
    energy_only_offer_mw5_from: float | Unset = UNSET,
    energy_only_offer_mw5_to: float | Unset = UNSET,
    energy_only_offer_price_5_from: float | Unset = UNSET,
    energy_only_offer_price_5_to: float | Unset = UNSET,
    energy_only_offer_mw6_from: float | Unset = UNSET,
    energy_only_offer_mw6_to: float | Unset = UNSET,
    energy_only_offer_price_6_from: float | Unset = UNSET,
    energy_only_offer_price_6_to: float | Unset = UNSET,
    energy_only_offer_mw7_from: float | Unset = UNSET,
    energy_only_offer_mw7_to: float | Unset = UNSET,
    energy_only_offer_price_7_from: float | Unset = UNSET,
    energy_only_offer_price_7_to: float | Unset = UNSET,
    energy_only_offer_mw8_from: float | Unset = UNSET,
    energy_only_offer_mw8_to: float | Unset = UNSET,
    energy_only_offer_price_8_from: float | Unset = UNSET,
    energy_only_offer_price_8_to: float | Unset = UNSET,
    energy_only_offer_mw9_from: float | Unset = UNSET,
    energy_only_offer_mw9_to: float | Unset = UNSET,
    energy_only_offer_price_9_from: float | Unset = UNSET,
    energy_only_offer_price_9_to: float | Unset = UNSET,
    energy_only_offer_mw10_from: float | Unset = UNSET,
    energy_only_offer_mw10_to: float | Unset = UNSET,
    energy_only_offer_price_10_from: float | Unset = UNSET,
    energy_only_offer_price_10_to: float | Unset = UNSET,
    offer_id_from: float | Unset = UNSET,
    offer_id_to: float | Unset = UNSET,
    multi_hour_block: bool | Unset = UNSET,
    block_curve: bool | Unset = UNSET,
    page: int | Unset = UNSET,
    size: int | Unset = UNSET,
    sort: str | Unset = UNSET,
    dir_: str | Unset = UNSET,
) -> Exception_ | Report | None:
    """60 Day DAM Energy Only Offers

     60 Day DAM Energy Only Offers

    Args:
        delivery_date_from (str | Unset):
        delivery_date_to (str | Unset):
        hour_ending_from (str | Unset):
        hour_ending_to (str | Unset):
        settlement_point_name (str | Unset):
        qse_name (str | Unset):
        energy_only_offer_mw1_from (float | Unset):
        energy_only_offer_mw1_to (float | Unset):
        energy_only_offer_price_1_from (float | Unset):
        energy_only_offer_price_1_to (float | Unset):
        energy_only_offer_mw2_from (float | Unset):
        energy_only_offer_mw2_to (float | Unset):
        energy_only_offer_price_2_from (float | Unset):
        energy_only_offer_price_2_to (float | Unset):
        energy_only_offer_mw3_from (float | Unset):
        energy_only_offer_mw3_to (float | Unset):
        energy_only_offer_price_3_from (float | Unset):
        energy_only_offer_price_3_to (float | Unset):
        energy_only_offer_mw4_from (float | Unset):
        energy_only_offer_mw4_to (float | Unset):
        energy_only_offer_price_4_from (float | Unset):
        energy_only_offer_price_4_to (float | Unset):
        energy_only_offer_mw5_from (float | Unset):
        energy_only_offer_mw5_to (float | Unset):
        energy_only_offer_price_5_from (float | Unset):
        energy_only_offer_price_5_to (float | Unset):
        energy_only_offer_mw6_from (float | Unset):
        energy_only_offer_mw6_to (float | Unset):
        energy_only_offer_price_6_from (float | Unset):
        energy_only_offer_price_6_to (float | Unset):
        energy_only_offer_mw7_from (float | Unset):
        energy_only_offer_mw7_to (float | Unset):
        energy_only_offer_price_7_from (float | Unset):
        energy_only_offer_price_7_to (float | Unset):
        energy_only_offer_mw8_from (float | Unset):
        energy_only_offer_mw8_to (float | Unset):
        energy_only_offer_price_8_from (float | Unset):
        energy_only_offer_price_8_to (float | Unset):
        energy_only_offer_mw9_from (float | Unset):
        energy_only_offer_mw9_to (float | Unset):
        energy_only_offer_price_9_from (float | Unset):
        energy_only_offer_price_9_to (float | Unset):
        energy_only_offer_mw10_from (float | Unset):
        energy_only_offer_mw10_to (float | Unset):
        energy_only_offer_price_10_from (float | Unset):
        energy_only_offer_price_10_to (float | Unset):
        offer_id_from (float | Unset):
        offer_id_to (float | Unset):
        multi_hour_block (bool | Unset):
        block_curve (bool | Unset):
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
        settlement_point_name=settlement_point_name,
        qse_name=qse_name,
        energy_only_offer_mw1_from=energy_only_offer_mw1_from,
        energy_only_offer_mw1_to=energy_only_offer_mw1_to,
        energy_only_offer_price_1_from=energy_only_offer_price_1_from,
        energy_only_offer_price_1_to=energy_only_offer_price_1_to,
        energy_only_offer_mw2_from=energy_only_offer_mw2_from,
        energy_only_offer_mw2_to=energy_only_offer_mw2_to,
        energy_only_offer_price_2_from=energy_only_offer_price_2_from,
        energy_only_offer_price_2_to=energy_only_offer_price_2_to,
        energy_only_offer_mw3_from=energy_only_offer_mw3_from,
        energy_only_offer_mw3_to=energy_only_offer_mw3_to,
        energy_only_offer_price_3_from=energy_only_offer_price_3_from,
        energy_only_offer_price_3_to=energy_only_offer_price_3_to,
        energy_only_offer_mw4_from=energy_only_offer_mw4_from,
        energy_only_offer_mw4_to=energy_only_offer_mw4_to,
        energy_only_offer_price_4_from=energy_only_offer_price_4_from,
        energy_only_offer_price_4_to=energy_only_offer_price_4_to,
        energy_only_offer_mw5_from=energy_only_offer_mw5_from,
        energy_only_offer_mw5_to=energy_only_offer_mw5_to,
        energy_only_offer_price_5_from=energy_only_offer_price_5_from,
        energy_only_offer_price_5_to=energy_only_offer_price_5_to,
        energy_only_offer_mw6_from=energy_only_offer_mw6_from,
        energy_only_offer_mw6_to=energy_only_offer_mw6_to,
        energy_only_offer_price_6_from=energy_only_offer_price_6_from,
        energy_only_offer_price_6_to=energy_only_offer_price_6_to,
        energy_only_offer_mw7_from=energy_only_offer_mw7_from,
        energy_only_offer_mw7_to=energy_only_offer_mw7_to,
        energy_only_offer_price_7_from=energy_only_offer_price_7_from,
        energy_only_offer_price_7_to=energy_only_offer_price_7_to,
        energy_only_offer_mw8_from=energy_only_offer_mw8_from,
        energy_only_offer_mw8_to=energy_only_offer_mw8_to,
        energy_only_offer_price_8_from=energy_only_offer_price_8_from,
        energy_only_offer_price_8_to=energy_only_offer_price_8_to,
        energy_only_offer_mw9_from=energy_only_offer_mw9_from,
        energy_only_offer_mw9_to=energy_only_offer_mw9_to,
        energy_only_offer_price_9_from=energy_only_offer_price_9_from,
        energy_only_offer_price_9_to=energy_only_offer_price_9_to,
        energy_only_offer_mw10_from=energy_only_offer_mw10_from,
        energy_only_offer_mw10_to=energy_only_offer_mw10_to,
        energy_only_offer_price_10_from=energy_only_offer_price_10_from,
        energy_only_offer_price_10_to=energy_only_offer_price_10_to,
        offer_id_from=offer_id_from,
        offer_id_to=offer_id_to,
        multi_hour_block=multi_hour_block,
        block_curve=block_curve,
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
    settlement_point_name: str | Unset = UNSET,
    qse_name: str | Unset = UNSET,
    energy_only_offer_mw1_from: float | Unset = UNSET,
    energy_only_offer_mw1_to: float | Unset = UNSET,
    energy_only_offer_price_1_from: float | Unset = UNSET,
    energy_only_offer_price_1_to: float | Unset = UNSET,
    energy_only_offer_mw2_from: float | Unset = UNSET,
    energy_only_offer_mw2_to: float | Unset = UNSET,
    energy_only_offer_price_2_from: float | Unset = UNSET,
    energy_only_offer_price_2_to: float | Unset = UNSET,
    energy_only_offer_mw3_from: float | Unset = UNSET,
    energy_only_offer_mw3_to: float | Unset = UNSET,
    energy_only_offer_price_3_from: float | Unset = UNSET,
    energy_only_offer_price_3_to: float | Unset = UNSET,
    energy_only_offer_mw4_from: float | Unset = UNSET,
    energy_only_offer_mw4_to: float | Unset = UNSET,
    energy_only_offer_price_4_from: float | Unset = UNSET,
    energy_only_offer_price_4_to: float | Unset = UNSET,
    energy_only_offer_mw5_from: float | Unset = UNSET,
    energy_only_offer_mw5_to: float | Unset = UNSET,
    energy_only_offer_price_5_from: float | Unset = UNSET,
    energy_only_offer_price_5_to: float | Unset = UNSET,
    energy_only_offer_mw6_from: float | Unset = UNSET,
    energy_only_offer_mw6_to: float | Unset = UNSET,
    energy_only_offer_price_6_from: float | Unset = UNSET,
    energy_only_offer_price_6_to: float | Unset = UNSET,
    energy_only_offer_mw7_from: float | Unset = UNSET,
    energy_only_offer_mw7_to: float | Unset = UNSET,
    energy_only_offer_price_7_from: float | Unset = UNSET,
    energy_only_offer_price_7_to: float | Unset = UNSET,
    energy_only_offer_mw8_from: float | Unset = UNSET,
    energy_only_offer_mw8_to: float | Unset = UNSET,
    energy_only_offer_price_8_from: float | Unset = UNSET,
    energy_only_offer_price_8_to: float | Unset = UNSET,
    energy_only_offer_mw9_from: float | Unset = UNSET,
    energy_only_offer_mw9_to: float | Unset = UNSET,
    energy_only_offer_price_9_from: float | Unset = UNSET,
    energy_only_offer_price_9_to: float | Unset = UNSET,
    energy_only_offer_mw10_from: float | Unset = UNSET,
    energy_only_offer_mw10_to: float | Unset = UNSET,
    energy_only_offer_price_10_from: float | Unset = UNSET,
    energy_only_offer_price_10_to: float | Unset = UNSET,
    offer_id_from: float | Unset = UNSET,
    offer_id_to: float | Unset = UNSET,
    multi_hour_block: bool | Unset = UNSET,
    block_curve: bool | Unset = UNSET,
    page: int | Unset = UNSET,
    size: int | Unset = UNSET,
    sort: str | Unset = UNSET,
    dir_: str | Unset = UNSET,
) -> Response[Exception_ | Report]:
    """60 Day DAM Energy Only Offers

     60 Day DAM Energy Only Offers

    Args:
        delivery_date_from (str | Unset):
        delivery_date_to (str | Unset):
        hour_ending_from (str | Unset):
        hour_ending_to (str | Unset):
        settlement_point_name (str | Unset):
        qse_name (str | Unset):
        energy_only_offer_mw1_from (float | Unset):
        energy_only_offer_mw1_to (float | Unset):
        energy_only_offer_price_1_from (float | Unset):
        energy_only_offer_price_1_to (float | Unset):
        energy_only_offer_mw2_from (float | Unset):
        energy_only_offer_mw2_to (float | Unset):
        energy_only_offer_price_2_from (float | Unset):
        energy_only_offer_price_2_to (float | Unset):
        energy_only_offer_mw3_from (float | Unset):
        energy_only_offer_mw3_to (float | Unset):
        energy_only_offer_price_3_from (float | Unset):
        energy_only_offer_price_3_to (float | Unset):
        energy_only_offer_mw4_from (float | Unset):
        energy_only_offer_mw4_to (float | Unset):
        energy_only_offer_price_4_from (float | Unset):
        energy_only_offer_price_4_to (float | Unset):
        energy_only_offer_mw5_from (float | Unset):
        energy_only_offer_mw5_to (float | Unset):
        energy_only_offer_price_5_from (float | Unset):
        energy_only_offer_price_5_to (float | Unset):
        energy_only_offer_mw6_from (float | Unset):
        energy_only_offer_mw6_to (float | Unset):
        energy_only_offer_price_6_from (float | Unset):
        energy_only_offer_price_6_to (float | Unset):
        energy_only_offer_mw7_from (float | Unset):
        energy_only_offer_mw7_to (float | Unset):
        energy_only_offer_price_7_from (float | Unset):
        energy_only_offer_price_7_to (float | Unset):
        energy_only_offer_mw8_from (float | Unset):
        energy_only_offer_mw8_to (float | Unset):
        energy_only_offer_price_8_from (float | Unset):
        energy_only_offer_price_8_to (float | Unset):
        energy_only_offer_mw9_from (float | Unset):
        energy_only_offer_mw9_to (float | Unset):
        energy_only_offer_price_9_from (float | Unset):
        energy_only_offer_price_9_to (float | Unset):
        energy_only_offer_mw10_from (float | Unset):
        energy_only_offer_mw10_to (float | Unset):
        energy_only_offer_price_10_from (float | Unset):
        energy_only_offer_price_10_to (float | Unset):
        offer_id_from (float | Unset):
        offer_id_to (float | Unset):
        multi_hour_block (bool | Unset):
        block_curve (bool | Unset):
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
        settlement_point_name=settlement_point_name,
        qse_name=qse_name,
        energy_only_offer_mw1_from=energy_only_offer_mw1_from,
        energy_only_offer_mw1_to=energy_only_offer_mw1_to,
        energy_only_offer_price_1_from=energy_only_offer_price_1_from,
        energy_only_offer_price_1_to=energy_only_offer_price_1_to,
        energy_only_offer_mw2_from=energy_only_offer_mw2_from,
        energy_only_offer_mw2_to=energy_only_offer_mw2_to,
        energy_only_offer_price_2_from=energy_only_offer_price_2_from,
        energy_only_offer_price_2_to=energy_only_offer_price_2_to,
        energy_only_offer_mw3_from=energy_only_offer_mw3_from,
        energy_only_offer_mw3_to=energy_only_offer_mw3_to,
        energy_only_offer_price_3_from=energy_only_offer_price_3_from,
        energy_only_offer_price_3_to=energy_only_offer_price_3_to,
        energy_only_offer_mw4_from=energy_only_offer_mw4_from,
        energy_only_offer_mw4_to=energy_only_offer_mw4_to,
        energy_only_offer_price_4_from=energy_only_offer_price_4_from,
        energy_only_offer_price_4_to=energy_only_offer_price_4_to,
        energy_only_offer_mw5_from=energy_only_offer_mw5_from,
        energy_only_offer_mw5_to=energy_only_offer_mw5_to,
        energy_only_offer_price_5_from=energy_only_offer_price_5_from,
        energy_only_offer_price_5_to=energy_only_offer_price_5_to,
        energy_only_offer_mw6_from=energy_only_offer_mw6_from,
        energy_only_offer_mw6_to=energy_only_offer_mw6_to,
        energy_only_offer_price_6_from=energy_only_offer_price_6_from,
        energy_only_offer_price_6_to=energy_only_offer_price_6_to,
        energy_only_offer_mw7_from=energy_only_offer_mw7_from,
        energy_only_offer_mw7_to=energy_only_offer_mw7_to,
        energy_only_offer_price_7_from=energy_only_offer_price_7_from,
        energy_only_offer_price_7_to=energy_only_offer_price_7_to,
        energy_only_offer_mw8_from=energy_only_offer_mw8_from,
        energy_only_offer_mw8_to=energy_only_offer_mw8_to,
        energy_only_offer_price_8_from=energy_only_offer_price_8_from,
        energy_only_offer_price_8_to=energy_only_offer_price_8_to,
        energy_only_offer_mw9_from=energy_only_offer_mw9_from,
        energy_only_offer_mw9_to=energy_only_offer_mw9_to,
        energy_only_offer_price_9_from=energy_only_offer_price_9_from,
        energy_only_offer_price_9_to=energy_only_offer_price_9_to,
        energy_only_offer_mw10_from=energy_only_offer_mw10_from,
        energy_only_offer_mw10_to=energy_only_offer_mw10_to,
        energy_only_offer_price_10_from=energy_only_offer_price_10_from,
        energy_only_offer_price_10_to=energy_only_offer_price_10_to,
        offer_id_from=offer_id_from,
        offer_id_to=offer_id_to,
        multi_hour_block=multi_hour_block,
        block_curve=block_curve,
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
    settlement_point_name: str | Unset = UNSET,
    qse_name: str | Unset = UNSET,
    energy_only_offer_mw1_from: float | Unset = UNSET,
    energy_only_offer_mw1_to: float | Unset = UNSET,
    energy_only_offer_price_1_from: float | Unset = UNSET,
    energy_only_offer_price_1_to: float | Unset = UNSET,
    energy_only_offer_mw2_from: float | Unset = UNSET,
    energy_only_offer_mw2_to: float | Unset = UNSET,
    energy_only_offer_price_2_from: float | Unset = UNSET,
    energy_only_offer_price_2_to: float | Unset = UNSET,
    energy_only_offer_mw3_from: float | Unset = UNSET,
    energy_only_offer_mw3_to: float | Unset = UNSET,
    energy_only_offer_price_3_from: float | Unset = UNSET,
    energy_only_offer_price_3_to: float | Unset = UNSET,
    energy_only_offer_mw4_from: float | Unset = UNSET,
    energy_only_offer_mw4_to: float | Unset = UNSET,
    energy_only_offer_price_4_from: float | Unset = UNSET,
    energy_only_offer_price_4_to: float | Unset = UNSET,
    energy_only_offer_mw5_from: float | Unset = UNSET,
    energy_only_offer_mw5_to: float | Unset = UNSET,
    energy_only_offer_price_5_from: float | Unset = UNSET,
    energy_only_offer_price_5_to: float | Unset = UNSET,
    energy_only_offer_mw6_from: float | Unset = UNSET,
    energy_only_offer_mw6_to: float | Unset = UNSET,
    energy_only_offer_price_6_from: float | Unset = UNSET,
    energy_only_offer_price_6_to: float | Unset = UNSET,
    energy_only_offer_mw7_from: float | Unset = UNSET,
    energy_only_offer_mw7_to: float | Unset = UNSET,
    energy_only_offer_price_7_from: float | Unset = UNSET,
    energy_only_offer_price_7_to: float | Unset = UNSET,
    energy_only_offer_mw8_from: float | Unset = UNSET,
    energy_only_offer_mw8_to: float | Unset = UNSET,
    energy_only_offer_price_8_from: float | Unset = UNSET,
    energy_only_offer_price_8_to: float | Unset = UNSET,
    energy_only_offer_mw9_from: float | Unset = UNSET,
    energy_only_offer_mw9_to: float | Unset = UNSET,
    energy_only_offer_price_9_from: float | Unset = UNSET,
    energy_only_offer_price_9_to: float | Unset = UNSET,
    energy_only_offer_mw10_from: float | Unset = UNSET,
    energy_only_offer_mw10_to: float | Unset = UNSET,
    energy_only_offer_price_10_from: float | Unset = UNSET,
    energy_only_offer_price_10_to: float | Unset = UNSET,
    offer_id_from: float | Unset = UNSET,
    offer_id_to: float | Unset = UNSET,
    multi_hour_block: bool | Unset = UNSET,
    block_curve: bool | Unset = UNSET,
    page: int | Unset = UNSET,
    size: int | Unset = UNSET,
    sort: str | Unset = UNSET,
    dir_: str | Unset = UNSET,
) -> Exception_ | Report | None:
    """60 Day DAM Energy Only Offers

     60 Day DAM Energy Only Offers

    Args:
        delivery_date_from (str | Unset):
        delivery_date_to (str | Unset):
        hour_ending_from (str | Unset):
        hour_ending_to (str | Unset):
        settlement_point_name (str | Unset):
        qse_name (str | Unset):
        energy_only_offer_mw1_from (float | Unset):
        energy_only_offer_mw1_to (float | Unset):
        energy_only_offer_price_1_from (float | Unset):
        energy_only_offer_price_1_to (float | Unset):
        energy_only_offer_mw2_from (float | Unset):
        energy_only_offer_mw2_to (float | Unset):
        energy_only_offer_price_2_from (float | Unset):
        energy_only_offer_price_2_to (float | Unset):
        energy_only_offer_mw3_from (float | Unset):
        energy_only_offer_mw3_to (float | Unset):
        energy_only_offer_price_3_from (float | Unset):
        energy_only_offer_price_3_to (float | Unset):
        energy_only_offer_mw4_from (float | Unset):
        energy_only_offer_mw4_to (float | Unset):
        energy_only_offer_price_4_from (float | Unset):
        energy_only_offer_price_4_to (float | Unset):
        energy_only_offer_mw5_from (float | Unset):
        energy_only_offer_mw5_to (float | Unset):
        energy_only_offer_price_5_from (float | Unset):
        energy_only_offer_price_5_to (float | Unset):
        energy_only_offer_mw6_from (float | Unset):
        energy_only_offer_mw6_to (float | Unset):
        energy_only_offer_price_6_from (float | Unset):
        energy_only_offer_price_6_to (float | Unset):
        energy_only_offer_mw7_from (float | Unset):
        energy_only_offer_mw7_to (float | Unset):
        energy_only_offer_price_7_from (float | Unset):
        energy_only_offer_price_7_to (float | Unset):
        energy_only_offer_mw8_from (float | Unset):
        energy_only_offer_mw8_to (float | Unset):
        energy_only_offer_price_8_from (float | Unset):
        energy_only_offer_price_8_to (float | Unset):
        energy_only_offer_mw9_from (float | Unset):
        energy_only_offer_mw9_to (float | Unset):
        energy_only_offer_price_9_from (float | Unset):
        energy_only_offer_price_9_to (float | Unset):
        energy_only_offer_mw10_from (float | Unset):
        energy_only_offer_mw10_to (float | Unset):
        energy_only_offer_price_10_from (float | Unset):
        energy_only_offer_price_10_to (float | Unset):
        offer_id_from (float | Unset):
        offer_id_to (float | Unset):
        multi_hour_block (bool | Unset):
        block_curve (bool | Unset):
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
            settlement_point_name=settlement_point_name,
            qse_name=qse_name,
            energy_only_offer_mw1_from=energy_only_offer_mw1_from,
            energy_only_offer_mw1_to=energy_only_offer_mw1_to,
            energy_only_offer_price_1_from=energy_only_offer_price_1_from,
            energy_only_offer_price_1_to=energy_only_offer_price_1_to,
            energy_only_offer_mw2_from=energy_only_offer_mw2_from,
            energy_only_offer_mw2_to=energy_only_offer_mw2_to,
            energy_only_offer_price_2_from=energy_only_offer_price_2_from,
            energy_only_offer_price_2_to=energy_only_offer_price_2_to,
            energy_only_offer_mw3_from=energy_only_offer_mw3_from,
            energy_only_offer_mw3_to=energy_only_offer_mw3_to,
            energy_only_offer_price_3_from=energy_only_offer_price_3_from,
            energy_only_offer_price_3_to=energy_only_offer_price_3_to,
            energy_only_offer_mw4_from=energy_only_offer_mw4_from,
            energy_only_offer_mw4_to=energy_only_offer_mw4_to,
            energy_only_offer_price_4_from=energy_only_offer_price_4_from,
            energy_only_offer_price_4_to=energy_only_offer_price_4_to,
            energy_only_offer_mw5_from=energy_only_offer_mw5_from,
            energy_only_offer_mw5_to=energy_only_offer_mw5_to,
            energy_only_offer_price_5_from=energy_only_offer_price_5_from,
            energy_only_offer_price_5_to=energy_only_offer_price_5_to,
            energy_only_offer_mw6_from=energy_only_offer_mw6_from,
            energy_only_offer_mw6_to=energy_only_offer_mw6_to,
            energy_only_offer_price_6_from=energy_only_offer_price_6_from,
            energy_only_offer_price_6_to=energy_only_offer_price_6_to,
            energy_only_offer_mw7_from=energy_only_offer_mw7_from,
            energy_only_offer_mw7_to=energy_only_offer_mw7_to,
            energy_only_offer_price_7_from=energy_only_offer_price_7_from,
            energy_only_offer_price_7_to=energy_only_offer_price_7_to,
            energy_only_offer_mw8_from=energy_only_offer_mw8_from,
            energy_only_offer_mw8_to=energy_only_offer_mw8_to,
            energy_only_offer_price_8_from=energy_only_offer_price_8_from,
            energy_only_offer_price_8_to=energy_only_offer_price_8_to,
            energy_only_offer_mw9_from=energy_only_offer_mw9_from,
            energy_only_offer_mw9_to=energy_only_offer_mw9_to,
            energy_only_offer_price_9_from=energy_only_offer_price_9_from,
            energy_only_offer_price_9_to=energy_only_offer_price_9_to,
            energy_only_offer_mw10_from=energy_only_offer_mw10_from,
            energy_only_offer_mw10_to=energy_only_offer_mw10_to,
            energy_only_offer_price_10_from=energy_only_offer_price_10_from,
            energy_only_offer_price_10_to=energy_only_offer_price_10_to,
            offer_id_from=offer_id_from,
            offer_id_to=offer_id_to,
            multi_hour_block=multi_hour_block,
            block_curve=block_curve,
            page=page,
            size=size,
            sort=sort,
            dir_=dir_,
        )
    ).parsed
