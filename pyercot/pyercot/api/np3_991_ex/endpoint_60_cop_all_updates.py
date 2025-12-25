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
    cancel_flag: bool | Unset = UNSET,
    update_time_from: str | Unset = UNSET,
    update_time_to: str | Unset = UNSET,
    submit_time_from: str | Unset = UNSET,
    submit_time_to: str | Unset = UNSET,
    delivery_date_from: str | Unset = UNSET,
    delivery_date_to: str | Unset = UNSET,
    qse_name: str | Unset = UNSET,
    resource_name: str | Unset = UNSET,
    hour_ending: str | Unset = UNSET,
    status: str | Unset = UNSET,
    high_sustained_limit_from: float | Unset = UNSET,
    high_sustained_limit_to: float | Unset = UNSET,
    low_sustained_limit_from: float | Unset = UNSET,
    low_sustained_limit_to: float | Unset = UNSET,
    high_emergency_limit_from: float | Unset = UNSET,
    high_emergency_limit_to: float | Unset = UNSET,
    low_emergency_limit_from: float | Unset = UNSET,
    low_emergency_limit_to: float | Unset = UNSET,
    regup_from: float | Unset = UNSET,
    regup_to: float | Unset = UNSET,
    regdn_from: float | Unset = UNSET,
    regdn_to: float | Unset = UNSET,
    rrspfr_from: float | Unset = UNSET,
    rrspfr_to: float | Unset = UNSET,
    rrsffr_from: float | Unset = UNSET,
    rrsffr_to: float | Unset = UNSET,
    rrsufr_from: float | Unset = UNSET,
    rrsufr_to: float | Unset = UNSET,
    nspin_from: float | Unset = UNSET,
    nspin_to: float | Unset = UNSET,
    page: int | Unset = UNSET,
    size: int | Unset = UNSET,
    sort: str | Unset = UNSET,
    dir_: str | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["cancelFlag"] = cancel_flag

    params["updateTimeFrom"] = update_time_from

    params["updateTimeTo"] = update_time_to

    params["submitTimeFrom"] = submit_time_from

    params["submitTimeTo"] = submit_time_to

    params["deliveryDateFrom"] = delivery_date_from

    params["deliveryDateTo"] = delivery_date_to

    params["qseName"] = qse_name

    params["resourceName"] = resource_name

    params["hourEnding"] = hour_ending

    params["status"] = status

    params["highSustainedLimitFrom"] = high_sustained_limit_from

    params["highSustainedLimitTo"] = high_sustained_limit_to

    params["lowSustainedLimitFrom"] = low_sustained_limit_from

    params["lowSustainedLimitTo"] = low_sustained_limit_to

    params["highEmergencyLimitFrom"] = high_emergency_limit_from

    params["highEmergencyLimitTo"] = high_emergency_limit_to

    params["lowEmergencyLimitFrom"] = low_emergency_limit_from

    params["lowEmergencyLimitTo"] = low_emergency_limit_to

    params["REGUPFrom"] = regup_from

    params["REGUPTo"] = regup_to

    params["REGDNFrom"] = regdn_from

    params["REGDNTo"] = regdn_to

    params["RRSPFRFrom"] = rrspfr_from

    params["RRSPFRTo"] = rrspfr_to

    params["RRSFFRFrom"] = rrsffr_from

    params["RRSFFRTo"] = rrsffr_to

    params["RRSUFRFrom"] = rrsufr_from

    params["RRSUFRTo"] = rrsufr_to

    params["NSPINFrom"] = nspin_from

    params["NSPINTo"] = nspin_to

    params["page"] = page

    params["size"] = size

    params["sort"] = sort

    params["dir"] = dir_

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/np3-991-ex/60_cop_all_updates",
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
    cancel_flag: bool | Unset = UNSET,
    update_time_from: str | Unset = UNSET,
    update_time_to: str | Unset = UNSET,
    submit_time_from: str | Unset = UNSET,
    submit_time_to: str | Unset = UNSET,
    delivery_date_from: str | Unset = UNSET,
    delivery_date_to: str | Unset = UNSET,
    qse_name: str | Unset = UNSET,
    resource_name: str | Unset = UNSET,
    hour_ending: str | Unset = UNSET,
    status: str | Unset = UNSET,
    high_sustained_limit_from: float | Unset = UNSET,
    high_sustained_limit_to: float | Unset = UNSET,
    low_sustained_limit_from: float | Unset = UNSET,
    low_sustained_limit_to: float | Unset = UNSET,
    high_emergency_limit_from: float | Unset = UNSET,
    high_emergency_limit_to: float | Unset = UNSET,
    low_emergency_limit_from: float | Unset = UNSET,
    low_emergency_limit_to: float | Unset = UNSET,
    regup_from: float | Unset = UNSET,
    regup_to: float | Unset = UNSET,
    regdn_from: float | Unset = UNSET,
    regdn_to: float | Unset = UNSET,
    rrspfr_from: float | Unset = UNSET,
    rrspfr_to: float | Unset = UNSET,
    rrsffr_from: float | Unset = UNSET,
    rrsffr_to: float | Unset = UNSET,
    rrsufr_from: float | Unset = UNSET,
    rrsufr_to: float | Unset = UNSET,
    nspin_from: float | Unset = UNSET,
    nspin_to: float | Unset = UNSET,
    page: int | Unset = UNSET,
    size: int | Unset = UNSET,
    sort: str | Unset = UNSET,
    dir_: str | Unset = UNSET,
) -> Response[Exception_ | Report]:
    """60-Day COP All Updates

     60-Day COP All Updates

    Args:
        cancel_flag (bool | Unset):
        update_time_from (str | Unset):
        update_time_to (str | Unset):
        submit_time_from (str | Unset):
        submit_time_to (str | Unset):
        delivery_date_from (str | Unset):
        delivery_date_to (str | Unset):
        qse_name (str | Unset):
        resource_name (str | Unset):
        hour_ending (str | Unset):
        status (str | Unset):
        high_sustained_limit_from (float | Unset):
        high_sustained_limit_to (float | Unset):
        low_sustained_limit_from (float | Unset):
        low_sustained_limit_to (float | Unset):
        high_emergency_limit_from (float | Unset):
        high_emergency_limit_to (float | Unset):
        low_emergency_limit_from (float | Unset):
        low_emergency_limit_to (float | Unset):
        regup_from (float | Unset):
        regup_to (float | Unset):
        regdn_from (float | Unset):
        regdn_to (float | Unset):
        rrspfr_from (float | Unset):
        rrspfr_to (float | Unset):
        rrsffr_from (float | Unset):
        rrsffr_to (float | Unset):
        rrsufr_from (float | Unset):
        rrsufr_to (float | Unset):
        nspin_from (float | Unset):
        nspin_to (float | Unset):
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
        cancel_flag=cancel_flag,
        update_time_from=update_time_from,
        update_time_to=update_time_to,
        submit_time_from=submit_time_from,
        submit_time_to=submit_time_to,
        delivery_date_from=delivery_date_from,
        delivery_date_to=delivery_date_to,
        qse_name=qse_name,
        resource_name=resource_name,
        hour_ending=hour_ending,
        status=status,
        high_sustained_limit_from=high_sustained_limit_from,
        high_sustained_limit_to=high_sustained_limit_to,
        low_sustained_limit_from=low_sustained_limit_from,
        low_sustained_limit_to=low_sustained_limit_to,
        high_emergency_limit_from=high_emergency_limit_from,
        high_emergency_limit_to=high_emergency_limit_to,
        low_emergency_limit_from=low_emergency_limit_from,
        low_emergency_limit_to=low_emergency_limit_to,
        regup_from=regup_from,
        regup_to=regup_to,
        regdn_from=regdn_from,
        regdn_to=regdn_to,
        rrspfr_from=rrspfr_from,
        rrspfr_to=rrspfr_to,
        rrsffr_from=rrsffr_from,
        rrsffr_to=rrsffr_to,
        rrsufr_from=rrsufr_from,
        rrsufr_to=rrsufr_to,
        nspin_from=nspin_from,
        nspin_to=nspin_to,
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
    cancel_flag: bool | Unset = UNSET,
    update_time_from: str | Unset = UNSET,
    update_time_to: str | Unset = UNSET,
    submit_time_from: str | Unset = UNSET,
    submit_time_to: str | Unset = UNSET,
    delivery_date_from: str | Unset = UNSET,
    delivery_date_to: str | Unset = UNSET,
    qse_name: str | Unset = UNSET,
    resource_name: str | Unset = UNSET,
    hour_ending: str | Unset = UNSET,
    status: str | Unset = UNSET,
    high_sustained_limit_from: float | Unset = UNSET,
    high_sustained_limit_to: float | Unset = UNSET,
    low_sustained_limit_from: float | Unset = UNSET,
    low_sustained_limit_to: float | Unset = UNSET,
    high_emergency_limit_from: float | Unset = UNSET,
    high_emergency_limit_to: float | Unset = UNSET,
    low_emergency_limit_from: float | Unset = UNSET,
    low_emergency_limit_to: float | Unset = UNSET,
    regup_from: float | Unset = UNSET,
    regup_to: float | Unset = UNSET,
    regdn_from: float | Unset = UNSET,
    regdn_to: float | Unset = UNSET,
    rrspfr_from: float | Unset = UNSET,
    rrspfr_to: float | Unset = UNSET,
    rrsffr_from: float | Unset = UNSET,
    rrsffr_to: float | Unset = UNSET,
    rrsufr_from: float | Unset = UNSET,
    rrsufr_to: float | Unset = UNSET,
    nspin_from: float | Unset = UNSET,
    nspin_to: float | Unset = UNSET,
    page: int | Unset = UNSET,
    size: int | Unset = UNSET,
    sort: str | Unset = UNSET,
    dir_: str | Unset = UNSET,
) -> Exception_ | Report | None:
    """60-Day COP All Updates

     60-Day COP All Updates

    Args:
        cancel_flag (bool | Unset):
        update_time_from (str | Unset):
        update_time_to (str | Unset):
        submit_time_from (str | Unset):
        submit_time_to (str | Unset):
        delivery_date_from (str | Unset):
        delivery_date_to (str | Unset):
        qse_name (str | Unset):
        resource_name (str | Unset):
        hour_ending (str | Unset):
        status (str | Unset):
        high_sustained_limit_from (float | Unset):
        high_sustained_limit_to (float | Unset):
        low_sustained_limit_from (float | Unset):
        low_sustained_limit_to (float | Unset):
        high_emergency_limit_from (float | Unset):
        high_emergency_limit_to (float | Unset):
        low_emergency_limit_from (float | Unset):
        low_emergency_limit_to (float | Unset):
        regup_from (float | Unset):
        regup_to (float | Unset):
        regdn_from (float | Unset):
        regdn_to (float | Unset):
        rrspfr_from (float | Unset):
        rrspfr_to (float | Unset):
        rrsffr_from (float | Unset):
        rrsffr_to (float | Unset):
        rrsufr_from (float | Unset):
        rrsufr_to (float | Unset):
        nspin_from (float | Unset):
        nspin_to (float | Unset):
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
        cancel_flag=cancel_flag,
        update_time_from=update_time_from,
        update_time_to=update_time_to,
        submit_time_from=submit_time_from,
        submit_time_to=submit_time_to,
        delivery_date_from=delivery_date_from,
        delivery_date_to=delivery_date_to,
        qse_name=qse_name,
        resource_name=resource_name,
        hour_ending=hour_ending,
        status=status,
        high_sustained_limit_from=high_sustained_limit_from,
        high_sustained_limit_to=high_sustained_limit_to,
        low_sustained_limit_from=low_sustained_limit_from,
        low_sustained_limit_to=low_sustained_limit_to,
        high_emergency_limit_from=high_emergency_limit_from,
        high_emergency_limit_to=high_emergency_limit_to,
        low_emergency_limit_from=low_emergency_limit_from,
        low_emergency_limit_to=low_emergency_limit_to,
        regup_from=regup_from,
        regup_to=regup_to,
        regdn_from=regdn_from,
        regdn_to=regdn_to,
        rrspfr_from=rrspfr_from,
        rrspfr_to=rrspfr_to,
        rrsffr_from=rrsffr_from,
        rrsffr_to=rrsffr_to,
        rrsufr_from=rrsufr_from,
        rrsufr_to=rrsufr_to,
        nspin_from=nspin_from,
        nspin_to=nspin_to,
        page=page,
        size=size,
        sort=sort,
        dir_=dir_,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    cancel_flag: bool | Unset = UNSET,
    update_time_from: str | Unset = UNSET,
    update_time_to: str | Unset = UNSET,
    submit_time_from: str | Unset = UNSET,
    submit_time_to: str | Unset = UNSET,
    delivery_date_from: str | Unset = UNSET,
    delivery_date_to: str | Unset = UNSET,
    qse_name: str | Unset = UNSET,
    resource_name: str | Unset = UNSET,
    hour_ending: str | Unset = UNSET,
    status: str | Unset = UNSET,
    high_sustained_limit_from: float | Unset = UNSET,
    high_sustained_limit_to: float | Unset = UNSET,
    low_sustained_limit_from: float | Unset = UNSET,
    low_sustained_limit_to: float | Unset = UNSET,
    high_emergency_limit_from: float | Unset = UNSET,
    high_emergency_limit_to: float | Unset = UNSET,
    low_emergency_limit_from: float | Unset = UNSET,
    low_emergency_limit_to: float | Unset = UNSET,
    regup_from: float | Unset = UNSET,
    regup_to: float | Unset = UNSET,
    regdn_from: float | Unset = UNSET,
    regdn_to: float | Unset = UNSET,
    rrspfr_from: float | Unset = UNSET,
    rrspfr_to: float | Unset = UNSET,
    rrsffr_from: float | Unset = UNSET,
    rrsffr_to: float | Unset = UNSET,
    rrsufr_from: float | Unset = UNSET,
    rrsufr_to: float | Unset = UNSET,
    nspin_from: float | Unset = UNSET,
    nspin_to: float | Unset = UNSET,
    page: int | Unset = UNSET,
    size: int | Unset = UNSET,
    sort: str | Unset = UNSET,
    dir_: str | Unset = UNSET,
) -> Response[Exception_ | Report]:
    """60-Day COP All Updates

     60-Day COP All Updates

    Args:
        cancel_flag (bool | Unset):
        update_time_from (str | Unset):
        update_time_to (str | Unset):
        submit_time_from (str | Unset):
        submit_time_to (str | Unset):
        delivery_date_from (str | Unset):
        delivery_date_to (str | Unset):
        qse_name (str | Unset):
        resource_name (str | Unset):
        hour_ending (str | Unset):
        status (str | Unset):
        high_sustained_limit_from (float | Unset):
        high_sustained_limit_to (float | Unset):
        low_sustained_limit_from (float | Unset):
        low_sustained_limit_to (float | Unset):
        high_emergency_limit_from (float | Unset):
        high_emergency_limit_to (float | Unset):
        low_emergency_limit_from (float | Unset):
        low_emergency_limit_to (float | Unset):
        regup_from (float | Unset):
        regup_to (float | Unset):
        regdn_from (float | Unset):
        regdn_to (float | Unset):
        rrspfr_from (float | Unset):
        rrspfr_to (float | Unset):
        rrsffr_from (float | Unset):
        rrsffr_to (float | Unset):
        rrsufr_from (float | Unset):
        rrsufr_to (float | Unset):
        nspin_from (float | Unset):
        nspin_to (float | Unset):
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
        cancel_flag=cancel_flag,
        update_time_from=update_time_from,
        update_time_to=update_time_to,
        submit_time_from=submit_time_from,
        submit_time_to=submit_time_to,
        delivery_date_from=delivery_date_from,
        delivery_date_to=delivery_date_to,
        qse_name=qse_name,
        resource_name=resource_name,
        hour_ending=hour_ending,
        status=status,
        high_sustained_limit_from=high_sustained_limit_from,
        high_sustained_limit_to=high_sustained_limit_to,
        low_sustained_limit_from=low_sustained_limit_from,
        low_sustained_limit_to=low_sustained_limit_to,
        high_emergency_limit_from=high_emergency_limit_from,
        high_emergency_limit_to=high_emergency_limit_to,
        low_emergency_limit_from=low_emergency_limit_from,
        low_emergency_limit_to=low_emergency_limit_to,
        regup_from=regup_from,
        regup_to=regup_to,
        regdn_from=regdn_from,
        regdn_to=regdn_to,
        rrspfr_from=rrspfr_from,
        rrspfr_to=rrspfr_to,
        rrsffr_from=rrsffr_from,
        rrsffr_to=rrsffr_to,
        rrsufr_from=rrsufr_from,
        rrsufr_to=rrsufr_to,
        nspin_from=nspin_from,
        nspin_to=nspin_to,
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
    cancel_flag: bool | Unset = UNSET,
    update_time_from: str | Unset = UNSET,
    update_time_to: str | Unset = UNSET,
    submit_time_from: str | Unset = UNSET,
    submit_time_to: str | Unset = UNSET,
    delivery_date_from: str | Unset = UNSET,
    delivery_date_to: str | Unset = UNSET,
    qse_name: str | Unset = UNSET,
    resource_name: str | Unset = UNSET,
    hour_ending: str | Unset = UNSET,
    status: str | Unset = UNSET,
    high_sustained_limit_from: float | Unset = UNSET,
    high_sustained_limit_to: float | Unset = UNSET,
    low_sustained_limit_from: float | Unset = UNSET,
    low_sustained_limit_to: float | Unset = UNSET,
    high_emergency_limit_from: float | Unset = UNSET,
    high_emergency_limit_to: float | Unset = UNSET,
    low_emergency_limit_from: float | Unset = UNSET,
    low_emergency_limit_to: float | Unset = UNSET,
    regup_from: float | Unset = UNSET,
    regup_to: float | Unset = UNSET,
    regdn_from: float | Unset = UNSET,
    regdn_to: float | Unset = UNSET,
    rrspfr_from: float | Unset = UNSET,
    rrspfr_to: float | Unset = UNSET,
    rrsffr_from: float | Unset = UNSET,
    rrsffr_to: float | Unset = UNSET,
    rrsufr_from: float | Unset = UNSET,
    rrsufr_to: float | Unset = UNSET,
    nspin_from: float | Unset = UNSET,
    nspin_to: float | Unset = UNSET,
    page: int | Unset = UNSET,
    size: int | Unset = UNSET,
    sort: str | Unset = UNSET,
    dir_: str | Unset = UNSET,
) -> Exception_ | Report | None:
    """60-Day COP All Updates

     60-Day COP All Updates

    Args:
        cancel_flag (bool | Unset):
        update_time_from (str | Unset):
        update_time_to (str | Unset):
        submit_time_from (str | Unset):
        submit_time_to (str | Unset):
        delivery_date_from (str | Unset):
        delivery_date_to (str | Unset):
        qse_name (str | Unset):
        resource_name (str | Unset):
        hour_ending (str | Unset):
        status (str | Unset):
        high_sustained_limit_from (float | Unset):
        high_sustained_limit_to (float | Unset):
        low_sustained_limit_from (float | Unset):
        low_sustained_limit_to (float | Unset):
        high_emergency_limit_from (float | Unset):
        high_emergency_limit_to (float | Unset):
        low_emergency_limit_from (float | Unset):
        low_emergency_limit_to (float | Unset):
        regup_from (float | Unset):
        regup_to (float | Unset):
        regdn_from (float | Unset):
        regdn_to (float | Unset):
        rrspfr_from (float | Unset):
        rrspfr_to (float | Unset):
        rrsffr_from (float | Unset):
        rrsffr_to (float | Unset):
        rrsufr_from (float | Unset):
        rrsufr_to (float | Unset):
        nspin_from (float | Unset):
        nspin_to (float | Unset):
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
            cancel_flag=cancel_flag,
            update_time_from=update_time_from,
            update_time_to=update_time_to,
            submit_time_from=submit_time_from,
            submit_time_to=submit_time_to,
            delivery_date_from=delivery_date_from,
            delivery_date_to=delivery_date_to,
            qse_name=qse_name,
            resource_name=resource_name,
            hour_ending=hour_ending,
            status=status,
            high_sustained_limit_from=high_sustained_limit_from,
            high_sustained_limit_to=high_sustained_limit_to,
            low_sustained_limit_from=low_sustained_limit_from,
            low_sustained_limit_to=low_sustained_limit_to,
            high_emergency_limit_from=high_emergency_limit_from,
            high_emergency_limit_to=high_emergency_limit_to,
            low_emergency_limit_from=low_emergency_limit_from,
            low_emergency_limit_to=low_emergency_limit_to,
            regup_from=regup_from,
            regup_to=regup_to,
            regdn_from=regdn_from,
            regdn_to=regdn_to,
            rrspfr_from=rrspfr_from,
            rrspfr_to=rrspfr_to,
            rrsffr_from=rrsffr_from,
            rrsffr_to=rrsffr_to,
            rrsufr_from=rrsufr_from,
            rrsufr_to=rrsufr_to,
            nspin_from=nspin_from,
            nspin_to=nspin_to,
            page=page,
            size=size,
            sort=sort,
            dir_=dir_,
        )
    ).parsed
