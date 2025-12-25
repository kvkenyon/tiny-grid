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
    operating_day_from: str | Unset = UNSET,
    operating_day_to: str | Unset = UNSET,
    hour_ending: str | Unset = UNSET,
    north_from: float | Unset = UNSET,
    north_to: float | Unset = UNSET,
    south_from: float | Unset = UNSET,
    south_to: float | Unset = UNSET,
    west_from: float | Unset = UNSET,
    west_to: float | Unset = UNSET,
    houston_from: float | Unset = UNSET,
    houston_to: float | Unset = UNSET,
    total_from: float | Unset = UNSET,
    total_to: float | Unset = UNSET,
    dst_flag: bool | Unset = UNSET,
    page: int | Unset = UNSET,
    size: int | Unset = UNSET,
    sort: str | Unset = UNSET,
    dir_: str | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["operatingDayFrom"] = operating_day_from

    params["operatingDayTo"] = operating_day_to

    params["hourEnding"] = hour_ending

    params["northFrom"] = north_from

    params["northTo"] = north_to

    params["southFrom"] = south_from

    params["southTo"] = south_to

    params["westFrom"] = west_from

    params["westTo"] = west_to

    params["houstonFrom"] = houston_from

    params["houstonTo"] = houston_to

    params["totalFrom"] = total_from

    params["totalTo"] = total_to

    params["DSTFlag"] = dst_flag

    params["page"] = page

    params["size"] = size

    params["sort"] = sort

    params["dir"] = dir_

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/np6-346-cd/act_sys_load_by_fzn",
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
    operating_day_from: str | Unset = UNSET,
    operating_day_to: str | Unset = UNSET,
    hour_ending: str | Unset = UNSET,
    north_from: float | Unset = UNSET,
    north_to: float | Unset = UNSET,
    south_from: float | Unset = UNSET,
    south_to: float | Unset = UNSET,
    west_from: float | Unset = UNSET,
    west_to: float | Unset = UNSET,
    houston_from: float | Unset = UNSET,
    houston_to: float | Unset = UNSET,
    total_from: float | Unset = UNSET,
    total_to: float | Unset = UNSET,
    dst_flag: bool | Unset = UNSET,
    page: int | Unset = UNSET,
    size: int | Unset = UNSET,
    sort: str | Unset = UNSET,
    dir_: str | Unset = UNSET,
) -> Response[Exception_ | Report]:
    """Actual System Load by Forecast Zone

     Actual System Load by Forecast Zone

    Args:
        operating_day_from (str | Unset):
        operating_day_to (str | Unset):
        hour_ending (str | Unset):
        north_from (float | Unset):
        north_to (float | Unset):
        south_from (float | Unset):
        south_to (float | Unset):
        west_from (float | Unset):
        west_to (float | Unset):
        houston_from (float | Unset):
        houston_to (float | Unset):
        total_from (float | Unset):
        total_to (float | Unset):
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
        operating_day_from=operating_day_from,
        operating_day_to=operating_day_to,
        hour_ending=hour_ending,
        north_from=north_from,
        north_to=north_to,
        south_from=south_from,
        south_to=south_to,
        west_from=west_from,
        west_to=west_to,
        houston_from=houston_from,
        houston_to=houston_to,
        total_from=total_from,
        total_to=total_to,
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
    operating_day_from: str | Unset = UNSET,
    operating_day_to: str | Unset = UNSET,
    hour_ending: str | Unset = UNSET,
    north_from: float | Unset = UNSET,
    north_to: float | Unset = UNSET,
    south_from: float | Unset = UNSET,
    south_to: float | Unset = UNSET,
    west_from: float | Unset = UNSET,
    west_to: float | Unset = UNSET,
    houston_from: float | Unset = UNSET,
    houston_to: float | Unset = UNSET,
    total_from: float | Unset = UNSET,
    total_to: float | Unset = UNSET,
    dst_flag: bool | Unset = UNSET,
    page: int | Unset = UNSET,
    size: int | Unset = UNSET,
    sort: str | Unset = UNSET,
    dir_: str | Unset = UNSET,
) -> Exception_ | Report | None:
    """Actual System Load by Forecast Zone

     Actual System Load by Forecast Zone

    Args:
        operating_day_from (str | Unset):
        operating_day_to (str | Unset):
        hour_ending (str | Unset):
        north_from (float | Unset):
        north_to (float | Unset):
        south_from (float | Unset):
        south_to (float | Unset):
        west_from (float | Unset):
        west_to (float | Unset):
        houston_from (float | Unset):
        houston_to (float | Unset):
        total_from (float | Unset):
        total_to (float | Unset):
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
        operating_day_from=operating_day_from,
        operating_day_to=operating_day_to,
        hour_ending=hour_ending,
        north_from=north_from,
        north_to=north_to,
        south_from=south_from,
        south_to=south_to,
        west_from=west_from,
        west_to=west_to,
        houston_from=houston_from,
        houston_to=houston_to,
        total_from=total_from,
        total_to=total_to,
        dst_flag=dst_flag,
        page=page,
        size=size,
        sort=sort,
        dir_=dir_,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    operating_day_from: str | Unset = UNSET,
    operating_day_to: str | Unset = UNSET,
    hour_ending: str | Unset = UNSET,
    north_from: float | Unset = UNSET,
    north_to: float | Unset = UNSET,
    south_from: float | Unset = UNSET,
    south_to: float | Unset = UNSET,
    west_from: float | Unset = UNSET,
    west_to: float | Unset = UNSET,
    houston_from: float | Unset = UNSET,
    houston_to: float | Unset = UNSET,
    total_from: float | Unset = UNSET,
    total_to: float | Unset = UNSET,
    dst_flag: bool | Unset = UNSET,
    page: int | Unset = UNSET,
    size: int | Unset = UNSET,
    sort: str | Unset = UNSET,
    dir_: str | Unset = UNSET,
) -> Response[Exception_ | Report]:
    """Actual System Load by Forecast Zone

     Actual System Load by Forecast Zone

    Args:
        operating_day_from (str | Unset):
        operating_day_to (str | Unset):
        hour_ending (str | Unset):
        north_from (float | Unset):
        north_to (float | Unset):
        south_from (float | Unset):
        south_to (float | Unset):
        west_from (float | Unset):
        west_to (float | Unset):
        houston_from (float | Unset):
        houston_to (float | Unset):
        total_from (float | Unset):
        total_to (float | Unset):
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
        operating_day_from=operating_day_from,
        operating_day_to=operating_day_to,
        hour_ending=hour_ending,
        north_from=north_from,
        north_to=north_to,
        south_from=south_from,
        south_to=south_to,
        west_from=west_from,
        west_to=west_to,
        houston_from=houston_from,
        houston_to=houston_to,
        total_from=total_from,
        total_to=total_to,
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
    operating_day_from: str | Unset = UNSET,
    operating_day_to: str | Unset = UNSET,
    hour_ending: str | Unset = UNSET,
    north_from: float | Unset = UNSET,
    north_to: float | Unset = UNSET,
    south_from: float | Unset = UNSET,
    south_to: float | Unset = UNSET,
    west_from: float | Unset = UNSET,
    west_to: float | Unset = UNSET,
    houston_from: float | Unset = UNSET,
    houston_to: float | Unset = UNSET,
    total_from: float | Unset = UNSET,
    total_to: float | Unset = UNSET,
    dst_flag: bool | Unset = UNSET,
    page: int | Unset = UNSET,
    size: int | Unset = UNSET,
    sort: str | Unset = UNSET,
    dir_: str | Unset = UNSET,
) -> Exception_ | Report | None:
    """Actual System Load by Forecast Zone

     Actual System Load by Forecast Zone

    Args:
        operating_day_from (str | Unset):
        operating_day_to (str | Unset):
        hour_ending (str | Unset):
        north_from (float | Unset):
        north_to (float | Unset):
        south_from (float | Unset):
        south_to (float | Unset):
        west_from (float | Unset):
        west_to (float | Unset):
        houston_from (float | Unset):
        houston_to (float | Unset):
        total_from (float | Unset):
        total_to (float | Unset):
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
            operating_day_from=operating_day_from,
            operating_day_to=operating_day_to,
            hour_ending=hour_ending,
            north_from=north_from,
            north_to=north_to,
            south_from=south_from,
            south_to=south_to,
            west_from=west_from,
            west_to=west_to,
            houston_from=houston_from,
            houston_to=houston_to,
            total_from=total_from,
            total_to=total_to,
            dst_flag=dst_flag,
            page=page,
            size=size,
            sort=sort,
            dir_=dir_,
        )
    ).parsed
