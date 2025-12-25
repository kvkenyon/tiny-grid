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
    hour_ending: str | Unset = UNSET,
    regdn_from: float | Unset = UNSET,
    regdn_to: float | Unset = UNSET,
    regup_from: float | Unset = UNSET,
    regup_to: float | Unset = UNSET,
    rrspfr_from: float | Unset = UNSET,
    rrspfr_to: float | Unset = UNSET,
    rrsffr_from: float | Unset = UNSET,
    rrsffr_to: float | Unset = UNSET,
    rrsufr_from: float | Unset = UNSET,
    rrsufr_to: float | Unset = UNSET,
    ecrssd_from: float | Unset = UNSET,
    ecrssd_to: float | Unset = UNSET,
    ecrsmd_from: float | Unset = UNSET,
    ecrsmd_to: float | Unset = UNSET,
    nspin_from: float | Unset = UNSET,
    nspin_to: float | Unset = UNSET,
    dst_flag: bool | Unset = UNSET,
    page: int | Unset = UNSET,
    size: int | Unset = UNSET,
    sort: str | Unset = UNSET,
    dir_: str | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["deliveryDateFrom"] = delivery_date_from

    params["deliveryDateTo"] = delivery_date_to

    params["hourEnding"] = hour_ending

    params["REGDNFrom"] = regdn_from

    params["REGDNTo"] = regdn_to

    params["REGUPFrom"] = regup_from

    params["REGUPTo"] = regup_to

    params["RRSPFRFrom"] = rrspfr_from

    params["RRSPFRTo"] = rrspfr_to

    params["RRSFFRFrom"] = rrsffr_from

    params["RRSFFRTo"] = rrsffr_to

    params["RRSUFRFrom"] = rrsufr_from

    params["RRSUFRTo"] = rrsufr_to

    params["ECRSSDFrom"] = ecrssd_from

    params["ECRSSDTo"] = ecrssd_to

    params["ECRSMDFrom"] = ecrsmd_from

    params["ECRSMDTo"] = ecrsmd_to

    params["NSPINFrom"] = nspin_from

    params["NSPINTo"] = nspin_to

    params["DSTFlag"] = dst_flag

    params["page"] = page

    params["size"] = size

    params["sort"] = sort

    params["dir"] = dir_

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/np4-179-cd/total_as_service_offers",
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
    hour_ending: str | Unset = UNSET,
    regdn_from: float | Unset = UNSET,
    regdn_to: float | Unset = UNSET,
    regup_from: float | Unset = UNSET,
    regup_to: float | Unset = UNSET,
    rrspfr_from: float | Unset = UNSET,
    rrspfr_to: float | Unset = UNSET,
    rrsffr_from: float | Unset = UNSET,
    rrsffr_to: float | Unset = UNSET,
    rrsufr_from: float | Unset = UNSET,
    rrsufr_to: float | Unset = UNSET,
    ecrssd_from: float | Unset = UNSET,
    ecrssd_to: float | Unset = UNSET,
    ecrsmd_from: float | Unset = UNSET,
    ecrsmd_to: float | Unset = UNSET,
    nspin_from: float | Unset = UNSET,
    nspin_to: float | Unset = UNSET,
    dst_flag: bool | Unset = UNSET,
    page: int | Unset = UNSET,
    size: int | Unset = UNSET,
    sort: str | Unset = UNSET,
    dir_: str | Unset = UNSET,
) -> Response[Exception_ | Report]:
    """Total Ancillary Service Offers

     Total Ancillary Service Offers

    Args:
        delivery_date_from (str | Unset):
        delivery_date_to (str | Unset):
        hour_ending (str | Unset):
        regdn_from (float | Unset):
        regdn_to (float | Unset):
        regup_from (float | Unset):
        regup_to (float | Unset):
        rrspfr_from (float | Unset):
        rrspfr_to (float | Unset):
        rrsffr_from (float | Unset):
        rrsffr_to (float | Unset):
        rrsufr_from (float | Unset):
        rrsufr_to (float | Unset):
        ecrssd_from (float | Unset):
        ecrssd_to (float | Unset):
        ecrsmd_from (float | Unset):
        ecrsmd_to (float | Unset):
        nspin_from (float | Unset):
        nspin_to (float | Unset):
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
        hour_ending=hour_ending,
        regdn_from=regdn_from,
        regdn_to=regdn_to,
        regup_from=regup_from,
        regup_to=regup_to,
        rrspfr_from=rrspfr_from,
        rrspfr_to=rrspfr_to,
        rrsffr_from=rrsffr_from,
        rrsffr_to=rrsffr_to,
        rrsufr_from=rrsufr_from,
        rrsufr_to=rrsufr_to,
        ecrssd_from=ecrssd_from,
        ecrssd_to=ecrssd_to,
        ecrsmd_from=ecrsmd_from,
        ecrsmd_to=ecrsmd_to,
        nspin_from=nspin_from,
        nspin_to=nspin_to,
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
    hour_ending: str | Unset = UNSET,
    regdn_from: float | Unset = UNSET,
    regdn_to: float | Unset = UNSET,
    regup_from: float | Unset = UNSET,
    regup_to: float | Unset = UNSET,
    rrspfr_from: float | Unset = UNSET,
    rrspfr_to: float | Unset = UNSET,
    rrsffr_from: float | Unset = UNSET,
    rrsffr_to: float | Unset = UNSET,
    rrsufr_from: float | Unset = UNSET,
    rrsufr_to: float | Unset = UNSET,
    ecrssd_from: float | Unset = UNSET,
    ecrssd_to: float | Unset = UNSET,
    ecrsmd_from: float | Unset = UNSET,
    ecrsmd_to: float | Unset = UNSET,
    nspin_from: float | Unset = UNSET,
    nspin_to: float | Unset = UNSET,
    dst_flag: bool | Unset = UNSET,
    page: int | Unset = UNSET,
    size: int | Unset = UNSET,
    sort: str | Unset = UNSET,
    dir_: str | Unset = UNSET,
) -> Exception_ | Report | None:
    """Total Ancillary Service Offers

     Total Ancillary Service Offers

    Args:
        delivery_date_from (str | Unset):
        delivery_date_to (str | Unset):
        hour_ending (str | Unset):
        regdn_from (float | Unset):
        regdn_to (float | Unset):
        regup_from (float | Unset):
        regup_to (float | Unset):
        rrspfr_from (float | Unset):
        rrspfr_to (float | Unset):
        rrsffr_from (float | Unset):
        rrsffr_to (float | Unset):
        rrsufr_from (float | Unset):
        rrsufr_to (float | Unset):
        ecrssd_from (float | Unset):
        ecrssd_to (float | Unset):
        ecrsmd_from (float | Unset):
        ecrsmd_to (float | Unset):
        nspin_from (float | Unset):
        nspin_to (float | Unset):
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
        hour_ending=hour_ending,
        regdn_from=regdn_from,
        regdn_to=regdn_to,
        regup_from=regup_from,
        regup_to=regup_to,
        rrspfr_from=rrspfr_from,
        rrspfr_to=rrspfr_to,
        rrsffr_from=rrsffr_from,
        rrsffr_to=rrsffr_to,
        rrsufr_from=rrsufr_from,
        rrsufr_to=rrsufr_to,
        ecrssd_from=ecrssd_from,
        ecrssd_to=ecrssd_to,
        ecrsmd_from=ecrsmd_from,
        ecrsmd_to=ecrsmd_to,
        nspin_from=nspin_from,
        nspin_to=nspin_to,
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
    hour_ending: str | Unset = UNSET,
    regdn_from: float | Unset = UNSET,
    regdn_to: float | Unset = UNSET,
    regup_from: float | Unset = UNSET,
    regup_to: float | Unset = UNSET,
    rrspfr_from: float | Unset = UNSET,
    rrspfr_to: float | Unset = UNSET,
    rrsffr_from: float | Unset = UNSET,
    rrsffr_to: float | Unset = UNSET,
    rrsufr_from: float | Unset = UNSET,
    rrsufr_to: float | Unset = UNSET,
    ecrssd_from: float | Unset = UNSET,
    ecrssd_to: float | Unset = UNSET,
    ecrsmd_from: float | Unset = UNSET,
    ecrsmd_to: float | Unset = UNSET,
    nspin_from: float | Unset = UNSET,
    nspin_to: float | Unset = UNSET,
    dst_flag: bool | Unset = UNSET,
    page: int | Unset = UNSET,
    size: int | Unset = UNSET,
    sort: str | Unset = UNSET,
    dir_: str | Unset = UNSET,
) -> Response[Exception_ | Report]:
    """Total Ancillary Service Offers

     Total Ancillary Service Offers

    Args:
        delivery_date_from (str | Unset):
        delivery_date_to (str | Unset):
        hour_ending (str | Unset):
        regdn_from (float | Unset):
        regdn_to (float | Unset):
        regup_from (float | Unset):
        regup_to (float | Unset):
        rrspfr_from (float | Unset):
        rrspfr_to (float | Unset):
        rrsffr_from (float | Unset):
        rrsffr_to (float | Unset):
        rrsufr_from (float | Unset):
        rrsufr_to (float | Unset):
        ecrssd_from (float | Unset):
        ecrssd_to (float | Unset):
        ecrsmd_from (float | Unset):
        ecrsmd_to (float | Unset):
        nspin_from (float | Unset):
        nspin_to (float | Unset):
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
        hour_ending=hour_ending,
        regdn_from=regdn_from,
        regdn_to=regdn_to,
        regup_from=regup_from,
        regup_to=regup_to,
        rrspfr_from=rrspfr_from,
        rrspfr_to=rrspfr_to,
        rrsffr_from=rrsffr_from,
        rrsffr_to=rrsffr_to,
        rrsufr_from=rrsufr_from,
        rrsufr_to=rrsufr_to,
        ecrssd_from=ecrssd_from,
        ecrssd_to=ecrssd_to,
        ecrsmd_from=ecrsmd_from,
        ecrsmd_to=ecrsmd_to,
        nspin_from=nspin_from,
        nspin_to=nspin_to,
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
    hour_ending: str | Unset = UNSET,
    regdn_from: float | Unset = UNSET,
    regdn_to: float | Unset = UNSET,
    regup_from: float | Unset = UNSET,
    regup_to: float | Unset = UNSET,
    rrspfr_from: float | Unset = UNSET,
    rrspfr_to: float | Unset = UNSET,
    rrsffr_from: float | Unset = UNSET,
    rrsffr_to: float | Unset = UNSET,
    rrsufr_from: float | Unset = UNSET,
    rrsufr_to: float | Unset = UNSET,
    ecrssd_from: float | Unset = UNSET,
    ecrssd_to: float | Unset = UNSET,
    ecrsmd_from: float | Unset = UNSET,
    ecrsmd_to: float | Unset = UNSET,
    nspin_from: float | Unset = UNSET,
    nspin_to: float | Unset = UNSET,
    dst_flag: bool | Unset = UNSET,
    page: int | Unset = UNSET,
    size: int | Unset = UNSET,
    sort: str | Unset = UNSET,
    dir_: str | Unset = UNSET,
) -> Exception_ | Report | None:
    """Total Ancillary Service Offers

     Total Ancillary Service Offers

    Args:
        delivery_date_from (str | Unset):
        delivery_date_to (str | Unset):
        hour_ending (str | Unset):
        regdn_from (float | Unset):
        regdn_to (float | Unset):
        regup_from (float | Unset):
        regup_to (float | Unset):
        rrspfr_from (float | Unset):
        rrspfr_to (float | Unset):
        rrsffr_from (float | Unset):
        rrsffr_to (float | Unset):
        rrsufr_from (float | Unset):
        rrsufr_to (float | Unset):
        ecrssd_from (float | Unset):
        ecrssd_to (float | Unset):
        ecrsmd_from (float | Unset):
        ecrsmd_to (float | Unset):
        nspin_from (float | Unset):
        nspin_to (float | Unset):
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
            hour_ending=hour_ending,
            regdn_from=regdn_from,
            regdn_to=regdn_to,
            regup_from=regup_from,
            regup_to=regup_to,
            rrspfr_from=rrspfr_from,
            rrspfr_to=rrspfr_to,
            rrsffr_from=rrsffr_from,
            rrsffr_to=rrsffr_to,
            rrsufr_from=rrsufr_from,
            rrsufr_to=rrsufr_to,
            ecrssd_from=ecrssd_from,
            ecrssd_to=ecrssd_to,
            ecrsmd_from=ecrsmd_from,
            ecrsmd_to=ecrsmd_to,
            nspin_from=nspin_from,
            nspin_to=nspin_to,
            dst_flag=dst_flag,
            page=page,
            size=size,
            sort=sort,
            dir_=dir_,
        )
    ).parsed
