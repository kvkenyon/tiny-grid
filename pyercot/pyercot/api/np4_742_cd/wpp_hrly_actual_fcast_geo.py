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
    actual_panhandle_from: float | Unset = UNSET,
    actual_panhandle_to: float | Unset = UNSET,
    cophsl_panhandle_from: float | Unset = UNSET,
    cophsl_panhandle_to: float | Unset = UNSET,
    stwpf_panhandle_from: float | Unset = UNSET,
    stwpf_panhandle_to: float | Unset = UNSET,
    wgrpp_panhandle_from: float | Unset = UNSET,
    wgrpp_panhandle_to: float | Unset = UNSET,
    actual_coastal_from: float | Unset = UNSET,
    actual_coastal_to: float | Unset = UNSET,
    cophsl_coastal_from: float | Unset = UNSET,
    cophsl_coastal_to: float | Unset = UNSET,
    stwpf_coastal_from: float | Unset = UNSET,
    stwpf_coastal_to: float | Unset = UNSET,
    wgrpp_coastal_from: float | Unset = UNSET,
    wgrpp_coastal_to: float | Unset = UNSET,
    actual_south_from: float | Unset = UNSET,
    actual_south_to: float | Unset = UNSET,
    cophsl_south_from: float | Unset = UNSET,
    cophsl_south_to: float | Unset = UNSET,
    stwpf_south_from: float | Unset = UNSET,
    stwpf_south_to: float | Unset = UNSET,
    wgrpp_south_from: float | Unset = UNSET,
    wgrpp_south_to: float | Unset = UNSET,
    actual_west_from: float | Unset = UNSET,
    actual_west_to: float | Unset = UNSET,
    cophsl_west_from: float | Unset = UNSET,
    cophsl_west_to: float | Unset = UNSET,
    stwpf_west_from: float | Unset = UNSET,
    stwpf_west_to: float | Unset = UNSET,
    wgrpp_west_from: float | Unset = UNSET,
    wgrpp_west_to: float | Unset = UNSET,
    actual_north_from: float | Unset = UNSET,
    actual_north_to: float | Unset = UNSET,
    cophsl_north_from: float | Unset = UNSET,
    cophsl_north_to: float | Unset = UNSET,
    stwpf_north_from: float | Unset = UNSET,
    stwpf_north_to: float | Unset = UNSET,
    wgrpp_north_from: float | Unset = UNSET,
    wgrpp_north_to: float | Unset = UNSET,
    dst_flag: bool | Unset = UNSET,
    posted_datetime_from: str | Unset = UNSET,
    posted_datetime_to: str | Unset = UNSET,
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

    params["actualSystemWideFrom"] = actual_system_wide_from

    params["actualSystemWideTo"] = actual_system_wide_to

    params["COPHSLSystemWideFrom"] = cophsl_system_wide_from

    params["COPHSLSystemWideTo"] = cophsl_system_wide_to

    params["STWPFSystemWideFrom"] = stwpf_system_wide_from

    params["STWPFSystemWideTo"] = stwpf_system_wide_to

    params["WGRPPSystemWideFrom"] = wgrpp_system_wide_from

    params["WGRPPSystemWideTo"] = wgrpp_system_wide_to

    params["actualPanhandleFrom"] = actual_panhandle_from

    params["actualPanhandleTo"] = actual_panhandle_to

    params["COPHSLPanhandleFrom"] = cophsl_panhandle_from

    params["COPHSLPanhandleTo"] = cophsl_panhandle_to

    params["STWPFPanhandleFrom"] = stwpf_panhandle_from

    params["STWPFPanhandleTo"] = stwpf_panhandle_to

    params["WGRPPPanhandleFrom"] = wgrpp_panhandle_from

    params["WGRPPPanhandleTo"] = wgrpp_panhandle_to

    params["actualCoastalFrom"] = actual_coastal_from

    params["actualCoastalTo"] = actual_coastal_to

    params["COPHSLCoastalFrom"] = cophsl_coastal_from

    params["COPHSLCoastalTo"] = cophsl_coastal_to

    params["STWPFCoastalFrom"] = stwpf_coastal_from

    params["STWPFCoastalTo"] = stwpf_coastal_to

    params["WGRPPCoastalFrom"] = wgrpp_coastal_from

    params["WGRPPCoastalTo"] = wgrpp_coastal_to

    params["actualSouthFrom"] = actual_south_from

    params["actualSouthTo"] = actual_south_to

    params["COPHSLSouthFrom"] = cophsl_south_from

    params["COPHSLSouthTo"] = cophsl_south_to

    params["STWPFSouthFrom"] = stwpf_south_from

    params["STWPFSouthTo"] = stwpf_south_to

    params["WGRPPSouthFrom"] = wgrpp_south_from

    params["WGRPPSouthTo"] = wgrpp_south_to

    params["actualWestFrom"] = actual_west_from

    params["actualWestTo"] = actual_west_to

    params["COPHSLWestFrom"] = cophsl_west_from

    params["COPHSLWestTo"] = cophsl_west_to

    params["STWPFWestFrom"] = stwpf_west_from

    params["STWPFWestTo"] = stwpf_west_to

    params["WGRPPWestFrom"] = wgrpp_west_from

    params["WGRPPWestTo"] = wgrpp_west_to

    params["actualNorthFrom"] = actual_north_from

    params["actualNorthTo"] = actual_north_to

    params["COPHSLNorthFrom"] = cophsl_north_from

    params["COPHSLNorthTo"] = cophsl_north_to

    params["STWPFNorthFrom"] = stwpf_north_from

    params["STWPFNorthTo"] = stwpf_north_to

    params["WGRPPNorthFrom"] = wgrpp_north_from

    params["WGRPPNorthTo"] = wgrpp_north_to

    params["DSTFlag"] = dst_flag

    params["postedDatetimeFrom"] = posted_datetime_from

    params["postedDatetimeTo"] = posted_datetime_to

    params["page"] = page

    params["size"] = size

    params["sort"] = sort

    params["dir"] = dir_

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/np4-742-cd/wpp_hrly_actual_fcast_geo",
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
    actual_panhandle_from: float | Unset = UNSET,
    actual_panhandle_to: float | Unset = UNSET,
    cophsl_panhandle_from: float | Unset = UNSET,
    cophsl_panhandle_to: float | Unset = UNSET,
    stwpf_panhandle_from: float | Unset = UNSET,
    stwpf_panhandle_to: float | Unset = UNSET,
    wgrpp_panhandle_from: float | Unset = UNSET,
    wgrpp_panhandle_to: float | Unset = UNSET,
    actual_coastal_from: float | Unset = UNSET,
    actual_coastal_to: float | Unset = UNSET,
    cophsl_coastal_from: float | Unset = UNSET,
    cophsl_coastal_to: float | Unset = UNSET,
    stwpf_coastal_from: float | Unset = UNSET,
    stwpf_coastal_to: float | Unset = UNSET,
    wgrpp_coastal_from: float | Unset = UNSET,
    wgrpp_coastal_to: float | Unset = UNSET,
    actual_south_from: float | Unset = UNSET,
    actual_south_to: float | Unset = UNSET,
    cophsl_south_from: float | Unset = UNSET,
    cophsl_south_to: float | Unset = UNSET,
    stwpf_south_from: float | Unset = UNSET,
    stwpf_south_to: float | Unset = UNSET,
    wgrpp_south_from: float | Unset = UNSET,
    wgrpp_south_to: float | Unset = UNSET,
    actual_west_from: float | Unset = UNSET,
    actual_west_to: float | Unset = UNSET,
    cophsl_west_from: float | Unset = UNSET,
    cophsl_west_to: float | Unset = UNSET,
    stwpf_west_from: float | Unset = UNSET,
    stwpf_west_to: float | Unset = UNSET,
    wgrpp_west_from: float | Unset = UNSET,
    wgrpp_west_to: float | Unset = UNSET,
    actual_north_from: float | Unset = UNSET,
    actual_north_to: float | Unset = UNSET,
    cophsl_north_from: float | Unset = UNSET,
    cophsl_north_to: float | Unset = UNSET,
    stwpf_north_from: float | Unset = UNSET,
    stwpf_north_to: float | Unset = UNSET,
    wgrpp_north_from: float | Unset = UNSET,
    wgrpp_north_to: float | Unset = UNSET,
    dst_flag: bool | Unset = UNSET,
    posted_datetime_from: str | Unset = UNSET,
    posted_datetime_to: str | Unset = UNSET,
    page: int | Unset = UNSET,
    size: int | Unset = UNSET,
    sort: str | Unset = UNSET,
    dir_: str | Unset = UNSET,
) -> Response[Exception_ | Report]:
    """Wind Power Production - Hourly Averaged Actual and Forecasted Values by Geographical Region

     Wind Power Production - Hourly Averaged Actual and Forecasted Values by Geographical Region

    Args:
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
        actual_panhandle_from (float | Unset):
        actual_panhandle_to (float | Unset):
        cophsl_panhandle_from (float | Unset):
        cophsl_panhandle_to (float | Unset):
        stwpf_panhandle_from (float | Unset):
        stwpf_panhandle_to (float | Unset):
        wgrpp_panhandle_from (float | Unset):
        wgrpp_panhandle_to (float | Unset):
        actual_coastal_from (float | Unset):
        actual_coastal_to (float | Unset):
        cophsl_coastal_from (float | Unset):
        cophsl_coastal_to (float | Unset):
        stwpf_coastal_from (float | Unset):
        stwpf_coastal_to (float | Unset):
        wgrpp_coastal_from (float | Unset):
        wgrpp_coastal_to (float | Unset):
        actual_south_from (float | Unset):
        actual_south_to (float | Unset):
        cophsl_south_from (float | Unset):
        cophsl_south_to (float | Unset):
        stwpf_south_from (float | Unset):
        stwpf_south_to (float | Unset):
        wgrpp_south_from (float | Unset):
        wgrpp_south_to (float | Unset):
        actual_west_from (float | Unset):
        actual_west_to (float | Unset):
        cophsl_west_from (float | Unset):
        cophsl_west_to (float | Unset):
        stwpf_west_from (float | Unset):
        stwpf_west_to (float | Unset):
        wgrpp_west_from (float | Unset):
        wgrpp_west_to (float | Unset):
        actual_north_from (float | Unset):
        actual_north_to (float | Unset):
        cophsl_north_from (float | Unset):
        cophsl_north_to (float | Unset):
        stwpf_north_from (float | Unset):
        stwpf_north_to (float | Unset):
        wgrpp_north_from (float | Unset):
        wgrpp_north_to (float | Unset):
        dst_flag (bool | Unset):
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
        actual_panhandle_from=actual_panhandle_from,
        actual_panhandle_to=actual_panhandle_to,
        cophsl_panhandle_from=cophsl_panhandle_from,
        cophsl_panhandle_to=cophsl_panhandle_to,
        stwpf_panhandle_from=stwpf_panhandle_from,
        stwpf_panhandle_to=stwpf_panhandle_to,
        wgrpp_panhandle_from=wgrpp_panhandle_from,
        wgrpp_panhandle_to=wgrpp_panhandle_to,
        actual_coastal_from=actual_coastal_from,
        actual_coastal_to=actual_coastal_to,
        cophsl_coastal_from=cophsl_coastal_from,
        cophsl_coastal_to=cophsl_coastal_to,
        stwpf_coastal_from=stwpf_coastal_from,
        stwpf_coastal_to=stwpf_coastal_to,
        wgrpp_coastal_from=wgrpp_coastal_from,
        wgrpp_coastal_to=wgrpp_coastal_to,
        actual_south_from=actual_south_from,
        actual_south_to=actual_south_to,
        cophsl_south_from=cophsl_south_from,
        cophsl_south_to=cophsl_south_to,
        stwpf_south_from=stwpf_south_from,
        stwpf_south_to=stwpf_south_to,
        wgrpp_south_from=wgrpp_south_from,
        wgrpp_south_to=wgrpp_south_to,
        actual_west_from=actual_west_from,
        actual_west_to=actual_west_to,
        cophsl_west_from=cophsl_west_from,
        cophsl_west_to=cophsl_west_to,
        stwpf_west_from=stwpf_west_from,
        stwpf_west_to=stwpf_west_to,
        wgrpp_west_from=wgrpp_west_from,
        wgrpp_west_to=wgrpp_west_to,
        actual_north_from=actual_north_from,
        actual_north_to=actual_north_to,
        cophsl_north_from=cophsl_north_from,
        cophsl_north_to=cophsl_north_to,
        stwpf_north_from=stwpf_north_from,
        stwpf_north_to=stwpf_north_to,
        wgrpp_north_from=wgrpp_north_from,
        wgrpp_north_to=wgrpp_north_to,
        dst_flag=dst_flag,
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
    actual_panhandle_from: float | Unset = UNSET,
    actual_panhandle_to: float | Unset = UNSET,
    cophsl_panhandle_from: float | Unset = UNSET,
    cophsl_panhandle_to: float | Unset = UNSET,
    stwpf_panhandle_from: float | Unset = UNSET,
    stwpf_panhandle_to: float | Unset = UNSET,
    wgrpp_panhandle_from: float | Unset = UNSET,
    wgrpp_panhandle_to: float | Unset = UNSET,
    actual_coastal_from: float | Unset = UNSET,
    actual_coastal_to: float | Unset = UNSET,
    cophsl_coastal_from: float | Unset = UNSET,
    cophsl_coastal_to: float | Unset = UNSET,
    stwpf_coastal_from: float | Unset = UNSET,
    stwpf_coastal_to: float | Unset = UNSET,
    wgrpp_coastal_from: float | Unset = UNSET,
    wgrpp_coastal_to: float | Unset = UNSET,
    actual_south_from: float | Unset = UNSET,
    actual_south_to: float | Unset = UNSET,
    cophsl_south_from: float | Unset = UNSET,
    cophsl_south_to: float | Unset = UNSET,
    stwpf_south_from: float | Unset = UNSET,
    stwpf_south_to: float | Unset = UNSET,
    wgrpp_south_from: float | Unset = UNSET,
    wgrpp_south_to: float | Unset = UNSET,
    actual_west_from: float | Unset = UNSET,
    actual_west_to: float | Unset = UNSET,
    cophsl_west_from: float | Unset = UNSET,
    cophsl_west_to: float | Unset = UNSET,
    stwpf_west_from: float | Unset = UNSET,
    stwpf_west_to: float | Unset = UNSET,
    wgrpp_west_from: float | Unset = UNSET,
    wgrpp_west_to: float | Unset = UNSET,
    actual_north_from: float | Unset = UNSET,
    actual_north_to: float | Unset = UNSET,
    cophsl_north_from: float | Unset = UNSET,
    cophsl_north_to: float | Unset = UNSET,
    stwpf_north_from: float | Unset = UNSET,
    stwpf_north_to: float | Unset = UNSET,
    wgrpp_north_from: float | Unset = UNSET,
    wgrpp_north_to: float | Unset = UNSET,
    dst_flag: bool | Unset = UNSET,
    posted_datetime_from: str | Unset = UNSET,
    posted_datetime_to: str | Unset = UNSET,
    page: int | Unset = UNSET,
    size: int | Unset = UNSET,
    sort: str | Unset = UNSET,
    dir_: str | Unset = UNSET,
) -> Exception_ | Report | None:
    """Wind Power Production - Hourly Averaged Actual and Forecasted Values by Geographical Region

     Wind Power Production - Hourly Averaged Actual and Forecasted Values by Geographical Region

    Args:
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
        actual_panhandle_from (float | Unset):
        actual_panhandle_to (float | Unset):
        cophsl_panhandle_from (float | Unset):
        cophsl_panhandle_to (float | Unset):
        stwpf_panhandle_from (float | Unset):
        stwpf_panhandle_to (float | Unset):
        wgrpp_panhandle_from (float | Unset):
        wgrpp_panhandle_to (float | Unset):
        actual_coastal_from (float | Unset):
        actual_coastal_to (float | Unset):
        cophsl_coastal_from (float | Unset):
        cophsl_coastal_to (float | Unset):
        stwpf_coastal_from (float | Unset):
        stwpf_coastal_to (float | Unset):
        wgrpp_coastal_from (float | Unset):
        wgrpp_coastal_to (float | Unset):
        actual_south_from (float | Unset):
        actual_south_to (float | Unset):
        cophsl_south_from (float | Unset):
        cophsl_south_to (float | Unset):
        stwpf_south_from (float | Unset):
        stwpf_south_to (float | Unset):
        wgrpp_south_from (float | Unset):
        wgrpp_south_to (float | Unset):
        actual_west_from (float | Unset):
        actual_west_to (float | Unset):
        cophsl_west_from (float | Unset):
        cophsl_west_to (float | Unset):
        stwpf_west_from (float | Unset):
        stwpf_west_to (float | Unset):
        wgrpp_west_from (float | Unset):
        wgrpp_west_to (float | Unset):
        actual_north_from (float | Unset):
        actual_north_to (float | Unset):
        cophsl_north_from (float | Unset):
        cophsl_north_to (float | Unset):
        stwpf_north_from (float | Unset):
        stwpf_north_to (float | Unset):
        wgrpp_north_from (float | Unset):
        wgrpp_north_to (float | Unset):
        dst_flag (bool | Unset):
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
        actual_panhandle_from=actual_panhandle_from,
        actual_panhandle_to=actual_panhandle_to,
        cophsl_panhandle_from=cophsl_panhandle_from,
        cophsl_panhandle_to=cophsl_panhandle_to,
        stwpf_panhandle_from=stwpf_panhandle_from,
        stwpf_panhandle_to=stwpf_panhandle_to,
        wgrpp_panhandle_from=wgrpp_panhandle_from,
        wgrpp_panhandle_to=wgrpp_panhandle_to,
        actual_coastal_from=actual_coastal_from,
        actual_coastal_to=actual_coastal_to,
        cophsl_coastal_from=cophsl_coastal_from,
        cophsl_coastal_to=cophsl_coastal_to,
        stwpf_coastal_from=stwpf_coastal_from,
        stwpf_coastal_to=stwpf_coastal_to,
        wgrpp_coastal_from=wgrpp_coastal_from,
        wgrpp_coastal_to=wgrpp_coastal_to,
        actual_south_from=actual_south_from,
        actual_south_to=actual_south_to,
        cophsl_south_from=cophsl_south_from,
        cophsl_south_to=cophsl_south_to,
        stwpf_south_from=stwpf_south_from,
        stwpf_south_to=stwpf_south_to,
        wgrpp_south_from=wgrpp_south_from,
        wgrpp_south_to=wgrpp_south_to,
        actual_west_from=actual_west_from,
        actual_west_to=actual_west_to,
        cophsl_west_from=cophsl_west_from,
        cophsl_west_to=cophsl_west_to,
        stwpf_west_from=stwpf_west_from,
        stwpf_west_to=stwpf_west_to,
        wgrpp_west_from=wgrpp_west_from,
        wgrpp_west_to=wgrpp_west_to,
        actual_north_from=actual_north_from,
        actual_north_to=actual_north_to,
        cophsl_north_from=cophsl_north_from,
        cophsl_north_to=cophsl_north_to,
        stwpf_north_from=stwpf_north_from,
        stwpf_north_to=stwpf_north_to,
        wgrpp_north_from=wgrpp_north_from,
        wgrpp_north_to=wgrpp_north_to,
        dst_flag=dst_flag,
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
    actual_panhandle_from: float | Unset = UNSET,
    actual_panhandle_to: float | Unset = UNSET,
    cophsl_panhandle_from: float | Unset = UNSET,
    cophsl_panhandle_to: float | Unset = UNSET,
    stwpf_panhandle_from: float | Unset = UNSET,
    stwpf_panhandle_to: float | Unset = UNSET,
    wgrpp_panhandle_from: float | Unset = UNSET,
    wgrpp_panhandle_to: float | Unset = UNSET,
    actual_coastal_from: float | Unset = UNSET,
    actual_coastal_to: float | Unset = UNSET,
    cophsl_coastal_from: float | Unset = UNSET,
    cophsl_coastal_to: float | Unset = UNSET,
    stwpf_coastal_from: float | Unset = UNSET,
    stwpf_coastal_to: float | Unset = UNSET,
    wgrpp_coastal_from: float | Unset = UNSET,
    wgrpp_coastal_to: float | Unset = UNSET,
    actual_south_from: float | Unset = UNSET,
    actual_south_to: float | Unset = UNSET,
    cophsl_south_from: float | Unset = UNSET,
    cophsl_south_to: float | Unset = UNSET,
    stwpf_south_from: float | Unset = UNSET,
    stwpf_south_to: float | Unset = UNSET,
    wgrpp_south_from: float | Unset = UNSET,
    wgrpp_south_to: float | Unset = UNSET,
    actual_west_from: float | Unset = UNSET,
    actual_west_to: float | Unset = UNSET,
    cophsl_west_from: float | Unset = UNSET,
    cophsl_west_to: float | Unset = UNSET,
    stwpf_west_from: float | Unset = UNSET,
    stwpf_west_to: float | Unset = UNSET,
    wgrpp_west_from: float | Unset = UNSET,
    wgrpp_west_to: float | Unset = UNSET,
    actual_north_from: float | Unset = UNSET,
    actual_north_to: float | Unset = UNSET,
    cophsl_north_from: float | Unset = UNSET,
    cophsl_north_to: float | Unset = UNSET,
    stwpf_north_from: float | Unset = UNSET,
    stwpf_north_to: float | Unset = UNSET,
    wgrpp_north_from: float | Unset = UNSET,
    wgrpp_north_to: float | Unset = UNSET,
    dst_flag: bool | Unset = UNSET,
    posted_datetime_from: str | Unset = UNSET,
    posted_datetime_to: str | Unset = UNSET,
    page: int | Unset = UNSET,
    size: int | Unset = UNSET,
    sort: str | Unset = UNSET,
    dir_: str | Unset = UNSET,
) -> Response[Exception_ | Report]:
    """Wind Power Production - Hourly Averaged Actual and Forecasted Values by Geographical Region

     Wind Power Production - Hourly Averaged Actual and Forecasted Values by Geographical Region

    Args:
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
        actual_panhandle_from (float | Unset):
        actual_panhandle_to (float | Unset):
        cophsl_panhandle_from (float | Unset):
        cophsl_panhandle_to (float | Unset):
        stwpf_panhandle_from (float | Unset):
        stwpf_panhandle_to (float | Unset):
        wgrpp_panhandle_from (float | Unset):
        wgrpp_panhandle_to (float | Unset):
        actual_coastal_from (float | Unset):
        actual_coastal_to (float | Unset):
        cophsl_coastal_from (float | Unset):
        cophsl_coastal_to (float | Unset):
        stwpf_coastal_from (float | Unset):
        stwpf_coastal_to (float | Unset):
        wgrpp_coastal_from (float | Unset):
        wgrpp_coastal_to (float | Unset):
        actual_south_from (float | Unset):
        actual_south_to (float | Unset):
        cophsl_south_from (float | Unset):
        cophsl_south_to (float | Unset):
        stwpf_south_from (float | Unset):
        stwpf_south_to (float | Unset):
        wgrpp_south_from (float | Unset):
        wgrpp_south_to (float | Unset):
        actual_west_from (float | Unset):
        actual_west_to (float | Unset):
        cophsl_west_from (float | Unset):
        cophsl_west_to (float | Unset):
        stwpf_west_from (float | Unset):
        stwpf_west_to (float | Unset):
        wgrpp_west_from (float | Unset):
        wgrpp_west_to (float | Unset):
        actual_north_from (float | Unset):
        actual_north_to (float | Unset):
        cophsl_north_from (float | Unset):
        cophsl_north_to (float | Unset):
        stwpf_north_from (float | Unset):
        stwpf_north_to (float | Unset):
        wgrpp_north_from (float | Unset):
        wgrpp_north_to (float | Unset):
        dst_flag (bool | Unset):
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
        actual_panhandle_from=actual_panhandle_from,
        actual_panhandle_to=actual_panhandle_to,
        cophsl_panhandle_from=cophsl_panhandle_from,
        cophsl_panhandle_to=cophsl_panhandle_to,
        stwpf_panhandle_from=stwpf_panhandle_from,
        stwpf_panhandle_to=stwpf_panhandle_to,
        wgrpp_panhandle_from=wgrpp_panhandle_from,
        wgrpp_panhandle_to=wgrpp_panhandle_to,
        actual_coastal_from=actual_coastal_from,
        actual_coastal_to=actual_coastal_to,
        cophsl_coastal_from=cophsl_coastal_from,
        cophsl_coastal_to=cophsl_coastal_to,
        stwpf_coastal_from=stwpf_coastal_from,
        stwpf_coastal_to=stwpf_coastal_to,
        wgrpp_coastal_from=wgrpp_coastal_from,
        wgrpp_coastal_to=wgrpp_coastal_to,
        actual_south_from=actual_south_from,
        actual_south_to=actual_south_to,
        cophsl_south_from=cophsl_south_from,
        cophsl_south_to=cophsl_south_to,
        stwpf_south_from=stwpf_south_from,
        stwpf_south_to=stwpf_south_to,
        wgrpp_south_from=wgrpp_south_from,
        wgrpp_south_to=wgrpp_south_to,
        actual_west_from=actual_west_from,
        actual_west_to=actual_west_to,
        cophsl_west_from=cophsl_west_from,
        cophsl_west_to=cophsl_west_to,
        stwpf_west_from=stwpf_west_from,
        stwpf_west_to=stwpf_west_to,
        wgrpp_west_from=wgrpp_west_from,
        wgrpp_west_to=wgrpp_west_to,
        actual_north_from=actual_north_from,
        actual_north_to=actual_north_to,
        cophsl_north_from=cophsl_north_from,
        cophsl_north_to=cophsl_north_to,
        stwpf_north_from=stwpf_north_from,
        stwpf_north_to=stwpf_north_to,
        wgrpp_north_from=wgrpp_north_from,
        wgrpp_north_to=wgrpp_north_to,
        dst_flag=dst_flag,
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
    actual_panhandle_from: float | Unset = UNSET,
    actual_panhandle_to: float | Unset = UNSET,
    cophsl_panhandle_from: float | Unset = UNSET,
    cophsl_panhandle_to: float | Unset = UNSET,
    stwpf_panhandle_from: float | Unset = UNSET,
    stwpf_panhandle_to: float | Unset = UNSET,
    wgrpp_panhandle_from: float | Unset = UNSET,
    wgrpp_panhandle_to: float | Unset = UNSET,
    actual_coastal_from: float | Unset = UNSET,
    actual_coastal_to: float | Unset = UNSET,
    cophsl_coastal_from: float | Unset = UNSET,
    cophsl_coastal_to: float | Unset = UNSET,
    stwpf_coastal_from: float | Unset = UNSET,
    stwpf_coastal_to: float | Unset = UNSET,
    wgrpp_coastal_from: float | Unset = UNSET,
    wgrpp_coastal_to: float | Unset = UNSET,
    actual_south_from: float | Unset = UNSET,
    actual_south_to: float | Unset = UNSET,
    cophsl_south_from: float | Unset = UNSET,
    cophsl_south_to: float | Unset = UNSET,
    stwpf_south_from: float | Unset = UNSET,
    stwpf_south_to: float | Unset = UNSET,
    wgrpp_south_from: float | Unset = UNSET,
    wgrpp_south_to: float | Unset = UNSET,
    actual_west_from: float | Unset = UNSET,
    actual_west_to: float | Unset = UNSET,
    cophsl_west_from: float | Unset = UNSET,
    cophsl_west_to: float | Unset = UNSET,
    stwpf_west_from: float | Unset = UNSET,
    stwpf_west_to: float | Unset = UNSET,
    wgrpp_west_from: float | Unset = UNSET,
    wgrpp_west_to: float | Unset = UNSET,
    actual_north_from: float | Unset = UNSET,
    actual_north_to: float | Unset = UNSET,
    cophsl_north_from: float | Unset = UNSET,
    cophsl_north_to: float | Unset = UNSET,
    stwpf_north_from: float | Unset = UNSET,
    stwpf_north_to: float | Unset = UNSET,
    wgrpp_north_from: float | Unset = UNSET,
    wgrpp_north_to: float | Unset = UNSET,
    dst_flag: bool | Unset = UNSET,
    posted_datetime_from: str | Unset = UNSET,
    posted_datetime_to: str | Unset = UNSET,
    page: int | Unset = UNSET,
    size: int | Unset = UNSET,
    sort: str | Unset = UNSET,
    dir_: str | Unset = UNSET,
) -> Exception_ | Report | None:
    """Wind Power Production - Hourly Averaged Actual and Forecasted Values by Geographical Region

     Wind Power Production - Hourly Averaged Actual and Forecasted Values by Geographical Region

    Args:
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
        actual_panhandle_from (float | Unset):
        actual_panhandle_to (float | Unset):
        cophsl_panhandle_from (float | Unset):
        cophsl_panhandle_to (float | Unset):
        stwpf_panhandle_from (float | Unset):
        stwpf_panhandle_to (float | Unset):
        wgrpp_panhandle_from (float | Unset):
        wgrpp_panhandle_to (float | Unset):
        actual_coastal_from (float | Unset):
        actual_coastal_to (float | Unset):
        cophsl_coastal_from (float | Unset):
        cophsl_coastal_to (float | Unset):
        stwpf_coastal_from (float | Unset):
        stwpf_coastal_to (float | Unset):
        wgrpp_coastal_from (float | Unset):
        wgrpp_coastal_to (float | Unset):
        actual_south_from (float | Unset):
        actual_south_to (float | Unset):
        cophsl_south_from (float | Unset):
        cophsl_south_to (float | Unset):
        stwpf_south_from (float | Unset):
        stwpf_south_to (float | Unset):
        wgrpp_south_from (float | Unset):
        wgrpp_south_to (float | Unset):
        actual_west_from (float | Unset):
        actual_west_to (float | Unset):
        cophsl_west_from (float | Unset):
        cophsl_west_to (float | Unset):
        stwpf_west_from (float | Unset):
        stwpf_west_to (float | Unset):
        wgrpp_west_from (float | Unset):
        wgrpp_west_to (float | Unset):
        actual_north_from (float | Unset):
        actual_north_to (float | Unset):
        cophsl_north_from (float | Unset):
        cophsl_north_to (float | Unset):
        stwpf_north_from (float | Unset):
        stwpf_north_to (float | Unset):
        wgrpp_north_from (float | Unset):
        wgrpp_north_to (float | Unset):
        dst_flag (bool | Unset):
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
            actual_panhandle_from=actual_panhandle_from,
            actual_panhandle_to=actual_panhandle_to,
            cophsl_panhandle_from=cophsl_panhandle_from,
            cophsl_panhandle_to=cophsl_panhandle_to,
            stwpf_panhandle_from=stwpf_panhandle_from,
            stwpf_panhandle_to=stwpf_panhandle_to,
            wgrpp_panhandle_from=wgrpp_panhandle_from,
            wgrpp_panhandle_to=wgrpp_panhandle_to,
            actual_coastal_from=actual_coastal_from,
            actual_coastal_to=actual_coastal_to,
            cophsl_coastal_from=cophsl_coastal_from,
            cophsl_coastal_to=cophsl_coastal_to,
            stwpf_coastal_from=stwpf_coastal_from,
            stwpf_coastal_to=stwpf_coastal_to,
            wgrpp_coastal_from=wgrpp_coastal_from,
            wgrpp_coastal_to=wgrpp_coastal_to,
            actual_south_from=actual_south_from,
            actual_south_to=actual_south_to,
            cophsl_south_from=cophsl_south_from,
            cophsl_south_to=cophsl_south_to,
            stwpf_south_from=stwpf_south_from,
            stwpf_south_to=stwpf_south_to,
            wgrpp_south_from=wgrpp_south_from,
            wgrpp_south_to=wgrpp_south_to,
            actual_west_from=actual_west_from,
            actual_west_to=actual_west_to,
            cophsl_west_from=cophsl_west_from,
            cophsl_west_to=cophsl_west_to,
            stwpf_west_from=stwpf_west_from,
            stwpf_west_to=stwpf_west_to,
            wgrpp_west_from=wgrpp_west_from,
            wgrpp_west_to=wgrpp_west_to,
            actual_north_from=actual_north_from,
            actual_north_to=actual_north_to,
            cophsl_north_from=cophsl_north_from,
            cophsl_north_to=cophsl_north_to,
            stwpf_north_from=stwpf_north_from,
            stwpf_north_to=stwpf_north_to,
            wgrpp_north_from=wgrpp_north_from,
            wgrpp_north_to=wgrpp_north_to,
            dst_flag=dst_flag,
            posted_datetime_from=posted_datetime_from,
            posted_datetime_to=posted_datetime_to,
            page=page,
            size=size,
            sort=sort,
            dir_=dir_,
        )
    ).parsed
