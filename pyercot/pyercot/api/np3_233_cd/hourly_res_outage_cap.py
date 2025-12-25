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
    operating_date_from: str | Unset = UNSET,
    operating_date_to: str | Unset = UNSET,
    hour_ending_from: int | Unset = UNSET,
    hour_ending_to: int | Unset = UNSET,
    total_resource_mw_zone_south_from: int | Unset = UNSET,
    total_resource_mw_zone_south_to: int | Unset = UNSET,
    total_resource_mw_zone_north_from: int | Unset = UNSET,
    total_resource_mw_zone_north_to: int | Unset = UNSET,
    total_resource_mw_zone_west_from: int | Unset = UNSET,
    total_resource_mw_zone_west_to: int | Unset = UNSET,
    total_resource_mw_zone_houston_from: int | Unset = UNSET,
    total_resource_mw_zone_houston_to: int | Unset = UNSET,
    total_irrmw_zone_south_from: int | Unset = UNSET,
    total_irrmw_zone_south_to: int | Unset = UNSET,
    total_irrmw_zone_north_from: int | Unset = UNSET,
    total_irrmw_zone_north_to: int | Unset = UNSET,
    total_irrmw_zone_west_from: int | Unset = UNSET,
    total_irrmw_zone_west_to: int | Unset = UNSET,
    total_irrmw_zone_houston_from: int | Unset = UNSET,
    total_irrmw_zone_houston_to: int | Unset = UNSET,
    total_new_equip_resource_mw_zone_south_from: int | Unset = UNSET,
    total_new_equip_resource_mw_zone_south_to: int | Unset = UNSET,
    total_new_equip_resource_mw_zone_north_from: int | Unset = UNSET,
    total_new_equip_resource_mw_zone_north_to: int | Unset = UNSET,
    total_new_equip_resource_mw_zone_west_from: int | Unset = UNSET,
    total_new_equip_resource_mw_zone_west_to: int | Unset = UNSET,
    total_new_equip_resource_mw_zone_houston_from: int | Unset = UNSET,
    total_new_equip_resource_mw_zone_houston_to: int | Unset = UNSET,
    posted_datetime_from: str | Unset = UNSET,
    posted_datetime_to: str | Unset = UNSET,
    page: int | Unset = UNSET,
    size: int | Unset = UNSET,
    sort: str | Unset = UNSET,
    dir_: str | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["operatingDateFrom"] = operating_date_from

    params["operatingDateTo"] = operating_date_to

    params["hourEndingFrom"] = hour_ending_from

    params["hourEndingTo"] = hour_ending_to

    params["totalResourceMWZoneSouthFrom"] = total_resource_mw_zone_south_from

    params["totalResourceMWZoneSouthTo"] = total_resource_mw_zone_south_to

    params["totalResourceMWZoneNorthFrom"] = total_resource_mw_zone_north_from

    params["totalResourceMWZoneNorthTo"] = total_resource_mw_zone_north_to

    params["totalResourceMWZoneWestFrom"] = total_resource_mw_zone_west_from

    params["totalResourceMWZoneWestTo"] = total_resource_mw_zone_west_to

    params["totalResourceMWZoneHoustonFrom"] = total_resource_mw_zone_houston_from

    params["totalResourceMWZoneHoustonTo"] = total_resource_mw_zone_houston_to

    params["totalIRRMWZoneSouthFrom"] = total_irrmw_zone_south_from

    params["totalIRRMWZoneSouthTo"] = total_irrmw_zone_south_to

    params["totalIRRMWZoneNorthFrom"] = total_irrmw_zone_north_from

    params["totalIRRMWZoneNorthTo"] = total_irrmw_zone_north_to

    params["totalIRRMWZoneWestFrom"] = total_irrmw_zone_west_from

    params["totalIRRMWZoneWestTo"] = total_irrmw_zone_west_to

    params["totalIRRMWZoneHoustonFrom"] = total_irrmw_zone_houston_from

    params["totalIRRMWZoneHoustonTo"] = total_irrmw_zone_houston_to

    params["totalNewEquipResourceMWZoneSouthFrom"] = total_new_equip_resource_mw_zone_south_from

    params["totalNewEquipResourceMWZoneSouthTo"] = total_new_equip_resource_mw_zone_south_to

    params["totalNewEquipResourceMWZoneNorthFrom"] = total_new_equip_resource_mw_zone_north_from

    params["totalNewEquipResourceMWZoneNorthTo"] = total_new_equip_resource_mw_zone_north_to

    params["totalNewEquipResourceMWZoneWestFrom"] = total_new_equip_resource_mw_zone_west_from

    params["totalNewEquipResourceMWZoneWestTo"] = total_new_equip_resource_mw_zone_west_to

    params["totalNewEquipResourceMWZoneHoustonFrom"] = total_new_equip_resource_mw_zone_houston_from

    params["totalNewEquipResourceMWZoneHoustonTo"] = total_new_equip_resource_mw_zone_houston_to

    params["postedDatetimeFrom"] = posted_datetime_from

    params["postedDatetimeTo"] = posted_datetime_to

    params["page"] = page

    params["size"] = size

    params["sort"] = sort

    params["dir"] = dir_

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/np3-233-cd/hourly_res_outage_cap",
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
    operating_date_from: str | Unset = UNSET,
    operating_date_to: str | Unset = UNSET,
    hour_ending_from: int | Unset = UNSET,
    hour_ending_to: int | Unset = UNSET,
    total_resource_mw_zone_south_from: int | Unset = UNSET,
    total_resource_mw_zone_south_to: int | Unset = UNSET,
    total_resource_mw_zone_north_from: int | Unset = UNSET,
    total_resource_mw_zone_north_to: int | Unset = UNSET,
    total_resource_mw_zone_west_from: int | Unset = UNSET,
    total_resource_mw_zone_west_to: int | Unset = UNSET,
    total_resource_mw_zone_houston_from: int | Unset = UNSET,
    total_resource_mw_zone_houston_to: int | Unset = UNSET,
    total_irrmw_zone_south_from: int | Unset = UNSET,
    total_irrmw_zone_south_to: int | Unset = UNSET,
    total_irrmw_zone_north_from: int | Unset = UNSET,
    total_irrmw_zone_north_to: int | Unset = UNSET,
    total_irrmw_zone_west_from: int | Unset = UNSET,
    total_irrmw_zone_west_to: int | Unset = UNSET,
    total_irrmw_zone_houston_from: int | Unset = UNSET,
    total_irrmw_zone_houston_to: int | Unset = UNSET,
    total_new_equip_resource_mw_zone_south_from: int | Unset = UNSET,
    total_new_equip_resource_mw_zone_south_to: int | Unset = UNSET,
    total_new_equip_resource_mw_zone_north_from: int | Unset = UNSET,
    total_new_equip_resource_mw_zone_north_to: int | Unset = UNSET,
    total_new_equip_resource_mw_zone_west_from: int | Unset = UNSET,
    total_new_equip_resource_mw_zone_west_to: int | Unset = UNSET,
    total_new_equip_resource_mw_zone_houston_from: int | Unset = UNSET,
    total_new_equip_resource_mw_zone_houston_to: int | Unset = UNSET,
    posted_datetime_from: str | Unset = UNSET,
    posted_datetime_to: str | Unset = UNSET,
    page: int | Unset = UNSET,
    size: int | Unset = UNSET,
    sort: str | Unset = UNSET,
    dir_: str | Unset = UNSET,
) -> Response[Exception_ | Report]:
    """Hourly Resource Outage Capacity

     Hourly Resource Outage Capacity

    Args:
        operating_date_from (str | Unset):
        operating_date_to (str | Unset):
        hour_ending_from (int | Unset):
        hour_ending_to (int | Unset):
        total_resource_mw_zone_south_from (int | Unset):
        total_resource_mw_zone_south_to (int | Unset):
        total_resource_mw_zone_north_from (int | Unset):
        total_resource_mw_zone_north_to (int | Unset):
        total_resource_mw_zone_west_from (int | Unset):
        total_resource_mw_zone_west_to (int | Unset):
        total_resource_mw_zone_houston_from (int | Unset):
        total_resource_mw_zone_houston_to (int | Unset):
        total_irrmw_zone_south_from (int | Unset):
        total_irrmw_zone_south_to (int | Unset):
        total_irrmw_zone_north_from (int | Unset):
        total_irrmw_zone_north_to (int | Unset):
        total_irrmw_zone_west_from (int | Unset):
        total_irrmw_zone_west_to (int | Unset):
        total_irrmw_zone_houston_from (int | Unset):
        total_irrmw_zone_houston_to (int | Unset):
        total_new_equip_resource_mw_zone_south_from (int | Unset):
        total_new_equip_resource_mw_zone_south_to (int | Unset):
        total_new_equip_resource_mw_zone_north_from (int | Unset):
        total_new_equip_resource_mw_zone_north_to (int | Unset):
        total_new_equip_resource_mw_zone_west_from (int | Unset):
        total_new_equip_resource_mw_zone_west_to (int | Unset):
        total_new_equip_resource_mw_zone_houston_from (int | Unset):
        total_new_equip_resource_mw_zone_houston_to (int | Unset):
        posted_datetime_from (str | Unset):
        posted_datetime_to (str | Unset):
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
        operating_date_from=operating_date_from,
        operating_date_to=operating_date_to,
        hour_ending_from=hour_ending_from,
        hour_ending_to=hour_ending_to,
        total_resource_mw_zone_south_from=total_resource_mw_zone_south_from,
        total_resource_mw_zone_south_to=total_resource_mw_zone_south_to,
        total_resource_mw_zone_north_from=total_resource_mw_zone_north_from,
        total_resource_mw_zone_north_to=total_resource_mw_zone_north_to,
        total_resource_mw_zone_west_from=total_resource_mw_zone_west_from,
        total_resource_mw_zone_west_to=total_resource_mw_zone_west_to,
        total_resource_mw_zone_houston_from=total_resource_mw_zone_houston_from,
        total_resource_mw_zone_houston_to=total_resource_mw_zone_houston_to,
        total_irrmw_zone_south_from=total_irrmw_zone_south_from,
        total_irrmw_zone_south_to=total_irrmw_zone_south_to,
        total_irrmw_zone_north_from=total_irrmw_zone_north_from,
        total_irrmw_zone_north_to=total_irrmw_zone_north_to,
        total_irrmw_zone_west_from=total_irrmw_zone_west_from,
        total_irrmw_zone_west_to=total_irrmw_zone_west_to,
        total_irrmw_zone_houston_from=total_irrmw_zone_houston_from,
        total_irrmw_zone_houston_to=total_irrmw_zone_houston_to,
        total_new_equip_resource_mw_zone_south_from=total_new_equip_resource_mw_zone_south_from,
        total_new_equip_resource_mw_zone_south_to=total_new_equip_resource_mw_zone_south_to,
        total_new_equip_resource_mw_zone_north_from=total_new_equip_resource_mw_zone_north_from,
        total_new_equip_resource_mw_zone_north_to=total_new_equip_resource_mw_zone_north_to,
        total_new_equip_resource_mw_zone_west_from=total_new_equip_resource_mw_zone_west_from,
        total_new_equip_resource_mw_zone_west_to=total_new_equip_resource_mw_zone_west_to,
        total_new_equip_resource_mw_zone_houston_from=total_new_equip_resource_mw_zone_houston_from,
        total_new_equip_resource_mw_zone_houston_to=total_new_equip_resource_mw_zone_houston_to,
        posted_datetime_from=posted_datetime_from,
        posted_datetime_to=posted_datetime_to,
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
    operating_date_from: str | Unset = UNSET,
    operating_date_to: str | Unset = UNSET,
    hour_ending_from: int | Unset = UNSET,
    hour_ending_to: int | Unset = UNSET,
    total_resource_mw_zone_south_from: int | Unset = UNSET,
    total_resource_mw_zone_south_to: int | Unset = UNSET,
    total_resource_mw_zone_north_from: int | Unset = UNSET,
    total_resource_mw_zone_north_to: int | Unset = UNSET,
    total_resource_mw_zone_west_from: int | Unset = UNSET,
    total_resource_mw_zone_west_to: int | Unset = UNSET,
    total_resource_mw_zone_houston_from: int | Unset = UNSET,
    total_resource_mw_zone_houston_to: int | Unset = UNSET,
    total_irrmw_zone_south_from: int | Unset = UNSET,
    total_irrmw_zone_south_to: int | Unset = UNSET,
    total_irrmw_zone_north_from: int | Unset = UNSET,
    total_irrmw_zone_north_to: int | Unset = UNSET,
    total_irrmw_zone_west_from: int | Unset = UNSET,
    total_irrmw_zone_west_to: int | Unset = UNSET,
    total_irrmw_zone_houston_from: int | Unset = UNSET,
    total_irrmw_zone_houston_to: int | Unset = UNSET,
    total_new_equip_resource_mw_zone_south_from: int | Unset = UNSET,
    total_new_equip_resource_mw_zone_south_to: int | Unset = UNSET,
    total_new_equip_resource_mw_zone_north_from: int | Unset = UNSET,
    total_new_equip_resource_mw_zone_north_to: int | Unset = UNSET,
    total_new_equip_resource_mw_zone_west_from: int | Unset = UNSET,
    total_new_equip_resource_mw_zone_west_to: int | Unset = UNSET,
    total_new_equip_resource_mw_zone_houston_from: int | Unset = UNSET,
    total_new_equip_resource_mw_zone_houston_to: int | Unset = UNSET,
    posted_datetime_from: str | Unset = UNSET,
    posted_datetime_to: str | Unset = UNSET,
    page: int | Unset = UNSET,
    size: int | Unset = UNSET,
    sort: str | Unset = UNSET,
    dir_: str | Unset = UNSET,
) -> Exception_ | Report | None:
    """Hourly Resource Outage Capacity

     Hourly Resource Outage Capacity

    Args:
        operating_date_from (str | Unset):
        operating_date_to (str | Unset):
        hour_ending_from (int | Unset):
        hour_ending_to (int | Unset):
        total_resource_mw_zone_south_from (int | Unset):
        total_resource_mw_zone_south_to (int | Unset):
        total_resource_mw_zone_north_from (int | Unset):
        total_resource_mw_zone_north_to (int | Unset):
        total_resource_mw_zone_west_from (int | Unset):
        total_resource_mw_zone_west_to (int | Unset):
        total_resource_mw_zone_houston_from (int | Unset):
        total_resource_mw_zone_houston_to (int | Unset):
        total_irrmw_zone_south_from (int | Unset):
        total_irrmw_zone_south_to (int | Unset):
        total_irrmw_zone_north_from (int | Unset):
        total_irrmw_zone_north_to (int | Unset):
        total_irrmw_zone_west_from (int | Unset):
        total_irrmw_zone_west_to (int | Unset):
        total_irrmw_zone_houston_from (int | Unset):
        total_irrmw_zone_houston_to (int | Unset):
        total_new_equip_resource_mw_zone_south_from (int | Unset):
        total_new_equip_resource_mw_zone_south_to (int | Unset):
        total_new_equip_resource_mw_zone_north_from (int | Unset):
        total_new_equip_resource_mw_zone_north_to (int | Unset):
        total_new_equip_resource_mw_zone_west_from (int | Unset):
        total_new_equip_resource_mw_zone_west_to (int | Unset):
        total_new_equip_resource_mw_zone_houston_from (int | Unset):
        total_new_equip_resource_mw_zone_houston_to (int | Unset):
        posted_datetime_from (str | Unset):
        posted_datetime_to (str | Unset):
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
        operating_date_from=operating_date_from,
        operating_date_to=operating_date_to,
        hour_ending_from=hour_ending_from,
        hour_ending_to=hour_ending_to,
        total_resource_mw_zone_south_from=total_resource_mw_zone_south_from,
        total_resource_mw_zone_south_to=total_resource_mw_zone_south_to,
        total_resource_mw_zone_north_from=total_resource_mw_zone_north_from,
        total_resource_mw_zone_north_to=total_resource_mw_zone_north_to,
        total_resource_mw_zone_west_from=total_resource_mw_zone_west_from,
        total_resource_mw_zone_west_to=total_resource_mw_zone_west_to,
        total_resource_mw_zone_houston_from=total_resource_mw_zone_houston_from,
        total_resource_mw_zone_houston_to=total_resource_mw_zone_houston_to,
        total_irrmw_zone_south_from=total_irrmw_zone_south_from,
        total_irrmw_zone_south_to=total_irrmw_zone_south_to,
        total_irrmw_zone_north_from=total_irrmw_zone_north_from,
        total_irrmw_zone_north_to=total_irrmw_zone_north_to,
        total_irrmw_zone_west_from=total_irrmw_zone_west_from,
        total_irrmw_zone_west_to=total_irrmw_zone_west_to,
        total_irrmw_zone_houston_from=total_irrmw_zone_houston_from,
        total_irrmw_zone_houston_to=total_irrmw_zone_houston_to,
        total_new_equip_resource_mw_zone_south_from=total_new_equip_resource_mw_zone_south_from,
        total_new_equip_resource_mw_zone_south_to=total_new_equip_resource_mw_zone_south_to,
        total_new_equip_resource_mw_zone_north_from=total_new_equip_resource_mw_zone_north_from,
        total_new_equip_resource_mw_zone_north_to=total_new_equip_resource_mw_zone_north_to,
        total_new_equip_resource_mw_zone_west_from=total_new_equip_resource_mw_zone_west_from,
        total_new_equip_resource_mw_zone_west_to=total_new_equip_resource_mw_zone_west_to,
        total_new_equip_resource_mw_zone_houston_from=total_new_equip_resource_mw_zone_houston_from,
        total_new_equip_resource_mw_zone_houston_to=total_new_equip_resource_mw_zone_houston_to,
        posted_datetime_from=posted_datetime_from,
        posted_datetime_to=posted_datetime_to,
        page=page,
        size=size,
        sort=sort,
        dir_=dir_,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    operating_date_from: str | Unset = UNSET,
    operating_date_to: str | Unset = UNSET,
    hour_ending_from: int | Unset = UNSET,
    hour_ending_to: int | Unset = UNSET,
    total_resource_mw_zone_south_from: int | Unset = UNSET,
    total_resource_mw_zone_south_to: int | Unset = UNSET,
    total_resource_mw_zone_north_from: int | Unset = UNSET,
    total_resource_mw_zone_north_to: int | Unset = UNSET,
    total_resource_mw_zone_west_from: int | Unset = UNSET,
    total_resource_mw_zone_west_to: int | Unset = UNSET,
    total_resource_mw_zone_houston_from: int | Unset = UNSET,
    total_resource_mw_zone_houston_to: int | Unset = UNSET,
    total_irrmw_zone_south_from: int | Unset = UNSET,
    total_irrmw_zone_south_to: int | Unset = UNSET,
    total_irrmw_zone_north_from: int | Unset = UNSET,
    total_irrmw_zone_north_to: int | Unset = UNSET,
    total_irrmw_zone_west_from: int | Unset = UNSET,
    total_irrmw_zone_west_to: int | Unset = UNSET,
    total_irrmw_zone_houston_from: int | Unset = UNSET,
    total_irrmw_zone_houston_to: int | Unset = UNSET,
    total_new_equip_resource_mw_zone_south_from: int | Unset = UNSET,
    total_new_equip_resource_mw_zone_south_to: int | Unset = UNSET,
    total_new_equip_resource_mw_zone_north_from: int | Unset = UNSET,
    total_new_equip_resource_mw_zone_north_to: int | Unset = UNSET,
    total_new_equip_resource_mw_zone_west_from: int | Unset = UNSET,
    total_new_equip_resource_mw_zone_west_to: int | Unset = UNSET,
    total_new_equip_resource_mw_zone_houston_from: int | Unset = UNSET,
    total_new_equip_resource_mw_zone_houston_to: int | Unset = UNSET,
    posted_datetime_from: str | Unset = UNSET,
    posted_datetime_to: str | Unset = UNSET,
    page: int | Unset = UNSET,
    size: int | Unset = UNSET,
    sort: str | Unset = UNSET,
    dir_: str | Unset = UNSET,
) -> Response[Exception_ | Report]:
    """Hourly Resource Outage Capacity

     Hourly Resource Outage Capacity

    Args:
        operating_date_from (str | Unset):
        operating_date_to (str | Unset):
        hour_ending_from (int | Unset):
        hour_ending_to (int | Unset):
        total_resource_mw_zone_south_from (int | Unset):
        total_resource_mw_zone_south_to (int | Unset):
        total_resource_mw_zone_north_from (int | Unset):
        total_resource_mw_zone_north_to (int | Unset):
        total_resource_mw_zone_west_from (int | Unset):
        total_resource_mw_zone_west_to (int | Unset):
        total_resource_mw_zone_houston_from (int | Unset):
        total_resource_mw_zone_houston_to (int | Unset):
        total_irrmw_zone_south_from (int | Unset):
        total_irrmw_zone_south_to (int | Unset):
        total_irrmw_zone_north_from (int | Unset):
        total_irrmw_zone_north_to (int | Unset):
        total_irrmw_zone_west_from (int | Unset):
        total_irrmw_zone_west_to (int | Unset):
        total_irrmw_zone_houston_from (int | Unset):
        total_irrmw_zone_houston_to (int | Unset):
        total_new_equip_resource_mw_zone_south_from (int | Unset):
        total_new_equip_resource_mw_zone_south_to (int | Unset):
        total_new_equip_resource_mw_zone_north_from (int | Unset):
        total_new_equip_resource_mw_zone_north_to (int | Unset):
        total_new_equip_resource_mw_zone_west_from (int | Unset):
        total_new_equip_resource_mw_zone_west_to (int | Unset):
        total_new_equip_resource_mw_zone_houston_from (int | Unset):
        total_new_equip_resource_mw_zone_houston_to (int | Unset):
        posted_datetime_from (str | Unset):
        posted_datetime_to (str | Unset):
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
        operating_date_from=operating_date_from,
        operating_date_to=operating_date_to,
        hour_ending_from=hour_ending_from,
        hour_ending_to=hour_ending_to,
        total_resource_mw_zone_south_from=total_resource_mw_zone_south_from,
        total_resource_mw_zone_south_to=total_resource_mw_zone_south_to,
        total_resource_mw_zone_north_from=total_resource_mw_zone_north_from,
        total_resource_mw_zone_north_to=total_resource_mw_zone_north_to,
        total_resource_mw_zone_west_from=total_resource_mw_zone_west_from,
        total_resource_mw_zone_west_to=total_resource_mw_zone_west_to,
        total_resource_mw_zone_houston_from=total_resource_mw_zone_houston_from,
        total_resource_mw_zone_houston_to=total_resource_mw_zone_houston_to,
        total_irrmw_zone_south_from=total_irrmw_zone_south_from,
        total_irrmw_zone_south_to=total_irrmw_zone_south_to,
        total_irrmw_zone_north_from=total_irrmw_zone_north_from,
        total_irrmw_zone_north_to=total_irrmw_zone_north_to,
        total_irrmw_zone_west_from=total_irrmw_zone_west_from,
        total_irrmw_zone_west_to=total_irrmw_zone_west_to,
        total_irrmw_zone_houston_from=total_irrmw_zone_houston_from,
        total_irrmw_zone_houston_to=total_irrmw_zone_houston_to,
        total_new_equip_resource_mw_zone_south_from=total_new_equip_resource_mw_zone_south_from,
        total_new_equip_resource_mw_zone_south_to=total_new_equip_resource_mw_zone_south_to,
        total_new_equip_resource_mw_zone_north_from=total_new_equip_resource_mw_zone_north_from,
        total_new_equip_resource_mw_zone_north_to=total_new_equip_resource_mw_zone_north_to,
        total_new_equip_resource_mw_zone_west_from=total_new_equip_resource_mw_zone_west_from,
        total_new_equip_resource_mw_zone_west_to=total_new_equip_resource_mw_zone_west_to,
        total_new_equip_resource_mw_zone_houston_from=total_new_equip_resource_mw_zone_houston_from,
        total_new_equip_resource_mw_zone_houston_to=total_new_equip_resource_mw_zone_houston_to,
        posted_datetime_from=posted_datetime_from,
        posted_datetime_to=posted_datetime_to,
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
    operating_date_from: str | Unset = UNSET,
    operating_date_to: str | Unset = UNSET,
    hour_ending_from: int | Unset = UNSET,
    hour_ending_to: int | Unset = UNSET,
    total_resource_mw_zone_south_from: int | Unset = UNSET,
    total_resource_mw_zone_south_to: int | Unset = UNSET,
    total_resource_mw_zone_north_from: int | Unset = UNSET,
    total_resource_mw_zone_north_to: int | Unset = UNSET,
    total_resource_mw_zone_west_from: int | Unset = UNSET,
    total_resource_mw_zone_west_to: int | Unset = UNSET,
    total_resource_mw_zone_houston_from: int | Unset = UNSET,
    total_resource_mw_zone_houston_to: int | Unset = UNSET,
    total_irrmw_zone_south_from: int | Unset = UNSET,
    total_irrmw_zone_south_to: int | Unset = UNSET,
    total_irrmw_zone_north_from: int | Unset = UNSET,
    total_irrmw_zone_north_to: int | Unset = UNSET,
    total_irrmw_zone_west_from: int | Unset = UNSET,
    total_irrmw_zone_west_to: int | Unset = UNSET,
    total_irrmw_zone_houston_from: int | Unset = UNSET,
    total_irrmw_zone_houston_to: int | Unset = UNSET,
    total_new_equip_resource_mw_zone_south_from: int | Unset = UNSET,
    total_new_equip_resource_mw_zone_south_to: int | Unset = UNSET,
    total_new_equip_resource_mw_zone_north_from: int | Unset = UNSET,
    total_new_equip_resource_mw_zone_north_to: int | Unset = UNSET,
    total_new_equip_resource_mw_zone_west_from: int | Unset = UNSET,
    total_new_equip_resource_mw_zone_west_to: int | Unset = UNSET,
    total_new_equip_resource_mw_zone_houston_from: int | Unset = UNSET,
    total_new_equip_resource_mw_zone_houston_to: int | Unset = UNSET,
    posted_datetime_from: str | Unset = UNSET,
    posted_datetime_to: str | Unset = UNSET,
    page: int | Unset = UNSET,
    size: int | Unset = UNSET,
    sort: str | Unset = UNSET,
    dir_: str | Unset = UNSET,
) -> Exception_ | Report | None:
    """Hourly Resource Outage Capacity

     Hourly Resource Outage Capacity

    Args:
        operating_date_from (str | Unset):
        operating_date_to (str | Unset):
        hour_ending_from (int | Unset):
        hour_ending_to (int | Unset):
        total_resource_mw_zone_south_from (int | Unset):
        total_resource_mw_zone_south_to (int | Unset):
        total_resource_mw_zone_north_from (int | Unset):
        total_resource_mw_zone_north_to (int | Unset):
        total_resource_mw_zone_west_from (int | Unset):
        total_resource_mw_zone_west_to (int | Unset):
        total_resource_mw_zone_houston_from (int | Unset):
        total_resource_mw_zone_houston_to (int | Unset):
        total_irrmw_zone_south_from (int | Unset):
        total_irrmw_zone_south_to (int | Unset):
        total_irrmw_zone_north_from (int | Unset):
        total_irrmw_zone_north_to (int | Unset):
        total_irrmw_zone_west_from (int | Unset):
        total_irrmw_zone_west_to (int | Unset):
        total_irrmw_zone_houston_from (int | Unset):
        total_irrmw_zone_houston_to (int | Unset):
        total_new_equip_resource_mw_zone_south_from (int | Unset):
        total_new_equip_resource_mw_zone_south_to (int | Unset):
        total_new_equip_resource_mw_zone_north_from (int | Unset):
        total_new_equip_resource_mw_zone_north_to (int | Unset):
        total_new_equip_resource_mw_zone_west_from (int | Unset):
        total_new_equip_resource_mw_zone_west_to (int | Unset):
        total_new_equip_resource_mw_zone_houston_from (int | Unset):
        total_new_equip_resource_mw_zone_houston_to (int | Unset):
        posted_datetime_from (str | Unset):
        posted_datetime_to (str | Unset):
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
            operating_date_from=operating_date_from,
            operating_date_to=operating_date_to,
            hour_ending_from=hour_ending_from,
            hour_ending_to=hour_ending_to,
            total_resource_mw_zone_south_from=total_resource_mw_zone_south_from,
            total_resource_mw_zone_south_to=total_resource_mw_zone_south_to,
            total_resource_mw_zone_north_from=total_resource_mw_zone_north_from,
            total_resource_mw_zone_north_to=total_resource_mw_zone_north_to,
            total_resource_mw_zone_west_from=total_resource_mw_zone_west_from,
            total_resource_mw_zone_west_to=total_resource_mw_zone_west_to,
            total_resource_mw_zone_houston_from=total_resource_mw_zone_houston_from,
            total_resource_mw_zone_houston_to=total_resource_mw_zone_houston_to,
            total_irrmw_zone_south_from=total_irrmw_zone_south_from,
            total_irrmw_zone_south_to=total_irrmw_zone_south_to,
            total_irrmw_zone_north_from=total_irrmw_zone_north_from,
            total_irrmw_zone_north_to=total_irrmw_zone_north_to,
            total_irrmw_zone_west_from=total_irrmw_zone_west_from,
            total_irrmw_zone_west_to=total_irrmw_zone_west_to,
            total_irrmw_zone_houston_from=total_irrmw_zone_houston_from,
            total_irrmw_zone_houston_to=total_irrmw_zone_houston_to,
            total_new_equip_resource_mw_zone_south_from=total_new_equip_resource_mw_zone_south_from,
            total_new_equip_resource_mw_zone_south_to=total_new_equip_resource_mw_zone_south_to,
            total_new_equip_resource_mw_zone_north_from=total_new_equip_resource_mw_zone_north_from,
            total_new_equip_resource_mw_zone_north_to=total_new_equip_resource_mw_zone_north_to,
            total_new_equip_resource_mw_zone_west_from=total_new_equip_resource_mw_zone_west_from,
            total_new_equip_resource_mw_zone_west_to=total_new_equip_resource_mw_zone_west_to,
            total_new_equip_resource_mw_zone_houston_from=total_new_equip_resource_mw_zone_houston_from,
            total_new_equip_resource_mw_zone_houston_to=total_new_equip_resource_mw_zone_houston_to,
            posted_datetime_from=posted_datetime_from,
            posted_datetime_to=posted_datetime_to,
            page=page,
            size=size,
            sort=sort,
            dir_=dir_,
        )
    ).parsed
