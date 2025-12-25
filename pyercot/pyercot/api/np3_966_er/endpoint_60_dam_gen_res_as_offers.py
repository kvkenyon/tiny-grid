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
    price_2rrsffr_from: float | Unset = UNSET,
    price_2rrsffr_to: float | Unset = UNSET,
    price_2rrsufr_from: float | Unset = UNSET,
    price_2rrsufr_to: float | Unset = UNSET,
    price_2_online_nspin_from: float | Unset = UNSET,
    price_2_online_nspin_to: float | Unset = UNSET,
    price_2regup_from: float | Unset = UNSET,
    price_2regup_to: float | Unset = UNSET,
    price_2regdn_from: float | Unset = UNSET,
    price_2regdn_to: float | Unset = UNSET,
    price_2_offline_nspin_from: float | Unset = UNSET,
    price_2_offline_nspin_to: float | Unset = UNSET,
    quantity_mw2_from: int | Unset = UNSET,
    quantity_mw2_to: int | Unset = UNSET,
    block_indicator_3: bool | Unset = UNSET,
    price_3rrspfr_from: float | Unset = UNSET,
    price_3rrspfr_to: float | Unset = UNSET,
    price_3rrsffr_from: float | Unset = UNSET,
    price_3rrsffr_to: float | Unset = UNSET,
    price_3rrsufr_from: float | Unset = UNSET,
    price_3rrsufr_to: float | Unset = UNSET,
    price_3_online_nspin_from: float | Unset = UNSET,
    price_3_online_nspin_to: float | Unset = UNSET,
    price_3regup_from: float | Unset = UNSET,
    price_3regup_to: float | Unset = UNSET,
    price_3regdn_from: float | Unset = UNSET,
    price_3regdn_to: float | Unset = UNSET,
    price_3_offline_nspin_from: float | Unset = UNSET,
    price_3_offline_nspin_to: float | Unset = UNSET,
    quantity_mw3_from: int | Unset = UNSET,
    quantity_mw3_to: int | Unset = UNSET,
    block_indicator_4: bool | Unset = UNSET,
    price_4rrspfr_from: float | Unset = UNSET,
    price_4rrspfr_to: float | Unset = UNSET,
    price_4rrsffr_from: float | Unset = UNSET,
    price_4rrsffr_to: float | Unset = UNSET,
    price_4rrsufr_from: float | Unset = UNSET,
    price_4rrsufr_to: float | Unset = UNSET,
    price_4_online_nspin_from: float | Unset = UNSET,
    price_4_online_nspin_to: float | Unset = UNSET,
    price_4regup_from: float | Unset = UNSET,
    price_4regup_to: float | Unset = UNSET,
    price_4regdn_from: float | Unset = UNSET,
    price_4regdn_to: float | Unset = UNSET,
    price_4_offline_nspin_from: float | Unset = UNSET,
    price_4_offline_nspin_to: float | Unset = UNSET,
    quantity_mw4_from: int | Unset = UNSET,
    quantity_mw4_to: int | Unset = UNSET,
    block_indicator_5: bool | Unset = UNSET,
    price_5rrspfr_from: float | Unset = UNSET,
    price_5rrspfr_to: float | Unset = UNSET,
    price_5rrsffr_from: float | Unset = UNSET,
    price_5rrsffr_to: float | Unset = UNSET,
    price_5rrsufr_from: float | Unset = UNSET,
    price_5rrsufr_to: float | Unset = UNSET,
    price_5_online_nspin_from: float | Unset = UNSET,
    price_5_online_nspin_to: float | Unset = UNSET,
    price_5regup_from: float | Unset = UNSET,
    price_5regup_to: float | Unset = UNSET,
    price_5regdn_from: float | Unset = UNSET,
    price_5regdn_to: float | Unset = UNSET,
    price_5_offline_nspin_from: float | Unset = UNSET,
    price_5_offline_nspin_to: float | Unset = UNSET,
    quantity_mw5_from: int | Unset = UNSET,
    quantity_mw5_to: int | Unset = UNSET,
    delivery_date_from: str | Unset = UNSET,
    delivery_date_to: str | Unset = UNSET,
    hour_ending_from: str | Unset = UNSET,
    hour_ending_to: str | Unset = UNSET,
    qse_name: str | Unset = UNSET,
    dme_name: str | Unset = UNSET,
    resource_name: str | Unset = UNSET,
    multi_hour_block: bool | Unset = UNSET,
    block_indicator_1: bool | Unset = UNSET,
    price_1rrspfr_from: float | Unset = UNSET,
    price_1rrspfr_to: float | Unset = UNSET,
    price_1rrsffr_from: float | Unset = UNSET,
    price_1rrsffr_to: float | Unset = UNSET,
    price_1rrsufr_from: float | Unset = UNSET,
    price_1rrsufr_to: float | Unset = UNSET,
    price_1_online_nspin_from: float | Unset = UNSET,
    price_1_online_nspin_to: float | Unset = UNSET,
    price_1regup_from: float | Unset = UNSET,
    price_1regup_to: float | Unset = UNSET,
    price_1regdn_from: float | Unset = UNSET,
    price_1regdn_to: float | Unset = UNSET,
    price_1_offline_nspin_from: float | Unset = UNSET,
    price_1_offline_nspin_to: float | Unset = UNSET,
    quantity_mw1_from: int | Unset = UNSET,
    quantity_mw1_to: int | Unset = UNSET,
    block_indicator_2: bool | Unset = UNSET,
    price_2rrspfr_from: float | Unset = UNSET,
    price_2rrspfr_to: float | Unset = UNSET,
    page: int | Unset = UNSET,
    size: int | Unset = UNSET,
    sort: str | Unset = UNSET,
    dir_: str | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["price2RRSFFRFrom"] = price_2rrsffr_from

    params["price2RRSFFRTo"] = price_2rrsffr_to

    params["price2RRSUFRFrom"] = price_2rrsufr_from

    params["price2RRSUFRTo"] = price_2rrsufr_to

    params["price2OnlineNSPINFrom"] = price_2_online_nspin_from

    params["price2OnlineNSPINTo"] = price_2_online_nspin_to

    params["price2REGUPFrom"] = price_2regup_from

    params["price2REGUPTo"] = price_2regup_to

    params["price2REGDNFrom"] = price_2regdn_from

    params["price2REGDNTo"] = price_2regdn_to

    params["price2OfflineNSPINFrom"] = price_2_offline_nspin_from

    params["price2OfflineNSPINTo"] = price_2_offline_nspin_to

    params["quantityMW2From"] = quantity_mw2_from

    params["quantityMW2To"] = quantity_mw2_to

    params["blockIndicator3"] = block_indicator_3

    params["price3RRSPFRFrom"] = price_3rrspfr_from

    params["price3RRSPFRTo"] = price_3rrspfr_to

    params["price3RRSFFRFrom"] = price_3rrsffr_from

    params["price3RRSFFRTo"] = price_3rrsffr_to

    params["price3RRSUFRFrom"] = price_3rrsufr_from

    params["price3RRSUFRTo"] = price_3rrsufr_to

    params["price3OnlineNSPINFrom"] = price_3_online_nspin_from

    params["price3OnlineNSPINTo"] = price_3_online_nspin_to

    params["price3REGUPFrom"] = price_3regup_from

    params["price3REGUPTo"] = price_3regup_to

    params["price3REGDNFrom"] = price_3regdn_from

    params["price3REGDNTo"] = price_3regdn_to

    params["price3OfflineNSPINFrom"] = price_3_offline_nspin_from

    params["price3OfflineNSPINTo"] = price_3_offline_nspin_to

    params["quantityMW3From"] = quantity_mw3_from

    params["quantityMW3To"] = quantity_mw3_to

    params["blockIndicator4"] = block_indicator_4

    params["price4RRSPFRFrom"] = price_4rrspfr_from

    params["price4RRSPFRTo"] = price_4rrspfr_to

    params["price4RRSFFRFrom"] = price_4rrsffr_from

    params["price4RRSFFRTo"] = price_4rrsffr_to

    params["price4RRSUFRFrom"] = price_4rrsufr_from

    params["price4RRSUFRTo"] = price_4rrsufr_to

    params["price4OnlineNSPINFrom"] = price_4_online_nspin_from

    params["price4OnlineNSPINTo"] = price_4_online_nspin_to

    params["price4REGUPFrom"] = price_4regup_from

    params["price4REGUPTo"] = price_4regup_to

    params["price4REGDNFrom"] = price_4regdn_from

    params["price4REGDNTo"] = price_4regdn_to

    params["price4OfflineNSPINFrom"] = price_4_offline_nspin_from

    params["price4OfflineNSPINTo"] = price_4_offline_nspin_to

    params["quantityMW4From"] = quantity_mw4_from

    params["quantityMW4To"] = quantity_mw4_to

    params["blockIndicator5"] = block_indicator_5

    params["price5RRSPFRFrom"] = price_5rrspfr_from

    params["price5RRSPFRTo"] = price_5rrspfr_to

    params["price5RRSFFRFrom"] = price_5rrsffr_from

    params["price5RRSFFRTo"] = price_5rrsffr_to

    params["price5RRSUFRFrom"] = price_5rrsufr_from

    params["price5RRSUFRTo"] = price_5rrsufr_to

    params["price5OnlineNSPINFrom"] = price_5_online_nspin_from

    params["price5OnlineNSPINTo"] = price_5_online_nspin_to

    params["price5REGUPFrom"] = price_5regup_from

    params["price5REGUPTo"] = price_5regup_to

    params["price5REGDNFrom"] = price_5regdn_from

    params["price5REGDNTo"] = price_5regdn_to

    params["price5OfflineNSPINFrom"] = price_5_offline_nspin_from

    params["price5OfflineNSPINTo"] = price_5_offline_nspin_to

    params["quantityMW5From"] = quantity_mw5_from

    params["quantityMW5To"] = quantity_mw5_to

    params["deliveryDateFrom"] = delivery_date_from

    params["deliveryDateTo"] = delivery_date_to

    params["hourEndingFrom"] = hour_ending_from

    params["hourEndingTo"] = hour_ending_to

    params["qseName"] = qse_name

    params["dmeName"] = dme_name

    params["resourceName"] = resource_name

    params["multiHourBlock"] = multi_hour_block

    params["blockIndicator1"] = block_indicator_1

    params["price1RRSPFRFrom"] = price_1rrspfr_from

    params["price1RRSPFRTo"] = price_1rrspfr_to

    params["price1RRSFFRFrom"] = price_1rrsffr_from

    params["price1RRSFFRTo"] = price_1rrsffr_to

    params["price1RRSUFRFrom"] = price_1rrsufr_from

    params["price1RRSUFRTo"] = price_1rrsufr_to

    params["price1OnlineNSPINFrom"] = price_1_online_nspin_from

    params["price1OnlineNSPINTo"] = price_1_online_nspin_to

    params["price1REGUPFrom"] = price_1regup_from

    params["price1REGUPTo"] = price_1regup_to

    params["price1REGDNFrom"] = price_1regdn_from

    params["price1REGDNTo"] = price_1regdn_to

    params["price1OfflineNSPINFrom"] = price_1_offline_nspin_from

    params["price1OfflineNSPINTo"] = price_1_offline_nspin_to

    params["quantityMW1From"] = quantity_mw1_from

    params["quantityMW1To"] = quantity_mw1_to

    params["blockIndicator2"] = block_indicator_2

    params["price2RRSPFRFrom"] = price_2rrspfr_from

    params["price2RRSPFRTo"] = price_2rrspfr_to

    params["page"] = page

    params["size"] = size

    params["sort"] = sort

    params["dir"] = dir_

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/np3-966-er/60_dam_gen_res_as_offers",
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
    price_2rrsffr_from: float | Unset = UNSET,
    price_2rrsffr_to: float | Unset = UNSET,
    price_2rrsufr_from: float | Unset = UNSET,
    price_2rrsufr_to: float | Unset = UNSET,
    price_2_online_nspin_from: float | Unset = UNSET,
    price_2_online_nspin_to: float | Unset = UNSET,
    price_2regup_from: float | Unset = UNSET,
    price_2regup_to: float | Unset = UNSET,
    price_2regdn_from: float | Unset = UNSET,
    price_2regdn_to: float | Unset = UNSET,
    price_2_offline_nspin_from: float | Unset = UNSET,
    price_2_offline_nspin_to: float | Unset = UNSET,
    quantity_mw2_from: int | Unset = UNSET,
    quantity_mw2_to: int | Unset = UNSET,
    block_indicator_3: bool | Unset = UNSET,
    price_3rrspfr_from: float | Unset = UNSET,
    price_3rrspfr_to: float | Unset = UNSET,
    price_3rrsffr_from: float | Unset = UNSET,
    price_3rrsffr_to: float | Unset = UNSET,
    price_3rrsufr_from: float | Unset = UNSET,
    price_3rrsufr_to: float | Unset = UNSET,
    price_3_online_nspin_from: float | Unset = UNSET,
    price_3_online_nspin_to: float | Unset = UNSET,
    price_3regup_from: float | Unset = UNSET,
    price_3regup_to: float | Unset = UNSET,
    price_3regdn_from: float | Unset = UNSET,
    price_3regdn_to: float | Unset = UNSET,
    price_3_offline_nspin_from: float | Unset = UNSET,
    price_3_offline_nspin_to: float | Unset = UNSET,
    quantity_mw3_from: int | Unset = UNSET,
    quantity_mw3_to: int | Unset = UNSET,
    block_indicator_4: bool | Unset = UNSET,
    price_4rrspfr_from: float | Unset = UNSET,
    price_4rrspfr_to: float | Unset = UNSET,
    price_4rrsffr_from: float | Unset = UNSET,
    price_4rrsffr_to: float | Unset = UNSET,
    price_4rrsufr_from: float | Unset = UNSET,
    price_4rrsufr_to: float | Unset = UNSET,
    price_4_online_nspin_from: float | Unset = UNSET,
    price_4_online_nspin_to: float | Unset = UNSET,
    price_4regup_from: float | Unset = UNSET,
    price_4regup_to: float | Unset = UNSET,
    price_4regdn_from: float | Unset = UNSET,
    price_4regdn_to: float | Unset = UNSET,
    price_4_offline_nspin_from: float | Unset = UNSET,
    price_4_offline_nspin_to: float | Unset = UNSET,
    quantity_mw4_from: int | Unset = UNSET,
    quantity_mw4_to: int | Unset = UNSET,
    block_indicator_5: bool | Unset = UNSET,
    price_5rrspfr_from: float | Unset = UNSET,
    price_5rrspfr_to: float | Unset = UNSET,
    price_5rrsffr_from: float | Unset = UNSET,
    price_5rrsffr_to: float | Unset = UNSET,
    price_5rrsufr_from: float | Unset = UNSET,
    price_5rrsufr_to: float | Unset = UNSET,
    price_5_online_nspin_from: float | Unset = UNSET,
    price_5_online_nspin_to: float | Unset = UNSET,
    price_5regup_from: float | Unset = UNSET,
    price_5regup_to: float | Unset = UNSET,
    price_5regdn_from: float | Unset = UNSET,
    price_5regdn_to: float | Unset = UNSET,
    price_5_offline_nspin_from: float | Unset = UNSET,
    price_5_offline_nspin_to: float | Unset = UNSET,
    quantity_mw5_from: int | Unset = UNSET,
    quantity_mw5_to: int | Unset = UNSET,
    delivery_date_from: str | Unset = UNSET,
    delivery_date_to: str | Unset = UNSET,
    hour_ending_from: str | Unset = UNSET,
    hour_ending_to: str | Unset = UNSET,
    qse_name: str | Unset = UNSET,
    dme_name: str | Unset = UNSET,
    resource_name: str | Unset = UNSET,
    multi_hour_block: bool | Unset = UNSET,
    block_indicator_1: bool | Unset = UNSET,
    price_1rrspfr_from: float | Unset = UNSET,
    price_1rrspfr_to: float | Unset = UNSET,
    price_1rrsffr_from: float | Unset = UNSET,
    price_1rrsffr_to: float | Unset = UNSET,
    price_1rrsufr_from: float | Unset = UNSET,
    price_1rrsufr_to: float | Unset = UNSET,
    price_1_online_nspin_from: float | Unset = UNSET,
    price_1_online_nspin_to: float | Unset = UNSET,
    price_1regup_from: float | Unset = UNSET,
    price_1regup_to: float | Unset = UNSET,
    price_1regdn_from: float | Unset = UNSET,
    price_1regdn_to: float | Unset = UNSET,
    price_1_offline_nspin_from: float | Unset = UNSET,
    price_1_offline_nspin_to: float | Unset = UNSET,
    quantity_mw1_from: int | Unset = UNSET,
    quantity_mw1_to: int | Unset = UNSET,
    block_indicator_2: bool | Unset = UNSET,
    price_2rrspfr_from: float | Unset = UNSET,
    price_2rrspfr_to: float | Unset = UNSET,
    page: int | Unset = UNSET,
    size: int | Unset = UNSET,
    sort: str | Unset = UNSET,
    dir_: str | Unset = UNSET,
) -> Response[Exception_ | Report]:
    """60 Day DAM Generation Resources AS Offers

     60 Day DAM Generation Resources AS Offers

    Args:
        price_2rrsffr_from (float | Unset):
        price_2rrsffr_to (float | Unset):
        price_2rrsufr_from (float | Unset):
        price_2rrsufr_to (float | Unset):
        price_2_online_nspin_from (float | Unset):
        price_2_online_nspin_to (float | Unset):
        price_2regup_from (float | Unset):
        price_2regup_to (float | Unset):
        price_2regdn_from (float | Unset):
        price_2regdn_to (float | Unset):
        price_2_offline_nspin_from (float | Unset):
        price_2_offline_nspin_to (float | Unset):
        quantity_mw2_from (int | Unset):
        quantity_mw2_to (int | Unset):
        block_indicator_3 (bool | Unset):
        price_3rrspfr_from (float | Unset):
        price_3rrspfr_to (float | Unset):
        price_3rrsffr_from (float | Unset):
        price_3rrsffr_to (float | Unset):
        price_3rrsufr_from (float | Unset):
        price_3rrsufr_to (float | Unset):
        price_3_online_nspin_from (float | Unset):
        price_3_online_nspin_to (float | Unset):
        price_3regup_from (float | Unset):
        price_3regup_to (float | Unset):
        price_3regdn_from (float | Unset):
        price_3regdn_to (float | Unset):
        price_3_offline_nspin_from (float | Unset):
        price_3_offline_nspin_to (float | Unset):
        quantity_mw3_from (int | Unset):
        quantity_mw3_to (int | Unset):
        block_indicator_4 (bool | Unset):
        price_4rrspfr_from (float | Unset):
        price_4rrspfr_to (float | Unset):
        price_4rrsffr_from (float | Unset):
        price_4rrsffr_to (float | Unset):
        price_4rrsufr_from (float | Unset):
        price_4rrsufr_to (float | Unset):
        price_4_online_nspin_from (float | Unset):
        price_4_online_nspin_to (float | Unset):
        price_4regup_from (float | Unset):
        price_4regup_to (float | Unset):
        price_4regdn_from (float | Unset):
        price_4regdn_to (float | Unset):
        price_4_offline_nspin_from (float | Unset):
        price_4_offline_nspin_to (float | Unset):
        quantity_mw4_from (int | Unset):
        quantity_mw4_to (int | Unset):
        block_indicator_5 (bool | Unset):
        price_5rrspfr_from (float | Unset):
        price_5rrspfr_to (float | Unset):
        price_5rrsffr_from (float | Unset):
        price_5rrsffr_to (float | Unset):
        price_5rrsufr_from (float | Unset):
        price_5rrsufr_to (float | Unset):
        price_5_online_nspin_from (float | Unset):
        price_5_online_nspin_to (float | Unset):
        price_5regup_from (float | Unset):
        price_5regup_to (float | Unset):
        price_5regdn_from (float | Unset):
        price_5regdn_to (float | Unset):
        price_5_offline_nspin_from (float | Unset):
        price_5_offline_nspin_to (float | Unset):
        quantity_mw5_from (int | Unset):
        quantity_mw5_to (int | Unset):
        delivery_date_from (str | Unset):
        delivery_date_to (str | Unset):
        hour_ending_from (str | Unset):
        hour_ending_to (str | Unset):
        qse_name (str | Unset):
        dme_name (str | Unset):
        resource_name (str | Unset):
        multi_hour_block (bool | Unset):
        block_indicator_1 (bool | Unset):
        price_1rrspfr_from (float | Unset):
        price_1rrspfr_to (float | Unset):
        price_1rrsffr_from (float | Unset):
        price_1rrsffr_to (float | Unset):
        price_1rrsufr_from (float | Unset):
        price_1rrsufr_to (float | Unset):
        price_1_online_nspin_from (float | Unset):
        price_1_online_nspin_to (float | Unset):
        price_1regup_from (float | Unset):
        price_1regup_to (float | Unset):
        price_1regdn_from (float | Unset):
        price_1regdn_to (float | Unset):
        price_1_offline_nspin_from (float | Unset):
        price_1_offline_nspin_to (float | Unset):
        quantity_mw1_from (int | Unset):
        quantity_mw1_to (int | Unset):
        block_indicator_2 (bool | Unset):
        price_2rrspfr_from (float | Unset):
        price_2rrspfr_to (float | Unset):
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
        price_2rrsffr_from=price_2rrsffr_from,
        price_2rrsffr_to=price_2rrsffr_to,
        price_2rrsufr_from=price_2rrsufr_from,
        price_2rrsufr_to=price_2rrsufr_to,
        price_2_online_nspin_from=price_2_online_nspin_from,
        price_2_online_nspin_to=price_2_online_nspin_to,
        price_2regup_from=price_2regup_from,
        price_2regup_to=price_2regup_to,
        price_2regdn_from=price_2regdn_from,
        price_2regdn_to=price_2regdn_to,
        price_2_offline_nspin_from=price_2_offline_nspin_from,
        price_2_offline_nspin_to=price_2_offline_nspin_to,
        quantity_mw2_from=quantity_mw2_from,
        quantity_mw2_to=quantity_mw2_to,
        block_indicator_3=block_indicator_3,
        price_3rrspfr_from=price_3rrspfr_from,
        price_3rrspfr_to=price_3rrspfr_to,
        price_3rrsffr_from=price_3rrsffr_from,
        price_3rrsffr_to=price_3rrsffr_to,
        price_3rrsufr_from=price_3rrsufr_from,
        price_3rrsufr_to=price_3rrsufr_to,
        price_3_online_nspin_from=price_3_online_nspin_from,
        price_3_online_nspin_to=price_3_online_nspin_to,
        price_3regup_from=price_3regup_from,
        price_3regup_to=price_3regup_to,
        price_3regdn_from=price_3regdn_from,
        price_3regdn_to=price_3regdn_to,
        price_3_offline_nspin_from=price_3_offline_nspin_from,
        price_3_offline_nspin_to=price_3_offline_nspin_to,
        quantity_mw3_from=quantity_mw3_from,
        quantity_mw3_to=quantity_mw3_to,
        block_indicator_4=block_indicator_4,
        price_4rrspfr_from=price_4rrspfr_from,
        price_4rrspfr_to=price_4rrspfr_to,
        price_4rrsffr_from=price_4rrsffr_from,
        price_4rrsffr_to=price_4rrsffr_to,
        price_4rrsufr_from=price_4rrsufr_from,
        price_4rrsufr_to=price_4rrsufr_to,
        price_4_online_nspin_from=price_4_online_nspin_from,
        price_4_online_nspin_to=price_4_online_nspin_to,
        price_4regup_from=price_4regup_from,
        price_4regup_to=price_4regup_to,
        price_4regdn_from=price_4regdn_from,
        price_4regdn_to=price_4regdn_to,
        price_4_offline_nspin_from=price_4_offline_nspin_from,
        price_4_offline_nspin_to=price_4_offline_nspin_to,
        quantity_mw4_from=quantity_mw4_from,
        quantity_mw4_to=quantity_mw4_to,
        block_indicator_5=block_indicator_5,
        price_5rrspfr_from=price_5rrspfr_from,
        price_5rrspfr_to=price_5rrspfr_to,
        price_5rrsffr_from=price_5rrsffr_from,
        price_5rrsffr_to=price_5rrsffr_to,
        price_5rrsufr_from=price_5rrsufr_from,
        price_5rrsufr_to=price_5rrsufr_to,
        price_5_online_nspin_from=price_5_online_nspin_from,
        price_5_online_nspin_to=price_5_online_nspin_to,
        price_5regup_from=price_5regup_from,
        price_5regup_to=price_5regup_to,
        price_5regdn_from=price_5regdn_from,
        price_5regdn_to=price_5regdn_to,
        price_5_offline_nspin_from=price_5_offline_nspin_from,
        price_5_offline_nspin_to=price_5_offline_nspin_to,
        quantity_mw5_from=quantity_mw5_from,
        quantity_mw5_to=quantity_mw5_to,
        delivery_date_from=delivery_date_from,
        delivery_date_to=delivery_date_to,
        hour_ending_from=hour_ending_from,
        hour_ending_to=hour_ending_to,
        qse_name=qse_name,
        dme_name=dme_name,
        resource_name=resource_name,
        multi_hour_block=multi_hour_block,
        block_indicator_1=block_indicator_1,
        price_1rrspfr_from=price_1rrspfr_from,
        price_1rrspfr_to=price_1rrspfr_to,
        price_1rrsffr_from=price_1rrsffr_from,
        price_1rrsffr_to=price_1rrsffr_to,
        price_1rrsufr_from=price_1rrsufr_from,
        price_1rrsufr_to=price_1rrsufr_to,
        price_1_online_nspin_from=price_1_online_nspin_from,
        price_1_online_nspin_to=price_1_online_nspin_to,
        price_1regup_from=price_1regup_from,
        price_1regup_to=price_1regup_to,
        price_1regdn_from=price_1regdn_from,
        price_1regdn_to=price_1regdn_to,
        price_1_offline_nspin_from=price_1_offline_nspin_from,
        price_1_offline_nspin_to=price_1_offline_nspin_to,
        quantity_mw1_from=quantity_mw1_from,
        quantity_mw1_to=quantity_mw1_to,
        block_indicator_2=block_indicator_2,
        price_2rrspfr_from=price_2rrspfr_from,
        price_2rrspfr_to=price_2rrspfr_to,
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
    price_2rrsffr_from: float | Unset = UNSET,
    price_2rrsffr_to: float | Unset = UNSET,
    price_2rrsufr_from: float | Unset = UNSET,
    price_2rrsufr_to: float | Unset = UNSET,
    price_2_online_nspin_from: float | Unset = UNSET,
    price_2_online_nspin_to: float | Unset = UNSET,
    price_2regup_from: float | Unset = UNSET,
    price_2regup_to: float | Unset = UNSET,
    price_2regdn_from: float | Unset = UNSET,
    price_2regdn_to: float | Unset = UNSET,
    price_2_offline_nspin_from: float | Unset = UNSET,
    price_2_offline_nspin_to: float | Unset = UNSET,
    quantity_mw2_from: int | Unset = UNSET,
    quantity_mw2_to: int | Unset = UNSET,
    block_indicator_3: bool | Unset = UNSET,
    price_3rrspfr_from: float | Unset = UNSET,
    price_3rrspfr_to: float | Unset = UNSET,
    price_3rrsffr_from: float | Unset = UNSET,
    price_3rrsffr_to: float | Unset = UNSET,
    price_3rrsufr_from: float | Unset = UNSET,
    price_3rrsufr_to: float | Unset = UNSET,
    price_3_online_nspin_from: float | Unset = UNSET,
    price_3_online_nspin_to: float | Unset = UNSET,
    price_3regup_from: float | Unset = UNSET,
    price_3regup_to: float | Unset = UNSET,
    price_3regdn_from: float | Unset = UNSET,
    price_3regdn_to: float | Unset = UNSET,
    price_3_offline_nspin_from: float | Unset = UNSET,
    price_3_offline_nspin_to: float | Unset = UNSET,
    quantity_mw3_from: int | Unset = UNSET,
    quantity_mw3_to: int | Unset = UNSET,
    block_indicator_4: bool | Unset = UNSET,
    price_4rrspfr_from: float | Unset = UNSET,
    price_4rrspfr_to: float | Unset = UNSET,
    price_4rrsffr_from: float | Unset = UNSET,
    price_4rrsffr_to: float | Unset = UNSET,
    price_4rrsufr_from: float | Unset = UNSET,
    price_4rrsufr_to: float | Unset = UNSET,
    price_4_online_nspin_from: float | Unset = UNSET,
    price_4_online_nspin_to: float | Unset = UNSET,
    price_4regup_from: float | Unset = UNSET,
    price_4regup_to: float | Unset = UNSET,
    price_4regdn_from: float | Unset = UNSET,
    price_4regdn_to: float | Unset = UNSET,
    price_4_offline_nspin_from: float | Unset = UNSET,
    price_4_offline_nspin_to: float | Unset = UNSET,
    quantity_mw4_from: int | Unset = UNSET,
    quantity_mw4_to: int | Unset = UNSET,
    block_indicator_5: bool | Unset = UNSET,
    price_5rrspfr_from: float | Unset = UNSET,
    price_5rrspfr_to: float | Unset = UNSET,
    price_5rrsffr_from: float | Unset = UNSET,
    price_5rrsffr_to: float | Unset = UNSET,
    price_5rrsufr_from: float | Unset = UNSET,
    price_5rrsufr_to: float | Unset = UNSET,
    price_5_online_nspin_from: float | Unset = UNSET,
    price_5_online_nspin_to: float | Unset = UNSET,
    price_5regup_from: float | Unset = UNSET,
    price_5regup_to: float | Unset = UNSET,
    price_5regdn_from: float | Unset = UNSET,
    price_5regdn_to: float | Unset = UNSET,
    price_5_offline_nspin_from: float | Unset = UNSET,
    price_5_offline_nspin_to: float | Unset = UNSET,
    quantity_mw5_from: int | Unset = UNSET,
    quantity_mw5_to: int | Unset = UNSET,
    delivery_date_from: str | Unset = UNSET,
    delivery_date_to: str | Unset = UNSET,
    hour_ending_from: str | Unset = UNSET,
    hour_ending_to: str | Unset = UNSET,
    qse_name: str | Unset = UNSET,
    dme_name: str | Unset = UNSET,
    resource_name: str | Unset = UNSET,
    multi_hour_block: bool | Unset = UNSET,
    block_indicator_1: bool | Unset = UNSET,
    price_1rrspfr_from: float | Unset = UNSET,
    price_1rrspfr_to: float | Unset = UNSET,
    price_1rrsffr_from: float | Unset = UNSET,
    price_1rrsffr_to: float | Unset = UNSET,
    price_1rrsufr_from: float | Unset = UNSET,
    price_1rrsufr_to: float | Unset = UNSET,
    price_1_online_nspin_from: float | Unset = UNSET,
    price_1_online_nspin_to: float | Unset = UNSET,
    price_1regup_from: float | Unset = UNSET,
    price_1regup_to: float | Unset = UNSET,
    price_1regdn_from: float | Unset = UNSET,
    price_1regdn_to: float | Unset = UNSET,
    price_1_offline_nspin_from: float | Unset = UNSET,
    price_1_offline_nspin_to: float | Unset = UNSET,
    quantity_mw1_from: int | Unset = UNSET,
    quantity_mw1_to: int | Unset = UNSET,
    block_indicator_2: bool | Unset = UNSET,
    price_2rrspfr_from: float | Unset = UNSET,
    price_2rrspfr_to: float | Unset = UNSET,
    page: int | Unset = UNSET,
    size: int | Unset = UNSET,
    sort: str | Unset = UNSET,
    dir_: str | Unset = UNSET,
) -> Exception_ | Report | None:
    """60 Day DAM Generation Resources AS Offers

     60 Day DAM Generation Resources AS Offers

    Args:
        price_2rrsffr_from (float | Unset):
        price_2rrsffr_to (float | Unset):
        price_2rrsufr_from (float | Unset):
        price_2rrsufr_to (float | Unset):
        price_2_online_nspin_from (float | Unset):
        price_2_online_nspin_to (float | Unset):
        price_2regup_from (float | Unset):
        price_2regup_to (float | Unset):
        price_2regdn_from (float | Unset):
        price_2regdn_to (float | Unset):
        price_2_offline_nspin_from (float | Unset):
        price_2_offline_nspin_to (float | Unset):
        quantity_mw2_from (int | Unset):
        quantity_mw2_to (int | Unset):
        block_indicator_3 (bool | Unset):
        price_3rrspfr_from (float | Unset):
        price_3rrspfr_to (float | Unset):
        price_3rrsffr_from (float | Unset):
        price_3rrsffr_to (float | Unset):
        price_3rrsufr_from (float | Unset):
        price_3rrsufr_to (float | Unset):
        price_3_online_nspin_from (float | Unset):
        price_3_online_nspin_to (float | Unset):
        price_3regup_from (float | Unset):
        price_3regup_to (float | Unset):
        price_3regdn_from (float | Unset):
        price_3regdn_to (float | Unset):
        price_3_offline_nspin_from (float | Unset):
        price_3_offline_nspin_to (float | Unset):
        quantity_mw3_from (int | Unset):
        quantity_mw3_to (int | Unset):
        block_indicator_4 (bool | Unset):
        price_4rrspfr_from (float | Unset):
        price_4rrspfr_to (float | Unset):
        price_4rrsffr_from (float | Unset):
        price_4rrsffr_to (float | Unset):
        price_4rrsufr_from (float | Unset):
        price_4rrsufr_to (float | Unset):
        price_4_online_nspin_from (float | Unset):
        price_4_online_nspin_to (float | Unset):
        price_4regup_from (float | Unset):
        price_4regup_to (float | Unset):
        price_4regdn_from (float | Unset):
        price_4regdn_to (float | Unset):
        price_4_offline_nspin_from (float | Unset):
        price_4_offline_nspin_to (float | Unset):
        quantity_mw4_from (int | Unset):
        quantity_mw4_to (int | Unset):
        block_indicator_5 (bool | Unset):
        price_5rrspfr_from (float | Unset):
        price_5rrspfr_to (float | Unset):
        price_5rrsffr_from (float | Unset):
        price_5rrsffr_to (float | Unset):
        price_5rrsufr_from (float | Unset):
        price_5rrsufr_to (float | Unset):
        price_5_online_nspin_from (float | Unset):
        price_5_online_nspin_to (float | Unset):
        price_5regup_from (float | Unset):
        price_5regup_to (float | Unset):
        price_5regdn_from (float | Unset):
        price_5regdn_to (float | Unset):
        price_5_offline_nspin_from (float | Unset):
        price_5_offline_nspin_to (float | Unset):
        quantity_mw5_from (int | Unset):
        quantity_mw5_to (int | Unset):
        delivery_date_from (str | Unset):
        delivery_date_to (str | Unset):
        hour_ending_from (str | Unset):
        hour_ending_to (str | Unset):
        qse_name (str | Unset):
        dme_name (str | Unset):
        resource_name (str | Unset):
        multi_hour_block (bool | Unset):
        block_indicator_1 (bool | Unset):
        price_1rrspfr_from (float | Unset):
        price_1rrspfr_to (float | Unset):
        price_1rrsffr_from (float | Unset):
        price_1rrsffr_to (float | Unset):
        price_1rrsufr_from (float | Unset):
        price_1rrsufr_to (float | Unset):
        price_1_online_nspin_from (float | Unset):
        price_1_online_nspin_to (float | Unset):
        price_1regup_from (float | Unset):
        price_1regup_to (float | Unset):
        price_1regdn_from (float | Unset):
        price_1regdn_to (float | Unset):
        price_1_offline_nspin_from (float | Unset):
        price_1_offline_nspin_to (float | Unset):
        quantity_mw1_from (int | Unset):
        quantity_mw1_to (int | Unset):
        block_indicator_2 (bool | Unset):
        price_2rrspfr_from (float | Unset):
        price_2rrspfr_to (float | Unset):
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
        price_2rrsffr_from=price_2rrsffr_from,
        price_2rrsffr_to=price_2rrsffr_to,
        price_2rrsufr_from=price_2rrsufr_from,
        price_2rrsufr_to=price_2rrsufr_to,
        price_2_online_nspin_from=price_2_online_nspin_from,
        price_2_online_nspin_to=price_2_online_nspin_to,
        price_2regup_from=price_2regup_from,
        price_2regup_to=price_2regup_to,
        price_2regdn_from=price_2regdn_from,
        price_2regdn_to=price_2regdn_to,
        price_2_offline_nspin_from=price_2_offline_nspin_from,
        price_2_offline_nspin_to=price_2_offline_nspin_to,
        quantity_mw2_from=quantity_mw2_from,
        quantity_mw2_to=quantity_mw2_to,
        block_indicator_3=block_indicator_3,
        price_3rrspfr_from=price_3rrspfr_from,
        price_3rrspfr_to=price_3rrspfr_to,
        price_3rrsffr_from=price_3rrsffr_from,
        price_3rrsffr_to=price_3rrsffr_to,
        price_3rrsufr_from=price_3rrsufr_from,
        price_3rrsufr_to=price_3rrsufr_to,
        price_3_online_nspin_from=price_3_online_nspin_from,
        price_3_online_nspin_to=price_3_online_nspin_to,
        price_3regup_from=price_3regup_from,
        price_3regup_to=price_3regup_to,
        price_3regdn_from=price_3regdn_from,
        price_3regdn_to=price_3regdn_to,
        price_3_offline_nspin_from=price_3_offline_nspin_from,
        price_3_offline_nspin_to=price_3_offline_nspin_to,
        quantity_mw3_from=quantity_mw3_from,
        quantity_mw3_to=quantity_mw3_to,
        block_indicator_4=block_indicator_4,
        price_4rrspfr_from=price_4rrspfr_from,
        price_4rrspfr_to=price_4rrspfr_to,
        price_4rrsffr_from=price_4rrsffr_from,
        price_4rrsffr_to=price_4rrsffr_to,
        price_4rrsufr_from=price_4rrsufr_from,
        price_4rrsufr_to=price_4rrsufr_to,
        price_4_online_nspin_from=price_4_online_nspin_from,
        price_4_online_nspin_to=price_4_online_nspin_to,
        price_4regup_from=price_4regup_from,
        price_4regup_to=price_4regup_to,
        price_4regdn_from=price_4regdn_from,
        price_4regdn_to=price_4regdn_to,
        price_4_offline_nspin_from=price_4_offline_nspin_from,
        price_4_offline_nspin_to=price_4_offline_nspin_to,
        quantity_mw4_from=quantity_mw4_from,
        quantity_mw4_to=quantity_mw4_to,
        block_indicator_5=block_indicator_5,
        price_5rrspfr_from=price_5rrspfr_from,
        price_5rrspfr_to=price_5rrspfr_to,
        price_5rrsffr_from=price_5rrsffr_from,
        price_5rrsffr_to=price_5rrsffr_to,
        price_5rrsufr_from=price_5rrsufr_from,
        price_5rrsufr_to=price_5rrsufr_to,
        price_5_online_nspin_from=price_5_online_nspin_from,
        price_5_online_nspin_to=price_5_online_nspin_to,
        price_5regup_from=price_5regup_from,
        price_5regup_to=price_5regup_to,
        price_5regdn_from=price_5regdn_from,
        price_5regdn_to=price_5regdn_to,
        price_5_offline_nspin_from=price_5_offline_nspin_from,
        price_5_offline_nspin_to=price_5_offline_nspin_to,
        quantity_mw5_from=quantity_mw5_from,
        quantity_mw5_to=quantity_mw5_to,
        delivery_date_from=delivery_date_from,
        delivery_date_to=delivery_date_to,
        hour_ending_from=hour_ending_from,
        hour_ending_to=hour_ending_to,
        qse_name=qse_name,
        dme_name=dme_name,
        resource_name=resource_name,
        multi_hour_block=multi_hour_block,
        block_indicator_1=block_indicator_1,
        price_1rrspfr_from=price_1rrspfr_from,
        price_1rrspfr_to=price_1rrspfr_to,
        price_1rrsffr_from=price_1rrsffr_from,
        price_1rrsffr_to=price_1rrsffr_to,
        price_1rrsufr_from=price_1rrsufr_from,
        price_1rrsufr_to=price_1rrsufr_to,
        price_1_online_nspin_from=price_1_online_nspin_from,
        price_1_online_nspin_to=price_1_online_nspin_to,
        price_1regup_from=price_1regup_from,
        price_1regup_to=price_1regup_to,
        price_1regdn_from=price_1regdn_from,
        price_1regdn_to=price_1regdn_to,
        price_1_offline_nspin_from=price_1_offline_nspin_from,
        price_1_offline_nspin_to=price_1_offline_nspin_to,
        quantity_mw1_from=quantity_mw1_from,
        quantity_mw1_to=quantity_mw1_to,
        block_indicator_2=block_indicator_2,
        price_2rrspfr_from=price_2rrspfr_from,
        price_2rrspfr_to=price_2rrspfr_to,
        page=page,
        size=size,
        sort=sort,
        dir_=dir_,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    price_2rrsffr_from: float | Unset = UNSET,
    price_2rrsffr_to: float | Unset = UNSET,
    price_2rrsufr_from: float | Unset = UNSET,
    price_2rrsufr_to: float | Unset = UNSET,
    price_2_online_nspin_from: float | Unset = UNSET,
    price_2_online_nspin_to: float | Unset = UNSET,
    price_2regup_from: float | Unset = UNSET,
    price_2regup_to: float | Unset = UNSET,
    price_2regdn_from: float | Unset = UNSET,
    price_2regdn_to: float | Unset = UNSET,
    price_2_offline_nspin_from: float | Unset = UNSET,
    price_2_offline_nspin_to: float | Unset = UNSET,
    quantity_mw2_from: int | Unset = UNSET,
    quantity_mw2_to: int | Unset = UNSET,
    block_indicator_3: bool | Unset = UNSET,
    price_3rrspfr_from: float | Unset = UNSET,
    price_3rrspfr_to: float | Unset = UNSET,
    price_3rrsffr_from: float | Unset = UNSET,
    price_3rrsffr_to: float | Unset = UNSET,
    price_3rrsufr_from: float | Unset = UNSET,
    price_3rrsufr_to: float | Unset = UNSET,
    price_3_online_nspin_from: float | Unset = UNSET,
    price_3_online_nspin_to: float | Unset = UNSET,
    price_3regup_from: float | Unset = UNSET,
    price_3regup_to: float | Unset = UNSET,
    price_3regdn_from: float | Unset = UNSET,
    price_3regdn_to: float | Unset = UNSET,
    price_3_offline_nspin_from: float | Unset = UNSET,
    price_3_offline_nspin_to: float | Unset = UNSET,
    quantity_mw3_from: int | Unset = UNSET,
    quantity_mw3_to: int | Unset = UNSET,
    block_indicator_4: bool | Unset = UNSET,
    price_4rrspfr_from: float | Unset = UNSET,
    price_4rrspfr_to: float | Unset = UNSET,
    price_4rrsffr_from: float | Unset = UNSET,
    price_4rrsffr_to: float | Unset = UNSET,
    price_4rrsufr_from: float | Unset = UNSET,
    price_4rrsufr_to: float | Unset = UNSET,
    price_4_online_nspin_from: float | Unset = UNSET,
    price_4_online_nspin_to: float | Unset = UNSET,
    price_4regup_from: float | Unset = UNSET,
    price_4regup_to: float | Unset = UNSET,
    price_4regdn_from: float | Unset = UNSET,
    price_4regdn_to: float | Unset = UNSET,
    price_4_offline_nspin_from: float | Unset = UNSET,
    price_4_offline_nspin_to: float | Unset = UNSET,
    quantity_mw4_from: int | Unset = UNSET,
    quantity_mw4_to: int | Unset = UNSET,
    block_indicator_5: bool | Unset = UNSET,
    price_5rrspfr_from: float | Unset = UNSET,
    price_5rrspfr_to: float | Unset = UNSET,
    price_5rrsffr_from: float | Unset = UNSET,
    price_5rrsffr_to: float | Unset = UNSET,
    price_5rrsufr_from: float | Unset = UNSET,
    price_5rrsufr_to: float | Unset = UNSET,
    price_5_online_nspin_from: float | Unset = UNSET,
    price_5_online_nspin_to: float | Unset = UNSET,
    price_5regup_from: float | Unset = UNSET,
    price_5regup_to: float | Unset = UNSET,
    price_5regdn_from: float | Unset = UNSET,
    price_5regdn_to: float | Unset = UNSET,
    price_5_offline_nspin_from: float | Unset = UNSET,
    price_5_offline_nspin_to: float | Unset = UNSET,
    quantity_mw5_from: int | Unset = UNSET,
    quantity_mw5_to: int | Unset = UNSET,
    delivery_date_from: str | Unset = UNSET,
    delivery_date_to: str | Unset = UNSET,
    hour_ending_from: str | Unset = UNSET,
    hour_ending_to: str | Unset = UNSET,
    qse_name: str | Unset = UNSET,
    dme_name: str | Unset = UNSET,
    resource_name: str | Unset = UNSET,
    multi_hour_block: bool | Unset = UNSET,
    block_indicator_1: bool | Unset = UNSET,
    price_1rrspfr_from: float | Unset = UNSET,
    price_1rrspfr_to: float | Unset = UNSET,
    price_1rrsffr_from: float | Unset = UNSET,
    price_1rrsffr_to: float | Unset = UNSET,
    price_1rrsufr_from: float | Unset = UNSET,
    price_1rrsufr_to: float | Unset = UNSET,
    price_1_online_nspin_from: float | Unset = UNSET,
    price_1_online_nspin_to: float | Unset = UNSET,
    price_1regup_from: float | Unset = UNSET,
    price_1regup_to: float | Unset = UNSET,
    price_1regdn_from: float | Unset = UNSET,
    price_1regdn_to: float | Unset = UNSET,
    price_1_offline_nspin_from: float | Unset = UNSET,
    price_1_offline_nspin_to: float | Unset = UNSET,
    quantity_mw1_from: int | Unset = UNSET,
    quantity_mw1_to: int | Unset = UNSET,
    block_indicator_2: bool | Unset = UNSET,
    price_2rrspfr_from: float | Unset = UNSET,
    price_2rrspfr_to: float | Unset = UNSET,
    page: int | Unset = UNSET,
    size: int | Unset = UNSET,
    sort: str | Unset = UNSET,
    dir_: str | Unset = UNSET,
) -> Response[Exception_ | Report]:
    """60 Day DAM Generation Resources AS Offers

     60 Day DAM Generation Resources AS Offers

    Args:
        price_2rrsffr_from (float | Unset):
        price_2rrsffr_to (float | Unset):
        price_2rrsufr_from (float | Unset):
        price_2rrsufr_to (float | Unset):
        price_2_online_nspin_from (float | Unset):
        price_2_online_nspin_to (float | Unset):
        price_2regup_from (float | Unset):
        price_2regup_to (float | Unset):
        price_2regdn_from (float | Unset):
        price_2regdn_to (float | Unset):
        price_2_offline_nspin_from (float | Unset):
        price_2_offline_nspin_to (float | Unset):
        quantity_mw2_from (int | Unset):
        quantity_mw2_to (int | Unset):
        block_indicator_3 (bool | Unset):
        price_3rrspfr_from (float | Unset):
        price_3rrspfr_to (float | Unset):
        price_3rrsffr_from (float | Unset):
        price_3rrsffr_to (float | Unset):
        price_3rrsufr_from (float | Unset):
        price_3rrsufr_to (float | Unset):
        price_3_online_nspin_from (float | Unset):
        price_3_online_nspin_to (float | Unset):
        price_3regup_from (float | Unset):
        price_3regup_to (float | Unset):
        price_3regdn_from (float | Unset):
        price_3regdn_to (float | Unset):
        price_3_offline_nspin_from (float | Unset):
        price_3_offline_nspin_to (float | Unset):
        quantity_mw3_from (int | Unset):
        quantity_mw3_to (int | Unset):
        block_indicator_4 (bool | Unset):
        price_4rrspfr_from (float | Unset):
        price_4rrspfr_to (float | Unset):
        price_4rrsffr_from (float | Unset):
        price_4rrsffr_to (float | Unset):
        price_4rrsufr_from (float | Unset):
        price_4rrsufr_to (float | Unset):
        price_4_online_nspin_from (float | Unset):
        price_4_online_nspin_to (float | Unset):
        price_4regup_from (float | Unset):
        price_4regup_to (float | Unset):
        price_4regdn_from (float | Unset):
        price_4regdn_to (float | Unset):
        price_4_offline_nspin_from (float | Unset):
        price_4_offline_nspin_to (float | Unset):
        quantity_mw4_from (int | Unset):
        quantity_mw4_to (int | Unset):
        block_indicator_5 (bool | Unset):
        price_5rrspfr_from (float | Unset):
        price_5rrspfr_to (float | Unset):
        price_5rrsffr_from (float | Unset):
        price_5rrsffr_to (float | Unset):
        price_5rrsufr_from (float | Unset):
        price_5rrsufr_to (float | Unset):
        price_5_online_nspin_from (float | Unset):
        price_5_online_nspin_to (float | Unset):
        price_5regup_from (float | Unset):
        price_5regup_to (float | Unset):
        price_5regdn_from (float | Unset):
        price_5regdn_to (float | Unset):
        price_5_offline_nspin_from (float | Unset):
        price_5_offline_nspin_to (float | Unset):
        quantity_mw5_from (int | Unset):
        quantity_mw5_to (int | Unset):
        delivery_date_from (str | Unset):
        delivery_date_to (str | Unset):
        hour_ending_from (str | Unset):
        hour_ending_to (str | Unset):
        qse_name (str | Unset):
        dme_name (str | Unset):
        resource_name (str | Unset):
        multi_hour_block (bool | Unset):
        block_indicator_1 (bool | Unset):
        price_1rrspfr_from (float | Unset):
        price_1rrspfr_to (float | Unset):
        price_1rrsffr_from (float | Unset):
        price_1rrsffr_to (float | Unset):
        price_1rrsufr_from (float | Unset):
        price_1rrsufr_to (float | Unset):
        price_1_online_nspin_from (float | Unset):
        price_1_online_nspin_to (float | Unset):
        price_1regup_from (float | Unset):
        price_1regup_to (float | Unset):
        price_1regdn_from (float | Unset):
        price_1regdn_to (float | Unset):
        price_1_offline_nspin_from (float | Unset):
        price_1_offline_nspin_to (float | Unset):
        quantity_mw1_from (int | Unset):
        quantity_mw1_to (int | Unset):
        block_indicator_2 (bool | Unset):
        price_2rrspfr_from (float | Unset):
        price_2rrspfr_to (float | Unset):
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
        price_2rrsffr_from=price_2rrsffr_from,
        price_2rrsffr_to=price_2rrsffr_to,
        price_2rrsufr_from=price_2rrsufr_from,
        price_2rrsufr_to=price_2rrsufr_to,
        price_2_online_nspin_from=price_2_online_nspin_from,
        price_2_online_nspin_to=price_2_online_nspin_to,
        price_2regup_from=price_2regup_from,
        price_2regup_to=price_2regup_to,
        price_2regdn_from=price_2regdn_from,
        price_2regdn_to=price_2regdn_to,
        price_2_offline_nspin_from=price_2_offline_nspin_from,
        price_2_offline_nspin_to=price_2_offline_nspin_to,
        quantity_mw2_from=quantity_mw2_from,
        quantity_mw2_to=quantity_mw2_to,
        block_indicator_3=block_indicator_3,
        price_3rrspfr_from=price_3rrspfr_from,
        price_3rrspfr_to=price_3rrspfr_to,
        price_3rrsffr_from=price_3rrsffr_from,
        price_3rrsffr_to=price_3rrsffr_to,
        price_3rrsufr_from=price_3rrsufr_from,
        price_3rrsufr_to=price_3rrsufr_to,
        price_3_online_nspin_from=price_3_online_nspin_from,
        price_3_online_nspin_to=price_3_online_nspin_to,
        price_3regup_from=price_3regup_from,
        price_3regup_to=price_3regup_to,
        price_3regdn_from=price_3regdn_from,
        price_3regdn_to=price_3regdn_to,
        price_3_offline_nspin_from=price_3_offline_nspin_from,
        price_3_offline_nspin_to=price_3_offline_nspin_to,
        quantity_mw3_from=quantity_mw3_from,
        quantity_mw3_to=quantity_mw3_to,
        block_indicator_4=block_indicator_4,
        price_4rrspfr_from=price_4rrspfr_from,
        price_4rrspfr_to=price_4rrspfr_to,
        price_4rrsffr_from=price_4rrsffr_from,
        price_4rrsffr_to=price_4rrsffr_to,
        price_4rrsufr_from=price_4rrsufr_from,
        price_4rrsufr_to=price_4rrsufr_to,
        price_4_online_nspin_from=price_4_online_nspin_from,
        price_4_online_nspin_to=price_4_online_nspin_to,
        price_4regup_from=price_4regup_from,
        price_4regup_to=price_4regup_to,
        price_4regdn_from=price_4regdn_from,
        price_4regdn_to=price_4regdn_to,
        price_4_offline_nspin_from=price_4_offline_nspin_from,
        price_4_offline_nspin_to=price_4_offline_nspin_to,
        quantity_mw4_from=quantity_mw4_from,
        quantity_mw4_to=quantity_mw4_to,
        block_indicator_5=block_indicator_5,
        price_5rrspfr_from=price_5rrspfr_from,
        price_5rrspfr_to=price_5rrspfr_to,
        price_5rrsffr_from=price_5rrsffr_from,
        price_5rrsffr_to=price_5rrsffr_to,
        price_5rrsufr_from=price_5rrsufr_from,
        price_5rrsufr_to=price_5rrsufr_to,
        price_5_online_nspin_from=price_5_online_nspin_from,
        price_5_online_nspin_to=price_5_online_nspin_to,
        price_5regup_from=price_5regup_from,
        price_5regup_to=price_5regup_to,
        price_5regdn_from=price_5regdn_from,
        price_5regdn_to=price_5regdn_to,
        price_5_offline_nspin_from=price_5_offline_nspin_from,
        price_5_offline_nspin_to=price_5_offline_nspin_to,
        quantity_mw5_from=quantity_mw5_from,
        quantity_mw5_to=quantity_mw5_to,
        delivery_date_from=delivery_date_from,
        delivery_date_to=delivery_date_to,
        hour_ending_from=hour_ending_from,
        hour_ending_to=hour_ending_to,
        qse_name=qse_name,
        dme_name=dme_name,
        resource_name=resource_name,
        multi_hour_block=multi_hour_block,
        block_indicator_1=block_indicator_1,
        price_1rrspfr_from=price_1rrspfr_from,
        price_1rrspfr_to=price_1rrspfr_to,
        price_1rrsffr_from=price_1rrsffr_from,
        price_1rrsffr_to=price_1rrsffr_to,
        price_1rrsufr_from=price_1rrsufr_from,
        price_1rrsufr_to=price_1rrsufr_to,
        price_1_online_nspin_from=price_1_online_nspin_from,
        price_1_online_nspin_to=price_1_online_nspin_to,
        price_1regup_from=price_1regup_from,
        price_1regup_to=price_1regup_to,
        price_1regdn_from=price_1regdn_from,
        price_1regdn_to=price_1regdn_to,
        price_1_offline_nspin_from=price_1_offline_nspin_from,
        price_1_offline_nspin_to=price_1_offline_nspin_to,
        quantity_mw1_from=quantity_mw1_from,
        quantity_mw1_to=quantity_mw1_to,
        block_indicator_2=block_indicator_2,
        price_2rrspfr_from=price_2rrspfr_from,
        price_2rrspfr_to=price_2rrspfr_to,
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
    price_2rrsffr_from: float | Unset = UNSET,
    price_2rrsffr_to: float | Unset = UNSET,
    price_2rrsufr_from: float | Unset = UNSET,
    price_2rrsufr_to: float | Unset = UNSET,
    price_2_online_nspin_from: float | Unset = UNSET,
    price_2_online_nspin_to: float | Unset = UNSET,
    price_2regup_from: float | Unset = UNSET,
    price_2regup_to: float | Unset = UNSET,
    price_2regdn_from: float | Unset = UNSET,
    price_2regdn_to: float | Unset = UNSET,
    price_2_offline_nspin_from: float | Unset = UNSET,
    price_2_offline_nspin_to: float | Unset = UNSET,
    quantity_mw2_from: int | Unset = UNSET,
    quantity_mw2_to: int | Unset = UNSET,
    block_indicator_3: bool | Unset = UNSET,
    price_3rrspfr_from: float | Unset = UNSET,
    price_3rrspfr_to: float | Unset = UNSET,
    price_3rrsffr_from: float | Unset = UNSET,
    price_3rrsffr_to: float | Unset = UNSET,
    price_3rrsufr_from: float | Unset = UNSET,
    price_3rrsufr_to: float | Unset = UNSET,
    price_3_online_nspin_from: float | Unset = UNSET,
    price_3_online_nspin_to: float | Unset = UNSET,
    price_3regup_from: float | Unset = UNSET,
    price_3regup_to: float | Unset = UNSET,
    price_3regdn_from: float | Unset = UNSET,
    price_3regdn_to: float | Unset = UNSET,
    price_3_offline_nspin_from: float | Unset = UNSET,
    price_3_offline_nspin_to: float | Unset = UNSET,
    quantity_mw3_from: int | Unset = UNSET,
    quantity_mw3_to: int | Unset = UNSET,
    block_indicator_4: bool | Unset = UNSET,
    price_4rrspfr_from: float | Unset = UNSET,
    price_4rrspfr_to: float | Unset = UNSET,
    price_4rrsffr_from: float | Unset = UNSET,
    price_4rrsffr_to: float | Unset = UNSET,
    price_4rrsufr_from: float | Unset = UNSET,
    price_4rrsufr_to: float | Unset = UNSET,
    price_4_online_nspin_from: float | Unset = UNSET,
    price_4_online_nspin_to: float | Unset = UNSET,
    price_4regup_from: float | Unset = UNSET,
    price_4regup_to: float | Unset = UNSET,
    price_4regdn_from: float | Unset = UNSET,
    price_4regdn_to: float | Unset = UNSET,
    price_4_offline_nspin_from: float | Unset = UNSET,
    price_4_offline_nspin_to: float | Unset = UNSET,
    quantity_mw4_from: int | Unset = UNSET,
    quantity_mw4_to: int | Unset = UNSET,
    block_indicator_5: bool | Unset = UNSET,
    price_5rrspfr_from: float | Unset = UNSET,
    price_5rrspfr_to: float | Unset = UNSET,
    price_5rrsffr_from: float | Unset = UNSET,
    price_5rrsffr_to: float | Unset = UNSET,
    price_5rrsufr_from: float | Unset = UNSET,
    price_5rrsufr_to: float | Unset = UNSET,
    price_5_online_nspin_from: float | Unset = UNSET,
    price_5_online_nspin_to: float | Unset = UNSET,
    price_5regup_from: float | Unset = UNSET,
    price_5regup_to: float | Unset = UNSET,
    price_5regdn_from: float | Unset = UNSET,
    price_5regdn_to: float | Unset = UNSET,
    price_5_offline_nspin_from: float | Unset = UNSET,
    price_5_offline_nspin_to: float | Unset = UNSET,
    quantity_mw5_from: int | Unset = UNSET,
    quantity_mw5_to: int | Unset = UNSET,
    delivery_date_from: str | Unset = UNSET,
    delivery_date_to: str | Unset = UNSET,
    hour_ending_from: str | Unset = UNSET,
    hour_ending_to: str | Unset = UNSET,
    qse_name: str | Unset = UNSET,
    dme_name: str | Unset = UNSET,
    resource_name: str | Unset = UNSET,
    multi_hour_block: bool | Unset = UNSET,
    block_indicator_1: bool | Unset = UNSET,
    price_1rrspfr_from: float | Unset = UNSET,
    price_1rrspfr_to: float | Unset = UNSET,
    price_1rrsffr_from: float | Unset = UNSET,
    price_1rrsffr_to: float | Unset = UNSET,
    price_1rrsufr_from: float | Unset = UNSET,
    price_1rrsufr_to: float | Unset = UNSET,
    price_1_online_nspin_from: float | Unset = UNSET,
    price_1_online_nspin_to: float | Unset = UNSET,
    price_1regup_from: float | Unset = UNSET,
    price_1regup_to: float | Unset = UNSET,
    price_1regdn_from: float | Unset = UNSET,
    price_1regdn_to: float | Unset = UNSET,
    price_1_offline_nspin_from: float | Unset = UNSET,
    price_1_offline_nspin_to: float | Unset = UNSET,
    quantity_mw1_from: int | Unset = UNSET,
    quantity_mw1_to: int | Unset = UNSET,
    block_indicator_2: bool | Unset = UNSET,
    price_2rrspfr_from: float | Unset = UNSET,
    price_2rrspfr_to: float | Unset = UNSET,
    page: int | Unset = UNSET,
    size: int | Unset = UNSET,
    sort: str | Unset = UNSET,
    dir_: str | Unset = UNSET,
) -> Exception_ | Report | None:
    """60 Day DAM Generation Resources AS Offers

     60 Day DAM Generation Resources AS Offers

    Args:
        price_2rrsffr_from (float | Unset):
        price_2rrsffr_to (float | Unset):
        price_2rrsufr_from (float | Unset):
        price_2rrsufr_to (float | Unset):
        price_2_online_nspin_from (float | Unset):
        price_2_online_nspin_to (float | Unset):
        price_2regup_from (float | Unset):
        price_2regup_to (float | Unset):
        price_2regdn_from (float | Unset):
        price_2regdn_to (float | Unset):
        price_2_offline_nspin_from (float | Unset):
        price_2_offline_nspin_to (float | Unset):
        quantity_mw2_from (int | Unset):
        quantity_mw2_to (int | Unset):
        block_indicator_3 (bool | Unset):
        price_3rrspfr_from (float | Unset):
        price_3rrspfr_to (float | Unset):
        price_3rrsffr_from (float | Unset):
        price_3rrsffr_to (float | Unset):
        price_3rrsufr_from (float | Unset):
        price_3rrsufr_to (float | Unset):
        price_3_online_nspin_from (float | Unset):
        price_3_online_nspin_to (float | Unset):
        price_3regup_from (float | Unset):
        price_3regup_to (float | Unset):
        price_3regdn_from (float | Unset):
        price_3regdn_to (float | Unset):
        price_3_offline_nspin_from (float | Unset):
        price_3_offline_nspin_to (float | Unset):
        quantity_mw3_from (int | Unset):
        quantity_mw3_to (int | Unset):
        block_indicator_4 (bool | Unset):
        price_4rrspfr_from (float | Unset):
        price_4rrspfr_to (float | Unset):
        price_4rrsffr_from (float | Unset):
        price_4rrsffr_to (float | Unset):
        price_4rrsufr_from (float | Unset):
        price_4rrsufr_to (float | Unset):
        price_4_online_nspin_from (float | Unset):
        price_4_online_nspin_to (float | Unset):
        price_4regup_from (float | Unset):
        price_4regup_to (float | Unset):
        price_4regdn_from (float | Unset):
        price_4regdn_to (float | Unset):
        price_4_offline_nspin_from (float | Unset):
        price_4_offline_nspin_to (float | Unset):
        quantity_mw4_from (int | Unset):
        quantity_mw4_to (int | Unset):
        block_indicator_5 (bool | Unset):
        price_5rrspfr_from (float | Unset):
        price_5rrspfr_to (float | Unset):
        price_5rrsffr_from (float | Unset):
        price_5rrsffr_to (float | Unset):
        price_5rrsufr_from (float | Unset):
        price_5rrsufr_to (float | Unset):
        price_5_online_nspin_from (float | Unset):
        price_5_online_nspin_to (float | Unset):
        price_5regup_from (float | Unset):
        price_5regup_to (float | Unset):
        price_5regdn_from (float | Unset):
        price_5regdn_to (float | Unset):
        price_5_offline_nspin_from (float | Unset):
        price_5_offline_nspin_to (float | Unset):
        quantity_mw5_from (int | Unset):
        quantity_mw5_to (int | Unset):
        delivery_date_from (str | Unset):
        delivery_date_to (str | Unset):
        hour_ending_from (str | Unset):
        hour_ending_to (str | Unset):
        qse_name (str | Unset):
        dme_name (str | Unset):
        resource_name (str | Unset):
        multi_hour_block (bool | Unset):
        block_indicator_1 (bool | Unset):
        price_1rrspfr_from (float | Unset):
        price_1rrspfr_to (float | Unset):
        price_1rrsffr_from (float | Unset):
        price_1rrsffr_to (float | Unset):
        price_1rrsufr_from (float | Unset):
        price_1rrsufr_to (float | Unset):
        price_1_online_nspin_from (float | Unset):
        price_1_online_nspin_to (float | Unset):
        price_1regup_from (float | Unset):
        price_1regup_to (float | Unset):
        price_1regdn_from (float | Unset):
        price_1regdn_to (float | Unset):
        price_1_offline_nspin_from (float | Unset):
        price_1_offline_nspin_to (float | Unset):
        quantity_mw1_from (int | Unset):
        quantity_mw1_to (int | Unset):
        block_indicator_2 (bool | Unset):
        price_2rrspfr_from (float | Unset):
        price_2rrspfr_to (float | Unset):
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
            price_2rrsffr_from=price_2rrsffr_from,
            price_2rrsffr_to=price_2rrsffr_to,
            price_2rrsufr_from=price_2rrsufr_from,
            price_2rrsufr_to=price_2rrsufr_to,
            price_2_online_nspin_from=price_2_online_nspin_from,
            price_2_online_nspin_to=price_2_online_nspin_to,
            price_2regup_from=price_2regup_from,
            price_2regup_to=price_2regup_to,
            price_2regdn_from=price_2regdn_from,
            price_2regdn_to=price_2regdn_to,
            price_2_offline_nspin_from=price_2_offline_nspin_from,
            price_2_offline_nspin_to=price_2_offline_nspin_to,
            quantity_mw2_from=quantity_mw2_from,
            quantity_mw2_to=quantity_mw2_to,
            block_indicator_3=block_indicator_3,
            price_3rrspfr_from=price_3rrspfr_from,
            price_3rrspfr_to=price_3rrspfr_to,
            price_3rrsffr_from=price_3rrsffr_from,
            price_3rrsffr_to=price_3rrsffr_to,
            price_3rrsufr_from=price_3rrsufr_from,
            price_3rrsufr_to=price_3rrsufr_to,
            price_3_online_nspin_from=price_3_online_nspin_from,
            price_3_online_nspin_to=price_3_online_nspin_to,
            price_3regup_from=price_3regup_from,
            price_3regup_to=price_3regup_to,
            price_3regdn_from=price_3regdn_from,
            price_3regdn_to=price_3regdn_to,
            price_3_offline_nspin_from=price_3_offline_nspin_from,
            price_3_offline_nspin_to=price_3_offline_nspin_to,
            quantity_mw3_from=quantity_mw3_from,
            quantity_mw3_to=quantity_mw3_to,
            block_indicator_4=block_indicator_4,
            price_4rrspfr_from=price_4rrspfr_from,
            price_4rrspfr_to=price_4rrspfr_to,
            price_4rrsffr_from=price_4rrsffr_from,
            price_4rrsffr_to=price_4rrsffr_to,
            price_4rrsufr_from=price_4rrsufr_from,
            price_4rrsufr_to=price_4rrsufr_to,
            price_4_online_nspin_from=price_4_online_nspin_from,
            price_4_online_nspin_to=price_4_online_nspin_to,
            price_4regup_from=price_4regup_from,
            price_4regup_to=price_4regup_to,
            price_4regdn_from=price_4regdn_from,
            price_4regdn_to=price_4regdn_to,
            price_4_offline_nspin_from=price_4_offline_nspin_from,
            price_4_offline_nspin_to=price_4_offline_nspin_to,
            quantity_mw4_from=quantity_mw4_from,
            quantity_mw4_to=quantity_mw4_to,
            block_indicator_5=block_indicator_5,
            price_5rrspfr_from=price_5rrspfr_from,
            price_5rrspfr_to=price_5rrspfr_to,
            price_5rrsffr_from=price_5rrsffr_from,
            price_5rrsffr_to=price_5rrsffr_to,
            price_5rrsufr_from=price_5rrsufr_from,
            price_5rrsufr_to=price_5rrsufr_to,
            price_5_online_nspin_from=price_5_online_nspin_from,
            price_5_online_nspin_to=price_5_online_nspin_to,
            price_5regup_from=price_5regup_from,
            price_5regup_to=price_5regup_to,
            price_5regdn_from=price_5regdn_from,
            price_5regdn_to=price_5regdn_to,
            price_5_offline_nspin_from=price_5_offline_nspin_from,
            price_5_offline_nspin_to=price_5_offline_nspin_to,
            quantity_mw5_from=quantity_mw5_from,
            quantity_mw5_to=quantity_mw5_to,
            delivery_date_from=delivery_date_from,
            delivery_date_to=delivery_date_to,
            hour_ending_from=hour_ending_from,
            hour_ending_to=hour_ending_to,
            qse_name=qse_name,
            dme_name=dme_name,
            resource_name=resource_name,
            multi_hour_block=multi_hour_block,
            block_indicator_1=block_indicator_1,
            price_1rrspfr_from=price_1rrspfr_from,
            price_1rrspfr_to=price_1rrspfr_to,
            price_1rrsffr_from=price_1rrsffr_from,
            price_1rrsffr_to=price_1rrsffr_to,
            price_1rrsufr_from=price_1rrsufr_from,
            price_1rrsufr_to=price_1rrsufr_to,
            price_1_online_nspin_from=price_1_online_nspin_from,
            price_1_online_nspin_to=price_1_online_nspin_to,
            price_1regup_from=price_1regup_from,
            price_1regup_to=price_1regup_to,
            price_1regdn_from=price_1regdn_from,
            price_1regdn_to=price_1regdn_to,
            price_1_offline_nspin_from=price_1_offline_nspin_from,
            price_1_offline_nspin_to=price_1_offline_nspin_to,
            quantity_mw1_from=quantity_mw1_from,
            quantity_mw1_to=quantity_mw1_to,
            block_indicator_2=block_indicator_2,
            price_2rrspfr_from=price_2rrspfr_from,
            price_2rrspfr_to=price_2rrspfr_to,
            page=page,
            size=size,
            sort=sort,
            dir_=dir_,
        )
    ).parsed
