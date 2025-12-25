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
    sum_base_point_non_wgr_from: float | Unset = UNSET,
    sum_base_point_non_wgr_to: float | Unset = UNSET,
    sum_hasl_non_wgr_from: float | Unset = UNSET,
    sum_hasl_non_wgr_to: float | Unset = UNSET,
    sum_lasl_non_wgr_from: float | Unset = UNSET,
    sum_lasl_non_wgr_to: float | Unset = UNSET,
    sum_base_point_wgr_from: float | Unset = UNSET,
    sum_base_point_wgr_to: float | Unset = UNSET,
    sum_hasl_wgr_from: float | Unset = UNSET,
    sum_hasl_wgr_to: float | Unset = UNSET,
    sum_lasl_wgr_from: float | Unset = UNSET,
    sum_lasl_wgr_to: float | Unset = UNSET,
    sum_base_point_rem_res_from: float | Unset = UNSET,
    sum_base_point_rem_res_to: float | Unset = UNSET,
    sum_hasl_rem_res_from: float | Unset = UNSET,
    sum_hasl_rem_res_to: float | Unset = UNSET,
    sum_lasl_rem_res_from: float | Unset = UNSET,
    sum_lasl_rem_res_to: float | Unset = UNSET,
    sum_gen_telem_mw_from: float | Unset = UNSET,
    sum_gen_telem_mw_to: float | Unset = UNSET,
    page: int | Unset = UNSET,
    size: int | Unset = UNSET,
    sort: str | Unset = UNSET,
    dir_: str | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["SCEDTimestampFrom"] = sced_timestamp_from

    params["SCEDTimestampTo"] = sced_timestamp_to

    params["repeatHourFlag"] = repeat_hour_flag

    params["sumBasePointNonWGRFrom"] = sum_base_point_non_wgr_from

    params["sumBasePointNonWGRTo"] = sum_base_point_non_wgr_to

    params["sumHaslNonWGRFrom"] = sum_hasl_non_wgr_from

    params["sumHaslNonWGRTo"] = sum_hasl_non_wgr_to

    params["sumLaslNonWGRFrom"] = sum_lasl_non_wgr_from

    params["sumLaslNonWGRTo"] = sum_lasl_non_wgr_to

    params["sumBasePointWGRFrom"] = sum_base_point_wgr_from

    params["sumBasePointWGRTo"] = sum_base_point_wgr_to

    params["sumHaslWGRFrom"] = sum_hasl_wgr_from

    params["sumHaslWGRTo"] = sum_hasl_wgr_to

    params["sumLaslWGRFrom"] = sum_lasl_wgr_from

    params["sumLaslWGRTo"] = sum_lasl_wgr_to

    params["sumBasePointRemResFrom"] = sum_base_point_rem_res_from

    params["sumBasePointRemResTo"] = sum_base_point_rem_res_to

    params["sumHaslRemResFrom"] = sum_hasl_rem_res_from

    params["sumHaslRemResTo"] = sum_hasl_rem_res_to

    params["sumLaslRemResFrom"] = sum_lasl_rem_res_from

    params["sumLaslRemResTo"] = sum_lasl_rem_res_to

    params["sumGenTelemMWFrom"] = sum_gen_telem_mw_from

    params["sumGenTelemMWTo"] = sum_gen_telem_mw_to

    params["page"] = page

    params["size"] = size

    params["sort"] = sort

    params["dir"] = dir_

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/np3-910-er/2d_agg_gen_summary_houston",
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
    sum_base_point_non_wgr_from: float | Unset = UNSET,
    sum_base_point_non_wgr_to: float | Unset = UNSET,
    sum_hasl_non_wgr_from: float | Unset = UNSET,
    sum_hasl_non_wgr_to: float | Unset = UNSET,
    sum_lasl_non_wgr_from: float | Unset = UNSET,
    sum_lasl_non_wgr_to: float | Unset = UNSET,
    sum_base_point_wgr_from: float | Unset = UNSET,
    sum_base_point_wgr_to: float | Unset = UNSET,
    sum_hasl_wgr_from: float | Unset = UNSET,
    sum_hasl_wgr_to: float | Unset = UNSET,
    sum_lasl_wgr_from: float | Unset = UNSET,
    sum_lasl_wgr_to: float | Unset = UNSET,
    sum_base_point_rem_res_from: float | Unset = UNSET,
    sum_base_point_rem_res_to: float | Unset = UNSET,
    sum_hasl_rem_res_from: float | Unset = UNSET,
    sum_hasl_rem_res_to: float | Unset = UNSET,
    sum_lasl_rem_res_from: float | Unset = UNSET,
    sum_lasl_rem_res_to: float | Unset = UNSET,
    sum_gen_telem_mw_from: float | Unset = UNSET,
    sum_gen_telem_mw_to: float | Unset = UNSET,
    page: int | Unset = UNSET,
    size: int | Unset = UNSET,
    sort: str | Unset = UNSET,
    dir_: str | Unset = UNSET,
) -> Response[Exception_ | Report]:
    """2 Day Aggregated Generation Summary Houston

     2 Day Aggregated Generation Summary Houston

    Args:
        sced_timestamp_from (str | Unset):
        sced_timestamp_to (str | Unset):
        repeat_hour_flag (bool | Unset):
        sum_base_point_non_wgr_from (float | Unset):
        sum_base_point_non_wgr_to (float | Unset):
        sum_hasl_non_wgr_from (float | Unset):
        sum_hasl_non_wgr_to (float | Unset):
        sum_lasl_non_wgr_from (float | Unset):
        sum_lasl_non_wgr_to (float | Unset):
        sum_base_point_wgr_from (float | Unset):
        sum_base_point_wgr_to (float | Unset):
        sum_hasl_wgr_from (float | Unset):
        sum_hasl_wgr_to (float | Unset):
        sum_lasl_wgr_from (float | Unset):
        sum_lasl_wgr_to (float | Unset):
        sum_base_point_rem_res_from (float | Unset):
        sum_base_point_rem_res_to (float | Unset):
        sum_hasl_rem_res_from (float | Unset):
        sum_hasl_rem_res_to (float | Unset):
        sum_lasl_rem_res_from (float | Unset):
        sum_lasl_rem_res_to (float | Unset):
        sum_gen_telem_mw_from (float | Unset):
        sum_gen_telem_mw_to (float | Unset):
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
        sum_base_point_non_wgr_from=sum_base_point_non_wgr_from,
        sum_base_point_non_wgr_to=sum_base_point_non_wgr_to,
        sum_hasl_non_wgr_from=sum_hasl_non_wgr_from,
        sum_hasl_non_wgr_to=sum_hasl_non_wgr_to,
        sum_lasl_non_wgr_from=sum_lasl_non_wgr_from,
        sum_lasl_non_wgr_to=sum_lasl_non_wgr_to,
        sum_base_point_wgr_from=sum_base_point_wgr_from,
        sum_base_point_wgr_to=sum_base_point_wgr_to,
        sum_hasl_wgr_from=sum_hasl_wgr_from,
        sum_hasl_wgr_to=sum_hasl_wgr_to,
        sum_lasl_wgr_from=sum_lasl_wgr_from,
        sum_lasl_wgr_to=sum_lasl_wgr_to,
        sum_base_point_rem_res_from=sum_base_point_rem_res_from,
        sum_base_point_rem_res_to=sum_base_point_rem_res_to,
        sum_hasl_rem_res_from=sum_hasl_rem_res_from,
        sum_hasl_rem_res_to=sum_hasl_rem_res_to,
        sum_lasl_rem_res_from=sum_lasl_rem_res_from,
        sum_lasl_rem_res_to=sum_lasl_rem_res_to,
        sum_gen_telem_mw_from=sum_gen_telem_mw_from,
        sum_gen_telem_mw_to=sum_gen_telem_mw_to,
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
    sum_base_point_non_wgr_from: float | Unset = UNSET,
    sum_base_point_non_wgr_to: float | Unset = UNSET,
    sum_hasl_non_wgr_from: float | Unset = UNSET,
    sum_hasl_non_wgr_to: float | Unset = UNSET,
    sum_lasl_non_wgr_from: float | Unset = UNSET,
    sum_lasl_non_wgr_to: float | Unset = UNSET,
    sum_base_point_wgr_from: float | Unset = UNSET,
    sum_base_point_wgr_to: float | Unset = UNSET,
    sum_hasl_wgr_from: float | Unset = UNSET,
    sum_hasl_wgr_to: float | Unset = UNSET,
    sum_lasl_wgr_from: float | Unset = UNSET,
    sum_lasl_wgr_to: float | Unset = UNSET,
    sum_base_point_rem_res_from: float | Unset = UNSET,
    sum_base_point_rem_res_to: float | Unset = UNSET,
    sum_hasl_rem_res_from: float | Unset = UNSET,
    sum_hasl_rem_res_to: float | Unset = UNSET,
    sum_lasl_rem_res_from: float | Unset = UNSET,
    sum_lasl_rem_res_to: float | Unset = UNSET,
    sum_gen_telem_mw_from: float | Unset = UNSET,
    sum_gen_telem_mw_to: float | Unset = UNSET,
    page: int | Unset = UNSET,
    size: int | Unset = UNSET,
    sort: str | Unset = UNSET,
    dir_: str | Unset = UNSET,
) -> Exception_ | Report | None:
    """2 Day Aggregated Generation Summary Houston

     2 Day Aggregated Generation Summary Houston

    Args:
        sced_timestamp_from (str | Unset):
        sced_timestamp_to (str | Unset):
        repeat_hour_flag (bool | Unset):
        sum_base_point_non_wgr_from (float | Unset):
        sum_base_point_non_wgr_to (float | Unset):
        sum_hasl_non_wgr_from (float | Unset):
        sum_hasl_non_wgr_to (float | Unset):
        sum_lasl_non_wgr_from (float | Unset):
        sum_lasl_non_wgr_to (float | Unset):
        sum_base_point_wgr_from (float | Unset):
        sum_base_point_wgr_to (float | Unset):
        sum_hasl_wgr_from (float | Unset):
        sum_hasl_wgr_to (float | Unset):
        sum_lasl_wgr_from (float | Unset):
        sum_lasl_wgr_to (float | Unset):
        sum_base_point_rem_res_from (float | Unset):
        sum_base_point_rem_res_to (float | Unset):
        sum_hasl_rem_res_from (float | Unset):
        sum_hasl_rem_res_to (float | Unset):
        sum_lasl_rem_res_from (float | Unset):
        sum_lasl_rem_res_to (float | Unset):
        sum_gen_telem_mw_from (float | Unset):
        sum_gen_telem_mw_to (float | Unset):
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
        sum_base_point_non_wgr_from=sum_base_point_non_wgr_from,
        sum_base_point_non_wgr_to=sum_base_point_non_wgr_to,
        sum_hasl_non_wgr_from=sum_hasl_non_wgr_from,
        sum_hasl_non_wgr_to=sum_hasl_non_wgr_to,
        sum_lasl_non_wgr_from=sum_lasl_non_wgr_from,
        sum_lasl_non_wgr_to=sum_lasl_non_wgr_to,
        sum_base_point_wgr_from=sum_base_point_wgr_from,
        sum_base_point_wgr_to=sum_base_point_wgr_to,
        sum_hasl_wgr_from=sum_hasl_wgr_from,
        sum_hasl_wgr_to=sum_hasl_wgr_to,
        sum_lasl_wgr_from=sum_lasl_wgr_from,
        sum_lasl_wgr_to=sum_lasl_wgr_to,
        sum_base_point_rem_res_from=sum_base_point_rem_res_from,
        sum_base_point_rem_res_to=sum_base_point_rem_res_to,
        sum_hasl_rem_res_from=sum_hasl_rem_res_from,
        sum_hasl_rem_res_to=sum_hasl_rem_res_to,
        sum_lasl_rem_res_from=sum_lasl_rem_res_from,
        sum_lasl_rem_res_to=sum_lasl_rem_res_to,
        sum_gen_telem_mw_from=sum_gen_telem_mw_from,
        sum_gen_telem_mw_to=sum_gen_telem_mw_to,
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
    sum_base_point_non_wgr_from: float | Unset = UNSET,
    sum_base_point_non_wgr_to: float | Unset = UNSET,
    sum_hasl_non_wgr_from: float | Unset = UNSET,
    sum_hasl_non_wgr_to: float | Unset = UNSET,
    sum_lasl_non_wgr_from: float | Unset = UNSET,
    sum_lasl_non_wgr_to: float | Unset = UNSET,
    sum_base_point_wgr_from: float | Unset = UNSET,
    sum_base_point_wgr_to: float | Unset = UNSET,
    sum_hasl_wgr_from: float | Unset = UNSET,
    sum_hasl_wgr_to: float | Unset = UNSET,
    sum_lasl_wgr_from: float | Unset = UNSET,
    sum_lasl_wgr_to: float | Unset = UNSET,
    sum_base_point_rem_res_from: float | Unset = UNSET,
    sum_base_point_rem_res_to: float | Unset = UNSET,
    sum_hasl_rem_res_from: float | Unset = UNSET,
    sum_hasl_rem_res_to: float | Unset = UNSET,
    sum_lasl_rem_res_from: float | Unset = UNSET,
    sum_lasl_rem_res_to: float | Unset = UNSET,
    sum_gen_telem_mw_from: float | Unset = UNSET,
    sum_gen_telem_mw_to: float | Unset = UNSET,
    page: int | Unset = UNSET,
    size: int | Unset = UNSET,
    sort: str | Unset = UNSET,
    dir_: str | Unset = UNSET,
) -> Response[Exception_ | Report]:
    """2 Day Aggregated Generation Summary Houston

     2 Day Aggregated Generation Summary Houston

    Args:
        sced_timestamp_from (str | Unset):
        sced_timestamp_to (str | Unset):
        repeat_hour_flag (bool | Unset):
        sum_base_point_non_wgr_from (float | Unset):
        sum_base_point_non_wgr_to (float | Unset):
        sum_hasl_non_wgr_from (float | Unset):
        sum_hasl_non_wgr_to (float | Unset):
        sum_lasl_non_wgr_from (float | Unset):
        sum_lasl_non_wgr_to (float | Unset):
        sum_base_point_wgr_from (float | Unset):
        sum_base_point_wgr_to (float | Unset):
        sum_hasl_wgr_from (float | Unset):
        sum_hasl_wgr_to (float | Unset):
        sum_lasl_wgr_from (float | Unset):
        sum_lasl_wgr_to (float | Unset):
        sum_base_point_rem_res_from (float | Unset):
        sum_base_point_rem_res_to (float | Unset):
        sum_hasl_rem_res_from (float | Unset):
        sum_hasl_rem_res_to (float | Unset):
        sum_lasl_rem_res_from (float | Unset):
        sum_lasl_rem_res_to (float | Unset):
        sum_gen_telem_mw_from (float | Unset):
        sum_gen_telem_mw_to (float | Unset):
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
        sum_base_point_non_wgr_from=sum_base_point_non_wgr_from,
        sum_base_point_non_wgr_to=sum_base_point_non_wgr_to,
        sum_hasl_non_wgr_from=sum_hasl_non_wgr_from,
        sum_hasl_non_wgr_to=sum_hasl_non_wgr_to,
        sum_lasl_non_wgr_from=sum_lasl_non_wgr_from,
        sum_lasl_non_wgr_to=sum_lasl_non_wgr_to,
        sum_base_point_wgr_from=sum_base_point_wgr_from,
        sum_base_point_wgr_to=sum_base_point_wgr_to,
        sum_hasl_wgr_from=sum_hasl_wgr_from,
        sum_hasl_wgr_to=sum_hasl_wgr_to,
        sum_lasl_wgr_from=sum_lasl_wgr_from,
        sum_lasl_wgr_to=sum_lasl_wgr_to,
        sum_base_point_rem_res_from=sum_base_point_rem_res_from,
        sum_base_point_rem_res_to=sum_base_point_rem_res_to,
        sum_hasl_rem_res_from=sum_hasl_rem_res_from,
        sum_hasl_rem_res_to=sum_hasl_rem_res_to,
        sum_lasl_rem_res_from=sum_lasl_rem_res_from,
        sum_lasl_rem_res_to=sum_lasl_rem_res_to,
        sum_gen_telem_mw_from=sum_gen_telem_mw_from,
        sum_gen_telem_mw_to=sum_gen_telem_mw_to,
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
    sum_base_point_non_wgr_from: float | Unset = UNSET,
    sum_base_point_non_wgr_to: float | Unset = UNSET,
    sum_hasl_non_wgr_from: float | Unset = UNSET,
    sum_hasl_non_wgr_to: float | Unset = UNSET,
    sum_lasl_non_wgr_from: float | Unset = UNSET,
    sum_lasl_non_wgr_to: float | Unset = UNSET,
    sum_base_point_wgr_from: float | Unset = UNSET,
    sum_base_point_wgr_to: float | Unset = UNSET,
    sum_hasl_wgr_from: float | Unset = UNSET,
    sum_hasl_wgr_to: float | Unset = UNSET,
    sum_lasl_wgr_from: float | Unset = UNSET,
    sum_lasl_wgr_to: float | Unset = UNSET,
    sum_base_point_rem_res_from: float | Unset = UNSET,
    sum_base_point_rem_res_to: float | Unset = UNSET,
    sum_hasl_rem_res_from: float | Unset = UNSET,
    sum_hasl_rem_res_to: float | Unset = UNSET,
    sum_lasl_rem_res_from: float | Unset = UNSET,
    sum_lasl_rem_res_to: float | Unset = UNSET,
    sum_gen_telem_mw_from: float | Unset = UNSET,
    sum_gen_telem_mw_to: float | Unset = UNSET,
    page: int | Unset = UNSET,
    size: int | Unset = UNSET,
    sort: str | Unset = UNSET,
    dir_: str | Unset = UNSET,
) -> Exception_ | Report | None:
    """2 Day Aggregated Generation Summary Houston

     2 Day Aggregated Generation Summary Houston

    Args:
        sced_timestamp_from (str | Unset):
        sced_timestamp_to (str | Unset):
        repeat_hour_flag (bool | Unset):
        sum_base_point_non_wgr_from (float | Unset):
        sum_base_point_non_wgr_to (float | Unset):
        sum_hasl_non_wgr_from (float | Unset):
        sum_hasl_non_wgr_to (float | Unset):
        sum_lasl_non_wgr_from (float | Unset):
        sum_lasl_non_wgr_to (float | Unset):
        sum_base_point_wgr_from (float | Unset):
        sum_base_point_wgr_to (float | Unset):
        sum_hasl_wgr_from (float | Unset):
        sum_hasl_wgr_to (float | Unset):
        sum_lasl_wgr_from (float | Unset):
        sum_lasl_wgr_to (float | Unset):
        sum_base_point_rem_res_from (float | Unset):
        sum_base_point_rem_res_to (float | Unset):
        sum_hasl_rem_res_from (float | Unset):
        sum_hasl_rem_res_to (float | Unset):
        sum_lasl_rem_res_from (float | Unset):
        sum_lasl_rem_res_to (float | Unset):
        sum_gen_telem_mw_from (float | Unset):
        sum_gen_telem_mw_to (float | Unset):
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
            sum_base_point_non_wgr_from=sum_base_point_non_wgr_from,
            sum_base_point_non_wgr_to=sum_base_point_non_wgr_to,
            sum_hasl_non_wgr_from=sum_hasl_non_wgr_from,
            sum_hasl_non_wgr_to=sum_hasl_non_wgr_to,
            sum_lasl_non_wgr_from=sum_lasl_non_wgr_from,
            sum_lasl_non_wgr_to=sum_lasl_non_wgr_to,
            sum_base_point_wgr_from=sum_base_point_wgr_from,
            sum_base_point_wgr_to=sum_base_point_wgr_to,
            sum_hasl_wgr_from=sum_hasl_wgr_from,
            sum_hasl_wgr_to=sum_hasl_wgr_to,
            sum_lasl_wgr_from=sum_lasl_wgr_from,
            sum_lasl_wgr_to=sum_lasl_wgr_to,
            sum_base_point_rem_res_from=sum_base_point_rem_res_from,
            sum_base_point_rem_res_to=sum_base_point_rem_res_to,
            sum_hasl_rem_res_from=sum_hasl_rem_res_from,
            sum_hasl_rem_res_to=sum_hasl_rem_res_to,
            sum_lasl_rem_res_from=sum_lasl_rem_res_from,
            sum_lasl_rem_res_to=sum_lasl_rem_res_to,
            sum_gen_telem_mw_from=sum_gen_telem_mw_from,
            sum_gen_telem_mw_to=sum_gen_telem_mw_to,
            page=page,
            size=size,
            sort=sort,
            dir_=dir_,
        )
    ).parsed
