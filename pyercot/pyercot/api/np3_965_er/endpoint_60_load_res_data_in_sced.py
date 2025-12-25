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
    as_resp_for_nspin_from: float | Unset = UNSET,
    as_resp_for_nspin_to: float | Unset = UNSET,
    as_resp_for_regup_from: float | Unset = UNSET,
    as_resp_for_regup_to: float | Unset = UNSET,
    as_resp_for_regdn_from: float | Unset = UNSET,
    as_resp_for_regdn_to: float | Unset = UNSET,
    sced_bid_curve_mw1_from: float | Unset = UNSET,
    sced_bid_curve_mw1_to: float | Unset = UNSET,
    sced_bid_curve_price_1_from: float | Unset = UNSET,
    sced_bid_curve_price_1_to: float | Unset = UNSET,
    sced_bid_curve_mw2_from: float | Unset = UNSET,
    sced_bid_curve_mw2_to: float | Unset = UNSET,
    sced_bid_curve_price_2_from: float | Unset = UNSET,
    sced_bid_curve_price_2_to: float | Unset = UNSET,
    sced_bid_curve_mw3_from: float | Unset = UNSET,
    sced_bid_curve_mw3_to: float | Unset = UNSET,
    sced_bid_curve_price_3_from: float | Unset = UNSET,
    sced_bid_curve_price_3_to: float | Unset = UNSET,
    sced_bid_curve_mw4_from: float | Unset = UNSET,
    sced_bid_curve_mw4_to: float | Unset = UNSET,
    sced_bid_curve_price_4_from: float | Unset = UNSET,
    sced_bid_curve_price_4_to: float | Unset = UNSET,
    sced_bid_curve_mw5_from: float | Unset = UNSET,
    sced_bid_curve_mw5_to: float | Unset = UNSET,
    sced_bid_curve_price_5_from: float | Unset = UNSET,
    sced_bid_curve_price_5_to: float | Unset = UNSET,
    sced_bid_curve_mw6_from: float | Unset = UNSET,
    sced_bid_curve_mw6_to: float | Unset = UNSET,
    sced_bid_curve_price_6_from: float | Unset = UNSET,
    sced_bid_curve_price_6_to: float | Unset = UNSET,
    sced_bid_curve_mw7_from: float | Unset = UNSET,
    sced_bid_curve_mw7_to: float | Unset = UNSET,
    sced_bid_curve_price_7_from: float | Unset = UNSET,
    sced_bid_curve_price_7_to: float | Unset = UNSET,
    sced_bid_curve_mw8_from: float | Unset = UNSET,
    sced_bid_curve_mw8_to: float | Unset = UNSET,
    sced_bid_curve_price_8_from: float | Unset = UNSET,
    sced_bid_curve_price_8_to: float | Unset = UNSET,
    sced_bid_curve_mw9_from: float | Unset = UNSET,
    sced_bid_curve_mw9_to: float | Unset = UNSET,
    sced_bid_curve_price_9_from: float | Unset = UNSET,
    sced_bid_curve_price_9_to: float | Unset = UNSET,
    sced_bid_curve_mw10_from: float | Unset = UNSET,
    sced_bid_curve_mw10_to: float | Unset = UNSET,
    sced_bid_curve_price_10_from: float | Unset = UNSET,
    sced_bid_curve_price_10_to: float | Unset = UNSET,
    hasl_from: float | Unset = UNSET,
    hasl_to: float | Unset = UNSET,
    hdl_from: float | Unset = UNSET,
    hdl_to: float | Unset = UNSET,
    lasl_from: float | Unset = UNSET,
    lasl_to: float | Unset = UNSET,
    ldl_from: float | Unset = UNSET,
    ldl_to: float | Unset = UNSET,
    base_point_from: float | Unset = UNSET,
    base_point_to: float | Unset = UNSET,
    sced_timestamp_from: str | Unset = UNSET,
    sced_timestamp_to: str | Unset = UNSET,
    repeat_hour_flag: bool | Unset = UNSET,
    qse_name: str | Unset = UNSET,
    dme_name: str | Unset = UNSET,
    resource_name: str | Unset = UNSET,
    tel_res_status: str | Unset = UNSET,
    max_power_consumption_from: float | Unset = UNSET,
    max_power_consumption_to: float | Unset = UNSET,
    low_power_consumption_from: float | Unset = UNSET,
    low_power_consumption_to: float | Unset = UNSET,
    real_power_consumption_from: float | Unset = UNSET,
    real_power_consumption_to: float | Unset = UNSET,
    as_resp_for_rrs_from: float | Unset = UNSET,
    as_resp_for_rrs_to: float | Unset = UNSET,
    as_resp_for_rrsffr_from: float | Unset = UNSET,
    as_resp_for_rrsffr_to: float | Unset = UNSET,
    page: int | Unset = UNSET,
    size: int | Unset = UNSET,
    sort: str | Unset = UNSET,
    dir_: str | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["ASRespForNSPINFrom"] = as_resp_for_nspin_from

    params["ASRespForNSPINTo"] = as_resp_for_nspin_to

    params["ASRespForREGUPFrom"] = as_resp_for_regup_from

    params["ASRespForREGUPTo"] = as_resp_for_regup_to

    params["ASRespForREGDNFrom"] = as_resp_for_regdn_from

    params["ASRespForREGDNTo"] = as_resp_for_regdn_to

    params["SCEDBidCurveMW1From"] = sced_bid_curve_mw1_from

    params["SCEDBidCurveMW1To"] = sced_bid_curve_mw1_to

    params["SCEDBidCurvePrice1From"] = sced_bid_curve_price_1_from

    params["SCEDBidCurvePrice1To"] = sced_bid_curve_price_1_to

    params["SCEDBidCurveMW2From"] = sced_bid_curve_mw2_from

    params["SCEDBidCurveMW2To"] = sced_bid_curve_mw2_to

    params["SCEDBidCurvePrice2From"] = sced_bid_curve_price_2_from

    params["SCEDBidCurvePrice2To"] = sced_bid_curve_price_2_to

    params["SCEDBidCurveMW3From"] = sced_bid_curve_mw3_from

    params["SCEDBidCurveMW3To"] = sced_bid_curve_mw3_to

    params["SCEDBidCurvePrice3From"] = sced_bid_curve_price_3_from

    params["SCEDBidCurvePrice3To"] = sced_bid_curve_price_3_to

    params["SCEDBidCurveMW4From"] = sced_bid_curve_mw4_from

    params["SCEDBidCurveMW4To"] = sced_bid_curve_mw4_to

    params["SCEDBidCurvePrice4From"] = sced_bid_curve_price_4_from

    params["SCEDBidCurvePrice4To"] = sced_bid_curve_price_4_to

    params["SCEDBidCurveMW5From"] = sced_bid_curve_mw5_from

    params["SCEDBidCurveMW5To"] = sced_bid_curve_mw5_to

    params["SCEDBidCurvePrice5From"] = sced_bid_curve_price_5_from

    params["SCEDBidCurvePrice5To"] = sced_bid_curve_price_5_to

    params["SCEDBidCurveMW6From"] = sced_bid_curve_mw6_from

    params["SCEDBidCurveMW6To"] = sced_bid_curve_mw6_to

    params["SCEDBidCurvePrice6From"] = sced_bid_curve_price_6_from

    params["SCEDBidCurvePrice6To"] = sced_bid_curve_price_6_to

    params["SCEDBidCurveMW7From"] = sced_bid_curve_mw7_from

    params["SCEDBidCurveMW7To"] = sced_bid_curve_mw7_to

    params["SCEDBidCurvePrice7From"] = sced_bid_curve_price_7_from

    params["SCEDBidCurvePrice7To"] = sced_bid_curve_price_7_to

    params["SCEDBidCurveMW8From"] = sced_bid_curve_mw8_from

    params["SCEDBidCurveMW8To"] = sced_bid_curve_mw8_to

    params["SCEDBidCurvePrice8From"] = sced_bid_curve_price_8_from

    params["SCEDBidCurvePrice8To"] = sced_bid_curve_price_8_to

    params["SCEDBidCurveMW9From"] = sced_bid_curve_mw9_from

    params["SCEDBidCurveMW9To"] = sced_bid_curve_mw9_to

    params["SCEDBidCurvePrice9From"] = sced_bid_curve_price_9_from

    params["SCEDBidCurvePrice9To"] = sced_bid_curve_price_9_to

    params["SCEDBidCurveMW10From"] = sced_bid_curve_mw10_from

    params["SCEDBidCurveMW10To"] = sced_bid_curve_mw10_to

    params["SCEDBidCurvePrice10From"] = sced_bid_curve_price_10_from

    params["SCEDBidCurvePrice10To"] = sced_bid_curve_price_10_to

    params["HASLFrom"] = hasl_from

    params["HASLTo"] = hasl_to

    params["HDLFrom"] = hdl_from

    params["HDLTo"] = hdl_to

    params["LASLFrom"] = lasl_from

    params["LASLTo"] = lasl_to

    params["LDLFrom"] = ldl_from

    params["LDLTo"] = ldl_to

    params["basePointFrom"] = base_point_from

    params["basePointTo"] = base_point_to

    params["SCEDTimestampFrom"] = sced_timestamp_from

    params["SCEDTimestampTo"] = sced_timestamp_to

    params["repeatHourFlag"] = repeat_hour_flag

    params["qseName"] = qse_name

    params["dmeName"] = dme_name

    params["resourceName"] = resource_name

    params["telResStatus"] = tel_res_status

    params["maxPowerConsumptionFrom"] = max_power_consumption_from

    params["maxPowerConsumptionTo"] = max_power_consumption_to

    params["lowPowerConsumptionFrom"] = low_power_consumption_from

    params["lowPowerConsumptionTo"] = low_power_consumption_to

    params["realPowerConsumptionFrom"] = real_power_consumption_from

    params["realPowerConsumptionTo"] = real_power_consumption_to

    params["ASRespForRRSFrom"] = as_resp_for_rrs_from

    params["ASRespForRRSTo"] = as_resp_for_rrs_to

    params["ASRespForRRSFFRFrom"] = as_resp_for_rrsffr_from

    params["ASRespForRRSFFRTo"] = as_resp_for_rrsffr_to

    params["page"] = page

    params["size"] = size

    params["sort"] = sort

    params["dir"] = dir_

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/np3-965-er/60_load_res_data_in_sced",
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
    as_resp_for_nspin_from: float | Unset = UNSET,
    as_resp_for_nspin_to: float | Unset = UNSET,
    as_resp_for_regup_from: float | Unset = UNSET,
    as_resp_for_regup_to: float | Unset = UNSET,
    as_resp_for_regdn_from: float | Unset = UNSET,
    as_resp_for_regdn_to: float | Unset = UNSET,
    sced_bid_curve_mw1_from: float | Unset = UNSET,
    sced_bid_curve_mw1_to: float | Unset = UNSET,
    sced_bid_curve_price_1_from: float | Unset = UNSET,
    sced_bid_curve_price_1_to: float | Unset = UNSET,
    sced_bid_curve_mw2_from: float | Unset = UNSET,
    sced_bid_curve_mw2_to: float | Unset = UNSET,
    sced_bid_curve_price_2_from: float | Unset = UNSET,
    sced_bid_curve_price_2_to: float | Unset = UNSET,
    sced_bid_curve_mw3_from: float | Unset = UNSET,
    sced_bid_curve_mw3_to: float | Unset = UNSET,
    sced_bid_curve_price_3_from: float | Unset = UNSET,
    sced_bid_curve_price_3_to: float | Unset = UNSET,
    sced_bid_curve_mw4_from: float | Unset = UNSET,
    sced_bid_curve_mw4_to: float | Unset = UNSET,
    sced_bid_curve_price_4_from: float | Unset = UNSET,
    sced_bid_curve_price_4_to: float | Unset = UNSET,
    sced_bid_curve_mw5_from: float | Unset = UNSET,
    sced_bid_curve_mw5_to: float | Unset = UNSET,
    sced_bid_curve_price_5_from: float | Unset = UNSET,
    sced_bid_curve_price_5_to: float | Unset = UNSET,
    sced_bid_curve_mw6_from: float | Unset = UNSET,
    sced_bid_curve_mw6_to: float | Unset = UNSET,
    sced_bid_curve_price_6_from: float | Unset = UNSET,
    sced_bid_curve_price_6_to: float | Unset = UNSET,
    sced_bid_curve_mw7_from: float | Unset = UNSET,
    sced_bid_curve_mw7_to: float | Unset = UNSET,
    sced_bid_curve_price_7_from: float | Unset = UNSET,
    sced_bid_curve_price_7_to: float | Unset = UNSET,
    sced_bid_curve_mw8_from: float | Unset = UNSET,
    sced_bid_curve_mw8_to: float | Unset = UNSET,
    sced_bid_curve_price_8_from: float | Unset = UNSET,
    sced_bid_curve_price_8_to: float | Unset = UNSET,
    sced_bid_curve_mw9_from: float | Unset = UNSET,
    sced_bid_curve_mw9_to: float | Unset = UNSET,
    sced_bid_curve_price_9_from: float | Unset = UNSET,
    sced_bid_curve_price_9_to: float | Unset = UNSET,
    sced_bid_curve_mw10_from: float | Unset = UNSET,
    sced_bid_curve_mw10_to: float | Unset = UNSET,
    sced_bid_curve_price_10_from: float | Unset = UNSET,
    sced_bid_curve_price_10_to: float | Unset = UNSET,
    hasl_from: float | Unset = UNSET,
    hasl_to: float | Unset = UNSET,
    hdl_from: float | Unset = UNSET,
    hdl_to: float | Unset = UNSET,
    lasl_from: float | Unset = UNSET,
    lasl_to: float | Unset = UNSET,
    ldl_from: float | Unset = UNSET,
    ldl_to: float | Unset = UNSET,
    base_point_from: float | Unset = UNSET,
    base_point_to: float | Unset = UNSET,
    sced_timestamp_from: str | Unset = UNSET,
    sced_timestamp_to: str | Unset = UNSET,
    repeat_hour_flag: bool | Unset = UNSET,
    qse_name: str | Unset = UNSET,
    dme_name: str | Unset = UNSET,
    resource_name: str | Unset = UNSET,
    tel_res_status: str | Unset = UNSET,
    max_power_consumption_from: float | Unset = UNSET,
    max_power_consumption_to: float | Unset = UNSET,
    low_power_consumption_from: float | Unset = UNSET,
    low_power_consumption_to: float | Unset = UNSET,
    real_power_consumption_from: float | Unset = UNSET,
    real_power_consumption_to: float | Unset = UNSET,
    as_resp_for_rrs_from: float | Unset = UNSET,
    as_resp_for_rrs_to: float | Unset = UNSET,
    as_resp_for_rrsffr_from: float | Unset = UNSET,
    as_resp_for_rrsffr_to: float | Unset = UNSET,
    page: int | Unset = UNSET,
    size: int | Unset = UNSET,
    sort: str | Unset = UNSET,
    dir_: str | Unset = UNSET,
) -> Response[Exception_ | Report]:
    """60 Day Load Resource Data in SCED

     60 Day Load Resource Data in SCED

    Args:
        as_resp_for_nspin_from (float | Unset):
        as_resp_for_nspin_to (float | Unset):
        as_resp_for_regup_from (float | Unset):
        as_resp_for_regup_to (float | Unset):
        as_resp_for_regdn_from (float | Unset):
        as_resp_for_regdn_to (float | Unset):
        sced_bid_curve_mw1_from (float | Unset):
        sced_bid_curve_mw1_to (float | Unset):
        sced_bid_curve_price_1_from (float | Unset):
        sced_bid_curve_price_1_to (float | Unset):
        sced_bid_curve_mw2_from (float | Unset):
        sced_bid_curve_mw2_to (float | Unset):
        sced_bid_curve_price_2_from (float | Unset):
        sced_bid_curve_price_2_to (float | Unset):
        sced_bid_curve_mw3_from (float | Unset):
        sced_bid_curve_mw3_to (float | Unset):
        sced_bid_curve_price_3_from (float | Unset):
        sced_bid_curve_price_3_to (float | Unset):
        sced_bid_curve_mw4_from (float | Unset):
        sced_bid_curve_mw4_to (float | Unset):
        sced_bid_curve_price_4_from (float | Unset):
        sced_bid_curve_price_4_to (float | Unset):
        sced_bid_curve_mw5_from (float | Unset):
        sced_bid_curve_mw5_to (float | Unset):
        sced_bid_curve_price_5_from (float | Unset):
        sced_bid_curve_price_5_to (float | Unset):
        sced_bid_curve_mw6_from (float | Unset):
        sced_bid_curve_mw6_to (float | Unset):
        sced_bid_curve_price_6_from (float | Unset):
        sced_bid_curve_price_6_to (float | Unset):
        sced_bid_curve_mw7_from (float | Unset):
        sced_bid_curve_mw7_to (float | Unset):
        sced_bid_curve_price_7_from (float | Unset):
        sced_bid_curve_price_7_to (float | Unset):
        sced_bid_curve_mw8_from (float | Unset):
        sced_bid_curve_mw8_to (float | Unset):
        sced_bid_curve_price_8_from (float | Unset):
        sced_bid_curve_price_8_to (float | Unset):
        sced_bid_curve_mw9_from (float | Unset):
        sced_bid_curve_mw9_to (float | Unset):
        sced_bid_curve_price_9_from (float | Unset):
        sced_bid_curve_price_9_to (float | Unset):
        sced_bid_curve_mw10_from (float | Unset):
        sced_bid_curve_mw10_to (float | Unset):
        sced_bid_curve_price_10_from (float | Unset):
        sced_bid_curve_price_10_to (float | Unset):
        hasl_from (float | Unset):
        hasl_to (float | Unset):
        hdl_from (float | Unset):
        hdl_to (float | Unset):
        lasl_from (float | Unset):
        lasl_to (float | Unset):
        ldl_from (float | Unset):
        ldl_to (float | Unset):
        base_point_from (float | Unset):
        base_point_to (float | Unset):
        sced_timestamp_from (str | Unset):
        sced_timestamp_to (str | Unset):
        repeat_hour_flag (bool | Unset):
        qse_name (str | Unset):
        dme_name (str | Unset):
        resource_name (str | Unset):
        tel_res_status (str | Unset):
        max_power_consumption_from (float | Unset):
        max_power_consumption_to (float | Unset):
        low_power_consumption_from (float | Unset):
        low_power_consumption_to (float | Unset):
        real_power_consumption_from (float | Unset):
        real_power_consumption_to (float | Unset):
        as_resp_for_rrs_from (float | Unset):
        as_resp_for_rrs_to (float | Unset):
        as_resp_for_rrsffr_from (float | Unset):
        as_resp_for_rrsffr_to (float | Unset):
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
        as_resp_for_nspin_from=as_resp_for_nspin_from,
        as_resp_for_nspin_to=as_resp_for_nspin_to,
        as_resp_for_regup_from=as_resp_for_regup_from,
        as_resp_for_regup_to=as_resp_for_regup_to,
        as_resp_for_regdn_from=as_resp_for_regdn_from,
        as_resp_for_regdn_to=as_resp_for_regdn_to,
        sced_bid_curve_mw1_from=sced_bid_curve_mw1_from,
        sced_bid_curve_mw1_to=sced_bid_curve_mw1_to,
        sced_bid_curve_price_1_from=sced_bid_curve_price_1_from,
        sced_bid_curve_price_1_to=sced_bid_curve_price_1_to,
        sced_bid_curve_mw2_from=sced_bid_curve_mw2_from,
        sced_bid_curve_mw2_to=sced_bid_curve_mw2_to,
        sced_bid_curve_price_2_from=sced_bid_curve_price_2_from,
        sced_bid_curve_price_2_to=sced_bid_curve_price_2_to,
        sced_bid_curve_mw3_from=sced_bid_curve_mw3_from,
        sced_bid_curve_mw3_to=sced_bid_curve_mw3_to,
        sced_bid_curve_price_3_from=sced_bid_curve_price_3_from,
        sced_bid_curve_price_3_to=sced_bid_curve_price_3_to,
        sced_bid_curve_mw4_from=sced_bid_curve_mw4_from,
        sced_bid_curve_mw4_to=sced_bid_curve_mw4_to,
        sced_bid_curve_price_4_from=sced_bid_curve_price_4_from,
        sced_bid_curve_price_4_to=sced_bid_curve_price_4_to,
        sced_bid_curve_mw5_from=sced_bid_curve_mw5_from,
        sced_bid_curve_mw5_to=sced_bid_curve_mw5_to,
        sced_bid_curve_price_5_from=sced_bid_curve_price_5_from,
        sced_bid_curve_price_5_to=sced_bid_curve_price_5_to,
        sced_bid_curve_mw6_from=sced_bid_curve_mw6_from,
        sced_bid_curve_mw6_to=sced_bid_curve_mw6_to,
        sced_bid_curve_price_6_from=sced_bid_curve_price_6_from,
        sced_bid_curve_price_6_to=sced_bid_curve_price_6_to,
        sced_bid_curve_mw7_from=sced_bid_curve_mw7_from,
        sced_bid_curve_mw7_to=sced_bid_curve_mw7_to,
        sced_bid_curve_price_7_from=sced_bid_curve_price_7_from,
        sced_bid_curve_price_7_to=sced_bid_curve_price_7_to,
        sced_bid_curve_mw8_from=sced_bid_curve_mw8_from,
        sced_bid_curve_mw8_to=sced_bid_curve_mw8_to,
        sced_bid_curve_price_8_from=sced_bid_curve_price_8_from,
        sced_bid_curve_price_8_to=sced_bid_curve_price_8_to,
        sced_bid_curve_mw9_from=sced_bid_curve_mw9_from,
        sced_bid_curve_mw9_to=sced_bid_curve_mw9_to,
        sced_bid_curve_price_9_from=sced_bid_curve_price_9_from,
        sced_bid_curve_price_9_to=sced_bid_curve_price_9_to,
        sced_bid_curve_mw10_from=sced_bid_curve_mw10_from,
        sced_bid_curve_mw10_to=sced_bid_curve_mw10_to,
        sced_bid_curve_price_10_from=sced_bid_curve_price_10_from,
        sced_bid_curve_price_10_to=sced_bid_curve_price_10_to,
        hasl_from=hasl_from,
        hasl_to=hasl_to,
        hdl_from=hdl_from,
        hdl_to=hdl_to,
        lasl_from=lasl_from,
        lasl_to=lasl_to,
        ldl_from=ldl_from,
        ldl_to=ldl_to,
        base_point_from=base_point_from,
        base_point_to=base_point_to,
        sced_timestamp_from=sced_timestamp_from,
        sced_timestamp_to=sced_timestamp_to,
        repeat_hour_flag=repeat_hour_flag,
        qse_name=qse_name,
        dme_name=dme_name,
        resource_name=resource_name,
        tel_res_status=tel_res_status,
        max_power_consumption_from=max_power_consumption_from,
        max_power_consumption_to=max_power_consumption_to,
        low_power_consumption_from=low_power_consumption_from,
        low_power_consumption_to=low_power_consumption_to,
        real_power_consumption_from=real_power_consumption_from,
        real_power_consumption_to=real_power_consumption_to,
        as_resp_for_rrs_from=as_resp_for_rrs_from,
        as_resp_for_rrs_to=as_resp_for_rrs_to,
        as_resp_for_rrsffr_from=as_resp_for_rrsffr_from,
        as_resp_for_rrsffr_to=as_resp_for_rrsffr_to,
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
    as_resp_for_nspin_from: float | Unset = UNSET,
    as_resp_for_nspin_to: float | Unset = UNSET,
    as_resp_for_regup_from: float | Unset = UNSET,
    as_resp_for_regup_to: float | Unset = UNSET,
    as_resp_for_regdn_from: float | Unset = UNSET,
    as_resp_for_regdn_to: float | Unset = UNSET,
    sced_bid_curve_mw1_from: float | Unset = UNSET,
    sced_bid_curve_mw1_to: float | Unset = UNSET,
    sced_bid_curve_price_1_from: float | Unset = UNSET,
    sced_bid_curve_price_1_to: float | Unset = UNSET,
    sced_bid_curve_mw2_from: float | Unset = UNSET,
    sced_bid_curve_mw2_to: float | Unset = UNSET,
    sced_bid_curve_price_2_from: float | Unset = UNSET,
    sced_bid_curve_price_2_to: float | Unset = UNSET,
    sced_bid_curve_mw3_from: float | Unset = UNSET,
    sced_bid_curve_mw3_to: float | Unset = UNSET,
    sced_bid_curve_price_3_from: float | Unset = UNSET,
    sced_bid_curve_price_3_to: float | Unset = UNSET,
    sced_bid_curve_mw4_from: float | Unset = UNSET,
    sced_bid_curve_mw4_to: float | Unset = UNSET,
    sced_bid_curve_price_4_from: float | Unset = UNSET,
    sced_bid_curve_price_4_to: float | Unset = UNSET,
    sced_bid_curve_mw5_from: float | Unset = UNSET,
    sced_bid_curve_mw5_to: float | Unset = UNSET,
    sced_bid_curve_price_5_from: float | Unset = UNSET,
    sced_bid_curve_price_5_to: float | Unset = UNSET,
    sced_bid_curve_mw6_from: float | Unset = UNSET,
    sced_bid_curve_mw6_to: float | Unset = UNSET,
    sced_bid_curve_price_6_from: float | Unset = UNSET,
    sced_bid_curve_price_6_to: float | Unset = UNSET,
    sced_bid_curve_mw7_from: float | Unset = UNSET,
    sced_bid_curve_mw7_to: float | Unset = UNSET,
    sced_bid_curve_price_7_from: float | Unset = UNSET,
    sced_bid_curve_price_7_to: float | Unset = UNSET,
    sced_bid_curve_mw8_from: float | Unset = UNSET,
    sced_bid_curve_mw8_to: float | Unset = UNSET,
    sced_bid_curve_price_8_from: float | Unset = UNSET,
    sced_bid_curve_price_8_to: float | Unset = UNSET,
    sced_bid_curve_mw9_from: float | Unset = UNSET,
    sced_bid_curve_mw9_to: float | Unset = UNSET,
    sced_bid_curve_price_9_from: float | Unset = UNSET,
    sced_bid_curve_price_9_to: float | Unset = UNSET,
    sced_bid_curve_mw10_from: float | Unset = UNSET,
    sced_bid_curve_mw10_to: float | Unset = UNSET,
    sced_bid_curve_price_10_from: float | Unset = UNSET,
    sced_bid_curve_price_10_to: float | Unset = UNSET,
    hasl_from: float | Unset = UNSET,
    hasl_to: float | Unset = UNSET,
    hdl_from: float | Unset = UNSET,
    hdl_to: float | Unset = UNSET,
    lasl_from: float | Unset = UNSET,
    lasl_to: float | Unset = UNSET,
    ldl_from: float | Unset = UNSET,
    ldl_to: float | Unset = UNSET,
    base_point_from: float | Unset = UNSET,
    base_point_to: float | Unset = UNSET,
    sced_timestamp_from: str | Unset = UNSET,
    sced_timestamp_to: str | Unset = UNSET,
    repeat_hour_flag: bool | Unset = UNSET,
    qse_name: str | Unset = UNSET,
    dme_name: str | Unset = UNSET,
    resource_name: str | Unset = UNSET,
    tel_res_status: str | Unset = UNSET,
    max_power_consumption_from: float | Unset = UNSET,
    max_power_consumption_to: float | Unset = UNSET,
    low_power_consumption_from: float | Unset = UNSET,
    low_power_consumption_to: float | Unset = UNSET,
    real_power_consumption_from: float | Unset = UNSET,
    real_power_consumption_to: float | Unset = UNSET,
    as_resp_for_rrs_from: float | Unset = UNSET,
    as_resp_for_rrs_to: float | Unset = UNSET,
    as_resp_for_rrsffr_from: float | Unset = UNSET,
    as_resp_for_rrsffr_to: float | Unset = UNSET,
    page: int | Unset = UNSET,
    size: int | Unset = UNSET,
    sort: str | Unset = UNSET,
    dir_: str | Unset = UNSET,
) -> Exception_ | Report | None:
    """60 Day Load Resource Data in SCED

     60 Day Load Resource Data in SCED

    Args:
        as_resp_for_nspin_from (float | Unset):
        as_resp_for_nspin_to (float | Unset):
        as_resp_for_regup_from (float | Unset):
        as_resp_for_regup_to (float | Unset):
        as_resp_for_regdn_from (float | Unset):
        as_resp_for_regdn_to (float | Unset):
        sced_bid_curve_mw1_from (float | Unset):
        sced_bid_curve_mw1_to (float | Unset):
        sced_bid_curve_price_1_from (float | Unset):
        sced_bid_curve_price_1_to (float | Unset):
        sced_bid_curve_mw2_from (float | Unset):
        sced_bid_curve_mw2_to (float | Unset):
        sced_bid_curve_price_2_from (float | Unset):
        sced_bid_curve_price_2_to (float | Unset):
        sced_bid_curve_mw3_from (float | Unset):
        sced_bid_curve_mw3_to (float | Unset):
        sced_bid_curve_price_3_from (float | Unset):
        sced_bid_curve_price_3_to (float | Unset):
        sced_bid_curve_mw4_from (float | Unset):
        sced_bid_curve_mw4_to (float | Unset):
        sced_bid_curve_price_4_from (float | Unset):
        sced_bid_curve_price_4_to (float | Unset):
        sced_bid_curve_mw5_from (float | Unset):
        sced_bid_curve_mw5_to (float | Unset):
        sced_bid_curve_price_5_from (float | Unset):
        sced_bid_curve_price_5_to (float | Unset):
        sced_bid_curve_mw6_from (float | Unset):
        sced_bid_curve_mw6_to (float | Unset):
        sced_bid_curve_price_6_from (float | Unset):
        sced_bid_curve_price_6_to (float | Unset):
        sced_bid_curve_mw7_from (float | Unset):
        sced_bid_curve_mw7_to (float | Unset):
        sced_bid_curve_price_7_from (float | Unset):
        sced_bid_curve_price_7_to (float | Unset):
        sced_bid_curve_mw8_from (float | Unset):
        sced_bid_curve_mw8_to (float | Unset):
        sced_bid_curve_price_8_from (float | Unset):
        sced_bid_curve_price_8_to (float | Unset):
        sced_bid_curve_mw9_from (float | Unset):
        sced_bid_curve_mw9_to (float | Unset):
        sced_bid_curve_price_9_from (float | Unset):
        sced_bid_curve_price_9_to (float | Unset):
        sced_bid_curve_mw10_from (float | Unset):
        sced_bid_curve_mw10_to (float | Unset):
        sced_bid_curve_price_10_from (float | Unset):
        sced_bid_curve_price_10_to (float | Unset):
        hasl_from (float | Unset):
        hasl_to (float | Unset):
        hdl_from (float | Unset):
        hdl_to (float | Unset):
        lasl_from (float | Unset):
        lasl_to (float | Unset):
        ldl_from (float | Unset):
        ldl_to (float | Unset):
        base_point_from (float | Unset):
        base_point_to (float | Unset):
        sced_timestamp_from (str | Unset):
        sced_timestamp_to (str | Unset):
        repeat_hour_flag (bool | Unset):
        qse_name (str | Unset):
        dme_name (str | Unset):
        resource_name (str | Unset):
        tel_res_status (str | Unset):
        max_power_consumption_from (float | Unset):
        max_power_consumption_to (float | Unset):
        low_power_consumption_from (float | Unset):
        low_power_consumption_to (float | Unset):
        real_power_consumption_from (float | Unset):
        real_power_consumption_to (float | Unset):
        as_resp_for_rrs_from (float | Unset):
        as_resp_for_rrs_to (float | Unset):
        as_resp_for_rrsffr_from (float | Unset):
        as_resp_for_rrsffr_to (float | Unset):
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
        as_resp_for_nspin_from=as_resp_for_nspin_from,
        as_resp_for_nspin_to=as_resp_for_nspin_to,
        as_resp_for_regup_from=as_resp_for_regup_from,
        as_resp_for_regup_to=as_resp_for_regup_to,
        as_resp_for_regdn_from=as_resp_for_regdn_from,
        as_resp_for_regdn_to=as_resp_for_regdn_to,
        sced_bid_curve_mw1_from=sced_bid_curve_mw1_from,
        sced_bid_curve_mw1_to=sced_bid_curve_mw1_to,
        sced_bid_curve_price_1_from=sced_bid_curve_price_1_from,
        sced_bid_curve_price_1_to=sced_bid_curve_price_1_to,
        sced_bid_curve_mw2_from=sced_bid_curve_mw2_from,
        sced_bid_curve_mw2_to=sced_bid_curve_mw2_to,
        sced_bid_curve_price_2_from=sced_bid_curve_price_2_from,
        sced_bid_curve_price_2_to=sced_bid_curve_price_2_to,
        sced_bid_curve_mw3_from=sced_bid_curve_mw3_from,
        sced_bid_curve_mw3_to=sced_bid_curve_mw3_to,
        sced_bid_curve_price_3_from=sced_bid_curve_price_3_from,
        sced_bid_curve_price_3_to=sced_bid_curve_price_3_to,
        sced_bid_curve_mw4_from=sced_bid_curve_mw4_from,
        sced_bid_curve_mw4_to=sced_bid_curve_mw4_to,
        sced_bid_curve_price_4_from=sced_bid_curve_price_4_from,
        sced_bid_curve_price_4_to=sced_bid_curve_price_4_to,
        sced_bid_curve_mw5_from=sced_bid_curve_mw5_from,
        sced_bid_curve_mw5_to=sced_bid_curve_mw5_to,
        sced_bid_curve_price_5_from=sced_bid_curve_price_5_from,
        sced_bid_curve_price_5_to=sced_bid_curve_price_5_to,
        sced_bid_curve_mw6_from=sced_bid_curve_mw6_from,
        sced_bid_curve_mw6_to=sced_bid_curve_mw6_to,
        sced_bid_curve_price_6_from=sced_bid_curve_price_6_from,
        sced_bid_curve_price_6_to=sced_bid_curve_price_6_to,
        sced_bid_curve_mw7_from=sced_bid_curve_mw7_from,
        sced_bid_curve_mw7_to=sced_bid_curve_mw7_to,
        sced_bid_curve_price_7_from=sced_bid_curve_price_7_from,
        sced_bid_curve_price_7_to=sced_bid_curve_price_7_to,
        sced_bid_curve_mw8_from=sced_bid_curve_mw8_from,
        sced_bid_curve_mw8_to=sced_bid_curve_mw8_to,
        sced_bid_curve_price_8_from=sced_bid_curve_price_8_from,
        sced_bid_curve_price_8_to=sced_bid_curve_price_8_to,
        sced_bid_curve_mw9_from=sced_bid_curve_mw9_from,
        sced_bid_curve_mw9_to=sced_bid_curve_mw9_to,
        sced_bid_curve_price_9_from=sced_bid_curve_price_9_from,
        sced_bid_curve_price_9_to=sced_bid_curve_price_9_to,
        sced_bid_curve_mw10_from=sced_bid_curve_mw10_from,
        sced_bid_curve_mw10_to=sced_bid_curve_mw10_to,
        sced_bid_curve_price_10_from=sced_bid_curve_price_10_from,
        sced_bid_curve_price_10_to=sced_bid_curve_price_10_to,
        hasl_from=hasl_from,
        hasl_to=hasl_to,
        hdl_from=hdl_from,
        hdl_to=hdl_to,
        lasl_from=lasl_from,
        lasl_to=lasl_to,
        ldl_from=ldl_from,
        ldl_to=ldl_to,
        base_point_from=base_point_from,
        base_point_to=base_point_to,
        sced_timestamp_from=sced_timestamp_from,
        sced_timestamp_to=sced_timestamp_to,
        repeat_hour_flag=repeat_hour_flag,
        qse_name=qse_name,
        dme_name=dme_name,
        resource_name=resource_name,
        tel_res_status=tel_res_status,
        max_power_consumption_from=max_power_consumption_from,
        max_power_consumption_to=max_power_consumption_to,
        low_power_consumption_from=low_power_consumption_from,
        low_power_consumption_to=low_power_consumption_to,
        real_power_consumption_from=real_power_consumption_from,
        real_power_consumption_to=real_power_consumption_to,
        as_resp_for_rrs_from=as_resp_for_rrs_from,
        as_resp_for_rrs_to=as_resp_for_rrs_to,
        as_resp_for_rrsffr_from=as_resp_for_rrsffr_from,
        as_resp_for_rrsffr_to=as_resp_for_rrsffr_to,
        page=page,
        size=size,
        sort=sort,
        dir_=dir_,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    as_resp_for_nspin_from: float | Unset = UNSET,
    as_resp_for_nspin_to: float | Unset = UNSET,
    as_resp_for_regup_from: float | Unset = UNSET,
    as_resp_for_regup_to: float | Unset = UNSET,
    as_resp_for_regdn_from: float | Unset = UNSET,
    as_resp_for_regdn_to: float | Unset = UNSET,
    sced_bid_curve_mw1_from: float | Unset = UNSET,
    sced_bid_curve_mw1_to: float | Unset = UNSET,
    sced_bid_curve_price_1_from: float | Unset = UNSET,
    sced_bid_curve_price_1_to: float | Unset = UNSET,
    sced_bid_curve_mw2_from: float | Unset = UNSET,
    sced_bid_curve_mw2_to: float | Unset = UNSET,
    sced_bid_curve_price_2_from: float | Unset = UNSET,
    sced_bid_curve_price_2_to: float | Unset = UNSET,
    sced_bid_curve_mw3_from: float | Unset = UNSET,
    sced_bid_curve_mw3_to: float | Unset = UNSET,
    sced_bid_curve_price_3_from: float | Unset = UNSET,
    sced_bid_curve_price_3_to: float | Unset = UNSET,
    sced_bid_curve_mw4_from: float | Unset = UNSET,
    sced_bid_curve_mw4_to: float | Unset = UNSET,
    sced_bid_curve_price_4_from: float | Unset = UNSET,
    sced_bid_curve_price_4_to: float | Unset = UNSET,
    sced_bid_curve_mw5_from: float | Unset = UNSET,
    sced_bid_curve_mw5_to: float | Unset = UNSET,
    sced_bid_curve_price_5_from: float | Unset = UNSET,
    sced_bid_curve_price_5_to: float | Unset = UNSET,
    sced_bid_curve_mw6_from: float | Unset = UNSET,
    sced_bid_curve_mw6_to: float | Unset = UNSET,
    sced_bid_curve_price_6_from: float | Unset = UNSET,
    sced_bid_curve_price_6_to: float | Unset = UNSET,
    sced_bid_curve_mw7_from: float | Unset = UNSET,
    sced_bid_curve_mw7_to: float | Unset = UNSET,
    sced_bid_curve_price_7_from: float | Unset = UNSET,
    sced_bid_curve_price_7_to: float | Unset = UNSET,
    sced_bid_curve_mw8_from: float | Unset = UNSET,
    sced_bid_curve_mw8_to: float | Unset = UNSET,
    sced_bid_curve_price_8_from: float | Unset = UNSET,
    sced_bid_curve_price_8_to: float | Unset = UNSET,
    sced_bid_curve_mw9_from: float | Unset = UNSET,
    sced_bid_curve_mw9_to: float | Unset = UNSET,
    sced_bid_curve_price_9_from: float | Unset = UNSET,
    sced_bid_curve_price_9_to: float | Unset = UNSET,
    sced_bid_curve_mw10_from: float | Unset = UNSET,
    sced_bid_curve_mw10_to: float | Unset = UNSET,
    sced_bid_curve_price_10_from: float | Unset = UNSET,
    sced_bid_curve_price_10_to: float | Unset = UNSET,
    hasl_from: float | Unset = UNSET,
    hasl_to: float | Unset = UNSET,
    hdl_from: float | Unset = UNSET,
    hdl_to: float | Unset = UNSET,
    lasl_from: float | Unset = UNSET,
    lasl_to: float | Unset = UNSET,
    ldl_from: float | Unset = UNSET,
    ldl_to: float | Unset = UNSET,
    base_point_from: float | Unset = UNSET,
    base_point_to: float | Unset = UNSET,
    sced_timestamp_from: str | Unset = UNSET,
    sced_timestamp_to: str | Unset = UNSET,
    repeat_hour_flag: bool | Unset = UNSET,
    qse_name: str | Unset = UNSET,
    dme_name: str | Unset = UNSET,
    resource_name: str | Unset = UNSET,
    tel_res_status: str | Unset = UNSET,
    max_power_consumption_from: float | Unset = UNSET,
    max_power_consumption_to: float | Unset = UNSET,
    low_power_consumption_from: float | Unset = UNSET,
    low_power_consumption_to: float | Unset = UNSET,
    real_power_consumption_from: float | Unset = UNSET,
    real_power_consumption_to: float | Unset = UNSET,
    as_resp_for_rrs_from: float | Unset = UNSET,
    as_resp_for_rrs_to: float | Unset = UNSET,
    as_resp_for_rrsffr_from: float | Unset = UNSET,
    as_resp_for_rrsffr_to: float | Unset = UNSET,
    page: int | Unset = UNSET,
    size: int | Unset = UNSET,
    sort: str | Unset = UNSET,
    dir_: str | Unset = UNSET,
) -> Response[Exception_ | Report]:
    """60 Day Load Resource Data in SCED

     60 Day Load Resource Data in SCED

    Args:
        as_resp_for_nspin_from (float | Unset):
        as_resp_for_nspin_to (float | Unset):
        as_resp_for_regup_from (float | Unset):
        as_resp_for_regup_to (float | Unset):
        as_resp_for_regdn_from (float | Unset):
        as_resp_for_regdn_to (float | Unset):
        sced_bid_curve_mw1_from (float | Unset):
        sced_bid_curve_mw1_to (float | Unset):
        sced_bid_curve_price_1_from (float | Unset):
        sced_bid_curve_price_1_to (float | Unset):
        sced_bid_curve_mw2_from (float | Unset):
        sced_bid_curve_mw2_to (float | Unset):
        sced_bid_curve_price_2_from (float | Unset):
        sced_bid_curve_price_2_to (float | Unset):
        sced_bid_curve_mw3_from (float | Unset):
        sced_bid_curve_mw3_to (float | Unset):
        sced_bid_curve_price_3_from (float | Unset):
        sced_bid_curve_price_3_to (float | Unset):
        sced_bid_curve_mw4_from (float | Unset):
        sced_bid_curve_mw4_to (float | Unset):
        sced_bid_curve_price_4_from (float | Unset):
        sced_bid_curve_price_4_to (float | Unset):
        sced_bid_curve_mw5_from (float | Unset):
        sced_bid_curve_mw5_to (float | Unset):
        sced_bid_curve_price_5_from (float | Unset):
        sced_bid_curve_price_5_to (float | Unset):
        sced_bid_curve_mw6_from (float | Unset):
        sced_bid_curve_mw6_to (float | Unset):
        sced_bid_curve_price_6_from (float | Unset):
        sced_bid_curve_price_6_to (float | Unset):
        sced_bid_curve_mw7_from (float | Unset):
        sced_bid_curve_mw7_to (float | Unset):
        sced_bid_curve_price_7_from (float | Unset):
        sced_bid_curve_price_7_to (float | Unset):
        sced_bid_curve_mw8_from (float | Unset):
        sced_bid_curve_mw8_to (float | Unset):
        sced_bid_curve_price_8_from (float | Unset):
        sced_bid_curve_price_8_to (float | Unset):
        sced_bid_curve_mw9_from (float | Unset):
        sced_bid_curve_mw9_to (float | Unset):
        sced_bid_curve_price_9_from (float | Unset):
        sced_bid_curve_price_9_to (float | Unset):
        sced_bid_curve_mw10_from (float | Unset):
        sced_bid_curve_mw10_to (float | Unset):
        sced_bid_curve_price_10_from (float | Unset):
        sced_bid_curve_price_10_to (float | Unset):
        hasl_from (float | Unset):
        hasl_to (float | Unset):
        hdl_from (float | Unset):
        hdl_to (float | Unset):
        lasl_from (float | Unset):
        lasl_to (float | Unset):
        ldl_from (float | Unset):
        ldl_to (float | Unset):
        base_point_from (float | Unset):
        base_point_to (float | Unset):
        sced_timestamp_from (str | Unset):
        sced_timestamp_to (str | Unset):
        repeat_hour_flag (bool | Unset):
        qse_name (str | Unset):
        dme_name (str | Unset):
        resource_name (str | Unset):
        tel_res_status (str | Unset):
        max_power_consumption_from (float | Unset):
        max_power_consumption_to (float | Unset):
        low_power_consumption_from (float | Unset):
        low_power_consumption_to (float | Unset):
        real_power_consumption_from (float | Unset):
        real_power_consumption_to (float | Unset):
        as_resp_for_rrs_from (float | Unset):
        as_resp_for_rrs_to (float | Unset):
        as_resp_for_rrsffr_from (float | Unset):
        as_resp_for_rrsffr_to (float | Unset):
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
        as_resp_for_nspin_from=as_resp_for_nspin_from,
        as_resp_for_nspin_to=as_resp_for_nspin_to,
        as_resp_for_regup_from=as_resp_for_regup_from,
        as_resp_for_regup_to=as_resp_for_regup_to,
        as_resp_for_regdn_from=as_resp_for_regdn_from,
        as_resp_for_regdn_to=as_resp_for_regdn_to,
        sced_bid_curve_mw1_from=sced_bid_curve_mw1_from,
        sced_bid_curve_mw1_to=sced_bid_curve_mw1_to,
        sced_bid_curve_price_1_from=sced_bid_curve_price_1_from,
        sced_bid_curve_price_1_to=sced_bid_curve_price_1_to,
        sced_bid_curve_mw2_from=sced_bid_curve_mw2_from,
        sced_bid_curve_mw2_to=sced_bid_curve_mw2_to,
        sced_bid_curve_price_2_from=sced_bid_curve_price_2_from,
        sced_bid_curve_price_2_to=sced_bid_curve_price_2_to,
        sced_bid_curve_mw3_from=sced_bid_curve_mw3_from,
        sced_bid_curve_mw3_to=sced_bid_curve_mw3_to,
        sced_bid_curve_price_3_from=sced_bid_curve_price_3_from,
        sced_bid_curve_price_3_to=sced_bid_curve_price_3_to,
        sced_bid_curve_mw4_from=sced_bid_curve_mw4_from,
        sced_bid_curve_mw4_to=sced_bid_curve_mw4_to,
        sced_bid_curve_price_4_from=sced_bid_curve_price_4_from,
        sced_bid_curve_price_4_to=sced_bid_curve_price_4_to,
        sced_bid_curve_mw5_from=sced_bid_curve_mw5_from,
        sced_bid_curve_mw5_to=sced_bid_curve_mw5_to,
        sced_bid_curve_price_5_from=sced_bid_curve_price_5_from,
        sced_bid_curve_price_5_to=sced_bid_curve_price_5_to,
        sced_bid_curve_mw6_from=sced_bid_curve_mw6_from,
        sced_bid_curve_mw6_to=sced_bid_curve_mw6_to,
        sced_bid_curve_price_6_from=sced_bid_curve_price_6_from,
        sced_bid_curve_price_6_to=sced_bid_curve_price_6_to,
        sced_bid_curve_mw7_from=sced_bid_curve_mw7_from,
        sced_bid_curve_mw7_to=sced_bid_curve_mw7_to,
        sced_bid_curve_price_7_from=sced_bid_curve_price_7_from,
        sced_bid_curve_price_7_to=sced_bid_curve_price_7_to,
        sced_bid_curve_mw8_from=sced_bid_curve_mw8_from,
        sced_bid_curve_mw8_to=sced_bid_curve_mw8_to,
        sced_bid_curve_price_8_from=sced_bid_curve_price_8_from,
        sced_bid_curve_price_8_to=sced_bid_curve_price_8_to,
        sced_bid_curve_mw9_from=sced_bid_curve_mw9_from,
        sced_bid_curve_mw9_to=sced_bid_curve_mw9_to,
        sced_bid_curve_price_9_from=sced_bid_curve_price_9_from,
        sced_bid_curve_price_9_to=sced_bid_curve_price_9_to,
        sced_bid_curve_mw10_from=sced_bid_curve_mw10_from,
        sced_bid_curve_mw10_to=sced_bid_curve_mw10_to,
        sced_bid_curve_price_10_from=sced_bid_curve_price_10_from,
        sced_bid_curve_price_10_to=sced_bid_curve_price_10_to,
        hasl_from=hasl_from,
        hasl_to=hasl_to,
        hdl_from=hdl_from,
        hdl_to=hdl_to,
        lasl_from=lasl_from,
        lasl_to=lasl_to,
        ldl_from=ldl_from,
        ldl_to=ldl_to,
        base_point_from=base_point_from,
        base_point_to=base_point_to,
        sced_timestamp_from=sced_timestamp_from,
        sced_timestamp_to=sced_timestamp_to,
        repeat_hour_flag=repeat_hour_flag,
        qse_name=qse_name,
        dme_name=dme_name,
        resource_name=resource_name,
        tel_res_status=tel_res_status,
        max_power_consumption_from=max_power_consumption_from,
        max_power_consumption_to=max_power_consumption_to,
        low_power_consumption_from=low_power_consumption_from,
        low_power_consumption_to=low_power_consumption_to,
        real_power_consumption_from=real_power_consumption_from,
        real_power_consumption_to=real_power_consumption_to,
        as_resp_for_rrs_from=as_resp_for_rrs_from,
        as_resp_for_rrs_to=as_resp_for_rrs_to,
        as_resp_for_rrsffr_from=as_resp_for_rrsffr_from,
        as_resp_for_rrsffr_to=as_resp_for_rrsffr_to,
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
    as_resp_for_nspin_from: float | Unset = UNSET,
    as_resp_for_nspin_to: float | Unset = UNSET,
    as_resp_for_regup_from: float | Unset = UNSET,
    as_resp_for_regup_to: float | Unset = UNSET,
    as_resp_for_regdn_from: float | Unset = UNSET,
    as_resp_for_regdn_to: float | Unset = UNSET,
    sced_bid_curve_mw1_from: float | Unset = UNSET,
    sced_bid_curve_mw1_to: float | Unset = UNSET,
    sced_bid_curve_price_1_from: float | Unset = UNSET,
    sced_bid_curve_price_1_to: float | Unset = UNSET,
    sced_bid_curve_mw2_from: float | Unset = UNSET,
    sced_bid_curve_mw2_to: float | Unset = UNSET,
    sced_bid_curve_price_2_from: float | Unset = UNSET,
    sced_bid_curve_price_2_to: float | Unset = UNSET,
    sced_bid_curve_mw3_from: float | Unset = UNSET,
    sced_bid_curve_mw3_to: float | Unset = UNSET,
    sced_bid_curve_price_3_from: float | Unset = UNSET,
    sced_bid_curve_price_3_to: float | Unset = UNSET,
    sced_bid_curve_mw4_from: float | Unset = UNSET,
    sced_bid_curve_mw4_to: float | Unset = UNSET,
    sced_bid_curve_price_4_from: float | Unset = UNSET,
    sced_bid_curve_price_4_to: float | Unset = UNSET,
    sced_bid_curve_mw5_from: float | Unset = UNSET,
    sced_bid_curve_mw5_to: float | Unset = UNSET,
    sced_bid_curve_price_5_from: float | Unset = UNSET,
    sced_bid_curve_price_5_to: float | Unset = UNSET,
    sced_bid_curve_mw6_from: float | Unset = UNSET,
    sced_bid_curve_mw6_to: float | Unset = UNSET,
    sced_bid_curve_price_6_from: float | Unset = UNSET,
    sced_bid_curve_price_6_to: float | Unset = UNSET,
    sced_bid_curve_mw7_from: float | Unset = UNSET,
    sced_bid_curve_mw7_to: float | Unset = UNSET,
    sced_bid_curve_price_7_from: float | Unset = UNSET,
    sced_bid_curve_price_7_to: float | Unset = UNSET,
    sced_bid_curve_mw8_from: float | Unset = UNSET,
    sced_bid_curve_mw8_to: float | Unset = UNSET,
    sced_bid_curve_price_8_from: float | Unset = UNSET,
    sced_bid_curve_price_8_to: float | Unset = UNSET,
    sced_bid_curve_mw9_from: float | Unset = UNSET,
    sced_bid_curve_mw9_to: float | Unset = UNSET,
    sced_bid_curve_price_9_from: float | Unset = UNSET,
    sced_bid_curve_price_9_to: float | Unset = UNSET,
    sced_bid_curve_mw10_from: float | Unset = UNSET,
    sced_bid_curve_mw10_to: float | Unset = UNSET,
    sced_bid_curve_price_10_from: float | Unset = UNSET,
    sced_bid_curve_price_10_to: float | Unset = UNSET,
    hasl_from: float | Unset = UNSET,
    hasl_to: float | Unset = UNSET,
    hdl_from: float | Unset = UNSET,
    hdl_to: float | Unset = UNSET,
    lasl_from: float | Unset = UNSET,
    lasl_to: float | Unset = UNSET,
    ldl_from: float | Unset = UNSET,
    ldl_to: float | Unset = UNSET,
    base_point_from: float | Unset = UNSET,
    base_point_to: float | Unset = UNSET,
    sced_timestamp_from: str | Unset = UNSET,
    sced_timestamp_to: str | Unset = UNSET,
    repeat_hour_flag: bool | Unset = UNSET,
    qse_name: str | Unset = UNSET,
    dme_name: str | Unset = UNSET,
    resource_name: str | Unset = UNSET,
    tel_res_status: str | Unset = UNSET,
    max_power_consumption_from: float | Unset = UNSET,
    max_power_consumption_to: float | Unset = UNSET,
    low_power_consumption_from: float | Unset = UNSET,
    low_power_consumption_to: float | Unset = UNSET,
    real_power_consumption_from: float | Unset = UNSET,
    real_power_consumption_to: float | Unset = UNSET,
    as_resp_for_rrs_from: float | Unset = UNSET,
    as_resp_for_rrs_to: float | Unset = UNSET,
    as_resp_for_rrsffr_from: float | Unset = UNSET,
    as_resp_for_rrsffr_to: float | Unset = UNSET,
    page: int | Unset = UNSET,
    size: int | Unset = UNSET,
    sort: str | Unset = UNSET,
    dir_: str | Unset = UNSET,
) -> Exception_ | Report | None:
    """60 Day Load Resource Data in SCED

     60 Day Load Resource Data in SCED

    Args:
        as_resp_for_nspin_from (float | Unset):
        as_resp_for_nspin_to (float | Unset):
        as_resp_for_regup_from (float | Unset):
        as_resp_for_regup_to (float | Unset):
        as_resp_for_regdn_from (float | Unset):
        as_resp_for_regdn_to (float | Unset):
        sced_bid_curve_mw1_from (float | Unset):
        sced_bid_curve_mw1_to (float | Unset):
        sced_bid_curve_price_1_from (float | Unset):
        sced_bid_curve_price_1_to (float | Unset):
        sced_bid_curve_mw2_from (float | Unset):
        sced_bid_curve_mw2_to (float | Unset):
        sced_bid_curve_price_2_from (float | Unset):
        sced_bid_curve_price_2_to (float | Unset):
        sced_bid_curve_mw3_from (float | Unset):
        sced_bid_curve_mw3_to (float | Unset):
        sced_bid_curve_price_3_from (float | Unset):
        sced_bid_curve_price_3_to (float | Unset):
        sced_bid_curve_mw4_from (float | Unset):
        sced_bid_curve_mw4_to (float | Unset):
        sced_bid_curve_price_4_from (float | Unset):
        sced_bid_curve_price_4_to (float | Unset):
        sced_bid_curve_mw5_from (float | Unset):
        sced_bid_curve_mw5_to (float | Unset):
        sced_bid_curve_price_5_from (float | Unset):
        sced_bid_curve_price_5_to (float | Unset):
        sced_bid_curve_mw6_from (float | Unset):
        sced_bid_curve_mw6_to (float | Unset):
        sced_bid_curve_price_6_from (float | Unset):
        sced_bid_curve_price_6_to (float | Unset):
        sced_bid_curve_mw7_from (float | Unset):
        sced_bid_curve_mw7_to (float | Unset):
        sced_bid_curve_price_7_from (float | Unset):
        sced_bid_curve_price_7_to (float | Unset):
        sced_bid_curve_mw8_from (float | Unset):
        sced_bid_curve_mw8_to (float | Unset):
        sced_bid_curve_price_8_from (float | Unset):
        sced_bid_curve_price_8_to (float | Unset):
        sced_bid_curve_mw9_from (float | Unset):
        sced_bid_curve_mw9_to (float | Unset):
        sced_bid_curve_price_9_from (float | Unset):
        sced_bid_curve_price_9_to (float | Unset):
        sced_bid_curve_mw10_from (float | Unset):
        sced_bid_curve_mw10_to (float | Unset):
        sced_bid_curve_price_10_from (float | Unset):
        sced_bid_curve_price_10_to (float | Unset):
        hasl_from (float | Unset):
        hasl_to (float | Unset):
        hdl_from (float | Unset):
        hdl_to (float | Unset):
        lasl_from (float | Unset):
        lasl_to (float | Unset):
        ldl_from (float | Unset):
        ldl_to (float | Unset):
        base_point_from (float | Unset):
        base_point_to (float | Unset):
        sced_timestamp_from (str | Unset):
        sced_timestamp_to (str | Unset):
        repeat_hour_flag (bool | Unset):
        qse_name (str | Unset):
        dme_name (str | Unset):
        resource_name (str | Unset):
        tel_res_status (str | Unset):
        max_power_consumption_from (float | Unset):
        max_power_consumption_to (float | Unset):
        low_power_consumption_from (float | Unset):
        low_power_consumption_to (float | Unset):
        real_power_consumption_from (float | Unset):
        real_power_consumption_to (float | Unset):
        as_resp_for_rrs_from (float | Unset):
        as_resp_for_rrs_to (float | Unset):
        as_resp_for_rrsffr_from (float | Unset):
        as_resp_for_rrsffr_to (float | Unset):
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
            as_resp_for_nspin_from=as_resp_for_nspin_from,
            as_resp_for_nspin_to=as_resp_for_nspin_to,
            as_resp_for_regup_from=as_resp_for_regup_from,
            as_resp_for_regup_to=as_resp_for_regup_to,
            as_resp_for_regdn_from=as_resp_for_regdn_from,
            as_resp_for_regdn_to=as_resp_for_regdn_to,
            sced_bid_curve_mw1_from=sced_bid_curve_mw1_from,
            sced_bid_curve_mw1_to=sced_bid_curve_mw1_to,
            sced_bid_curve_price_1_from=sced_bid_curve_price_1_from,
            sced_bid_curve_price_1_to=sced_bid_curve_price_1_to,
            sced_bid_curve_mw2_from=sced_bid_curve_mw2_from,
            sced_bid_curve_mw2_to=sced_bid_curve_mw2_to,
            sced_bid_curve_price_2_from=sced_bid_curve_price_2_from,
            sced_bid_curve_price_2_to=sced_bid_curve_price_2_to,
            sced_bid_curve_mw3_from=sced_bid_curve_mw3_from,
            sced_bid_curve_mw3_to=sced_bid_curve_mw3_to,
            sced_bid_curve_price_3_from=sced_bid_curve_price_3_from,
            sced_bid_curve_price_3_to=sced_bid_curve_price_3_to,
            sced_bid_curve_mw4_from=sced_bid_curve_mw4_from,
            sced_bid_curve_mw4_to=sced_bid_curve_mw4_to,
            sced_bid_curve_price_4_from=sced_bid_curve_price_4_from,
            sced_bid_curve_price_4_to=sced_bid_curve_price_4_to,
            sced_bid_curve_mw5_from=sced_bid_curve_mw5_from,
            sced_bid_curve_mw5_to=sced_bid_curve_mw5_to,
            sced_bid_curve_price_5_from=sced_bid_curve_price_5_from,
            sced_bid_curve_price_5_to=sced_bid_curve_price_5_to,
            sced_bid_curve_mw6_from=sced_bid_curve_mw6_from,
            sced_bid_curve_mw6_to=sced_bid_curve_mw6_to,
            sced_bid_curve_price_6_from=sced_bid_curve_price_6_from,
            sced_bid_curve_price_6_to=sced_bid_curve_price_6_to,
            sced_bid_curve_mw7_from=sced_bid_curve_mw7_from,
            sced_bid_curve_mw7_to=sced_bid_curve_mw7_to,
            sced_bid_curve_price_7_from=sced_bid_curve_price_7_from,
            sced_bid_curve_price_7_to=sced_bid_curve_price_7_to,
            sced_bid_curve_mw8_from=sced_bid_curve_mw8_from,
            sced_bid_curve_mw8_to=sced_bid_curve_mw8_to,
            sced_bid_curve_price_8_from=sced_bid_curve_price_8_from,
            sced_bid_curve_price_8_to=sced_bid_curve_price_8_to,
            sced_bid_curve_mw9_from=sced_bid_curve_mw9_from,
            sced_bid_curve_mw9_to=sced_bid_curve_mw9_to,
            sced_bid_curve_price_9_from=sced_bid_curve_price_9_from,
            sced_bid_curve_price_9_to=sced_bid_curve_price_9_to,
            sced_bid_curve_mw10_from=sced_bid_curve_mw10_from,
            sced_bid_curve_mw10_to=sced_bid_curve_mw10_to,
            sced_bid_curve_price_10_from=sced_bid_curve_price_10_from,
            sced_bid_curve_price_10_to=sced_bid_curve_price_10_to,
            hasl_from=hasl_from,
            hasl_to=hasl_to,
            hdl_from=hdl_from,
            hdl_to=hdl_to,
            lasl_from=lasl_from,
            lasl_to=lasl_to,
            ldl_from=ldl_from,
            ldl_to=ldl_to,
            base_point_from=base_point_from,
            base_point_to=base_point_to,
            sced_timestamp_from=sced_timestamp_from,
            sced_timestamp_to=sced_timestamp_to,
            repeat_hour_flag=repeat_hour_flag,
            qse_name=qse_name,
            dme_name=dme_name,
            resource_name=resource_name,
            tel_res_status=tel_res_status,
            max_power_consumption_from=max_power_consumption_from,
            max_power_consumption_to=max_power_consumption_to,
            low_power_consumption_from=low_power_consumption_from,
            low_power_consumption_to=low_power_consumption_to,
            real_power_consumption_from=real_power_consumption_from,
            real_power_consumption_to=real_power_consumption_to,
            as_resp_for_rrs_from=as_resp_for_rrs_from,
            as_resp_for_rrs_to=as_resp_for_rrs_to,
            as_resp_for_rrsffr_from=as_resp_for_rrsffr_from,
            as_resp_for_rrsffr_to=as_resp_for_rrsffr_to,
            page=page,
            size=size,
            sort=sort,
            dir_=dir_,
        )
    ).parsed
