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
    hour_ending_from: str | Unset = UNSET,
    hour_ending_to: str | Unset = UNSET,
    qse_name: str | Unset = UNSET,
    dme_name: str | Unset = UNSET,
    resource_name: str | Unset = UNSET,
    resource_type: str | Unset = UNSET,
    qse_submitted_curve_mw1_from: float | Unset = UNSET,
    qse_submitted_curve_mw1_to: float | Unset = UNSET,
    qse_submitted_curve_price_1_from: float | Unset = UNSET,
    qse_submitted_curve_price_1_to: float | Unset = UNSET,
    qse_submitted_curve_mw2_from: float | Unset = UNSET,
    qse_submitted_curve_mw2_to: float | Unset = UNSET,
    qse_submitted_curve_price_2_from: float | Unset = UNSET,
    qse_submitted_curve_price_2_to: float | Unset = UNSET,
    qse_submitted_curve_mw3_from: float | Unset = UNSET,
    qse_submitted_curve_mw3_to: float | Unset = UNSET,
    qse_submitted_curve_price_3_from: float | Unset = UNSET,
    qse_submitted_curve_price_3_to: float | Unset = UNSET,
    qse_submitted_curve_mw4_from: float | Unset = UNSET,
    qse_submitted_curve_mw4_to: float | Unset = UNSET,
    qse_submitted_curve_price_4_from: float | Unset = UNSET,
    qse_submitted_curve_price_4_to: float | Unset = UNSET,
    qse_submitted_curve_mw5_from: float | Unset = UNSET,
    qse_submitted_curve_mw5_to: float | Unset = UNSET,
    qse_submitted_curve_price_5_from: float | Unset = UNSET,
    qse_submitted_curve_price_5_to: float | Unset = UNSET,
    qse_submitted_curve_mw6_from: float | Unset = UNSET,
    qse_submitted_curve_mw6_to: float | Unset = UNSET,
    qse_submitted_curve_price_6_from: float | Unset = UNSET,
    qse_submitted_curve_price_6_to: float | Unset = UNSET,
    qse_submitted_curve_mw7_from: float | Unset = UNSET,
    qse_submitted_curve_mw7_to: float | Unset = UNSET,
    qse_submitted_curve_price_7_from: float | Unset = UNSET,
    qse_submitted_curve_price_7_to: float | Unset = UNSET,
    qse_submitted_curve_mw8_from: float | Unset = UNSET,
    qse_submitted_curve_mw8_to: float | Unset = UNSET,
    qse_submitted_curve_price_8_from: float | Unset = UNSET,
    qse_submitted_curve_price_8_to: float | Unset = UNSET,
    qse_submitted_curve_mw9_from: float | Unset = UNSET,
    qse_submitted_curve_mw9_to: float | Unset = UNSET,
    qse_submitted_curve_price_9_from: float | Unset = UNSET,
    qse_submitted_curve_price_9_to: float | Unset = UNSET,
    qse_submitted_curve_mw10_from: float | Unset = UNSET,
    qse_submitted_curve_mw10_to: float | Unset = UNSET,
    qse_submitted_curve_price_10_from: float | Unset = UNSET,
    qse_submitted_curve_price_10_to: float | Unset = UNSET,
    start_up_hot_from: float | Unset = UNSET,
    start_up_hot_to: float | Unset = UNSET,
    start_up_inter_from: float | Unset = UNSET,
    start_up_inter_to: float | Unset = UNSET,
    start_up_cold_from: float | Unset = UNSET,
    start_up_cold_to: float | Unset = UNSET,
    min_gen_cost_from: float | Unset = UNSET,
    min_gen_cost_to: float | Unset = UNSET,
    hsl_from: float | Unset = UNSET,
    hsl_to: float | Unset = UNSET,
    lsl_from: float | Unset = UNSET,
    lsl_to: float | Unset = UNSET,
    resource_status: str | Unset = UNSET,
    awarded_quantity_from: int | Unset = UNSET,
    awarded_quantity_to: int | Unset = UNSET,
    settlement_point_name: str | Unset = UNSET,
    energy_settlement_point_price_from: float | Unset = UNSET,
    energy_settlement_point_price_to: float | Unset = UNSET,
    regup_awarded_from: float | Unset = UNSET,
    regup_awarded_to: float | Unset = UNSET,
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

    params["deliveryDateFrom"] = delivery_date_from

    params["deliveryDateTo"] = delivery_date_to

    params["hourEndingFrom"] = hour_ending_from

    params["hourEndingTo"] = hour_ending_to

    params["qseName"] = qse_name

    params["dmeName"] = dme_name

    params["resourceName"] = resource_name

    params["resourceType"] = resource_type

    params["qseSubmittedCurveMW1From"] = qse_submitted_curve_mw1_from

    params["qseSubmittedCurveMW1To"] = qse_submitted_curve_mw1_to

    params["qseSubmittedCurvePrice1From"] = qse_submitted_curve_price_1_from

    params["qseSubmittedCurvePrice1To"] = qse_submitted_curve_price_1_to

    params["qseSubmittedCurveMW2From"] = qse_submitted_curve_mw2_from

    params["qseSubmittedCurveMW2To"] = qse_submitted_curve_mw2_to

    params["qseSubmittedCurvePrice2From"] = qse_submitted_curve_price_2_from

    params["qseSubmittedCurvePrice2To"] = qse_submitted_curve_price_2_to

    params["qseSubmittedCurveMW3From"] = qse_submitted_curve_mw3_from

    params["qseSubmittedCurveMW3To"] = qse_submitted_curve_mw3_to

    params["qseSubmittedCurvePrice3From"] = qse_submitted_curve_price_3_from

    params["qseSubmittedCurvePrice3To"] = qse_submitted_curve_price_3_to

    params["qseSubmittedCurveMW4From"] = qse_submitted_curve_mw4_from

    params["qseSubmittedCurveMW4To"] = qse_submitted_curve_mw4_to

    params["qseSubmittedCurvePrice4From"] = qse_submitted_curve_price_4_from

    params["qseSubmittedCurvePrice4To"] = qse_submitted_curve_price_4_to

    params["qseSubmittedCurveMW5From"] = qse_submitted_curve_mw5_from

    params["qseSubmittedCurveMW5To"] = qse_submitted_curve_mw5_to

    params["qseSubmittedCurvePrice5From"] = qse_submitted_curve_price_5_from

    params["qseSubmittedCurvePrice5To"] = qse_submitted_curve_price_5_to

    params["qseSubmittedCurveMW6From"] = qse_submitted_curve_mw6_from

    params["qseSubmittedCurveMW6To"] = qse_submitted_curve_mw6_to

    params["qseSubmittedCurvePrice6From"] = qse_submitted_curve_price_6_from

    params["qseSubmittedCurvePrice6To"] = qse_submitted_curve_price_6_to

    params["qseSubmittedCurveMW7From"] = qse_submitted_curve_mw7_from

    params["qseSubmittedCurveMW7To"] = qse_submitted_curve_mw7_to

    params["qseSubmittedCurvePrice7From"] = qse_submitted_curve_price_7_from

    params["qseSubmittedCurvePrice7To"] = qse_submitted_curve_price_7_to

    params["qseSubmittedCurveMW8From"] = qse_submitted_curve_mw8_from

    params["qseSubmittedCurveMW8To"] = qse_submitted_curve_mw8_to

    params["qseSubmittedCurvePrice8From"] = qse_submitted_curve_price_8_from

    params["qseSubmittedCurvePrice8To"] = qse_submitted_curve_price_8_to

    params["qseSubmittedCurveMW9From"] = qse_submitted_curve_mw9_from

    params["qseSubmittedCurveMW9To"] = qse_submitted_curve_mw9_to

    params["qseSubmittedCurvePrice9From"] = qse_submitted_curve_price_9_from

    params["qseSubmittedCurvePrice9To"] = qse_submitted_curve_price_9_to

    params["qseSubmittedCurveMW10From"] = qse_submitted_curve_mw10_from

    params["qseSubmittedCurveMW10To"] = qse_submitted_curve_mw10_to

    params["qseSubmittedCurvePrice10From"] = qse_submitted_curve_price_10_from

    params["qseSubmittedCurvePrice10To"] = qse_submitted_curve_price_10_to

    params["startUpHotFrom"] = start_up_hot_from

    params["startUpHotTo"] = start_up_hot_to

    params["startUpInterFrom"] = start_up_inter_from

    params["startUpInterTo"] = start_up_inter_to

    params["startUpColdFrom"] = start_up_cold_from

    params["startUpColdTo"] = start_up_cold_to

    params["minGenCostFrom"] = min_gen_cost_from

    params["minGenCostTo"] = min_gen_cost_to

    params["HSLFrom"] = hsl_from

    params["HSLTo"] = hsl_to

    params["LSLFrom"] = lsl_from

    params["LSLTo"] = lsl_to

    params["resourceStatus"] = resource_status

    params["awardedQuantityFrom"] = awarded_quantity_from

    params["awardedQuantityTo"] = awarded_quantity_to

    params["settlementPointName"] = settlement_point_name

    params["energySettlementPointPriceFrom"] = energy_settlement_point_price_from

    params["energySettlementPointPriceTo"] = energy_settlement_point_price_to

    params["REGUPAwardedFrom"] = regup_awarded_from

    params["REGUPAwardedTo"] = regup_awarded_to

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
        "url": "/np3-966-er/60_dam_gen_res_data",
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
    hour_ending_from: str | Unset = UNSET,
    hour_ending_to: str | Unset = UNSET,
    qse_name: str | Unset = UNSET,
    dme_name: str | Unset = UNSET,
    resource_name: str | Unset = UNSET,
    resource_type: str | Unset = UNSET,
    qse_submitted_curve_mw1_from: float | Unset = UNSET,
    qse_submitted_curve_mw1_to: float | Unset = UNSET,
    qse_submitted_curve_price_1_from: float | Unset = UNSET,
    qse_submitted_curve_price_1_to: float | Unset = UNSET,
    qse_submitted_curve_mw2_from: float | Unset = UNSET,
    qse_submitted_curve_mw2_to: float | Unset = UNSET,
    qse_submitted_curve_price_2_from: float | Unset = UNSET,
    qse_submitted_curve_price_2_to: float | Unset = UNSET,
    qse_submitted_curve_mw3_from: float | Unset = UNSET,
    qse_submitted_curve_mw3_to: float | Unset = UNSET,
    qse_submitted_curve_price_3_from: float | Unset = UNSET,
    qse_submitted_curve_price_3_to: float | Unset = UNSET,
    qse_submitted_curve_mw4_from: float | Unset = UNSET,
    qse_submitted_curve_mw4_to: float | Unset = UNSET,
    qse_submitted_curve_price_4_from: float | Unset = UNSET,
    qse_submitted_curve_price_4_to: float | Unset = UNSET,
    qse_submitted_curve_mw5_from: float | Unset = UNSET,
    qse_submitted_curve_mw5_to: float | Unset = UNSET,
    qse_submitted_curve_price_5_from: float | Unset = UNSET,
    qse_submitted_curve_price_5_to: float | Unset = UNSET,
    qse_submitted_curve_mw6_from: float | Unset = UNSET,
    qse_submitted_curve_mw6_to: float | Unset = UNSET,
    qse_submitted_curve_price_6_from: float | Unset = UNSET,
    qse_submitted_curve_price_6_to: float | Unset = UNSET,
    qse_submitted_curve_mw7_from: float | Unset = UNSET,
    qse_submitted_curve_mw7_to: float | Unset = UNSET,
    qse_submitted_curve_price_7_from: float | Unset = UNSET,
    qse_submitted_curve_price_7_to: float | Unset = UNSET,
    qse_submitted_curve_mw8_from: float | Unset = UNSET,
    qse_submitted_curve_mw8_to: float | Unset = UNSET,
    qse_submitted_curve_price_8_from: float | Unset = UNSET,
    qse_submitted_curve_price_8_to: float | Unset = UNSET,
    qse_submitted_curve_mw9_from: float | Unset = UNSET,
    qse_submitted_curve_mw9_to: float | Unset = UNSET,
    qse_submitted_curve_price_9_from: float | Unset = UNSET,
    qse_submitted_curve_price_9_to: float | Unset = UNSET,
    qse_submitted_curve_mw10_from: float | Unset = UNSET,
    qse_submitted_curve_mw10_to: float | Unset = UNSET,
    qse_submitted_curve_price_10_from: float | Unset = UNSET,
    qse_submitted_curve_price_10_to: float | Unset = UNSET,
    start_up_hot_from: float | Unset = UNSET,
    start_up_hot_to: float | Unset = UNSET,
    start_up_inter_from: float | Unset = UNSET,
    start_up_inter_to: float | Unset = UNSET,
    start_up_cold_from: float | Unset = UNSET,
    start_up_cold_to: float | Unset = UNSET,
    min_gen_cost_from: float | Unset = UNSET,
    min_gen_cost_to: float | Unset = UNSET,
    hsl_from: float | Unset = UNSET,
    hsl_to: float | Unset = UNSET,
    lsl_from: float | Unset = UNSET,
    lsl_to: float | Unset = UNSET,
    resource_status: str | Unset = UNSET,
    awarded_quantity_from: int | Unset = UNSET,
    awarded_quantity_to: int | Unset = UNSET,
    settlement_point_name: str | Unset = UNSET,
    energy_settlement_point_price_from: float | Unset = UNSET,
    energy_settlement_point_price_to: float | Unset = UNSET,
    regup_awarded_from: float | Unset = UNSET,
    regup_awarded_to: float | Unset = UNSET,
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
    """60 Day DAM Generation Resource Data

     60 Day DAM Generation Resource Data

    Args:
        delivery_date_from (str | Unset):
        delivery_date_to (str | Unset):
        hour_ending_from (str | Unset):
        hour_ending_to (str | Unset):
        qse_name (str | Unset):
        dme_name (str | Unset):
        resource_name (str | Unset):
        resource_type (str | Unset):
        qse_submitted_curve_mw1_from (float | Unset):
        qse_submitted_curve_mw1_to (float | Unset):
        qse_submitted_curve_price_1_from (float | Unset):
        qse_submitted_curve_price_1_to (float | Unset):
        qse_submitted_curve_mw2_from (float | Unset):
        qse_submitted_curve_mw2_to (float | Unset):
        qse_submitted_curve_price_2_from (float | Unset):
        qse_submitted_curve_price_2_to (float | Unset):
        qse_submitted_curve_mw3_from (float | Unset):
        qse_submitted_curve_mw3_to (float | Unset):
        qse_submitted_curve_price_3_from (float | Unset):
        qse_submitted_curve_price_3_to (float | Unset):
        qse_submitted_curve_mw4_from (float | Unset):
        qse_submitted_curve_mw4_to (float | Unset):
        qse_submitted_curve_price_4_from (float | Unset):
        qse_submitted_curve_price_4_to (float | Unset):
        qse_submitted_curve_mw5_from (float | Unset):
        qse_submitted_curve_mw5_to (float | Unset):
        qse_submitted_curve_price_5_from (float | Unset):
        qse_submitted_curve_price_5_to (float | Unset):
        qse_submitted_curve_mw6_from (float | Unset):
        qse_submitted_curve_mw6_to (float | Unset):
        qse_submitted_curve_price_6_from (float | Unset):
        qse_submitted_curve_price_6_to (float | Unset):
        qse_submitted_curve_mw7_from (float | Unset):
        qse_submitted_curve_mw7_to (float | Unset):
        qse_submitted_curve_price_7_from (float | Unset):
        qse_submitted_curve_price_7_to (float | Unset):
        qse_submitted_curve_mw8_from (float | Unset):
        qse_submitted_curve_mw8_to (float | Unset):
        qse_submitted_curve_price_8_from (float | Unset):
        qse_submitted_curve_price_8_to (float | Unset):
        qse_submitted_curve_mw9_from (float | Unset):
        qse_submitted_curve_mw9_to (float | Unset):
        qse_submitted_curve_price_9_from (float | Unset):
        qse_submitted_curve_price_9_to (float | Unset):
        qse_submitted_curve_mw10_from (float | Unset):
        qse_submitted_curve_mw10_to (float | Unset):
        qse_submitted_curve_price_10_from (float | Unset):
        qse_submitted_curve_price_10_to (float | Unset):
        start_up_hot_from (float | Unset):
        start_up_hot_to (float | Unset):
        start_up_inter_from (float | Unset):
        start_up_inter_to (float | Unset):
        start_up_cold_from (float | Unset):
        start_up_cold_to (float | Unset):
        min_gen_cost_from (float | Unset):
        min_gen_cost_to (float | Unset):
        hsl_from (float | Unset):
        hsl_to (float | Unset):
        lsl_from (float | Unset):
        lsl_to (float | Unset):
        resource_status (str | Unset):
        awarded_quantity_from (int | Unset):
        awarded_quantity_to (int | Unset):
        settlement_point_name (str | Unset):
        energy_settlement_point_price_from (float | Unset):
        energy_settlement_point_price_to (float | Unset):
        regup_awarded_from (float | Unset):
        regup_awarded_to (float | Unset):
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
        delivery_date_from=delivery_date_from,
        delivery_date_to=delivery_date_to,
        hour_ending_from=hour_ending_from,
        hour_ending_to=hour_ending_to,
        qse_name=qse_name,
        dme_name=dme_name,
        resource_name=resource_name,
        resource_type=resource_type,
        qse_submitted_curve_mw1_from=qse_submitted_curve_mw1_from,
        qse_submitted_curve_mw1_to=qse_submitted_curve_mw1_to,
        qse_submitted_curve_price_1_from=qse_submitted_curve_price_1_from,
        qse_submitted_curve_price_1_to=qse_submitted_curve_price_1_to,
        qse_submitted_curve_mw2_from=qse_submitted_curve_mw2_from,
        qse_submitted_curve_mw2_to=qse_submitted_curve_mw2_to,
        qse_submitted_curve_price_2_from=qse_submitted_curve_price_2_from,
        qse_submitted_curve_price_2_to=qse_submitted_curve_price_2_to,
        qse_submitted_curve_mw3_from=qse_submitted_curve_mw3_from,
        qse_submitted_curve_mw3_to=qse_submitted_curve_mw3_to,
        qse_submitted_curve_price_3_from=qse_submitted_curve_price_3_from,
        qse_submitted_curve_price_3_to=qse_submitted_curve_price_3_to,
        qse_submitted_curve_mw4_from=qse_submitted_curve_mw4_from,
        qse_submitted_curve_mw4_to=qse_submitted_curve_mw4_to,
        qse_submitted_curve_price_4_from=qse_submitted_curve_price_4_from,
        qse_submitted_curve_price_4_to=qse_submitted_curve_price_4_to,
        qse_submitted_curve_mw5_from=qse_submitted_curve_mw5_from,
        qse_submitted_curve_mw5_to=qse_submitted_curve_mw5_to,
        qse_submitted_curve_price_5_from=qse_submitted_curve_price_5_from,
        qse_submitted_curve_price_5_to=qse_submitted_curve_price_5_to,
        qse_submitted_curve_mw6_from=qse_submitted_curve_mw6_from,
        qse_submitted_curve_mw6_to=qse_submitted_curve_mw6_to,
        qse_submitted_curve_price_6_from=qse_submitted_curve_price_6_from,
        qse_submitted_curve_price_6_to=qse_submitted_curve_price_6_to,
        qse_submitted_curve_mw7_from=qse_submitted_curve_mw7_from,
        qse_submitted_curve_mw7_to=qse_submitted_curve_mw7_to,
        qse_submitted_curve_price_7_from=qse_submitted_curve_price_7_from,
        qse_submitted_curve_price_7_to=qse_submitted_curve_price_7_to,
        qse_submitted_curve_mw8_from=qse_submitted_curve_mw8_from,
        qse_submitted_curve_mw8_to=qse_submitted_curve_mw8_to,
        qse_submitted_curve_price_8_from=qse_submitted_curve_price_8_from,
        qse_submitted_curve_price_8_to=qse_submitted_curve_price_8_to,
        qse_submitted_curve_mw9_from=qse_submitted_curve_mw9_from,
        qse_submitted_curve_mw9_to=qse_submitted_curve_mw9_to,
        qse_submitted_curve_price_9_from=qse_submitted_curve_price_9_from,
        qse_submitted_curve_price_9_to=qse_submitted_curve_price_9_to,
        qse_submitted_curve_mw10_from=qse_submitted_curve_mw10_from,
        qse_submitted_curve_mw10_to=qse_submitted_curve_mw10_to,
        qse_submitted_curve_price_10_from=qse_submitted_curve_price_10_from,
        qse_submitted_curve_price_10_to=qse_submitted_curve_price_10_to,
        start_up_hot_from=start_up_hot_from,
        start_up_hot_to=start_up_hot_to,
        start_up_inter_from=start_up_inter_from,
        start_up_inter_to=start_up_inter_to,
        start_up_cold_from=start_up_cold_from,
        start_up_cold_to=start_up_cold_to,
        min_gen_cost_from=min_gen_cost_from,
        min_gen_cost_to=min_gen_cost_to,
        hsl_from=hsl_from,
        hsl_to=hsl_to,
        lsl_from=lsl_from,
        lsl_to=lsl_to,
        resource_status=resource_status,
        awarded_quantity_from=awarded_quantity_from,
        awarded_quantity_to=awarded_quantity_to,
        settlement_point_name=settlement_point_name,
        energy_settlement_point_price_from=energy_settlement_point_price_from,
        energy_settlement_point_price_to=energy_settlement_point_price_to,
        regup_awarded_from=regup_awarded_from,
        regup_awarded_to=regup_awarded_to,
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
    delivery_date_from: str | Unset = UNSET,
    delivery_date_to: str | Unset = UNSET,
    hour_ending_from: str | Unset = UNSET,
    hour_ending_to: str | Unset = UNSET,
    qse_name: str | Unset = UNSET,
    dme_name: str | Unset = UNSET,
    resource_name: str | Unset = UNSET,
    resource_type: str | Unset = UNSET,
    qse_submitted_curve_mw1_from: float | Unset = UNSET,
    qse_submitted_curve_mw1_to: float | Unset = UNSET,
    qse_submitted_curve_price_1_from: float | Unset = UNSET,
    qse_submitted_curve_price_1_to: float | Unset = UNSET,
    qse_submitted_curve_mw2_from: float | Unset = UNSET,
    qse_submitted_curve_mw2_to: float | Unset = UNSET,
    qse_submitted_curve_price_2_from: float | Unset = UNSET,
    qse_submitted_curve_price_2_to: float | Unset = UNSET,
    qse_submitted_curve_mw3_from: float | Unset = UNSET,
    qse_submitted_curve_mw3_to: float | Unset = UNSET,
    qse_submitted_curve_price_3_from: float | Unset = UNSET,
    qse_submitted_curve_price_3_to: float | Unset = UNSET,
    qse_submitted_curve_mw4_from: float | Unset = UNSET,
    qse_submitted_curve_mw4_to: float | Unset = UNSET,
    qse_submitted_curve_price_4_from: float | Unset = UNSET,
    qse_submitted_curve_price_4_to: float | Unset = UNSET,
    qse_submitted_curve_mw5_from: float | Unset = UNSET,
    qse_submitted_curve_mw5_to: float | Unset = UNSET,
    qse_submitted_curve_price_5_from: float | Unset = UNSET,
    qse_submitted_curve_price_5_to: float | Unset = UNSET,
    qse_submitted_curve_mw6_from: float | Unset = UNSET,
    qse_submitted_curve_mw6_to: float | Unset = UNSET,
    qse_submitted_curve_price_6_from: float | Unset = UNSET,
    qse_submitted_curve_price_6_to: float | Unset = UNSET,
    qse_submitted_curve_mw7_from: float | Unset = UNSET,
    qse_submitted_curve_mw7_to: float | Unset = UNSET,
    qse_submitted_curve_price_7_from: float | Unset = UNSET,
    qse_submitted_curve_price_7_to: float | Unset = UNSET,
    qse_submitted_curve_mw8_from: float | Unset = UNSET,
    qse_submitted_curve_mw8_to: float | Unset = UNSET,
    qse_submitted_curve_price_8_from: float | Unset = UNSET,
    qse_submitted_curve_price_8_to: float | Unset = UNSET,
    qse_submitted_curve_mw9_from: float | Unset = UNSET,
    qse_submitted_curve_mw9_to: float | Unset = UNSET,
    qse_submitted_curve_price_9_from: float | Unset = UNSET,
    qse_submitted_curve_price_9_to: float | Unset = UNSET,
    qse_submitted_curve_mw10_from: float | Unset = UNSET,
    qse_submitted_curve_mw10_to: float | Unset = UNSET,
    qse_submitted_curve_price_10_from: float | Unset = UNSET,
    qse_submitted_curve_price_10_to: float | Unset = UNSET,
    start_up_hot_from: float | Unset = UNSET,
    start_up_hot_to: float | Unset = UNSET,
    start_up_inter_from: float | Unset = UNSET,
    start_up_inter_to: float | Unset = UNSET,
    start_up_cold_from: float | Unset = UNSET,
    start_up_cold_to: float | Unset = UNSET,
    min_gen_cost_from: float | Unset = UNSET,
    min_gen_cost_to: float | Unset = UNSET,
    hsl_from: float | Unset = UNSET,
    hsl_to: float | Unset = UNSET,
    lsl_from: float | Unset = UNSET,
    lsl_to: float | Unset = UNSET,
    resource_status: str | Unset = UNSET,
    awarded_quantity_from: int | Unset = UNSET,
    awarded_quantity_to: int | Unset = UNSET,
    settlement_point_name: str | Unset = UNSET,
    energy_settlement_point_price_from: float | Unset = UNSET,
    energy_settlement_point_price_to: float | Unset = UNSET,
    regup_awarded_from: float | Unset = UNSET,
    regup_awarded_to: float | Unset = UNSET,
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
    """60 Day DAM Generation Resource Data

     60 Day DAM Generation Resource Data

    Args:
        delivery_date_from (str | Unset):
        delivery_date_to (str | Unset):
        hour_ending_from (str | Unset):
        hour_ending_to (str | Unset):
        qse_name (str | Unset):
        dme_name (str | Unset):
        resource_name (str | Unset):
        resource_type (str | Unset):
        qse_submitted_curve_mw1_from (float | Unset):
        qse_submitted_curve_mw1_to (float | Unset):
        qse_submitted_curve_price_1_from (float | Unset):
        qse_submitted_curve_price_1_to (float | Unset):
        qse_submitted_curve_mw2_from (float | Unset):
        qse_submitted_curve_mw2_to (float | Unset):
        qse_submitted_curve_price_2_from (float | Unset):
        qse_submitted_curve_price_2_to (float | Unset):
        qse_submitted_curve_mw3_from (float | Unset):
        qse_submitted_curve_mw3_to (float | Unset):
        qse_submitted_curve_price_3_from (float | Unset):
        qse_submitted_curve_price_3_to (float | Unset):
        qse_submitted_curve_mw4_from (float | Unset):
        qse_submitted_curve_mw4_to (float | Unset):
        qse_submitted_curve_price_4_from (float | Unset):
        qse_submitted_curve_price_4_to (float | Unset):
        qse_submitted_curve_mw5_from (float | Unset):
        qse_submitted_curve_mw5_to (float | Unset):
        qse_submitted_curve_price_5_from (float | Unset):
        qse_submitted_curve_price_5_to (float | Unset):
        qse_submitted_curve_mw6_from (float | Unset):
        qse_submitted_curve_mw6_to (float | Unset):
        qse_submitted_curve_price_6_from (float | Unset):
        qse_submitted_curve_price_6_to (float | Unset):
        qse_submitted_curve_mw7_from (float | Unset):
        qse_submitted_curve_mw7_to (float | Unset):
        qse_submitted_curve_price_7_from (float | Unset):
        qse_submitted_curve_price_7_to (float | Unset):
        qse_submitted_curve_mw8_from (float | Unset):
        qse_submitted_curve_mw8_to (float | Unset):
        qse_submitted_curve_price_8_from (float | Unset):
        qse_submitted_curve_price_8_to (float | Unset):
        qse_submitted_curve_mw9_from (float | Unset):
        qse_submitted_curve_mw9_to (float | Unset):
        qse_submitted_curve_price_9_from (float | Unset):
        qse_submitted_curve_price_9_to (float | Unset):
        qse_submitted_curve_mw10_from (float | Unset):
        qse_submitted_curve_mw10_to (float | Unset):
        qse_submitted_curve_price_10_from (float | Unset):
        qse_submitted_curve_price_10_to (float | Unset):
        start_up_hot_from (float | Unset):
        start_up_hot_to (float | Unset):
        start_up_inter_from (float | Unset):
        start_up_inter_to (float | Unset):
        start_up_cold_from (float | Unset):
        start_up_cold_to (float | Unset):
        min_gen_cost_from (float | Unset):
        min_gen_cost_to (float | Unset):
        hsl_from (float | Unset):
        hsl_to (float | Unset):
        lsl_from (float | Unset):
        lsl_to (float | Unset):
        resource_status (str | Unset):
        awarded_quantity_from (int | Unset):
        awarded_quantity_to (int | Unset):
        settlement_point_name (str | Unset):
        energy_settlement_point_price_from (float | Unset):
        energy_settlement_point_price_to (float | Unset):
        regup_awarded_from (float | Unset):
        regup_awarded_to (float | Unset):
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
        delivery_date_from=delivery_date_from,
        delivery_date_to=delivery_date_to,
        hour_ending_from=hour_ending_from,
        hour_ending_to=hour_ending_to,
        qse_name=qse_name,
        dme_name=dme_name,
        resource_name=resource_name,
        resource_type=resource_type,
        qse_submitted_curve_mw1_from=qse_submitted_curve_mw1_from,
        qse_submitted_curve_mw1_to=qse_submitted_curve_mw1_to,
        qse_submitted_curve_price_1_from=qse_submitted_curve_price_1_from,
        qse_submitted_curve_price_1_to=qse_submitted_curve_price_1_to,
        qse_submitted_curve_mw2_from=qse_submitted_curve_mw2_from,
        qse_submitted_curve_mw2_to=qse_submitted_curve_mw2_to,
        qse_submitted_curve_price_2_from=qse_submitted_curve_price_2_from,
        qse_submitted_curve_price_2_to=qse_submitted_curve_price_2_to,
        qse_submitted_curve_mw3_from=qse_submitted_curve_mw3_from,
        qse_submitted_curve_mw3_to=qse_submitted_curve_mw3_to,
        qse_submitted_curve_price_3_from=qse_submitted_curve_price_3_from,
        qse_submitted_curve_price_3_to=qse_submitted_curve_price_3_to,
        qse_submitted_curve_mw4_from=qse_submitted_curve_mw4_from,
        qse_submitted_curve_mw4_to=qse_submitted_curve_mw4_to,
        qse_submitted_curve_price_4_from=qse_submitted_curve_price_4_from,
        qse_submitted_curve_price_4_to=qse_submitted_curve_price_4_to,
        qse_submitted_curve_mw5_from=qse_submitted_curve_mw5_from,
        qse_submitted_curve_mw5_to=qse_submitted_curve_mw5_to,
        qse_submitted_curve_price_5_from=qse_submitted_curve_price_5_from,
        qse_submitted_curve_price_5_to=qse_submitted_curve_price_5_to,
        qse_submitted_curve_mw6_from=qse_submitted_curve_mw6_from,
        qse_submitted_curve_mw6_to=qse_submitted_curve_mw6_to,
        qse_submitted_curve_price_6_from=qse_submitted_curve_price_6_from,
        qse_submitted_curve_price_6_to=qse_submitted_curve_price_6_to,
        qse_submitted_curve_mw7_from=qse_submitted_curve_mw7_from,
        qse_submitted_curve_mw7_to=qse_submitted_curve_mw7_to,
        qse_submitted_curve_price_7_from=qse_submitted_curve_price_7_from,
        qse_submitted_curve_price_7_to=qse_submitted_curve_price_7_to,
        qse_submitted_curve_mw8_from=qse_submitted_curve_mw8_from,
        qse_submitted_curve_mw8_to=qse_submitted_curve_mw8_to,
        qse_submitted_curve_price_8_from=qse_submitted_curve_price_8_from,
        qse_submitted_curve_price_8_to=qse_submitted_curve_price_8_to,
        qse_submitted_curve_mw9_from=qse_submitted_curve_mw9_from,
        qse_submitted_curve_mw9_to=qse_submitted_curve_mw9_to,
        qse_submitted_curve_price_9_from=qse_submitted_curve_price_9_from,
        qse_submitted_curve_price_9_to=qse_submitted_curve_price_9_to,
        qse_submitted_curve_mw10_from=qse_submitted_curve_mw10_from,
        qse_submitted_curve_mw10_to=qse_submitted_curve_mw10_to,
        qse_submitted_curve_price_10_from=qse_submitted_curve_price_10_from,
        qse_submitted_curve_price_10_to=qse_submitted_curve_price_10_to,
        start_up_hot_from=start_up_hot_from,
        start_up_hot_to=start_up_hot_to,
        start_up_inter_from=start_up_inter_from,
        start_up_inter_to=start_up_inter_to,
        start_up_cold_from=start_up_cold_from,
        start_up_cold_to=start_up_cold_to,
        min_gen_cost_from=min_gen_cost_from,
        min_gen_cost_to=min_gen_cost_to,
        hsl_from=hsl_from,
        hsl_to=hsl_to,
        lsl_from=lsl_from,
        lsl_to=lsl_to,
        resource_status=resource_status,
        awarded_quantity_from=awarded_quantity_from,
        awarded_quantity_to=awarded_quantity_to,
        settlement_point_name=settlement_point_name,
        energy_settlement_point_price_from=energy_settlement_point_price_from,
        energy_settlement_point_price_to=energy_settlement_point_price_to,
        regup_awarded_from=regup_awarded_from,
        regup_awarded_to=regup_awarded_to,
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
    delivery_date_from: str | Unset = UNSET,
    delivery_date_to: str | Unset = UNSET,
    hour_ending_from: str | Unset = UNSET,
    hour_ending_to: str | Unset = UNSET,
    qse_name: str | Unset = UNSET,
    dme_name: str | Unset = UNSET,
    resource_name: str | Unset = UNSET,
    resource_type: str | Unset = UNSET,
    qse_submitted_curve_mw1_from: float | Unset = UNSET,
    qse_submitted_curve_mw1_to: float | Unset = UNSET,
    qse_submitted_curve_price_1_from: float | Unset = UNSET,
    qse_submitted_curve_price_1_to: float | Unset = UNSET,
    qse_submitted_curve_mw2_from: float | Unset = UNSET,
    qse_submitted_curve_mw2_to: float | Unset = UNSET,
    qse_submitted_curve_price_2_from: float | Unset = UNSET,
    qse_submitted_curve_price_2_to: float | Unset = UNSET,
    qse_submitted_curve_mw3_from: float | Unset = UNSET,
    qse_submitted_curve_mw3_to: float | Unset = UNSET,
    qse_submitted_curve_price_3_from: float | Unset = UNSET,
    qse_submitted_curve_price_3_to: float | Unset = UNSET,
    qse_submitted_curve_mw4_from: float | Unset = UNSET,
    qse_submitted_curve_mw4_to: float | Unset = UNSET,
    qse_submitted_curve_price_4_from: float | Unset = UNSET,
    qse_submitted_curve_price_4_to: float | Unset = UNSET,
    qse_submitted_curve_mw5_from: float | Unset = UNSET,
    qse_submitted_curve_mw5_to: float | Unset = UNSET,
    qse_submitted_curve_price_5_from: float | Unset = UNSET,
    qse_submitted_curve_price_5_to: float | Unset = UNSET,
    qse_submitted_curve_mw6_from: float | Unset = UNSET,
    qse_submitted_curve_mw6_to: float | Unset = UNSET,
    qse_submitted_curve_price_6_from: float | Unset = UNSET,
    qse_submitted_curve_price_6_to: float | Unset = UNSET,
    qse_submitted_curve_mw7_from: float | Unset = UNSET,
    qse_submitted_curve_mw7_to: float | Unset = UNSET,
    qse_submitted_curve_price_7_from: float | Unset = UNSET,
    qse_submitted_curve_price_7_to: float | Unset = UNSET,
    qse_submitted_curve_mw8_from: float | Unset = UNSET,
    qse_submitted_curve_mw8_to: float | Unset = UNSET,
    qse_submitted_curve_price_8_from: float | Unset = UNSET,
    qse_submitted_curve_price_8_to: float | Unset = UNSET,
    qse_submitted_curve_mw9_from: float | Unset = UNSET,
    qse_submitted_curve_mw9_to: float | Unset = UNSET,
    qse_submitted_curve_price_9_from: float | Unset = UNSET,
    qse_submitted_curve_price_9_to: float | Unset = UNSET,
    qse_submitted_curve_mw10_from: float | Unset = UNSET,
    qse_submitted_curve_mw10_to: float | Unset = UNSET,
    qse_submitted_curve_price_10_from: float | Unset = UNSET,
    qse_submitted_curve_price_10_to: float | Unset = UNSET,
    start_up_hot_from: float | Unset = UNSET,
    start_up_hot_to: float | Unset = UNSET,
    start_up_inter_from: float | Unset = UNSET,
    start_up_inter_to: float | Unset = UNSET,
    start_up_cold_from: float | Unset = UNSET,
    start_up_cold_to: float | Unset = UNSET,
    min_gen_cost_from: float | Unset = UNSET,
    min_gen_cost_to: float | Unset = UNSET,
    hsl_from: float | Unset = UNSET,
    hsl_to: float | Unset = UNSET,
    lsl_from: float | Unset = UNSET,
    lsl_to: float | Unset = UNSET,
    resource_status: str | Unset = UNSET,
    awarded_quantity_from: int | Unset = UNSET,
    awarded_quantity_to: int | Unset = UNSET,
    settlement_point_name: str | Unset = UNSET,
    energy_settlement_point_price_from: float | Unset = UNSET,
    energy_settlement_point_price_to: float | Unset = UNSET,
    regup_awarded_from: float | Unset = UNSET,
    regup_awarded_to: float | Unset = UNSET,
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
    """60 Day DAM Generation Resource Data

     60 Day DAM Generation Resource Data

    Args:
        delivery_date_from (str | Unset):
        delivery_date_to (str | Unset):
        hour_ending_from (str | Unset):
        hour_ending_to (str | Unset):
        qse_name (str | Unset):
        dme_name (str | Unset):
        resource_name (str | Unset):
        resource_type (str | Unset):
        qse_submitted_curve_mw1_from (float | Unset):
        qse_submitted_curve_mw1_to (float | Unset):
        qse_submitted_curve_price_1_from (float | Unset):
        qse_submitted_curve_price_1_to (float | Unset):
        qse_submitted_curve_mw2_from (float | Unset):
        qse_submitted_curve_mw2_to (float | Unset):
        qse_submitted_curve_price_2_from (float | Unset):
        qse_submitted_curve_price_2_to (float | Unset):
        qse_submitted_curve_mw3_from (float | Unset):
        qse_submitted_curve_mw3_to (float | Unset):
        qse_submitted_curve_price_3_from (float | Unset):
        qse_submitted_curve_price_3_to (float | Unset):
        qse_submitted_curve_mw4_from (float | Unset):
        qse_submitted_curve_mw4_to (float | Unset):
        qse_submitted_curve_price_4_from (float | Unset):
        qse_submitted_curve_price_4_to (float | Unset):
        qse_submitted_curve_mw5_from (float | Unset):
        qse_submitted_curve_mw5_to (float | Unset):
        qse_submitted_curve_price_5_from (float | Unset):
        qse_submitted_curve_price_5_to (float | Unset):
        qse_submitted_curve_mw6_from (float | Unset):
        qse_submitted_curve_mw6_to (float | Unset):
        qse_submitted_curve_price_6_from (float | Unset):
        qse_submitted_curve_price_6_to (float | Unset):
        qse_submitted_curve_mw7_from (float | Unset):
        qse_submitted_curve_mw7_to (float | Unset):
        qse_submitted_curve_price_7_from (float | Unset):
        qse_submitted_curve_price_7_to (float | Unset):
        qse_submitted_curve_mw8_from (float | Unset):
        qse_submitted_curve_mw8_to (float | Unset):
        qse_submitted_curve_price_8_from (float | Unset):
        qse_submitted_curve_price_8_to (float | Unset):
        qse_submitted_curve_mw9_from (float | Unset):
        qse_submitted_curve_mw9_to (float | Unset):
        qse_submitted_curve_price_9_from (float | Unset):
        qse_submitted_curve_price_9_to (float | Unset):
        qse_submitted_curve_mw10_from (float | Unset):
        qse_submitted_curve_mw10_to (float | Unset):
        qse_submitted_curve_price_10_from (float | Unset):
        qse_submitted_curve_price_10_to (float | Unset):
        start_up_hot_from (float | Unset):
        start_up_hot_to (float | Unset):
        start_up_inter_from (float | Unset):
        start_up_inter_to (float | Unset):
        start_up_cold_from (float | Unset):
        start_up_cold_to (float | Unset):
        min_gen_cost_from (float | Unset):
        min_gen_cost_to (float | Unset):
        hsl_from (float | Unset):
        hsl_to (float | Unset):
        lsl_from (float | Unset):
        lsl_to (float | Unset):
        resource_status (str | Unset):
        awarded_quantity_from (int | Unset):
        awarded_quantity_to (int | Unset):
        settlement_point_name (str | Unset):
        energy_settlement_point_price_from (float | Unset):
        energy_settlement_point_price_to (float | Unset):
        regup_awarded_from (float | Unset):
        regup_awarded_to (float | Unset):
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
        delivery_date_from=delivery_date_from,
        delivery_date_to=delivery_date_to,
        hour_ending_from=hour_ending_from,
        hour_ending_to=hour_ending_to,
        qse_name=qse_name,
        dme_name=dme_name,
        resource_name=resource_name,
        resource_type=resource_type,
        qse_submitted_curve_mw1_from=qse_submitted_curve_mw1_from,
        qse_submitted_curve_mw1_to=qse_submitted_curve_mw1_to,
        qse_submitted_curve_price_1_from=qse_submitted_curve_price_1_from,
        qse_submitted_curve_price_1_to=qse_submitted_curve_price_1_to,
        qse_submitted_curve_mw2_from=qse_submitted_curve_mw2_from,
        qse_submitted_curve_mw2_to=qse_submitted_curve_mw2_to,
        qse_submitted_curve_price_2_from=qse_submitted_curve_price_2_from,
        qse_submitted_curve_price_2_to=qse_submitted_curve_price_2_to,
        qse_submitted_curve_mw3_from=qse_submitted_curve_mw3_from,
        qse_submitted_curve_mw3_to=qse_submitted_curve_mw3_to,
        qse_submitted_curve_price_3_from=qse_submitted_curve_price_3_from,
        qse_submitted_curve_price_3_to=qse_submitted_curve_price_3_to,
        qse_submitted_curve_mw4_from=qse_submitted_curve_mw4_from,
        qse_submitted_curve_mw4_to=qse_submitted_curve_mw4_to,
        qse_submitted_curve_price_4_from=qse_submitted_curve_price_4_from,
        qse_submitted_curve_price_4_to=qse_submitted_curve_price_4_to,
        qse_submitted_curve_mw5_from=qse_submitted_curve_mw5_from,
        qse_submitted_curve_mw5_to=qse_submitted_curve_mw5_to,
        qse_submitted_curve_price_5_from=qse_submitted_curve_price_5_from,
        qse_submitted_curve_price_5_to=qse_submitted_curve_price_5_to,
        qse_submitted_curve_mw6_from=qse_submitted_curve_mw6_from,
        qse_submitted_curve_mw6_to=qse_submitted_curve_mw6_to,
        qse_submitted_curve_price_6_from=qse_submitted_curve_price_6_from,
        qse_submitted_curve_price_6_to=qse_submitted_curve_price_6_to,
        qse_submitted_curve_mw7_from=qse_submitted_curve_mw7_from,
        qse_submitted_curve_mw7_to=qse_submitted_curve_mw7_to,
        qse_submitted_curve_price_7_from=qse_submitted_curve_price_7_from,
        qse_submitted_curve_price_7_to=qse_submitted_curve_price_7_to,
        qse_submitted_curve_mw8_from=qse_submitted_curve_mw8_from,
        qse_submitted_curve_mw8_to=qse_submitted_curve_mw8_to,
        qse_submitted_curve_price_8_from=qse_submitted_curve_price_8_from,
        qse_submitted_curve_price_8_to=qse_submitted_curve_price_8_to,
        qse_submitted_curve_mw9_from=qse_submitted_curve_mw9_from,
        qse_submitted_curve_mw9_to=qse_submitted_curve_mw9_to,
        qse_submitted_curve_price_9_from=qse_submitted_curve_price_9_from,
        qse_submitted_curve_price_9_to=qse_submitted_curve_price_9_to,
        qse_submitted_curve_mw10_from=qse_submitted_curve_mw10_from,
        qse_submitted_curve_mw10_to=qse_submitted_curve_mw10_to,
        qse_submitted_curve_price_10_from=qse_submitted_curve_price_10_from,
        qse_submitted_curve_price_10_to=qse_submitted_curve_price_10_to,
        start_up_hot_from=start_up_hot_from,
        start_up_hot_to=start_up_hot_to,
        start_up_inter_from=start_up_inter_from,
        start_up_inter_to=start_up_inter_to,
        start_up_cold_from=start_up_cold_from,
        start_up_cold_to=start_up_cold_to,
        min_gen_cost_from=min_gen_cost_from,
        min_gen_cost_to=min_gen_cost_to,
        hsl_from=hsl_from,
        hsl_to=hsl_to,
        lsl_from=lsl_from,
        lsl_to=lsl_to,
        resource_status=resource_status,
        awarded_quantity_from=awarded_quantity_from,
        awarded_quantity_to=awarded_quantity_to,
        settlement_point_name=settlement_point_name,
        energy_settlement_point_price_from=energy_settlement_point_price_from,
        energy_settlement_point_price_to=energy_settlement_point_price_to,
        regup_awarded_from=regup_awarded_from,
        regup_awarded_to=regup_awarded_to,
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
    delivery_date_from: str | Unset = UNSET,
    delivery_date_to: str | Unset = UNSET,
    hour_ending_from: str | Unset = UNSET,
    hour_ending_to: str | Unset = UNSET,
    qse_name: str | Unset = UNSET,
    dme_name: str | Unset = UNSET,
    resource_name: str | Unset = UNSET,
    resource_type: str | Unset = UNSET,
    qse_submitted_curve_mw1_from: float | Unset = UNSET,
    qse_submitted_curve_mw1_to: float | Unset = UNSET,
    qse_submitted_curve_price_1_from: float | Unset = UNSET,
    qse_submitted_curve_price_1_to: float | Unset = UNSET,
    qse_submitted_curve_mw2_from: float | Unset = UNSET,
    qse_submitted_curve_mw2_to: float | Unset = UNSET,
    qse_submitted_curve_price_2_from: float | Unset = UNSET,
    qse_submitted_curve_price_2_to: float | Unset = UNSET,
    qse_submitted_curve_mw3_from: float | Unset = UNSET,
    qse_submitted_curve_mw3_to: float | Unset = UNSET,
    qse_submitted_curve_price_3_from: float | Unset = UNSET,
    qse_submitted_curve_price_3_to: float | Unset = UNSET,
    qse_submitted_curve_mw4_from: float | Unset = UNSET,
    qse_submitted_curve_mw4_to: float | Unset = UNSET,
    qse_submitted_curve_price_4_from: float | Unset = UNSET,
    qse_submitted_curve_price_4_to: float | Unset = UNSET,
    qse_submitted_curve_mw5_from: float | Unset = UNSET,
    qse_submitted_curve_mw5_to: float | Unset = UNSET,
    qse_submitted_curve_price_5_from: float | Unset = UNSET,
    qse_submitted_curve_price_5_to: float | Unset = UNSET,
    qse_submitted_curve_mw6_from: float | Unset = UNSET,
    qse_submitted_curve_mw6_to: float | Unset = UNSET,
    qse_submitted_curve_price_6_from: float | Unset = UNSET,
    qse_submitted_curve_price_6_to: float | Unset = UNSET,
    qse_submitted_curve_mw7_from: float | Unset = UNSET,
    qse_submitted_curve_mw7_to: float | Unset = UNSET,
    qse_submitted_curve_price_7_from: float | Unset = UNSET,
    qse_submitted_curve_price_7_to: float | Unset = UNSET,
    qse_submitted_curve_mw8_from: float | Unset = UNSET,
    qse_submitted_curve_mw8_to: float | Unset = UNSET,
    qse_submitted_curve_price_8_from: float | Unset = UNSET,
    qse_submitted_curve_price_8_to: float | Unset = UNSET,
    qse_submitted_curve_mw9_from: float | Unset = UNSET,
    qse_submitted_curve_mw9_to: float | Unset = UNSET,
    qse_submitted_curve_price_9_from: float | Unset = UNSET,
    qse_submitted_curve_price_9_to: float | Unset = UNSET,
    qse_submitted_curve_mw10_from: float | Unset = UNSET,
    qse_submitted_curve_mw10_to: float | Unset = UNSET,
    qse_submitted_curve_price_10_from: float | Unset = UNSET,
    qse_submitted_curve_price_10_to: float | Unset = UNSET,
    start_up_hot_from: float | Unset = UNSET,
    start_up_hot_to: float | Unset = UNSET,
    start_up_inter_from: float | Unset = UNSET,
    start_up_inter_to: float | Unset = UNSET,
    start_up_cold_from: float | Unset = UNSET,
    start_up_cold_to: float | Unset = UNSET,
    min_gen_cost_from: float | Unset = UNSET,
    min_gen_cost_to: float | Unset = UNSET,
    hsl_from: float | Unset = UNSET,
    hsl_to: float | Unset = UNSET,
    lsl_from: float | Unset = UNSET,
    lsl_to: float | Unset = UNSET,
    resource_status: str | Unset = UNSET,
    awarded_quantity_from: int | Unset = UNSET,
    awarded_quantity_to: int | Unset = UNSET,
    settlement_point_name: str | Unset = UNSET,
    energy_settlement_point_price_from: float | Unset = UNSET,
    energy_settlement_point_price_to: float | Unset = UNSET,
    regup_awarded_from: float | Unset = UNSET,
    regup_awarded_to: float | Unset = UNSET,
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
    """60 Day DAM Generation Resource Data

     60 Day DAM Generation Resource Data

    Args:
        delivery_date_from (str | Unset):
        delivery_date_to (str | Unset):
        hour_ending_from (str | Unset):
        hour_ending_to (str | Unset):
        qse_name (str | Unset):
        dme_name (str | Unset):
        resource_name (str | Unset):
        resource_type (str | Unset):
        qse_submitted_curve_mw1_from (float | Unset):
        qse_submitted_curve_mw1_to (float | Unset):
        qse_submitted_curve_price_1_from (float | Unset):
        qse_submitted_curve_price_1_to (float | Unset):
        qse_submitted_curve_mw2_from (float | Unset):
        qse_submitted_curve_mw2_to (float | Unset):
        qse_submitted_curve_price_2_from (float | Unset):
        qse_submitted_curve_price_2_to (float | Unset):
        qse_submitted_curve_mw3_from (float | Unset):
        qse_submitted_curve_mw3_to (float | Unset):
        qse_submitted_curve_price_3_from (float | Unset):
        qse_submitted_curve_price_3_to (float | Unset):
        qse_submitted_curve_mw4_from (float | Unset):
        qse_submitted_curve_mw4_to (float | Unset):
        qse_submitted_curve_price_4_from (float | Unset):
        qse_submitted_curve_price_4_to (float | Unset):
        qse_submitted_curve_mw5_from (float | Unset):
        qse_submitted_curve_mw5_to (float | Unset):
        qse_submitted_curve_price_5_from (float | Unset):
        qse_submitted_curve_price_5_to (float | Unset):
        qse_submitted_curve_mw6_from (float | Unset):
        qse_submitted_curve_mw6_to (float | Unset):
        qse_submitted_curve_price_6_from (float | Unset):
        qse_submitted_curve_price_6_to (float | Unset):
        qse_submitted_curve_mw7_from (float | Unset):
        qse_submitted_curve_mw7_to (float | Unset):
        qse_submitted_curve_price_7_from (float | Unset):
        qse_submitted_curve_price_7_to (float | Unset):
        qse_submitted_curve_mw8_from (float | Unset):
        qse_submitted_curve_mw8_to (float | Unset):
        qse_submitted_curve_price_8_from (float | Unset):
        qse_submitted_curve_price_8_to (float | Unset):
        qse_submitted_curve_mw9_from (float | Unset):
        qse_submitted_curve_mw9_to (float | Unset):
        qse_submitted_curve_price_9_from (float | Unset):
        qse_submitted_curve_price_9_to (float | Unset):
        qse_submitted_curve_mw10_from (float | Unset):
        qse_submitted_curve_mw10_to (float | Unset):
        qse_submitted_curve_price_10_from (float | Unset):
        qse_submitted_curve_price_10_to (float | Unset):
        start_up_hot_from (float | Unset):
        start_up_hot_to (float | Unset):
        start_up_inter_from (float | Unset):
        start_up_inter_to (float | Unset):
        start_up_cold_from (float | Unset):
        start_up_cold_to (float | Unset):
        min_gen_cost_from (float | Unset):
        min_gen_cost_to (float | Unset):
        hsl_from (float | Unset):
        hsl_to (float | Unset):
        lsl_from (float | Unset):
        lsl_to (float | Unset):
        resource_status (str | Unset):
        awarded_quantity_from (int | Unset):
        awarded_quantity_to (int | Unset):
        settlement_point_name (str | Unset):
        energy_settlement_point_price_from (float | Unset):
        energy_settlement_point_price_to (float | Unset):
        regup_awarded_from (float | Unset):
        regup_awarded_to (float | Unset):
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
            delivery_date_from=delivery_date_from,
            delivery_date_to=delivery_date_to,
            hour_ending_from=hour_ending_from,
            hour_ending_to=hour_ending_to,
            qse_name=qse_name,
            dme_name=dme_name,
            resource_name=resource_name,
            resource_type=resource_type,
            qse_submitted_curve_mw1_from=qse_submitted_curve_mw1_from,
            qse_submitted_curve_mw1_to=qse_submitted_curve_mw1_to,
            qse_submitted_curve_price_1_from=qse_submitted_curve_price_1_from,
            qse_submitted_curve_price_1_to=qse_submitted_curve_price_1_to,
            qse_submitted_curve_mw2_from=qse_submitted_curve_mw2_from,
            qse_submitted_curve_mw2_to=qse_submitted_curve_mw2_to,
            qse_submitted_curve_price_2_from=qse_submitted_curve_price_2_from,
            qse_submitted_curve_price_2_to=qse_submitted_curve_price_2_to,
            qse_submitted_curve_mw3_from=qse_submitted_curve_mw3_from,
            qse_submitted_curve_mw3_to=qse_submitted_curve_mw3_to,
            qse_submitted_curve_price_3_from=qse_submitted_curve_price_3_from,
            qse_submitted_curve_price_3_to=qse_submitted_curve_price_3_to,
            qse_submitted_curve_mw4_from=qse_submitted_curve_mw4_from,
            qse_submitted_curve_mw4_to=qse_submitted_curve_mw4_to,
            qse_submitted_curve_price_4_from=qse_submitted_curve_price_4_from,
            qse_submitted_curve_price_4_to=qse_submitted_curve_price_4_to,
            qse_submitted_curve_mw5_from=qse_submitted_curve_mw5_from,
            qse_submitted_curve_mw5_to=qse_submitted_curve_mw5_to,
            qse_submitted_curve_price_5_from=qse_submitted_curve_price_5_from,
            qse_submitted_curve_price_5_to=qse_submitted_curve_price_5_to,
            qse_submitted_curve_mw6_from=qse_submitted_curve_mw6_from,
            qse_submitted_curve_mw6_to=qse_submitted_curve_mw6_to,
            qse_submitted_curve_price_6_from=qse_submitted_curve_price_6_from,
            qse_submitted_curve_price_6_to=qse_submitted_curve_price_6_to,
            qse_submitted_curve_mw7_from=qse_submitted_curve_mw7_from,
            qse_submitted_curve_mw7_to=qse_submitted_curve_mw7_to,
            qse_submitted_curve_price_7_from=qse_submitted_curve_price_7_from,
            qse_submitted_curve_price_7_to=qse_submitted_curve_price_7_to,
            qse_submitted_curve_mw8_from=qse_submitted_curve_mw8_from,
            qse_submitted_curve_mw8_to=qse_submitted_curve_mw8_to,
            qse_submitted_curve_price_8_from=qse_submitted_curve_price_8_from,
            qse_submitted_curve_price_8_to=qse_submitted_curve_price_8_to,
            qse_submitted_curve_mw9_from=qse_submitted_curve_mw9_from,
            qse_submitted_curve_mw9_to=qse_submitted_curve_mw9_to,
            qse_submitted_curve_price_9_from=qse_submitted_curve_price_9_from,
            qse_submitted_curve_price_9_to=qse_submitted_curve_price_9_to,
            qse_submitted_curve_mw10_from=qse_submitted_curve_mw10_from,
            qse_submitted_curve_mw10_to=qse_submitted_curve_mw10_to,
            qse_submitted_curve_price_10_from=qse_submitted_curve_price_10_from,
            qse_submitted_curve_price_10_to=qse_submitted_curve_price_10_to,
            start_up_hot_from=start_up_hot_from,
            start_up_hot_to=start_up_hot_to,
            start_up_inter_from=start_up_inter_from,
            start_up_inter_to=start_up_inter_to,
            start_up_cold_from=start_up_cold_from,
            start_up_cold_to=start_up_cold_to,
            min_gen_cost_from=min_gen_cost_from,
            min_gen_cost_to=min_gen_cost_to,
            hsl_from=hsl_from,
            hsl_to=hsl_to,
            lsl_from=lsl_from,
            lsl_to=lsl_to,
            resource_status=resource_status,
            awarded_quantity_from=awarded_quantity_from,
            awarded_quantity_to=awarded_quantity_to,
            settlement_point_name=settlement_point_name,
            energy_settlement_point_price_from=energy_settlement_point_price_from,
            energy_settlement_point_price_to=energy_settlement_point_price_to,
            regup_awarded_from=regup_awarded_from,
            regup_awarded_to=regup_awarded_to,
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
