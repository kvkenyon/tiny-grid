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
    dst_flag: bool | Unset = UNSET,
    delivery_date_from: str | Unset = UNSET,
    delivery_date_to: str | Unset = UNSET,
    hour_ending: str | Unset = UNSET,
    coast_from: float | Unset = UNSET,
    coast_to: float | Unset = UNSET,
    east_from: float | Unset = UNSET,
    east_to: float | Unset = UNSET,
    far_west_from: float | Unset = UNSET,
    far_west_to: float | Unset = UNSET,
    north_from: float | Unset = UNSET,
    north_to: float | Unset = UNSET,
    north_central_from: float | Unset = UNSET,
    north_central_to: float | Unset = UNSET,
    south_central_from: float | Unset = UNSET,
    south_central_to: float | Unset = UNSET,
    southern_from: float | Unset = UNSET,
    southern_to: float | Unset = UNSET,
    posted_datetime_from: str | Unset = UNSET,
    posted_datetime_to: str | Unset = UNSET,
    west_from: float | Unset = UNSET,
    west_to: float | Unset = UNSET,
    system_total_from: float | Unset = UNSET,
    system_total_to: float | Unset = UNSET,
    model: str | Unset = UNSET,
    in_use_flag: bool | Unset = UNSET,
    page: int | Unset = UNSET,
    size: int | Unset = UNSET,
    sort: str | Unset = UNSET,
    dir_: str | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["DSTFlag"] = dst_flag

    params["deliveryDateFrom"] = delivery_date_from

    params["deliveryDateTo"] = delivery_date_to

    params["hourEnding"] = hour_ending

    params["coastFrom"] = coast_from

    params["coastTo"] = coast_to

    params["eastFrom"] = east_from

    params["eastTo"] = east_to

    params["farWestFrom"] = far_west_from

    params["farWestTo"] = far_west_to

    params["northFrom"] = north_from

    params["northTo"] = north_to

    params["northCentralFrom"] = north_central_from

    params["northCentralTo"] = north_central_to

    params["southCentralFrom"] = south_central_from

    params["southCentralTo"] = south_central_to

    params["southernFrom"] = southern_from

    params["southernTo"] = southern_to

    params["postedDatetimeFrom"] = posted_datetime_from

    params["postedDatetimeTo"] = posted_datetime_to

    params["westFrom"] = west_from

    params["westTo"] = west_to

    params["systemTotalFrom"] = system_total_from

    params["systemTotalTo"] = system_total_to

    params["model"] = model

    params["inUseFlag"] = in_use_flag

    params["page"] = page

    params["size"] = size

    params["sort"] = sort

    params["dir"] = dir_

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/np3-565-cd/lf_by_model_weather_zone",
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
    dst_flag: bool | Unset = UNSET,
    delivery_date_from: str | Unset = UNSET,
    delivery_date_to: str | Unset = UNSET,
    hour_ending: str | Unset = UNSET,
    coast_from: float | Unset = UNSET,
    coast_to: float | Unset = UNSET,
    east_from: float | Unset = UNSET,
    east_to: float | Unset = UNSET,
    far_west_from: float | Unset = UNSET,
    far_west_to: float | Unset = UNSET,
    north_from: float | Unset = UNSET,
    north_to: float | Unset = UNSET,
    north_central_from: float | Unset = UNSET,
    north_central_to: float | Unset = UNSET,
    south_central_from: float | Unset = UNSET,
    south_central_to: float | Unset = UNSET,
    southern_from: float | Unset = UNSET,
    southern_to: float | Unset = UNSET,
    posted_datetime_from: str | Unset = UNSET,
    posted_datetime_to: str | Unset = UNSET,
    west_from: float | Unset = UNSET,
    west_to: float | Unset = UNSET,
    system_total_from: float | Unset = UNSET,
    system_total_to: float | Unset = UNSET,
    model: str | Unset = UNSET,
    in_use_flag: bool | Unset = UNSET,
    page: int | Unset = UNSET,
    size: int | Unset = UNSET,
    sort: str | Unset = UNSET,
    dir_: str | Unset = UNSET,
) -> Response[Exception_ | Report]:
    """Seven-Day Load Forecast by Model and Weather Zone

     Seven-Day Load Forecast by Model and Weather Zone

    Args:
        dst_flag (bool | Unset):
        delivery_date_from (str | Unset):
        delivery_date_to (str | Unset):
        hour_ending (str | Unset):
        coast_from (float | Unset):
        coast_to (float | Unset):
        east_from (float | Unset):
        east_to (float | Unset):
        far_west_from (float | Unset):
        far_west_to (float | Unset):
        north_from (float | Unset):
        north_to (float | Unset):
        north_central_from (float | Unset):
        north_central_to (float | Unset):
        south_central_from (float | Unset):
        south_central_to (float | Unset):
        southern_from (float | Unset):
        southern_to (float | Unset):
        posted_datetime_from (str | Unset):
        posted_datetime_to (str | Unset):
        west_from (float | Unset):
        west_to (float | Unset):
        system_total_from (float | Unset):
        system_total_to (float | Unset):
        model (str | Unset):
        in_use_flag (bool | Unset):
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
        dst_flag=dst_flag,
        delivery_date_from=delivery_date_from,
        delivery_date_to=delivery_date_to,
        hour_ending=hour_ending,
        coast_from=coast_from,
        coast_to=coast_to,
        east_from=east_from,
        east_to=east_to,
        far_west_from=far_west_from,
        far_west_to=far_west_to,
        north_from=north_from,
        north_to=north_to,
        north_central_from=north_central_from,
        north_central_to=north_central_to,
        south_central_from=south_central_from,
        south_central_to=south_central_to,
        southern_from=southern_from,
        southern_to=southern_to,
        posted_datetime_from=posted_datetime_from,
        posted_datetime_to=posted_datetime_to,
        west_from=west_from,
        west_to=west_to,
        system_total_from=system_total_from,
        system_total_to=system_total_to,
        model=model,
        in_use_flag=in_use_flag,
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
    dst_flag: bool | Unset = UNSET,
    delivery_date_from: str | Unset = UNSET,
    delivery_date_to: str | Unset = UNSET,
    hour_ending: str | Unset = UNSET,
    coast_from: float | Unset = UNSET,
    coast_to: float | Unset = UNSET,
    east_from: float | Unset = UNSET,
    east_to: float | Unset = UNSET,
    far_west_from: float | Unset = UNSET,
    far_west_to: float | Unset = UNSET,
    north_from: float | Unset = UNSET,
    north_to: float | Unset = UNSET,
    north_central_from: float | Unset = UNSET,
    north_central_to: float | Unset = UNSET,
    south_central_from: float | Unset = UNSET,
    south_central_to: float | Unset = UNSET,
    southern_from: float | Unset = UNSET,
    southern_to: float | Unset = UNSET,
    posted_datetime_from: str | Unset = UNSET,
    posted_datetime_to: str | Unset = UNSET,
    west_from: float | Unset = UNSET,
    west_to: float | Unset = UNSET,
    system_total_from: float | Unset = UNSET,
    system_total_to: float | Unset = UNSET,
    model: str | Unset = UNSET,
    in_use_flag: bool | Unset = UNSET,
    page: int | Unset = UNSET,
    size: int | Unset = UNSET,
    sort: str | Unset = UNSET,
    dir_: str | Unset = UNSET,
) -> Exception_ | Report | None:
    """Seven-Day Load Forecast by Model and Weather Zone

     Seven-Day Load Forecast by Model and Weather Zone

    Args:
        dst_flag (bool | Unset):
        delivery_date_from (str | Unset):
        delivery_date_to (str | Unset):
        hour_ending (str | Unset):
        coast_from (float | Unset):
        coast_to (float | Unset):
        east_from (float | Unset):
        east_to (float | Unset):
        far_west_from (float | Unset):
        far_west_to (float | Unset):
        north_from (float | Unset):
        north_to (float | Unset):
        north_central_from (float | Unset):
        north_central_to (float | Unset):
        south_central_from (float | Unset):
        south_central_to (float | Unset):
        southern_from (float | Unset):
        southern_to (float | Unset):
        posted_datetime_from (str | Unset):
        posted_datetime_to (str | Unset):
        west_from (float | Unset):
        west_to (float | Unset):
        system_total_from (float | Unset):
        system_total_to (float | Unset):
        model (str | Unset):
        in_use_flag (bool | Unset):
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
        dst_flag=dst_flag,
        delivery_date_from=delivery_date_from,
        delivery_date_to=delivery_date_to,
        hour_ending=hour_ending,
        coast_from=coast_from,
        coast_to=coast_to,
        east_from=east_from,
        east_to=east_to,
        far_west_from=far_west_from,
        far_west_to=far_west_to,
        north_from=north_from,
        north_to=north_to,
        north_central_from=north_central_from,
        north_central_to=north_central_to,
        south_central_from=south_central_from,
        south_central_to=south_central_to,
        southern_from=southern_from,
        southern_to=southern_to,
        posted_datetime_from=posted_datetime_from,
        posted_datetime_to=posted_datetime_to,
        west_from=west_from,
        west_to=west_to,
        system_total_from=system_total_from,
        system_total_to=system_total_to,
        model=model,
        in_use_flag=in_use_flag,
        page=page,
        size=size,
        sort=sort,
        dir_=dir_,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    dst_flag: bool | Unset = UNSET,
    delivery_date_from: str | Unset = UNSET,
    delivery_date_to: str | Unset = UNSET,
    hour_ending: str | Unset = UNSET,
    coast_from: float | Unset = UNSET,
    coast_to: float | Unset = UNSET,
    east_from: float | Unset = UNSET,
    east_to: float | Unset = UNSET,
    far_west_from: float | Unset = UNSET,
    far_west_to: float | Unset = UNSET,
    north_from: float | Unset = UNSET,
    north_to: float | Unset = UNSET,
    north_central_from: float | Unset = UNSET,
    north_central_to: float | Unset = UNSET,
    south_central_from: float | Unset = UNSET,
    south_central_to: float | Unset = UNSET,
    southern_from: float | Unset = UNSET,
    southern_to: float | Unset = UNSET,
    posted_datetime_from: str | Unset = UNSET,
    posted_datetime_to: str | Unset = UNSET,
    west_from: float | Unset = UNSET,
    west_to: float | Unset = UNSET,
    system_total_from: float | Unset = UNSET,
    system_total_to: float | Unset = UNSET,
    model: str | Unset = UNSET,
    in_use_flag: bool | Unset = UNSET,
    page: int | Unset = UNSET,
    size: int | Unset = UNSET,
    sort: str | Unset = UNSET,
    dir_: str | Unset = UNSET,
) -> Response[Exception_ | Report]:
    """Seven-Day Load Forecast by Model and Weather Zone

     Seven-Day Load Forecast by Model and Weather Zone

    Args:
        dst_flag (bool | Unset):
        delivery_date_from (str | Unset):
        delivery_date_to (str | Unset):
        hour_ending (str | Unset):
        coast_from (float | Unset):
        coast_to (float | Unset):
        east_from (float | Unset):
        east_to (float | Unset):
        far_west_from (float | Unset):
        far_west_to (float | Unset):
        north_from (float | Unset):
        north_to (float | Unset):
        north_central_from (float | Unset):
        north_central_to (float | Unset):
        south_central_from (float | Unset):
        south_central_to (float | Unset):
        southern_from (float | Unset):
        southern_to (float | Unset):
        posted_datetime_from (str | Unset):
        posted_datetime_to (str | Unset):
        west_from (float | Unset):
        west_to (float | Unset):
        system_total_from (float | Unset):
        system_total_to (float | Unset):
        model (str | Unset):
        in_use_flag (bool | Unset):
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
        dst_flag=dst_flag,
        delivery_date_from=delivery_date_from,
        delivery_date_to=delivery_date_to,
        hour_ending=hour_ending,
        coast_from=coast_from,
        coast_to=coast_to,
        east_from=east_from,
        east_to=east_to,
        far_west_from=far_west_from,
        far_west_to=far_west_to,
        north_from=north_from,
        north_to=north_to,
        north_central_from=north_central_from,
        north_central_to=north_central_to,
        south_central_from=south_central_from,
        south_central_to=south_central_to,
        southern_from=southern_from,
        southern_to=southern_to,
        posted_datetime_from=posted_datetime_from,
        posted_datetime_to=posted_datetime_to,
        west_from=west_from,
        west_to=west_to,
        system_total_from=system_total_from,
        system_total_to=system_total_to,
        model=model,
        in_use_flag=in_use_flag,
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
    dst_flag: bool | Unset = UNSET,
    delivery_date_from: str | Unset = UNSET,
    delivery_date_to: str | Unset = UNSET,
    hour_ending: str | Unset = UNSET,
    coast_from: float | Unset = UNSET,
    coast_to: float | Unset = UNSET,
    east_from: float | Unset = UNSET,
    east_to: float | Unset = UNSET,
    far_west_from: float | Unset = UNSET,
    far_west_to: float | Unset = UNSET,
    north_from: float | Unset = UNSET,
    north_to: float | Unset = UNSET,
    north_central_from: float | Unset = UNSET,
    north_central_to: float | Unset = UNSET,
    south_central_from: float | Unset = UNSET,
    south_central_to: float | Unset = UNSET,
    southern_from: float | Unset = UNSET,
    southern_to: float | Unset = UNSET,
    posted_datetime_from: str | Unset = UNSET,
    posted_datetime_to: str | Unset = UNSET,
    west_from: float | Unset = UNSET,
    west_to: float | Unset = UNSET,
    system_total_from: float | Unset = UNSET,
    system_total_to: float | Unset = UNSET,
    model: str | Unset = UNSET,
    in_use_flag: bool | Unset = UNSET,
    page: int | Unset = UNSET,
    size: int | Unset = UNSET,
    sort: str | Unset = UNSET,
    dir_: str | Unset = UNSET,
) -> Exception_ | Report | None:
    """Seven-Day Load Forecast by Model and Weather Zone

     Seven-Day Load Forecast by Model and Weather Zone

    Args:
        dst_flag (bool | Unset):
        delivery_date_from (str | Unset):
        delivery_date_to (str | Unset):
        hour_ending (str | Unset):
        coast_from (float | Unset):
        coast_to (float | Unset):
        east_from (float | Unset):
        east_to (float | Unset):
        far_west_from (float | Unset):
        far_west_to (float | Unset):
        north_from (float | Unset):
        north_to (float | Unset):
        north_central_from (float | Unset):
        north_central_to (float | Unset):
        south_central_from (float | Unset):
        south_central_to (float | Unset):
        southern_from (float | Unset):
        southern_to (float | Unset):
        posted_datetime_from (str | Unset):
        posted_datetime_to (str | Unset):
        west_from (float | Unset):
        west_to (float | Unset):
        system_total_from (float | Unset):
        system_total_to (float | Unset):
        model (str | Unset):
        in_use_flag (bool | Unset):
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
            dst_flag=dst_flag,
            delivery_date_from=delivery_date_from,
            delivery_date_to=delivery_date_to,
            hour_ending=hour_ending,
            coast_from=coast_from,
            coast_to=coast_to,
            east_from=east_from,
            east_to=east_to,
            far_west_from=far_west_from,
            far_west_to=far_west_to,
            north_from=north_from,
            north_to=north_to,
            north_central_from=north_central_from,
            north_central_to=north_central_to,
            south_central_from=south_central_from,
            south_central_to=south_central_to,
            southern_from=southern_from,
            southern_to=southern_to,
            posted_datetime_from=posted_datetime_from,
            posted_datetime_to=posted_datetime_to,
            west_from=west_from,
            west_to=west_to,
            system_total_from=system_total_from,
            system_total_to=system_total_to,
            model=model,
            in_use_flag=in_use_flag,
            page=page,
            size=size,
            sort=sort,
            dir_=dir_,
        )
    ).parsed
