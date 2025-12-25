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
    posted_datetime_from: str | Unset = UNSET,
    posted_datetime_to: str | Unset = UNSET,
    hour_ending_from: int | Unset = UNSET,
    hour_ending_to: int | Unset = UNSET,
    gen_system_wide_from: float | Unset = UNSET,
    gen_system_wide_to: float | Unset = UNSET,
    cophsl_system_wide_from: float | Unset = UNSET,
    cophsl_system_wide_to: float | Unset = UNSET,
    stppf_system_wide_from: float | Unset = UNSET,
    stppf_system_wide_to: float | Unset = UNSET,
    pvgrpp_system_wide_from: float | Unset = UNSET,
    pvgrpp_system_wide_to: float | Unset = UNSET,
    gen_center_west_from: float | Unset = UNSET,
    gen_center_west_to: float | Unset = UNSET,
    cophsl_center_west_from: float | Unset = UNSET,
    cophsl_center_west_to: float | Unset = UNSET,
    stppf_center_west_from: float | Unset = UNSET,
    stppf_center_west_to: float | Unset = UNSET,
    pvgrpp_center_west_from: float | Unset = UNSET,
    pvgrpp_center_west_to: float | Unset = UNSET,
    gen_north_west_from: float | Unset = UNSET,
    gen_north_west_to: float | Unset = UNSET,
    cophsl_north_west_from: float | Unset = UNSET,
    cophsl_north_west_to: float | Unset = UNSET,
    stppf_north_west_from: float | Unset = UNSET,
    stppf_north_west_to: float | Unset = UNSET,
    pvgrpp_north_west_from: float | Unset = UNSET,
    pvgrpp_north_west_to: float | Unset = UNSET,
    gen_far_west_from: float | Unset = UNSET,
    gen_far_west_to: float | Unset = UNSET,
    cophsl_far_west_from: float | Unset = UNSET,
    cophsl_far_west_to: float | Unset = UNSET,
    stppf_far_west_from: float | Unset = UNSET,
    stppf_far_west_to: float | Unset = UNSET,
    pvgrpp_far_west_from: float | Unset = UNSET,
    pvgrpp_far_west_to: float | Unset = UNSET,
    gen_far_east_from: float | Unset = UNSET,
    gen_far_east_to: float | Unset = UNSET,
    cophsl_far_east_from: float | Unset = UNSET,
    cophsl_far_east_to: float | Unset = UNSET,
    stppf_far_east_from: float | Unset = UNSET,
    stppf_far_east_to: float | Unset = UNSET,
    pvgrpp_far_east_from: float | Unset = UNSET,
    pvgrpp_far_east_to: float | Unset = UNSET,
    gen_south_east_from: float | Unset = UNSET,
    gen_south_east_to: float | Unset = UNSET,
    cophsl_south_east_from: float | Unset = UNSET,
    cophsl_south_east_to: float | Unset = UNSET,
    stppf_south_east_from: float | Unset = UNSET,
    stppf_south_east_to: float | Unset = UNSET,
    pvgrpp_south_east_from: float | Unset = UNSET,
    pvgrpp_south_east_to: float | Unset = UNSET,
    gen_center_east_from: float | Unset = UNSET,
    gen_center_east_to: float | Unset = UNSET,
    cophsl_center_east_from: float | Unset = UNSET,
    cophsl_center_east_to: float | Unset = UNSET,
    stppf_center_east_from: float | Unset = UNSET,
    stppf_center_east_to: float | Unset = UNSET,
    pvgrpp_center_east_from: float | Unset = UNSET,
    pvgrpp_center_east_to: float | Unset = UNSET,
    dst_flag: bool | Unset = UNSET,
    page: int | Unset = UNSET,
    size: int | Unset = UNSET,
    sort: str | Unset = UNSET,
    dir_: str | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["deliveryDateFrom"] = delivery_date_from

    params["deliveryDateTo"] = delivery_date_to

    params["postedDatetimeFrom"] = posted_datetime_from

    params["postedDatetimeTo"] = posted_datetime_to

    params["hourEndingFrom"] = hour_ending_from

    params["hourEndingTo"] = hour_ending_to

    params["genSystemWideFrom"] = gen_system_wide_from

    params["genSystemWideTo"] = gen_system_wide_to

    params["COPHSLSystemWideFrom"] = cophsl_system_wide_from

    params["COPHSLSystemWideTo"] = cophsl_system_wide_to

    params["STPPFSystemWideFrom"] = stppf_system_wide_from

    params["STPPFSystemWideTo"] = stppf_system_wide_to

    params["PVGRPPSystemWideFrom"] = pvgrpp_system_wide_from

    params["PVGRPPSystemWideTo"] = pvgrpp_system_wide_to

    params["genCenterWestFrom"] = gen_center_west_from

    params["genCenterWestTo"] = gen_center_west_to

    params["COPHSLCenterWestFrom"] = cophsl_center_west_from

    params["COPHSLCenterWestTo"] = cophsl_center_west_to

    params["STPPFCenterWestFrom"] = stppf_center_west_from

    params["STPPFCenterWestTo"] = stppf_center_west_to

    params["PVGRPPCenterWestFrom"] = pvgrpp_center_west_from

    params["PVGRPPCenterWestTo"] = pvgrpp_center_west_to

    params["genNorthWestFrom"] = gen_north_west_from

    params["genNorthWestTo"] = gen_north_west_to

    params["COPHSLNorthWestFrom"] = cophsl_north_west_from

    params["COPHSLNorthWestTo"] = cophsl_north_west_to

    params["STPPFNorthWestFrom"] = stppf_north_west_from

    params["STPPFNorthWestTo"] = stppf_north_west_to

    params["PVGRPPNorthWestFrom"] = pvgrpp_north_west_from

    params["PVGRPPNorthWestTo"] = pvgrpp_north_west_to

    params["genFarWestFrom"] = gen_far_west_from

    params["genFarWestTo"] = gen_far_west_to

    params["COPHSLFarWestFrom"] = cophsl_far_west_from

    params["COPHSLFarWestTo"] = cophsl_far_west_to

    params["STPPFFarWestFrom"] = stppf_far_west_from

    params["STPPFFarWestTo"] = stppf_far_west_to

    params["PVGRPPFarWestFrom"] = pvgrpp_far_west_from

    params["PVGRPPFarWestTo"] = pvgrpp_far_west_to

    params["genFarEastFrom"] = gen_far_east_from

    params["genFarEastTo"] = gen_far_east_to

    params["COPHSLFarEastFrom"] = cophsl_far_east_from

    params["COPHSLFarEastTo"] = cophsl_far_east_to

    params["STPPFFarEastFrom"] = stppf_far_east_from

    params["STPPFFarEastTo"] = stppf_far_east_to

    params["PVGRPPFarEastFrom"] = pvgrpp_far_east_from

    params["PVGRPPFarEastTo"] = pvgrpp_far_east_to

    params["genSouthEastFrom"] = gen_south_east_from

    params["genSouthEastTo"] = gen_south_east_to

    params["COPHSLSouthEastFrom"] = cophsl_south_east_from

    params["COPHSLSouthEastTo"] = cophsl_south_east_to

    params["STPPFSouthEastFrom"] = stppf_south_east_from

    params["STPPFSouthEastTo"] = stppf_south_east_to

    params["PVGRPPSouthEastFrom"] = pvgrpp_south_east_from

    params["PVGRPPSouthEastTo"] = pvgrpp_south_east_to

    params["genCenterEastFrom"] = gen_center_east_from

    params["genCenterEastTo"] = gen_center_east_to

    params["COPHSLCenterEastFrom"] = cophsl_center_east_from

    params["COPHSLCenterEastTo"] = cophsl_center_east_to

    params["STPPFCenterEastFrom"] = stppf_center_east_from

    params["STPPFCenterEastTo"] = stppf_center_east_to

    params["PVGRPPCenterEastFrom"] = pvgrpp_center_east_from

    params["PVGRPPCenterEastTo"] = pvgrpp_center_east_to

    params["DSTFlag"] = dst_flag

    params["page"] = page

    params["size"] = size

    params["sort"] = sort

    params["dir"] = dir_

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/np4-745-cd/spp_hrly_actual_fcast_geo",
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
    posted_datetime_from: str | Unset = UNSET,
    posted_datetime_to: str | Unset = UNSET,
    hour_ending_from: int | Unset = UNSET,
    hour_ending_to: int | Unset = UNSET,
    gen_system_wide_from: float | Unset = UNSET,
    gen_system_wide_to: float | Unset = UNSET,
    cophsl_system_wide_from: float | Unset = UNSET,
    cophsl_system_wide_to: float | Unset = UNSET,
    stppf_system_wide_from: float | Unset = UNSET,
    stppf_system_wide_to: float | Unset = UNSET,
    pvgrpp_system_wide_from: float | Unset = UNSET,
    pvgrpp_system_wide_to: float | Unset = UNSET,
    gen_center_west_from: float | Unset = UNSET,
    gen_center_west_to: float | Unset = UNSET,
    cophsl_center_west_from: float | Unset = UNSET,
    cophsl_center_west_to: float | Unset = UNSET,
    stppf_center_west_from: float | Unset = UNSET,
    stppf_center_west_to: float | Unset = UNSET,
    pvgrpp_center_west_from: float | Unset = UNSET,
    pvgrpp_center_west_to: float | Unset = UNSET,
    gen_north_west_from: float | Unset = UNSET,
    gen_north_west_to: float | Unset = UNSET,
    cophsl_north_west_from: float | Unset = UNSET,
    cophsl_north_west_to: float | Unset = UNSET,
    stppf_north_west_from: float | Unset = UNSET,
    stppf_north_west_to: float | Unset = UNSET,
    pvgrpp_north_west_from: float | Unset = UNSET,
    pvgrpp_north_west_to: float | Unset = UNSET,
    gen_far_west_from: float | Unset = UNSET,
    gen_far_west_to: float | Unset = UNSET,
    cophsl_far_west_from: float | Unset = UNSET,
    cophsl_far_west_to: float | Unset = UNSET,
    stppf_far_west_from: float | Unset = UNSET,
    stppf_far_west_to: float | Unset = UNSET,
    pvgrpp_far_west_from: float | Unset = UNSET,
    pvgrpp_far_west_to: float | Unset = UNSET,
    gen_far_east_from: float | Unset = UNSET,
    gen_far_east_to: float | Unset = UNSET,
    cophsl_far_east_from: float | Unset = UNSET,
    cophsl_far_east_to: float | Unset = UNSET,
    stppf_far_east_from: float | Unset = UNSET,
    stppf_far_east_to: float | Unset = UNSET,
    pvgrpp_far_east_from: float | Unset = UNSET,
    pvgrpp_far_east_to: float | Unset = UNSET,
    gen_south_east_from: float | Unset = UNSET,
    gen_south_east_to: float | Unset = UNSET,
    cophsl_south_east_from: float | Unset = UNSET,
    cophsl_south_east_to: float | Unset = UNSET,
    stppf_south_east_from: float | Unset = UNSET,
    stppf_south_east_to: float | Unset = UNSET,
    pvgrpp_south_east_from: float | Unset = UNSET,
    pvgrpp_south_east_to: float | Unset = UNSET,
    gen_center_east_from: float | Unset = UNSET,
    gen_center_east_to: float | Unset = UNSET,
    cophsl_center_east_from: float | Unset = UNSET,
    cophsl_center_east_to: float | Unset = UNSET,
    stppf_center_east_from: float | Unset = UNSET,
    stppf_center_east_to: float | Unset = UNSET,
    pvgrpp_center_east_from: float | Unset = UNSET,
    pvgrpp_center_east_to: float | Unset = UNSET,
    dst_flag: bool | Unset = UNSET,
    page: int | Unset = UNSET,
    size: int | Unset = UNSET,
    sort: str | Unset = UNSET,
    dir_: str | Unset = UNSET,
) -> Response[Exception_ | Report]:
    """Solar Power Production - Hourly Averaged Actual and Forecasted Values by Geographical Region

     Solar Power Production - Hourly Averaged Actual and Forecasted Values by Geographical Region

    Args:
        delivery_date_from (str | Unset):
        delivery_date_to (str | Unset):
        posted_datetime_from (str | Unset):
        posted_datetime_to (str | Unset):
        hour_ending_from (int | Unset):
        hour_ending_to (int | Unset):
        gen_system_wide_from (float | Unset):
        gen_system_wide_to (float | Unset):
        cophsl_system_wide_from (float | Unset):
        cophsl_system_wide_to (float | Unset):
        stppf_system_wide_from (float | Unset):
        stppf_system_wide_to (float | Unset):
        pvgrpp_system_wide_from (float | Unset):
        pvgrpp_system_wide_to (float | Unset):
        gen_center_west_from (float | Unset):
        gen_center_west_to (float | Unset):
        cophsl_center_west_from (float | Unset):
        cophsl_center_west_to (float | Unset):
        stppf_center_west_from (float | Unset):
        stppf_center_west_to (float | Unset):
        pvgrpp_center_west_from (float | Unset):
        pvgrpp_center_west_to (float | Unset):
        gen_north_west_from (float | Unset):
        gen_north_west_to (float | Unset):
        cophsl_north_west_from (float | Unset):
        cophsl_north_west_to (float | Unset):
        stppf_north_west_from (float | Unset):
        stppf_north_west_to (float | Unset):
        pvgrpp_north_west_from (float | Unset):
        pvgrpp_north_west_to (float | Unset):
        gen_far_west_from (float | Unset):
        gen_far_west_to (float | Unset):
        cophsl_far_west_from (float | Unset):
        cophsl_far_west_to (float | Unset):
        stppf_far_west_from (float | Unset):
        stppf_far_west_to (float | Unset):
        pvgrpp_far_west_from (float | Unset):
        pvgrpp_far_west_to (float | Unset):
        gen_far_east_from (float | Unset):
        gen_far_east_to (float | Unset):
        cophsl_far_east_from (float | Unset):
        cophsl_far_east_to (float | Unset):
        stppf_far_east_from (float | Unset):
        stppf_far_east_to (float | Unset):
        pvgrpp_far_east_from (float | Unset):
        pvgrpp_far_east_to (float | Unset):
        gen_south_east_from (float | Unset):
        gen_south_east_to (float | Unset):
        cophsl_south_east_from (float | Unset):
        cophsl_south_east_to (float | Unset):
        stppf_south_east_from (float | Unset):
        stppf_south_east_to (float | Unset):
        pvgrpp_south_east_from (float | Unset):
        pvgrpp_south_east_to (float | Unset):
        gen_center_east_from (float | Unset):
        gen_center_east_to (float | Unset):
        cophsl_center_east_from (float | Unset):
        cophsl_center_east_to (float | Unset):
        stppf_center_east_from (float | Unset):
        stppf_center_east_to (float | Unset):
        pvgrpp_center_east_from (float | Unset):
        pvgrpp_center_east_to (float | Unset):
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
        posted_datetime_from=posted_datetime_from,
        posted_datetime_to=posted_datetime_to,
        hour_ending_from=hour_ending_from,
        hour_ending_to=hour_ending_to,
        gen_system_wide_from=gen_system_wide_from,
        gen_system_wide_to=gen_system_wide_to,
        cophsl_system_wide_from=cophsl_system_wide_from,
        cophsl_system_wide_to=cophsl_system_wide_to,
        stppf_system_wide_from=stppf_system_wide_from,
        stppf_system_wide_to=stppf_system_wide_to,
        pvgrpp_system_wide_from=pvgrpp_system_wide_from,
        pvgrpp_system_wide_to=pvgrpp_system_wide_to,
        gen_center_west_from=gen_center_west_from,
        gen_center_west_to=gen_center_west_to,
        cophsl_center_west_from=cophsl_center_west_from,
        cophsl_center_west_to=cophsl_center_west_to,
        stppf_center_west_from=stppf_center_west_from,
        stppf_center_west_to=stppf_center_west_to,
        pvgrpp_center_west_from=pvgrpp_center_west_from,
        pvgrpp_center_west_to=pvgrpp_center_west_to,
        gen_north_west_from=gen_north_west_from,
        gen_north_west_to=gen_north_west_to,
        cophsl_north_west_from=cophsl_north_west_from,
        cophsl_north_west_to=cophsl_north_west_to,
        stppf_north_west_from=stppf_north_west_from,
        stppf_north_west_to=stppf_north_west_to,
        pvgrpp_north_west_from=pvgrpp_north_west_from,
        pvgrpp_north_west_to=pvgrpp_north_west_to,
        gen_far_west_from=gen_far_west_from,
        gen_far_west_to=gen_far_west_to,
        cophsl_far_west_from=cophsl_far_west_from,
        cophsl_far_west_to=cophsl_far_west_to,
        stppf_far_west_from=stppf_far_west_from,
        stppf_far_west_to=stppf_far_west_to,
        pvgrpp_far_west_from=pvgrpp_far_west_from,
        pvgrpp_far_west_to=pvgrpp_far_west_to,
        gen_far_east_from=gen_far_east_from,
        gen_far_east_to=gen_far_east_to,
        cophsl_far_east_from=cophsl_far_east_from,
        cophsl_far_east_to=cophsl_far_east_to,
        stppf_far_east_from=stppf_far_east_from,
        stppf_far_east_to=stppf_far_east_to,
        pvgrpp_far_east_from=pvgrpp_far_east_from,
        pvgrpp_far_east_to=pvgrpp_far_east_to,
        gen_south_east_from=gen_south_east_from,
        gen_south_east_to=gen_south_east_to,
        cophsl_south_east_from=cophsl_south_east_from,
        cophsl_south_east_to=cophsl_south_east_to,
        stppf_south_east_from=stppf_south_east_from,
        stppf_south_east_to=stppf_south_east_to,
        pvgrpp_south_east_from=pvgrpp_south_east_from,
        pvgrpp_south_east_to=pvgrpp_south_east_to,
        gen_center_east_from=gen_center_east_from,
        gen_center_east_to=gen_center_east_to,
        cophsl_center_east_from=cophsl_center_east_from,
        cophsl_center_east_to=cophsl_center_east_to,
        stppf_center_east_from=stppf_center_east_from,
        stppf_center_east_to=stppf_center_east_to,
        pvgrpp_center_east_from=pvgrpp_center_east_from,
        pvgrpp_center_east_to=pvgrpp_center_east_to,
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
    posted_datetime_from: str | Unset = UNSET,
    posted_datetime_to: str | Unset = UNSET,
    hour_ending_from: int | Unset = UNSET,
    hour_ending_to: int | Unset = UNSET,
    gen_system_wide_from: float | Unset = UNSET,
    gen_system_wide_to: float | Unset = UNSET,
    cophsl_system_wide_from: float | Unset = UNSET,
    cophsl_system_wide_to: float | Unset = UNSET,
    stppf_system_wide_from: float | Unset = UNSET,
    stppf_system_wide_to: float | Unset = UNSET,
    pvgrpp_system_wide_from: float | Unset = UNSET,
    pvgrpp_system_wide_to: float | Unset = UNSET,
    gen_center_west_from: float | Unset = UNSET,
    gen_center_west_to: float | Unset = UNSET,
    cophsl_center_west_from: float | Unset = UNSET,
    cophsl_center_west_to: float | Unset = UNSET,
    stppf_center_west_from: float | Unset = UNSET,
    stppf_center_west_to: float | Unset = UNSET,
    pvgrpp_center_west_from: float | Unset = UNSET,
    pvgrpp_center_west_to: float | Unset = UNSET,
    gen_north_west_from: float | Unset = UNSET,
    gen_north_west_to: float | Unset = UNSET,
    cophsl_north_west_from: float | Unset = UNSET,
    cophsl_north_west_to: float | Unset = UNSET,
    stppf_north_west_from: float | Unset = UNSET,
    stppf_north_west_to: float | Unset = UNSET,
    pvgrpp_north_west_from: float | Unset = UNSET,
    pvgrpp_north_west_to: float | Unset = UNSET,
    gen_far_west_from: float | Unset = UNSET,
    gen_far_west_to: float | Unset = UNSET,
    cophsl_far_west_from: float | Unset = UNSET,
    cophsl_far_west_to: float | Unset = UNSET,
    stppf_far_west_from: float | Unset = UNSET,
    stppf_far_west_to: float | Unset = UNSET,
    pvgrpp_far_west_from: float | Unset = UNSET,
    pvgrpp_far_west_to: float | Unset = UNSET,
    gen_far_east_from: float | Unset = UNSET,
    gen_far_east_to: float | Unset = UNSET,
    cophsl_far_east_from: float | Unset = UNSET,
    cophsl_far_east_to: float | Unset = UNSET,
    stppf_far_east_from: float | Unset = UNSET,
    stppf_far_east_to: float | Unset = UNSET,
    pvgrpp_far_east_from: float | Unset = UNSET,
    pvgrpp_far_east_to: float | Unset = UNSET,
    gen_south_east_from: float | Unset = UNSET,
    gen_south_east_to: float | Unset = UNSET,
    cophsl_south_east_from: float | Unset = UNSET,
    cophsl_south_east_to: float | Unset = UNSET,
    stppf_south_east_from: float | Unset = UNSET,
    stppf_south_east_to: float | Unset = UNSET,
    pvgrpp_south_east_from: float | Unset = UNSET,
    pvgrpp_south_east_to: float | Unset = UNSET,
    gen_center_east_from: float | Unset = UNSET,
    gen_center_east_to: float | Unset = UNSET,
    cophsl_center_east_from: float | Unset = UNSET,
    cophsl_center_east_to: float | Unset = UNSET,
    stppf_center_east_from: float | Unset = UNSET,
    stppf_center_east_to: float | Unset = UNSET,
    pvgrpp_center_east_from: float | Unset = UNSET,
    pvgrpp_center_east_to: float | Unset = UNSET,
    dst_flag: bool | Unset = UNSET,
    page: int | Unset = UNSET,
    size: int | Unset = UNSET,
    sort: str | Unset = UNSET,
    dir_: str | Unset = UNSET,
) -> Exception_ | Report | None:
    """Solar Power Production - Hourly Averaged Actual and Forecasted Values by Geographical Region

     Solar Power Production - Hourly Averaged Actual and Forecasted Values by Geographical Region

    Args:
        delivery_date_from (str | Unset):
        delivery_date_to (str | Unset):
        posted_datetime_from (str | Unset):
        posted_datetime_to (str | Unset):
        hour_ending_from (int | Unset):
        hour_ending_to (int | Unset):
        gen_system_wide_from (float | Unset):
        gen_system_wide_to (float | Unset):
        cophsl_system_wide_from (float | Unset):
        cophsl_system_wide_to (float | Unset):
        stppf_system_wide_from (float | Unset):
        stppf_system_wide_to (float | Unset):
        pvgrpp_system_wide_from (float | Unset):
        pvgrpp_system_wide_to (float | Unset):
        gen_center_west_from (float | Unset):
        gen_center_west_to (float | Unset):
        cophsl_center_west_from (float | Unset):
        cophsl_center_west_to (float | Unset):
        stppf_center_west_from (float | Unset):
        stppf_center_west_to (float | Unset):
        pvgrpp_center_west_from (float | Unset):
        pvgrpp_center_west_to (float | Unset):
        gen_north_west_from (float | Unset):
        gen_north_west_to (float | Unset):
        cophsl_north_west_from (float | Unset):
        cophsl_north_west_to (float | Unset):
        stppf_north_west_from (float | Unset):
        stppf_north_west_to (float | Unset):
        pvgrpp_north_west_from (float | Unset):
        pvgrpp_north_west_to (float | Unset):
        gen_far_west_from (float | Unset):
        gen_far_west_to (float | Unset):
        cophsl_far_west_from (float | Unset):
        cophsl_far_west_to (float | Unset):
        stppf_far_west_from (float | Unset):
        stppf_far_west_to (float | Unset):
        pvgrpp_far_west_from (float | Unset):
        pvgrpp_far_west_to (float | Unset):
        gen_far_east_from (float | Unset):
        gen_far_east_to (float | Unset):
        cophsl_far_east_from (float | Unset):
        cophsl_far_east_to (float | Unset):
        stppf_far_east_from (float | Unset):
        stppf_far_east_to (float | Unset):
        pvgrpp_far_east_from (float | Unset):
        pvgrpp_far_east_to (float | Unset):
        gen_south_east_from (float | Unset):
        gen_south_east_to (float | Unset):
        cophsl_south_east_from (float | Unset):
        cophsl_south_east_to (float | Unset):
        stppf_south_east_from (float | Unset):
        stppf_south_east_to (float | Unset):
        pvgrpp_south_east_from (float | Unset):
        pvgrpp_south_east_to (float | Unset):
        gen_center_east_from (float | Unset):
        gen_center_east_to (float | Unset):
        cophsl_center_east_from (float | Unset):
        cophsl_center_east_to (float | Unset):
        stppf_center_east_from (float | Unset):
        stppf_center_east_to (float | Unset):
        pvgrpp_center_east_from (float | Unset):
        pvgrpp_center_east_to (float | Unset):
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
        posted_datetime_from=posted_datetime_from,
        posted_datetime_to=posted_datetime_to,
        hour_ending_from=hour_ending_from,
        hour_ending_to=hour_ending_to,
        gen_system_wide_from=gen_system_wide_from,
        gen_system_wide_to=gen_system_wide_to,
        cophsl_system_wide_from=cophsl_system_wide_from,
        cophsl_system_wide_to=cophsl_system_wide_to,
        stppf_system_wide_from=stppf_system_wide_from,
        stppf_system_wide_to=stppf_system_wide_to,
        pvgrpp_system_wide_from=pvgrpp_system_wide_from,
        pvgrpp_system_wide_to=pvgrpp_system_wide_to,
        gen_center_west_from=gen_center_west_from,
        gen_center_west_to=gen_center_west_to,
        cophsl_center_west_from=cophsl_center_west_from,
        cophsl_center_west_to=cophsl_center_west_to,
        stppf_center_west_from=stppf_center_west_from,
        stppf_center_west_to=stppf_center_west_to,
        pvgrpp_center_west_from=pvgrpp_center_west_from,
        pvgrpp_center_west_to=pvgrpp_center_west_to,
        gen_north_west_from=gen_north_west_from,
        gen_north_west_to=gen_north_west_to,
        cophsl_north_west_from=cophsl_north_west_from,
        cophsl_north_west_to=cophsl_north_west_to,
        stppf_north_west_from=stppf_north_west_from,
        stppf_north_west_to=stppf_north_west_to,
        pvgrpp_north_west_from=pvgrpp_north_west_from,
        pvgrpp_north_west_to=pvgrpp_north_west_to,
        gen_far_west_from=gen_far_west_from,
        gen_far_west_to=gen_far_west_to,
        cophsl_far_west_from=cophsl_far_west_from,
        cophsl_far_west_to=cophsl_far_west_to,
        stppf_far_west_from=stppf_far_west_from,
        stppf_far_west_to=stppf_far_west_to,
        pvgrpp_far_west_from=pvgrpp_far_west_from,
        pvgrpp_far_west_to=pvgrpp_far_west_to,
        gen_far_east_from=gen_far_east_from,
        gen_far_east_to=gen_far_east_to,
        cophsl_far_east_from=cophsl_far_east_from,
        cophsl_far_east_to=cophsl_far_east_to,
        stppf_far_east_from=stppf_far_east_from,
        stppf_far_east_to=stppf_far_east_to,
        pvgrpp_far_east_from=pvgrpp_far_east_from,
        pvgrpp_far_east_to=pvgrpp_far_east_to,
        gen_south_east_from=gen_south_east_from,
        gen_south_east_to=gen_south_east_to,
        cophsl_south_east_from=cophsl_south_east_from,
        cophsl_south_east_to=cophsl_south_east_to,
        stppf_south_east_from=stppf_south_east_from,
        stppf_south_east_to=stppf_south_east_to,
        pvgrpp_south_east_from=pvgrpp_south_east_from,
        pvgrpp_south_east_to=pvgrpp_south_east_to,
        gen_center_east_from=gen_center_east_from,
        gen_center_east_to=gen_center_east_to,
        cophsl_center_east_from=cophsl_center_east_from,
        cophsl_center_east_to=cophsl_center_east_to,
        stppf_center_east_from=stppf_center_east_from,
        stppf_center_east_to=stppf_center_east_to,
        pvgrpp_center_east_from=pvgrpp_center_east_from,
        pvgrpp_center_east_to=pvgrpp_center_east_to,
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
    posted_datetime_from: str | Unset = UNSET,
    posted_datetime_to: str | Unset = UNSET,
    hour_ending_from: int | Unset = UNSET,
    hour_ending_to: int | Unset = UNSET,
    gen_system_wide_from: float | Unset = UNSET,
    gen_system_wide_to: float | Unset = UNSET,
    cophsl_system_wide_from: float | Unset = UNSET,
    cophsl_system_wide_to: float | Unset = UNSET,
    stppf_system_wide_from: float | Unset = UNSET,
    stppf_system_wide_to: float | Unset = UNSET,
    pvgrpp_system_wide_from: float | Unset = UNSET,
    pvgrpp_system_wide_to: float | Unset = UNSET,
    gen_center_west_from: float | Unset = UNSET,
    gen_center_west_to: float | Unset = UNSET,
    cophsl_center_west_from: float | Unset = UNSET,
    cophsl_center_west_to: float | Unset = UNSET,
    stppf_center_west_from: float | Unset = UNSET,
    stppf_center_west_to: float | Unset = UNSET,
    pvgrpp_center_west_from: float | Unset = UNSET,
    pvgrpp_center_west_to: float | Unset = UNSET,
    gen_north_west_from: float | Unset = UNSET,
    gen_north_west_to: float | Unset = UNSET,
    cophsl_north_west_from: float | Unset = UNSET,
    cophsl_north_west_to: float | Unset = UNSET,
    stppf_north_west_from: float | Unset = UNSET,
    stppf_north_west_to: float | Unset = UNSET,
    pvgrpp_north_west_from: float | Unset = UNSET,
    pvgrpp_north_west_to: float | Unset = UNSET,
    gen_far_west_from: float | Unset = UNSET,
    gen_far_west_to: float | Unset = UNSET,
    cophsl_far_west_from: float | Unset = UNSET,
    cophsl_far_west_to: float | Unset = UNSET,
    stppf_far_west_from: float | Unset = UNSET,
    stppf_far_west_to: float | Unset = UNSET,
    pvgrpp_far_west_from: float | Unset = UNSET,
    pvgrpp_far_west_to: float | Unset = UNSET,
    gen_far_east_from: float | Unset = UNSET,
    gen_far_east_to: float | Unset = UNSET,
    cophsl_far_east_from: float | Unset = UNSET,
    cophsl_far_east_to: float | Unset = UNSET,
    stppf_far_east_from: float | Unset = UNSET,
    stppf_far_east_to: float | Unset = UNSET,
    pvgrpp_far_east_from: float | Unset = UNSET,
    pvgrpp_far_east_to: float | Unset = UNSET,
    gen_south_east_from: float | Unset = UNSET,
    gen_south_east_to: float | Unset = UNSET,
    cophsl_south_east_from: float | Unset = UNSET,
    cophsl_south_east_to: float | Unset = UNSET,
    stppf_south_east_from: float | Unset = UNSET,
    stppf_south_east_to: float | Unset = UNSET,
    pvgrpp_south_east_from: float | Unset = UNSET,
    pvgrpp_south_east_to: float | Unset = UNSET,
    gen_center_east_from: float | Unset = UNSET,
    gen_center_east_to: float | Unset = UNSET,
    cophsl_center_east_from: float | Unset = UNSET,
    cophsl_center_east_to: float | Unset = UNSET,
    stppf_center_east_from: float | Unset = UNSET,
    stppf_center_east_to: float | Unset = UNSET,
    pvgrpp_center_east_from: float | Unset = UNSET,
    pvgrpp_center_east_to: float | Unset = UNSET,
    dst_flag: bool | Unset = UNSET,
    page: int | Unset = UNSET,
    size: int | Unset = UNSET,
    sort: str | Unset = UNSET,
    dir_: str | Unset = UNSET,
) -> Response[Exception_ | Report]:
    """Solar Power Production - Hourly Averaged Actual and Forecasted Values by Geographical Region

     Solar Power Production - Hourly Averaged Actual and Forecasted Values by Geographical Region

    Args:
        delivery_date_from (str | Unset):
        delivery_date_to (str | Unset):
        posted_datetime_from (str | Unset):
        posted_datetime_to (str | Unset):
        hour_ending_from (int | Unset):
        hour_ending_to (int | Unset):
        gen_system_wide_from (float | Unset):
        gen_system_wide_to (float | Unset):
        cophsl_system_wide_from (float | Unset):
        cophsl_system_wide_to (float | Unset):
        stppf_system_wide_from (float | Unset):
        stppf_system_wide_to (float | Unset):
        pvgrpp_system_wide_from (float | Unset):
        pvgrpp_system_wide_to (float | Unset):
        gen_center_west_from (float | Unset):
        gen_center_west_to (float | Unset):
        cophsl_center_west_from (float | Unset):
        cophsl_center_west_to (float | Unset):
        stppf_center_west_from (float | Unset):
        stppf_center_west_to (float | Unset):
        pvgrpp_center_west_from (float | Unset):
        pvgrpp_center_west_to (float | Unset):
        gen_north_west_from (float | Unset):
        gen_north_west_to (float | Unset):
        cophsl_north_west_from (float | Unset):
        cophsl_north_west_to (float | Unset):
        stppf_north_west_from (float | Unset):
        stppf_north_west_to (float | Unset):
        pvgrpp_north_west_from (float | Unset):
        pvgrpp_north_west_to (float | Unset):
        gen_far_west_from (float | Unset):
        gen_far_west_to (float | Unset):
        cophsl_far_west_from (float | Unset):
        cophsl_far_west_to (float | Unset):
        stppf_far_west_from (float | Unset):
        stppf_far_west_to (float | Unset):
        pvgrpp_far_west_from (float | Unset):
        pvgrpp_far_west_to (float | Unset):
        gen_far_east_from (float | Unset):
        gen_far_east_to (float | Unset):
        cophsl_far_east_from (float | Unset):
        cophsl_far_east_to (float | Unset):
        stppf_far_east_from (float | Unset):
        stppf_far_east_to (float | Unset):
        pvgrpp_far_east_from (float | Unset):
        pvgrpp_far_east_to (float | Unset):
        gen_south_east_from (float | Unset):
        gen_south_east_to (float | Unset):
        cophsl_south_east_from (float | Unset):
        cophsl_south_east_to (float | Unset):
        stppf_south_east_from (float | Unset):
        stppf_south_east_to (float | Unset):
        pvgrpp_south_east_from (float | Unset):
        pvgrpp_south_east_to (float | Unset):
        gen_center_east_from (float | Unset):
        gen_center_east_to (float | Unset):
        cophsl_center_east_from (float | Unset):
        cophsl_center_east_to (float | Unset):
        stppf_center_east_from (float | Unset):
        stppf_center_east_to (float | Unset):
        pvgrpp_center_east_from (float | Unset):
        pvgrpp_center_east_to (float | Unset):
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
        posted_datetime_from=posted_datetime_from,
        posted_datetime_to=posted_datetime_to,
        hour_ending_from=hour_ending_from,
        hour_ending_to=hour_ending_to,
        gen_system_wide_from=gen_system_wide_from,
        gen_system_wide_to=gen_system_wide_to,
        cophsl_system_wide_from=cophsl_system_wide_from,
        cophsl_system_wide_to=cophsl_system_wide_to,
        stppf_system_wide_from=stppf_system_wide_from,
        stppf_system_wide_to=stppf_system_wide_to,
        pvgrpp_system_wide_from=pvgrpp_system_wide_from,
        pvgrpp_system_wide_to=pvgrpp_system_wide_to,
        gen_center_west_from=gen_center_west_from,
        gen_center_west_to=gen_center_west_to,
        cophsl_center_west_from=cophsl_center_west_from,
        cophsl_center_west_to=cophsl_center_west_to,
        stppf_center_west_from=stppf_center_west_from,
        stppf_center_west_to=stppf_center_west_to,
        pvgrpp_center_west_from=pvgrpp_center_west_from,
        pvgrpp_center_west_to=pvgrpp_center_west_to,
        gen_north_west_from=gen_north_west_from,
        gen_north_west_to=gen_north_west_to,
        cophsl_north_west_from=cophsl_north_west_from,
        cophsl_north_west_to=cophsl_north_west_to,
        stppf_north_west_from=stppf_north_west_from,
        stppf_north_west_to=stppf_north_west_to,
        pvgrpp_north_west_from=pvgrpp_north_west_from,
        pvgrpp_north_west_to=pvgrpp_north_west_to,
        gen_far_west_from=gen_far_west_from,
        gen_far_west_to=gen_far_west_to,
        cophsl_far_west_from=cophsl_far_west_from,
        cophsl_far_west_to=cophsl_far_west_to,
        stppf_far_west_from=stppf_far_west_from,
        stppf_far_west_to=stppf_far_west_to,
        pvgrpp_far_west_from=pvgrpp_far_west_from,
        pvgrpp_far_west_to=pvgrpp_far_west_to,
        gen_far_east_from=gen_far_east_from,
        gen_far_east_to=gen_far_east_to,
        cophsl_far_east_from=cophsl_far_east_from,
        cophsl_far_east_to=cophsl_far_east_to,
        stppf_far_east_from=stppf_far_east_from,
        stppf_far_east_to=stppf_far_east_to,
        pvgrpp_far_east_from=pvgrpp_far_east_from,
        pvgrpp_far_east_to=pvgrpp_far_east_to,
        gen_south_east_from=gen_south_east_from,
        gen_south_east_to=gen_south_east_to,
        cophsl_south_east_from=cophsl_south_east_from,
        cophsl_south_east_to=cophsl_south_east_to,
        stppf_south_east_from=stppf_south_east_from,
        stppf_south_east_to=stppf_south_east_to,
        pvgrpp_south_east_from=pvgrpp_south_east_from,
        pvgrpp_south_east_to=pvgrpp_south_east_to,
        gen_center_east_from=gen_center_east_from,
        gen_center_east_to=gen_center_east_to,
        cophsl_center_east_from=cophsl_center_east_from,
        cophsl_center_east_to=cophsl_center_east_to,
        stppf_center_east_from=stppf_center_east_from,
        stppf_center_east_to=stppf_center_east_to,
        pvgrpp_center_east_from=pvgrpp_center_east_from,
        pvgrpp_center_east_to=pvgrpp_center_east_to,
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
    posted_datetime_from: str | Unset = UNSET,
    posted_datetime_to: str | Unset = UNSET,
    hour_ending_from: int | Unset = UNSET,
    hour_ending_to: int | Unset = UNSET,
    gen_system_wide_from: float | Unset = UNSET,
    gen_system_wide_to: float | Unset = UNSET,
    cophsl_system_wide_from: float | Unset = UNSET,
    cophsl_system_wide_to: float | Unset = UNSET,
    stppf_system_wide_from: float | Unset = UNSET,
    stppf_system_wide_to: float | Unset = UNSET,
    pvgrpp_system_wide_from: float | Unset = UNSET,
    pvgrpp_system_wide_to: float | Unset = UNSET,
    gen_center_west_from: float | Unset = UNSET,
    gen_center_west_to: float | Unset = UNSET,
    cophsl_center_west_from: float | Unset = UNSET,
    cophsl_center_west_to: float | Unset = UNSET,
    stppf_center_west_from: float | Unset = UNSET,
    stppf_center_west_to: float | Unset = UNSET,
    pvgrpp_center_west_from: float | Unset = UNSET,
    pvgrpp_center_west_to: float | Unset = UNSET,
    gen_north_west_from: float | Unset = UNSET,
    gen_north_west_to: float | Unset = UNSET,
    cophsl_north_west_from: float | Unset = UNSET,
    cophsl_north_west_to: float | Unset = UNSET,
    stppf_north_west_from: float | Unset = UNSET,
    stppf_north_west_to: float | Unset = UNSET,
    pvgrpp_north_west_from: float | Unset = UNSET,
    pvgrpp_north_west_to: float | Unset = UNSET,
    gen_far_west_from: float | Unset = UNSET,
    gen_far_west_to: float | Unset = UNSET,
    cophsl_far_west_from: float | Unset = UNSET,
    cophsl_far_west_to: float | Unset = UNSET,
    stppf_far_west_from: float | Unset = UNSET,
    stppf_far_west_to: float | Unset = UNSET,
    pvgrpp_far_west_from: float | Unset = UNSET,
    pvgrpp_far_west_to: float | Unset = UNSET,
    gen_far_east_from: float | Unset = UNSET,
    gen_far_east_to: float | Unset = UNSET,
    cophsl_far_east_from: float | Unset = UNSET,
    cophsl_far_east_to: float | Unset = UNSET,
    stppf_far_east_from: float | Unset = UNSET,
    stppf_far_east_to: float | Unset = UNSET,
    pvgrpp_far_east_from: float | Unset = UNSET,
    pvgrpp_far_east_to: float | Unset = UNSET,
    gen_south_east_from: float | Unset = UNSET,
    gen_south_east_to: float | Unset = UNSET,
    cophsl_south_east_from: float | Unset = UNSET,
    cophsl_south_east_to: float | Unset = UNSET,
    stppf_south_east_from: float | Unset = UNSET,
    stppf_south_east_to: float | Unset = UNSET,
    pvgrpp_south_east_from: float | Unset = UNSET,
    pvgrpp_south_east_to: float | Unset = UNSET,
    gen_center_east_from: float | Unset = UNSET,
    gen_center_east_to: float | Unset = UNSET,
    cophsl_center_east_from: float | Unset = UNSET,
    cophsl_center_east_to: float | Unset = UNSET,
    stppf_center_east_from: float | Unset = UNSET,
    stppf_center_east_to: float | Unset = UNSET,
    pvgrpp_center_east_from: float | Unset = UNSET,
    pvgrpp_center_east_to: float | Unset = UNSET,
    dst_flag: bool | Unset = UNSET,
    page: int | Unset = UNSET,
    size: int | Unset = UNSET,
    sort: str | Unset = UNSET,
    dir_: str | Unset = UNSET,
) -> Exception_ | Report | None:
    """Solar Power Production - Hourly Averaged Actual and Forecasted Values by Geographical Region

     Solar Power Production - Hourly Averaged Actual and Forecasted Values by Geographical Region

    Args:
        delivery_date_from (str | Unset):
        delivery_date_to (str | Unset):
        posted_datetime_from (str | Unset):
        posted_datetime_to (str | Unset):
        hour_ending_from (int | Unset):
        hour_ending_to (int | Unset):
        gen_system_wide_from (float | Unset):
        gen_system_wide_to (float | Unset):
        cophsl_system_wide_from (float | Unset):
        cophsl_system_wide_to (float | Unset):
        stppf_system_wide_from (float | Unset):
        stppf_system_wide_to (float | Unset):
        pvgrpp_system_wide_from (float | Unset):
        pvgrpp_system_wide_to (float | Unset):
        gen_center_west_from (float | Unset):
        gen_center_west_to (float | Unset):
        cophsl_center_west_from (float | Unset):
        cophsl_center_west_to (float | Unset):
        stppf_center_west_from (float | Unset):
        stppf_center_west_to (float | Unset):
        pvgrpp_center_west_from (float | Unset):
        pvgrpp_center_west_to (float | Unset):
        gen_north_west_from (float | Unset):
        gen_north_west_to (float | Unset):
        cophsl_north_west_from (float | Unset):
        cophsl_north_west_to (float | Unset):
        stppf_north_west_from (float | Unset):
        stppf_north_west_to (float | Unset):
        pvgrpp_north_west_from (float | Unset):
        pvgrpp_north_west_to (float | Unset):
        gen_far_west_from (float | Unset):
        gen_far_west_to (float | Unset):
        cophsl_far_west_from (float | Unset):
        cophsl_far_west_to (float | Unset):
        stppf_far_west_from (float | Unset):
        stppf_far_west_to (float | Unset):
        pvgrpp_far_west_from (float | Unset):
        pvgrpp_far_west_to (float | Unset):
        gen_far_east_from (float | Unset):
        gen_far_east_to (float | Unset):
        cophsl_far_east_from (float | Unset):
        cophsl_far_east_to (float | Unset):
        stppf_far_east_from (float | Unset):
        stppf_far_east_to (float | Unset):
        pvgrpp_far_east_from (float | Unset):
        pvgrpp_far_east_to (float | Unset):
        gen_south_east_from (float | Unset):
        gen_south_east_to (float | Unset):
        cophsl_south_east_from (float | Unset):
        cophsl_south_east_to (float | Unset):
        stppf_south_east_from (float | Unset):
        stppf_south_east_to (float | Unset):
        pvgrpp_south_east_from (float | Unset):
        pvgrpp_south_east_to (float | Unset):
        gen_center_east_from (float | Unset):
        gen_center_east_to (float | Unset):
        cophsl_center_east_from (float | Unset):
        cophsl_center_east_to (float | Unset):
        stppf_center_east_from (float | Unset):
        stppf_center_east_to (float | Unset):
        pvgrpp_center_east_from (float | Unset):
        pvgrpp_center_east_to (float | Unset):
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
            posted_datetime_from=posted_datetime_from,
            posted_datetime_to=posted_datetime_to,
            hour_ending_from=hour_ending_from,
            hour_ending_to=hour_ending_to,
            gen_system_wide_from=gen_system_wide_from,
            gen_system_wide_to=gen_system_wide_to,
            cophsl_system_wide_from=cophsl_system_wide_from,
            cophsl_system_wide_to=cophsl_system_wide_to,
            stppf_system_wide_from=stppf_system_wide_from,
            stppf_system_wide_to=stppf_system_wide_to,
            pvgrpp_system_wide_from=pvgrpp_system_wide_from,
            pvgrpp_system_wide_to=pvgrpp_system_wide_to,
            gen_center_west_from=gen_center_west_from,
            gen_center_west_to=gen_center_west_to,
            cophsl_center_west_from=cophsl_center_west_from,
            cophsl_center_west_to=cophsl_center_west_to,
            stppf_center_west_from=stppf_center_west_from,
            stppf_center_west_to=stppf_center_west_to,
            pvgrpp_center_west_from=pvgrpp_center_west_from,
            pvgrpp_center_west_to=pvgrpp_center_west_to,
            gen_north_west_from=gen_north_west_from,
            gen_north_west_to=gen_north_west_to,
            cophsl_north_west_from=cophsl_north_west_from,
            cophsl_north_west_to=cophsl_north_west_to,
            stppf_north_west_from=stppf_north_west_from,
            stppf_north_west_to=stppf_north_west_to,
            pvgrpp_north_west_from=pvgrpp_north_west_from,
            pvgrpp_north_west_to=pvgrpp_north_west_to,
            gen_far_west_from=gen_far_west_from,
            gen_far_west_to=gen_far_west_to,
            cophsl_far_west_from=cophsl_far_west_from,
            cophsl_far_west_to=cophsl_far_west_to,
            stppf_far_west_from=stppf_far_west_from,
            stppf_far_west_to=stppf_far_west_to,
            pvgrpp_far_west_from=pvgrpp_far_west_from,
            pvgrpp_far_west_to=pvgrpp_far_west_to,
            gen_far_east_from=gen_far_east_from,
            gen_far_east_to=gen_far_east_to,
            cophsl_far_east_from=cophsl_far_east_from,
            cophsl_far_east_to=cophsl_far_east_to,
            stppf_far_east_from=stppf_far_east_from,
            stppf_far_east_to=stppf_far_east_to,
            pvgrpp_far_east_from=pvgrpp_far_east_from,
            pvgrpp_far_east_to=pvgrpp_far_east_to,
            gen_south_east_from=gen_south_east_from,
            gen_south_east_to=gen_south_east_to,
            cophsl_south_east_from=cophsl_south_east_from,
            cophsl_south_east_to=cophsl_south_east_to,
            stppf_south_east_from=stppf_south_east_from,
            stppf_south_east_to=stppf_south_east_to,
            pvgrpp_south_east_from=pvgrpp_south_east_from,
            pvgrpp_south_east_to=pvgrpp_south_east_to,
            gen_center_east_from=gen_center_east_from,
            gen_center_east_to=gen_center_east_to,
            cophsl_center_east_from=cophsl_center_east_from,
            cophsl_center_east_to=cophsl_center_east_to,
            stppf_center_east_from=stppf_center_east_from,
            stppf_center_east_to=stppf_center_east_to,
            pvgrpp_center_east_from=pvgrpp_center_east_from,
            pvgrpp_center_east_to=pvgrpp_center_east_to,
            dst_flag=dst_flag,
            page=page,
            size=size,
            sort=sort,
            dir_=dir_,
        )
    ).parsed
