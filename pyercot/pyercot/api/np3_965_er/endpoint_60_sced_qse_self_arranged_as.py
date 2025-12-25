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
    qse_name: str | Unset = UNSET,
    regup: str | Unset = UNSET,
    regdn_from: float | Unset = UNSET,
    regdn_to: float | Unset = UNSET,
    nspin_from: float | Unset = UNSET,
    nspin_to: float | Unset = UNSET,
    nspnm_from: float | Unset = UNSET,
    nspnm_to: float | Unset = UNSET,
    rrspfr_from: float | Unset = UNSET,
    rrspfr_to: float | Unset = UNSET,
    rrsffr_from: float | Unset = UNSET,
    rrsffr_to: float | Unset = UNSET,
    rrsufr_from: float | Unset = UNSET,
    rrsufr_to: float | Unset = UNSET,
    page: int | Unset = UNSET,
    size: int | Unset = UNSET,
    sort: str | Unset = UNSET,
    dir_: str | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["SCEDTimestampFrom"] = sced_timestamp_from

    params["SCEDTimestampTo"] = sced_timestamp_to

    params["repeatHourFlag"] = repeat_hour_flag

    params["qseName"] = qse_name

    params["REGUP"] = regup

    params["REGDNFrom"] = regdn_from

    params["REGDNTo"] = regdn_to

    params["NSPINFrom"] = nspin_from

    params["NSPINTo"] = nspin_to

    params["NSPNMFrom"] = nspnm_from

    params["NSPNMTo"] = nspnm_to

    params["RRSPFRFrom"] = rrspfr_from

    params["RRSPFRTo"] = rrspfr_to

    params["RRSFFRFrom"] = rrsffr_from

    params["RRSFFRTo"] = rrsffr_to

    params["RRSUFRFrom"] = rrsufr_from

    params["RRSUFRTo"] = rrsufr_to

    params["page"] = page

    params["size"] = size

    params["sort"] = sort

    params["dir"] = dir_

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/np3-965-er/60_sced_qse_self_arranged_as",
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
    qse_name: str | Unset = UNSET,
    regup: str | Unset = UNSET,
    regdn_from: float | Unset = UNSET,
    regdn_to: float | Unset = UNSET,
    nspin_from: float | Unset = UNSET,
    nspin_to: float | Unset = UNSET,
    nspnm_from: float | Unset = UNSET,
    nspnm_to: float | Unset = UNSET,
    rrspfr_from: float | Unset = UNSET,
    rrspfr_to: float | Unset = UNSET,
    rrsffr_from: float | Unset = UNSET,
    rrsffr_to: float | Unset = UNSET,
    rrsufr_from: float | Unset = UNSET,
    rrsufr_to: float | Unset = UNSET,
    page: int | Unset = UNSET,
    size: int | Unset = UNSET,
    sort: str | Unset = UNSET,
    dir_: str | Unset = UNSET,
) -> Response[Exception_ | Report]:
    """60 Day QSE-specific Self-Arranged AS in SCED

     60 Day QSE-specific Self-Arranged AS in SCED

    Args:
        sced_timestamp_from (str | Unset):
        sced_timestamp_to (str | Unset):
        repeat_hour_flag (bool | Unset):
        qse_name (str | Unset):
        regup (str | Unset):
        regdn_from (float | Unset):
        regdn_to (float | Unset):
        nspin_from (float | Unset):
        nspin_to (float | Unset):
        nspnm_from (float | Unset):
        nspnm_to (float | Unset):
        rrspfr_from (float | Unset):
        rrspfr_to (float | Unset):
        rrsffr_from (float | Unset):
        rrsffr_to (float | Unset):
        rrsufr_from (float | Unset):
        rrsufr_to (float | Unset):
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
        qse_name=qse_name,
        regup=regup,
        regdn_from=regdn_from,
        regdn_to=regdn_to,
        nspin_from=nspin_from,
        nspin_to=nspin_to,
        nspnm_from=nspnm_from,
        nspnm_to=nspnm_to,
        rrspfr_from=rrspfr_from,
        rrspfr_to=rrspfr_to,
        rrsffr_from=rrsffr_from,
        rrsffr_to=rrsffr_to,
        rrsufr_from=rrsufr_from,
        rrsufr_to=rrsufr_to,
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
    qse_name: str | Unset = UNSET,
    regup: str | Unset = UNSET,
    regdn_from: float | Unset = UNSET,
    regdn_to: float | Unset = UNSET,
    nspin_from: float | Unset = UNSET,
    nspin_to: float | Unset = UNSET,
    nspnm_from: float | Unset = UNSET,
    nspnm_to: float | Unset = UNSET,
    rrspfr_from: float | Unset = UNSET,
    rrspfr_to: float | Unset = UNSET,
    rrsffr_from: float | Unset = UNSET,
    rrsffr_to: float | Unset = UNSET,
    rrsufr_from: float | Unset = UNSET,
    rrsufr_to: float | Unset = UNSET,
    page: int | Unset = UNSET,
    size: int | Unset = UNSET,
    sort: str | Unset = UNSET,
    dir_: str | Unset = UNSET,
) -> Exception_ | Report | None:
    """60 Day QSE-specific Self-Arranged AS in SCED

     60 Day QSE-specific Self-Arranged AS in SCED

    Args:
        sced_timestamp_from (str | Unset):
        sced_timestamp_to (str | Unset):
        repeat_hour_flag (bool | Unset):
        qse_name (str | Unset):
        regup (str | Unset):
        regdn_from (float | Unset):
        regdn_to (float | Unset):
        nspin_from (float | Unset):
        nspin_to (float | Unset):
        nspnm_from (float | Unset):
        nspnm_to (float | Unset):
        rrspfr_from (float | Unset):
        rrspfr_to (float | Unset):
        rrsffr_from (float | Unset):
        rrsffr_to (float | Unset):
        rrsufr_from (float | Unset):
        rrsufr_to (float | Unset):
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
        qse_name=qse_name,
        regup=regup,
        regdn_from=regdn_from,
        regdn_to=regdn_to,
        nspin_from=nspin_from,
        nspin_to=nspin_to,
        nspnm_from=nspnm_from,
        nspnm_to=nspnm_to,
        rrspfr_from=rrspfr_from,
        rrspfr_to=rrspfr_to,
        rrsffr_from=rrsffr_from,
        rrsffr_to=rrsffr_to,
        rrsufr_from=rrsufr_from,
        rrsufr_to=rrsufr_to,
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
    qse_name: str | Unset = UNSET,
    regup: str | Unset = UNSET,
    regdn_from: float | Unset = UNSET,
    regdn_to: float | Unset = UNSET,
    nspin_from: float | Unset = UNSET,
    nspin_to: float | Unset = UNSET,
    nspnm_from: float | Unset = UNSET,
    nspnm_to: float | Unset = UNSET,
    rrspfr_from: float | Unset = UNSET,
    rrspfr_to: float | Unset = UNSET,
    rrsffr_from: float | Unset = UNSET,
    rrsffr_to: float | Unset = UNSET,
    rrsufr_from: float | Unset = UNSET,
    rrsufr_to: float | Unset = UNSET,
    page: int | Unset = UNSET,
    size: int | Unset = UNSET,
    sort: str | Unset = UNSET,
    dir_: str | Unset = UNSET,
) -> Response[Exception_ | Report]:
    """60 Day QSE-specific Self-Arranged AS in SCED

     60 Day QSE-specific Self-Arranged AS in SCED

    Args:
        sced_timestamp_from (str | Unset):
        sced_timestamp_to (str | Unset):
        repeat_hour_flag (bool | Unset):
        qse_name (str | Unset):
        regup (str | Unset):
        regdn_from (float | Unset):
        regdn_to (float | Unset):
        nspin_from (float | Unset):
        nspin_to (float | Unset):
        nspnm_from (float | Unset):
        nspnm_to (float | Unset):
        rrspfr_from (float | Unset):
        rrspfr_to (float | Unset):
        rrsffr_from (float | Unset):
        rrsffr_to (float | Unset):
        rrsufr_from (float | Unset):
        rrsufr_to (float | Unset):
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
        qse_name=qse_name,
        regup=regup,
        regdn_from=regdn_from,
        regdn_to=regdn_to,
        nspin_from=nspin_from,
        nspin_to=nspin_to,
        nspnm_from=nspnm_from,
        nspnm_to=nspnm_to,
        rrspfr_from=rrspfr_from,
        rrspfr_to=rrspfr_to,
        rrsffr_from=rrsffr_from,
        rrsffr_to=rrsffr_to,
        rrsufr_from=rrsufr_from,
        rrsufr_to=rrsufr_to,
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
    qse_name: str | Unset = UNSET,
    regup: str | Unset = UNSET,
    regdn_from: float | Unset = UNSET,
    regdn_to: float | Unset = UNSET,
    nspin_from: float | Unset = UNSET,
    nspin_to: float | Unset = UNSET,
    nspnm_from: float | Unset = UNSET,
    nspnm_to: float | Unset = UNSET,
    rrspfr_from: float | Unset = UNSET,
    rrspfr_to: float | Unset = UNSET,
    rrsffr_from: float | Unset = UNSET,
    rrsffr_to: float | Unset = UNSET,
    rrsufr_from: float | Unset = UNSET,
    rrsufr_to: float | Unset = UNSET,
    page: int | Unset = UNSET,
    size: int | Unset = UNSET,
    sort: str | Unset = UNSET,
    dir_: str | Unset = UNSET,
) -> Exception_ | Report | None:
    """60 Day QSE-specific Self-Arranged AS in SCED

     60 Day QSE-specific Self-Arranged AS in SCED

    Args:
        sced_timestamp_from (str | Unset):
        sced_timestamp_to (str | Unset):
        repeat_hour_flag (bool | Unset):
        qse_name (str | Unset):
        regup (str | Unset):
        regdn_from (float | Unset):
        regdn_to (float | Unset):
        nspin_from (float | Unset):
        nspin_to (float | Unset):
        nspnm_from (float | Unset):
        nspnm_to (float | Unset):
        rrspfr_from (float | Unset):
        rrspfr_to (float | Unset):
        rrsffr_from (float | Unset):
        rrsffr_to (float | Unset):
        rrsufr_from (float | Unset):
        rrsufr_to (float | Unset):
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
            qse_name=qse_name,
            regup=regup,
            regdn_from=regdn_from,
            regdn_to=regdn_to,
            nspin_from=nspin_from,
            nspin_to=nspin_to,
            nspnm_from=nspnm_from,
            nspnm_to=nspnm_to,
            rrspfr_from=rrspfr_from,
            rrspfr_to=rrspfr_to,
            rrsffr_from=rrsffr_from,
            rrsffr_to=rrsffr_to,
            rrsufr_from=rrsufr_from,
            rrsufr_to=rrsufr_to,
            page=page,
            size=size,
            sort=sort,
            dir_=dir_,
        )
    ).parsed
