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
    settlement_point_name: str | Unset = UNSET,
    lmp_original_from: float | Unset = UNSET,
    lmp_original_to: float | Unset = UNSET,
    lmp_corrected_from: float | Unset = UNSET,
    lmp_corrected_to: float | Unset = UNSET,
    price_correction_time_from: str | Unset = UNSET,
    price_correction_time_to: str | Unset = UNSET,
    dst_flag: bool | Unset = UNSET,
    sced_timestamp_from: str | Unset = UNSET,
    sced_timestamp_to: str | Unset = UNSET,
    page: int | Unset = UNSET,
    size: int | Unset = UNSET,
    sort: str | Unset = UNSET,
    dir_: str | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["settlementPointName"] = settlement_point_name

    params["LMPOriginalFrom"] = lmp_original_from

    params["LMPOriginalTo"] = lmp_original_to

    params["LMPCorrectedFrom"] = lmp_corrected_from

    params["LMPCorrectedTo"] = lmp_corrected_to

    params["priceCorrectionTimeFrom"] = price_correction_time_from

    params["priceCorrectionTimeTo"] = price_correction_time_to

    params["DSTFlag"] = dst_flag

    params["SCEDTimestampFrom"] = sced_timestamp_from

    params["SCEDTimestampTo"] = sced_timestamp_to

    params["page"] = page

    params["size"] = size

    params["sort"] = sort

    params["dir"] = dir_

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/np4-197-m/rtm_price_corrections_splmp",
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
    settlement_point_name: str | Unset = UNSET,
    lmp_original_from: float | Unset = UNSET,
    lmp_original_to: float | Unset = UNSET,
    lmp_corrected_from: float | Unset = UNSET,
    lmp_corrected_to: float | Unset = UNSET,
    price_correction_time_from: str | Unset = UNSET,
    price_correction_time_to: str | Unset = UNSET,
    dst_flag: bool | Unset = UNSET,
    sced_timestamp_from: str | Unset = UNSET,
    sced_timestamp_to: str | Unset = UNSET,
    page: int | Unset = UNSET,
    size: int | Unset = UNSET,
    sort: str | Unset = UNSET,
    dir_: str | Unset = UNSET,
) -> Response[Exception_ | Report]:
    """RTM Price Corrections SP LMP

     RTM Price Corrections SP LMP

    Args:
        settlement_point_name (str | Unset):
        lmp_original_from (float | Unset):
        lmp_original_to (float | Unset):
        lmp_corrected_from (float | Unset):
        lmp_corrected_to (float | Unset):
        price_correction_time_from (str | Unset):
        price_correction_time_to (str | Unset):
        dst_flag (bool | Unset):
        sced_timestamp_from (str | Unset):
        sced_timestamp_to (str | Unset):
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
        settlement_point_name=settlement_point_name,
        lmp_original_from=lmp_original_from,
        lmp_original_to=lmp_original_to,
        lmp_corrected_from=lmp_corrected_from,
        lmp_corrected_to=lmp_corrected_to,
        price_correction_time_from=price_correction_time_from,
        price_correction_time_to=price_correction_time_to,
        dst_flag=dst_flag,
        sced_timestamp_from=sced_timestamp_from,
        sced_timestamp_to=sced_timestamp_to,
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
    settlement_point_name: str | Unset = UNSET,
    lmp_original_from: float | Unset = UNSET,
    lmp_original_to: float | Unset = UNSET,
    lmp_corrected_from: float | Unset = UNSET,
    lmp_corrected_to: float | Unset = UNSET,
    price_correction_time_from: str | Unset = UNSET,
    price_correction_time_to: str | Unset = UNSET,
    dst_flag: bool | Unset = UNSET,
    sced_timestamp_from: str | Unset = UNSET,
    sced_timestamp_to: str | Unset = UNSET,
    page: int | Unset = UNSET,
    size: int | Unset = UNSET,
    sort: str | Unset = UNSET,
    dir_: str | Unset = UNSET,
) -> Exception_ | Report | None:
    """RTM Price Corrections SP LMP

     RTM Price Corrections SP LMP

    Args:
        settlement_point_name (str | Unset):
        lmp_original_from (float | Unset):
        lmp_original_to (float | Unset):
        lmp_corrected_from (float | Unset):
        lmp_corrected_to (float | Unset):
        price_correction_time_from (str | Unset):
        price_correction_time_to (str | Unset):
        dst_flag (bool | Unset):
        sced_timestamp_from (str | Unset):
        sced_timestamp_to (str | Unset):
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
        settlement_point_name=settlement_point_name,
        lmp_original_from=lmp_original_from,
        lmp_original_to=lmp_original_to,
        lmp_corrected_from=lmp_corrected_from,
        lmp_corrected_to=lmp_corrected_to,
        price_correction_time_from=price_correction_time_from,
        price_correction_time_to=price_correction_time_to,
        dst_flag=dst_flag,
        sced_timestamp_from=sced_timestamp_from,
        sced_timestamp_to=sced_timestamp_to,
        page=page,
        size=size,
        sort=sort,
        dir_=dir_,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    settlement_point_name: str | Unset = UNSET,
    lmp_original_from: float | Unset = UNSET,
    lmp_original_to: float | Unset = UNSET,
    lmp_corrected_from: float | Unset = UNSET,
    lmp_corrected_to: float | Unset = UNSET,
    price_correction_time_from: str | Unset = UNSET,
    price_correction_time_to: str | Unset = UNSET,
    dst_flag: bool | Unset = UNSET,
    sced_timestamp_from: str | Unset = UNSET,
    sced_timestamp_to: str | Unset = UNSET,
    page: int | Unset = UNSET,
    size: int | Unset = UNSET,
    sort: str | Unset = UNSET,
    dir_: str | Unset = UNSET,
) -> Response[Exception_ | Report]:
    """RTM Price Corrections SP LMP

     RTM Price Corrections SP LMP

    Args:
        settlement_point_name (str | Unset):
        lmp_original_from (float | Unset):
        lmp_original_to (float | Unset):
        lmp_corrected_from (float | Unset):
        lmp_corrected_to (float | Unset):
        price_correction_time_from (str | Unset):
        price_correction_time_to (str | Unset):
        dst_flag (bool | Unset):
        sced_timestamp_from (str | Unset):
        sced_timestamp_to (str | Unset):
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
        settlement_point_name=settlement_point_name,
        lmp_original_from=lmp_original_from,
        lmp_original_to=lmp_original_to,
        lmp_corrected_from=lmp_corrected_from,
        lmp_corrected_to=lmp_corrected_to,
        price_correction_time_from=price_correction_time_from,
        price_correction_time_to=price_correction_time_to,
        dst_flag=dst_flag,
        sced_timestamp_from=sced_timestamp_from,
        sced_timestamp_to=sced_timestamp_to,
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
    settlement_point_name: str | Unset = UNSET,
    lmp_original_from: float | Unset = UNSET,
    lmp_original_to: float | Unset = UNSET,
    lmp_corrected_from: float | Unset = UNSET,
    lmp_corrected_to: float | Unset = UNSET,
    price_correction_time_from: str | Unset = UNSET,
    price_correction_time_to: str | Unset = UNSET,
    dst_flag: bool | Unset = UNSET,
    sced_timestamp_from: str | Unset = UNSET,
    sced_timestamp_to: str | Unset = UNSET,
    page: int | Unset = UNSET,
    size: int | Unset = UNSET,
    sort: str | Unset = UNSET,
    dir_: str | Unset = UNSET,
) -> Exception_ | Report | None:
    """RTM Price Corrections SP LMP

     RTM Price Corrections SP LMP

    Args:
        settlement_point_name (str | Unset):
        lmp_original_from (float | Unset):
        lmp_original_to (float | Unset):
        lmp_corrected_from (float | Unset):
        lmp_corrected_to (float | Unset):
        price_correction_time_from (str | Unset):
        price_correction_time_to (str | Unset):
        dst_flag (bool | Unset):
        sced_timestamp_from (str | Unset):
        sced_timestamp_to (str | Unset):
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
            settlement_point_name=settlement_point_name,
            lmp_original_from=lmp_original_from,
            lmp_original_to=lmp_original_to,
            lmp_corrected_from=lmp_corrected_from,
            lmp_corrected_to=lmp_corrected_to,
            price_correction_time_from=price_correction_time_from,
            price_correction_time_to=price_correction_time_to,
            dst_flag=dst_flag,
            sced_timestamp_from=sced_timestamp_from,
            sced_timestamp_to=sced_timestamp_to,
            page=page,
            size=size,
            sort=sort,
            dir_=dir_,
        )
    ).parsed
