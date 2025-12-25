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
    stppf_system_wide_from: float | Unset = UNSET,
    stppf_system_wide_to: float | Unset = UNSET,
    pvgrpp_system_wide_from: float | Unset = UNSET,
    pvgrpp_system_wide_to: float | Unset = UNSET,
    dst_flag: bool | Unset = UNSET,
    delivery_date_from: str | Unset = UNSET,
    delivery_date_to: str | Unset = UNSET,
    hour_ending_from: int | Unset = UNSET,
    hour_ending_to: int | Unset = UNSET,
    actual_system_wide_from: float | Unset = UNSET,
    actual_system_wide_to: float | Unset = UNSET,
    cophsl_system_wide_from: float | Unset = UNSET,
    cophsl_system_wide_to: float | Unset = UNSET,
    posted_datetime_from: str | Unset = UNSET,
    posted_datetime_to: str | Unset = UNSET,
    page: int | Unset = UNSET,
    size: int | Unset = UNSET,
    sort: str | Unset = UNSET,
    dir_: str | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["STPPFSystemWideFrom"] = stppf_system_wide_from

    params["STPPFSystemWideTo"] = stppf_system_wide_to

    params["PVGRPPSystemWideFrom"] = pvgrpp_system_wide_from

    params["PVGRPPSystemWideTo"] = pvgrpp_system_wide_to

    params["DSTFlag"] = dst_flag

    params["deliveryDateFrom"] = delivery_date_from

    params["deliveryDateTo"] = delivery_date_to

    params["hourEndingFrom"] = hour_ending_from

    params["hourEndingTo"] = hour_ending_to

    params["actualSystemWideFrom"] = actual_system_wide_from

    params["actualSystemWideTo"] = actual_system_wide_to

    params["COPHSLSystemWideFrom"] = cophsl_system_wide_from

    params["COPHSLSystemWideTo"] = cophsl_system_wide_to

    params["postedDatetimeFrom"] = posted_datetime_from

    params["postedDatetimeTo"] = posted_datetime_to

    params["page"] = page

    params["size"] = size

    params["sort"] = sort

    params["dir"] = dir_

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/np4-737-cd/spp_hrly_avrg_actl_fcast",
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
    stppf_system_wide_from: float | Unset = UNSET,
    stppf_system_wide_to: float | Unset = UNSET,
    pvgrpp_system_wide_from: float | Unset = UNSET,
    pvgrpp_system_wide_to: float | Unset = UNSET,
    dst_flag: bool | Unset = UNSET,
    delivery_date_from: str | Unset = UNSET,
    delivery_date_to: str | Unset = UNSET,
    hour_ending_from: int | Unset = UNSET,
    hour_ending_to: int | Unset = UNSET,
    actual_system_wide_from: float | Unset = UNSET,
    actual_system_wide_to: float | Unset = UNSET,
    cophsl_system_wide_from: float | Unset = UNSET,
    cophsl_system_wide_to: float | Unset = UNSET,
    posted_datetime_from: str | Unset = UNSET,
    posted_datetime_to: str | Unset = UNSET,
    page: int | Unset = UNSET,
    size: int | Unset = UNSET,
    sort: str | Unset = UNSET,
    dir_: str | Unset = UNSET,
) -> Response[Exception_ | Report]:
    """Solar Power Production - Hourly Averaged Actual and Forecasted Values

     Solar Power Production - Hourly Averaged Actual and Forecasted Values

    Args:
        stppf_system_wide_from (float | Unset):
        stppf_system_wide_to (float | Unset):
        pvgrpp_system_wide_from (float | Unset):
        pvgrpp_system_wide_to (float | Unset):
        dst_flag (bool | Unset):
        delivery_date_from (str | Unset):
        delivery_date_to (str | Unset):
        hour_ending_from (int | Unset):
        hour_ending_to (int | Unset):
        actual_system_wide_from (float | Unset):
        actual_system_wide_to (float | Unset):
        cophsl_system_wide_from (float | Unset):
        cophsl_system_wide_to (float | Unset):
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
        stppf_system_wide_from=stppf_system_wide_from,
        stppf_system_wide_to=stppf_system_wide_to,
        pvgrpp_system_wide_from=pvgrpp_system_wide_from,
        pvgrpp_system_wide_to=pvgrpp_system_wide_to,
        dst_flag=dst_flag,
        delivery_date_from=delivery_date_from,
        delivery_date_to=delivery_date_to,
        hour_ending_from=hour_ending_from,
        hour_ending_to=hour_ending_to,
        actual_system_wide_from=actual_system_wide_from,
        actual_system_wide_to=actual_system_wide_to,
        cophsl_system_wide_from=cophsl_system_wide_from,
        cophsl_system_wide_to=cophsl_system_wide_to,
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
    stppf_system_wide_from: float | Unset = UNSET,
    stppf_system_wide_to: float | Unset = UNSET,
    pvgrpp_system_wide_from: float | Unset = UNSET,
    pvgrpp_system_wide_to: float | Unset = UNSET,
    dst_flag: bool | Unset = UNSET,
    delivery_date_from: str | Unset = UNSET,
    delivery_date_to: str | Unset = UNSET,
    hour_ending_from: int | Unset = UNSET,
    hour_ending_to: int | Unset = UNSET,
    actual_system_wide_from: float | Unset = UNSET,
    actual_system_wide_to: float | Unset = UNSET,
    cophsl_system_wide_from: float | Unset = UNSET,
    cophsl_system_wide_to: float | Unset = UNSET,
    posted_datetime_from: str | Unset = UNSET,
    posted_datetime_to: str | Unset = UNSET,
    page: int | Unset = UNSET,
    size: int | Unset = UNSET,
    sort: str | Unset = UNSET,
    dir_: str | Unset = UNSET,
) -> Exception_ | Report | None:
    """Solar Power Production - Hourly Averaged Actual and Forecasted Values

     Solar Power Production - Hourly Averaged Actual and Forecasted Values

    Args:
        stppf_system_wide_from (float | Unset):
        stppf_system_wide_to (float | Unset):
        pvgrpp_system_wide_from (float | Unset):
        pvgrpp_system_wide_to (float | Unset):
        dst_flag (bool | Unset):
        delivery_date_from (str | Unset):
        delivery_date_to (str | Unset):
        hour_ending_from (int | Unset):
        hour_ending_to (int | Unset):
        actual_system_wide_from (float | Unset):
        actual_system_wide_to (float | Unset):
        cophsl_system_wide_from (float | Unset):
        cophsl_system_wide_to (float | Unset):
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
        stppf_system_wide_from=stppf_system_wide_from,
        stppf_system_wide_to=stppf_system_wide_to,
        pvgrpp_system_wide_from=pvgrpp_system_wide_from,
        pvgrpp_system_wide_to=pvgrpp_system_wide_to,
        dst_flag=dst_flag,
        delivery_date_from=delivery_date_from,
        delivery_date_to=delivery_date_to,
        hour_ending_from=hour_ending_from,
        hour_ending_to=hour_ending_to,
        actual_system_wide_from=actual_system_wide_from,
        actual_system_wide_to=actual_system_wide_to,
        cophsl_system_wide_from=cophsl_system_wide_from,
        cophsl_system_wide_to=cophsl_system_wide_to,
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
    stppf_system_wide_from: float | Unset = UNSET,
    stppf_system_wide_to: float | Unset = UNSET,
    pvgrpp_system_wide_from: float | Unset = UNSET,
    pvgrpp_system_wide_to: float | Unset = UNSET,
    dst_flag: bool | Unset = UNSET,
    delivery_date_from: str | Unset = UNSET,
    delivery_date_to: str | Unset = UNSET,
    hour_ending_from: int | Unset = UNSET,
    hour_ending_to: int | Unset = UNSET,
    actual_system_wide_from: float | Unset = UNSET,
    actual_system_wide_to: float | Unset = UNSET,
    cophsl_system_wide_from: float | Unset = UNSET,
    cophsl_system_wide_to: float | Unset = UNSET,
    posted_datetime_from: str | Unset = UNSET,
    posted_datetime_to: str | Unset = UNSET,
    page: int | Unset = UNSET,
    size: int | Unset = UNSET,
    sort: str | Unset = UNSET,
    dir_: str | Unset = UNSET,
) -> Response[Exception_ | Report]:
    """Solar Power Production - Hourly Averaged Actual and Forecasted Values

     Solar Power Production - Hourly Averaged Actual and Forecasted Values

    Args:
        stppf_system_wide_from (float | Unset):
        stppf_system_wide_to (float | Unset):
        pvgrpp_system_wide_from (float | Unset):
        pvgrpp_system_wide_to (float | Unset):
        dst_flag (bool | Unset):
        delivery_date_from (str | Unset):
        delivery_date_to (str | Unset):
        hour_ending_from (int | Unset):
        hour_ending_to (int | Unset):
        actual_system_wide_from (float | Unset):
        actual_system_wide_to (float | Unset):
        cophsl_system_wide_from (float | Unset):
        cophsl_system_wide_to (float | Unset):
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
        stppf_system_wide_from=stppf_system_wide_from,
        stppf_system_wide_to=stppf_system_wide_to,
        pvgrpp_system_wide_from=pvgrpp_system_wide_from,
        pvgrpp_system_wide_to=pvgrpp_system_wide_to,
        dst_flag=dst_flag,
        delivery_date_from=delivery_date_from,
        delivery_date_to=delivery_date_to,
        hour_ending_from=hour_ending_from,
        hour_ending_to=hour_ending_to,
        actual_system_wide_from=actual_system_wide_from,
        actual_system_wide_to=actual_system_wide_to,
        cophsl_system_wide_from=cophsl_system_wide_from,
        cophsl_system_wide_to=cophsl_system_wide_to,
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
    stppf_system_wide_from: float | Unset = UNSET,
    stppf_system_wide_to: float | Unset = UNSET,
    pvgrpp_system_wide_from: float | Unset = UNSET,
    pvgrpp_system_wide_to: float | Unset = UNSET,
    dst_flag: bool | Unset = UNSET,
    delivery_date_from: str | Unset = UNSET,
    delivery_date_to: str | Unset = UNSET,
    hour_ending_from: int | Unset = UNSET,
    hour_ending_to: int | Unset = UNSET,
    actual_system_wide_from: float | Unset = UNSET,
    actual_system_wide_to: float | Unset = UNSET,
    cophsl_system_wide_from: float | Unset = UNSET,
    cophsl_system_wide_to: float | Unset = UNSET,
    posted_datetime_from: str | Unset = UNSET,
    posted_datetime_to: str | Unset = UNSET,
    page: int | Unset = UNSET,
    size: int | Unset = UNSET,
    sort: str | Unset = UNSET,
    dir_: str | Unset = UNSET,
) -> Exception_ | Report | None:
    """Solar Power Production - Hourly Averaged Actual and Forecasted Values

     Solar Power Production - Hourly Averaged Actual and Forecasted Values

    Args:
        stppf_system_wide_from (float | Unset):
        stppf_system_wide_to (float | Unset):
        pvgrpp_system_wide_from (float | Unset):
        pvgrpp_system_wide_to (float | Unset):
        dst_flag (bool | Unset):
        delivery_date_from (str | Unset):
        delivery_date_to (str | Unset):
        hour_ending_from (int | Unset):
        hour_ending_to (int | Unset):
        actual_system_wide_from (float | Unset):
        actual_system_wide_to (float | Unset):
        cophsl_system_wide_from (float | Unset):
        cophsl_system_wide_to (float | Unset):
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
            stppf_system_wide_from=stppf_system_wide_from,
            stppf_system_wide_to=stppf_system_wide_to,
            pvgrpp_system_wide_from=pvgrpp_system_wide_from,
            pvgrpp_system_wide_to=pvgrpp_system_wide_to,
            dst_flag=dst_flag,
            delivery_date_from=delivery_date_from,
            delivery_date_to=delivery_date_to,
            hour_ending_from=hour_ending_from,
            hour_ending_to=hour_ending_to,
            actual_system_wide_from=actual_system_wide_from,
            actual_system_wide_to=actual_system_wide_to,
            cophsl_system_wide_from=cophsl_system_wide_from,
            cophsl_system_wide_to=cophsl_system_wide_to,
            posted_datetime_from=posted_datetime_from,
            posted_datetime_to=posted_datetime_to,
            page=page,
            size=size,
            sort=sort,
            dir_=dir_,
        )
    ).parsed
