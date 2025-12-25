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
    interval_ending_from: str | Unset = UNSET,
    interval_ending_to: str | Unset = UNSET,
    posted_datetime_from: str | Unset = UNSET,
    posted_datetime_to: str | Unset = UNSET,
    gen_system_wide_from: float | Unset = UNSET,
    gen_system_wide_to: float | Unset = UNSET,
    gen_center_west_from: float | Unset = UNSET,
    gen_center_west_to: float | Unset = UNSET,
    gen_north_west_from: float | Unset = UNSET,
    gen_north_west_to: float | Unset = UNSET,
    gen_far_west_from: float | Unset = UNSET,
    gen_far_west_to: float | Unset = UNSET,
    gen_far_east_from: float | Unset = UNSET,
    gen_far_east_to: float | Unset = UNSET,
    gen_south_east_from: float | Unset = UNSET,
    gen_south_east_to: float | Unset = UNSET,
    gen_center_east_from: float | Unset = UNSET,
    gen_center_east_to: float | Unset = UNSET,
    dst_flag: bool | Unset = UNSET,
    page: int | Unset = UNSET,
    size: int | Unset = UNSET,
    sort: str | Unset = UNSET,
    dir_: str | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["intervalEndingFrom"] = interval_ending_from

    params["intervalEndingTo"] = interval_ending_to

    params["postedDatetimeFrom"] = posted_datetime_from

    params["postedDatetimeTo"] = posted_datetime_to

    params["genSystemWideFrom"] = gen_system_wide_from

    params["genSystemWideTo"] = gen_system_wide_to

    params["genCenterWestFrom"] = gen_center_west_from

    params["genCenterWestTo"] = gen_center_west_to

    params["genNorthWestFrom"] = gen_north_west_from

    params["genNorthWestTo"] = gen_north_west_to

    params["genFarWestFrom"] = gen_far_west_from

    params["genFarWestTo"] = gen_far_west_to

    params["genFarEastFrom"] = gen_far_east_from

    params["genFarEastTo"] = gen_far_east_to

    params["genSouthEastFrom"] = gen_south_east_from

    params["genSouthEastTo"] = gen_south_east_to

    params["genCenterEastFrom"] = gen_center_east_from

    params["genCenterEastTo"] = gen_center_east_to

    params["DSTFlag"] = dst_flag

    params["page"] = page

    params["size"] = size

    params["sort"] = sort

    params["dir"] = dir_

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/np4-746-cd/spp_actual_5min_avg_values_geo",
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
    interval_ending_from: str | Unset = UNSET,
    interval_ending_to: str | Unset = UNSET,
    posted_datetime_from: str | Unset = UNSET,
    posted_datetime_to: str | Unset = UNSET,
    gen_system_wide_from: float | Unset = UNSET,
    gen_system_wide_to: float | Unset = UNSET,
    gen_center_west_from: float | Unset = UNSET,
    gen_center_west_to: float | Unset = UNSET,
    gen_north_west_from: float | Unset = UNSET,
    gen_north_west_to: float | Unset = UNSET,
    gen_far_west_from: float | Unset = UNSET,
    gen_far_west_to: float | Unset = UNSET,
    gen_far_east_from: float | Unset = UNSET,
    gen_far_east_to: float | Unset = UNSET,
    gen_south_east_from: float | Unset = UNSET,
    gen_south_east_to: float | Unset = UNSET,
    gen_center_east_from: float | Unset = UNSET,
    gen_center_east_to: float | Unset = UNSET,
    dst_flag: bool | Unset = UNSET,
    page: int | Unset = UNSET,
    size: int | Unset = UNSET,
    sort: str | Unset = UNSET,
    dir_: str | Unset = UNSET,
) -> Response[Exception_ | Report]:
    """Solar Power Production - Actual 5-Minute Averaged Values by Geographical Region

     Solar Power Production - Actual 5-Minute Averaged Values by Geographical Region

    Args:
        interval_ending_from (str | Unset):
        interval_ending_to (str | Unset):
        posted_datetime_from (str | Unset):
        posted_datetime_to (str | Unset):
        gen_system_wide_from (float | Unset):
        gen_system_wide_to (float | Unset):
        gen_center_west_from (float | Unset):
        gen_center_west_to (float | Unset):
        gen_north_west_from (float | Unset):
        gen_north_west_to (float | Unset):
        gen_far_west_from (float | Unset):
        gen_far_west_to (float | Unset):
        gen_far_east_from (float | Unset):
        gen_far_east_to (float | Unset):
        gen_south_east_from (float | Unset):
        gen_south_east_to (float | Unset):
        gen_center_east_from (float | Unset):
        gen_center_east_to (float | Unset):
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
        interval_ending_from=interval_ending_from,
        interval_ending_to=interval_ending_to,
        posted_datetime_from=posted_datetime_from,
        posted_datetime_to=posted_datetime_to,
        gen_system_wide_from=gen_system_wide_from,
        gen_system_wide_to=gen_system_wide_to,
        gen_center_west_from=gen_center_west_from,
        gen_center_west_to=gen_center_west_to,
        gen_north_west_from=gen_north_west_from,
        gen_north_west_to=gen_north_west_to,
        gen_far_west_from=gen_far_west_from,
        gen_far_west_to=gen_far_west_to,
        gen_far_east_from=gen_far_east_from,
        gen_far_east_to=gen_far_east_to,
        gen_south_east_from=gen_south_east_from,
        gen_south_east_to=gen_south_east_to,
        gen_center_east_from=gen_center_east_from,
        gen_center_east_to=gen_center_east_to,
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
    interval_ending_from: str | Unset = UNSET,
    interval_ending_to: str | Unset = UNSET,
    posted_datetime_from: str | Unset = UNSET,
    posted_datetime_to: str | Unset = UNSET,
    gen_system_wide_from: float | Unset = UNSET,
    gen_system_wide_to: float | Unset = UNSET,
    gen_center_west_from: float | Unset = UNSET,
    gen_center_west_to: float | Unset = UNSET,
    gen_north_west_from: float | Unset = UNSET,
    gen_north_west_to: float | Unset = UNSET,
    gen_far_west_from: float | Unset = UNSET,
    gen_far_west_to: float | Unset = UNSET,
    gen_far_east_from: float | Unset = UNSET,
    gen_far_east_to: float | Unset = UNSET,
    gen_south_east_from: float | Unset = UNSET,
    gen_south_east_to: float | Unset = UNSET,
    gen_center_east_from: float | Unset = UNSET,
    gen_center_east_to: float | Unset = UNSET,
    dst_flag: bool | Unset = UNSET,
    page: int | Unset = UNSET,
    size: int | Unset = UNSET,
    sort: str | Unset = UNSET,
    dir_: str | Unset = UNSET,
) -> Exception_ | Report | None:
    """Solar Power Production - Actual 5-Minute Averaged Values by Geographical Region

     Solar Power Production - Actual 5-Minute Averaged Values by Geographical Region

    Args:
        interval_ending_from (str | Unset):
        interval_ending_to (str | Unset):
        posted_datetime_from (str | Unset):
        posted_datetime_to (str | Unset):
        gen_system_wide_from (float | Unset):
        gen_system_wide_to (float | Unset):
        gen_center_west_from (float | Unset):
        gen_center_west_to (float | Unset):
        gen_north_west_from (float | Unset):
        gen_north_west_to (float | Unset):
        gen_far_west_from (float | Unset):
        gen_far_west_to (float | Unset):
        gen_far_east_from (float | Unset):
        gen_far_east_to (float | Unset):
        gen_south_east_from (float | Unset):
        gen_south_east_to (float | Unset):
        gen_center_east_from (float | Unset):
        gen_center_east_to (float | Unset):
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
        interval_ending_from=interval_ending_from,
        interval_ending_to=interval_ending_to,
        posted_datetime_from=posted_datetime_from,
        posted_datetime_to=posted_datetime_to,
        gen_system_wide_from=gen_system_wide_from,
        gen_system_wide_to=gen_system_wide_to,
        gen_center_west_from=gen_center_west_from,
        gen_center_west_to=gen_center_west_to,
        gen_north_west_from=gen_north_west_from,
        gen_north_west_to=gen_north_west_to,
        gen_far_west_from=gen_far_west_from,
        gen_far_west_to=gen_far_west_to,
        gen_far_east_from=gen_far_east_from,
        gen_far_east_to=gen_far_east_to,
        gen_south_east_from=gen_south_east_from,
        gen_south_east_to=gen_south_east_to,
        gen_center_east_from=gen_center_east_from,
        gen_center_east_to=gen_center_east_to,
        dst_flag=dst_flag,
        page=page,
        size=size,
        sort=sort,
        dir_=dir_,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    interval_ending_from: str | Unset = UNSET,
    interval_ending_to: str | Unset = UNSET,
    posted_datetime_from: str | Unset = UNSET,
    posted_datetime_to: str | Unset = UNSET,
    gen_system_wide_from: float | Unset = UNSET,
    gen_system_wide_to: float | Unset = UNSET,
    gen_center_west_from: float | Unset = UNSET,
    gen_center_west_to: float | Unset = UNSET,
    gen_north_west_from: float | Unset = UNSET,
    gen_north_west_to: float | Unset = UNSET,
    gen_far_west_from: float | Unset = UNSET,
    gen_far_west_to: float | Unset = UNSET,
    gen_far_east_from: float | Unset = UNSET,
    gen_far_east_to: float | Unset = UNSET,
    gen_south_east_from: float | Unset = UNSET,
    gen_south_east_to: float | Unset = UNSET,
    gen_center_east_from: float | Unset = UNSET,
    gen_center_east_to: float | Unset = UNSET,
    dst_flag: bool | Unset = UNSET,
    page: int | Unset = UNSET,
    size: int | Unset = UNSET,
    sort: str | Unset = UNSET,
    dir_: str | Unset = UNSET,
) -> Response[Exception_ | Report]:
    """Solar Power Production - Actual 5-Minute Averaged Values by Geographical Region

     Solar Power Production - Actual 5-Minute Averaged Values by Geographical Region

    Args:
        interval_ending_from (str | Unset):
        interval_ending_to (str | Unset):
        posted_datetime_from (str | Unset):
        posted_datetime_to (str | Unset):
        gen_system_wide_from (float | Unset):
        gen_system_wide_to (float | Unset):
        gen_center_west_from (float | Unset):
        gen_center_west_to (float | Unset):
        gen_north_west_from (float | Unset):
        gen_north_west_to (float | Unset):
        gen_far_west_from (float | Unset):
        gen_far_west_to (float | Unset):
        gen_far_east_from (float | Unset):
        gen_far_east_to (float | Unset):
        gen_south_east_from (float | Unset):
        gen_south_east_to (float | Unset):
        gen_center_east_from (float | Unset):
        gen_center_east_to (float | Unset):
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
        interval_ending_from=interval_ending_from,
        interval_ending_to=interval_ending_to,
        posted_datetime_from=posted_datetime_from,
        posted_datetime_to=posted_datetime_to,
        gen_system_wide_from=gen_system_wide_from,
        gen_system_wide_to=gen_system_wide_to,
        gen_center_west_from=gen_center_west_from,
        gen_center_west_to=gen_center_west_to,
        gen_north_west_from=gen_north_west_from,
        gen_north_west_to=gen_north_west_to,
        gen_far_west_from=gen_far_west_from,
        gen_far_west_to=gen_far_west_to,
        gen_far_east_from=gen_far_east_from,
        gen_far_east_to=gen_far_east_to,
        gen_south_east_from=gen_south_east_from,
        gen_south_east_to=gen_south_east_to,
        gen_center_east_from=gen_center_east_from,
        gen_center_east_to=gen_center_east_to,
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
    interval_ending_from: str | Unset = UNSET,
    interval_ending_to: str | Unset = UNSET,
    posted_datetime_from: str | Unset = UNSET,
    posted_datetime_to: str | Unset = UNSET,
    gen_system_wide_from: float | Unset = UNSET,
    gen_system_wide_to: float | Unset = UNSET,
    gen_center_west_from: float | Unset = UNSET,
    gen_center_west_to: float | Unset = UNSET,
    gen_north_west_from: float | Unset = UNSET,
    gen_north_west_to: float | Unset = UNSET,
    gen_far_west_from: float | Unset = UNSET,
    gen_far_west_to: float | Unset = UNSET,
    gen_far_east_from: float | Unset = UNSET,
    gen_far_east_to: float | Unset = UNSET,
    gen_south_east_from: float | Unset = UNSET,
    gen_south_east_to: float | Unset = UNSET,
    gen_center_east_from: float | Unset = UNSET,
    gen_center_east_to: float | Unset = UNSET,
    dst_flag: bool | Unset = UNSET,
    page: int | Unset = UNSET,
    size: int | Unset = UNSET,
    sort: str | Unset = UNSET,
    dir_: str | Unset = UNSET,
) -> Exception_ | Report | None:
    """Solar Power Production - Actual 5-Minute Averaged Values by Geographical Region

     Solar Power Production - Actual 5-Minute Averaged Values by Geographical Region

    Args:
        interval_ending_from (str | Unset):
        interval_ending_to (str | Unset):
        posted_datetime_from (str | Unset):
        posted_datetime_to (str | Unset):
        gen_system_wide_from (float | Unset):
        gen_system_wide_to (float | Unset):
        gen_center_west_from (float | Unset):
        gen_center_west_to (float | Unset):
        gen_north_west_from (float | Unset):
        gen_north_west_to (float | Unset):
        gen_far_west_from (float | Unset):
        gen_far_west_to (float | Unset):
        gen_far_east_from (float | Unset):
        gen_far_east_to (float | Unset):
        gen_south_east_from (float | Unset):
        gen_south_east_to (float | Unset):
        gen_center_east_from (float | Unset):
        gen_center_east_to (float | Unset):
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
            interval_ending_from=interval_ending_from,
            interval_ending_to=interval_ending_to,
            posted_datetime_from=posted_datetime_from,
            posted_datetime_to=posted_datetime_to,
            gen_system_wide_from=gen_system_wide_from,
            gen_system_wide_to=gen_system_wide_to,
            gen_center_west_from=gen_center_west_from,
            gen_center_west_to=gen_center_west_to,
            gen_north_west_from=gen_north_west_from,
            gen_north_west_to=gen_north_west_to,
            gen_far_west_from=gen_far_west_from,
            gen_far_west_to=gen_far_west_to,
            gen_far_east_from=gen_far_east_from,
            gen_far_east_to=gen_far_east_to,
            gen_south_east_from=gen_south_east_from,
            gen_south_east_to=gen_south_east_to,
            gen_center_east_from=gen_center_east_from,
            gen_center_east_to=gen_center_east_to,
            dst_flag=dst_flag,
            page=page,
            size=size,
            sort=sort,
            dir_=dir_,
        )
    ).parsed
