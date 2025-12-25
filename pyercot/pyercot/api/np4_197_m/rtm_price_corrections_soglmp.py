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
    sced_timestamp_from: str | Unset = UNSET,
    sced_timestamp_to: str | Unset = UNSET,
    resource_type: str | Unset = UNSET,
    resource_name: str | Unset = UNSET,
    meter_name: str | Unset = UNSET,
    meter_lmp_original_from: float | Unset = UNSET,
    meter_lmp_original_to: float | Unset = UNSET,
    meter_lmp_corrected_from: float | Unset = UNSET,
    meter_lmp_corrected_to: float | Unset = UNSET,
    rtorpa_original_from: float | Unset = UNSET,
    rtorpa_original_to: float | Unset = UNSET,
    rtorpa_corrected_from: float | Unset = UNSET,
    rtorpa_corrected_to: float | Unset = UNSET,
    rtordpa_original_from: float | Unset = UNSET,
    rtordpa_original_to: float | Unset = UNSET,
    rtordpa_corrected_from: float | Unset = UNSET,
    rtordpa_corrected_to: float | Unset = UNSET,
    final_lmp_original_from: float | Unset = UNSET,
    final_lmp_original_to: float | Unset = UNSET,
    final_lmp_corrected_from: float | Unset = UNSET,
    final_lmp_corrected_to: float | Unset = UNSET,
    price_correction_time_from: str | Unset = UNSET,
    price_correction_time_to: str | Unset = UNSET,
    page: int | Unset = UNSET,
    size: int | Unset = UNSET,
    sort: str | Unset = UNSET,
    dir_: str | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["DSTFlag"] = dst_flag

    params["SCEDTimestampFrom"] = sced_timestamp_from

    params["SCEDTimestampTo"] = sced_timestamp_to

    params["resourceType"] = resource_type

    params["resourceName"] = resource_name

    params["meterName"] = meter_name

    params["meterLMPOriginalFrom"] = meter_lmp_original_from

    params["meterLMPOriginalTo"] = meter_lmp_original_to

    params["meterLMPCorrectedFrom"] = meter_lmp_corrected_from

    params["meterLMPCorrectedTo"] = meter_lmp_corrected_to

    params["RTORPAOriginalFrom"] = rtorpa_original_from

    params["RTORPAOriginalTo"] = rtorpa_original_to

    params["RTORPACorrectedFrom"] = rtorpa_corrected_from

    params["RTORPACorrectedTo"] = rtorpa_corrected_to

    params["RTORDPAOriginalFrom"] = rtordpa_original_from

    params["RTORDPAOriginalTo"] = rtordpa_original_to

    params["RTORDPACorrectedFrom"] = rtordpa_corrected_from

    params["RTORDPACorrectedTo"] = rtordpa_corrected_to

    params["finalLMPOriginalFrom"] = final_lmp_original_from

    params["finalLMPOriginalTo"] = final_lmp_original_to

    params["finalLMPCorrectedFrom"] = final_lmp_corrected_from

    params["finalLMPCorrectedTo"] = final_lmp_corrected_to

    params["priceCorrectionTimeFrom"] = price_correction_time_from

    params["priceCorrectionTimeTo"] = price_correction_time_to

    params["page"] = page

    params["size"] = size

    params["sort"] = sort

    params["dir"] = dir_

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/np4-197-m/rtm_price_corrections_soglmp",
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
    sced_timestamp_from: str | Unset = UNSET,
    sced_timestamp_to: str | Unset = UNSET,
    resource_type: str | Unset = UNSET,
    resource_name: str | Unset = UNSET,
    meter_name: str | Unset = UNSET,
    meter_lmp_original_from: float | Unset = UNSET,
    meter_lmp_original_to: float | Unset = UNSET,
    meter_lmp_corrected_from: float | Unset = UNSET,
    meter_lmp_corrected_to: float | Unset = UNSET,
    rtorpa_original_from: float | Unset = UNSET,
    rtorpa_original_to: float | Unset = UNSET,
    rtorpa_corrected_from: float | Unset = UNSET,
    rtorpa_corrected_to: float | Unset = UNSET,
    rtordpa_original_from: float | Unset = UNSET,
    rtordpa_original_to: float | Unset = UNSET,
    rtordpa_corrected_from: float | Unset = UNSET,
    rtordpa_corrected_to: float | Unset = UNSET,
    final_lmp_original_from: float | Unset = UNSET,
    final_lmp_original_to: float | Unset = UNSET,
    final_lmp_corrected_from: float | Unset = UNSET,
    final_lmp_corrected_to: float | Unset = UNSET,
    price_correction_time_from: str | Unset = UNSET,
    price_correction_time_to: str | Unset = UNSET,
    page: int | Unset = UNSET,
    size: int | Unset = UNSET,
    sort: str | Unset = UNSET,
    dir_: str | Unset = UNSET,
) -> Response[Exception_ | Report]:
    """RTM Price Corrections for SOG LMP

     RTM Price Corrections for SOG LMP

    Args:
        dst_flag (bool | Unset):
        sced_timestamp_from (str | Unset):
        sced_timestamp_to (str | Unset):
        resource_type (str | Unset):
        resource_name (str | Unset):
        meter_name (str | Unset):
        meter_lmp_original_from (float | Unset):
        meter_lmp_original_to (float | Unset):
        meter_lmp_corrected_from (float | Unset):
        meter_lmp_corrected_to (float | Unset):
        rtorpa_original_from (float | Unset):
        rtorpa_original_to (float | Unset):
        rtorpa_corrected_from (float | Unset):
        rtorpa_corrected_to (float | Unset):
        rtordpa_original_from (float | Unset):
        rtordpa_original_to (float | Unset):
        rtordpa_corrected_from (float | Unset):
        rtordpa_corrected_to (float | Unset):
        final_lmp_original_from (float | Unset):
        final_lmp_original_to (float | Unset):
        final_lmp_corrected_from (float | Unset):
        final_lmp_corrected_to (float | Unset):
        price_correction_time_from (str | Unset):
        price_correction_time_to (str | Unset):
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
        sced_timestamp_from=sced_timestamp_from,
        sced_timestamp_to=sced_timestamp_to,
        resource_type=resource_type,
        resource_name=resource_name,
        meter_name=meter_name,
        meter_lmp_original_from=meter_lmp_original_from,
        meter_lmp_original_to=meter_lmp_original_to,
        meter_lmp_corrected_from=meter_lmp_corrected_from,
        meter_lmp_corrected_to=meter_lmp_corrected_to,
        rtorpa_original_from=rtorpa_original_from,
        rtorpa_original_to=rtorpa_original_to,
        rtorpa_corrected_from=rtorpa_corrected_from,
        rtorpa_corrected_to=rtorpa_corrected_to,
        rtordpa_original_from=rtordpa_original_from,
        rtordpa_original_to=rtordpa_original_to,
        rtordpa_corrected_from=rtordpa_corrected_from,
        rtordpa_corrected_to=rtordpa_corrected_to,
        final_lmp_original_from=final_lmp_original_from,
        final_lmp_original_to=final_lmp_original_to,
        final_lmp_corrected_from=final_lmp_corrected_from,
        final_lmp_corrected_to=final_lmp_corrected_to,
        price_correction_time_from=price_correction_time_from,
        price_correction_time_to=price_correction_time_to,
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
    sced_timestamp_from: str | Unset = UNSET,
    sced_timestamp_to: str | Unset = UNSET,
    resource_type: str | Unset = UNSET,
    resource_name: str | Unset = UNSET,
    meter_name: str | Unset = UNSET,
    meter_lmp_original_from: float | Unset = UNSET,
    meter_lmp_original_to: float | Unset = UNSET,
    meter_lmp_corrected_from: float | Unset = UNSET,
    meter_lmp_corrected_to: float | Unset = UNSET,
    rtorpa_original_from: float | Unset = UNSET,
    rtorpa_original_to: float | Unset = UNSET,
    rtorpa_corrected_from: float | Unset = UNSET,
    rtorpa_corrected_to: float | Unset = UNSET,
    rtordpa_original_from: float | Unset = UNSET,
    rtordpa_original_to: float | Unset = UNSET,
    rtordpa_corrected_from: float | Unset = UNSET,
    rtordpa_corrected_to: float | Unset = UNSET,
    final_lmp_original_from: float | Unset = UNSET,
    final_lmp_original_to: float | Unset = UNSET,
    final_lmp_corrected_from: float | Unset = UNSET,
    final_lmp_corrected_to: float | Unset = UNSET,
    price_correction_time_from: str | Unset = UNSET,
    price_correction_time_to: str | Unset = UNSET,
    page: int | Unset = UNSET,
    size: int | Unset = UNSET,
    sort: str | Unset = UNSET,
    dir_: str | Unset = UNSET,
) -> Exception_ | Report | None:
    """RTM Price Corrections for SOG LMP

     RTM Price Corrections for SOG LMP

    Args:
        dst_flag (bool | Unset):
        sced_timestamp_from (str | Unset):
        sced_timestamp_to (str | Unset):
        resource_type (str | Unset):
        resource_name (str | Unset):
        meter_name (str | Unset):
        meter_lmp_original_from (float | Unset):
        meter_lmp_original_to (float | Unset):
        meter_lmp_corrected_from (float | Unset):
        meter_lmp_corrected_to (float | Unset):
        rtorpa_original_from (float | Unset):
        rtorpa_original_to (float | Unset):
        rtorpa_corrected_from (float | Unset):
        rtorpa_corrected_to (float | Unset):
        rtordpa_original_from (float | Unset):
        rtordpa_original_to (float | Unset):
        rtordpa_corrected_from (float | Unset):
        rtordpa_corrected_to (float | Unset):
        final_lmp_original_from (float | Unset):
        final_lmp_original_to (float | Unset):
        final_lmp_corrected_from (float | Unset):
        final_lmp_corrected_to (float | Unset):
        price_correction_time_from (str | Unset):
        price_correction_time_to (str | Unset):
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
        sced_timestamp_from=sced_timestamp_from,
        sced_timestamp_to=sced_timestamp_to,
        resource_type=resource_type,
        resource_name=resource_name,
        meter_name=meter_name,
        meter_lmp_original_from=meter_lmp_original_from,
        meter_lmp_original_to=meter_lmp_original_to,
        meter_lmp_corrected_from=meter_lmp_corrected_from,
        meter_lmp_corrected_to=meter_lmp_corrected_to,
        rtorpa_original_from=rtorpa_original_from,
        rtorpa_original_to=rtorpa_original_to,
        rtorpa_corrected_from=rtorpa_corrected_from,
        rtorpa_corrected_to=rtorpa_corrected_to,
        rtordpa_original_from=rtordpa_original_from,
        rtordpa_original_to=rtordpa_original_to,
        rtordpa_corrected_from=rtordpa_corrected_from,
        rtordpa_corrected_to=rtordpa_corrected_to,
        final_lmp_original_from=final_lmp_original_from,
        final_lmp_original_to=final_lmp_original_to,
        final_lmp_corrected_from=final_lmp_corrected_from,
        final_lmp_corrected_to=final_lmp_corrected_to,
        price_correction_time_from=price_correction_time_from,
        price_correction_time_to=price_correction_time_to,
        page=page,
        size=size,
        sort=sort,
        dir_=dir_,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    dst_flag: bool | Unset = UNSET,
    sced_timestamp_from: str | Unset = UNSET,
    sced_timestamp_to: str | Unset = UNSET,
    resource_type: str | Unset = UNSET,
    resource_name: str | Unset = UNSET,
    meter_name: str | Unset = UNSET,
    meter_lmp_original_from: float | Unset = UNSET,
    meter_lmp_original_to: float | Unset = UNSET,
    meter_lmp_corrected_from: float | Unset = UNSET,
    meter_lmp_corrected_to: float | Unset = UNSET,
    rtorpa_original_from: float | Unset = UNSET,
    rtorpa_original_to: float | Unset = UNSET,
    rtorpa_corrected_from: float | Unset = UNSET,
    rtorpa_corrected_to: float | Unset = UNSET,
    rtordpa_original_from: float | Unset = UNSET,
    rtordpa_original_to: float | Unset = UNSET,
    rtordpa_corrected_from: float | Unset = UNSET,
    rtordpa_corrected_to: float | Unset = UNSET,
    final_lmp_original_from: float | Unset = UNSET,
    final_lmp_original_to: float | Unset = UNSET,
    final_lmp_corrected_from: float | Unset = UNSET,
    final_lmp_corrected_to: float | Unset = UNSET,
    price_correction_time_from: str | Unset = UNSET,
    price_correction_time_to: str | Unset = UNSET,
    page: int | Unset = UNSET,
    size: int | Unset = UNSET,
    sort: str | Unset = UNSET,
    dir_: str | Unset = UNSET,
) -> Response[Exception_ | Report]:
    """RTM Price Corrections for SOG LMP

     RTM Price Corrections for SOG LMP

    Args:
        dst_flag (bool | Unset):
        sced_timestamp_from (str | Unset):
        sced_timestamp_to (str | Unset):
        resource_type (str | Unset):
        resource_name (str | Unset):
        meter_name (str | Unset):
        meter_lmp_original_from (float | Unset):
        meter_lmp_original_to (float | Unset):
        meter_lmp_corrected_from (float | Unset):
        meter_lmp_corrected_to (float | Unset):
        rtorpa_original_from (float | Unset):
        rtorpa_original_to (float | Unset):
        rtorpa_corrected_from (float | Unset):
        rtorpa_corrected_to (float | Unset):
        rtordpa_original_from (float | Unset):
        rtordpa_original_to (float | Unset):
        rtordpa_corrected_from (float | Unset):
        rtordpa_corrected_to (float | Unset):
        final_lmp_original_from (float | Unset):
        final_lmp_original_to (float | Unset):
        final_lmp_corrected_from (float | Unset):
        final_lmp_corrected_to (float | Unset):
        price_correction_time_from (str | Unset):
        price_correction_time_to (str | Unset):
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
        sced_timestamp_from=sced_timestamp_from,
        sced_timestamp_to=sced_timestamp_to,
        resource_type=resource_type,
        resource_name=resource_name,
        meter_name=meter_name,
        meter_lmp_original_from=meter_lmp_original_from,
        meter_lmp_original_to=meter_lmp_original_to,
        meter_lmp_corrected_from=meter_lmp_corrected_from,
        meter_lmp_corrected_to=meter_lmp_corrected_to,
        rtorpa_original_from=rtorpa_original_from,
        rtorpa_original_to=rtorpa_original_to,
        rtorpa_corrected_from=rtorpa_corrected_from,
        rtorpa_corrected_to=rtorpa_corrected_to,
        rtordpa_original_from=rtordpa_original_from,
        rtordpa_original_to=rtordpa_original_to,
        rtordpa_corrected_from=rtordpa_corrected_from,
        rtordpa_corrected_to=rtordpa_corrected_to,
        final_lmp_original_from=final_lmp_original_from,
        final_lmp_original_to=final_lmp_original_to,
        final_lmp_corrected_from=final_lmp_corrected_from,
        final_lmp_corrected_to=final_lmp_corrected_to,
        price_correction_time_from=price_correction_time_from,
        price_correction_time_to=price_correction_time_to,
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
    sced_timestamp_from: str | Unset = UNSET,
    sced_timestamp_to: str | Unset = UNSET,
    resource_type: str | Unset = UNSET,
    resource_name: str | Unset = UNSET,
    meter_name: str | Unset = UNSET,
    meter_lmp_original_from: float | Unset = UNSET,
    meter_lmp_original_to: float | Unset = UNSET,
    meter_lmp_corrected_from: float | Unset = UNSET,
    meter_lmp_corrected_to: float | Unset = UNSET,
    rtorpa_original_from: float | Unset = UNSET,
    rtorpa_original_to: float | Unset = UNSET,
    rtorpa_corrected_from: float | Unset = UNSET,
    rtorpa_corrected_to: float | Unset = UNSET,
    rtordpa_original_from: float | Unset = UNSET,
    rtordpa_original_to: float | Unset = UNSET,
    rtordpa_corrected_from: float | Unset = UNSET,
    rtordpa_corrected_to: float | Unset = UNSET,
    final_lmp_original_from: float | Unset = UNSET,
    final_lmp_original_to: float | Unset = UNSET,
    final_lmp_corrected_from: float | Unset = UNSET,
    final_lmp_corrected_to: float | Unset = UNSET,
    price_correction_time_from: str | Unset = UNSET,
    price_correction_time_to: str | Unset = UNSET,
    page: int | Unset = UNSET,
    size: int | Unset = UNSET,
    sort: str | Unset = UNSET,
    dir_: str | Unset = UNSET,
) -> Exception_ | Report | None:
    """RTM Price Corrections for SOG LMP

     RTM Price Corrections for SOG LMP

    Args:
        dst_flag (bool | Unset):
        sced_timestamp_from (str | Unset):
        sced_timestamp_to (str | Unset):
        resource_type (str | Unset):
        resource_name (str | Unset):
        meter_name (str | Unset):
        meter_lmp_original_from (float | Unset):
        meter_lmp_original_to (float | Unset):
        meter_lmp_corrected_from (float | Unset):
        meter_lmp_corrected_to (float | Unset):
        rtorpa_original_from (float | Unset):
        rtorpa_original_to (float | Unset):
        rtorpa_corrected_from (float | Unset):
        rtorpa_corrected_to (float | Unset):
        rtordpa_original_from (float | Unset):
        rtordpa_original_to (float | Unset):
        rtordpa_corrected_from (float | Unset):
        rtordpa_corrected_to (float | Unset):
        final_lmp_original_from (float | Unset):
        final_lmp_original_to (float | Unset):
        final_lmp_corrected_from (float | Unset):
        final_lmp_corrected_to (float | Unset):
        price_correction_time_from (str | Unset):
        price_correction_time_to (str | Unset):
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
            sced_timestamp_from=sced_timestamp_from,
            sced_timestamp_to=sced_timestamp_to,
            resource_type=resource_type,
            resource_name=resource_name,
            meter_name=meter_name,
            meter_lmp_original_from=meter_lmp_original_from,
            meter_lmp_original_to=meter_lmp_original_to,
            meter_lmp_corrected_from=meter_lmp_corrected_from,
            meter_lmp_corrected_to=meter_lmp_corrected_to,
            rtorpa_original_from=rtorpa_original_from,
            rtorpa_original_to=rtorpa_original_to,
            rtorpa_corrected_from=rtorpa_corrected_from,
            rtorpa_corrected_to=rtorpa_corrected_to,
            rtordpa_original_from=rtordpa_original_from,
            rtordpa_original_to=rtordpa_original_to,
            rtordpa_corrected_from=rtordpa_corrected_from,
            rtordpa_corrected_to=rtordpa_corrected_to,
            final_lmp_original_from=final_lmp_original_from,
            final_lmp_original_to=final_lmp_original_to,
            final_lmp_corrected_from=final_lmp_corrected_from,
            final_lmp_corrected_to=final_lmp_corrected_to,
            price_correction_time_from=price_correction_time_from,
            price_correction_time_to=price_correction_time_to,
            page=page,
            size=size,
            sort=sort,
            dir_=dir_,
        )
    ).parsed
