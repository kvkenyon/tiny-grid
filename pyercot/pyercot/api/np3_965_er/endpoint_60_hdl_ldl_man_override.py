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
    participant_name: str | Unset = UNSET,
    resource_name: str | Unset = UNSET,
    hdl_original_from: float | Unset = UNSET,
    hdl_original_to: float | Unset = UNSET,
    hdl_manual_from: float | Unset = UNSET,
    hdl_manual_to: float | Unset = UNSET,
    hdl_final_from: float | Unset = UNSET,
    hdl_final_to: float | Unset = UNSET,
    ldl_original_from: float | Unset = UNSET,
    ldl_original_to: float | Unset = UNSET,
    ldl_manual_from: float | Unset = UNSET,
    ldl_manual_to: float | Unset = UNSET,
    ldl_final_from: float | Unset = UNSET,
    ldl_final_to: float | Unset = UNSET,
    reason_code: str | Unset = UNSET,
    page: int | Unset = UNSET,
    size: int | Unset = UNSET,
    sort: str | Unset = UNSET,
    dir_: str | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["SCEDTimestampFrom"] = sced_timestamp_from

    params["SCEDTimestampTo"] = sced_timestamp_to

    params["repeatHourFlag"] = repeat_hour_flag

    params["participantName"] = participant_name

    params["resourceName"] = resource_name

    params["HDLOriginalFrom"] = hdl_original_from

    params["HDLOriginalTo"] = hdl_original_to

    params["HDLManualFrom"] = hdl_manual_from

    params["HDLManualTo"] = hdl_manual_to

    params["HDLFinalFrom"] = hdl_final_from

    params["HDLFinalTo"] = hdl_final_to

    params["LDLOriginalFrom"] = ldl_original_from

    params["LDLOriginalTo"] = ldl_original_to

    params["LDLManualFrom"] = ldl_manual_from

    params["LDLManualTo"] = ldl_manual_to

    params["LDLFinalFrom"] = ldl_final_from

    params["LDLFinalTo"] = ldl_final_to

    params["reasonCode"] = reason_code

    params["page"] = page

    params["size"] = size

    params["sort"] = sort

    params["dir"] = dir_

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/np3-965-er/60_hdl_ldl_man_override",
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
    participant_name: str | Unset = UNSET,
    resource_name: str | Unset = UNSET,
    hdl_original_from: float | Unset = UNSET,
    hdl_original_to: float | Unset = UNSET,
    hdl_manual_from: float | Unset = UNSET,
    hdl_manual_to: float | Unset = UNSET,
    hdl_final_from: float | Unset = UNSET,
    hdl_final_to: float | Unset = UNSET,
    ldl_original_from: float | Unset = UNSET,
    ldl_original_to: float | Unset = UNSET,
    ldl_manual_from: float | Unset = UNSET,
    ldl_manual_to: float | Unset = UNSET,
    ldl_final_from: float | Unset = UNSET,
    ldl_final_to: float | Unset = UNSET,
    reason_code: str | Unset = UNSET,
    page: int | Unset = UNSET,
    size: int | Unset = UNSET,
    sort: str | Unset = UNSET,
    dir_: str | Unset = UNSET,
) -> Response[Exception_ | Report]:
    """60 Day HDL and LDL Manual Override Summary

     60 Day HDL and LDL Manual Override Summary

    Args:
        sced_timestamp_from (str | Unset):
        sced_timestamp_to (str | Unset):
        repeat_hour_flag (bool | Unset):
        participant_name (str | Unset):
        resource_name (str | Unset):
        hdl_original_from (float | Unset):
        hdl_original_to (float | Unset):
        hdl_manual_from (float | Unset):
        hdl_manual_to (float | Unset):
        hdl_final_from (float | Unset):
        hdl_final_to (float | Unset):
        ldl_original_from (float | Unset):
        ldl_original_to (float | Unset):
        ldl_manual_from (float | Unset):
        ldl_manual_to (float | Unset):
        ldl_final_from (float | Unset):
        ldl_final_to (float | Unset):
        reason_code (str | Unset):
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
        participant_name=participant_name,
        resource_name=resource_name,
        hdl_original_from=hdl_original_from,
        hdl_original_to=hdl_original_to,
        hdl_manual_from=hdl_manual_from,
        hdl_manual_to=hdl_manual_to,
        hdl_final_from=hdl_final_from,
        hdl_final_to=hdl_final_to,
        ldl_original_from=ldl_original_from,
        ldl_original_to=ldl_original_to,
        ldl_manual_from=ldl_manual_from,
        ldl_manual_to=ldl_manual_to,
        ldl_final_from=ldl_final_from,
        ldl_final_to=ldl_final_to,
        reason_code=reason_code,
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
    participant_name: str | Unset = UNSET,
    resource_name: str | Unset = UNSET,
    hdl_original_from: float | Unset = UNSET,
    hdl_original_to: float | Unset = UNSET,
    hdl_manual_from: float | Unset = UNSET,
    hdl_manual_to: float | Unset = UNSET,
    hdl_final_from: float | Unset = UNSET,
    hdl_final_to: float | Unset = UNSET,
    ldl_original_from: float | Unset = UNSET,
    ldl_original_to: float | Unset = UNSET,
    ldl_manual_from: float | Unset = UNSET,
    ldl_manual_to: float | Unset = UNSET,
    ldl_final_from: float | Unset = UNSET,
    ldl_final_to: float | Unset = UNSET,
    reason_code: str | Unset = UNSET,
    page: int | Unset = UNSET,
    size: int | Unset = UNSET,
    sort: str | Unset = UNSET,
    dir_: str | Unset = UNSET,
) -> Exception_ | Report | None:
    """60 Day HDL and LDL Manual Override Summary

     60 Day HDL and LDL Manual Override Summary

    Args:
        sced_timestamp_from (str | Unset):
        sced_timestamp_to (str | Unset):
        repeat_hour_flag (bool | Unset):
        participant_name (str | Unset):
        resource_name (str | Unset):
        hdl_original_from (float | Unset):
        hdl_original_to (float | Unset):
        hdl_manual_from (float | Unset):
        hdl_manual_to (float | Unset):
        hdl_final_from (float | Unset):
        hdl_final_to (float | Unset):
        ldl_original_from (float | Unset):
        ldl_original_to (float | Unset):
        ldl_manual_from (float | Unset):
        ldl_manual_to (float | Unset):
        ldl_final_from (float | Unset):
        ldl_final_to (float | Unset):
        reason_code (str | Unset):
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
        participant_name=participant_name,
        resource_name=resource_name,
        hdl_original_from=hdl_original_from,
        hdl_original_to=hdl_original_to,
        hdl_manual_from=hdl_manual_from,
        hdl_manual_to=hdl_manual_to,
        hdl_final_from=hdl_final_from,
        hdl_final_to=hdl_final_to,
        ldl_original_from=ldl_original_from,
        ldl_original_to=ldl_original_to,
        ldl_manual_from=ldl_manual_from,
        ldl_manual_to=ldl_manual_to,
        ldl_final_from=ldl_final_from,
        ldl_final_to=ldl_final_to,
        reason_code=reason_code,
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
    participant_name: str | Unset = UNSET,
    resource_name: str | Unset = UNSET,
    hdl_original_from: float | Unset = UNSET,
    hdl_original_to: float | Unset = UNSET,
    hdl_manual_from: float | Unset = UNSET,
    hdl_manual_to: float | Unset = UNSET,
    hdl_final_from: float | Unset = UNSET,
    hdl_final_to: float | Unset = UNSET,
    ldl_original_from: float | Unset = UNSET,
    ldl_original_to: float | Unset = UNSET,
    ldl_manual_from: float | Unset = UNSET,
    ldl_manual_to: float | Unset = UNSET,
    ldl_final_from: float | Unset = UNSET,
    ldl_final_to: float | Unset = UNSET,
    reason_code: str | Unset = UNSET,
    page: int | Unset = UNSET,
    size: int | Unset = UNSET,
    sort: str | Unset = UNSET,
    dir_: str | Unset = UNSET,
) -> Response[Exception_ | Report]:
    """60 Day HDL and LDL Manual Override Summary

     60 Day HDL and LDL Manual Override Summary

    Args:
        sced_timestamp_from (str | Unset):
        sced_timestamp_to (str | Unset):
        repeat_hour_flag (bool | Unset):
        participant_name (str | Unset):
        resource_name (str | Unset):
        hdl_original_from (float | Unset):
        hdl_original_to (float | Unset):
        hdl_manual_from (float | Unset):
        hdl_manual_to (float | Unset):
        hdl_final_from (float | Unset):
        hdl_final_to (float | Unset):
        ldl_original_from (float | Unset):
        ldl_original_to (float | Unset):
        ldl_manual_from (float | Unset):
        ldl_manual_to (float | Unset):
        ldl_final_from (float | Unset):
        ldl_final_to (float | Unset):
        reason_code (str | Unset):
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
        participant_name=participant_name,
        resource_name=resource_name,
        hdl_original_from=hdl_original_from,
        hdl_original_to=hdl_original_to,
        hdl_manual_from=hdl_manual_from,
        hdl_manual_to=hdl_manual_to,
        hdl_final_from=hdl_final_from,
        hdl_final_to=hdl_final_to,
        ldl_original_from=ldl_original_from,
        ldl_original_to=ldl_original_to,
        ldl_manual_from=ldl_manual_from,
        ldl_manual_to=ldl_manual_to,
        ldl_final_from=ldl_final_from,
        ldl_final_to=ldl_final_to,
        reason_code=reason_code,
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
    participant_name: str | Unset = UNSET,
    resource_name: str | Unset = UNSET,
    hdl_original_from: float | Unset = UNSET,
    hdl_original_to: float | Unset = UNSET,
    hdl_manual_from: float | Unset = UNSET,
    hdl_manual_to: float | Unset = UNSET,
    hdl_final_from: float | Unset = UNSET,
    hdl_final_to: float | Unset = UNSET,
    ldl_original_from: float | Unset = UNSET,
    ldl_original_to: float | Unset = UNSET,
    ldl_manual_from: float | Unset = UNSET,
    ldl_manual_to: float | Unset = UNSET,
    ldl_final_from: float | Unset = UNSET,
    ldl_final_to: float | Unset = UNSET,
    reason_code: str | Unset = UNSET,
    page: int | Unset = UNSET,
    size: int | Unset = UNSET,
    sort: str | Unset = UNSET,
    dir_: str | Unset = UNSET,
) -> Exception_ | Report | None:
    """60 Day HDL and LDL Manual Override Summary

     60 Day HDL and LDL Manual Override Summary

    Args:
        sced_timestamp_from (str | Unset):
        sced_timestamp_to (str | Unset):
        repeat_hour_flag (bool | Unset):
        participant_name (str | Unset):
        resource_name (str | Unset):
        hdl_original_from (float | Unset):
        hdl_original_to (float | Unset):
        hdl_manual_from (float | Unset):
        hdl_manual_to (float | Unset):
        hdl_final_from (float | Unset):
        hdl_final_to (float | Unset):
        ldl_original_from (float | Unset):
        ldl_original_to (float | Unset):
        ldl_manual_from (float | Unset):
        ldl_manual_to (float | Unset):
        ldl_final_from (float | Unset):
        ldl_final_to (float | Unset):
        reason_code (str | Unset):
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
            participant_name=participant_name,
            resource_name=resource_name,
            hdl_original_from=hdl_original_from,
            hdl_original_to=hdl_original_to,
            hdl_manual_from=hdl_manual_from,
            hdl_manual_to=hdl_manual_to,
            hdl_final_from=hdl_final_from,
            hdl_final_to=hdl_final_to,
            ldl_original_from=ldl_original_from,
            ldl_original_to=ldl_original_to,
            ldl_manual_from=ldl_manual_from,
            ldl_manual_to=ldl_manual_to,
            ldl_final_from=ldl_final_from,
            ldl_final_to=ldl_final_to,
            reason_code=reason_code,
            page=page,
            size=size,
            sort=sort,
            dir_=dir_,
        )
    ).parsed
