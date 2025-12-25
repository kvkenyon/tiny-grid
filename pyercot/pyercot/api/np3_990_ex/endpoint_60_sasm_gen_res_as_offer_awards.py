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
    sasm_id_from: str | Unset = UNSET,
    sasm_id_to: str | Unset = UNSET,
    delivery_date_from: str | Unset = UNSET,
    delivery_date_to: str | Unset = UNSET,
    hour_ending_from: int | Unset = UNSET,
    hour_ending_to: int | Unset = UNSET,
    resource_name: str | Unset = UNSET,
    resource_type: str | Unset = UNSET,
    regup_aawarded_from: float | Unset = UNSET,
    regup_aawarded_to: float | Unset = UNSET,
    regupmcpc_from: float | Unset = UNSET,
    regupmcpc_to: float | Unset = UNSET,
    regdn_awarded_from: float | Unset = UNSET,
    regdn_awarded_to: float | Unset = UNSET,
    regdnmcpc_from: float | Unset = UNSET,
    regdnmcpc_to: float | Unset = UNSET,
    rrspfr_awarded_from: float | Unset = UNSET,
    rrspfr_awarded_to: float | Unset = UNSET,
    rrsffr_awarded_from: float | Unset = UNSET,
    rrsffr_awarded_to: float | Unset = UNSET,
    rrsufr_awarded_from: float | Unset = UNSET,
    rrsufr_awarded_to: float | Unset = UNSET,
    rrsmcpc_from: float | Unset = UNSET,
    rrsmcpc_to: float | Unset = UNSET,
    nspin_awarded_from: float | Unset = UNSET,
    nspin_awarded_to: float | Unset = UNSET,
    nspinmcpc_from: float | Unset = UNSET,
    nspinmcpc_to: float | Unset = UNSET,
    page: int | Unset = UNSET,
    size: int | Unset = UNSET,
    sort: str | Unset = UNSET,
    dir_: str | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["SASMIdFrom"] = sasm_id_from

    params["SASMIdTo"] = sasm_id_to

    params["deliveryDateFrom"] = delivery_date_from

    params["deliveryDateTo"] = delivery_date_to

    params["hourEndingFrom"] = hour_ending_from

    params["hourEndingTo"] = hour_ending_to

    params["resourceName"] = resource_name

    params["resourceType"] = resource_type

    params["REGUPAawardedFrom"] = regup_aawarded_from

    params["REGUPAawardedTo"] = regup_aawarded_to

    params["REGUPMCPCFrom"] = regupmcpc_from

    params["REGUPMCPCTo"] = regupmcpc_to

    params["REGDNAwardedFrom"] = regdn_awarded_from

    params["REGDNAwardedTo"] = regdn_awarded_to

    params["REGDNMCPCFrom"] = regdnmcpc_from

    params["REGDNMCPCTo"] = regdnmcpc_to

    params["RRSPFRAwardedFrom"] = rrspfr_awarded_from

    params["RRSPFRAwardedTo"] = rrspfr_awarded_to

    params["RRSFFRAwardedFrom"] = rrsffr_awarded_from

    params["RRSFFRAwardedTo"] = rrsffr_awarded_to

    params["RRSUFRAwardedFrom"] = rrsufr_awarded_from

    params["RRSUFRAwardedTo"] = rrsufr_awarded_to

    params["RRSMCPCFrom"] = rrsmcpc_from

    params["RRSMCPCTo"] = rrsmcpc_to

    params["NSPINAwardedFrom"] = nspin_awarded_from

    params["NSPINAwardedTo"] = nspin_awarded_to

    params["NSPINMCPCFrom"] = nspinmcpc_from

    params["NSPINMCPCTo"] = nspinmcpc_to

    params["page"] = page

    params["size"] = size

    params["sort"] = sort

    params["dir"] = dir_

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/np3-990-ex/60_sasm_gen_res_as_offer_awards",
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
    sasm_id_from: str | Unset = UNSET,
    sasm_id_to: str | Unset = UNSET,
    delivery_date_from: str | Unset = UNSET,
    delivery_date_to: str | Unset = UNSET,
    hour_ending_from: int | Unset = UNSET,
    hour_ending_to: int | Unset = UNSET,
    resource_name: str | Unset = UNSET,
    resource_type: str | Unset = UNSET,
    regup_aawarded_from: float | Unset = UNSET,
    regup_aawarded_to: float | Unset = UNSET,
    regupmcpc_from: float | Unset = UNSET,
    regupmcpc_to: float | Unset = UNSET,
    regdn_awarded_from: float | Unset = UNSET,
    regdn_awarded_to: float | Unset = UNSET,
    regdnmcpc_from: float | Unset = UNSET,
    regdnmcpc_to: float | Unset = UNSET,
    rrspfr_awarded_from: float | Unset = UNSET,
    rrspfr_awarded_to: float | Unset = UNSET,
    rrsffr_awarded_from: float | Unset = UNSET,
    rrsffr_awarded_to: float | Unset = UNSET,
    rrsufr_awarded_from: float | Unset = UNSET,
    rrsufr_awarded_to: float | Unset = UNSET,
    rrsmcpc_from: float | Unset = UNSET,
    rrsmcpc_to: float | Unset = UNSET,
    nspin_awarded_from: float | Unset = UNSET,
    nspin_awarded_to: float | Unset = UNSET,
    nspinmcpc_from: float | Unset = UNSET,
    nspinmcpc_to: float | Unset = UNSET,
    page: int | Unset = UNSET,
    size: int | Unset = UNSET,
    sort: str | Unset = UNSET,
    dir_: str | Unset = UNSET,
) -> Response[Exception_ | Report]:
    """60 Day SASM Generation Resource AS Offer Awards

     60 Day SASM Generation Resource AS Offer Awards

    Args:
        sasm_id_from (str | Unset):
        sasm_id_to (str | Unset):
        delivery_date_from (str | Unset):
        delivery_date_to (str | Unset):
        hour_ending_from (int | Unset):
        hour_ending_to (int | Unset):
        resource_name (str | Unset):
        resource_type (str | Unset):
        regup_aawarded_from (float | Unset):
        regup_aawarded_to (float | Unset):
        regupmcpc_from (float | Unset):
        regupmcpc_to (float | Unset):
        regdn_awarded_from (float | Unset):
        regdn_awarded_to (float | Unset):
        regdnmcpc_from (float | Unset):
        regdnmcpc_to (float | Unset):
        rrspfr_awarded_from (float | Unset):
        rrspfr_awarded_to (float | Unset):
        rrsffr_awarded_from (float | Unset):
        rrsffr_awarded_to (float | Unset):
        rrsufr_awarded_from (float | Unset):
        rrsufr_awarded_to (float | Unset):
        rrsmcpc_from (float | Unset):
        rrsmcpc_to (float | Unset):
        nspin_awarded_from (float | Unset):
        nspin_awarded_to (float | Unset):
        nspinmcpc_from (float | Unset):
        nspinmcpc_to (float | Unset):
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
        sasm_id_from=sasm_id_from,
        sasm_id_to=sasm_id_to,
        delivery_date_from=delivery_date_from,
        delivery_date_to=delivery_date_to,
        hour_ending_from=hour_ending_from,
        hour_ending_to=hour_ending_to,
        resource_name=resource_name,
        resource_type=resource_type,
        regup_aawarded_from=regup_aawarded_from,
        regup_aawarded_to=regup_aawarded_to,
        regupmcpc_from=regupmcpc_from,
        regupmcpc_to=regupmcpc_to,
        regdn_awarded_from=regdn_awarded_from,
        regdn_awarded_to=regdn_awarded_to,
        regdnmcpc_from=regdnmcpc_from,
        regdnmcpc_to=regdnmcpc_to,
        rrspfr_awarded_from=rrspfr_awarded_from,
        rrspfr_awarded_to=rrspfr_awarded_to,
        rrsffr_awarded_from=rrsffr_awarded_from,
        rrsffr_awarded_to=rrsffr_awarded_to,
        rrsufr_awarded_from=rrsufr_awarded_from,
        rrsufr_awarded_to=rrsufr_awarded_to,
        rrsmcpc_from=rrsmcpc_from,
        rrsmcpc_to=rrsmcpc_to,
        nspin_awarded_from=nspin_awarded_from,
        nspin_awarded_to=nspin_awarded_to,
        nspinmcpc_from=nspinmcpc_from,
        nspinmcpc_to=nspinmcpc_to,
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
    sasm_id_from: str | Unset = UNSET,
    sasm_id_to: str | Unset = UNSET,
    delivery_date_from: str | Unset = UNSET,
    delivery_date_to: str | Unset = UNSET,
    hour_ending_from: int | Unset = UNSET,
    hour_ending_to: int | Unset = UNSET,
    resource_name: str | Unset = UNSET,
    resource_type: str | Unset = UNSET,
    regup_aawarded_from: float | Unset = UNSET,
    regup_aawarded_to: float | Unset = UNSET,
    regupmcpc_from: float | Unset = UNSET,
    regupmcpc_to: float | Unset = UNSET,
    regdn_awarded_from: float | Unset = UNSET,
    regdn_awarded_to: float | Unset = UNSET,
    regdnmcpc_from: float | Unset = UNSET,
    regdnmcpc_to: float | Unset = UNSET,
    rrspfr_awarded_from: float | Unset = UNSET,
    rrspfr_awarded_to: float | Unset = UNSET,
    rrsffr_awarded_from: float | Unset = UNSET,
    rrsffr_awarded_to: float | Unset = UNSET,
    rrsufr_awarded_from: float | Unset = UNSET,
    rrsufr_awarded_to: float | Unset = UNSET,
    rrsmcpc_from: float | Unset = UNSET,
    rrsmcpc_to: float | Unset = UNSET,
    nspin_awarded_from: float | Unset = UNSET,
    nspin_awarded_to: float | Unset = UNSET,
    nspinmcpc_from: float | Unset = UNSET,
    nspinmcpc_to: float | Unset = UNSET,
    page: int | Unset = UNSET,
    size: int | Unset = UNSET,
    sort: str | Unset = UNSET,
    dir_: str | Unset = UNSET,
) -> Exception_ | Report | None:
    """60 Day SASM Generation Resource AS Offer Awards

     60 Day SASM Generation Resource AS Offer Awards

    Args:
        sasm_id_from (str | Unset):
        sasm_id_to (str | Unset):
        delivery_date_from (str | Unset):
        delivery_date_to (str | Unset):
        hour_ending_from (int | Unset):
        hour_ending_to (int | Unset):
        resource_name (str | Unset):
        resource_type (str | Unset):
        regup_aawarded_from (float | Unset):
        regup_aawarded_to (float | Unset):
        regupmcpc_from (float | Unset):
        regupmcpc_to (float | Unset):
        regdn_awarded_from (float | Unset):
        regdn_awarded_to (float | Unset):
        regdnmcpc_from (float | Unset):
        regdnmcpc_to (float | Unset):
        rrspfr_awarded_from (float | Unset):
        rrspfr_awarded_to (float | Unset):
        rrsffr_awarded_from (float | Unset):
        rrsffr_awarded_to (float | Unset):
        rrsufr_awarded_from (float | Unset):
        rrsufr_awarded_to (float | Unset):
        rrsmcpc_from (float | Unset):
        rrsmcpc_to (float | Unset):
        nspin_awarded_from (float | Unset):
        nspin_awarded_to (float | Unset):
        nspinmcpc_from (float | Unset):
        nspinmcpc_to (float | Unset):
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
        sasm_id_from=sasm_id_from,
        sasm_id_to=sasm_id_to,
        delivery_date_from=delivery_date_from,
        delivery_date_to=delivery_date_to,
        hour_ending_from=hour_ending_from,
        hour_ending_to=hour_ending_to,
        resource_name=resource_name,
        resource_type=resource_type,
        regup_aawarded_from=regup_aawarded_from,
        regup_aawarded_to=regup_aawarded_to,
        regupmcpc_from=regupmcpc_from,
        regupmcpc_to=regupmcpc_to,
        regdn_awarded_from=regdn_awarded_from,
        regdn_awarded_to=regdn_awarded_to,
        regdnmcpc_from=regdnmcpc_from,
        regdnmcpc_to=regdnmcpc_to,
        rrspfr_awarded_from=rrspfr_awarded_from,
        rrspfr_awarded_to=rrspfr_awarded_to,
        rrsffr_awarded_from=rrsffr_awarded_from,
        rrsffr_awarded_to=rrsffr_awarded_to,
        rrsufr_awarded_from=rrsufr_awarded_from,
        rrsufr_awarded_to=rrsufr_awarded_to,
        rrsmcpc_from=rrsmcpc_from,
        rrsmcpc_to=rrsmcpc_to,
        nspin_awarded_from=nspin_awarded_from,
        nspin_awarded_to=nspin_awarded_to,
        nspinmcpc_from=nspinmcpc_from,
        nspinmcpc_to=nspinmcpc_to,
        page=page,
        size=size,
        sort=sort,
        dir_=dir_,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    sasm_id_from: str | Unset = UNSET,
    sasm_id_to: str | Unset = UNSET,
    delivery_date_from: str | Unset = UNSET,
    delivery_date_to: str | Unset = UNSET,
    hour_ending_from: int | Unset = UNSET,
    hour_ending_to: int | Unset = UNSET,
    resource_name: str | Unset = UNSET,
    resource_type: str | Unset = UNSET,
    regup_aawarded_from: float | Unset = UNSET,
    regup_aawarded_to: float | Unset = UNSET,
    regupmcpc_from: float | Unset = UNSET,
    regupmcpc_to: float | Unset = UNSET,
    regdn_awarded_from: float | Unset = UNSET,
    regdn_awarded_to: float | Unset = UNSET,
    regdnmcpc_from: float | Unset = UNSET,
    regdnmcpc_to: float | Unset = UNSET,
    rrspfr_awarded_from: float | Unset = UNSET,
    rrspfr_awarded_to: float | Unset = UNSET,
    rrsffr_awarded_from: float | Unset = UNSET,
    rrsffr_awarded_to: float | Unset = UNSET,
    rrsufr_awarded_from: float | Unset = UNSET,
    rrsufr_awarded_to: float | Unset = UNSET,
    rrsmcpc_from: float | Unset = UNSET,
    rrsmcpc_to: float | Unset = UNSET,
    nspin_awarded_from: float | Unset = UNSET,
    nspin_awarded_to: float | Unset = UNSET,
    nspinmcpc_from: float | Unset = UNSET,
    nspinmcpc_to: float | Unset = UNSET,
    page: int | Unset = UNSET,
    size: int | Unset = UNSET,
    sort: str | Unset = UNSET,
    dir_: str | Unset = UNSET,
) -> Response[Exception_ | Report]:
    """60 Day SASM Generation Resource AS Offer Awards

     60 Day SASM Generation Resource AS Offer Awards

    Args:
        sasm_id_from (str | Unset):
        sasm_id_to (str | Unset):
        delivery_date_from (str | Unset):
        delivery_date_to (str | Unset):
        hour_ending_from (int | Unset):
        hour_ending_to (int | Unset):
        resource_name (str | Unset):
        resource_type (str | Unset):
        regup_aawarded_from (float | Unset):
        regup_aawarded_to (float | Unset):
        regupmcpc_from (float | Unset):
        regupmcpc_to (float | Unset):
        regdn_awarded_from (float | Unset):
        regdn_awarded_to (float | Unset):
        regdnmcpc_from (float | Unset):
        regdnmcpc_to (float | Unset):
        rrspfr_awarded_from (float | Unset):
        rrspfr_awarded_to (float | Unset):
        rrsffr_awarded_from (float | Unset):
        rrsffr_awarded_to (float | Unset):
        rrsufr_awarded_from (float | Unset):
        rrsufr_awarded_to (float | Unset):
        rrsmcpc_from (float | Unset):
        rrsmcpc_to (float | Unset):
        nspin_awarded_from (float | Unset):
        nspin_awarded_to (float | Unset):
        nspinmcpc_from (float | Unset):
        nspinmcpc_to (float | Unset):
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
        sasm_id_from=sasm_id_from,
        sasm_id_to=sasm_id_to,
        delivery_date_from=delivery_date_from,
        delivery_date_to=delivery_date_to,
        hour_ending_from=hour_ending_from,
        hour_ending_to=hour_ending_to,
        resource_name=resource_name,
        resource_type=resource_type,
        regup_aawarded_from=regup_aawarded_from,
        regup_aawarded_to=regup_aawarded_to,
        regupmcpc_from=regupmcpc_from,
        regupmcpc_to=regupmcpc_to,
        regdn_awarded_from=regdn_awarded_from,
        regdn_awarded_to=regdn_awarded_to,
        regdnmcpc_from=regdnmcpc_from,
        regdnmcpc_to=regdnmcpc_to,
        rrspfr_awarded_from=rrspfr_awarded_from,
        rrspfr_awarded_to=rrspfr_awarded_to,
        rrsffr_awarded_from=rrsffr_awarded_from,
        rrsffr_awarded_to=rrsffr_awarded_to,
        rrsufr_awarded_from=rrsufr_awarded_from,
        rrsufr_awarded_to=rrsufr_awarded_to,
        rrsmcpc_from=rrsmcpc_from,
        rrsmcpc_to=rrsmcpc_to,
        nspin_awarded_from=nspin_awarded_from,
        nspin_awarded_to=nspin_awarded_to,
        nspinmcpc_from=nspinmcpc_from,
        nspinmcpc_to=nspinmcpc_to,
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
    sasm_id_from: str | Unset = UNSET,
    sasm_id_to: str | Unset = UNSET,
    delivery_date_from: str | Unset = UNSET,
    delivery_date_to: str | Unset = UNSET,
    hour_ending_from: int | Unset = UNSET,
    hour_ending_to: int | Unset = UNSET,
    resource_name: str | Unset = UNSET,
    resource_type: str | Unset = UNSET,
    regup_aawarded_from: float | Unset = UNSET,
    regup_aawarded_to: float | Unset = UNSET,
    regupmcpc_from: float | Unset = UNSET,
    regupmcpc_to: float | Unset = UNSET,
    regdn_awarded_from: float | Unset = UNSET,
    regdn_awarded_to: float | Unset = UNSET,
    regdnmcpc_from: float | Unset = UNSET,
    regdnmcpc_to: float | Unset = UNSET,
    rrspfr_awarded_from: float | Unset = UNSET,
    rrspfr_awarded_to: float | Unset = UNSET,
    rrsffr_awarded_from: float | Unset = UNSET,
    rrsffr_awarded_to: float | Unset = UNSET,
    rrsufr_awarded_from: float | Unset = UNSET,
    rrsufr_awarded_to: float | Unset = UNSET,
    rrsmcpc_from: float | Unset = UNSET,
    rrsmcpc_to: float | Unset = UNSET,
    nspin_awarded_from: float | Unset = UNSET,
    nspin_awarded_to: float | Unset = UNSET,
    nspinmcpc_from: float | Unset = UNSET,
    nspinmcpc_to: float | Unset = UNSET,
    page: int | Unset = UNSET,
    size: int | Unset = UNSET,
    sort: str | Unset = UNSET,
    dir_: str | Unset = UNSET,
) -> Exception_ | Report | None:
    """60 Day SASM Generation Resource AS Offer Awards

     60 Day SASM Generation Resource AS Offer Awards

    Args:
        sasm_id_from (str | Unset):
        sasm_id_to (str | Unset):
        delivery_date_from (str | Unset):
        delivery_date_to (str | Unset):
        hour_ending_from (int | Unset):
        hour_ending_to (int | Unset):
        resource_name (str | Unset):
        resource_type (str | Unset):
        regup_aawarded_from (float | Unset):
        regup_aawarded_to (float | Unset):
        regupmcpc_from (float | Unset):
        regupmcpc_to (float | Unset):
        regdn_awarded_from (float | Unset):
        regdn_awarded_to (float | Unset):
        regdnmcpc_from (float | Unset):
        regdnmcpc_to (float | Unset):
        rrspfr_awarded_from (float | Unset):
        rrspfr_awarded_to (float | Unset):
        rrsffr_awarded_from (float | Unset):
        rrsffr_awarded_to (float | Unset):
        rrsufr_awarded_from (float | Unset):
        rrsufr_awarded_to (float | Unset):
        rrsmcpc_from (float | Unset):
        rrsmcpc_to (float | Unset):
        nspin_awarded_from (float | Unset):
        nspin_awarded_to (float | Unset):
        nspinmcpc_from (float | Unset):
        nspinmcpc_to (float | Unset):
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
            sasm_id_from=sasm_id_from,
            sasm_id_to=sasm_id_to,
            delivery_date_from=delivery_date_from,
            delivery_date_to=delivery_date_to,
            hour_ending_from=hour_ending_from,
            hour_ending_to=hour_ending_to,
            resource_name=resource_name,
            resource_type=resource_type,
            regup_aawarded_from=regup_aawarded_from,
            regup_aawarded_to=regup_aawarded_to,
            regupmcpc_from=regupmcpc_from,
            regupmcpc_to=regupmcpc_to,
            regdn_awarded_from=regdn_awarded_from,
            regdn_awarded_to=regdn_awarded_to,
            regdnmcpc_from=regdnmcpc_from,
            regdnmcpc_to=regdnmcpc_to,
            rrspfr_awarded_from=rrspfr_awarded_from,
            rrspfr_awarded_to=rrspfr_awarded_to,
            rrsffr_awarded_from=rrsffr_awarded_from,
            rrsffr_awarded_to=rrsffr_awarded_to,
            rrsufr_awarded_from=rrsufr_awarded_from,
            rrsufr_awarded_to=rrsufr_awarded_to,
            rrsmcpc_from=rrsmcpc_from,
            rrsmcpc_to=rrsmcpc_to,
            nspin_awarded_from=nspin_awarded_from,
            nspin_awarded_to=nspin_awarded_to,
            nspinmcpc_from=nspinmcpc_from,
            nspinmcpc_to=nspinmcpc_to,
            page=page,
            size=size,
            sort=sort,
            dir_=dir_,
        )
    ).parsed
