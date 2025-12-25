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
    sced_timestamp_from: str | Unset = UNSET,
    sced_timestamp_to: str | Unset = UNSET,
    repeat_hour_flag: bool | Unset = UNSET,
    sum_telem_dsr_load_from: float | Unset = UNSET,
    sum_telem_dsr_load_to: float | Unset = UNSET,
    sum_telem_dsr_gen_from: float | Unset = UNSET,
    sum_telem_dsr_gen_to: float | Unset = UNSET,
    page: int | Unset = UNSET,
    size: int | Unset = UNSET,
    sort: str | Unset = UNSET,
    dir_: str | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["SCEDTimestampFrom"] = sced_timestamp_from

    params["SCEDTimestampTo"] = sced_timestamp_to

    params["repeatHourFlag"] = repeat_hour_flag

    params["sumTelemDSRLoadFrom"] = sum_telem_dsr_load_from

    params["sumTelemDSRLoadTo"] = sum_telem_dsr_load_to

    params["sumTelemDSRGenFrom"] = sum_telem_dsr_gen_from

    params["sumTelemDSRGenTo"] = sum_telem_dsr_gen_to

    params["page"] = page

    params["size"] = size

    params["sort"] = sort

    params["dir"] = dir_

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/np3-910-er/2d_agg_dsr_loads",
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
    sced_timestamp_from: str | Unset = UNSET,
    sced_timestamp_to: str | Unset = UNSET,
    repeat_hour_flag: bool | Unset = UNSET,
    sum_telem_dsr_load_from: float | Unset = UNSET,
    sum_telem_dsr_load_to: float | Unset = UNSET,
    sum_telem_dsr_gen_from: float | Unset = UNSET,
    sum_telem_dsr_gen_to: float | Unset = UNSET,
    page: int | Unset = UNSET,
    size: int | Unset = UNSET,
    sort: str | Unset = UNSET,
    dir_: str | Unset = UNSET,
) -> Response[Exception_ | Report]:
    """2 Day Aggregated DSR Loads

     2 Day Aggregated DSR Loads

    Args:
        sced_timestamp_from (str | Unset):
        sced_timestamp_to (str | Unset):
        repeat_hour_flag (bool | Unset):
        sum_telem_dsr_load_from (float | Unset):
        sum_telem_dsr_load_to (float | Unset):
        sum_telem_dsr_gen_from (float | Unset):
        sum_telem_dsr_gen_to (float | Unset):
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
        sced_timestamp_from=sced_timestamp_from,
        sced_timestamp_to=sced_timestamp_to,
        repeat_hour_flag=repeat_hour_flag,
        sum_telem_dsr_load_from=sum_telem_dsr_load_from,
        sum_telem_dsr_load_to=sum_telem_dsr_load_to,
        sum_telem_dsr_gen_from=sum_telem_dsr_gen_from,
        sum_telem_dsr_gen_to=sum_telem_dsr_gen_to,
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
    sced_timestamp_from: str | Unset = UNSET,
    sced_timestamp_to: str | Unset = UNSET,
    repeat_hour_flag: bool | Unset = UNSET,
    sum_telem_dsr_load_from: float | Unset = UNSET,
    sum_telem_dsr_load_to: float | Unset = UNSET,
    sum_telem_dsr_gen_from: float | Unset = UNSET,
    sum_telem_dsr_gen_to: float | Unset = UNSET,
    page: int | Unset = UNSET,
    size: int | Unset = UNSET,
    sort: str | Unset = UNSET,
    dir_: str | Unset = UNSET,
) -> Exception_ | Report | None:
    """2 Day Aggregated DSR Loads

     2 Day Aggregated DSR Loads

    Args:
        sced_timestamp_from (str | Unset):
        sced_timestamp_to (str | Unset):
        repeat_hour_flag (bool | Unset):
        sum_telem_dsr_load_from (float | Unset):
        sum_telem_dsr_load_to (float | Unset):
        sum_telem_dsr_gen_from (float | Unset):
        sum_telem_dsr_gen_to (float | Unset):
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
        sced_timestamp_from=sced_timestamp_from,
        sced_timestamp_to=sced_timestamp_to,
        repeat_hour_flag=repeat_hour_flag,
        sum_telem_dsr_load_from=sum_telem_dsr_load_from,
        sum_telem_dsr_load_to=sum_telem_dsr_load_to,
        sum_telem_dsr_gen_from=sum_telem_dsr_gen_from,
        sum_telem_dsr_gen_to=sum_telem_dsr_gen_to,
        page=page,
        size=size,
        sort=sort,
        dir_=dir_,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    sced_timestamp_from: str | Unset = UNSET,
    sced_timestamp_to: str | Unset = UNSET,
    repeat_hour_flag: bool | Unset = UNSET,
    sum_telem_dsr_load_from: float | Unset = UNSET,
    sum_telem_dsr_load_to: float | Unset = UNSET,
    sum_telem_dsr_gen_from: float | Unset = UNSET,
    sum_telem_dsr_gen_to: float | Unset = UNSET,
    page: int | Unset = UNSET,
    size: int | Unset = UNSET,
    sort: str | Unset = UNSET,
    dir_: str | Unset = UNSET,
) -> Response[Exception_ | Report]:
    """2 Day Aggregated DSR Loads

     2 Day Aggregated DSR Loads

    Args:
        sced_timestamp_from (str | Unset):
        sced_timestamp_to (str | Unset):
        repeat_hour_flag (bool | Unset):
        sum_telem_dsr_load_from (float | Unset):
        sum_telem_dsr_load_to (float | Unset):
        sum_telem_dsr_gen_from (float | Unset):
        sum_telem_dsr_gen_to (float | Unset):
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
        sced_timestamp_from=sced_timestamp_from,
        sced_timestamp_to=sced_timestamp_to,
        repeat_hour_flag=repeat_hour_flag,
        sum_telem_dsr_load_from=sum_telem_dsr_load_from,
        sum_telem_dsr_load_to=sum_telem_dsr_load_to,
        sum_telem_dsr_gen_from=sum_telem_dsr_gen_from,
        sum_telem_dsr_gen_to=sum_telem_dsr_gen_to,
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
    sced_timestamp_from: str | Unset = UNSET,
    sced_timestamp_to: str | Unset = UNSET,
    repeat_hour_flag: bool | Unset = UNSET,
    sum_telem_dsr_load_from: float | Unset = UNSET,
    sum_telem_dsr_load_to: float | Unset = UNSET,
    sum_telem_dsr_gen_from: float | Unset = UNSET,
    sum_telem_dsr_gen_to: float | Unset = UNSET,
    page: int | Unset = UNSET,
    size: int | Unset = UNSET,
    sort: str | Unset = UNSET,
    dir_: str | Unset = UNSET,
) -> Exception_ | Report | None:
    """2 Day Aggregated DSR Loads

     2 Day Aggregated DSR Loads

    Args:
        sced_timestamp_from (str | Unset):
        sced_timestamp_to (str | Unset):
        repeat_hour_flag (bool | Unset):
        sum_telem_dsr_load_from (float | Unset):
        sum_telem_dsr_load_to (float | Unset):
        sum_telem_dsr_gen_from (float | Unset):
        sum_telem_dsr_gen_to (float | Unset):
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
            sced_timestamp_from=sced_timestamp_from,
            sced_timestamp_to=sced_timestamp_to,
            repeat_hour_flag=repeat_hour_flag,
            sum_telem_dsr_load_from=sum_telem_dsr_load_from,
            sum_telem_dsr_load_to=sum_telem_dsr_load_to,
            sum_telem_dsr_gen_from=sum_telem_dsr_gen_from,
            sum_telem_dsr_gen_to=sum_telem_dsr_gen_to,
            page=page,
            size=size,
            sort=sort,
            dir_=dir_,
        )
    ).parsed
