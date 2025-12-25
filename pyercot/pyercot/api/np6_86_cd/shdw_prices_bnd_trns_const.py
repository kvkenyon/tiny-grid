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
    from_station: str | Unset = UNSET,
    to_station: str | Unset = UNSET,
    from_stationk_v_from: float | Unset = UNSET,
    from_stationk_v_to: float | Unset = UNSET,
    to_stationk_v_from: float | Unset = UNSET,
    to_stationk_v_to: float | Unset = UNSET,
    cct_status: str | Unset = UNSET,
    sced_timestamp_from: str | Unset = UNSET,
    sced_timestamp_to: str | Unset = UNSET,
    repeated_hour_flag: bool | Unset = UNSET,
    constraint_id_from: int | Unset = UNSET,
    constraint_id_to: int | Unset = UNSET,
    constraint_name: str | Unset = UNSET,
    contingency_name: str | Unset = UNSET,
    shadow_price_from: float | Unset = UNSET,
    shadow_price_to: float | Unset = UNSET,
    max_shadow_price_from: float | Unset = UNSET,
    max_shadow_price_to: float | Unset = UNSET,
    limit_from: float | Unset = UNSET,
    limit_to: float | Unset = UNSET,
    value_from: float | Unset = UNSET,
    value_to: float | Unset = UNSET,
    violated_mw_from: float | Unset = UNSET,
    violated_mw_to: float | Unset = UNSET,
    page: int | Unset = UNSET,
    size: int | Unset = UNSET,
    sort: str | Unset = UNSET,
    dir_: str | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["fromStation"] = from_station

    params["toStation"] = to_station

    params["fromStationkVFrom"] = from_stationk_v_from

    params["fromStationkVTo"] = from_stationk_v_to

    params["toStationkVFrom"] = to_stationk_v_from

    params["toStationkVTo"] = to_stationk_v_to

    params["CCTStatus"] = cct_status

    params["SCEDTimestampFrom"] = sced_timestamp_from

    params["SCEDTimestampTo"] = sced_timestamp_to

    params["repeatedHourFlag"] = repeated_hour_flag

    params["constraintIDFrom"] = constraint_id_from

    params["constraintIDTo"] = constraint_id_to

    params["constraintName"] = constraint_name

    params["contingencyName"] = contingency_name

    params["shadowPriceFrom"] = shadow_price_from

    params["shadowPriceTo"] = shadow_price_to

    params["maxShadowPriceFrom"] = max_shadow_price_from

    params["maxShadowPriceTo"] = max_shadow_price_to

    params["limitFrom"] = limit_from

    params["limitTo"] = limit_to

    params["valueFrom"] = value_from

    params["valueTo"] = value_to

    params["violatedMWFrom"] = violated_mw_from

    params["violatedMWTo"] = violated_mw_to

    params["page"] = page

    params["size"] = size

    params["sort"] = sort

    params["dir"] = dir_

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/np6-86-cd/shdw_prices_bnd_trns_const",
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
    from_station: str | Unset = UNSET,
    to_station: str | Unset = UNSET,
    from_stationk_v_from: float | Unset = UNSET,
    from_stationk_v_to: float | Unset = UNSET,
    to_stationk_v_from: float | Unset = UNSET,
    to_stationk_v_to: float | Unset = UNSET,
    cct_status: str | Unset = UNSET,
    sced_timestamp_from: str | Unset = UNSET,
    sced_timestamp_to: str | Unset = UNSET,
    repeated_hour_flag: bool | Unset = UNSET,
    constraint_id_from: int | Unset = UNSET,
    constraint_id_to: int | Unset = UNSET,
    constraint_name: str | Unset = UNSET,
    contingency_name: str | Unset = UNSET,
    shadow_price_from: float | Unset = UNSET,
    shadow_price_to: float | Unset = UNSET,
    max_shadow_price_from: float | Unset = UNSET,
    max_shadow_price_to: float | Unset = UNSET,
    limit_from: float | Unset = UNSET,
    limit_to: float | Unset = UNSET,
    value_from: float | Unset = UNSET,
    value_to: float | Unset = UNSET,
    violated_mw_from: float | Unset = UNSET,
    violated_mw_to: float | Unset = UNSET,
    page: int | Unset = UNSET,
    size: int | Unset = UNSET,
    sort: str | Unset = UNSET,
    dir_: str | Unset = UNSET,
) -> Response[Exception_ | Report]:
    """SCED Shadow Prices and Binding Transmission Constraints

     SCED Shadow Prices and Binding Transmission Constraints

    Args:
        from_station (str | Unset):
        to_station (str | Unset):
        from_stationk_v_from (float | Unset):
        from_stationk_v_to (float | Unset):
        to_stationk_v_from (float | Unset):
        to_stationk_v_to (float | Unset):
        cct_status (str | Unset):
        sced_timestamp_from (str | Unset):
        sced_timestamp_to (str | Unset):
        repeated_hour_flag (bool | Unset):
        constraint_id_from (int | Unset):
        constraint_id_to (int | Unset):
        constraint_name (str | Unset):
        contingency_name (str | Unset):
        shadow_price_from (float | Unset):
        shadow_price_to (float | Unset):
        max_shadow_price_from (float | Unset):
        max_shadow_price_to (float | Unset):
        limit_from (float | Unset):
        limit_to (float | Unset):
        value_from (float | Unset):
        value_to (float | Unset):
        violated_mw_from (float | Unset):
        violated_mw_to (float | Unset):
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
        from_station=from_station,
        to_station=to_station,
        from_stationk_v_from=from_stationk_v_from,
        from_stationk_v_to=from_stationk_v_to,
        to_stationk_v_from=to_stationk_v_from,
        to_stationk_v_to=to_stationk_v_to,
        cct_status=cct_status,
        sced_timestamp_from=sced_timestamp_from,
        sced_timestamp_to=sced_timestamp_to,
        repeated_hour_flag=repeated_hour_flag,
        constraint_id_from=constraint_id_from,
        constraint_id_to=constraint_id_to,
        constraint_name=constraint_name,
        contingency_name=contingency_name,
        shadow_price_from=shadow_price_from,
        shadow_price_to=shadow_price_to,
        max_shadow_price_from=max_shadow_price_from,
        max_shadow_price_to=max_shadow_price_to,
        limit_from=limit_from,
        limit_to=limit_to,
        value_from=value_from,
        value_to=value_to,
        violated_mw_from=violated_mw_from,
        violated_mw_to=violated_mw_to,
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
    from_station: str | Unset = UNSET,
    to_station: str | Unset = UNSET,
    from_stationk_v_from: float | Unset = UNSET,
    from_stationk_v_to: float | Unset = UNSET,
    to_stationk_v_from: float | Unset = UNSET,
    to_stationk_v_to: float | Unset = UNSET,
    cct_status: str | Unset = UNSET,
    sced_timestamp_from: str | Unset = UNSET,
    sced_timestamp_to: str | Unset = UNSET,
    repeated_hour_flag: bool | Unset = UNSET,
    constraint_id_from: int | Unset = UNSET,
    constraint_id_to: int | Unset = UNSET,
    constraint_name: str | Unset = UNSET,
    contingency_name: str | Unset = UNSET,
    shadow_price_from: float | Unset = UNSET,
    shadow_price_to: float | Unset = UNSET,
    max_shadow_price_from: float | Unset = UNSET,
    max_shadow_price_to: float | Unset = UNSET,
    limit_from: float | Unset = UNSET,
    limit_to: float | Unset = UNSET,
    value_from: float | Unset = UNSET,
    value_to: float | Unset = UNSET,
    violated_mw_from: float | Unset = UNSET,
    violated_mw_to: float | Unset = UNSET,
    page: int | Unset = UNSET,
    size: int | Unset = UNSET,
    sort: str | Unset = UNSET,
    dir_: str | Unset = UNSET,
) -> Exception_ | Report | None:
    """SCED Shadow Prices and Binding Transmission Constraints

     SCED Shadow Prices and Binding Transmission Constraints

    Args:
        from_station (str | Unset):
        to_station (str | Unset):
        from_stationk_v_from (float | Unset):
        from_stationk_v_to (float | Unset):
        to_stationk_v_from (float | Unset):
        to_stationk_v_to (float | Unset):
        cct_status (str | Unset):
        sced_timestamp_from (str | Unset):
        sced_timestamp_to (str | Unset):
        repeated_hour_flag (bool | Unset):
        constraint_id_from (int | Unset):
        constraint_id_to (int | Unset):
        constraint_name (str | Unset):
        contingency_name (str | Unset):
        shadow_price_from (float | Unset):
        shadow_price_to (float | Unset):
        max_shadow_price_from (float | Unset):
        max_shadow_price_to (float | Unset):
        limit_from (float | Unset):
        limit_to (float | Unset):
        value_from (float | Unset):
        value_to (float | Unset):
        violated_mw_from (float | Unset):
        violated_mw_to (float | Unset):
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
        from_station=from_station,
        to_station=to_station,
        from_stationk_v_from=from_stationk_v_from,
        from_stationk_v_to=from_stationk_v_to,
        to_stationk_v_from=to_stationk_v_from,
        to_stationk_v_to=to_stationk_v_to,
        cct_status=cct_status,
        sced_timestamp_from=sced_timestamp_from,
        sced_timestamp_to=sced_timestamp_to,
        repeated_hour_flag=repeated_hour_flag,
        constraint_id_from=constraint_id_from,
        constraint_id_to=constraint_id_to,
        constraint_name=constraint_name,
        contingency_name=contingency_name,
        shadow_price_from=shadow_price_from,
        shadow_price_to=shadow_price_to,
        max_shadow_price_from=max_shadow_price_from,
        max_shadow_price_to=max_shadow_price_to,
        limit_from=limit_from,
        limit_to=limit_to,
        value_from=value_from,
        value_to=value_to,
        violated_mw_from=violated_mw_from,
        violated_mw_to=violated_mw_to,
        page=page,
        size=size,
        sort=sort,
        dir_=dir_,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    from_station: str | Unset = UNSET,
    to_station: str | Unset = UNSET,
    from_stationk_v_from: float | Unset = UNSET,
    from_stationk_v_to: float | Unset = UNSET,
    to_stationk_v_from: float | Unset = UNSET,
    to_stationk_v_to: float | Unset = UNSET,
    cct_status: str | Unset = UNSET,
    sced_timestamp_from: str | Unset = UNSET,
    sced_timestamp_to: str | Unset = UNSET,
    repeated_hour_flag: bool | Unset = UNSET,
    constraint_id_from: int | Unset = UNSET,
    constraint_id_to: int | Unset = UNSET,
    constraint_name: str | Unset = UNSET,
    contingency_name: str | Unset = UNSET,
    shadow_price_from: float | Unset = UNSET,
    shadow_price_to: float | Unset = UNSET,
    max_shadow_price_from: float | Unset = UNSET,
    max_shadow_price_to: float | Unset = UNSET,
    limit_from: float | Unset = UNSET,
    limit_to: float | Unset = UNSET,
    value_from: float | Unset = UNSET,
    value_to: float | Unset = UNSET,
    violated_mw_from: float | Unset = UNSET,
    violated_mw_to: float | Unset = UNSET,
    page: int | Unset = UNSET,
    size: int | Unset = UNSET,
    sort: str | Unset = UNSET,
    dir_: str | Unset = UNSET,
) -> Response[Exception_ | Report]:
    """SCED Shadow Prices and Binding Transmission Constraints

     SCED Shadow Prices and Binding Transmission Constraints

    Args:
        from_station (str | Unset):
        to_station (str | Unset):
        from_stationk_v_from (float | Unset):
        from_stationk_v_to (float | Unset):
        to_stationk_v_from (float | Unset):
        to_stationk_v_to (float | Unset):
        cct_status (str | Unset):
        sced_timestamp_from (str | Unset):
        sced_timestamp_to (str | Unset):
        repeated_hour_flag (bool | Unset):
        constraint_id_from (int | Unset):
        constraint_id_to (int | Unset):
        constraint_name (str | Unset):
        contingency_name (str | Unset):
        shadow_price_from (float | Unset):
        shadow_price_to (float | Unset):
        max_shadow_price_from (float | Unset):
        max_shadow_price_to (float | Unset):
        limit_from (float | Unset):
        limit_to (float | Unset):
        value_from (float | Unset):
        value_to (float | Unset):
        violated_mw_from (float | Unset):
        violated_mw_to (float | Unset):
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
        from_station=from_station,
        to_station=to_station,
        from_stationk_v_from=from_stationk_v_from,
        from_stationk_v_to=from_stationk_v_to,
        to_stationk_v_from=to_stationk_v_from,
        to_stationk_v_to=to_stationk_v_to,
        cct_status=cct_status,
        sced_timestamp_from=sced_timestamp_from,
        sced_timestamp_to=sced_timestamp_to,
        repeated_hour_flag=repeated_hour_flag,
        constraint_id_from=constraint_id_from,
        constraint_id_to=constraint_id_to,
        constraint_name=constraint_name,
        contingency_name=contingency_name,
        shadow_price_from=shadow_price_from,
        shadow_price_to=shadow_price_to,
        max_shadow_price_from=max_shadow_price_from,
        max_shadow_price_to=max_shadow_price_to,
        limit_from=limit_from,
        limit_to=limit_to,
        value_from=value_from,
        value_to=value_to,
        violated_mw_from=violated_mw_from,
        violated_mw_to=violated_mw_to,
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
    from_station: str | Unset = UNSET,
    to_station: str | Unset = UNSET,
    from_stationk_v_from: float | Unset = UNSET,
    from_stationk_v_to: float | Unset = UNSET,
    to_stationk_v_from: float | Unset = UNSET,
    to_stationk_v_to: float | Unset = UNSET,
    cct_status: str | Unset = UNSET,
    sced_timestamp_from: str | Unset = UNSET,
    sced_timestamp_to: str | Unset = UNSET,
    repeated_hour_flag: bool | Unset = UNSET,
    constraint_id_from: int | Unset = UNSET,
    constraint_id_to: int | Unset = UNSET,
    constraint_name: str | Unset = UNSET,
    contingency_name: str | Unset = UNSET,
    shadow_price_from: float | Unset = UNSET,
    shadow_price_to: float | Unset = UNSET,
    max_shadow_price_from: float | Unset = UNSET,
    max_shadow_price_to: float | Unset = UNSET,
    limit_from: float | Unset = UNSET,
    limit_to: float | Unset = UNSET,
    value_from: float | Unset = UNSET,
    value_to: float | Unset = UNSET,
    violated_mw_from: float | Unset = UNSET,
    violated_mw_to: float | Unset = UNSET,
    page: int | Unset = UNSET,
    size: int | Unset = UNSET,
    sort: str | Unset = UNSET,
    dir_: str | Unset = UNSET,
) -> Exception_ | Report | None:
    """SCED Shadow Prices and Binding Transmission Constraints

     SCED Shadow Prices and Binding Transmission Constraints

    Args:
        from_station (str | Unset):
        to_station (str | Unset):
        from_stationk_v_from (float | Unset):
        from_stationk_v_to (float | Unset):
        to_stationk_v_from (float | Unset):
        to_stationk_v_to (float | Unset):
        cct_status (str | Unset):
        sced_timestamp_from (str | Unset):
        sced_timestamp_to (str | Unset):
        repeated_hour_flag (bool | Unset):
        constraint_id_from (int | Unset):
        constraint_id_to (int | Unset):
        constraint_name (str | Unset):
        contingency_name (str | Unset):
        shadow_price_from (float | Unset):
        shadow_price_to (float | Unset):
        max_shadow_price_from (float | Unset):
        max_shadow_price_to (float | Unset):
        limit_from (float | Unset):
        limit_to (float | Unset):
        value_from (float | Unset):
        value_to (float | Unset):
        violated_mw_from (float | Unset):
        violated_mw_to (float | Unset):
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
            from_station=from_station,
            to_station=to_station,
            from_stationk_v_from=from_stationk_v_from,
            from_stationk_v_to=from_stationk_v_to,
            to_stationk_v_from=to_stationk_v_from,
            to_stationk_v_to=to_stationk_v_to,
            cct_status=cct_status,
            sced_timestamp_from=sced_timestamp_from,
            sced_timestamp_to=sced_timestamp_to,
            repeated_hour_flag=repeated_hour_flag,
            constraint_id_from=constraint_id_from,
            constraint_id_to=constraint_id_to,
            constraint_name=constraint_name,
            contingency_name=contingency_name,
            shadow_price_from=shadow_price_from,
            shadow_price_to=shadow_price_to,
            max_shadow_price_from=max_shadow_price_from,
            max_shadow_price_to=max_shadow_price_to,
            limit_from=limit_from,
            limit_to=limit_to,
            value_from=value_from,
            value_to=value_to,
            violated_mw_from=violated_mw_from,
            violated_mw_to=violated_mw_to,
            page=page,
            size=size,
            sort=sort,
            dir_=dir_,
        )
    ).parsed
