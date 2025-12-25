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
    system_wide_from: float | Unset = UNSET,
    system_wide_to: float | Unset = UNSET,
    panhandle_from: float | Unset = UNSET,
    panhandle_to: float | Unset = UNSET,
    coast_from: float | Unset = UNSET,
    coast_to: float | Unset = UNSET,
    south_from: float | Unset = UNSET,
    south_to: float | Unset = UNSET,
    west_from: float | Unset = UNSET,
    west_to: float | Unset = UNSET,
    north_from: float | Unset = UNSET,
    north_to: float | Unset = UNSET,
    dst_flag: bool | Unset = UNSET,
    posted_datetime_from: str | Unset = UNSET,
    posted_datetime_to: str | Unset = UNSET,
    page: int | Unset = UNSET,
    size: int | Unset = UNSET,
    sort: str | Unset = UNSET,
    dir_: str | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["intervalEndingFrom"] = interval_ending_from

    params["intervalEndingTo"] = interval_ending_to

    params["systemWideFrom"] = system_wide_from

    params["systemWideTo"] = system_wide_to

    params["panhandleFrom"] = panhandle_from

    params["panhandleTo"] = panhandle_to

    params["coastFrom"] = coast_from

    params["coastTo"] = coast_to

    params["southFrom"] = south_from

    params["southTo"] = south_to

    params["westFrom"] = west_from

    params["westTo"] = west_to

    params["northFrom"] = north_from

    params["northTo"] = north_to

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
        "url": "/np4-743-cd/wpp_actual_5min_avg_values_geo",
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
    system_wide_from: float | Unset = UNSET,
    system_wide_to: float | Unset = UNSET,
    panhandle_from: float | Unset = UNSET,
    panhandle_to: float | Unset = UNSET,
    coast_from: float | Unset = UNSET,
    coast_to: float | Unset = UNSET,
    south_from: float | Unset = UNSET,
    south_to: float | Unset = UNSET,
    west_from: float | Unset = UNSET,
    west_to: float | Unset = UNSET,
    north_from: float | Unset = UNSET,
    north_to: float | Unset = UNSET,
    dst_flag: bool | Unset = UNSET,
    posted_datetime_from: str | Unset = UNSET,
    posted_datetime_to: str | Unset = UNSET,
    page: int | Unset = UNSET,
    size: int | Unset = UNSET,
    sort: str | Unset = UNSET,
    dir_: str | Unset = UNSET,
) -> Response[Exception_ | Report]:
    """Wind Power Production - Actual 5-Minute Averaged Values by Geographical Region

     Wind Power Production - Actual 5-Minute Averaged Values by Geographical Region

    Args:
        interval_ending_from (str | Unset):
        interval_ending_to (str | Unset):
        system_wide_from (float | Unset):
        system_wide_to (float | Unset):
        panhandle_from (float | Unset):
        panhandle_to (float | Unset):
        coast_from (float | Unset):
        coast_to (float | Unset):
        south_from (float | Unset):
        south_to (float | Unset):
        west_from (float | Unset):
        west_to (float | Unset):
        north_from (float | Unset):
        north_to (float | Unset):
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
        interval_ending_from=interval_ending_from,
        interval_ending_to=interval_ending_to,
        system_wide_from=system_wide_from,
        system_wide_to=system_wide_to,
        panhandle_from=panhandle_from,
        panhandle_to=panhandle_to,
        coast_from=coast_from,
        coast_to=coast_to,
        south_from=south_from,
        south_to=south_to,
        west_from=west_from,
        west_to=west_to,
        north_from=north_from,
        north_to=north_to,
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
    interval_ending_from: str | Unset = UNSET,
    interval_ending_to: str | Unset = UNSET,
    system_wide_from: float | Unset = UNSET,
    system_wide_to: float | Unset = UNSET,
    panhandle_from: float | Unset = UNSET,
    panhandle_to: float | Unset = UNSET,
    coast_from: float | Unset = UNSET,
    coast_to: float | Unset = UNSET,
    south_from: float | Unset = UNSET,
    south_to: float | Unset = UNSET,
    west_from: float | Unset = UNSET,
    west_to: float | Unset = UNSET,
    north_from: float | Unset = UNSET,
    north_to: float | Unset = UNSET,
    dst_flag: bool | Unset = UNSET,
    posted_datetime_from: str | Unset = UNSET,
    posted_datetime_to: str | Unset = UNSET,
    page: int | Unset = UNSET,
    size: int | Unset = UNSET,
    sort: str | Unset = UNSET,
    dir_: str | Unset = UNSET,
) -> Exception_ | Report | None:
    """Wind Power Production - Actual 5-Minute Averaged Values by Geographical Region

     Wind Power Production - Actual 5-Minute Averaged Values by Geographical Region

    Args:
        interval_ending_from (str | Unset):
        interval_ending_to (str | Unset):
        system_wide_from (float | Unset):
        system_wide_to (float | Unset):
        panhandle_from (float | Unset):
        panhandle_to (float | Unset):
        coast_from (float | Unset):
        coast_to (float | Unset):
        south_from (float | Unset):
        south_to (float | Unset):
        west_from (float | Unset):
        west_to (float | Unset):
        north_from (float | Unset):
        north_to (float | Unset):
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
        interval_ending_from=interval_ending_from,
        interval_ending_to=interval_ending_to,
        system_wide_from=system_wide_from,
        system_wide_to=system_wide_to,
        panhandle_from=panhandle_from,
        panhandle_to=panhandle_to,
        coast_from=coast_from,
        coast_to=coast_to,
        south_from=south_from,
        south_to=south_to,
        west_from=west_from,
        west_to=west_to,
        north_from=north_from,
        north_to=north_to,
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
    interval_ending_from: str | Unset = UNSET,
    interval_ending_to: str | Unset = UNSET,
    system_wide_from: float | Unset = UNSET,
    system_wide_to: float | Unset = UNSET,
    panhandle_from: float | Unset = UNSET,
    panhandle_to: float | Unset = UNSET,
    coast_from: float | Unset = UNSET,
    coast_to: float | Unset = UNSET,
    south_from: float | Unset = UNSET,
    south_to: float | Unset = UNSET,
    west_from: float | Unset = UNSET,
    west_to: float | Unset = UNSET,
    north_from: float | Unset = UNSET,
    north_to: float | Unset = UNSET,
    dst_flag: bool | Unset = UNSET,
    posted_datetime_from: str | Unset = UNSET,
    posted_datetime_to: str | Unset = UNSET,
    page: int | Unset = UNSET,
    size: int | Unset = UNSET,
    sort: str | Unset = UNSET,
    dir_: str | Unset = UNSET,
) -> Response[Exception_ | Report]:
    """Wind Power Production - Actual 5-Minute Averaged Values by Geographical Region

     Wind Power Production - Actual 5-Minute Averaged Values by Geographical Region

    Args:
        interval_ending_from (str | Unset):
        interval_ending_to (str | Unset):
        system_wide_from (float | Unset):
        system_wide_to (float | Unset):
        panhandle_from (float | Unset):
        panhandle_to (float | Unset):
        coast_from (float | Unset):
        coast_to (float | Unset):
        south_from (float | Unset):
        south_to (float | Unset):
        west_from (float | Unset):
        west_to (float | Unset):
        north_from (float | Unset):
        north_to (float | Unset):
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
        interval_ending_from=interval_ending_from,
        interval_ending_to=interval_ending_to,
        system_wide_from=system_wide_from,
        system_wide_to=system_wide_to,
        panhandle_from=panhandle_from,
        panhandle_to=panhandle_to,
        coast_from=coast_from,
        coast_to=coast_to,
        south_from=south_from,
        south_to=south_to,
        west_from=west_from,
        west_to=west_to,
        north_from=north_from,
        north_to=north_to,
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
    interval_ending_from: str | Unset = UNSET,
    interval_ending_to: str | Unset = UNSET,
    system_wide_from: float | Unset = UNSET,
    system_wide_to: float | Unset = UNSET,
    panhandle_from: float | Unset = UNSET,
    panhandle_to: float | Unset = UNSET,
    coast_from: float | Unset = UNSET,
    coast_to: float | Unset = UNSET,
    south_from: float | Unset = UNSET,
    south_to: float | Unset = UNSET,
    west_from: float | Unset = UNSET,
    west_to: float | Unset = UNSET,
    north_from: float | Unset = UNSET,
    north_to: float | Unset = UNSET,
    dst_flag: bool | Unset = UNSET,
    posted_datetime_from: str | Unset = UNSET,
    posted_datetime_to: str | Unset = UNSET,
    page: int | Unset = UNSET,
    size: int | Unset = UNSET,
    sort: str | Unset = UNSET,
    dir_: str | Unset = UNSET,
) -> Exception_ | Report | None:
    """Wind Power Production - Actual 5-Minute Averaged Values by Geographical Region

     Wind Power Production - Actual 5-Minute Averaged Values by Geographical Region

    Args:
        interval_ending_from (str | Unset):
        interval_ending_to (str | Unset):
        system_wide_from (float | Unset):
        system_wide_to (float | Unset):
        panhandle_from (float | Unset):
        panhandle_to (float | Unset):
        coast_from (float | Unset):
        coast_to (float | Unset):
        south_from (float | Unset):
        south_to (float | Unset):
        west_from (float | Unset):
        west_to (float | Unset):
        north_from (float | Unset):
        north_to (float | Unset):
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
            interval_ending_from=interval_ending_from,
            interval_ending_to=interval_ending_to,
            system_wide_from=system_wide_from,
            system_wide_to=system_wide_to,
            panhandle_from=panhandle_from,
            panhandle_to=panhandle_to,
            coast_from=coast_from,
            coast_to=coast_to,
            south_from=south_from,
            south_to=south_to,
            west_from=west_from,
            west_to=west_to,
            north_from=north_from,
            north_to=north_to,
            dst_flag=dst_flag,
            posted_datetime_from=posted_datetime_from,
            posted_datetime_to=posted_datetime_to,
            page=page,
            size=size,
            sort=sort,
            dir_=dir_,
        )
    ).parsed
