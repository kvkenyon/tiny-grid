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
    constraint_id_from: int | Unset = UNSET,
    constraint_id_to: int | Unset = UNSET,
    constraint_name: str | Unset = UNSET,
    contingency_name: str | Unset = UNSET,
    constraint_limit_from: int | Unset = UNSET,
    constraint_limit_to: int | Unset = UNSET,
    constraint_value_from: int | Unset = UNSET,
    constraint_value_to: int | Unset = UNSET,
    violation_amount_from: int | Unset = UNSET,
    violation_amount_to: int | Unset = UNSET,
    shadow_price_from: float | Unset = UNSET,
    shadow_price_to: float | Unset = UNSET,
    from_station: str | Unset = UNSET,
    to_station: str | Unset = UNSET,
    from_stationk_v_from: float | Unset = UNSET,
    from_stationk_v_to: float | Unset = UNSET,
    to_stationk_v_from: float | Unset = UNSET,
    to_stationk_v_to: float | Unset = UNSET,
    delivery_time_from: str | Unset = UNSET,
    delivery_time_to: str | Unset = UNSET,
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

    params["constraintIdFrom"] = constraint_id_from

    params["constraintIdTo"] = constraint_id_to

    params["constraintName"] = constraint_name

    params["contingencyName"] = contingency_name

    params["constraintLimitFrom"] = constraint_limit_from

    params["constraintLimitTo"] = constraint_limit_to

    params["constraintValueFrom"] = constraint_value_from

    params["constraintValueTo"] = constraint_value_to

    params["violationAmountFrom"] = violation_amount_from

    params["violationAmountTo"] = violation_amount_to

    params["shadowPriceFrom"] = shadow_price_from

    params["shadowPriceTo"] = shadow_price_to

    params["fromStation"] = from_station

    params["toStation"] = to_station

    params["fromStationkVFrom"] = from_stationk_v_from

    params["fromStationkVTo"] = from_stationk_v_to

    params["toStationkVFrom"] = to_stationk_v_from

    params["toStationkVTo"] = to_stationk_v_to

    params["deliveryTimeFrom"] = delivery_time_from

    params["deliveryTimeTo"] = delivery_time_to

    params["DSTFlag"] = dst_flag

    params["page"] = page

    params["size"] = size

    params["sort"] = sort

    params["dir"] = dir_

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/np4-191-cd/dam_shadow_prices",
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
    constraint_id_from: int | Unset = UNSET,
    constraint_id_to: int | Unset = UNSET,
    constraint_name: str | Unset = UNSET,
    contingency_name: str | Unset = UNSET,
    constraint_limit_from: int | Unset = UNSET,
    constraint_limit_to: int | Unset = UNSET,
    constraint_value_from: int | Unset = UNSET,
    constraint_value_to: int | Unset = UNSET,
    violation_amount_from: int | Unset = UNSET,
    violation_amount_to: int | Unset = UNSET,
    shadow_price_from: float | Unset = UNSET,
    shadow_price_to: float | Unset = UNSET,
    from_station: str | Unset = UNSET,
    to_station: str | Unset = UNSET,
    from_stationk_v_from: float | Unset = UNSET,
    from_stationk_v_to: float | Unset = UNSET,
    to_stationk_v_from: float | Unset = UNSET,
    to_stationk_v_to: float | Unset = UNSET,
    delivery_time_from: str | Unset = UNSET,
    delivery_time_to: str | Unset = UNSET,
    dst_flag: bool | Unset = UNSET,
    page: int | Unset = UNSET,
    size: int | Unset = UNSET,
    sort: str | Unset = UNSET,
    dir_: str | Unset = UNSET,
) -> Response[Exception_ | Report]:
    """DAM Shadow Prices

     DAM Shadow Prices

    Args:
        delivery_date_from (str | Unset):
        delivery_date_to (str | Unset):
        hour_ending (str | Unset):
        constraint_id_from (int | Unset):
        constraint_id_to (int | Unset):
        constraint_name (str | Unset):
        contingency_name (str | Unset):
        constraint_limit_from (int | Unset):
        constraint_limit_to (int | Unset):
        constraint_value_from (int | Unset):
        constraint_value_to (int | Unset):
        violation_amount_from (int | Unset):
        violation_amount_to (int | Unset):
        shadow_price_from (float | Unset):
        shadow_price_to (float | Unset):
        from_station (str | Unset):
        to_station (str | Unset):
        from_stationk_v_from (float | Unset):
        from_stationk_v_to (float | Unset):
        to_stationk_v_from (float | Unset):
        to_stationk_v_to (float | Unset):
        delivery_time_from (str | Unset):
        delivery_time_to (str | Unset):
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
        constraint_id_from=constraint_id_from,
        constraint_id_to=constraint_id_to,
        constraint_name=constraint_name,
        contingency_name=contingency_name,
        constraint_limit_from=constraint_limit_from,
        constraint_limit_to=constraint_limit_to,
        constraint_value_from=constraint_value_from,
        constraint_value_to=constraint_value_to,
        violation_amount_from=violation_amount_from,
        violation_amount_to=violation_amount_to,
        shadow_price_from=shadow_price_from,
        shadow_price_to=shadow_price_to,
        from_station=from_station,
        to_station=to_station,
        from_stationk_v_from=from_stationk_v_from,
        from_stationk_v_to=from_stationk_v_to,
        to_stationk_v_from=to_stationk_v_from,
        to_stationk_v_to=to_stationk_v_to,
        delivery_time_from=delivery_time_from,
        delivery_time_to=delivery_time_to,
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
    constraint_id_from: int | Unset = UNSET,
    constraint_id_to: int | Unset = UNSET,
    constraint_name: str | Unset = UNSET,
    contingency_name: str | Unset = UNSET,
    constraint_limit_from: int | Unset = UNSET,
    constraint_limit_to: int | Unset = UNSET,
    constraint_value_from: int | Unset = UNSET,
    constraint_value_to: int | Unset = UNSET,
    violation_amount_from: int | Unset = UNSET,
    violation_amount_to: int | Unset = UNSET,
    shadow_price_from: float | Unset = UNSET,
    shadow_price_to: float | Unset = UNSET,
    from_station: str | Unset = UNSET,
    to_station: str | Unset = UNSET,
    from_stationk_v_from: float | Unset = UNSET,
    from_stationk_v_to: float | Unset = UNSET,
    to_stationk_v_from: float | Unset = UNSET,
    to_stationk_v_to: float | Unset = UNSET,
    delivery_time_from: str | Unset = UNSET,
    delivery_time_to: str | Unset = UNSET,
    dst_flag: bool | Unset = UNSET,
    page: int | Unset = UNSET,
    size: int | Unset = UNSET,
    sort: str | Unset = UNSET,
    dir_: str | Unset = UNSET,
) -> Exception_ | Report | None:
    """DAM Shadow Prices

     DAM Shadow Prices

    Args:
        delivery_date_from (str | Unset):
        delivery_date_to (str | Unset):
        hour_ending (str | Unset):
        constraint_id_from (int | Unset):
        constraint_id_to (int | Unset):
        constraint_name (str | Unset):
        contingency_name (str | Unset):
        constraint_limit_from (int | Unset):
        constraint_limit_to (int | Unset):
        constraint_value_from (int | Unset):
        constraint_value_to (int | Unset):
        violation_amount_from (int | Unset):
        violation_amount_to (int | Unset):
        shadow_price_from (float | Unset):
        shadow_price_to (float | Unset):
        from_station (str | Unset):
        to_station (str | Unset):
        from_stationk_v_from (float | Unset):
        from_stationk_v_to (float | Unset):
        to_stationk_v_from (float | Unset):
        to_stationk_v_to (float | Unset):
        delivery_time_from (str | Unset):
        delivery_time_to (str | Unset):
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
        constraint_id_from=constraint_id_from,
        constraint_id_to=constraint_id_to,
        constraint_name=constraint_name,
        contingency_name=contingency_name,
        constraint_limit_from=constraint_limit_from,
        constraint_limit_to=constraint_limit_to,
        constraint_value_from=constraint_value_from,
        constraint_value_to=constraint_value_to,
        violation_amount_from=violation_amount_from,
        violation_amount_to=violation_amount_to,
        shadow_price_from=shadow_price_from,
        shadow_price_to=shadow_price_to,
        from_station=from_station,
        to_station=to_station,
        from_stationk_v_from=from_stationk_v_from,
        from_stationk_v_to=from_stationk_v_to,
        to_stationk_v_from=to_stationk_v_from,
        to_stationk_v_to=to_stationk_v_to,
        delivery_time_from=delivery_time_from,
        delivery_time_to=delivery_time_to,
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
    constraint_id_from: int | Unset = UNSET,
    constraint_id_to: int | Unset = UNSET,
    constraint_name: str | Unset = UNSET,
    contingency_name: str | Unset = UNSET,
    constraint_limit_from: int | Unset = UNSET,
    constraint_limit_to: int | Unset = UNSET,
    constraint_value_from: int | Unset = UNSET,
    constraint_value_to: int | Unset = UNSET,
    violation_amount_from: int | Unset = UNSET,
    violation_amount_to: int | Unset = UNSET,
    shadow_price_from: float | Unset = UNSET,
    shadow_price_to: float | Unset = UNSET,
    from_station: str | Unset = UNSET,
    to_station: str | Unset = UNSET,
    from_stationk_v_from: float | Unset = UNSET,
    from_stationk_v_to: float | Unset = UNSET,
    to_stationk_v_from: float | Unset = UNSET,
    to_stationk_v_to: float | Unset = UNSET,
    delivery_time_from: str | Unset = UNSET,
    delivery_time_to: str | Unset = UNSET,
    dst_flag: bool | Unset = UNSET,
    page: int | Unset = UNSET,
    size: int | Unset = UNSET,
    sort: str | Unset = UNSET,
    dir_: str | Unset = UNSET,
) -> Response[Exception_ | Report]:
    """DAM Shadow Prices

     DAM Shadow Prices

    Args:
        delivery_date_from (str | Unset):
        delivery_date_to (str | Unset):
        hour_ending (str | Unset):
        constraint_id_from (int | Unset):
        constraint_id_to (int | Unset):
        constraint_name (str | Unset):
        contingency_name (str | Unset):
        constraint_limit_from (int | Unset):
        constraint_limit_to (int | Unset):
        constraint_value_from (int | Unset):
        constraint_value_to (int | Unset):
        violation_amount_from (int | Unset):
        violation_amount_to (int | Unset):
        shadow_price_from (float | Unset):
        shadow_price_to (float | Unset):
        from_station (str | Unset):
        to_station (str | Unset):
        from_stationk_v_from (float | Unset):
        from_stationk_v_to (float | Unset):
        to_stationk_v_from (float | Unset):
        to_stationk_v_to (float | Unset):
        delivery_time_from (str | Unset):
        delivery_time_to (str | Unset):
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
        constraint_id_from=constraint_id_from,
        constraint_id_to=constraint_id_to,
        constraint_name=constraint_name,
        contingency_name=contingency_name,
        constraint_limit_from=constraint_limit_from,
        constraint_limit_to=constraint_limit_to,
        constraint_value_from=constraint_value_from,
        constraint_value_to=constraint_value_to,
        violation_amount_from=violation_amount_from,
        violation_amount_to=violation_amount_to,
        shadow_price_from=shadow_price_from,
        shadow_price_to=shadow_price_to,
        from_station=from_station,
        to_station=to_station,
        from_stationk_v_from=from_stationk_v_from,
        from_stationk_v_to=from_stationk_v_to,
        to_stationk_v_from=to_stationk_v_from,
        to_stationk_v_to=to_stationk_v_to,
        delivery_time_from=delivery_time_from,
        delivery_time_to=delivery_time_to,
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
    constraint_id_from: int | Unset = UNSET,
    constraint_id_to: int | Unset = UNSET,
    constraint_name: str | Unset = UNSET,
    contingency_name: str | Unset = UNSET,
    constraint_limit_from: int | Unset = UNSET,
    constraint_limit_to: int | Unset = UNSET,
    constraint_value_from: int | Unset = UNSET,
    constraint_value_to: int | Unset = UNSET,
    violation_amount_from: int | Unset = UNSET,
    violation_amount_to: int | Unset = UNSET,
    shadow_price_from: float | Unset = UNSET,
    shadow_price_to: float | Unset = UNSET,
    from_station: str | Unset = UNSET,
    to_station: str | Unset = UNSET,
    from_stationk_v_from: float | Unset = UNSET,
    from_stationk_v_to: float | Unset = UNSET,
    to_stationk_v_from: float | Unset = UNSET,
    to_stationk_v_to: float | Unset = UNSET,
    delivery_time_from: str | Unset = UNSET,
    delivery_time_to: str | Unset = UNSET,
    dst_flag: bool | Unset = UNSET,
    page: int | Unset = UNSET,
    size: int | Unset = UNSET,
    sort: str | Unset = UNSET,
    dir_: str | Unset = UNSET,
) -> Exception_ | Report | None:
    """DAM Shadow Prices

     DAM Shadow Prices

    Args:
        delivery_date_from (str | Unset):
        delivery_date_to (str | Unset):
        hour_ending (str | Unset):
        constraint_id_from (int | Unset):
        constraint_id_to (int | Unset):
        constraint_name (str | Unset):
        contingency_name (str | Unset):
        constraint_limit_from (int | Unset):
        constraint_limit_to (int | Unset):
        constraint_value_from (int | Unset):
        constraint_value_to (int | Unset):
        violation_amount_from (int | Unset):
        violation_amount_to (int | Unset):
        shadow_price_from (float | Unset):
        shadow_price_to (float | Unset):
        from_station (str | Unset):
        to_station (str | Unset):
        from_stationk_v_from (float | Unset):
        from_stationk_v_to (float | Unset):
        to_stationk_v_from (float | Unset):
        to_stationk_v_to (float | Unset):
        delivery_time_from (str | Unset):
        delivery_time_to (str | Unset):
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
            constraint_id_from=constraint_id_from,
            constraint_id_to=constraint_id_to,
            constraint_name=constraint_name,
            contingency_name=contingency_name,
            constraint_limit_from=constraint_limit_from,
            constraint_limit_to=constraint_limit_to,
            constraint_value_from=constraint_value_from,
            constraint_value_to=constraint_value_to,
            violation_amount_from=violation_amount_from,
            violation_amount_to=violation_amount_to,
            shadow_price_from=shadow_price_from,
            shadow_price_to=shadow_price_to,
            from_station=from_station,
            to_station=to_station,
            from_stationk_v_from=from_stationk_v_from,
            from_stationk_v_to=from_stationk_v_to,
            to_stationk_v_from=to_stationk_v_from,
            to_stationk_v_to=to_stationk_v_to,
            delivery_time_from=delivery_time_from,
            delivery_time_to=delivery_time_to,
            dst_flag=dst_flag,
            page=page,
            size=size,
            sort=sort,
            dir_=dir_,
        )
    ).parsed
