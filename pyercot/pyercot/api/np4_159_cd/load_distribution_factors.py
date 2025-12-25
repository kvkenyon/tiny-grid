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
    ldf_date_from: str | Unset = UNSET,
    ldf_date_to: str | Unset = UNSET,
    ldf_hour: str | Unset = UNSET,
    substation: str | Unset = UNSET,
    distribution_factor_from: float | Unset = UNSET,
    distribution_factor_to: float | Unset = UNSET,
    load_id: str | Unset = UNSET,
    mvar_distribution_factor_from: float | Unset = UNSET,
    mvar_distribution_factor_to: float | Unset = UNSET,
    posted_datetime_from: str | Unset = UNSET,
    posted_datetime_to: str | Unset = UNSET,
    mrid_load: str | Unset = UNSET,
    dst_flag: bool | Unset = UNSET,
    page: int | Unset = UNSET,
    size: int | Unset = UNSET,
    sort: str | Unset = UNSET,
    dir_: str | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["LDFDateFrom"] = ldf_date_from

    params["LDFDateTo"] = ldf_date_to

    params["LDFHour"] = ldf_hour

    params["substation"] = substation

    params["distributionFactorFrom"] = distribution_factor_from

    params["distributionFactorTo"] = distribution_factor_to

    params["loadId"] = load_id

    params["MVARDistributionFactorFrom"] = mvar_distribution_factor_from

    params["MVARDistributionFactorTo"] = mvar_distribution_factor_to

    params["postedDatetimeFrom"] = posted_datetime_from

    params["postedDatetimeTo"] = posted_datetime_to

    params["MRIDLoad"] = mrid_load

    params["DSTFlag"] = dst_flag

    params["page"] = page

    params["size"] = size

    params["sort"] = sort

    params["dir"] = dir_

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/np4-159-cd/load_distribution_factors",
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
    ldf_date_from: str | Unset = UNSET,
    ldf_date_to: str | Unset = UNSET,
    ldf_hour: str | Unset = UNSET,
    substation: str | Unset = UNSET,
    distribution_factor_from: float | Unset = UNSET,
    distribution_factor_to: float | Unset = UNSET,
    load_id: str | Unset = UNSET,
    mvar_distribution_factor_from: float | Unset = UNSET,
    mvar_distribution_factor_to: float | Unset = UNSET,
    posted_datetime_from: str | Unset = UNSET,
    posted_datetime_to: str | Unset = UNSET,
    mrid_load: str | Unset = UNSET,
    dst_flag: bool | Unset = UNSET,
    page: int | Unset = UNSET,
    size: int | Unset = UNSET,
    sort: str | Unset = UNSET,
    dir_: str | Unset = UNSET,
) -> Response[Exception_ | Report]:
    """Load Distribution Factors

     Load Distribution Factors

    Args:
        ldf_date_from (str | Unset):
        ldf_date_to (str | Unset):
        ldf_hour (str | Unset):
        substation (str | Unset):
        distribution_factor_from (float | Unset):
        distribution_factor_to (float | Unset):
        load_id (str | Unset):
        mvar_distribution_factor_from (float | Unset):
        mvar_distribution_factor_to (float | Unset):
        posted_datetime_from (str | Unset):
        posted_datetime_to (str | Unset):
        mrid_load (str | Unset):
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
        ldf_date_from=ldf_date_from,
        ldf_date_to=ldf_date_to,
        ldf_hour=ldf_hour,
        substation=substation,
        distribution_factor_from=distribution_factor_from,
        distribution_factor_to=distribution_factor_to,
        load_id=load_id,
        mvar_distribution_factor_from=mvar_distribution_factor_from,
        mvar_distribution_factor_to=mvar_distribution_factor_to,
        posted_datetime_from=posted_datetime_from,
        posted_datetime_to=posted_datetime_to,
        mrid_load=mrid_load,
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
    ldf_date_from: str | Unset = UNSET,
    ldf_date_to: str | Unset = UNSET,
    ldf_hour: str | Unset = UNSET,
    substation: str | Unset = UNSET,
    distribution_factor_from: float | Unset = UNSET,
    distribution_factor_to: float | Unset = UNSET,
    load_id: str | Unset = UNSET,
    mvar_distribution_factor_from: float | Unset = UNSET,
    mvar_distribution_factor_to: float | Unset = UNSET,
    posted_datetime_from: str | Unset = UNSET,
    posted_datetime_to: str | Unset = UNSET,
    mrid_load: str | Unset = UNSET,
    dst_flag: bool | Unset = UNSET,
    page: int | Unset = UNSET,
    size: int | Unset = UNSET,
    sort: str | Unset = UNSET,
    dir_: str | Unset = UNSET,
) -> Exception_ | Report | None:
    """Load Distribution Factors

     Load Distribution Factors

    Args:
        ldf_date_from (str | Unset):
        ldf_date_to (str | Unset):
        ldf_hour (str | Unset):
        substation (str | Unset):
        distribution_factor_from (float | Unset):
        distribution_factor_to (float | Unset):
        load_id (str | Unset):
        mvar_distribution_factor_from (float | Unset):
        mvar_distribution_factor_to (float | Unset):
        posted_datetime_from (str | Unset):
        posted_datetime_to (str | Unset):
        mrid_load (str | Unset):
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
        ldf_date_from=ldf_date_from,
        ldf_date_to=ldf_date_to,
        ldf_hour=ldf_hour,
        substation=substation,
        distribution_factor_from=distribution_factor_from,
        distribution_factor_to=distribution_factor_to,
        load_id=load_id,
        mvar_distribution_factor_from=mvar_distribution_factor_from,
        mvar_distribution_factor_to=mvar_distribution_factor_to,
        posted_datetime_from=posted_datetime_from,
        posted_datetime_to=posted_datetime_to,
        mrid_load=mrid_load,
        dst_flag=dst_flag,
        page=page,
        size=size,
        sort=sort,
        dir_=dir_,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    ldf_date_from: str | Unset = UNSET,
    ldf_date_to: str | Unset = UNSET,
    ldf_hour: str | Unset = UNSET,
    substation: str | Unset = UNSET,
    distribution_factor_from: float | Unset = UNSET,
    distribution_factor_to: float | Unset = UNSET,
    load_id: str | Unset = UNSET,
    mvar_distribution_factor_from: float | Unset = UNSET,
    mvar_distribution_factor_to: float | Unset = UNSET,
    posted_datetime_from: str | Unset = UNSET,
    posted_datetime_to: str | Unset = UNSET,
    mrid_load: str | Unset = UNSET,
    dst_flag: bool | Unset = UNSET,
    page: int | Unset = UNSET,
    size: int | Unset = UNSET,
    sort: str | Unset = UNSET,
    dir_: str | Unset = UNSET,
) -> Response[Exception_ | Report]:
    """Load Distribution Factors

     Load Distribution Factors

    Args:
        ldf_date_from (str | Unset):
        ldf_date_to (str | Unset):
        ldf_hour (str | Unset):
        substation (str | Unset):
        distribution_factor_from (float | Unset):
        distribution_factor_to (float | Unset):
        load_id (str | Unset):
        mvar_distribution_factor_from (float | Unset):
        mvar_distribution_factor_to (float | Unset):
        posted_datetime_from (str | Unset):
        posted_datetime_to (str | Unset):
        mrid_load (str | Unset):
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
        ldf_date_from=ldf_date_from,
        ldf_date_to=ldf_date_to,
        ldf_hour=ldf_hour,
        substation=substation,
        distribution_factor_from=distribution_factor_from,
        distribution_factor_to=distribution_factor_to,
        load_id=load_id,
        mvar_distribution_factor_from=mvar_distribution_factor_from,
        mvar_distribution_factor_to=mvar_distribution_factor_to,
        posted_datetime_from=posted_datetime_from,
        posted_datetime_to=posted_datetime_to,
        mrid_load=mrid_load,
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
    ldf_date_from: str | Unset = UNSET,
    ldf_date_to: str | Unset = UNSET,
    ldf_hour: str | Unset = UNSET,
    substation: str | Unset = UNSET,
    distribution_factor_from: float | Unset = UNSET,
    distribution_factor_to: float | Unset = UNSET,
    load_id: str | Unset = UNSET,
    mvar_distribution_factor_from: float | Unset = UNSET,
    mvar_distribution_factor_to: float | Unset = UNSET,
    posted_datetime_from: str | Unset = UNSET,
    posted_datetime_to: str | Unset = UNSET,
    mrid_load: str | Unset = UNSET,
    dst_flag: bool | Unset = UNSET,
    page: int | Unset = UNSET,
    size: int | Unset = UNSET,
    sort: str | Unset = UNSET,
    dir_: str | Unset = UNSET,
) -> Exception_ | Report | None:
    """Load Distribution Factors

     Load Distribution Factors

    Args:
        ldf_date_from (str | Unset):
        ldf_date_to (str | Unset):
        ldf_hour (str | Unset):
        substation (str | Unset):
        distribution_factor_from (float | Unset):
        distribution_factor_to (float | Unset):
        load_id (str | Unset):
        mvar_distribution_factor_from (float | Unset):
        mvar_distribution_factor_to (float | Unset):
        posted_datetime_from (str | Unset):
        posted_datetime_to (str | Unset):
        mrid_load (str | Unset):
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
            ldf_date_from=ldf_date_from,
            ldf_date_to=ldf_date_to,
            ldf_hour=ldf_hour,
            substation=substation,
            distribution_factor_from=distribution_factor_from,
            distribution_factor_to=distribution_factor_to,
            load_id=load_id,
            mvar_distribution_factor_from=mvar_distribution_factor_from,
            mvar_distribution_factor_to=mvar_distribution_factor_to,
            posted_datetime_from=posted_datetime_from,
            posted_datetime_to=posted_datetime_to,
            mrid_load=mrid_load,
            dst_flag=dst_flag,
            page=page,
            size=size,
            sort=sort,
            dir_=dir_,
        )
    ).parsed
