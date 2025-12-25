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
    wgrpp_load_zone_north_from: float | Unset = UNSET,
    wgrpp_load_zone_north_to: float | Unset = UNSET,
    dst_flag: bool | Unset = UNSET,
    posted_datetime_from: str | Unset = UNSET,
    posted_datetime_to: str | Unset = UNSET,
    delivery_date_from: str | Unset = UNSET,
    delivery_date_to: str | Unset = UNSET,
    hour_ending_from: int | Unset = UNSET,
    hour_ending_to: int | Unset = UNSET,
    actual_system_wide_from: float | Unset = UNSET,
    actual_system_wide_to: float | Unset = UNSET,
    cophsl_system_wide_from: float | Unset = UNSET,
    cophsl_system_wide_to: float | Unset = UNSET,
    stwpf_system_wide_from: float | Unset = UNSET,
    stwpf_system_wide_to: float | Unset = UNSET,
    wgrpp_system_wide_from: float | Unset = UNSET,
    wgrpp_system_wide_to: float | Unset = UNSET,
    actual_load_zone_south_houston_from: float | Unset = UNSET,
    actual_load_zone_south_houston_to: float | Unset = UNSET,
    cophsl_load_zone_south_houston_from: float | Unset = UNSET,
    cophsl_load_zone_south_houston_to: float | Unset = UNSET,
    stwpf_load_zone_south_houston_from: float | Unset = UNSET,
    stwpf_load_zone_south_houston_to: float | Unset = UNSET,
    wgrpp_load_zone_south_houston_from: float | Unset = UNSET,
    wgrpp_load_zone_south_houston_to: float | Unset = UNSET,
    actual_load_zone_west_from: float | Unset = UNSET,
    actual_load_zone_west_to: float | Unset = UNSET,
    cophsl_load_zone_west_from: float | Unset = UNSET,
    cophsl_load_zone_west_to: float | Unset = UNSET,
    stwpf_load_zone_west_from: float | Unset = UNSET,
    stwpf_load_zone_west_to: float | Unset = UNSET,
    wgrpp_load_zone_west_from: float | Unset = UNSET,
    wgrpp_load_zone_west_to: float | Unset = UNSET,
    actual_load_zone_north_from: float | Unset = UNSET,
    actual_load_zone_north_to: float | Unset = UNSET,
    cophsl_load_zone_north_from: float | Unset = UNSET,
    cophsl_load_zone_north_to: float | Unset = UNSET,
    stwpf_load_zone_north_from: float | Unset = UNSET,
    stwpf_load_zone_north_to: float | Unset = UNSET,
    page: int | Unset = UNSET,
    size: int | Unset = UNSET,
    sort: str | Unset = UNSET,
    dir_: str | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["WGRPPLoadZoneNorthFrom"] = wgrpp_load_zone_north_from

    params["WGRPPLoadZoneNorthTo"] = wgrpp_load_zone_north_to

    params["DSTFlag"] = dst_flag

    params["postedDatetimeFrom"] = posted_datetime_from

    params["postedDatetimeTo"] = posted_datetime_to

    params["deliveryDateFrom"] = delivery_date_from

    params["deliveryDateTo"] = delivery_date_to

    params["hourEndingFrom"] = hour_ending_from

    params["hourEndingTo"] = hour_ending_to

    params["actualSystemWideFrom"] = actual_system_wide_from

    params["actualSystemWideTo"] = actual_system_wide_to

    params["COPHSLSystemWideFrom"] = cophsl_system_wide_from

    params["COPHSLSystemWideTo"] = cophsl_system_wide_to

    params["STWPFSystemWideFrom"] = stwpf_system_wide_from

    params["STWPFSystemWideTo"] = stwpf_system_wide_to

    params["WGRPPSystemWideFrom"] = wgrpp_system_wide_from

    params["WGRPPSystemWideTo"] = wgrpp_system_wide_to

    params["actualLoadZoneSouthHoustonFrom"] = actual_load_zone_south_houston_from

    params["actualLoadZoneSouthHoustonTo"] = actual_load_zone_south_houston_to

    params["COPHSLLoadZoneSouthHoustonFrom"] = cophsl_load_zone_south_houston_from

    params["COPHSLLoadZoneSouthHoustonTo"] = cophsl_load_zone_south_houston_to

    params["STWPFLoadZoneSouthHoustonFrom"] = stwpf_load_zone_south_houston_from

    params["STWPFLoadZoneSouthHoustonTo"] = stwpf_load_zone_south_houston_to

    params["WGRPPLoadZoneSouthHoustonFrom"] = wgrpp_load_zone_south_houston_from

    params["WGRPPLoadZoneSouthHoustonTo"] = wgrpp_load_zone_south_houston_to

    params["actualLoadZoneWestFrom"] = actual_load_zone_west_from

    params["actualLoadZoneWestTo"] = actual_load_zone_west_to

    params["COPHSLLoadZoneWestFrom"] = cophsl_load_zone_west_from

    params["COPHSLLoadZoneWestTo"] = cophsl_load_zone_west_to

    params["STWPFLoadZoneWestFrom"] = stwpf_load_zone_west_from

    params["STWPFLoadZoneWestTo"] = stwpf_load_zone_west_to

    params["WGRPPLoadZoneWestFrom"] = wgrpp_load_zone_west_from

    params["WGRPPLoadZoneWestTo"] = wgrpp_load_zone_west_to

    params["actualLoadZoneNorthFrom"] = actual_load_zone_north_from

    params["actualLoadZoneNorthTo"] = actual_load_zone_north_to

    params["COPHSLLoadZoneNorthFrom"] = cophsl_load_zone_north_from

    params["COPHSLLoadZoneNorthTo"] = cophsl_load_zone_north_to

    params["STWPFLoadZoneNorthFrom"] = stwpf_load_zone_north_from

    params["STWPFLoadZoneNorthTo"] = stwpf_load_zone_north_to

    params["page"] = page

    params["size"] = size

    params["sort"] = sort

    params["dir"] = dir_

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/np4-732-cd/wpp_hrly_avrg_actl_fcast",
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
    wgrpp_load_zone_north_from: float | Unset = UNSET,
    wgrpp_load_zone_north_to: float | Unset = UNSET,
    dst_flag: bool | Unset = UNSET,
    posted_datetime_from: str | Unset = UNSET,
    posted_datetime_to: str | Unset = UNSET,
    delivery_date_from: str | Unset = UNSET,
    delivery_date_to: str | Unset = UNSET,
    hour_ending_from: int | Unset = UNSET,
    hour_ending_to: int | Unset = UNSET,
    actual_system_wide_from: float | Unset = UNSET,
    actual_system_wide_to: float | Unset = UNSET,
    cophsl_system_wide_from: float | Unset = UNSET,
    cophsl_system_wide_to: float | Unset = UNSET,
    stwpf_system_wide_from: float | Unset = UNSET,
    stwpf_system_wide_to: float | Unset = UNSET,
    wgrpp_system_wide_from: float | Unset = UNSET,
    wgrpp_system_wide_to: float | Unset = UNSET,
    actual_load_zone_south_houston_from: float | Unset = UNSET,
    actual_load_zone_south_houston_to: float | Unset = UNSET,
    cophsl_load_zone_south_houston_from: float | Unset = UNSET,
    cophsl_load_zone_south_houston_to: float | Unset = UNSET,
    stwpf_load_zone_south_houston_from: float | Unset = UNSET,
    stwpf_load_zone_south_houston_to: float | Unset = UNSET,
    wgrpp_load_zone_south_houston_from: float | Unset = UNSET,
    wgrpp_load_zone_south_houston_to: float | Unset = UNSET,
    actual_load_zone_west_from: float | Unset = UNSET,
    actual_load_zone_west_to: float | Unset = UNSET,
    cophsl_load_zone_west_from: float | Unset = UNSET,
    cophsl_load_zone_west_to: float | Unset = UNSET,
    stwpf_load_zone_west_from: float | Unset = UNSET,
    stwpf_load_zone_west_to: float | Unset = UNSET,
    wgrpp_load_zone_west_from: float | Unset = UNSET,
    wgrpp_load_zone_west_to: float | Unset = UNSET,
    actual_load_zone_north_from: float | Unset = UNSET,
    actual_load_zone_north_to: float | Unset = UNSET,
    cophsl_load_zone_north_from: float | Unset = UNSET,
    cophsl_load_zone_north_to: float | Unset = UNSET,
    stwpf_load_zone_north_from: float | Unset = UNSET,
    stwpf_load_zone_north_to: float | Unset = UNSET,
    page: int | Unset = UNSET,
    size: int | Unset = UNSET,
    sort: str | Unset = UNSET,
    dir_: str | Unset = UNSET,
) -> Response[Exception_ | Report]:
    """Wind Power Production - Hourly Averaged Actual and Forecasted Values

     Wind Power Production - Hourly Averaged Actual and Forecasted Values

    Args:
        wgrpp_load_zone_north_from (float | Unset):
        wgrpp_load_zone_north_to (float | Unset):
        dst_flag (bool | Unset):
        posted_datetime_from (str | Unset):
        posted_datetime_to (str | Unset):
        delivery_date_from (str | Unset):
        delivery_date_to (str | Unset):
        hour_ending_from (int | Unset):
        hour_ending_to (int | Unset):
        actual_system_wide_from (float | Unset):
        actual_system_wide_to (float | Unset):
        cophsl_system_wide_from (float | Unset):
        cophsl_system_wide_to (float | Unset):
        stwpf_system_wide_from (float | Unset):
        stwpf_system_wide_to (float | Unset):
        wgrpp_system_wide_from (float | Unset):
        wgrpp_system_wide_to (float | Unset):
        actual_load_zone_south_houston_from (float | Unset):
        actual_load_zone_south_houston_to (float | Unset):
        cophsl_load_zone_south_houston_from (float | Unset):
        cophsl_load_zone_south_houston_to (float | Unset):
        stwpf_load_zone_south_houston_from (float | Unset):
        stwpf_load_zone_south_houston_to (float | Unset):
        wgrpp_load_zone_south_houston_from (float | Unset):
        wgrpp_load_zone_south_houston_to (float | Unset):
        actual_load_zone_west_from (float | Unset):
        actual_load_zone_west_to (float | Unset):
        cophsl_load_zone_west_from (float | Unset):
        cophsl_load_zone_west_to (float | Unset):
        stwpf_load_zone_west_from (float | Unset):
        stwpf_load_zone_west_to (float | Unset):
        wgrpp_load_zone_west_from (float | Unset):
        wgrpp_load_zone_west_to (float | Unset):
        actual_load_zone_north_from (float | Unset):
        actual_load_zone_north_to (float | Unset):
        cophsl_load_zone_north_from (float | Unset):
        cophsl_load_zone_north_to (float | Unset):
        stwpf_load_zone_north_from (float | Unset):
        stwpf_load_zone_north_to (float | Unset):
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
        wgrpp_load_zone_north_from=wgrpp_load_zone_north_from,
        wgrpp_load_zone_north_to=wgrpp_load_zone_north_to,
        dst_flag=dst_flag,
        posted_datetime_from=posted_datetime_from,
        posted_datetime_to=posted_datetime_to,
        delivery_date_from=delivery_date_from,
        delivery_date_to=delivery_date_to,
        hour_ending_from=hour_ending_from,
        hour_ending_to=hour_ending_to,
        actual_system_wide_from=actual_system_wide_from,
        actual_system_wide_to=actual_system_wide_to,
        cophsl_system_wide_from=cophsl_system_wide_from,
        cophsl_system_wide_to=cophsl_system_wide_to,
        stwpf_system_wide_from=stwpf_system_wide_from,
        stwpf_system_wide_to=stwpf_system_wide_to,
        wgrpp_system_wide_from=wgrpp_system_wide_from,
        wgrpp_system_wide_to=wgrpp_system_wide_to,
        actual_load_zone_south_houston_from=actual_load_zone_south_houston_from,
        actual_load_zone_south_houston_to=actual_load_zone_south_houston_to,
        cophsl_load_zone_south_houston_from=cophsl_load_zone_south_houston_from,
        cophsl_load_zone_south_houston_to=cophsl_load_zone_south_houston_to,
        stwpf_load_zone_south_houston_from=stwpf_load_zone_south_houston_from,
        stwpf_load_zone_south_houston_to=stwpf_load_zone_south_houston_to,
        wgrpp_load_zone_south_houston_from=wgrpp_load_zone_south_houston_from,
        wgrpp_load_zone_south_houston_to=wgrpp_load_zone_south_houston_to,
        actual_load_zone_west_from=actual_load_zone_west_from,
        actual_load_zone_west_to=actual_load_zone_west_to,
        cophsl_load_zone_west_from=cophsl_load_zone_west_from,
        cophsl_load_zone_west_to=cophsl_load_zone_west_to,
        stwpf_load_zone_west_from=stwpf_load_zone_west_from,
        stwpf_load_zone_west_to=stwpf_load_zone_west_to,
        wgrpp_load_zone_west_from=wgrpp_load_zone_west_from,
        wgrpp_load_zone_west_to=wgrpp_load_zone_west_to,
        actual_load_zone_north_from=actual_load_zone_north_from,
        actual_load_zone_north_to=actual_load_zone_north_to,
        cophsl_load_zone_north_from=cophsl_load_zone_north_from,
        cophsl_load_zone_north_to=cophsl_load_zone_north_to,
        stwpf_load_zone_north_from=stwpf_load_zone_north_from,
        stwpf_load_zone_north_to=stwpf_load_zone_north_to,
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
    wgrpp_load_zone_north_from: float | Unset = UNSET,
    wgrpp_load_zone_north_to: float | Unset = UNSET,
    dst_flag: bool | Unset = UNSET,
    posted_datetime_from: str | Unset = UNSET,
    posted_datetime_to: str | Unset = UNSET,
    delivery_date_from: str | Unset = UNSET,
    delivery_date_to: str | Unset = UNSET,
    hour_ending_from: int | Unset = UNSET,
    hour_ending_to: int | Unset = UNSET,
    actual_system_wide_from: float | Unset = UNSET,
    actual_system_wide_to: float | Unset = UNSET,
    cophsl_system_wide_from: float | Unset = UNSET,
    cophsl_system_wide_to: float | Unset = UNSET,
    stwpf_system_wide_from: float | Unset = UNSET,
    stwpf_system_wide_to: float | Unset = UNSET,
    wgrpp_system_wide_from: float | Unset = UNSET,
    wgrpp_system_wide_to: float | Unset = UNSET,
    actual_load_zone_south_houston_from: float | Unset = UNSET,
    actual_load_zone_south_houston_to: float | Unset = UNSET,
    cophsl_load_zone_south_houston_from: float | Unset = UNSET,
    cophsl_load_zone_south_houston_to: float | Unset = UNSET,
    stwpf_load_zone_south_houston_from: float | Unset = UNSET,
    stwpf_load_zone_south_houston_to: float | Unset = UNSET,
    wgrpp_load_zone_south_houston_from: float | Unset = UNSET,
    wgrpp_load_zone_south_houston_to: float | Unset = UNSET,
    actual_load_zone_west_from: float | Unset = UNSET,
    actual_load_zone_west_to: float | Unset = UNSET,
    cophsl_load_zone_west_from: float | Unset = UNSET,
    cophsl_load_zone_west_to: float | Unset = UNSET,
    stwpf_load_zone_west_from: float | Unset = UNSET,
    stwpf_load_zone_west_to: float | Unset = UNSET,
    wgrpp_load_zone_west_from: float | Unset = UNSET,
    wgrpp_load_zone_west_to: float | Unset = UNSET,
    actual_load_zone_north_from: float | Unset = UNSET,
    actual_load_zone_north_to: float | Unset = UNSET,
    cophsl_load_zone_north_from: float | Unset = UNSET,
    cophsl_load_zone_north_to: float | Unset = UNSET,
    stwpf_load_zone_north_from: float | Unset = UNSET,
    stwpf_load_zone_north_to: float | Unset = UNSET,
    page: int | Unset = UNSET,
    size: int | Unset = UNSET,
    sort: str | Unset = UNSET,
    dir_: str | Unset = UNSET,
) -> Exception_ | Report | None:
    """Wind Power Production - Hourly Averaged Actual and Forecasted Values

     Wind Power Production - Hourly Averaged Actual and Forecasted Values

    Args:
        wgrpp_load_zone_north_from (float | Unset):
        wgrpp_load_zone_north_to (float | Unset):
        dst_flag (bool | Unset):
        posted_datetime_from (str | Unset):
        posted_datetime_to (str | Unset):
        delivery_date_from (str | Unset):
        delivery_date_to (str | Unset):
        hour_ending_from (int | Unset):
        hour_ending_to (int | Unset):
        actual_system_wide_from (float | Unset):
        actual_system_wide_to (float | Unset):
        cophsl_system_wide_from (float | Unset):
        cophsl_system_wide_to (float | Unset):
        stwpf_system_wide_from (float | Unset):
        stwpf_system_wide_to (float | Unset):
        wgrpp_system_wide_from (float | Unset):
        wgrpp_system_wide_to (float | Unset):
        actual_load_zone_south_houston_from (float | Unset):
        actual_load_zone_south_houston_to (float | Unset):
        cophsl_load_zone_south_houston_from (float | Unset):
        cophsl_load_zone_south_houston_to (float | Unset):
        stwpf_load_zone_south_houston_from (float | Unset):
        stwpf_load_zone_south_houston_to (float | Unset):
        wgrpp_load_zone_south_houston_from (float | Unset):
        wgrpp_load_zone_south_houston_to (float | Unset):
        actual_load_zone_west_from (float | Unset):
        actual_load_zone_west_to (float | Unset):
        cophsl_load_zone_west_from (float | Unset):
        cophsl_load_zone_west_to (float | Unset):
        stwpf_load_zone_west_from (float | Unset):
        stwpf_load_zone_west_to (float | Unset):
        wgrpp_load_zone_west_from (float | Unset):
        wgrpp_load_zone_west_to (float | Unset):
        actual_load_zone_north_from (float | Unset):
        actual_load_zone_north_to (float | Unset):
        cophsl_load_zone_north_from (float | Unset):
        cophsl_load_zone_north_to (float | Unset):
        stwpf_load_zone_north_from (float | Unset):
        stwpf_load_zone_north_to (float | Unset):
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
        wgrpp_load_zone_north_from=wgrpp_load_zone_north_from,
        wgrpp_load_zone_north_to=wgrpp_load_zone_north_to,
        dst_flag=dst_flag,
        posted_datetime_from=posted_datetime_from,
        posted_datetime_to=posted_datetime_to,
        delivery_date_from=delivery_date_from,
        delivery_date_to=delivery_date_to,
        hour_ending_from=hour_ending_from,
        hour_ending_to=hour_ending_to,
        actual_system_wide_from=actual_system_wide_from,
        actual_system_wide_to=actual_system_wide_to,
        cophsl_system_wide_from=cophsl_system_wide_from,
        cophsl_system_wide_to=cophsl_system_wide_to,
        stwpf_system_wide_from=stwpf_system_wide_from,
        stwpf_system_wide_to=stwpf_system_wide_to,
        wgrpp_system_wide_from=wgrpp_system_wide_from,
        wgrpp_system_wide_to=wgrpp_system_wide_to,
        actual_load_zone_south_houston_from=actual_load_zone_south_houston_from,
        actual_load_zone_south_houston_to=actual_load_zone_south_houston_to,
        cophsl_load_zone_south_houston_from=cophsl_load_zone_south_houston_from,
        cophsl_load_zone_south_houston_to=cophsl_load_zone_south_houston_to,
        stwpf_load_zone_south_houston_from=stwpf_load_zone_south_houston_from,
        stwpf_load_zone_south_houston_to=stwpf_load_zone_south_houston_to,
        wgrpp_load_zone_south_houston_from=wgrpp_load_zone_south_houston_from,
        wgrpp_load_zone_south_houston_to=wgrpp_load_zone_south_houston_to,
        actual_load_zone_west_from=actual_load_zone_west_from,
        actual_load_zone_west_to=actual_load_zone_west_to,
        cophsl_load_zone_west_from=cophsl_load_zone_west_from,
        cophsl_load_zone_west_to=cophsl_load_zone_west_to,
        stwpf_load_zone_west_from=stwpf_load_zone_west_from,
        stwpf_load_zone_west_to=stwpf_load_zone_west_to,
        wgrpp_load_zone_west_from=wgrpp_load_zone_west_from,
        wgrpp_load_zone_west_to=wgrpp_load_zone_west_to,
        actual_load_zone_north_from=actual_load_zone_north_from,
        actual_load_zone_north_to=actual_load_zone_north_to,
        cophsl_load_zone_north_from=cophsl_load_zone_north_from,
        cophsl_load_zone_north_to=cophsl_load_zone_north_to,
        stwpf_load_zone_north_from=stwpf_load_zone_north_from,
        stwpf_load_zone_north_to=stwpf_load_zone_north_to,
        page=page,
        size=size,
        sort=sort,
        dir_=dir_,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    wgrpp_load_zone_north_from: float | Unset = UNSET,
    wgrpp_load_zone_north_to: float | Unset = UNSET,
    dst_flag: bool | Unset = UNSET,
    posted_datetime_from: str | Unset = UNSET,
    posted_datetime_to: str | Unset = UNSET,
    delivery_date_from: str | Unset = UNSET,
    delivery_date_to: str | Unset = UNSET,
    hour_ending_from: int | Unset = UNSET,
    hour_ending_to: int | Unset = UNSET,
    actual_system_wide_from: float | Unset = UNSET,
    actual_system_wide_to: float | Unset = UNSET,
    cophsl_system_wide_from: float | Unset = UNSET,
    cophsl_system_wide_to: float | Unset = UNSET,
    stwpf_system_wide_from: float | Unset = UNSET,
    stwpf_system_wide_to: float | Unset = UNSET,
    wgrpp_system_wide_from: float | Unset = UNSET,
    wgrpp_system_wide_to: float | Unset = UNSET,
    actual_load_zone_south_houston_from: float | Unset = UNSET,
    actual_load_zone_south_houston_to: float | Unset = UNSET,
    cophsl_load_zone_south_houston_from: float | Unset = UNSET,
    cophsl_load_zone_south_houston_to: float | Unset = UNSET,
    stwpf_load_zone_south_houston_from: float | Unset = UNSET,
    stwpf_load_zone_south_houston_to: float | Unset = UNSET,
    wgrpp_load_zone_south_houston_from: float | Unset = UNSET,
    wgrpp_load_zone_south_houston_to: float | Unset = UNSET,
    actual_load_zone_west_from: float | Unset = UNSET,
    actual_load_zone_west_to: float | Unset = UNSET,
    cophsl_load_zone_west_from: float | Unset = UNSET,
    cophsl_load_zone_west_to: float | Unset = UNSET,
    stwpf_load_zone_west_from: float | Unset = UNSET,
    stwpf_load_zone_west_to: float | Unset = UNSET,
    wgrpp_load_zone_west_from: float | Unset = UNSET,
    wgrpp_load_zone_west_to: float | Unset = UNSET,
    actual_load_zone_north_from: float | Unset = UNSET,
    actual_load_zone_north_to: float | Unset = UNSET,
    cophsl_load_zone_north_from: float | Unset = UNSET,
    cophsl_load_zone_north_to: float | Unset = UNSET,
    stwpf_load_zone_north_from: float | Unset = UNSET,
    stwpf_load_zone_north_to: float | Unset = UNSET,
    page: int | Unset = UNSET,
    size: int | Unset = UNSET,
    sort: str | Unset = UNSET,
    dir_: str | Unset = UNSET,
) -> Response[Exception_ | Report]:
    """Wind Power Production - Hourly Averaged Actual and Forecasted Values

     Wind Power Production - Hourly Averaged Actual and Forecasted Values

    Args:
        wgrpp_load_zone_north_from (float | Unset):
        wgrpp_load_zone_north_to (float | Unset):
        dst_flag (bool | Unset):
        posted_datetime_from (str | Unset):
        posted_datetime_to (str | Unset):
        delivery_date_from (str | Unset):
        delivery_date_to (str | Unset):
        hour_ending_from (int | Unset):
        hour_ending_to (int | Unset):
        actual_system_wide_from (float | Unset):
        actual_system_wide_to (float | Unset):
        cophsl_system_wide_from (float | Unset):
        cophsl_system_wide_to (float | Unset):
        stwpf_system_wide_from (float | Unset):
        stwpf_system_wide_to (float | Unset):
        wgrpp_system_wide_from (float | Unset):
        wgrpp_system_wide_to (float | Unset):
        actual_load_zone_south_houston_from (float | Unset):
        actual_load_zone_south_houston_to (float | Unset):
        cophsl_load_zone_south_houston_from (float | Unset):
        cophsl_load_zone_south_houston_to (float | Unset):
        stwpf_load_zone_south_houston_from (float | Unset):
        stwpf_load_zone_south_houston_to (float | Unset):
        wgrpp_load_zone_south_houston_from (float | Unset):
        wgrpp_load_zone_south_houston_to (float | Unset):
        actual_load_zone_west_from (float | Unset):
        actual_load_zone_west_to (float | Unset):
        cophsl_load_zone_west_from (float | Unset):
        cophsl_load_zone_west_to (float | Unset):
        stwpf_load_zone_west_from (float | Unset):
        stwpf_load_zone_west_to (float | Unset):
        wgrpp_load_zone_west_from (float | Unset):
        wgrpp_load_zone_west_to (float | Unset):
        actual_load_zone_north_from (float | Unset):
        actual_load_zone_north_to (float | Unset):
        cophsl_load_zone_north_from (float | Unset):
        cophsl_load_zone_north_to (float | Unset):
        stwpf_load_zone_north_from (float | Unset):
        stwpf_load_zone_north_to (float | Unset):
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
        wgrpp_load_zone_north_from=wgrpp_load_zone_north_from,
        wgrpp_load_zone_north_to=wgrpp_load_zone_north_to,
        dst_flag=dst_flag,
        posted_datetime_from=posted_datetime_from,
        posted_datetime_to=posted_datetime_to,
        delivery_date_from=delivery_date_from,
        delivery_date_to=delivery_date_to,
        hour_ending_from=hour_ending_from,
        hour_ending_to=hour_ending_to,
        actual_system_wide_from=actual_system_wide_from,
        actual_system_wide_to=actual_system_wide_to,
        cophsl_system_wide_from=cophsl_system_wide_from,
        cophsl_system_wide_to=cophsl_system_wide_to,
        stwpf_system_wide_from=stwpf_system_wide_from,
        stwpf_system_wide_to=stwpf_system_wide_to,
        wgrpp_system_wide_from=wgrpp_system_wide_from,
        wgrpp_system_wide_to=wgrpp_system_wide_to,
        actual_load_zone_south_houston_from=actual_load_zone_south_houston_from,
        actual_load_zone_south_houston_to=actual_load_zone_south_houston_to,
        cophsl_load_zone_south_houston_from=cophsl_load_zone_south_houston_from,
        cophsl_load_zone_south_houston_to=cophsl_load_zone_south_houston_to,
        stwpf_load_zone_south_houston_from=stwpf_load_zone_south_houston_from,
        stwpf_load_zone_south_houston_to=stwpf_load_zone_south_houston_to,
        wgrpp_load_zone_south_houston_from=wgrpp_load_zone_south_houston_from,
        wgrpp_load_zone_south_houston_to=wgrpp_load_zone_south_houston_to,
        actual_load_zone_west_from=actual_load_zone_west_from,
        actual_load_zone_west_to=actual_load_zone_west_to,
        cophsl_load_zone_west_from=cophsl_load_zone_west_from,
        cophsl_load_zone_west_to=cophsl_load_zone_west_to,
        stwpf_load_zone_west_from=stwpf_load_zone_west_from,
        stwpf_load_zone_west_to=stwpf_load_zone_west_to,
        wgrpp_load_zone_west_from=wgrpp_load_zone_west_from,
        wgrpp_load_zone_west_to=wgrpp_load_zone_west_to,
        actual_load_zone_north_from=actual_load_zone_north_from,
        actual_load_zone_north_to=actual_load_zone_north_to,
        cophsl_load_zone_north_from=cophsl_load_zone_north_from,
        cophsl_load_zone_north_to=cophsl_load_zone_north_to,
        stwpf_load_zone_north_from=stwpf_load_zone_north_from,
        stwpf_load_zone_north_to=stwpf_load_zone_north_to,
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
    wgrpp_load_zone_north_from: float | Unset = UNSET,
    wgrpp_load_zone_north_to: float | Unset = UNSET,
    dst_flag: bool | Unset = UNSET,
    posted_datetime_from: str | Unset = UNSET,
    posted_datetime_to: str | Unset = UNSET,
    delivery_date_from: str | Unset = UNSET,
    delivery_date_to: str | Unset = UNSET,
    hour_ending_from: int | Unset = UNSET,
    hour_ending_to: int | Unset = UNSET,
    actual_system_wide_from: float | Unset = UNSET,
    actual_system_wide_to: float | Unset = UNSET,
    cophsl_system_wide_from: float | Unset = UNSET,
    cophsl_system_wide_to: float | Unset = UNSET,
    stwpf_system_wide_from: float | Unset = UNSET,
    stwpf_system_wide_to: float | Unset = UNSET,
    wgrpp_system_wide_from: float | Unset = UNSET,
    wgrpp_system_wide_to: float | Unset = UNSET,
    actual_load_zone_south_houston_from: float | Unset = UNSET,
    actual_load_zone_south_houston_to: float | Unset = UNSET,
    cophsl_load_zone_south_houston_from: float | Unset = UNSET,
    cophsl_load_zone_south_houston_to: float | Unset = UNSET,
    stwpf_load_zone_south_houston_from: float | Unset = UNSET,
    stwpf_load_zone_south_houston_to: float | Unset = UNSET,
    wgrpp_load_zone_south_houston_from: float | Unset = UNSET,
    wgrpp_load_zone_south_houston_to: float | Unset = UNSET,
    actual_load_zone_west_from: float | Unset = UNSET,
    actual_load_zone_west_to: float | Unset = UNSET,
    cophsl_load_zone_west_from: float | Unset = UNSET,
    cophsl_load_zone_west_to: float | Unset = UNSET,
    stwpf_load_zone_west_from: float | Unset = UNSET,
    stwpf_load_zone_west_to: float | Unset = UNSET,
    wgrpp_load_zone_west_from: float | Unset = UNSET,
    wgrpp_load_zone_west_to: float | Unset = UNSET,
    actual_load_zone_north_from: float | Unset = UNSET,
    actual_load_zone_north_to: float | Unset = UNSET,
    cophsl_load_zone_north_from: float | Unset = UNSET,
    cophsl_load_zone_north_to: float | Unset = UNSET,
    stwpf_load_zone_north_from: float | Unset = UNSET,
    stwpf_load_zone_north_to: float | Unset = UNSET,
    page: int | Unset = UNSET,
    size: int | Unset = UNSET,
    sort: str | Unset = UNSET,
    dir_: str | Unset = UNSET,
) -> Exception_ | Report | None:
    """Wind Power Production - Hourly Averaged Actual and Forecasted Values

     Wind Power Production - Hourly Averaged Actual and Forecasted Values

    Args:
        wgrpp_load_zone_north_from (float | Unset):
        wgrpp_load_zone_north_to (float | Unset):
        dst_flag (bool | Unset):
        posted_datetime_from (str | Unset):
        posted_datetime_to (str | Unset):
        delivery_date_from (str | Unset):
        delivery_date_to (str | Unset):
        hour_ending_from (int | Unset):
        hour_ending_to (int | Unset):
        actual_system_wide_from (float | Unset):
        actual_system_wide_to (float | Unset):
        cophsl_system_wide_from (float | Unset):
        cophsl_system_wide_to (float | Unset):
        stwpf_system_wide_from (float | Unset):
        stwpf_system_wide_to (float | Unset):
        wgrpp_system_wide_from (float | Unset):
        wgrpp_system_wide_to (float | Unset):
        actual_load_zone_south_houston_from (float | Unset):
        actual_load_zone_south_houston_to (float | Unset):
        cophsl_load_zone_south_houston_from (float | Unset):
        cophsl_load_zone_south_houston_to (float | Unset):
        stwpf_load_zone_south_houston_from (float | Unset):
        stwpf_load_zone_south_houston_to (float | Unset):
        wgrpp_load_zone_south_houston_from (float | Unset):
        wgrpp_load_zone_south_houston_to (float | Unset):
        actual_load_zone_west_from (float | Unset):
        actual_load_zone_west_to (float | Unset):
        cophsl_load_zone_west_from (float | Unset):
        cophsl_load_zone_west_to (float | Unset):
        stwpf_load_zone_west_from (float | Unset):
        stwpf_load_zone_west_to (float | Unset):
        wgrpp_load_zone_west_from (float | Unset):
        wgrpp_load_zone_west_to (float | Unset):
        actual_load_zone_north_from (float | Unset):
        actual_load_zone_north_to (float | Unset):
        cophsl_load_zone_north_from (float | Unset):
        cophsl_load_zone_north_to (float | Unset):
        stwpf_load_zone_north_from (float | Unset):
        stwpf_load_zone_north_to (float | Unset):
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
            wgrpp_load_zone_north_from=wgrpp_load_zone_north_from,
            wgrpp_load_zone_north_to=wgrpp_load_zone_north_to,
            dst_flag=dst_flag,
            posted_datetime_from=posted_datetime_from,
            posted_datetime_to=posted_datetime_to,
            delivery_date_from=delivery_date_from,
            delivery_date_to=delivery_date_to,
            hour_ending_from=hour_ending_from,
            hour_ending_to=hour_ending_to,
            actual_system_wide_from=actual_system_wide_from,
            actual_system_wide_to=actual_system_wide_to,
            cophsl_system_wide_from=cophsl_system_wide_from,
            cophsl_system_wide_to=cophsl_system_wide_to,
            stwpf_system_wide_from=stwpf_system_wide_from,
            stwpf_system_wide_to=stwpf_system_wide_to,
            wgrpp_system_wide_from=wgrpp_system_wide_from,
            wgrpp_system_wide_to=wgrpp_system_wide_to,
            actual_load_zone_south_houston_from=actual_load_zone_south_houston_from,
            actual_load_zone_south_houston_to=actual_load_zone_south_houston_to,
            cophsl_load_zone_south_houston_from=cophsl_load_zone_south_houston_from,
            cophsl_load_zone_south_houston_to=cophsl_load_zone_south_houston_to,
            stwpf_load_zone_south_houston_from=stwpf_load_zone_south_houston_from,
            stwpf_load_zone_south_houston_to=stwpf_load_zone_south_houston_to,
            wgrpp_load_zone_south_houston_from=wgrpp_load_zone_south_houston_from,
            wgrpp_load_zone_south_houston_to=wgrpp_load_zone_south_houston_to,
            actual_load_zone_west_from=actual_load_zone_west_from,
            actual_load_zone_west_to=actual_load_zone_west_to,
            cophsl_load_zone_west_from=cophsl_load_zone_west_from,
            cophsl_load_zone_west_to=cophsl_load_zone_west_to,
            stwpf_load_zone_west_from=stwpf_load_zone_west_from,
            stwpf_load_zone_west_to=stwpf_load_zone_west_to,
            wgrpp_load_zone_west_from=wgrpp_load_zone_west_from,
            wgrpp_load_zone_west_to=wgrpp_load_zone_west_to,
            actual_load_zone_north_from=actual_load_zone_north_from,
            actual_load_zone_north_to=actual_load_zone_north_to,
            cophsl_load_zone_north_from=cophsl_load_zone_north_from,
            cophsl_load_zone_north_to=cophsl_load_zone_north_to,
            stwpf_load_zone_north_from=stwpf_load_zone_north_from,
            stwpf_load_zone_north_to=stwpf_load_zone_north_to,
            page=page,
            size=size,
            sort=sort,
            dir_=dir_,
        )
    ).parsed
