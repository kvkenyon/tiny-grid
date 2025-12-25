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
    sced2_curve_mw9_from: float | Unset = UNSET,
    sced2_curve_mw9_to: float | Unset = UNSET,
    sced2_curve_price_9_from: float | Unset = UNSET,
    sced2_curve_price_9_to: float | Unset = UNSET,
    sced2_curve_mw10_from: float | Unset = UNSET,
    sced2_curve_mw10_to: float | Unset = UNSET,
    sced2_curve_price_10_from: float | Unset = UNSET,
    sced2_curve_price_10_to: float | Unset = UNSET,
    sced2_curve_mw11_from: float | Unset = UNSET,
    sced2_curve_mw11_to: float | Unset = UNSET,
    sced2_curve_price_11_from: float | Unset = UNSET,
    sced2_curve_price_11_to: float | Unset = UNSET,
    sced2_curve_mw12_from: float | Unset = UNSET,
    sced2_curve_mw12_to: float | Unset = UNSET,
    sced2_curve_price_12_from: float | Unset = UNSET,
    sced2_curve_price_12_to: float | Unset = UNSET,
    sced2_curve_mw13_from: float | Unset = UNSET,
    sced2_curve_mw13_to: float | Unset = UNSET,
    sced2_curve_price_13_from: float | Unset = UNSET,
    sced2_curve_price_13_to: float | Unset = UNSET,
    sced2_curve_mw14_from: float | Unset = UNSET,
    sced2_curve_mw14_to: float | Unset = UNSET,
    sced2_curve_price_14_from: float | Unset = UNSET,
    sced2_curve_price_14_to: float | Unset = UNSET,
    sced2_curve_mw15_from: float | Unset = UNSET,
    sced2_curve_mw15_to: float | Unset = UNSET,
    sced2_curve_price_15_from: float | Unset = UNSET,
    sced2_curve_price_15_to: float | Unset = UNSET,
    sced2_curve_mw16_from: float | Unset = UNSET,
    sced2_curve_mw16_to: float | Unset = UNSET,
    sced2_curve_price_16_from: float | Unset = UNSET,
    sced2_curve_price_16_to: float | Unset = UNSET,
    sced2_curve_mw17_from: float | Unset = UNSET,
    sced2_curve_mw17_to: float | Unset = UNSET,
    sced2_curve_price_17_from: float | Unset = UNSET,
    sced2_curve_price_17_to: float | Unset = UNSET,
    sced2_curve_mw18_from: float | Unset = UNSET,
    sced2_curve_mw18_to: float | Unset = UNSET,
    sced2_curve_price_18_from: float | Unset = UNSET,
    sced2_curve_price_18_to: float | Unset = UNSET,
    sced2_curve_mw19_from: float | Unset = UNSET,
    sced2_curve_mw19_to: float | Unset = UNSET,
    sced2_curve_price_19_from: float | Unset = UNSET,
    sced2_curve_price_19_to: float | Unset = UNSET,
    sced2_curve_mw20_from: float | Unset = UNSET,
    sced2_curve_mw20_to: float | Unset = UNSET,
    sced2_curve_price_20_from: float | Unset = UNSET,
    sced2_curve_price_20_to: float | Unset = UNSET,
    sced2_curve_mw21_from: float | Unset = UNSET,
    sced2_curve_mw21_to: float | Unset = UNSET,
    sced2_curve_price_21_from: float | Unset = UNSET,
    sced2_curve_price_21_to: float | Unset = UNSET,
    sced2_curve_mw22_from: float | Unset = UNSET,
    sced2_curve_mw22_to: float | Unset = UNSET,
    sced2_curve_price_22_from: float | Unset = UNSET,
    sced2_curve_price_22_to: float | Unset = UNSET,
    sced2_curve_mw23_from: float | Unset = UNSET,
    sced2_curve_mw23_to: float | Unset = UNSET,
    sced2_curve_price_23_from: float | Unset = UNSET,
    sced2_curve_price_23_to: float | Unset = UNSET,
    sced2_curve_mw24_from: float | Unset = UNSET,
    sced2_curve_mw24_to: float | Unset = UNSET,
    sced2_curve_price_24_from: float | Unset = UNSET,
    sced2_curve_price_24_to: float | Unset = UNSET,
    sced2_curve_mw25_from: float | Unset = UNSET,
    sced2_curve_mw25_to: float | Unset = UNSET,
    sced2_curve_price_25_from: float | Unset = UNSET,
    sced2_curve_price_25_to: float | Unset = UNSET,
    sced2_curve_mw26_from: float | Unset = UNSET,
    sced2_curve_mw26_to: float | Unset = UNSET,
    sced2_curve_price_26_from: float | Unset = UNSET,
    sced2_curve_price_26_to: float | Unset = UNSET,
    sced2_curve_mw27_from: float | Unset = UNSET,
    sced2_curve_mw27_to: float | Unset = UNSET,
    sced2_curve_price_27_from: float | Unset = UNSET,
    sced2_curve_price_27_to: float | Unset = UNSET,
    sced2_curve_mw28_from: float | Unset = UNSET,
    sced2_curve_mw28_to: float | Unset = UNSET,
    sced2_curve_price_28_from: float | Unset = UNSET,
    sced2_curve_price_28_to: float | Unset = UNSET,
    sced2_curve_mw29_from: float | Unset = UNSET,
    sced2_curve_mw29_to: float | Unset = UNSET,
    sced2_curve_price_29_from: float | Unset = UNSET,
    sced2_curve_price_29_to: float | Unset = UNSET,
    sced2_curve_mw30_from: float | Unset = UNSET,
    sced2_curve_mw30_to: float | Unset = UNSET,
    sced2_curve_price_30_from: float | Unset = UNSET,
    sced2_curve_price_30_to: float | Unset = UNSET,
    sced2_curve_mw31_from: float | Unset = UNSET,
    sced2_curve_mw31_to: float | Unset = UNSET,
    sced2_curve_price_31_from: float | Unset = UNSET,
    sced2_curve_price_31_to: float | Unset = UNSET,
    sced2_curve_mw32_from: float | Unset = UNSET,
    sced2_curve_mw32_to: float | Unset = UNSET,
    sced2_curve_price_32_from: float | Unset = UNSET,
    sced2_curve_price_32_to: float | Unset = UNSET,
    sced2_curve_mw33_from: float | Unset = UNSET,
    sced2_curve_mw33_to: float | Unset = UNSET,
    sced2_curve_price_33_from: float | Unset = UNSET,
    sced2_curve_price_33_to: float | Unset = UNSET,
    sced2_curve_mw34_from: float | Unset = UNSET,
    sced2_curve_mw34_to: float | Unset = UNSET,
    sced2_curve_price_34_from: float | Unset = UNSET,
    sced2_curve_price_34_to: float | Unset = UNSET,
    sced2_curve_mw35_from: float | Unset = UNSET,
    sced2_curve_mw35_to: float | Unset = UNSET,
    sced2_curve_price_35_from: float | Unset = UNSET,
    sced2_curve_price_35_to: float | Unset = UNSET,
    output_schedule_from: float | Unset = UNSET,
    output_schedule_to: float | Unset = UNSET,
    hsl_from: float | Unset = UNSET,
    hsl_to: float | Unset = UNSET,
    hasl_from: float | Unset = UNSET,
    hasl_to: float | Unset = UNSET,
    hdl_from: float | Unset = UNSET,
    hdl_to: float | Unset = UNSET,
    lsl_from: float | Unset = UNSET,
    lsl_to: float | Unset = UNSET,
    lasl_from: float | Unset = UNSET,
    lasl_to: float | Unset = UNSET,
    ldl_from: float | Unset = UNSET,
    ldl_to: float | Unset = UNSET,
    telemetered_resource_status: str | Unset = UNSET,
    base_point_from: float | Unset = UNSET,
    base_point_to: float | Unset = UNSET,
    telemetered_net_output_from: float | Unset = UNSET,
    telemetered_net_output_to: float | Unset = UNSET,
    asregup_from: float | Unset = UNSET,
    asregup_to: float | Unset = UNSET,
    asregdn_from: float | Unset = UNSET,
    asregdn_to: float | Unset = UNSET,
    asrrs_from: float | Unset = UNSET,
    asrrs_to: float | Unset = UNSET,
    asrrsffr_from: float | Unset = UNSET,
    asrrsffr_to: float | Unset = UNSET,
    asnsrs_from: float | Unset = UNSET,
    asnsrs_to: float | Unset = UNSET,
    bid_type: str | Unset = UNSET,
    start_up_cold_offer_from: float | Unset = UNSET,
    start_up_cold_offer_to: float | Unset = UNSET,
    start_up_hot_offer_from: float | Unset = UNSET,
    start_up_hot_offer_to: float | Unset = UNSET,
    start_up_inter_offer_from: float | Unset = UNSET,
    start_up_inter_offer_to: float | Unset = UNSET,
    min_gen_cost_from: float | Unset = UNSET,
    min_gen_cost_to: float | Unset = UNSET,
    submitted_tpomw1_from: float | Unset = UNSET,
    submitted_tpomw1_to: float | Unset = UNSET,
    submitted_tpo_price_1_from: float | Unset = UNSET,
    submitted_tpo_price_1_to: float | Unset = UNSET,
    submitted_tpomw2_from: float | Unset = UNSET,
    submitted_tpomw2_to: float | Unset = UNSET,
    submitted_tpo_price_2_from: float | Unset = UNSET,
    submitted_tpo_price_2_to: float | Unset = UNSET,
    submitted_tpomw3_from: float | Unset = UNSET,
    submitted_tpomw3_to: float | Unset = UNSET,
    submitted_tpo_price_3_from: float | Unset = UNSET,
    submitted_tpo_price_3_to: float | Unset = UNSET,
    submitted_tpomw4_from: float | Unset = UNSET,
    submitted_tpomw4_to: float | Unset = UNSET,
    submitted_tpo_price_4_from: float | Unset = UNSET,
    submitted_tpo_price_4_to: float | Unset = UNSET,
    submitted_tpomw5_from: float | Unset = UNSET,
    submitted_tpomw5_to: float | Unset = UNSET,
    submitted_tpo_price_5_from: float | Unset = UNSET,
    submitted_tpo_price_5_to: float | Unset = UNSET,
    submitted_tpomw6_from: float | Unset = UNSET,
    submitted_tpomw6_to: float | Unset = UNSET,
    submitted_tpo_price_6_from: float | Unset = UNSET,
    submitted_tpo_price_6_to: float | Unset = UNSET,
    submitted_tpomw7_from: float | Unset = UNSET,
    submitted_tpomw7_to: float | Unset = UNSET,
    submitted_tpo_price_7_from: float | Unset = UNSET,
    submitted_tpo_price_7_to: float | Unset = UNSET,
    submitted_tpomw8_from: float | Unset = UNSET,
    submitted_tpomw8_to: float | Unset = UNSET,
    submitted_tpo_price_8_from: float | Unset = UNSET,
    submitted_tpo_price_8_to: float | Unset = UNSET,
    submitted_tpomw9_from: float | Unset = UNSET,
    submitted_tpomw9_to: float | Unset = UNSET,
    submitted_tpo_price_9_from: float | Unset = UNSET,
    submitted_tpo_price_9_to: float | Unset = UNSET,
    submitted_tpomw10_from: float | Unset = UNSET,
    submitted_tpomw10_to: float | Unset = UNSET,
    submitted_tpo_price_10_from: float | Unset = UNSET,
    submitted_tpo_price_10_to: float | Unset = UNSET,
    proxy_extension: str | Unset = UNSET,
    sced_timestamp_from: str | Unset = UNSET,
    sced_timestamp_to: str | Unset = UNSET,
    repeat_hour_flag: bool | Unset = UNSET,
    qse_name: str | Unset = UNSET,
    dme_name: str | Unset = UNSET,
    resource_name: str | Unset = UNSET,
    resource_type: str | Unset = UNSET,
    sced1_curve_mw1_from: float | Unset = UNSET,
    sced1_curve_mw1_to: float | Unset = UNSET,
    sced1_curve_price_1_from: float | Unset = UNSET,
    sced1_curve_price_1_to: float | Unset = UNSET,
    sced1_curve_mw2_from: float | Unset = UNSET,
    sced1_curve_mw2_to: float | Unset = UNSET,
    sced1_curve_price_2_from: float | Unset = UNSET,
    sced1_curve_price_2_to: float | Unset = UNSET,
    sced1_curve_mw3_from: float | Unset = UNSET,
    sced1_curve_mw3_to: float | Unset = UNSET,
    sced1_curve_price_3_from: float | Unset = UNSET,
    sced1_curve_price_3_to: float | Unset = UNSET,
    sced1_curve_mw4_from: float | Unset = UNSET,
    sced1_curve_mw4_to: float | Unset = UNSET,
    sced1_curve_price_4_from: float | Unset = UNSET,
    sced1_curve_price_4_to: float | Unset = UNSET,
    sced1_curve_mw5_from: float | Unset = UNSET,
    sced1_curve_mw5_to: float | Unset = UNSET,
    sced1_curve_price_5_from: float | Unset = UNSET,
    sced1_curve_price_5_to: float | Unset = UNSET,
    sced1_curve_mw6_from: float | Unset = UNSET,
    sced1_curve_mw6_to: float | Unset = UNSET,
    sced1_curve_price_6_from: float | Unset = UNSET,
    sced1_curve_price_6_to: float | Unset = UNSET,
    sced1_curve_mw7_from: float | Unset = UNSET,
    sced1_curve_mw7_to: float | Unset = UNSET,
    sced1_curve_price_7_from: float | Unset = UNSET,
    sced1_curve_price_7_to: float | Unset = UNSET,
    sced1_curve_mw8_from: float | Unset = UNSET,
    sced1_curve_mw8_to: float | Unset = UNSET,
    sced1_curve_price_8_from: float | Unset = UNSET,
    sced1_curve_price_8_to: float | Unset = UNSET,
    sced1_curve_mw9_from: float | Unset = UNSET,
    sced1_curve_mw9_to: float | Unset = UNSET,
    sced1_curve_price_9_from: float | Unset = UNSET,
    sced1_curve_price_9_to: float | Unset = UNSET,
    sced1_curve_mw10_from: float | Unset = UNSET,
    sced1_curve_mw10_to: float | Unset = UNSET,
    sced1_curve_price_10_from: float | Unset = UNSET,
    sced1_curve_price_10_to: float | Unset = UNSET,
    sced1_curve_mw11_from: float | Unset = UNSET,
    sced1_curve_mw11_to: float | Unset = UNSET,
    sced1_curve_price_11_from: float | Unset = UNSET,
    sced1_curve_price_11_to: float | Unset = UNSET,
    sced1_curve_mw12_from: float | Unset = UNSET,
    sced1_curve_mw12_to: float | Unset = UNSET,
    sced1_curve_price_12_from: float | Unset = UNSET,
    sced1_curve_price_12_to: float | Unset = UNSET,
    sced1_curve_mw13_from: float | Unset = UNSET,
    sced1_curve_mw13_to: float | Unset = UNSET,
    sced1_curve_price_13_from: float | Unset = UNSET,
    sced1_curve_price_13_to: float | Unset = UNSET,
    sced1_curve_mw14_from: float | Unset = UNSET,
    sced1_curve_mw14_to: float | Unset = UNSET,
    sced1_curve_price_14_from: float | Unset = UNSET,
    sced1_curve_price_14_to: float | Unset = UNSET,
    sced1_curve_mw15_from: float | Unset = UNSET,
    sced1_curve_mw15_to: float | Unset = UNSET,
    sced1_curve_price_15_from: float | Unset = UNSET,
    sced1_curve_price_15_to: float | Unset = UNSET,
    sced1_curve_mw16_from: float | Unset = UNSET,
    sced1_curve_mw16_to: float | Unset = UNSET,
    sced1_curve_price_16_from: float | Unset = UNSET,
    sced1_curve_price_16_to: float | Unset = UNSET,
    sced1_curve_mw17_from: float | Unset = UNSET,
    sced1_curve_mw17_to: float | Unset = UNSET,
    sced1_curve_price_17_from: float | Unset = UNSET,
    sced1_curve_price_17_to: float | Unset = UNSET,
    sced1_curve_mw18_from: float | Unset = UNSET,
    sced1_curve_mw18_to: float | Unset = UNSET,
    sced1_curve_price_18_from: float | Unset = UNSET,
    sced1_curve_price_18_to: float | Unset = UNSET,
    sced1_curve_mw19_from: float | Unset = UNSET,
    sced1_curve_mw19_to: float | Unset = UNSET,
    sced1_curve_price_19_from: float | Unset = UNSET,
    sced1_curve_price_19_to: float | Unset = UNSET,
    sced1_curve_mw20_from: float | Unset = UNSET,
    sced1_curve_mw20_to: float | Unset = UNSET,
    sced1_curve_price_20_from: float | Unset = UNSET,
    sced1_curve_price_20_to: float | Unset = UNSET,
    sced1_curve_mw21_from: float | Unset = UNSET,
    sced1_curve_mw21_to: float | Unset = UNSET,
    sced1_curve_price_21_from: float | Unset = UNSET,
    sced1_curve_price_21_to: float | Unset = UNSET,
    sced1_curve_mw22_from: float | Unset = UNSET,
    sced1_curve_mw22_to: float | Unset = UNSET,
    sced1_curve_price_22_from: float | Unset = UNSET,
    sced1_curve_price_22_to: float | Unset = UNSET,
    sced1_curve_mw23_from: float | Unset = UNSET,
    sced1_curve_mw23_to: float | Unset = UNSET,
    sced1_curve_price_23_from: float | Unset = UNSET,
    sced1_curve_price_23_to: float | Unset = UNSET,
    sced1_curve_mw24_from: float | Unset = UNSET,
    sced1_curve_mw24_to: float | Unset = UNSET,
    sced1_curve_price_24_from: float | Unset = UNSET,
    sced1_curve_price_24_to: float | Unset = UNSET,
    sced1_curve_mw25_from: float | Unset = UNSET,
    sced1_curve_mw25_to: float | Unset = UNSET,
    sced1_curve_price_25_from: float | Unset = UNSET,
    sced1_curve_price_25_to: float | Unset = UNSET,
    sced1_curve_mw26_from: float | Unset = UNSET,
    sced1_curve_mw26_to: float | Unset = UNSET,
    sced1_curve_price_26_from: float | Unset = UNSET,
    sced1_curve_price_26_to: float | Unset = UNSET,
    sced1_curve_mw27_from: float | Unset = UNSET,
    sced1_curve_mw27_to: float | Unset = UNSET,
    sced1_curve_price_27_from: float | Unset = UNSET,
    sced1_curve_price_27_to: float | Unset = UNSET,
    sced1_curve_mw28_from: float | Unset = UNSET,
    sced1_curve_mw28_to: float | Unset = UNSET,
    sced1_curve_price_28_from: float | Unset = UNSET,
    sced1_curve_price_28_to: float | Unset = UNSET,
    sced1_curve_mw29_from: float | Unset = UNSET,
    sced1_curve_mw29_to: float | Unset = UNSET,
    sced1_curve_price_29_from: float | Unset = UNSET,
    sced1_curve_price_29_to: float | Unset = UNSET,
    sced1_curve_mw30_from: float | Unset = UNSET,
    sced1_curve_mw30_to: float | Unset = UNSET,
    sced1_curve_price_30_from: float | Unset = UNSET,
    sced1_curve_price_30_to: float | Unset = UNSET,
    sced1_curve_mw31_from: float | Unset = UNSET,
    sced1_curve_mw31_to: float | Unset = UNSET,
    sced1_curve_price_31_from: float | Unset = UNSET,
    sced1_curve_price_31_to: float | Unset = UNSET,
    sced1_curve_mw32_from: float | Unset = UNSET,
    sced1_curve_mw32_to: float | Unset = UNSET,
    sced1_curve_price_32_from: float | Unset = UNSET,
    sced1_curve_price_32_to: float | Unset = UNSET,
    sced1_curve_mw33_from: float | Unset = UNSET,
    sced1_curve_mw33_to: float | Unset = UNSET,
    sced1_curve_price_33_from: float | Unset = UNSET,
    sced1_curve_price_33_to: float | Unset = UNSET,
    sced1_curve_mw34_from: float | Unset = UNSET,
    sced1_curve_mw34_to: float | Unset = UNSET,
    sced1_curve_price_34_from: float | Unset = UNSET,
    sced1_curve_price_34_to: float | Unset = UNSET,
    sced1_curve_mw35_from: float | Unset = UNSET,
    sced1_curve_mw35_to: float | Unset = UNSET,
    sced1_curve_price_35_from: float | Unset = UNSET,
    sced1_curve_price_35_to: float | Unset = UNSET,
    sced2_curve_mw1_from: float | Unset = UNSET,
    sced2_curve_mw1_to: float | Unset = UNSET,
    sced2_curve_price_1_from: float | Unset = UNSET,
    sced2_curve_price_1_to: float | Unset = UNSET,
    sced2_curve_mw2_from: float | Unset = UNSET,
    sced2_curve_mw2_to: float | Unset = UNSET,
    sced2_curve_price_2_from: float | Unset = UNSET,
    sced2_curve_price_2_to: float | Unset = UNSET,
    sced2_curve_mw3_from: float | Unset = UNSET,
    sced2_curve_mw3_to: float | Unset = UNSET,
    sced2_curve_price_3_from: float | Unset = UNSET,
    sced2_curve_price_3_to: float | Unset = UNSET,
    sced2_curve_mw4_from: float | Unset = UNSET,
    sced2_curve_mw4_to: float | Unset = UNSET,
    sced2_curve_price_4_from: float | Unset = UNSET,
    sced2_curve_price_4_to: float | Unset = UNSET,
    sced2_curve_mw5_from: float | Unset = UNSET,
    sced2_curve_mw5_to: float | Unset = UNSET,
    sced2_curve_price_5_from: float | Unset = UNSET,
    sced2_curve_price_5_to: float | Unset = UNSET,
    sced2_curve_mw6_from: float | Unset = UNSET,
    sced2_curve_mw6_to: float | Unset = UNSET,
    sced2_curve_price_6_from: float | Unset = UNSET,
    sced2_curve_price_6_to: float | Unset = UNSET,
    sced2_curve_mw7_from: float | Unset = UNSET,
    sced2_curve_mw7_to: float | Unset = UNSET,
    sced2_curve_price_7_from: float | Unset = UNSET,
    sced2_curve_price_7_to: float | Unset = UNSET,
    sced2_curve_mw8_from: float | Unset = UNSET,
    sced2_curve_mw8_to: float | Unset = UNSET,
    sced2_curve_price_8_from: float | Unset = UNSET,
    sced2_curve_price_8_to: float | Unset = UNSET,
    page: int | Unset = UNSET,
    size: int | Unset = UNSET,
    sort: str | Unset = UNSET,
    dir_: str | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["SCED2CurveMW9From"] = sced2_curve_mw9_from

    params["SCED2CurveMW9To"] = sced2_curve_mw9_to

    params["SCED2CurvePrice9From"] = sced2_curve_price_9_from

    params["SCED2CurvePrice9To"] = sced2_curve_price_9_to

    params["SCED2CurveMW10From"] = sced2_curve_mw10_from

    params["SCED2CurveMW10To"] = sced2_curve_mw10_to

    params["SCED2CurvePrice10From"] = sced2_curve_price_10_from

    params["SCED2CurvePrice10To"] = sced2_curve_price_10_to

    params["SCED2CurveMW11From"] = sced2_curve_mw11_from

    params["SCED2CurveMW11To"] = sced2_curve_mw11_to

    params["SCED2CurvePrice11From"] = sced2_curve_price_11_from

    params["SCED2CurvePrice11To"] = sced2_curve_price_11_to

    params["SCED2CurveMW12From"] = sced2_curve_mw12_from

    params["SCED2CurveMW12To"] = sced2_curve_mw12_to

    params["SCED2CurvePrice12From"] = sced2_curve_price_12_from

    params["SCED2CurvePrice12To"] = sced2_curve_price_12_to

    params["SCED2CurveMW13From"] = sced2_curve_mw13_from

    params["SCED2CurveMW13To"] = sced2_curve_mw13_to

    params["SCED2CurvePrice13From"] = sced2_curve_price_13_from

    params["SCED2CurvePrice13To"] = sced2_curve_price_13_to

    params["SCED2CurveMW14From"] = sced2_curve_mw14_from

    params["SCED2CurveMW14To"] = sced2_curve_mw14_to

    params["SCED2CurvePrice14From"] = sced2_curve_price_14_from

    params["SCED2CurvePrice14To"] = sced2_curve_price_14_to

    params["SCED2CurveMW15From"] = sced2_curve_mw15_from

    params["SCED2CurveMW15To"] = sced2_curve_mw15_to

    params["SCED2CurvePrice15From"] = sced2_curve_price_15_from

    params["SCED2CurvePrice15To"] = sced2_curve_price_15_to

    params["SCED2CurveMW16From"] = sced2_curve_mw16_from

    params["SCED2CurveMW16To"] = sced2_curve_mw16_to

    params["SCED2CurvePrice16From"] = sced2_curve_price_16_from

    params["SCED2CurvePrice16To"] = sced2_curve_price_16_to

    params["SCED2CurveMW17From"] = sced2_curve_mw17_from

    params["SCED2CurveMW17To"] = sced2_curve_mw17_to

    params["SCED2CurvePrice17From"] = sced2_curve_price_17_from

    params["SCED2CurvePrice17To"] = sced2_curve_price_17_to

    params["SCED2CurveMW18From"] = sced2_curve_mw18_from

    params["SCED2CurveMW18To"] = sced2_curve_mw18_to

    params["SCED2CurvePrice18From"] = sced2_curve_price_18_from

    params["SCED2CurvePrice18To"] = sced2_curve_price_18_to

    params["SCED2CurveMW19From"] = sced2_curve_mw19_from

    params["SCED2CurveMW19To"] = sced2_curve_mw19_to

    params["SCED2CurvePrice19From"] = sced2_curve_price_19_from

    params["SCED2CurvePrice19To"] = sced2_curve_price_19_to

    params["SCED2CurveMW20From"] = sced2_curve_mw20_from

    params["SCED2CurveMW20To"] = sced2_curve_mw20_to

    params["SCED2CurvePrice20From"] = sced2_curve_price_20_from

    params["SCED2CurvePrice20To"] = sced2_curve_price_20_to

    params["SCED2CurveMW21From"] = sced2_curve_mw21_from

    params["SCED2CurveMW21To"] = sced2_curve_mw21_to

    params["SCED2CurvePrice21From"] = sced2_curve_price_21_from

    params["SCED2CurvePrice21To"] = sced2_curve_price_21_to

    params["SCED2CurveMW22From"] = sced2_curve_mw22_from

    params["SCED2CurveMW22To"] = sced2_curve_mw22_to

    params["SCED2CurvePrice22From"] = sced2_curve_price_22_from

    params["SCED2CurvePrice22To"] = sced2_curve_price_22_to

    params["SCED2CurveMW23From"] = sced2_curve_mw23_from

    params["SCED2CurveMW23To"] = sced2_curve_mw23_to

    params["SCED2CurvePrice23From"] = sced2_curve_price_23_from

    params["SCED2CurvePrice23To"] = sced2_curve_price_23_to

    params["SCED2CurveMW24From"] = sced2_curve_mw24_from

    params["SCED2CurveMW24To"] = sced2_curve_mw24_to

    params["SCED2CurvePrice24From"] = sced2_curve_price_24_from

    params["SCED2CurvePrice24To"] = sced2_curve_price_24_to

    params["SCED2CurveMW25From"] = sced2_curve_mw25_from

    params["SCED2CurveMW25To"] = sced2_curve_mw25_to

    params["SCED2CurvePrice25From"] = sced2_curve_price_25_from

    params["SCED2CurvePrice25To"] = sced2_curve_price_25_to

    params["SCED2CurveMW26From"] = sced2_curve_mw26_from

    params["SCED2CurveMW26To"] = sced2_curve_mw26_to

    params["SCED2CurvePrice26From"] = sced2_curve_price_26_from

    params["SCED2CurvePrice26To"] = sced2_curve_price_26_to

    params["SCED2CurveMW27From"] = sced2_curve_mw27_from

    params["SCED2CurveMW27To"] = sced2_curve_mw27_to

    params["SCED2CurvePrice27From"] = sced2_curve_price_27_from

    params["SCED2CurvePrice27To"] = sced2_curve_price_27_to

    params["SCED2CurveMW28From"] = sced2_curve_mw28_from

    params["SCED2CurveMW28To"] = sced2_curve_mw28_to

    params["SCED2CurvePrice28From"] = sced2_curve_price_28_from

    params["SCED2CurvePrice28To"] = sced2_curve_price_28_to

    params["SCED2CurveMW29From"] = sced2_curve_mw29_from

    params["SCED2CurveMW29To"] = sced2_curve_mw29_to

    params["SCED2CurvePrice29From"] = sced2_curve_price_29_from

    params["SCED2CurvePrice29To"] = sced2_curve_price_29_to

    params["SCED2CurveMW30From"] = sced2_curve_mw30_from

    params["SCED2CurveMW30To"] = sced2_curve_mw30_to

    params["SCED2CurvePrice30From"] = sced2_curve_price_30_from

    params["SCED2CurvePrice30To"] = sced2_curve_price_30_to

    params["SCED2CurveMW31From"] = sced2_curve_mw31_from

    params["SCED2CurveMW31To"] = sced2_curve_mw31_to

    params["SCED2CurvePrice31From"] = sced2_curve_price_31_from

    params["SCED2CurvePrice31To"] = sced2_curve_price_31_to

    params["SCED2CurveMW32From"] = sced2_curve_mw32_from

    params["SCED2CurveMW32To"] = sced2_curve_mw32_to

    params["SCED2CurvePrice32From"] = sced2_curve_price_32_from

    params["SCED2CurvePrice32To"] = sced2_curve_price_32_to

    params["SCED2CurveMW33From"] = sced2_curve_mw33_from

    params["SCED2CurveMW33To"] = sced2_curve_mw33_to

    params["SCED2CurvePrice33From"] = sced2_curve_price_33_from

    params["SCED2CurvePrice33To"] = sced2_curve_price_33_to

    params["SCED2CurveMW34From"] = sced2_curve_mw34_from

    params["SCED2CurveMW34To"] = sced2_curve_mw34_to

    params["SCED2CurvePrice34From"] = sced2_curve_price_34_from

    params["SCED2CurvePrice34To"] = sced2_curve_price_34_to

    params["SCED2CurveMW35From"] = sced2_curve_mw35_from

    params["SCED2CurveMW35To"] = sced2_curve_mw35_to

    params["SCED2CurvePrice35From"] = sced2_curve_price_35_from

    params["SCED2CurvePrice35To"] = sced2_curve_price_35_to

    params["outputScheduleFrom"] = output_schedule_from

    params["outputScheduleTo"] = output_schedule_to

    params["HSLFrom"] = hsl_from

    params["HSLTo"] = hsl_to

    params["HASLFrom"] = hasl_from

    params["HASLTo"] = hasl_to

    params["HDLFrom"] = hdl_from

    params["HDLTo"] = hdl_to

    params["LSLFrom"] = lsl_from

    params["LSLTo"] = lsl_to

    params["LASLFrom"] = lasl_from

    params["LASLTo"] = lasl_to

    params["LDLFrom"] = ldl_from

    params["LDLTo"] = ldl_to

    params["telemeteredResourceStatus"] = telemetered_resource_status

    params["basePointFrom"] = base_point_from

    params["basePointTo"] = base_point_to

    params["telemeteredNetOutputFrom"] = telemetered_net_output_from

    params["telemeteredNetOutputTo"] = telemetered_net_output_to

    params["ASREGUPFrom"] = asregup_from

    params["ASREGUPTo"] = asregup_to

    params["ASREGDNFrom"] = asregdn_from

    params["ASREGDNTo"] = asregdn_to

    params["ASRRSFrom"] = asrrs_from

    params["ASRRSTo"] = asrrs_to

    params["ASRRSFFRFrom"] = asrrsffr_from

    params["ASRRSFFRTo"] = asrrsffr_to

    params["ASNSRSFrom"] = asnsrs_from

    params["ASNSRSTo"] = asnsrs_to

    params["bidType"] = bid_type

    params["startUpColdOfferFrom"] = start_up_cold_offer_from

    params["startUpColdOfferTo"] = start_up_cold_offer_to

    params["startUpHotOfferFrom"] = start_up_hot_offer_from

    params["startUpHotOfferTo"] = start_up_hot_offer_to

    params["startUpInterOfferFrom"] = start_up_inter_offer_from

    params["startUpInterOfferTo"] = start_up_inter_offer_to

    params["minGenCostFrom"] = min_gen_cost_from

    params["minGenCostTo"] = min_gen_cost_to

    params["submittedTPOMW1From"] = submitted_tpomw1_from

    params["submittedTPOMW1To"] = submitted_tpomw1_to

    params["submittedTPOPrice1From"] = submitted_tpo_price_1_from

    params["submittedTPOPrice1To"] = submitted_tpo_price_1_to

    params["submittedTPOMW2From"] = submitted_tpomw2_from

    params["submittedTPOMW2To"] = submitted_tpomw2_to

    params["submittedTPOPrice2From"] = submitted_tpo_price_2_from

    params["submittedTPOPrice2To"] = submitted_tpo_price_2_to

    params["submittedTPOMW3From"] = submitted_tpomw3_from

    params["submittedTPOMW3To"] = submitted_tpomw3_to

    params["submittedTPOPrice3From"] = submitted_tpo_price_3_from

    params["submittedTPOPrice3To"] = submitted_tpo_price_3_to

    params["submittedTPOMW4From"] = submitted_tpomw4_from

    params["submittedTPOMW4To"] = submitted_tpomw4_to

    params["submittedTPOPrice4From"] = submitted_tpo_price_4_from

    params["submittedTPOPrice4To"] = submitted_tpo_price_4_to

    params["submittedTPOMW5From"] = submitted_tpomw5_from

    params["submittedTPOMW5To"] = submitted_tpomw5_to

    params["submittedTPOPrice5From"] = submitted_tpo_price_5_from

    params["submittedTPOPrice5To"] = submitted_tpo_price_5_to

    params["submittedTPOMW6From"] = submitted_tpomw6_from

    params["submittedTPOMW6To"] = submitted_tpomw6_to

    params["submittedTPOPrice6From"] = submitted_tpo_price_6_from

    params["submittedTPOPrice6To"] = submitted_tpo_price_6_to

    params["submittedTPOMW7From"] = submitted_tpomw7_from

    params["submittedTPOMW7To"] = submitted_tpomw7_to

    params["submittedTPOPrice7From"] = submitted_tpo_price_7_from

    params["submittedTPOPrice7To"] = submitted_tpo_price_7_to

    params["submittedTPOMW8From"] = submitted_tpomw8_from

    params["submittedTPOMW8To"] = submitted_tpomw8_to

    params["submittedTPOPrice8From"] = submitted_tpo_price_8_from

    params["submittedTPOPrice8To"] = submitted_tpo_price_8_to

    params["submittedTPOMW9From"] = submitted_tpomw9_from

    params["submittedTPOMW9To"] = submitted_tpomw9_to

    params["submittedTPOPrice9From"] = submitted_tpo_price_9_from

    params["submittedTPOPrice9To"] = submitted_tpo_price_9_to

    params["submittedTPOMW10From"] = submitted_tpomw10_from

    params["submittedTPOMW10To"] = submitted_tpomw10_to

    params["submittedTPOPrice10From"] = submitted_tpo_price_10_from

    params["submittedTPOPrice10To"] = submitted_tpo_price_10_to

    params["proxyExtension"] = proxy_extension

    params["SCEDTimestampFrom"] = sced_timestamp_from

    params["SCEDTimestampTo"] = sced_timestamp_to

    params["repeatHourFlag"] = repeat_hour_flag

    params["qseName"] = qse_name

    params["dmeName"] = dme_name

    params["resourceName"] = resource_name

    params["resourceType"] = resource_type

    params["SCED1CurveMW1From"] = sced1_curve_mw1_from

    params["SCED1CurveMW1To"] = sced1_curve_mw1_to

    params["SCED1CurvePrice1From"] = sced1_curve_price_1_from

    params["SCED1CurvePrice1To"] = sced1_curve_price_1_to

    params["SCED1CurveMW2From"] = sced1_curve_mw2_from

    params["SCED1CurveMW2To"] = sced1_curve_mw2_to

    params["SCED1CurvePrice2From"] = sced1_curve_price_2_from

    params["SCED1CurvePrice2To"] = sced1_curve_price_2_to

    params["SCED1CurveMW3From"] = sced1_curve_mw3_from

    params["SCED1CurveMW3To"] = sced1_curve_mw3_to

    params["SCED1CurvePrice3From"] = sced1_curve_price_3_from

    params["SCED1CurvePrice3To"] = sced1_curve_price_3_to

    params["SCED1CurveMW4From"] = sced1_curve_mw4_from

    params["SCED1CurveMW4To"] = sced1_curve_mw4_to

    params["SCED1CurvePrice4From"] = sced1_curve_price_4_from

    params["SCED1CurvePrice4To"] = sced1_curve_price_4_to

    params["SCED1CurveMW5From"] = sced1_curve_mw5_from

    params["SCED1CurveMW5To"] = sced1_curve_mw5_to

    params["SCED1CurvePrice5From"] = sced1_curve_price_5_from

    params["SCED1CurvePrice5To"] = sced1_curve_price_5_to

    params["SCED1CurveMW6From"] = sced1_curve_mw6_from

    params["SCED1CurveMW6To"] = sced1_curve_mw6_to

    params["SCED1CurvePrice6From"] = sced1_curve_price_6_from

    params["SCED1CurvePrice6To"] = sced1_curve_price_6_to

    params["SCED1CurveMW7From"] = sced1_curve_mw7_from

    params["SCED1CurveMW7To"] = sced1_curve_mw7_to

    params["SCED1CurvePrice7From"] = sced1_curve_price_7_from

    params["SCED1CurvePrice7To"] = sced1_curve_price_7_to

    params["SCED1CurveMW8From"] = sced1_curve_mw8_from

    params["SCED1CurveMW8To"] = sced1_curve_mw8_to

    params["SCED1CurvePrice8From"] = sced1_curve_price_8_from

    params["SCED1CurvePrice8To"] = sced1_curve_price_8_to

    params["SCED1CurveMW9From"] = sced1_curve_mw9_from

    params["SCED1CurveMW9To"] = sced1_curve_mw9_to

    params["SCED1CurvePrice9From"] = sced1_curve_price_9_from

    params["SCED1CurvePrice9To"] = sced1_curve_price_9_to

    params["SCED1CurveMW10From"] = sced1_curve_mw10_from

    params["SCED1CurveMW10To"] = sced1_curve_mw10_to

    params["SCED1CurvePrice10From"] = sced1_curve_price_10_from

    params["SCED1CurvePrice10To"] = sced1_curve_price_10_to

    params["SCED1CurveMW11From"] = sced1_curve_mw11_from

    params["SCED1CurveMW11To"] = sced1_curve_mw11_to

    params["SCED1CurvePrice11From"] = sced1_curve_price_11_from

    params["SCED1CurvePrice11To"] = sced1_curve_price_11_to

    params["SCED1CurveMW12From"] = sced1_curve_mw12_from

    params["SCED1CurveMW12To"] = sced1_curve_mw12_to

    params["SCED1CurvePrice12From"] = sced1_curve_price_12_from

    params["SCED1CurvePrice12To"] = sced1_curve_price_12_to

    params["SCED1CurveMW13From"] = sced1_curve_mw13_from

    params["SCED1CurveMW13To"] = sced1_curve_mw13_to

    params["SCED1CurvePrice13From"] = sced1_curve_price_13_from

    params["SCED1CurvePrice13To"] = sced1_curve_price_13_to

    params["SCED1CurveMW14From"] = sced1_curve_mw14_from

    params["SCED1CurveMW14To"] = sced1_curve_mw14_to

    params["SCED1CurvePrice14From"] = sced1_curve_price_14_from

    params["SCED1CurvePrice14To"] = sced1_curve_price_14_to

    params["SCED1CurveMW15From"] = sced1_curve_mw15_from

    params["SCED1CurveMW15To"] = sced1_curve_mw15_to

    params["SCED1CurvePrice15From"] = sced1_curve_price_15_from

    params["SCED1CurvePrice15To"] = sced1_curve_price_15_to

    params["SCED1CurveMW16From"] = sced1_curve_mw16_from

    params["SCED1CurveMW16To"] = sced1_curve_mw16_to

    params["SCED1CurvePrice16From"] = sced1_curve_price_16_from

    params["SCED1CurvePrice16To"] = sced1_curve_price_16_to

    params["SCED1CurveMW17From"] = sced1_curve_mw17_from

    params["SCED1CurveMW17To"] = sced1_curve_mw17_to

    params["SCED1CurvePrice17From"] = sced1_curve_price_17_from

    params["SCED1CurvePrice17To"] = sced1_curve_price_17_to

    params["SCED1CurveMW18From"] = sced1_curve_mw18_from

    params["SCED1CurveMW18To"] = sced1_curve_mw18_to

    params["SCED1CurvePrice18From"] = sced1_curve_price_18_from

    params["SCED1CurvePrice18To"] = sced1_curve_price_18_to

    params["SCED1CurveMW19From"] = sced1_curve_mw19_from

    params["SCED1CurveMW19To"] = sced1_curve_mw19_to

    params["SCED1CurvePrice19From"] = sced1_curve_price_19_from

    params["SCED1CurvePrice19To"] = sced1_curve_price_19_to

    params["SCED1CurveMW20From"] = sced1_curve_mw20_from

    params["SCED1CurveMW20To"] = sced1_curve_mw20_to

    params["SCED1CurvePrice20From"] = sced1_curve_price_20_from

    params["SCED1CurvePrice20To"] = sced1_curve_price_20_to

    params["SCED1CurveMW21From"] = sced1_curve_mw21_from

    params["SCED1CurveMW21To"] = sced1_curve_mw21_to

    params["SCED1CurvePrice21From"] = sced1_curve_price_21_from

    params["SCED1CurvePrice21To"] = sced1_curve_price_21_to

    params["SCED1CurveMW22From"] = sced1_curve_mw22_from

    params["SCED1CurveMW22To"] = sced1_curve_mw22_to

    params["SCED1CurvePrice22From"] = sced1_curve_price_22_from

    params["SCED1CurvePrice22To"] = sced1_curve_price_22_to

    params["SCED1CurveMW23From"] = sced1_curve_mw23_from

    params["SCED1CurveMW23To"] = sced1_curve_mw23_to

    params["SCED1CurvePrice23From"] = sced1_curve_price_23_from

    params["SCED1CurvePrice23To"] = sced1_curve_price_23_to

    params["SCED1CurveMW24From"] = sced1_curve_mw24_from

    params["SCED1CurveMW24To"] = sced1_curve_mw24_to

    params["SCED1CurvePrice24From"] = sced1_curve_price_24_from

    params["SCED1CurvePrice24To"] = sced1_curve_price_24_to

    params["SCED1CurveMW25From"] = sced1_curve_mw25_from

    params["SCED1CurveMW25To"] = sced1_curve_mw25_to

    params["SCED1CurvePrice25From"] = sced1_curve_price_25_from

    params["SCED1CurvePrice25To"] = sced1_curve_price_25_to

    params["SCED1CurveMW26From"] = sced1_curve_mw26_from

    params["SCED1CurveMW26To"] = sced1_curve_mw26_to

    params["SCED1CurvePrice26From"] = sced1_curve_price_26_from

    params["SCED1CurvePrice26To"] = sced1_curve_price_26_to

    params["SCED1CurveMW27From"] = sced1_curve_mw27_from

    params["SCED1CurveMW27To"] = sced1_curve_mw27_to

    params["SCED1CurvePrice27From"] = sced1_curve_price_27_from

    params["SCED1CurvePrice27To"] = sced1_curve_price_27_to

    params["SCED1CurveMW28From"] = sced1_curve_mw28_from

    params["SCED1CurveMW28To"] = sced1_curve_mw28_to

    params["SCED1CurvePrice28From"] = sced1_curve_price_28_from

    params["SCED1CurvePrice28To"] = sced1_curve_price_28_to

    params["SCED1CurveMW29From"] = sced1_curve_mw29_from

    params["SCED1CurveMW29To"] = sced1_curve_mw29_to

    params["SCED1CurvePrice29From"] = sced1_curve_price_29_from

    params["SCED1CurvePrice29To"] = sced1_curve_price_29_to

    params["SCED1CurveMW30From"] = sced1_curve_mw30_from

    params["SCED1CurveMW30To"] = sced1_curve_mw30_to

    params["SCED1CurvePrice30From"] = sced1_curve_price_30_from

    params["SCED1CurvePrice30To"] = sced1_curve_price_30_to

    params["SCED1CurveMW31From"] = sced1_curve_mw31_from

    params["SCED1CurveMW31To"] = sced1_curve_mw31_to

    params["SCED1CurvePrice31From"] = sced1_curve_price_31_from

    params["SCED1CurvePrice31To"] = sced1_curve_price_31_to

    params["SCED1CurveMW32From"] = sced1_curve_mw32_from

    params["SCED1CurveMW32To"] = sced1_curve_mw32_to

    params["SCED1CurvePrice32From"] = sced1_curve_price_32_from

    params["SCED1CurvePrice32To"] = sced1_curve_price_32_to

    params["SCED1CurveMW33From"] = sced1_curve_mw33_from

    params["SCED1CurveMW33To"] = sced1_curve_mw33_to

    params["SCED1CurvePrice33From"] = sced1_curve_price_33_from

    params["SCED1CurvePrice33To"] = sced1_curve_price_33_to

    params["SCED1CurveMW34From"] = sced1_curve_mw34_from

    params["SCED1CurveMW34To"] = sced1_curve_mw34_to

    params["SCED1CurvePrice34From"] = sced1_curve_price_34_from

    params["SCED1CurvePrice34To"] = sced1_curve_price_34_to

    params["SCED1CurveMW35From"] = sced1_curve_mw35_from

    params["SCED1CurveMW35To"] = sced1_curve_mw35_to

    params["SCED1CurvePrice35From"] = sced1_curve_price_35_from

    params["SCED1CurvePrice35To"] = sced1_curve_price_35_to

    params["SCED2CurveMW1From"] = sced2_curve_mw1_from

    params["SCED2CurveMW1To"] = sced2_curve_mw1_to

    params["SCED2CurvePrice1From"] = sced2_curve_price_1_from

    params["SCED2CurvePrice1To"] = sced2_curve_price_1_to

    params["SCED2CurveMW2From"] = sced2_curve_mw2_from

    params["SCED2CurveMW2To"] = sced2_curve_mw2_to

    params["SCED2CurvePrice2From"] = sced2_curve_price_2_from

    params["SCED2CurvePrice2To"] = sced2_curve_price_2_to

    params["SCED2CurveMW3From"] = sced2_curve_mw3_from

    params["SCED2CurveMW3To"] = sced2_curve_mw3_to

    params["SCED2CurvePrice3From"] = sced2_curve_price_3_from

    params["SCED2CurvePrice3To"] = sced2_curve_price_3_to

    params["SCED2CurveMW4From"] = sced2_curve_mw4_from

    params["SCED2CurveMW4To"] = sced2_curve_mw4_to

    params["SCED2CurvePrice4From"] = sced2_curve_price_4_from

    params["SCED2CurvePrice4To"] = sced2_curve_price_4_to

    params["SCED2CurveMW5From"] = sced2_curve_mw5_from

    params["SCED2CurveMW5To"] = sced2_curve_mw5_to

    params["SCED2CurvePrice5From"] = sced2_curve_price_5_from

    params["SCED2CurvePrice5To"] = sced2_curve_price_5_to

    params["SCED2CurveMW6From"] = sced2_curve_mw6_from

    params["SCED2CurveMW6To"] = sced2_curve_mw6_to

    params["SCED2CurvePrice6From"] = sced2_curve_price_6_from

    params["SCED2CurvePrice6To"] = sced2_curve_price_6_to

    params["SCED2CurveMW7From"] = sced2_curve_mw7_from

    params["SCED2CurveMW7To"] = sced2_curve_mw7_to

    params["SCED2CurvePrice7From"] = sced2_curve_price_7_from

    params["SCED2CurvePrice7To"] = sced2_curve_price_7_to

    params["SCED2CurveMW8From"] = sced2_curve_mw8_from

    params["SCED2CurveMW8To"] = sced2_curve_mw8_to

    params["SCED2CurvePrice8From"] = sced2_curve_price_8_from

    params["SCED2CurvePrice8To"] = sced2_curve_price_8_to

    params["page"] = page

    params["size"] = size

    params["sort"] = sort

    params["dir"] = dir_

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/np3-965-er/60_sced_gen_res_data",
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
    sced2_curve_mw9_from: float | Unset = UNSET,
    sced2_curve_mw9_to: float | Unset = UNSET,
    sced2_curve_price_9_from: float | Unset = UNSET,
    sced2_curve_price_9_to: float | Unset = UNSET,
    sced2_curve_mw10_from: float | Unset = UNSET,
    sced2_curve_mw10_to: float | Unset = UNSET,
    sced2_curve_price_10_from: float | Unset = UNSET,
    sced2_curve_price_10_to: float | Unset = UNSET,
    sced2_curve_mw11_from: float | Unset = UNSET,
    sced2_curve_mw11_to: float | Unset = UNSET,
    sced2_curve_price_11_from: float | Unset = UNSET,
    sced2_curve_price_11_to: float | Unset = UNSET,
    sced2_curve_mw12_from: float | Unset = UNSET,
    sced2_curve_mw12_to: float | Unset = UNSET,
    sced2_curve_price_12_from: float | Unset = UNSET,
    sced2_curve_price_12_to: float | Unset = UNSET,
    sced2_curve_mw13_from: float | Unset = UNSET,
    sced2_curve_mw13_to: float | Unset = UNSET,
    sced2_curve_price_13_from: float | Unset = UNSET,
    sced2_curve_price_13_to: float | Unset = UNSET,
    sced2_curve_mw14_from: float | Unset = UNSET,
    sced2_curve_mw14_to: float | Unset = UNSET,
    sced2_curve_price_14_from: float | Unset = UNSET,
    sced2_curve_price_14_to: float | Unset = UNSET,
    sced2_curve_mw15_from: float | Unset = UNSET,
    sced2_curve_mw15_to: float | Unset = UNSET,
    sced2_curve_price_15_from: float | Unset = UNSET,
    sced2_curve_price_15_to: float | Unset = UNSET,
    sced2_curve_mw16_from: float | Unset = UNSET,
    sced2_curve_mw16_to: float | Unset = UNSET,
    sced2_curve_price_16_from: float | Unset = UNSET,
    sced2_curve_price_16_to: float | Unset = UNSET,
    sced2_curve_mw17_from: float | Unset = UNSET,
    sced2_curve_mw17_to: float | Unset = UNSET,
    sced2_curve_price_17_from: float | Unset = UNSET,
    sced2_curve_price_17_to: float | Unset = UNSET,
    sced2_curve_mw18_from: float | Unset = UNSET,
    sced2_curve_mw18_to: float | Unset = UNSET,
    sced2_curve_price_18_from: float | Unset = UNSET,
    sced2_curve_price_18_to: float | Unset = UNSET,
    sced2_curve_mw19_from: float | Unset = UNSET,
    sced2_curve_mw19_to: float | Unset = UNSET,
    sced2_curve_price_19_from: float | Unset = UNSET,
    sced2_curve_price_19_to: float | Unset = UNSET,
    sced2_curve_mw20_from: float | Unset = UNSET,
    sced2_curve_mw20_to: float | Unset = UNSET,
    sced2_curve_price_20_from: float | Unset = UNSET,
    sced2_curve_price_20_to: float | Unset = UNSET,
    sced2_curve_mw21_from: float | Unset = UNSET,
    sced2_curve_mw21_to: float | Unset = UNSET,
    sced2_curve_price_21_from: float | Unset = UNSET,
    sced2_curve_price_21_to: float | Unset = UNSET,
    sced2_curve_mw22_from: float | Unset = UNSET,
    sced2_curve_mw22_to: float | Unset = UNSET,
    sced2_curve_price_22_from: float | Unset = UNSET,
    sced2_curve_price_22_to: float | Unset = UNSET,
    sced2_curve_mw23_from: float | Unset = UNSET,
    sced2_curve_mw23_to: float | Unset = UNSET,
    sced2_curve_price_23_from: float | Unset = UNSET,
    sced2_curve_price_23_to: float | Unset = UNSET,
    sced2_curve_mw24_from: float | Unset = UNSET,
    sced2_curve_mw24_to: float | Unset = UNSET,
    sced2_curve_price_24_from: float | Unset = UNSET,
    sced2_curve_price_24_to: float | Unset = UNSET,
    sced2_curve_mw25_from: float | Unset = UNSET,
    sced2_curve_mw25_to: float | Unset = UNSET,
    sced2_curve_price_25_from: float | Unset = UNSET,
    sced2_curve_price_25_to: float | Unset = UNSET,
    sced2_curve_mw26_from: float | Unset = UNSET,
    sced2_curve_mw26_to: float | Unset = UNSET,
    sced2_curve_price_26_from: float | Unset = UNSET,
    sced2_curve_price_26_to: float | Unset = UNSET,
    sced2_curve_mw27_from: float | Unset = UNSET,
    sced2_curve_mw27_to: float | Unset = UNSET,
    sced2_curve_price_27_from: float | Unset = UNSET,
    sced2_curve_price_27_to: float | Unset = UNSET,
    sced2_curve_mw28_from: float | Unset = UNSET,
    sced2_curve_mw28_to: float | Unset = UNSET,
    sced2_curve_price_28_from: float | Unset = UNSET,
    sced2_curve_price_28_to: float | Unset = UNSET,
    sced2_curve_mw29_from: float | Unset = UNSET,
    sced2_curve_mw29_to: float | Unset = UNSET,
    sced2_curve_price_29_from: float | Unset = UNSET,
    sced2_curve_price_29_to: float | Unset = UNSET,
    sced2_curve_mw30_from: float | Unset = UNSET,
    sced2_curve_mw30_to: float | Unset = UNSET,
    sced2_curve_price_30_from: float | Unset = UNSET,
    sced2_curve_price_30_to: float | Unset = UNSET,
    sced2_curve_mw31_from: float | Unset = UNSET,
    sced2_curve_mw31_to: float | Unset = UNSET,
    sced2_curve_price_31_from: float | Unset = UNSET,
    sced2_curve_price_31_to: float | Unset = UNSET,
    sced2_curve_mw32_from: float | Unset = UNSET,
    sced2_curve_mw32_to: float | Unset = UNSET,
    sced2_curve_price_32_from: float | Unset = UNSET,
    sced2_curve_price_32_to: float | Unset = UNSET,
    sced2_curve_mw33_from: float | Unset = UNSET,
    sced2_curve_mw33_to: float | Unset = UNSET,
    sced2_curve_price_33_from: float | Unset = UNSET,
    sced2_curve_price_33_to: float | Unset = UNSET,
    sced2_curve_mw34_from: float | Unset = UNSET,
    sced2_curve_mw34_to: float | Unset = UNSET,
    sced2_curve_price_34_from: float | Unset = UNSET,
    sced2_curve_price_34_to: float | Unset = UNSET,
    sced2_curve_mw35_from: float | Unset = UNSET,
    sced2_curve_mw35_to: float | Unset = UNSET,
    sced2_curve_price_35_from: float | Unset = UNSET,
    sced2_curve_price_35_to: float | Unset = UNSET,
    output_schedule_from: float | Unset = UNSET,
    output_schedule_to: float | Unset = UNSET,
    hsl_from: float | Unset = UNSET,
    hsl_to: float | Unset = UNSET,
    hasl_from: float | Unset = UNSET,
    hasl_to: float | Unset = UNSET,
    hdl_from: float | Unset = UNSET,
    hdl_to: float | Unset = UNSET,
    lsl_from: float | Unset = UNSET,
    lsl_to: float | Unset = UNSET,
    lasl_from: float | Unset = UNSET,
    lasl_to: float | Unset = UNSET,
    ldl_from: float | Unset = UNSET,
    ldl_to: float | Unset = UNSET,
    telemetered_resource_status: str | Unset = UNSET,
    base_point_from: float | Unset = UNSET,
    base_point_to: float | Unset = UNSET,
    telemetered_net_output_from: float | Unset = UNSET,
    telemetered_net_output_to: float | Unset = UNSET,
    asregup_from: float | Unset = UNSET,
    asregup_to: float | Unset = UNSET,
    asregdn_from: float | Unset = UNSET,
    asregdn_to: float | Unset = UNSET,
    asrrs_from: float | Unset = UNSET,
    asrrs_to: float | Unset = UNSET,
    asrrsffr_from: float | Unset = UNSET,
    asrrsffr_to: float | Unset = UNSET,
    asnsrs_from: float | Unset = UNSET,
    asnsrs_to: float | Unset = UNSET,
    bid_type: str | Unset = UNSET,
    start_up_cold_offer_from: float | Unset = UNSET,
    start_up_cold_offer_to: float | Unset = UNSET,
    start_up_hot_offer_from: float | Unset = UNSET,
    start_up_hot_offer_to: float | Unset = UNSET,
    start_up_inter_offer_from: float | Unset = UNSET,
    start_up_inter_offer_to: float | Unset = UNSET,
    min_gen_cost_from: float | Unset = UNSET,
    min_gen_cost_to: float | Unset = UNSET,
    submitted_tpomw1_from: float | Unset = UNSET,
    submitted_tpomw1_to: float | Unset = UNSET,
    submitted_tpo_price_1_from: float | Unset = UNSET,
    submitted_tpo_price_1_to: float | Unset = UNSET,
    submitted_tpomw2_from: float | Unset = UNSET,
    submitted_tpomw2_to: float | Unset = UNSET,
    submitted_tpo_price_2_from: float | Unset = UNSET,
    submitted_tpo_price_2_to: float | Unset = UNSET,
    submitted_tpomw3_from: float | Unset = UNSET,
    submitted_tpomw3_to: float | Unset = UNSET,
    submitted_tpo_price_3_from: float | Unset = UNSET,
    submitted_tpo_price_3_to: float | Unset = UNSET,
    submitted_tpomw4_from: float | Unset = UNSET,
    submitted_tpomw4_to: float | Unset = UNSET,
    submitted_tpo_price_4_from: float | Unset = UNSET,
    submitted_tpo_price_4_to: float | Unset = UNSET,
    submitted_tpomw5_from: float | Unset = UNSET,
    submitted_tpomw5_to: float | Unset = UNSET,
    submitted_tpo_price_5_from: float | Unset = UNSET,
    submitted_tpo_price_5_to: float | Unset = UNSET,
    submitted_tpomw6_from: float | Unset = UNSET,
    submitted_tpomw6_to: float | Unset = UNSET,
    submitted_tpo_price_6_from: float | Unset = UNSET,
    submitted_tpo_price_6_to: float | Unset = UNSET,
    submitted_tpomw7_from: float | Unset = UNSET,
    submitted_tpomw7_to: float | Unset = UNSET,
    submitted_tpo_price_7_from: float | Unset = UNSET,
    submitted_tpo_price_7_to: float | Unset = UNSET,
    submitted_tpomw8_from: float | Unset = UNSET,
    submitted_tpomw8_to: float | Unset = UNSET,
    submitted_tpo_price_8_from: float | Unset = UNSET,
    submitted_tpo_price_8_to: float | Unset = UNSET,
    submitted_tpomw9_from: float | Unset = UNSET,
    submitted_tpomw9_to: float | Unset = UNSET,
    submitted_tpo_price_9_from: float | Unset = UNSET,
    submitted_tpo_price_9_to: float | Unset = UNSET,
    submitted_tpomw10_from: float | Unset = UNSET,
    submitted_tpomw10_to: float | Unset = UNSET,
    submitted_tpo_price_10_from: float | Unset = UNSET,
    submitted_tpo_price_10_to: float | Unset = UNSET,
    proxy_extension: str | Unset = UNSET,
    sced_timestamp_from: str | Unset = UNSET,
    sced_timestamp_to: str | Unset = UNSET,
    repeat_hour_flag: bool | Unset = UNSET,
    qse_name: str | Unset = UNSET,
    dme_name: str | Unset = UNSET,
    resource_name: str | Unset = UNSET,
    resource_type: str | Unset = UNSET,
    sced1_curve_mw1_from: float | Unset = UNSET,
    sced1_curve_mw1_to: float | Unset = UNSET,
    sced1_curve_price_1_from: float | Unset = UNSET,
    sced1_curve_price_1_to: float | Unset = UNSET,
    sced1_curve_mw2_from: float | Unset = UNSET,
    sced1_curve_mw2_to: float | Unset = UNSET,
    sced1_curve_price_2_from: float | Unset = UNSET,
    sced1_curve_price_2_to: float | Unset = UNSET,
    sced1_curve_mw3_from: float | Unset = UNSET,
    sced1_curve_mw3_to: float | Unset = UNSET,
    sced1_curve_price_3_from: float | Unset = UNSET,
    sced1_curve_price_3_to: float | Unset = UNSET,
    sced1_curve_mw4_from: float | Unset = UNSET,
    sced1_curve_mw4_to: float | Unset = UNSET,
    sced1_curve_price_4_from: float | Unset = UNSET,
    sced1_curve_price_4_to: float | Unset = UNSET,
    sced1_curve_mw5_from: float | Unset = UNSET,
    sced1_curve_mw5_to: float | Unset = UNSET,
    sced1_curve_price_5_from: float | Unset = UNSET,
    sced1_curve_price_5_to: float | Unset = UNSET,
    sced1_curve_mw6_from: float | Unset = UNSET,
    sced1_curve_mw6_to: float | Unset = UNSET,
    sced1_curve_price_6_from: float | Unset = UNSET,
    sced1_curve_price_6_to: float | Unset = UNSET,
    sced1_curve_mw7_from: float | Unset = UNSET,
    sced1_curve_mw7_to: float | Unset = UNSET,
    sced1_curve_price_7_from: float | Unset = UNSET,
    sced1_curve_price_7_to: float | Unset = UNSET,
    sced1_curve_mw8_from: float | Unset = UNSET,
    sced1_curve_mw8_to: float | Unset = UNSET,
    sced1_curve_price_8_from: float | Unset = UNSET,
    sced1_curve_price_8_to: float | Unset = UNSET,
    sced1_curve_mw9_from: float | Unset = UNSET,
    sced1_curve_mw9_to: float | Unset = UNSET,
    sced1_curve_price_9_from: float | Unset = UNSET,
    sced1_curve_price_9_to: float | Unset = UNSET,
    sced1_curve_mw10_from: float | Unset = UNSET,
    sced1_curve_mw10_to: float | Unset = UNSET,
    sced1_curve_price_10_from: float | Unset = UNSET,
    sced1_curve_price_10_to: float | Unset = UNSET,
    sced1_curve_mw11_from: float | Unset = UNSET,
    sced1_curve_mw11_to: float | Unset = UNSET,
    sced1_curve_price_11_from: float | Unset = UNSET,
    sced1_curve_price_11_to: float | Unset = UNSET,
    sced1_curve_mw12_from: float | Unset = UNSET,
    sced1_curve_mw12_to: float | Unset = UNSET,
    sced1_curve_price_12_from: float | Unset = UNSET,
    sced1_curve_price_12_to: float | Unset = UNSET,
    sced1_curve_mw13_from: float | Unset = UNSET,
    sced1_curve_mw13_to: float | Unset = UNSET,
    sced1_curve_price_13_from: float | Unset = UNSET,
    sced1_curve_price_13_to: float | Unset = UNSET,
    sced1_curve_mw14_from: float | Unset = UNSET,
    sced1_curve_mw14_to: float | Unset = UNSET,
    sced1_curve_price_14_from: float | Unset = UNSET,
    sced1_curve_price_14_to: float | Unset = UNSET,
    sced1_curve_mw15_from: float | Unset = UNSET,
    sced1_curve_mw15_to: float | Unset = UNSET,
    sced1_curve_price_15_from: float | Unset = UNSET,
    sced1_curve_price_15_to: float | Unset = UNSET,
    sced1_curve_mw16_from: float | Unset = UNSET,
    sced1_curve_mw16_to: float | Unset = UNSET,
    sced1_curve_price_16_from: float | Unset = UNSET,
    sced1_curve_price_16_to: float | Unset = UNSET,
    sced1_curve_mw17_from: float | Unset = UNSET,
    sced1_curve_mw17_to: float | Unset = UNSET,
    sced1_curve_price_17_from: float | Unset = UNSET,
    sced1_curve_price_17_to: float | Unset = UNSET,
    sced1_curve_mw18_from: float | Unset = UNSET,
    sced1_curve_mw18_to: float | Unset = UNSET,
    sced1_curve_price_18_from: float | Unset = UNSET,
    sced1_curve_price_18_to: float | Unset = UNSET,
    sced1_curve_mw19_from: float | Unset = UNSET,
    sced1_curve_mw19_to: float | Unset = UNSET,
    sced1_curve_price_19_from: float | Unset = UNSET,
    sced1_curve_price_19_to: float | Unset = UNSET,
    sced1_curve_mw20_from: float | Unset = UNSET,
    sced1_curve_mw20_to: float | Unset = UNSET,
    sced1_curve_price_20_from: float | Unset = UNSET,
    sced1_curve_price_20_to: float | Unset = UNSET,
    sced1_curve_mw21_from: float | Unset = UNSET,
    sced1_curve_mw21_to: float | Unset = UNSET,
    sced1_curve_price_21_from: float | Unset = UNSET,
    sced1_curve_price_21_to: float | Unset = UNSET,
    sced1_curve_mw22_from: float | Unset = UNSET,
    sced1_curve_mw22_to: float | Unset = UNSET,
    sced1_curve_price_22_from: float | Unset = UNSET,
    sced1_curve_price_22_to: float | Unset = UNSET,
    sced1_curve_mw23_from: float | Unset = UNSET,
    sced1_curve_mw23_to: float | Unset = UNSET,
    sced1_curve_price_23_from: float | Unset = UNSET,
    sced1_curve_price_23_to: float | Unset = UNSET,
    sced1_curve_mw24_from: float | Unset = UNSET,
    sced1_curve_mw24_to: float | Unset = UNSET,
    sced1_curve_price_24_from: float | Unset = UNSET,
    sced1_curve_price_24_to: float | Unset = UNSET,
    sced1_curve_mw25_from: float | Unset = UNSET,
    sced1_curve_mw25_to: float | Unset = UNSET,
    sced1_curve_price_25_from: float | Unset = UNSET,
    sced1_curve_price_25_to: float | Unset = UNSET,
    sced1_curve_mw26_from: float | Unset = UNSET,
    sced1_curve_mw26_to: float | Unset = UNSET,
    sced1_curve_price_26_from: float | Unset = UNSET,
    sced1_curve_price_26_to: float | Unset = UNSET,
    sced1_curve_mw27_from: float | Unset = UNSET,
    sced1_curve_mw27_to: float | Unset = UNSET,
    sced1_curve_price_27_from: float | Unset = UNSET,
    sced1_curve_price_27_to: float | Unset = UNSET,
    sced1_curve_mw28_from: float | Unset = UNSET,
    sced1_curve_mw28_to: float | Unset = UNSET,
    sced1_curve_price_28_from: float | Unset = UNSET,
    sced1_curve_price_28_to: float | Unset = UNSET,
    sced1_curve_mw29_from: float | Unset = UNSET,
    sced1_curve_mw29_to: float | Unset = UNSET,
    sced1_curve_price_29_from: float | Unset = UNSET,
    sced1_curve_price_29_to: float | Unset = UNSET,
    sced1_curve_mw30_from: float | Unset = UNSET,
    sced1_curve_mw30_to: float | Unset = UNSET,
    sced1_curve_price_30_from: float | Unset = UNSET,
    sced1_curve_price_30_to: float | Unset = UNSET,
    sced1_curve_mw31_from: float | Unset = UNSET,
    sced1_curve_mw31_to: float | Unset = UNSET,
    sced1_curve_price_31_from: float | Unset = UNSET,
    sced1_curve_price_31_to: float | Unset = UNSET,
    sced1_curve_mw32_from: float | Unset = UNSET,
    sced1_curve_mw32_to: float | Unset = UNSET,
    sced1_curve_price_32_from: float | Unset = UNSET,
    sced1_curve_price_32_to: float | Unset = UNSET,
    sced1_curve_mw33_from: float | Unset = UNSET,
    sced1_curve_mw33_to: float | Unset = UNSET,
    sced1_curve_price_33_from: float | Unset = UNSET,
    sced1_curve_price_33_to: float | Unset = UNSET,
    sced1_curve_mw34_from: float | Unset = UNSET,
    sced1_curve_mw34_to: float | Unset = UNSET,
    sced1_curve_price_34_from: float | Unset = UNSET,
    sced1_curve_price_34_to: float | Unset = UNSET,
    sced1_curve_mw35_from: float | Unset = UNSET,
    sced1_curve_mw35_to: float | Unset = UNSET,
    sced1_curve_price_35_from: float | Unset = UNSET,
    sced1_curve_price_35_to: float | Unset = UNSET,
    sced2_curve_mw1_from: float | Unset = UNSET,
    sced2_curve_mw1_to: float | Unset = UNSET,
    sced2_curve_price_1_from: float | Unset = UNSET,
    sced2_curve_price_1_to: float | Unset = UNSET,
    sced2_curve_mw2_from: float | Unset = UNSET,
    sced2_curve_mw2_to: float | Unset = UNSET,
    sced2_curve_price_2_from: float | Unset = UNSET,
    sced2_curve_price_2_to: float | Unset = UNSET,
    sced2_curve_mw3_from: float | Unset = UNSET,
    sced2_curve_mw3_to: float | Unset = UNSET,
    sced2_curve_price_3_from: float | Unset = UNSET,
    sced2_curve_price_3_to: float | Unset = UNSET,
    sced2_curve_mw4_from: float | Unset = UNSET,
    sced2_curve_mw4_to: float | Unset = UNSET,
    sced2_curve_price_4_from: float | Unset = UNSET,
    sced2_curve_price_4_to: float | Unset = UNSET,
    sced2_curve_mw5_from: float | Unset = UNSET,
    sced2_curve_mw5_to: float | Unset = UNSET,
    sced2_curve_price_5_from: float | Unset = UNSET,
    sced2_curve_price_5_to: float | Unset = UNSET,
    sced2_curve_mw6_from: float | Unset = UNSET,
    sced2_curve_mw6_to: float | Unset = UNSET,
    sced2_curve_price_6_from: float | Unset = UNSET,
    sced2_curve_price_6_to: float | Unset = UNSET,
    sced2_curve_mw7_from: float | Unset = UNSET,
    sced2_curve_mw7_to: float | Unset = UNSET,
    sced2_curve_price_7_from: float | Unset = UNSET,
    sced2_curve_price_7_to: float | Unset = UNSET,
    sced2_curve_mw8_from: float | Unset = UNSET,
    sced2_curve_mw8_to: float | Unset = UNSET,
    sced2_curve_price_8_from: float | Unset = UNSET,
    sced2_curve_price_8_to: float | Unset = UNSET,
    page: int | Unset = UNSET,
    size: int | Unset = UNSET,
    sort: str | Unset = UNSET,
    dir_: str | Unset = UNSET,
) -> Response[Exception_ | Report]:
    """60 Day SCED Gen Resource Data

     60 Day SCED Gen Resource Data

    Args:
        sced2_curve_mw9_from (float | Unset):
        sced2_curve_mw9_to (float | Unset):
        sced2_curve_price_9_from (float | Unset):
        sced2_curve_price_9_to (float | Unset):
        sced2_curve_mw10_from (float | Unset):
        sced2_curve_mw10_to (float | Unset):
        sced2_curve_price_10_from (float | Unset):
        sced2_curve_price_10_to (float | Unset):
        sced2_curve_mw11_from (float | Unset):
        sced2_curve_mw11_to (float | Unset):
        sced2_curve_price_11_from (float | Unset):
        sced2_curve_price_11_to (float | Unset):
        sced2_curve_mw12_from (float | Unset):
        sced2_curve_mw12_to (float | Unset):
        sced2_curve_price_12_from (float | Unset):
        sced2_curve_price_12_to (float | Unset):
        sced2_curve_mw13_from (float | Unset):
        sced2_curve_mw13_to (float | Unset):
        sced2_curve_price_13_from (float | Unset):
        sced2_curve_price_13_to (float | Unset):
        sced2_curve_mw14_from (float | Unset):
        sced2_curve_mw14_to (float | Unset):
        sced2_curve_price_14_from (float | Unset):
        sced2_curve_price_14_to (float | Unset):
        sced2_curve_mw15_from (float | Unset):
        sced2_curve_mw15_to (float | Unset):
        sced2_curve_price_15_from (float | Unset):
        sced2_curve_price_15_to (float | Unset):
        sced2_curve_mw16_from (float | Unset):
        sced2_curve_mw16_to (float | Unset):
        sced2_curve_price_16_from (float | Unset):
        sced2_curve_price_16_to (float | Unset):
        sced2_curve_mw17_from (float | Unset):
        sced2_curve_mw17_to (float | Unset):
        sced2_curve_price_17_from (float | Unset):
        sced2_curve_price_17_to (float | Unset):
        sced2_curve_mw18_from (float | Unset):
        sced2_curve_mw18_to (float | Unset):
        sced2_curve_price_18_from (float | Unset):
        sced2_curve_price_18_to (float | Unset):
        sced2_curve_mw19_from (float | Unset):
        sced2_curve_mw19_to (float | Unset):
        sced2_curve_price_19_from (float | Unset):
        sced2_curve_price_19_to (float | Unset):
        sced2_curve_mw20_from (float | Unset):
        sced2_curve_mw20_to (float | Unset):
        sced2_curve_price_20_from (float | Unset):
        sced2_curve_price_20_to (float | Unset):
        sced2_curve_mw21_from (float | Unset):
        sced2_curve_mw21_to (float | Unset):
        sced2_curve_price_21_from (float | Unset):
        sced2_curve_price_21_to (float | Unset):
        sced2_curve_mw22_from (float | Unset):
        sced2_curve_mw22_to (float | Unset):
        sced2_curve_price_22_from (float | Unset):
        sced2_curve_price_22_to (float | Unset):
        sced2_curve_mw23_from (float | Unset):
        sced2_curve_mw23_to (float | Unset):
        sced2_curve_price_23_from (float | Unset):
        sced2_curve_price_23_to (float | Unset):
        sced2_curve_mw24_from (float | Unset):
        sced2_curve_mw24_to (float | Unset):
        sced2_curve_price_24_from (float | Unset):
        sced2_curve_price_24_to (float | Unset):
        sced2_curve_mw25_from (float | Unset):
        sced2_curve_mw25_to (float | Unset):
        sced2_curve_price_25_from (float | Unset):
        sced2_curve_price_25_to (float | Unset):
        sced2_curve_mw26_from (float | Unset):
        sced2_curve_mw26_to (float | Unset):
        sced2_curve_price_26_from (float | Unset):
        sced2_curve_price_26_to (float | Unset):
        sced2_curve_mw27_from (float | Unset):
        sced2_curve_mw27_to (float | Unset):
        sced2_curve_price_27_from (float | Unset):
        sced2_curve_price_27_to (float | Unset):
        sced2_curve_mw28_from (float | Unset):
        sced2_curve_mw28_to (float | Unset):
        sced2_curve_price_28_from (float | Unset):
        sced2_curve_price_28_to (float | Unset):
        sced2_curve_mw29_from (float | Unset):
        sced2_curve_mw29_to (float | Unset):
        sced2_curve_price_29_from (float | Unset):
        sced2_curve_price_29_to (float | Unset):
        sced2_curve_mw30_from (float | Unset):
        sced2_curve_mw30_to (float | Unset):
        sced2_curve_price_30_from (float | Unset):
        sced2_curve_price_30_to (float | Unset):
        sced2_curve_mw31_from (float | Unset):
        sced2_curve_mw31_to (float | Unset):
        sced2_curve_price_31_from (float | Unset):
        sced2_curve_price_31_to (float | Unset):
        sced2_curve_mw32_from (float | Unset):
        sced2_curve_mw32_to (float | Unset):
        sced2_curve_price_32_from (float | Unset):
        sced2_curve_price_32_to (float | Unset):
        sced2_curve_mw33_from (float | Unset):
        sced2_curve_mw33_to (float | Unset):
        sced2_curve_price_33_from (float | Unset):
        sced2_curve_price_33_to (float | Unset):
        sced2_curve_mw34_from (float | Unset):
        sced2_curve_mw34_to (float | Unset):
        sced2_curve_price_34_from (float | Unset):
        sced2_curve_price_34_to (float | Unset):
        sced2_curve_mw35_from (float | Unset):
        sced2_curve_mw35_to (float | Unset):
        sced2_curve_price_35_from (float | Unset):
        sced2_curve_price_35_to (float | Unset):
        output_schedule_from (float | Unset):
        output_schedule_to (float | Unset):
        hsl_from (float | Unset):
        hsl_to (float | Unset):
        hasl_from (float | Unset):
        hasl_to (float | Unset):
        hdl_from (float | Unset):
        hdl_to (float | Unset):
        lsl_from (float | Unset):
        lsl_to (float | Unset):
        lasl_from (float | Unset):
        lasl_to (float | Unset):
        ldl_from (float | Unset):
        ldl_to (float | Unset):
        telemetered_resource_status (str | Unset):
        base_point_from (float | Unset):
        base_point_to (float | Unset):
        telemetered_net_output_from (float | Unset):
        telemetered_net_output_to (float | Unset):
        asregup_from (float | Unset):
        asregup_to (float | Unset):
        asregdn_from (float | Unset):
        asregdn_to (float | Unset):
        asrrs_from (float | Unset):
        asrrs_to (float | Unset):
        asrrsffr_from (float | Unset):
        asrrsffr_to (float | Unset):
        asnsrs_from (float | Unset):
        asnsrs_to (float | Unset):
        bid_type (str | Unset):
        start_up_cold_offer_from (float | Unset):
        start_up_cold_offer_to (float | Unset):
        start_up_hot_offer_from (float | Unset):
        start_up_hot_offer_to (float | Unset):
        start_up_inter_offer_from (float | Unset):
        start_up_inter_offer_to (float | Unset):
        min_gen_cost_from (float | Unset):
        min_gen_cost_to (float | Unset):
        submitted_tpomw1_from (float | Unset):
        submitted_tpomw1_to (float | Unset):
        submitted_tpo_price_1_from (float | Unset):
        submitted_tpo_price_1_to (float | Unset):
        submitted_tpomw2_from (float | Unset):
        submitted_tpomw2_to (float | Unset):
        submitted_tpo_price_2_from (float | Unset):
        submitted_tpo_price_2_to (float | Unset):
        submitted_tpomw3_from (float | Unset):
        submitted_tpomw3_to (float | Unset):
        submitted_tpo_price_3_from (float | Unset):
        submitted_tpo_price_3_to (float | Unset):
        submitted_tpomw4_from (float | Unset):
        submitted_tpomw4_to (float | Unset):
        submitted_tpo_price_4_from (float | Unset):
        submitted_tpo_price_4_to (float | Unset):
        submitted_tpomw5_from (float | Unset):
        submitted_tpomw5_to (float | Unset):
        submitted_tpo_price_5_from (float | Unset):
        submitted_tpo_price_5_to (float | Unset):
        submitted_tpomw6_from (float | Unset):
        submitted_tpomw6_to (float | Unset):
        submitted_tpo_price_6_from (float | Unset):
        submitted_tpo_price_6_to (float | Unset):
        submitted_tpomw7_from (float | Unset):
        submitted_tpomw7_to (float | Unset):
        submitted_tpo_price_7_from (float | Unset):
        submitted_tpo_price_7_to (float | Unset):
        submitted_tpomw8_from (float | Unset):
        submitted_tpomw8_to (float | Unset):
        submitted_tpo_price_8_from (float | Unset):
        submitted_tpo_price_8_to (float | Unset):
        submitted_tpomw9_from (float | Unset):
        submitted_tpomw9_to (float | Unset):
        submitted_tpo_price_9_from (float | Unset):
        submitted_tpo_price_9_to (float | Unset):
        submitted_tpomw10_from (float | Unset):
        submitted_tpomw10_to (float | Unset):
        submitted_tpo_price_10_from (float | Unset):
        submitted_tpo_price_10_to (float | Unset):
        proxy_extension (str | Unset):
        sced_timestamp_from (str | Unset):
        sced_timestamp_to (str | Unset):
        repeat_hour_flag (bool | Unset):
        qse_name (str | Unset):
        dme_name (str | Unset):
        resource_name (str | Unset):
        resource_type (str | Unset):
        sced1_curve_mw1_from (float | Unset):
        sced1_curve_mw1_to (float | Unset):
        sced1_curve_price_1_from (float | Unset):
        sced1_curve_price_1_to (float | Unset):
        sced1_curve_mw2_from (float | Unset):
        sced1_curve_mw2_to (float | Unset):
        sced1_curve_price_2_from (float | Unset):
        sced1_curve_price_2_to (float | Unset):
        sced1_curve_mw3_from (float | Unset):
        sced1_curve_mw3_to (float | Unset):
        sced1_curve_price_3_from (float | Unset):
        sced1_curve_price_3_to (float | Unset):
        sced1_curve_mw4_from (float | Unset):
        sced1_curve_mw4_to (float | Unset):
        sced1_curve_price_4_from (float | Unset):
        sced1_curve_price_4_to (float | Unset):
        sced1_curve_mw5_from (float | Unset):
        sced1_curve_mw5_to (float | Unset):
        sced1_curve_price_5_from (float | Unset):
        sced1_curve_price_5_to (float | Unset):
        sced1_curve_mw6_from (float | Unset):
        sced1_curve_mw6_to (float | Unset):
        sced1_curve_price_6_from (float | Unset):
        sced1_curve_price_6_to (float | Unset):
        sced1_curve_mw7_from (float | Unset):
        sced1_curve_mw7_to (float | Unset):
        sced1_curve_price_7_from (float | Unset):
        sced1_curve_price_7_to (float | Unset):
        sced1_curve_mw8_from (float | Unset):
        sced1_curve_mw8_to (float | Unset):
        sced1_curve_price_8_from (float | Unset):
        sced1_curve_price_8_to (float | Unset):
        sced1_curve_mw9_from (float | Unset):
        sced1_curve_mw9_to (float | Unset):
        sced1_curve_price_9_from (float | Unset):
        sced1_curve_price_9_to (float | Unset):
        sced1_curve_mw10_from (float | Unset):
        sced1_curve_mw10_to (float | Unset):
        sced1_curve_price_10_from (float | Unset):
        sced1_curve_price_10_to (float | Unset):
        sced1_curve_mw11_from (float | Unset):
        sced1_curve_mw11_to (float | Unset):
        sced1_curve_price_11_from (float | Unset):
        sced1_curve_price_11_to (float | Unset):
        sced1_curve_mw12_from (float | Unset):
        sced1_curve_mw12_to (float | Unset):
        sced1_curve_price_12_from (float | Unset):
        sced1_curve_price_12_to (float | Unset):
        sced1_curve_mw13_from (float | Unset):
        sced1_curve_mw13_to (float | Unset):
        sced1_curve_price_13_from (float | Unset):
        sced1_curve_price_13_to (float | Unset):
        sced1_curve_mw14_from (float | Unset):
        sced1_curve_mw14_to (float | Unset):
        sced1_curve_price_14_from (float | Unset):
        sced1_curve_price_14_to (float | Unset):
        sced1_curve_mw15_from (float | Unset):
        sced1_curve_mw15_to (float | Unset):
        sced1_curve_price_15_from (float | Unset):
        sced1_curve_price_15_to (float | Unset):
        sced1_curve_mw16_from (float | Unset):
        sced1_curve_mw16_to (float | Unset):
        sced1_curve_price_16_from (float | Unset):
        sced1_curve_price_16_to (float | Unset):
        sced1_curve_mw17_from (float | Unset):
        sced1_curve_mw17_to (float | Unset):
        sced1_curve_price_17_from (float | Unset):
        sced1_curve_price_17_to (float | Unset):
        sced1_curve_mw18_from (float | Unset):
        sced1_curve_mw18_to (float | Unset):
        sced1_curve_price_18_from (float | Unset):
        sced1_curve_price_18_to (float | Unset):
        sced1_curve_mw19_from (float | Unset):
        sced1_curve_mw19_to (float | Unset):
        sced1_curve_price_19_from (float | Unset):
        sced1_curve_price_19_to (float | Unset):
        sced1_curve_mw20_from (float | Unset):
        sced1_curve_mw20_to (float | Unset):
        sced1_curve_price_20_from (float | Unset):
        sced1_curve_price_20_to (float | Unset):
        sced1_curve_mw21_from (float | Unset):
        sced1_curve_mw21_to (float | Unset):
        sced1_curve_price_21_from (float | Unset):
        sced1_curve_price_21_to (float | Unset):
        sced1_curve_mw22_from (float | Unset):
        sced1_curve_mw22_to (float | Unset):
        sced1_curve_price_22_from (float | Unset):
        sced1_curve_price_22_to (float | Unset):
        sced1_curve_mw23_from (float | Unset):
        sced1_curve_mw23_to (float | Unset):
        sced1_curve_price_23_from (float | Unset):
        sced1_curve_price_23_to (float | Unset):
        sced1_curve_mw24_from (float | Unset):
        sced1_curve_mw24_to (float | Unset):
        sced1_curve_price_24_from (float | Unset):
        sced1_curve_price_24_to (float | Unset):
        sced1_curve_mw25_from (float | Unset):
        sced1_curve_mw25_to (float | Unset):
        sced1_curve_price_25_from (float | Unset):
        sced1_curve_price_25_to (float | Unset):
        sced1_curve_mw26_from (float | Unset):
        sced1_curve_mw26_to (float | Unset):
        sced1_curve_price_26_from (float | Unset):
        sced1_curve_price_26_to (float | Unset):
        sced1_curve_mw27_from (float | Unset):
        sced1_curve_mw27_to (float | Unset):
        sced1_curve_price_27_from (float | Unset):
        sced1_curve_price_27_to (float | Unset):
        sced1_curve_mw28_from (float | Unset):
        sced1_curve_mw28_to (float | Unset):
        sced1_curve_price_28_from (float | Unset):
        sced1_curve_price_28_to (float | Unset):
        sced1_curve_mw29_from (float | Unset):
        sced1_curve_mw29_to (float | Unset):
        sced1_curve_price_29_from (float | Unset):
        sced1_curve_price_29_to (float | Unset):
        sced1_curve_mw30_from (float | Unset):
        sced1_curve_mw30_to (float | Unset):
        sced1_curve_price_30_from (float | Unset):
        sced1_curve_price_30_to (float | Unset):
        sced1_curve_mw31_from (float | Unset):
        sced1_curve_mw31_to (float | Unset):
        sced1_curve_price_31_from (float | Unset):
        sced1_curve_price_31_to (float | Unset):
        sced1_curve_mw32_from (float | Unset):
        sced1_curve_mw32_to (float | Unset):
        sced1_curve_price_32_from (float | Unset):
        sced1_curve_price_32_to (float | Unset):
        sced1_curve_mw33_from (float | Unset):
        sced1_curve_mw33_to (float | Unset):
        sced1_curve_price_33_from (float | Unset):
        sced1_curve_price_33_to (float | Unset):
        sced1_curve_mw34_from (float | Unset):
        sced1_curve_mw34_to (float | Unset):
        sced1_curve_price_34_from (float | Unset):
        sced1_curve_price_34_to (float | Unset):
        sced1_curve_mw35_from (float | Unset):
        sced1_curve_mw35_to (float | Unset):
        sced1_curve_price_35_from (float | Unset):
        sced1_curve_price_35_to (float | Unset):
        sced2_curve_mw1_from (float | Unset):
        sced2_curve_mw1_to (float | Unset):
        sced2_curve_price_1_from (float | Unset):
        sced2_curve_price_1_to (float | Unset):
        sced2_curve_mw2_from (float | Unset):
        sced2_curve_mw2_to (float | Unset):
        sced2_curve_price_2_from (float | Unset):
        sced2_curve_price_2_to (float | Unset):
        sced2_curve_mw3_from (float | Unset):
        sced2_curve_mw3_to (float | Unset):
        sced2_curve_price_3_from (float | Unset):
        sced2_curve_price_3_to (float | Unset):
        sced2_curve_mw4_from (float | Unset):
        sced2_curve_mw4_to (float | Unset):
        sced2_curve_price_4_from (float | Unset):
        sced2_curve_price_4_to (float | Unset):
        sced2_curve_mw5_from (float | Unset):
        sced2_curve_mw5_to (float | Unset):
        sced2_curve_price_5_from (float | Unset):
        sced2_curve_price_5_to (float | Unset):
        sced2_curve_mw6_from (float | Unset):
        sced2_curve_mw6_to (float | Unset):
        sced2_curve_price_6_from (float | Unset):
        sced2_curve_price_6_to (float | Unset):
        sced2_curve_mw7_from (float | Unset):
        sced2_curve_mw7_to (float | Unset):
        sced2_curve_price_7_from (float | Unset):
        sced2_curve_price_7_to (float | Unset):
        sced2_curve_mw8_from (float | Unset):
        sced2_curve_mw8_to (float | Unset):
        sced2_curve_price_8_from (float | Unset):
        sced2_curve_price_8_to (float | Unset):
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
        sced2_curve_mw9_from=sced2_curve_mw9_from,
        sced2_curve_mw9_to=sced2_curve_mw9_to,
        sced2_curve_price_9_from=sced2_curve_price_9_from,
        sced2_curve_price_9_to=sced2_curve_price_9_to,
        sced2_curve_mw10_from=sced2_curve_mw10_from,
        sced2_curve_mw10_to=sced2_curve_mw10_to,
        sced2_curve_price_10_from=sced2_curve_price_10_from,
        sced2_curve_price_10_to=sced2_curve_price_10_to,
        sced2_curve_mw11_from=sced2_curve_mw11_from,
        sced2_curve_mw11_to=sced2_curve_mw11_to,
        sced2_curve_price_11_from=sced2_curve_price_11_from,
        sced2_curve_price_11_to=sced2_curve_price_11_to,
        sced2_curve_mw12_from=sced2_curve_mw12_from,
        sced2_curve_mw12_to=sced2_curve_mw12_to,
        sced2_curve_price_12_from=sced2_curve_price_12_from,
        sced2_curve_price_12_to=sced2_curve_price_12_to,
        sced2_curve_mw13_from=sced2_curve_mw13_from,
        sced2_curve_mw13_to=sced2_curve_mw13_to,
        sced2_curve_price_13_from=sced2_curve_price_13_from,
        sced2_curve_price_13_to=sced2_curve_price_13_to,
        sced2_curve_mw14_from=sced2_curve_mw14_from,
        sced2_curve_mw14_to=sced2_curve_mw14_to,
        sced2_curve_price_14_from=sced2_curve_price_14_from,
        sced2_curve_price_14_to=sced2_curve_price_14_to,
        sced2_curve_mw15_from=sced2_curve_mw15_from,
        sced2_curve_mw15_to=sced2_curve_mw15_to,
        sced2_curve_price_15_from=sced2_curve_price_15_from,
        sced2_curve_price_15_to=sced2_curve_price_15_to,
        sced2_curve_mw16_from=sced2_curve_mw16_from,
        sced2_curve_mw16_to=sced2_curve_mw16_to,
        sced2_curve_price_16_from=sced2_curve_price_16_from,
        sced2_curve_price_16_to=sced2_curve_price_16_to,
        sced2_curve_mw17_from=sced2_curve_mw17_from,
        sced2_curve_mw17_to=sced2_curve_mw17_to,
        sced2_curve_price_17_from=sced2_curve_price_17_from,
        sced2_curve_price_17_to=sced2_curve_price_17_to,
        sced2_curve_mw18_from=sced2_curve_mw18_from,
        sced2_curve_mw18_to=sced2_curve_mw18_to,
        sced2_curve_price_18_from=sced2_curve_price_18_from,
        sced2_curve_price_18_to=sced2_curve_price_18_to,
        sced2_curve_mw19_from=sced2_curve_mw19_from,
        sced2_curve_mw19_to=sced2_curve_mw19_to,
        sced2_curve_price_19_from=sced2_curve_price_19_from,
        sced2_curve_price_19_to=sced2_curve_price_19_to,
        sced2_curve_mw20_from=sced2_curve_mw20_from,
        sced2_curve_mw20_to=sced2_curve_mw20_to,
        sced2_curve_price_20_from=sced2_curve_price_20_from,
        sced2_curve_price_20_to=sced2_curve_price_20_to,
        sced2_curve_mw21_from=sced2_curve_mw21_from,
        sced2_curve_mw21_to=sced2_curve_mw21_to,
        sced2_curve_price_21_from=sced2_curve_price_21_from,
        sced2_curve_price_21_to=sced2_curve_price_21_to,
        sced2_curve_mw22_from=sced2_curve_mw22_from,
        sced2_curve_mw22_to=sced2_curve_mw22_to,
        sced2_curve_price_22_from=sced2_curve_price_22_from,
        sced2_curve_price_22_to=sced2_curve_price_22_to,
        sced2_curve_mw23_from=sced2_curve_mw23_from,
        sced2_curve_mw23_to=sced2_curve_mw23_to,
        sced2_curve_price_23_from=sced2_curve_price_23_from,
        sced2_curve_price_23_to=sced2_curve_price_23_to,
        sced2_curve_mw24_from=sced2_curve_mw24_from,
        sced2_curve_mw24_to=sced2_curve_mw24_to,
        sced2_curve_price_24_from=sced2_curve_price_24_from,
        sced2_curve_price_24_to=sced2_curve_price_24_to,
        sced2_curve_mw25_from=sced2_curve_mw25_from,
        sced2_curve_mw25_to=sced2_curve_mw25_to,
        sced2_curve_price_25_from=sced2_curve_price_25_from,
        sced2_curve_price_25_to=sced2_curve_price_25_to,
        sced2_curve_mw26_from=sced2_curve_mw26_from,
        sced2_curve_mw26_to=sced2_curve_mw26_to,
        sced2_curve_price_26_from=sced2_curve_price_26_from,
        sced2_curve_price_26_to=sced2_curve_price_26_to,
        sced2_curve_mw27_from=sced2_curve_mw27_from,
        sced2_curve_mw27_to=sced2_curve_mw27_to,
        sced2_curve_price_27_from=sced2_curve_price_27_from,
        sced2_curve_price_27_to=sced2_curve_price_27_to,
        sced2_curve_mw28_from=sced2_curve_mw28_from,
        sced2_curve_mw28_to=sced2_curve_mw28_to,
        sced2_curve_price_28_from=sced2_curve_price_28_from,
        sced2_curve_price_28_to=sced2_curve_price_28_to,
        sced2_curve_mw29_from=sced2_curve_mw29_from,
        sced2_curve_mw29_to=sced2_curve_mw29_to,
        sced2_curve_price_29_from=sced2_curve_price_29_from,
        sced2_curve_price_29_to=sced2_curve_price_29_to,
        sced2_curve_mw30_from=sced2_curve_mw30_from,
        sced2_curve_mw30_to=sced2_curve_mw30_to,
        sced2_curve_price_30_from=sced2_curve_price_30_from,
        sced2_curve_price_30_to=sced2_curve_price_30_to,
        sced2_curve_mw31_from=sced2_curve_mw31_from,
        sced2_curve_mw31_to=sced2_curve_mw31_to,
        sced2_curve_price_31_from=sced2_curve_price_31_from,
        sced2_curve_price_31_to=sced2_curve_price_31_to,
        sced2_curve_mw32_from=sced2_curve_mw32_from,
        sced2_curve_mw32_to=sced2_curve_mw32_to,
        sced2_curve_price_32_from=sced2_curve_price_32_from,
        sced2_curve_price_32_to=sced2_curve_price_32_to,
        sced2_curve_mw33_from=sced2_curve_mw33_from,
        sced2_curve_mw33_to=sced2_curve_mw33_to,
        sced2_curve_price_33_from=sced2_curve_price_33_from,
        sced2_curve_price_33_to=sced2_curve_price_33_to,
        sced2_curve_mw34_from=sced2_curve_mw34_from,
        sced2_curve_mw34_to=sced2_curve_mw34_to,
        sced2_curve_price_34_from=sced2_curve_price_34_from,
        sced2_curve_price_34_to=sced2_curve_price_34_to,
        sced2_curve_mw35_from=sced2_curve_mw35_from,
        sced2_curve_mw35_to=sced2_curve_mw35_to,
        sced2_curve_price_35_from=sced2_curve_price_35_from,
        sced2_curve_price_35_to=sced2_curve_price_35_to,
        output_schedule_from=output_schedule_from,
        output_schedule_to=output_schedule_to,
        hsl_from=hsl_from,
        hsl_to=hsl_to,
        hasl_from=hasl_from,
        hasl_to=hasl_to,
        hdl_from=hdl_from,
        hdl_to=hdl_to,
        lsl_from=lsl_from,
        lsl_to=lsl_to,
        lasl_from=lasl_from,
        lasl_to=lasl_to,
        ldl_from=ldl_from,
        ldl_to=ldl_to,
        telemetered_resource_status=telemetered_resource_status,
        base_point_from=base_point_from,
        base_point_to=base_point_to,
        telemetered_net_output_from=telemetered_net_output_from,
        telemetered_net_output_to=telemetered_net_output_to,
        asregup_from=asregup_from,
        asregup_to=asregup_to,
        asregdn_from=asregdn_from,
        asregdn_to=asregdn_to,
        asrrs_from=asrrs_from,
        asrrs_to=asrrs_to,
        asrrsffr_from=asrrsffr_from,
        asrrsffr_to=asrrsffr_to,
        asnsrs_from=asnsrs_from,
        asnsrs_to=asnsrs_to,
        bid_type=bid_type,
        start_up_cold_offer_from=start_up_cold_offer_from,
        start_up_cold_offer_to=start_up_cold_offer_to,
        start_up_hot_offer_from=start_up_hot_offer_from,
        start_up_hot_offer_to=start_up_hot_offer_to,
        start_up_inter_offer_from=start_up_inter_offer_from,
        start_up_inter_offer_to=start_up_inter_offer_to,
        min_gen_cost_from=min_gen_cost_from,
        min_gen_cost_to=min_gen_cost_to,
        submitted_tpomw1_from=submitted_tpomw1_from,
        submitted_tpomw1_to=submitted_tpomw1_to,
        submitted_tpo_price_1_from=submitted_tpo_price_1_from,
        submitted_tpo_price_1_to=submitted_tpo_price_1_to,
        submitted_tpomw2_from=submitted_tpomw2_from,
        submitted_tpomw2_to=submitted_tpomw2_to,
        submitted_tpo_price_2_from=submitted_tpo_price_2_from,
        submitted_tpo_price_2_to=submitted_tpo_price_2_to,
        submitted_tpomw3_from=submitted_tpomw3_from,
        submitted_tpomw3_to=submitted_tpomw3_to,
        submitted_tpo_price_3_from=submitted_tpo_price_3_from,
        submitted_tpo_price_3_to=submitted_tpo_price_3_to,
        submitted_tpomw4_from=submitted_tpomw4_from,
        submitted_tpomw4_to=submitted_tpomw4_to,
        submitted_tpo_price_4_from=submitted_tpo_price_4_from,
        submitted_tpo_price_4_to=submitted_tpo_price_4_to,
        submitted_tpomw5_from=submitted_tpomw5_from,
        submitted_tpomw5_to=submitted_tpomw5_to,
        submitted_tpo_price_5_from=submitted_tpo_price_5_from,
        submitted_tpo_price_5_to=submitted_tpo_price_5_to,
        submitted_tpomw6_from=submitted_tpomw6_from,
        submitted_tpomw6_to=submitted_tpomw6_to,
        submitted_tpo_price_6_from=submitted_tpo_price_6_from,
        submitted_tpo_price_6_to=submitted_tpo_price_6_to,
        submitted_tpomw7_from=submitted_tpomw7_from,
        submitted_tpomw7_to=submitted_tpomw7_to,
        submitted_tpo_price_7_from=submitted_tpo_price_7_from,
        submitted_tpo_price_7_to=submitted_tpo_price_7_to,
        submitted_tpomw8_from=submitted_tpomw8_from,
        submitted_tpomw8_to=submitted_tpomw8_to,
        submitted_tpo_price_8_from=submitted_tpo_price_8_from,
        submitted_tpo_price_8_to=submitted_tpo_price_8_to,
        submitted_tpomw9_from=submitted_tpomw9_from,
        submitted_tpomw9_to=submitted_tpomw9_to,
        submitted_tpo_price_9_from=submitted_tpo_price_9_from,
        submitted_tpo_price_9_to=submitted_tpo_price_9_to,
        submitted_tpomw10_from=submitted_tpomw10_from,
        submitted_tpomw10_to=submitted_tpomw10_to,
        submitted_tpo_price_10_from=submitted_tpo_price_10_from,
        submitted_tpo_price_10_to=submitted_tpo_price_10_to,
        proxy_extension=proxy_extension,
        sced_timestamp_from=sced_timestamp_from,
        sced_timestamp_to=sced_timestamp_to,
        repeat_hour_flag=repeat_hour_flag,
        qse_name=qse_name,
        dme_name=dme_name,
        resource_name=resource_name,
        resource_type=resource_type,
        sced1_curve_mw1_from=sced1_curve_mw1_from,
        sced1_curve_mw1_to=sced1_curve_mw1_to,
        sced1_curve_price_1_from=sced1_curve_price_1_from,
        sced1_curve_price_1_to=sced1_curve_price_1_to,
        sced1_curve_mw2_from=sced1_curve_mw2_from,
        sced1_curve_mw2_to=sced1_curve_mw2_to,
        sced1_curve_price_2_from=sced1_curve_price_2_from,
        sced1_curve_price_2_to=sced1_curve_price_2_to,
        sced1_curve_mw3_from=sced1_curve_mw3_from,
        sced1_curve_mw3_to=sced1_curve_mw3_to,
        sced1_curve_price_3_from=sced1_curve_price_3_from,
        sced1_curve_price_3_to=sced1_curve_price_3_to,
        sced1_curve_mw4_from=sced1_curve_mw4_from,
        sced1_curve_mw4_to=sced1_curve_mw4_to,
        sced1_curve_price_4_from=sced1_curve_price_4_from,
        sced1_curve_price_4_to=sced1_curve_price_4_to,
        sced1_curve_mw5_from=sced1_curve_mw5_from,
        sced1_curve_mw5_to=sced1_curve_mw5_to,
        sced1_curve_price_5_from=sced1_curve_price_5_from,
        sced1_curve_price_5_to=sced1_curve_price_5_to,
        sced1_curve_mw6_from=sced1_curve_mw6_from,
        sced1_curve_mw6_to=sced1_curve_mw6_to,
        sced1_curve_price_6_from=sced1_curve_price_6_from,
        sced1_curve_price_6_to=sced1_curve_price_6_to,
        sced1_curve_mw7_from=sced1_curve_mw7_from,
        sced1_curve_mw7_to=sced1_curve_mw7_to,
        sced1_curve_price_7_from=sced1_curve_price_7_from,
        sced1_curve_price_7_to=sced1_curve_price_7_to,
        sced1_curve_mw8_from=sced1_curve_mw8_from,
        sced1_curve_mw8_to=sced1_curve_mw8_to,
        sced1_curve_price_8_from=sced1_curve_price_8_from,
        sced1_curve_price_8_to=sced1_curve_price_8_to,
        sced1_curve_mw9_from=sced1_curve_mw9_from,
        sced1_curve_mw9_to=sced1_curve_mw9_to,
        sced1_curve_price_9_from=sced1_curve_price_9_from,
        sced1_curve_price_9_to=sced1_curve_price_9_to,
        sced1_curve_mw10_from=sced1_curve_mw10_from,
        sced1_curve_mw10_to=sced1_curve_mw10_to,
        sced1_curve_price_10_from=sced1_curve_price_10_from,
        sced1_curve_price_10_to=sced1_curve_price_10_to,
        sced1_curve_mw11_from=sced1_curve_mw11_from,
        sced1_curve_mw11_to=sced1_curve_mw11_to,
        sced1_curve_price_11_from=sced1_curve_price_11_from,
        sced1_curve_price_11_to=sced1_curve_price_11_to,
        sced1_curve_mw12_from=sced1_curve_mw12_from,
        sced1_curve_mw12_to=sced1_curve_mw12_to,
        sced1_curve_price_12_from=sced1_curve_price_12_from,
        sced1_curve_price_12_to=sced1_curve_price_12_to,
        sced1_curve_mw13_from=sced1_curve_mw13_from,
        sced1_curve_mw13_to=sced1_curve_mw13_to,
        sced1_curve_price_13_from=sced1_curve_price_13_from,
        sced1_curve_price_13_to=sced1_curve_price_13_to,
        sced1_curve_mw14_from=sced1_curve_mw14_from,
        sced1_curve_mw14_to=sced1_curve_mw14_to,
        sced1_curve_price_14_from=sced1_curve_price_14_from,
        sced1_curve_price_14_to=sced1_curve_price_14_to,
        sced1_curve_mw15_from=sced1_curve_mw15_from,
        sced1_curve_mw15_to=sced1_curve_mw15_to,
        sced1_curve_price_15_from=sced1_curve_price_15_from,
        sced1_curve_price_15_to=sced1_curve_price_15_to,
        sced1_curve_mw16_from=sced1_curve_mw16_from,
        sced1_curve_mw16_to=sced1_curve_mw16_to,
        sced1_curve_price_16_from=sced1_curve_price_16_from,
        sced1_curve_price_16_to=sced1_curve_price_16_to,
        sced1_curve_mw17_from=sced1_curve_mw17_from,
        sced1_curve_mw17_to=sced1_curve_mw17_to,
        sced1_curve_price_17_from=sced1_curve_price_17_from,
        sced1_curve_price_17_to=sced1_curve_price_17_to,
        sced1_curve_mw18_from=sced1_curve_mw18_from,
        sced1_curve_mw18_to=sced1_curve_mw18_to,
        sced1_curve_price_18_from=sced1_curve_price_18_from,
        sced1_curve_price_18_to=sced1_curve_price_18_to,
        sced1_curve_mw19_from=sced1_curve_mw19_from,
        sced1_curve_mw19_to=sced1_curve_mw19_to,
        sced1_curve_price_19_from=sced1_curve_price_19_from,
        sced1_curve_price_19_to=sced1_curve_price_19_to,
        sced1_curve_mw20_from=sced1_curve_mw20_from,
        sced1_curve_mw20_to=sced1_curve_mw20_to,
        sced1_curve_price_20_from=sced1_curve_price_20_from,
        sced1_curve_price_20_to=sced1_curve_price_20_to,
        sced1_curve_mw21_from=sced1_curve_mw21_from,
        sced1_curve_mw21_to=sced1_curve_mw21_to,
        sced1_curve_price_21_from=sced1_curve_price_21_from,
        sced1_curve_price_21_to=sced1_curve_price_21_to,
        sced1_curve_mw22_from=sced1_curve_mw22_from,
        sced1_curve_mw22_to=sced1_curve_mw22_to,
        sced1_curve_price_22_from=sced1_curve_price_22_from,
        sced1_curve_price_22_to=sced1_curve_price_22_to,
        sced1_curve_mw23_from=sced1_curve_mw23_from,
        sced1_curve_mw23_to=sced1_curve_mw23_to,
        sced1_curve_price_23_from=sced1_curve_price_23_from,
        sced1_curve_price_23_to=sced1_curve_price_23_to,
        sced1_curve_mw24_from=sced1_curve_mw24_from,
        sced1_curve_mw24_to=sced1_curve_mw24_to,
        sced1_curve_price_24_from=sced1_curve_price_24_from,
        sced1_curve_price_24_to=sced1_curve_price_24_to,
        sced1_curve_mw25_from=sced1_curve_mw25_from,
        sced1_curve_mw25_to=sced1_curve_mw25_to,
        sced1_curve_price_25_from=sced1_curve_price_25_from,
        sced1_curve_price_25_to=sced1_curve_price_25_to,
        sced1_curve_mw26_from=sced1_curve_mw26_from,
        sced1_curve_mw26_to=sced1_curve_mw26_to,
        sced1_curve_price_26_from=sced1_curve_price_26_from,
        sced1_curve_price_26_to=sced1_curve_price_26_to,
        sced1_curve_mw27_from=sced1_curve_mw27_from,
        sced1_curve_mw27_to=sced1_curve_mw27_to,
        sced1_curve_price_27_from=sced1_curve_price_27_from,
        sced1_curve_price_27_to=sced1_curve_price_27_to,
        sced1_curve_mw28_from=sced1_curve_mw28_from,
        sced1_curve_mw28_to=sced1_curve_mw28_to,
        sced1_curve_price_28_from=sced1_curve_price_28_from,
        sced1_curve_price_28_to=sced1_curve_price_28_to,
        sced1_curve_mw29_from=sced1_curve_mw29_from,
        sced1_curve_mw29_to=sced1_curve_mw29_to,
        sced1_curve_price_29_from=sced1_curve_price_29_from,
        sced1_curve_price_29_to=sced1_curve_price_29_to,
        sced1_curve_mw30_from=sced1_curve_mw30_from,
        sced1_curve_mw30_to=sced1_curve_mw30_to,
        sced1_curve_price_30_from=sced1_curve_price_30_from,
        sced1_curve_price_30_to=sced1_curve_price_30_to,
        sced1_curve_mw31_from=sced1_curve_mw31_from,
        sced1_curve_mw31_to=sced1_curve_mw31_to,
        sced1_curve_price_31_from=sced1_curve_price_31_from,
        sced1_curve_price_31_to=sced1_curve_price_31_to,
        sced1_curve_mw32_from=sced1_curve_mw32_from,
        sced1_curve_mw32_to=sced1_curve_mw32_to,
        sced1_curve_price_32_from=sced1_curve_price_32_from,
        sced1_curve_price_32_to=sced1_curve_price_32_to,
        sced1_curve_mw33_from=sced1_curve_mw33_from,
        sced1_curve_mw33_to=sced1_curve_mw33_to,
        sced1_curve_price_33_from=sced1_curve_price_33_from,
        sced1_curve_price_33_to=sced1_curve_price_33_to,
        sced1_curve_mw34_from=sced1_curve_mw34_from,
        sced1_curve_mw34_to=sced1_curve_mw34_to,
        sced1_curve_price_34_from=sced1_curve_price_34_from,
        sced1_curve_price_34_to=sced1_curve_price_34_to,
        sced1_curve_mw35_from=sced1_curve_mw35_from,
        sced1_curve_mw35_to=sced1_curve_mw35_to,
        sced1_curve_price_35_from=sced1_curve_price_35_from,
        sced1_curve_price_35_to=sced1_curve_price_35_to,
        sced2_curve_mw1_from=sced2_curve_mw1_from,
        sced2_curve_mw1_to=sced2_curve_mw1_to,
        sced2_curve_price_1_from=sced2_curve_price_1_from,
        sced2_curve_price_1_to=sced2_curve_price_1_to,
        sced2_curve_mw2_from=sced2_curve_mw2_from,
        sced2_curve_mw2_to=sced2_curve_mw2_to,
        sced2_curve_price_2_from=sced2_curve_price_2_from,
        sced2_curve_price_2_to=sced2_curve_price_2_to,
        sced2_curve_mw3_from=sced2_curve_mw3_from,
        sced2_curve_mw3_to=sced2_curve_mw3_to,
        sced2_curve_price_3_from=sced2_curve_price_3_from,
        sced2_curve_price_3_to=sced2_curve_price_3_to,
        sced2_curve_mw4_from=sced2_curve_mw4_from,
        sced2_curve_mw4_to=sced2_curve_mw4_to,
        sced2_curve_price_4_from=sced2_curve_price_4_from,
        sced2_curve_price_4_to=sced2_curve_price_4_to,
        sced2_curve_mw5_from=sced2_curve_mw5_from,
        sced2_curve_mw5_to=sced2_curve_mw5_to,
        sced2_curve_price_5_from=sced2_curve_price_5_from,
        sced2_curve_price_5_to=sced2_curve_price_5_to,
        sced2_curve_mw6_from=sced2_curve_mw6_from,
        sced2_curve_mw6_to=sced2_curve_mw6_to,
        sced2_curve_price_6_from=sced2_curve_price_6_from,
        sced2_curve_price_6_to=sced2_curve_price_6_to,
        sced2_curve_mw7_from=sced2_curve_mw7_from,
        sced2_curve_mw7_to=sced2_curve_mw7_to,
        sced2_curve_price_7_from=sced2_curve_price_7_from,
        sced2_curve_price_7_to=sced2_curve_price_7_to,
        sced2_curve_mw8_from=sced2_curve_mw8_from,
        sced2_curve_mw8_to=sced2_curve_mw8_to,
        sced2_curve_price_8_from=sced2_curve_price_8_from,
        sced2_curve_price_8_to=sced2_curve_price_8_to,
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
    sced2_curve_mw9_from: float | Unset = UNSET,
    sced2_curve_mw9_to: float | Unset = UNSET,
    sced2_curve_price_9_from: float | Unset = UNSET,
    sced2_curve_price_9_to: float | Unset = UNSET,
    sced2_curve_mw10_from: float | Unset = UNSET,
    sced2_curve_mw10_to: float | Unset = UNSET,
    sced2_curve_price_10_from: float | Unset = UNSET,
    sced2_curve_price_10_to: float | Unset = UNSET,
    sced2_curve_mw11_from: float | Unset = UNSET,
    sced2_curve_mw11_to: float | Unset = UNSET,
    sced2_curve_price_11_from: float | Unset = UNSET,
    sced2_curve_price_11_to: float | Unset = UNSET,
    sced2_curve_mw12_from: float | Unset = UNSET,
    sced2_curve_mw12_to: float | Unset = UNSET,
    sced2_curve_price_12_from: float | Unset = UNSET,
    sced2_curve_price_12_to: float | Unset = UNSET,
    sced2_curve_mw13_from: float | Unset = UNSET,
    sced2_curve_mw13_to: float | Unset = UNSET,
    sced2_curve_price_13_from: float | Unset = UNSET,
    sced2_curve_price_13_to: float | Unset = UNSET,
    sced2_curve_mw14_from: float | Unset = UNSET,
    sced2_curve_mw14_to: float | Unset = UNSET,
    sced2_curve_price_14_from: float | Unset = UNSET,
    sced2_curve_price_14_to: float | Unset = UNSET,
    sced2_curve_mw15_from: float | Unset = UNSET,
    sced2_curve_mw15_to: float | Unset = UNSET,
    sced2_curve_price_15_from: float | Unset = UNSET,
    sced2_curve_price_15_to: float | Unset = UNSET,
    sced2_curve_mw16_from: float | Unset = UNSET,
    sced2_curve_mw16_to: float | Unset = UNSET,
    sced2_curve_price_16_from: float | Unset = UNSET,
    sced2_curve_price_16_to: float | Unset = UNSET,
    sced2_curve_mw17_from: float | Unset = UNSET,
    sced2_curve_mw17_to: float | Unset = UNSET,
    sced2_curve_price_17_from: float | Unset = UNSET,
    sced2_curve_price_17_to: float | Unset = UNSET,
    sced2_curve_mw18_from: float | Unset = UNSET,
    sced2_curve_mw18_to: float | Unset = UNSET,
    sced2_curve_price_18_from: float | Unset = UNSET,
    sced2_curve_price_18_to: float | Unset = UNSET,
    sced2_curve_mw19_from: float | Unset = UNSET,
    sced2_curve_mw19_to: float | Unset = UNSET,
    sced2_curve_price_19_from: float | Unset = UNSET,
    sced2_curve_price_19_to: float | Unset = UNSET,
    sced2_curve_mw20_from: float | Unset = UNSET,
    sced2_curve_mw20_to: float | Unset = UNSET,
    sced2_curve_price_20_from: float | Unset = UNSET,
    sced2_curve_price_20_to: float | Unset = UNSET,
    sced2_curve_mw21_from: float | Unset = UNSET,
    sced2_curve_mw21_to: float | Unset = UNSET,
    sced2_curve_price_21_from: float | Unset = UNSET,
    sced2_curve_price_21_to: float | Unset = UNSET,
    sced2_curve_mw22_from: float | Unset = UNSET,
    sced2_curve_mw22_to: float | Unset = UNSET,
    sced2_curve_price_22_from: float | Unset = UNSET,
    sced2_curve_price_22_to: float | Unset = UNSET,
    sced2_curve_mw23_from: float | Unset = UNSET,
    sced2_curve_mw23_to: float | Unset = UNSET,
    sced2_curve_price_23_from: float | Unset = UNSET,
    sced2_curve_price_23_to: float | Unset = UNSET,
    sced2_curve_mw24_from: float | Unset = UNSET,
    sced2_curve_mw24_to: float | Unset = UNSET,
    sced2_curve_price_24_from: float | Unset = UNSET,
    sced2_curve_price_24_to: float | Unset = UNSET,
    sced2_curve_mw25_from: float | Unset = UNSET,
    sced2_curve_mw25_to: float | Unset = UNSET,
    sced2_curve_price_25_from: float | Unset = UNSET,
    sced2_curve_price_25_to: float | Unset = UNSET,
    sced2_curve_mw26_from: float | Unset = UNSET,
    sced2_curve_mw26_to: float | Unset = UNSET,
    sced2_curve_price_26_from: float | Unset = UNSET,
    sced2_curve_price_26_to: float | Unset = UNSET,
    sced2_curve_mw27_from: float | Unset = UNSET,
    sced2_curve_mw27_to: float | Unset = UNSET,
    sced2_curve_price_27_from: float | Unset = UNSET,
    sced2_curve_price_27_to: float | Unset = UNSET,
    sced2_curve_mw28_from: float | Unset = UNSET,
    sced2_curve_mw28_to: float | Unset = UNSET,
    sced2_curve_price_28_from: float | Unset = UNSET,
    sced2_curve_price_28_to: float | Unset = UNSET,
    sced2_curve_mw29_from: float | Unset = UNSET,
    sced2_curve_mw29_to: float | Unset = UNSET,
    sced2_curve_price_29_from: float | Unset = UNSET,
    sced2_curve_price_29_to: float | Unset = UNSET,
    sced2_curve_mw30_from: float | Unset = UNSET,
    sced2_curve_mw30_to: float | Unset = UNSET,
    sced2_curve_price_30_from: float | Unset = UNSET,
    sced2_curve_price_30_to: float | Unset = UNSET,
    sced2_curve_mw31_from: float | Unset = UNSET,
    sced2_curve_mw31_to: float | Unset = UNSET,
    sced2_curve_price_31_from: float | Unset = UNSET,
    sced2_curve_price_31_to: float | Unset = UNSET,
    sced2_curve_mw32_from: float | Unset = UNSET,
    sced2_curve_mw32_to: float | Unset = UNSET,
    sced2_curve_price_32_from: float | Unset = UNSET,
    sced2_curve_price_32_to: float | Unset = UNSET,
    sced2_curve_mw33_from: float | Unset = UNSET,
    sced2_curve_mw33_to: float | Unset = UNSET,
    sced2_curve_price_33_from: float | Unset = UNSET,
    sced2_curve_price_33_to: float | Unset = UNSET,
    sced2_curve_mw34_from: float | Unset = UNSET,
    sced2_curve_mw34_to: float | Unset = UNSET,
    sced2_curve_price_34_from: float | Unset = UNSET,
    sced2_curve_price_34_to: float | Unset = UNSET,
    sced2_curve_mw35_from: float | Unset = UNSET,
    sced2_curve_mw35_to: float | Unset = UNSET,
    sced2_curve_price_35_from: float | Unset = UNSET,
    sced2_curve_price_35_to: float | Unset = UNSET,
    output_schedule_from: float | Unset = UNSET,
    output_schedule_to: float | Unset = UNSET,
    hsl_from: float | Unset = UNSET,
    hsl_to: float | Unset = UNSET,
    hasl_from: float | Unset = UNSET,
    hasl_to: float | Unset = UNSET,
    hdl_from: float | Unset = UNSET,
    hdl_to: float | Unset = UNSET,
    lsl_from: float | Unset = UNSET,
    lsl_to: float | Unset = UNSET,
    lasl_from: float | Unset = UNSET,
    lasl_to: float | Unset = UNSET,
    ldl_from: float | Unset = UNSET,
    ldl_to: float | Unset = UNSET,
    telemetered_resource_status: str | Unset = UNSET,
    base_point_from: float | Unset = UNSET,
    base_point_to: float | Unset = UNSET,
    telemetered_net_output_from: float | Unset = UNSET,
    telemetered_net_output_to: float | Unset = UNSET,
    asregup_from: float | Unset = UNSET,
    asregup_to: float | Unset = UNSET,
    asregdn_from: float | Unset = UNSET,
    asregdn_to: float | Unset = UNSET,
    asrrs_from: float | Unset = UNSET,
    asrrs_to: float | Unset = UNSET,
    asrrsffr_from: float | Unset = UNSET,
    asrrsffr_to: float | Unset = UNSET,
    asnsrs_from: float | Unset = UNSET,
    asnsrs_to: float | Unset = UNSET,
    bid_type: str | Unset = UNSET,
    start_up_cold_offer_from: float | Unset = UNSET,
    start_up_cold_offer_to: float | Unset = UNSET,
    start_up_hot_offer_from: float | Unset = UNSET,
    start_up_hot_offer_to: float | Unset = UNSET,
    start_up_inter_offer_from: float | Unset = UNSET,
    start_up_inter_offer_to: float | Unset = UNSET,
    min_gen_cost_from: float | Unset = UNSET,
    min_gen_cost_to: float | Unset = UNSET,
    submitted_tpomw1_from: float | Unset = UNSET,
    submitted_tpomw1_to: float | Unset = UNSET,
    submitted_tpo_price_1_from: float | Unset = UNSET,
    submitted_tpo_price_1_to: float | Unset = UNSET,
    submitted_tpomw2_from: float | Unset = UNSET,
    submitted_tpomw2_to: float | Unset = UNSET,
    submitted_tpo_price_2_from: float | Unset = UNSET,
    submitted_tpo_price_2_to: float | Unset = UNSET,
    submitted_tpomw3_from: float | Unset = UNSET,
    submitted_tpomw3_to: float | Unset = UNSET,
    submitted_tpo_price_3_from: float | Unset = UNSET,
    submitted_tpo_price_3_to: float | Unset = UNSET,
    submitted_tpomw4_from: float | Unset = UNSET,
    submitted_tpomw4_to: float | Unset = UNSET,
    submitted_tpo_price_4_from: float | Unset = UNSET,
    submitted_tpo_price_4_to: float | Unset = UNSET,
    submitted_tpomw5_from: float | Unset = UNSET,
    submitted_tpomw5_to: float | Unset = UNSET,
    submitted_tpo_price_5_from: float | Unset = UNSET,
    submitted_tpo_price_5_to: float | Unset = UNSET,
    submitted_tpomw6_from: float | Unset = UNSET,
    submitted_tpomw6_to: float | Unset = UNSET,
    submitted_tpo_price_6_from: float | Unset = UNSET,
    submitted_tpo_price_6_to: float | Unset = UNSET,
    submitted_tpomw7_from: float | Unset = UNSET,
    submitted_tpomw7_to: float | Unset = UNSET,
    submitted_tpo_price_7_from: float | Unset = UNSET,
    submitted_tpo_price_7_to: float | Unset = UNSET,
    submitted_tpomw8_from: float | Unset = UNSET,
    submitted_tpomw8_to: float | Unset = UNSET,
    submitted_tpo_price_8_from: float | Unset = UNSET,
    submitted_tpo_price_8_to: float | Unset = UNSET,
    submitted_tpomw9_from: float | Unset = UNSET,
    submitted_tpomw9_to: float | Unset = UNSET,
    submitted_tpo_price_9_from: float | Unset = UNSET,
    submitted_tpo_price_9_to: float | Unset = UNSET,
    submitted_tpomw10_from: float | Unset = UNSET,
    submitted_tpomw10_to: float | Unset = UNSET,
    submitted_tpo_price_10_from: float | Unset = UNSET,
    submitted_tpo_price_10_to: float | Unset = UNSET,
    proxy_extension: str | Unset = UNSET,
    sced_timestamp_from: str | Unset = UNSET,
    sced_timestamp_to: str | Unset = UNSET,
    repeat_hour_flag: bool | Unset = UNSET,
    qse_name: str | Unset = UNSET,
    dme_name: str | Unset = UNSET,
    resource_name: str | Unset = UNSET,
    resource_type: str | Unset = UNSET,
    sced1_curve_mw1_from: float | Unset = UNSET,
    sced1_curve_mw1_to: float | Unset = UNSET,
    sced1_curve_price_1_from: float | Unset = UNSET,
    sced1_curve_price_1_to: float | Unset = UNSET,
    sced1_curve_mw2_from: float | Unset = UNSET,
    sced1_curve_mw2_to: float | Unset = UNSET,
    sced1_curve_price_2_from: float | Unset = UNSET,
    sced1_curve_price_2_to: float | Unset = UNSET,
    sced1_curve_mw3_from: float | Unset = UNSET,
    sced1_curve_mw3_to: float | Unset = UNSET,
    sced1_curve_price_3_from: float | Unset = UNSET,
    sced1_curve_price_3_to: float | Unset = UNSET,
    sced1_curve_mw4_from: float | Unset = UNSET,
    sced1_curve_mw4_to: float | Unset = UNSET,
    sced1_curve_price_4_from: float | Unset = UNSET,
    sced1_curve_price_4_to: float | Unset = UNSET,
    sced1_curve_mw5_from: float | Unset = UNSET,
    sced1_curve_mw5_to: float | Unset = UNSET,
    sced1_curve_price_5_from: float | Unset = UNSET,
    sced1_curve_price_5_to: float | Unset = UNSET,
    sced1_curve_mw6_from: float | Unset = UNSET,
    sced1_curve_mw6_to: float | Unset = UNSET,
    sced1_curve_price_6_from: float | Unset = UNSET,
    sced1_curve_price_6_to: float | Unset = UNSET,
    sced1_curve_mw7_from: float | Unset = UNSET,
    sced1_curve_mw7_to: float | Unset = UNSET,
    sced1_curve_price_7_from: float | Unset = UNSET,
    sced1_curve_price_7_to: float | Unset = UNSET,
    sced1_curve_mw8_from: float | Unset = UNSET,
    sced1_curve_mw8_to: float | Unset = UNSET,
    sced1_curve_price_8_from: float | Unset = UNSET,
    sced1_curve_price_8_to: float | Unset = UNSET,
    sced1_curve_mw9_from: float | Unset = UNSET,
    sced1_curve_mw9_to: float | Unset = UNSET,
    sced1_curve_price_9_from: float | Unset = UNSET,
    sced1_curve_price_9_to: float | Unset = UNSET,
    sced1_curve_mw10_from: float | Unset = UNSET,
    sced1_curve_mw10_to: float | Unset = UNSET,
    sced1_curve_price_10_from: float | Unset = UNSET,
    sced1_curve_price_10_to: float | Unset = UNSET,
    sced1_curve_mw11_from: float | Unset = UNSET,
    sced1_curve_mw11_to: float | Unset = UNSET,
    sced1_curve_price_11_from: float | Unset = UNSET,
    sced1_curve_price_11_to: float | Unset = UNSET,
    sced1_curve_mw12_from: float | Unset = UNSET,
    sced1_curve_mw12_to: float | Unset = UNSET,
    sced1_curve_price_12_from: float | Unset = UNSET,
    sced1_curve_price_12_to: float | Unset = UNSET,
    sced1_curve_mw13_from: float | Unset = UNSET,
    sced1_curve_mw13_to: float | Unset = UNSET,
    sced1_curve_price_13_from: float | Unset = UNSET,
    sced1_curve_price_13_to: float | Unset = UNSET,
    sced1_curve_mw14_from: float | Unset = UNSET,
    sced1_curve_mw14_to: float | Unset = UNSET,
    sced1_curve_price_14_from: float | Unset = UNSET,
    sced1_curve_price_14_to: float | Unset = UNSET,
    sced1_curve_mw15_from: float | Unset = UNSET,
    sced1_curve_mw15_to: float | Unset = UNSET,
    sced1_curve_price_15_from: float | Unset = UNSET,
    sced1_curve_price_15_to: float | Unset = UNSET,
    sced1_curve_mw16_from: float | Unset = UNSET,
    sced1_curve_mw16_to: float | Unset = UNSET,
    sced1_curve_price_16_from: float | Unset = UNSET,
    sced1_curve_price_16_to: float | Unset = UNSET,
    sced1_curve_mw17_from: float | Unset = UNSET,
    sced1_curve_mw17_to: float | Unset = UNSET,
    sced1_curve_price_17_from: float | Unset = UNSET,
    sced1_curve_price_17_to: float | Unset = UNSET,
    sced1_curve_mw18_from: float | Unset = UNSET,
    sced1_curve_mw18_to: float | Unset = UNSET,
    sced1_curve_price_18_from: float | Unset = UNSET,
    sced1_curve_price_18_to: float | Unset = UNSET,
    sced1_curve_mw19_from: float | Unset = UNSET,
    sced1_curve_mw19_to: float | Unset = UNSET,
    sced1_curve_price_19_from: float | Unset = UNSET,
    sced1_curve_price_19_to: float | Unset = UNSET,
    sced1_curve_mw20_from: float | Unset = UNSET,
    sced1_curve_mw20_to: float | Unset = UNSET,
    sced1_curve_price_20_from: float | Unset = UNSET,
    sced1_curve_price_20_to: float | Unset = UNSET,
    sced1_curve_mw21_from: float | Unset = UNSET,
    sced1_curve_mw21_to: float | Unset = UNSET,
    sced1_curve_price_21_from: float | Unset = UNSET,
    sced1_curve_price_21_to: float | Unset = UNSET,
    sced1_curve_mw22_from: float | Unset = UNSET,
    sced1_curve_mw22_to: float | Unset = UNSET,
    sced1_curve_price_22_from: float | Unset = UNSET,
    sced1_curve_price_22_to: float | Unset = UNSET,
    sced1_curve_mw23_from: float | Unset = UNSET,
    sced1_curve_mw23_to: float | Unset = UNSET,
    sced1_curve_price_23_from: float | Unset = UNSET,
    sced1_curve_price_23_to: float | Unset = UNSET,
    sced1_curve_mw24_from: float | Unset = UNSET,
    sced1_curve_mw24_to: float | Unset = UNSET,
    sced1_curve_price_24_from: float | Unset = UNSET,
    sced1_curve_price_24_to: float | Unset = UNSET,
    sced1_curve_mw25_from: float | Unset = UNSET,
    sced1_curve_mw25_to: float | Unset = UNSET,
    sced1_curve_price_25_from: float | Unset = UNSET,
    sced1_curve_price_25_to: float | Unset = UNSET,
    sced1_curve_mw26_from: float | Unset = UNSET,
    sced1_curve_mw26_to: float | Unset = UNSET,
    sced1_curve_price_26_from: float | Unset = UNSET,
    sced1_curve_price_26_to: float | Unset = UNSET,
    sced1_curve_mw27_from: float | Unset = UNSET,
    sced1_curve_mw27_to: float | Unset = UNSET,
    sced1_curve_price_27_from: float | Unset = UNSET,
    sced1_curve_price_27_to: float | Unset = UNSET,
    sced1_curve_mw28_from: float | Unset = UNSET,
    sced1_curve_mw28_to: float | Unset = UNSET,
    sced1_curve_price_28_from: float | Unset = UNSET,
    sced1_curve_price_28_to: float | Unset = UNSET,
    sced1_curve_mw29_from: float | Unset = UNSET,
    sced1_curve_mw29_to: float | Unset = UNSET,
    sced1_curve_price_29_from: float | Unset = UNSET,
    sced1_curve_price_29_to: float | Unset = UNSET,
    sced1_curve_mw30_from: float | Unset = UNSET,
    sced1_curve_mw30_to: float | Unset = UNSET,
    sced1_curve_price_30_from: float | Unset = UNSET,
    sced1_curve_price_30_to: float | Unset = UNSET,
    sced1_curve_mw31_from: float | Unset = UNSET,
    sced1_curve_mw31_to: float | Unset = UNSET,
    sced1_curve_price_31_from: float | Unset = UNSET,
    sced1_curve_price_31_to: float | Unset = UNSET,
    sced1_curve_mw32_from: float | Unset = UNSET,
    sced1_curve_mw32_to: float | Unset = UNSET,
    sced1_curve_price_32_from: float | Unset = UNSET,
    sced1_curve_price_32_to: float | Unset = UNSET,
    sced1_curve_mw33_from: float | Unset = UNSET,
    sced1_curve_mw33_to: float | Unset = UNSET,
    sced1_curve_price_33_from: float | Unset = UNSET,
    sced1_curve_price_33_to: float | Unset = UNSET,
    sced1_curve_mw34_from: float | Unset = UNSET,
    sced1_curve_mw34_to: float | Unset = UNSET,
    sced1_curve_price_34_from: float | Unset = UNSET,
    sced1_curve_price_34_to: float | Unset = UNSET,
    sced1_curve_mw35_from: float | Unset = UNSET,
    sced1_curve_mw35_to: float | Unset = UNSET,
    sced1_curve_price_35_from: float | Unset = UNSET,
    sced1_curve_price_35_to: float | Unset = UNSET,
    sced2_curve_mw1_from: float | Unset = UNSET,
    sced2_curve_mw1_to: float | Unset = UNSET,
    sced2_curve_price_1_from: float | Unset = UNSET,
    sced2_curve_price_1_to: float | Unset = UNSET,
    sced2_curve_mw2_from: float | Unset = UNSET,
    sced2_curve_mw2_to: float | Unset = UNSET,
    sced2_curve_price_2_from: float | Unset = UNSET,
    sced2_curve_price_2_to: float | Unset = UNSET,
    sced2_curve_mw3_from: float | Unset = UNSET,
    sced2_curve_mw3_to: float | Unset = UNSET,
    sced2_curve_price_3_from: float | Unset = UNSET,
    sced2_curve_price_3_to: float | Unset = UNSET,
    sced2_curve_mw4_from: float | Unset = UNSET,
    sced2_curve_mw4_to: float | Unset = UNSET,
    sced2_curve_price_4_from: float | Unset = UNSET,
    sced2_curve_price_4_to: float | Unset = UNSET,
    sced2_curve_mw5_from: float | Unset = UNSET,
    sced2_curve_mw5_to: float | Unset = UNSET,
    sced2_curve_price_5_from: float | Unset = UNSET,
    sced2_curve_price_5_to: float | Unset = UNSET,
    sced2_curve_mw6_from: float | Unset = UNSET,
    sced2_curve_mw6_to: float | Unset = UNSET,
    sced2_curve_price_6_from: float | Unset = UNSET,
    sced2_curve_price_6_to: float | Unset = UNSET,
    sced2_curve_mw7_from: float | Unset = UNSET,
    sced2_curve_mw7_to: float | Unset = UNSET,
    sced2_curve_price_7_from: float | Unset = UNSET,
    sced2_curve_price_7_to: float | Unset = UNSET,
    sced2_curve_mw8_from: float | Unset = UNSET,
    sced2_curve_mw8_to: float | Unset = UNSET,
    sced2_curve_price_8_from: float | Unset = UNSET,
    sced2_curve_price_8_to: float | Unset = UNSET,
    page: int | Unset = UNSET,
    size: int | Unset = UNSET,
    sort: str | Unset = UNSET,
    dir_: str | Unset = UNSET,
) -> Exception_ | Report | None:
    """60 Day SCED Gen Resource Data

     60 Day SCED Gen Resource Data

    Args:
        sced2_curve_mw9_from (float | Unset):
        sced2_curve_mw9_to (float | Unset):
        sced2_curve_price_9_from (float | Unset):
        sced2_curve_price_9_to (float | Unset):
        sced2_curve_mw10_from (float | Unset):
        sced2_curve_mw10_to (float | Unset):
        sced2_curve_price_10_from (float | Unset):
        sced2_curve_price_10_to (float | Unset):
        sced2_curve_mw11_from (float | Unset):
        sced2_curve_mw11_to (float | Unset):
        sced2_curve_price_11_from (float | Unset):
        sced2_curve_price_11_to (float | Unset):
        sced2_curve_mw12_from (float | Unset):
        sced2_curve_mw12_to (float | Unset):
        sced2_curve_price_12_from (float | Unset):
        sced2_curve_price_12_to (float | Unset):
        sced2_curve_mw13_from (float | Unset):
        sced2_curve_mw13_to (float | Unset):
        sced2_curve_price_13_from (float | Unset):
        sced2_curve_price_13_to (float | Unset):
        sced2_curve_mw14_from (float | Unset):
        sced2_curve_mw14_to (float | Unset):
        sced2_curve_price_14_from (float | Unset):
        sced2_curve_price_14_to (float | Unset):
        sced2_curve_mw15_from (float | Unset):
        sced2_curve_mw15_to (float | Unset):
        sced2_curve_price_15_from (float | Unset):
        sced2_curve_price_15_to (float | Unset):
        sced2_curve_mw16_from (float | Unset):
        sced2_curve_mw16_to (float | Unset):
        sced2_curve_price_16_from (float | Unset):
        sced2_curve_price_16_to (float | Unset):
        sced2_curve_mw17_from (float | Unset):
        sced2_curve_mw17_to (float | Unset):
        sced2_curve_price_17_from (float | Unset):
        sced2_curve_price_17_to (float | Unset):
        sced2_curve_mw18_from (float | Unset):
        sced2_curve_mw18_to (float | Unset):
        sced2_curve_price_18_from (float | Unset):
        sced2_curve_price_18_to (float | Unset):
        sced2_curve_mw19_from (float | Unset):
        sced2_curve_mw19_to (float | Unset):
        sced2_curve_price_19_from (float | Unset):
        sced2_curve_price_19_to (float | Unset):
        sced2_curve_mw20_from (float | Unset):
        sced2_curve_mw20_to (float | Unset):
        sced2_curve_price_20_from (float | Unset):
        sced2_curve_price_20_to (float | Unset):
        sced2_curve_mw21_from (float | Unset):
        sced2_curve_mw21_to (float | Unset):
        sced2_curve_price_21_from (float | Unset):
        sced2_curve_price_21_to (float | Unset):
        sced2_curve_mw22_from (float | Unset):
        sced2_curve_mw22_to (float | Unset):
        sced2_curve_price_22_from (float | Unset):
        sced2_curve_price_22_to (float | Unset):
        sced2_curve_mw23_from (float | Unset):
        sced2_curve_mw23_to (float | Unset):
        sced2_curve_price_23_from (float | Unset):
        sced2_curve_price_23_to (float | Unset):
        sced2_curve_mw24_from (float | Unset):
        sced2_curve_mw24_to (float | Unset):
        sced2_curve_price_24_from (float | Unset):
        sced2_curve_price_24_to (float | Unset):
        sced2_curve_mw25_from (float | Unset):
        sced2_curve_mw25_to (float | Unset):
        sced2_curve_price_25_from (float | Unset):
        sced2_curve_price_25_to (float | Unset):
        sced2_curve_mw26_from (float | Unset):
        sced2_curve_mw26_to (float | Unset):
        sced2_curve_price_26_from (float | Unset):
        sced2_curve_price_26_to (float | Unset):
        sced2_curve_mw27_from (float | Unset):
        sced2_curve_mw27_to (float | Unset):
        sced2_curve_price_27_from (float | Unset):
        sced2_curve_price_27_to (float | Unset):
        sced2_curve_mw28_from (float | Unset):
        sced2_curve_mw28_to (float | Unset):
        sced2_curve_price_28_from (float | Unset):
        sced2_curve_price_28_to (float | Unset):
        sced2_curve_mw29_from (float | Unset):
        sced2_curve_mw29_to (float | Unset):
        sced2_curve_price_29_from (float | Unset):
        sced2_curve_price_29_to (float | Unset):
        sced2_curve_mw30_from (float | Unset):
        sced2_curve_mw30_to (float | Unset):
        sced2_curve_price_30_from (float | Unset):
        sced2_curve_price_30_to (float | Unset):
        sced2_curve_mw31_from (float | Unset):
        sced2_curve_mw31_to (float | Unset):
        sced2_curve_price_31_from (float | Unset):
        sced2_curve_price_31_to (float | Unset):
        sced2_curve_mw32_from (float | Unset):
        sced2_curve_mw32_to (float | Unset):
        sced2_curve_price_32_from (float | Unset):
        sced2_curve_price_32_to (float | Unset):
        sced2_curve_mw33_from (float | Unset):
        sced2_curve_mw33_to (float | Unset):
        sced2_curve_price_33_from (float | Unset):
        sced2_curve_price_33_to (float | Unset):
        sced2_curve_mw34_from (float | Unset):
        sced2_curve_mw34_to (float | Unset):
        sced2_curve_price_34_from (float | Unset):
        sced2_curve_price_34_to (float | Unset):
        sced2_curve_mw35_from (float | Unset):
        sced2_curve_mw35_to (float | Unset):
        sced2_curve_price_35_from (float | Unset):
        sced2_curve_price_35_to (float | Unset):
        output_schedule_from (float | Unset):
        output_schedule_to (float | Unset):
        hsl_from (float | Unset):
        hsl_to (float | Unset):
        hasl_from (float | Unset):
        hasl_to (float | Unset):
        hdl_from (float | Unset):
        hdl_to (float | Unset):
        lsl_from (float | Unset):
        lsl_to (float | Unset):
        lasl_from (float | Unset):
        lasl_to (float | Unset):
        ldl_from (float | Unset):
        ldl_to (float | Unset):
        telemetered_resource_status (str | Unset):
        base_point_from (float | Unset):
        base_point_to (float | Unset):
        telemetered_net_output_from (float | Unset):
        telemetered_net_output_to (float | Unset):
        asregup_from (float | Unset):
        asregup_to (float | Unset):
        asregdn_from (float | Unset):
        asregdn_to (float | Unset):
        asrrs_from (float | Unset):
        asrrs_to (float | Unset):
        asrrsffr_from (float | Unset):
        asrrsffr_to (float | Unset):
        asnsrs_from (float | Unset):
        asnsrs_to (float | Unset):
        bid_type (str | Unset):
        start_up_cold_offer_from (float | Unset):
        start_up_cold_offer_to (float | Unset):
        start_up_hot_offer_from (float | Unset):
        start_up_hot_offer_to (float | Unset):
        start_up_inter_offer_from (float | Unset):
        start_up_inter_offer_to (float | Unset):
        min_gen_cost_from (float | Unset):
        min_gen_cost_to (float | Unset):
        submitted_tpomw1_from (float | Unset):
        submitted_tpomw1_to (float | Unset):
        submitted_tpo_price_1_from (float | Unset):
        submitted_tpo_price_1_to (float | Unset):
        submitted_tpomw2_from (float | Unset):
        submitted_tpomw2_to (float | Unset):
        submitted_tpo_price_2_from (float | Unset):
        submitted_tpo_price_2_to (float | Unset):
        submitted_tpomw3_from (float | Unset):
        submitted_tpomw3_to (float | Unset):
        submitted_tpo_price_3_from (float | Unset):
        submitted_tpo_price_3_to (float | Unset):
        submitted_tpomw4_from (float | Unset):
        submitted_tpomw4_to (float | Unset):
        submitted_tpo_price_4_from (float | Unset):
        submitted_tpo_price_4_to (float | Unset):
        submitted_tpomw5_from (float | Unset):
        submitted_tpomw5_to (float | Unset):
        submitted_tpo_price_5_from (float | Unset):
        submitted_tpo_price_5_to (float | Unset):
        submitted_tpomw6_from (float | Unset):
        submitted_tpomw6_to (float | Unset):
        submitted_tpo_price_6_from (float | Unset):
        submitted_tpo_price_6_to (float | Unset):
        submitted_tpomw7_from (float | Unset):
        submitted_tpomw7_to (float | Unset):
        submitted_tpo_price_7_from (float | Unset):
        submitted_tpo_price_7_to (float | Unset):
        submitted_tpomw8_from (float | Unset):
        submitted_tpomw8_to (float | Unset):
        submitted_tpo_price_8_from (float | Unset):
        submitted_tpo_price_8_to (float | Unset):
        submitted_tpomw9_from (float | Unset):
        submitted_tpomw9_to (float | Unset):
        submitted_tpo_price_9_from (float | Unset):
        submitted_tpo_price_9_to (float | Unset):
        submitted_tpomw10_from (float | Unset):
        submitted_tpomw10_to (float | Unset):
        submitted_tpo_price_10_from (float | Unset):
        submitted_tpo_price_10_to (float | Unset):
        proxy_extension (str | Unset):
        sced_timestamp_from (str | Unset):
        sced_timestamp_to (str | Unset):
        repeat_hour_flag (bool | Unset):
        qse_name (str | Unset):
        dme_name (str | Unset):
        resource_name (str | Unset):
        resource_type (str | Unset):
        sced1_curve_mw1_from (float | Unset):
        sced1_curve_mw1_to (float | Unset):
        sced1_curve_price_1_from (float | Unset):
        sced1_curve_price_1_to (float | Unset):
        sced1_curve_mw2_from (float | Unset):
        sced1_curve_mw2_to (float | Unset):
        sced1_curve_price_2_from (float | Unset):
        sced1_curve_price_2_to (float | Unset):
        sced1_curve_mw3_from (float | Unset):
        sced1_curve_mw3_to (float | Unset):
        sced1_curve_price_3_from (float | Unset):
        sced1_curve_price_3_to (float | Unset):
        sced1_curve_mw4_from (float | Unset):
        sced1_curve_mw4_to (float | Unset):
        sced1_curve_price_4_from (float | Unset):
        sced1_curve_price_4_to (float | Unset):
        sced1_curve_mw5_from (float | Unset):
        sced1_curve_mw5_to (float | Unset):
        sced1_curve_price_5_from (float | Unset):
        sced1_curve_price_5_to (float | Unset):
        sced1_curve_mw6_from (float | Unset):
        sced1_curve_mw6_to (float | Unset):
        sced1_curve_price_6_from (float | Unset):
        sced1_curve_price_6_to (float | Unset):
        sced1_curve_mw7_from (float | Unset):
        sced1_curve_mw7_to (float | Unset):
        sced1_curve_price_7_from (float | Unset):
        sced1_curve_price_7_to (float | Unset):
        sced1_curve_mw8_from (float | Unset):
        sced1_curve_mw8_to (float | Unset):
        sced1_curve_price_8_from (float | Unset):
        sced1_curve_price_8_to (float | Unset):
        sced1_curve_mw9_from (float | Unset):
        sced1_curve_mw9_to (float | Unset):
        sced1_curve_price_9_from (float | Unset):
        sced1_curve_price_9_to (float | Unset):
        sced1_curve_mw10_from (float | Unset):
        sced1_curve_mw10_to (float | Unset):
        sced1_curve_price_10_from (float | Unset):
        sced1_curve_price_10_to (float | Unset):
        sced1_curve_mw11_from (float | Unset):
        sced1_curve_mw11_to (float | Unset):
        sced1_curve_price_11_from (float | Unset):
        sced1_curve_price_11_to (float | Unset):
        sced1_curve_mw12_from (float | Unset):
        sced1_curve_mw12_to (float | Unset):
        sced1_curve_price_12_from (float | Unset):
        sced1_curve_price_12_to (float | Unset):
        sced1_curve_mw13_from (float | Unset):
        sced1_curve_mw13_to (float | Unset):
        sced1_curve_price_13_from (float | Unset):
        sced1_curve_price_13_to (float | Unset):
        sced1_curve_mw14_from (float | Unset):
        sced1_curve_mw14_to (float | Unset):
        sced1_curve_price_14_from (float | Unset):
        sced1_curve_price_14_to (float | Unset):
        sced1_curve_mw15_from (float | Unset):
        sced1_curve_mw15_to (float | Unset):
        sced1_curve_price_15_from (float | Unset):
        sced1_curve_price_15_to (float | Unset):
        sced1_curve_mw16_from (float | Unset):
        sced1_curve_mw16_to (float | Unset):
        sced1_curve_price_16_from (float | Unset):
        sced1_curve_price_16_to (float | Unset):
        sced1_curve_mw17_from (float | Unset):
        sced1_curve_mw17_to (float | Unset):
        sced1_curve_price_17_from (float | Unset):
        sced1_curve_price_17_to (float | Unset):
        sced1_curve_mw18_from (float | Unset):
        sced1_curve_mw18_to (float | Unset):
        sced1_curve_price_18_from (float | Unset):
        sced1_curve_price_18_to (float | Unset):
        sced1_curve_mw19_from (float | Unset):
        sced1_curve_mw19_to (float | Unset):
        sced1_curve_price_19_from (float | Unset):
        sced1_curve_price_19_to (float | Unset):
        sced1_curve_mw20_from (float | Unset):
        sced1_curve_mw20_to (float | Unset):
        sced1_curve_price_20_from (float | Unset):
        sced1_curve_price_20_to (float | Unset):
        sced1_curve_mw21_from (float | Unset):
        sced1_curve_mw21_to (float | Unset):
        sced1_curve_price_21_from (float | Unset):
        sced1_curve_price_21_to (float | Unset):
        sced1_curve_mw22_from (float | Unset):
        sced1_curve_mw22_to (float | Unset):
        sced1_curve_price_22_from (float | Unset):
        sced1_curve_price_22_to (float | Unset):
        sced1_curve_mw23_from (float | Unset):
        sced1_curve_mw23_to (float | Unset):
        sced1_curve_price_23_from (float | Unset):
        sced1_curve_price_23_to (float | Unset):
        sced1_curve_mw24_from (float | Unset):
        sced1_curve_mw24_to (float | Unset):
        sced1_curve_price_24_from (float | Unset):
        sced1_curve_price_24_to (float | Unset):
        sced1_curve_mw25_from (float | Unset):
        sced1_curve_mw25_to (float | Unset):
        sced1_curve_price_25_from (float | Unset):
        sced1_curve_price_25_to (float | Unset):
        sced1_curve_mw26_from (float | Unset):
        sced1_curve_mw26_to (float | Unset):
        sced1_curve_price_26_from (float | Unset):
        sced1_curve_price_26_to (float | Unset):
        sced1_curve_mw27_from (float | Unset):
        sced1_curve_mw27_to (float | Unset):
        sced1_curve_price_27_from (float | Unset):
        sced1_curve_price_27_to (float | Unset):
        sced1_curve_mw28_from (float | Unset):
        sced1_curve_mw28_to (float | Unset):
        sced1_curve_price_28_from (float | Unset):
        sced1_curve_price_28_to (float | Unset):
        sced1_curve_mw29_from (float | Unset):
        sced1_curve_mw29_to (float | Unset):
        sced1_curve_price_29_from (float | Unset):
        sced1_curve_price_29_to (float | Unset):
        sced1_curve_mw30_from (float | Unset):
        sced1_curve_mw30_to (float | Unset):
        sced1_curve_price_30_from (float | Unset):
        sced1_curve_price_30_to (float | Unset):
        sced1_curve_mw31_from (float | Unset):
        sced1_curve_mw31_to (float | Unset):
        sced1_curve_price_31_from (float | Unset):
        sced1_curve_price_31_to (float | Unset):
        sced1_curve_mw32_from (float | Unset):
        sced1_curve_mw32_to (float | Unset):
        sced1_curve_price_32_from (float | Unset):
        sced1_curve_price_32_to (float | Unset):
        sced1_curve_mw33_from (float | Unset):
        sced1_curve_mw33_to (float | Unset):
        sced1_curve_price_33_from (float | Unset):
        sced1_curve_price_33_to (float | Unset):
        sced1_curve_mw34_from (float | Unset):
        sced1_curve_mw34_to (float | Unset):
        sced1_curve_price_34_from (float | Unset):
        sced1_curve_price_34_to (float | Unset):
        sced1_curve_mw35_from (float | Unset):
        sced1_curve_mw35_to (float | Unset):
        sced1_curve_price_35_from (float | Unset):
        sced1_curve_price_35_to (float | Unset):
        sced2_curve_mw1_from (float | Unset):
        sced2_curve_mw1_to (float | Unset):
        sced2_curve_price_1_from (float | Unset):
        sced2_curve_price_1_to (float | Unset):
        sced2_curve_mw2_from (float | Unset):
        sced2_curve_mw2_to (float | Unset):
        sced2_curve_price_2_from (float | Unset):
        sced2_curve_price_2_to (float | Unset):
        sced2_curve_mw3_from (float | Unset):
        sced2_curve_mw3_to (float | Unset):
        sced2_curve_price_3_from (float | Unset):
        sced2_curve_price_3_to (float | Unset):
        sced2_curve_mw4_from (float | Unset):
        sced2_curve_mw4_to (float | Unset):
        sced2_curve_price_4_from (float | Unset):
        sced2_curve_price_4_to (float | Unset):
        sced2_curve_mw5_from (float | Unset):
        sced2_curve_mw5_to (float | Unset):
        sced2_curve_price_5_from (float | Unset):
        sced2_curve_price_5_to (float | Unset):
        sced2_curve_mw6_from (float | Unset):
        sced2_curve_mw6_to (float | Unset):
        sced2_curve_price_6_from (float | Unset):
        sced2_curve_price_6_to (float | Unset):
        sced2_curve_mw7_from (float | Unset):
        sced2_curve_mw7_to (float | Unset):
        sced2_curve_price_7_from (float | Unset):
        sced2_curve_price_7_to (float | Unset):
        sced2_curve_mw8_from (float | Unset):
        sced2_curve_mw8_to (float | Unset):
        sced2_curve_price_8_from (float | Unset):
        sced2_curve_price_8_to (float | Unset):
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
        sced2_curve_mw9_from=sced2_curve_mw9_from,
        sced2_curve_mw9_to=sced2_curve_mw9_to,
        sced2_curve_price_9_from=sced2_curve_price_9_from,
        sced2_curve_price_9_to=sced2_curve_price_9_to,
        sced2_curve_mw10_from=sced2_curve_mw10_from,
        sced2_curve_mw10_to=sced2_curve_mw10_to,
        sced2_curve_price_10_from=sced2_curve_price_10_from,
        sced2_curve_price_10_to=sced2_curve_price_10_to,
        sced2_curve_mw11_from=sced2_curve_mw11_from,
        sced2_curve_mw11_to=sced2_curve_mw11_to,
        sced2_curve_price_11_from=sced2_curve_price_11_from,
        sced2_curve_price_11_to=sced2_curve_price_11_to,
        sced2_curve_mw12_from=sced2_curve_mw12_from,
        sced2_curve_mw12_to=sced2_curve_mw12_to,
        sced2_curve_price_12_from=sced2_curve_price_12_from,
        sced2_curve_price_12_to=sced2_curve_price_12_to,
        sced2_curve_mw13_from=sced2_curve_mw13_from,
        sced2_curve_mw13_to=sced2_curve_mw13_to,
        sced2_curve_price_13_from=sced2_curve_price_13_from,
        sced2_curve_price_13_to=sced2_curve_price_13_to,
        sced2_curve_mw14_from=sced2_curve_mw14_from,
        sced2_curve_mw14_to=sced2_curve_mw14_to,
        sced2_curve_price_14_from=sced2_curve_price_14_from,
        sced2_curve_price_14_to=sced2_curve_price_14_to,
        sced2_curve_mw15_from=sced2_curve_mw15_from,
        sced2_curve_mw15_to=sced2_curve_mw15_to,
        sced2_curve_price_15_from=sced2_curve_price_15_from,
        sced2_curve_price_15_to=sced2_curve_price_15_to,
        sced2_curve_mw16_from=sced2_curve_mw16_from,
        sced2_curve_mw16_to=sced2_curve_mw16_to,
        sced2_curve_price_16_from=sced2_curve_price_16_from,
        sced2_curve_price_16_to=sced2_curve_price_16_to,
        sced2_curve_mw17_from=sced2_curve_mw17_from,
        sced2_curve_mw17_to=sced2_curve_mw17_to,
        sced2_curve_price_17_from=sced2_curve_price_17_from,
        sced2_curve_price_17_to=sced2_curve_price_17_to,
        sced2_curve_mw18_from=sced2_curve_mw18_from,
        sced2_curve_mw18_to=sced2_curve_mw18_to,
        sced2_curve_price_18_from=sced2_curve_price_18_from,
        sced2_curve_price_18_to=sced2_curve_price_18_to,
        sced2_curve_mw19_from=sced2_curve_mw19_from,
        sced2_curve_mw19_to=sced2_curve_mw19_to,
        sced2_curve_price_19_from=sced2_curve_price_19_from,
        sced2_curve_price_19_to=sced2_curve_price_19_to,
        sced2_curve_mw20_from=sced2_curve_mw20_from,
        sced2_curve_mw20_to=sced2_curve_mw20_to,
        sced2_curve_price_20_from=sced2_curve_price_20_from,
        sced2_curve_price_20_to=sced2_curve_price_20_to,
        sced2_curve_mw21_from=sced2_curve_mw21_from,
        sced2_curve_mw21_to=sced2_curve_mw21_to,
        sced2_curve_price_21_from=sced2_curve_price_21_from,
        sced2_curve_price_21_to=sced2_curve_price_21_to,
        sced2_curve_mw22_from=sced2_curve_mw22_from,
        sced2_curve_mw22_to=sced2_curve_mw22_to,
        sced2_curve_price_22_from=sced2_curve_price_22_from,
        sced2_curve_price_22_to=sced2_curve_price_22_to,
        sced2_curve_mw23_from=sced2_curve_mw23_from,
        sced2_curve_mw23_to=sced2_curve_mw23_to,
        sced2_curve_price_23_from=sced2_curve_price_23_from,
        sced2_curve_price_23_to=sced2_curve_price_23_to,
        sced2_curve_mw24_from=sced2_curve_mw24_from,
        sced2_curve_mw24_to=sced2_curve_mw24_to,
        sced2_curve_price_24_from=sced2_curve_price_24_from,
        sced2_curve_price_24_to=sced2_curve_price_24_to,
        sced2_curve_mw25_from=sced2_curve_mw25_from,
        sced2_curve_mw25_to=sced2_curve_mw25_to,
        sced2_curve_price_25_from=sced2_curve_price_25_from,
        sced2_curve_price_25_to=sced2_curve_price_25_to,
        sced2_curve_mw26_from=sced2_curve_mw26_from,
        sced2_curve_mw26_to=sced2_curve_mw26_to,
        sced2_curve_price_26_from=sced2_curve_price_26_from,
        sced2_curve_price_26_to=sced2_curve_price_26_to,
        sced2_curve_mw27_from=sced2_curve_mw27_from,
        sced2_curve_mw27_to=sced2_curve_mw27_to,
        sced2_curve_price_27_from=sced2_curve_price_27_from,
        sced2_curve_price_27_to=sced2_curve_price_27_to,
        sced2_curve_mw28_from=sced2_curve_mw28_from,
        sced2_curve_mw28_to=sced2_curve_mw28_to,
        sced2_curve_price_28_from=sced2_curve_price_28_from,
        sced2_curve_price_28_to=sced2_curve_price_28_to,
        sced2_curve_mw29_from=sced2_curve_mw29_from,
        sced2_curve_mw29_to=sced2_curve_mw29_to,
        sced2_curve_price_29_from=sced2_curve_price_29_from,
        sced2_curve_price_29_to=sced2_curve_price_29_to,
        sced2_curve_mw30_from=sced2_curve_mw30_from,
        sced2_curve_mw30_to=sced2_curve_mw30_to,
        sced2_curve_price_30_from=sced2_curve_price_30_from,
        sced2_curve_price_30_to=sced2_curve_price_30_to,
        sced2_curve_mw31_from=sced2_curve_mw31_from,
        sced2_curve_mw31_to=sced2_curve_mw31_to,
        sced2_curve_price_31_from=sced2_curve_price_31_from,
        sced2_curve_price_31_to=sced2_curve_price_31_to,
        sced2_curve_mw32_from=sced2_curve_mw32_from,
        sced2_curve_mw32_to=sced2_curve_mw32_to,
        sced2_curve_price_32_from=sced2_curve_price_32_from,
        sced2_curve_price_32_to=sced2_curve_price_32_to,
        sced2_curve_mw33_from=sced2_curve_mw33_from,
        sced2_curve_mw33_to=sced2_curve_mw33_to,
        sced2_curve_price_33_from=sced2_curve_price_33_from,
        sced2_curve_price_33_to=sced2_curve_price_33_to,
        sced2_curve_mw34_from=sced2_curve_mw34_from,
        sced2_curve_mw34_to=sced2_curve_mw34_to,
        sced2_curve_price_34_from=sced2_curve_price_34_from,
        sced2_curve_price_34_to=sced2_curve_price_34_to,
        sced2_curve_mw35_from=sced2_curve_mw35_from,
        sced2_curve_mw35_to=sced2_curve_mw35_to,
        sced2_curve_price_35_from=sced2_curve_price_35_from,
        sced2_curve_price_35_to=sced2_curve_price_35_to,
        output_schedule_from=output_schedule_from,
        output_schedule_to=output_schedule_to,
        hsl_from=hsl_from,
        hsl_to=hsl_to,
        hasl_from=hasl_from,
        hasl_to=hasl_to,
        hdl_from=hdl_from,
        hdl_to=hdl_to,
        lsl_from=lsl_from,
        lsl_to=lsl_to,
        lasl_from=lasl_from,
        lasl_to=lasl_to,
        ldl_from=ldl_from,
        ldl_to=ldl_to,
        telemetered_resource_status=telemetered_resource_status,
        base_point_from=base_point_from,
        base_point_to=base_point_to,
        telemetered_net_output_from=telemetered_net_output_from,
        telemetered_net_output_to=telemetered_net_output_to,
        asregup_from=asregup_from,
        asregup_to=asregup_to,
        asregdn_from=asregdn_from,
        asregdn_to=asregdn_to,
        asrrs_from=asrrs_from,
        asrrs_to=asrrs_to,
        asrrsffr_from=asrrsffr_from,
        asrrsffr_to=asrrsffr_to,
        asnsrs_from=asnsrs_from,
        asnsrs_to=asnsrs_to,
        bid_type=bid_type,
        start_up_cold_offer_from=start_up_cold_offer_from,
        start_up_cold_offer_to=start_up_cold_offer_to,
        start_up_hot_offer_from=start_up_hot_offer_from,
        start_up_hot_offer_to=start_up_hot_offer_to,
        start_up_inter_offer_from=start_up_inter_offer_from,
        start_up_inter_offer_to=start_up_inter_offer_to,
        min_gen_cost_from=min_gen_cost_from,
        min_gen_cost_to=min_gen_cost_to,
        submitted_tpomw1_from=submitted_tpomw1_from,
        submitted_tpomw1_to=submitted_tpomw1_to,
        submitted_tpo_price_1_from=submitted_tpo_price_1_from,
        submitted_tpo_price_1_to=submitted_tpo_price_1_to,
        submitted_tpomw2_from=submitted_tpomw2_from,
        submitted_tpomw2_to=submitted_tpomw2_to,
        submitted_tpo_price_2_from=submitted_tpo_price_2_from,
        submitted_tpo_price_2_to=submitted_tpo_price_2_to,
        submitted_tpomw3_from=submitted_tpomw3_from,
        submitted_tpomw3_to=submitted_tpomw3_to,
        submitted_tpo_price_3_from=submitted_tpo_price_3_from,
        submitted_tpo_price_3_to=submitted_tpo_price_3_to,
        submitted_tpomw4_from=submitted_tpomw4_from,
        submitted_tpomw4_to=submitted_tpomw4_to,
        submitted_tpo_price_4_from=submitted_tpo_price_4_from,
        submitted_tpo_price_4_to=submitted_tpo_price_4_to,
        submitted_tpomw5_from=submitted_tpomw5_from,
        submitted_tpomw5_to=submitted_tpomw5_to,
        submitted_tpo_price_5_from=submitted_tpo_price_5_from,
        submitted_tpo_price_5_to=submitted_tpo_price_5_to,
        submitted_tpomw6_from=submitted_tpomw6_from,
        submitted_tpomw6_to=submitted_tpomw6_to,
        submitted_tpo_price_6_from=submitted_tpo_price_6_from,
        submitted_tpo_price_6_to=submitted_tpo_price_6_to,
        submitted_tpomw7_from=submitted_tpomw7_from,
        submitted_tpomw7_to=submitted_tpomw7_to,
        submitted_tpo_price_7_from=submitted_tpo_price_7_from,
        submitted_tpo_price_7_to=submitted_tpo_price_7_to,
        submitted_tpomw8_from=submitted_tpomw8_from,
        submitted_tpomw8_to=submitted_tpomw8_to,
        submitted_tpo_price_8_from=submitted_tpo_price_8_from,
        submitted_tpo_price_8_to=submitted_tpo_price_8_to,
        submitted_tpomw9_from=submitted_tpomw9_from,
        submitted_tpomw9_to=submitted_tpomw9_to,
        submitted_tpo_price_9_from=submitted_tpo_price_9_from,
        submitted_tpo_price_9_to=submitted_tpo_price_9_to,
        submitted_tpomw10_from=submitted_tpomw10_from,
        submitted_tpomw10_to=submitted_tpomw10_to,
        submitted_tpo_price_10_from=submitted_tpo_price_10_from,
        submitted_tpo_price_10_to=submitted_tpo_price_10_to,
        proxy_extension=proxy_extension,
        sced_timestamp_from=sced_timestamp_from,
        sced_timestamp_to=sced_timestamp_to,
        repeat_hour_flag=repeat_hour_flag,
        qse_name=qse_name,
        dme_name=dme_name,
        resource_name=resource_name,
        resource_type=resource_type,
        sced1_curve_mw1_from=sced1_curve_mw1_from,
        sced1_curve_mw1_to=sced1_curve_mw1_to,
        sced1_curve_price_1_from=sced1_curve_price_1_from,
        sced1_curve_price_1_to=sced1_curve_price_1_to,
        sced1_curve_mw2_from=sced1_curve_mw2_from,
        sced1_curve_mw2_to=sced1_curve_mw2_to,
        sced1_curve_price_2_from=sced1_curve_price_2_from,
        sced1_curve_price_2_to=sced1_curve_price_2_to,
        sced1_curve_mw3_from=sced1_curve_mw3_from,
        sced1_curve_mw3_to=sced1_curve_mw3_to,
        sced1_curve_price_3_from=sced1_curve_price_3_from,
        sced1_curve_price_3_to=sced1_curve_price_3_to,
        sced1_curve_mw4_from=sced1_curve_mw4_from,
        sced1_curve_mw4_to=sced1_curve_mw4_to,
        sced1_curve_price_4_from=sced1_curve_price_4_from,
        sced1_curve_price_4_to=sced1_curve_price_4_to,
        sced1_curve_mw5_from=sced1_curve_mw5_from,
        sced1_curve_mw5_to=sced1_curve_mw5_to,
        sced1_curve_price_5_from=sced1_curve_price_5_from,
        sced1_curve_price_5_to=sced1_curve_price_5_to,
        sced1_curve_mw6_from=sced1_curve_mw6_from,
        sced1_curve_mw6_to=sced1_curve_mw6_to,
        sced1_curve_price_6_from=sced1_curve_price_6_from,
        sced1_curve_price_6_to=sced1_curve_price_6_to,
        sced1_curve_mw7_from=sced1_curve_mw7_from,
        sced1_curve_mw7_to=sced1_curve_mw7_to,
        sced1_curve_price_7_from=sced1_curve_price_7_from,
        sced1_curve_price_7_to=sced1_curve_price_7_to,
        sced1_curve_mw8_from=sced1_curve_mw8_from,
        sced1_curve_mw8_to=sced1_curve_mw8_to,
        sced1_curve_price_8_from=sced1_curve_price_8_from,
        sced1_curve_price_8_to=sced1_curve_price_8_to,
        sced1_curve_mw9_from=sced1_curve_mw9_from,
        sced1_curve_mw9_to=sced1_curve_mw9_to,
        sced1_curve_price_9_from=sced1_curve_price_9_from,
        sced1_curve_price_9_to=sced1_curve_price_9_to,
        sced1_curve_mw10_from=sced1_curve_mw10_from,
        sced1_curve_mw10_to=sced1_curve_mw10_to,
        sced1_curve_price_10_from=sced1_curve_price_10_from,
        sced1_curve_price_10_to=sced1_curve_price_10_to,
        sced1_curve_mw11_from=sced1_curve_mw11_from,
        sced1_curve_mw11_to=sced1_curve_mw11_to,
        sced1_curve_price_11_from=sced1_curve_price_11_from,
        sced1_curve_price_11_to=sced1_curve_price_11_to,
        sced1_curve_mw12_from=sced1_curve_mw12_from,
        sced1_curve_mw12_to=sced1_curve_mw12_to,
        sced1_curve_price_12_from=sced1_curve_price_12_from,
        sced1_curve_price_12_to=sced1_curve_price_12_to,
        sced1_curve_mw13_from=sced1_curve_mw13_from,
        sced1_curve_mw13_to=sced1_curve_mw13_to,
        sced1_curve_price_13_from=sced1_curve_price_13_from,
        sced1_curve_price_13_to=sced1_curve_price_13_to,
        sced1_curve_mw14_from=sced1_curve_mw14_from,
        sced1_curve_mw14_to=sced1_curve_mw14_to,
        sced1_curve_price_14_from=sced1_curve_price_14_from,
        sced1_curve_price_14_to=sced1_curve_price_14_to,
        sced1_curve_mw15_from=sced1_curve_mw15_from,
        sced1_curve_mw15_to=sced1_curve_mw15_to,
        sced1_curve_price_15_from=sced1_curve_price_15_from,
        sced1_curve_price_15_to=sced1_curve_price_15_to,
        sced1_curve_mw16_from=sced1_curve_mw16_from,
        sced1_curve_mw16_to=sced1_curve_mw16_to,
        sced1_curve_price_16_from=sced1_curve_price_16_from,
        sced1_curve_price_16_to=sced1_curve_price_16_to,
        sced1_curve_mw17_from=sced1_curve_mw17_from,
        sced1_curve_mw17_to=sced1_curve_mw17_to,
        sced1_curve_price_17_from=sced1_curve_price_17_from,
        sced1_curve_price_17_to=sced1_curve_price_17_to,
        sced1_curve_mw18_from=sced1_curve_mw18_from,
        sced1_curve_mw18_to=sced1_curve_mw18_to,
        sced1_curve_price_18_from=sced1_curve_price_18_from,
        sced1_curve_price_18_to=sced1_curve_price_18_to,
        sced1_curve_mw19_from=sced1_curve_mw19_from,
        sced1_curve_mw19_to=sced1_curve_mw19_to,
        sced1_curve_price_19_from=sced1_curve_price_19_from,
        sced1_curve_price_19_to=sced1_curve_price_19_to,
        sced1_curve_mw20_from=sced1_curve_mw20_from,
        sced1_curve_mw20_to=sced1_curve_mw20_to,
        sced1_curve_price_20_from=sced1_curve_price_20_from,
        sced1_curve_price_20_to=sced1_curve_price_20_to,
        sced1_curve_mw21_from=sced1_curve_mw21_from,
        sced1_curve_mw21_to=sced1_curve_mw21_to,
        sced1_curve_price_21_from=sced1_curve_price_21_from,
        sced1_curve_price_21_to=sced1_curve_price_21_to,
        sced1_curve_mw22_from=sced1_curve_mw22_from,
        sced1_curve_mw22_to=sced1_curve_mw22_to,
        sced1_curve_price_22_from=sced1_curve_price_22_from,
        sced1_curve_price_22_to=sced1_curve_price_22_to,
        sced1_curve_mw23_from=sced1_curve_mw23_from,
        sced1_curve_mw23_to=sced1_curve_mw23_to,
        sced1_curve_price_23_from=sced1_curve_price_23_from,
        sced1_curve_price_23_to=sced1_curve_price_23_to,
        sced1_curve_mw24_from=sced1_curve_mw24_from,
        sced1_curve_mw24_to=sced1_curve_mw24_to,
        sced1_curve_price_24_from=sced1_curve_price_24_from,
        sced1_curve_price_24_to=sced1_curve_price_24_to,
        sced1_curve_mw25_from=sced1_curve_mw25_from,
        sced1_curve_mw25_to=sced1_curve_mw25_to,
        sced1_curve_price_25_from=sced1_curve_price_25_from,
        sced1_curve_price_25_to=sced1_curve_price_25_to,
        sced1_curve_mw26_from=sced1_curve_mw26_from,
        sced1_curve_mw26_to=sced1_curve_mw26_to,
        sced1_curve_price_26_from=sced1_curve_price_26_from,
        sced1_curve_price_26_to=sced1_curve_price_26_to,
        sced1_curve_mw27_from=sced1_curve_mw27_from,
        sced1_curve_mw27_to=sced1_curve_mw27_to,
        sced1_curve_price_27_from=sced1_curve_price_27_from,
        sced1_curve_price_27_to=sced1_curve_price_27_to,
        sced1_curve_mw28_from=sced1_curve_mw28_from,
        sced1_curve_mw28_to=sced1_curve_mw28_to,
        sced1_curve_price_28_from=sced1_curve_price_28_from,
        sced1_curve_price_28_to=sced1_curve_price_28_to,
        sced1_curve_mw29_from=sced1_curve_mw29_from,
        sced1_curve_mw29_to=sced1_curve_mw29_to,
        sced1_curve_price_29_from=sced1_curve_price_29_from,
        sced1_curve_price_29_to=sced1_curve_price_29_to,
        sced1_curve_mw30_from=sced1_curve_mw30_from,
        sced1_curve_mw30_to=sced1_curve_mw30_to,
        sced1_curve_price_30_from=sced1_curve_price_30_from,
        sced1_curve_price_30_to=sced1_curve_price_30_to,
        sced1_curve_mw31_from=sced1_curve_mw31_from,
        sced1_curve_mw31_to=sced1_curve_mw31_to,
        sced1_curve_price_31_from=sced1_curve_price_31_from,
        sced1_curve_price_31_to=sced1_curve_price_31_to,
        sced1_curve_mw32_from=sced1_curve_mw32_from,
        sced1_curve_mw32_to=sced1_curve_mw32_to,
        sced1_curve_price_32_from=sced1_curve_price_32_from,
        sced1_curve_price_32_to=sced1_curve_price_32_to,
        sced1_curve_mw33_from=sced1_curve_mw33_from,
        sced1_curve_mw33_to=sced1_curve_mw33_to,
        sced1_curve_price_33_from=sced1_curve_price_33_from,
        sced1_curve_price_33_to=sced1_curve_price_33_to,
        sced1_curve_mw34_from=sced1_curve_mw34_from,
        sced1_curve_mw34_to=sced1_curve_mw34_to,
        sced1_curve_price_34_from=sced1_curve_price_34_from,
        sced1_curve_price_34_to=sced1_curve_price_34_to,
        sced1_curve_mw35_from=sced1_curve_mw35_from,
        sced1_curve_mw35_to=sced1_curve_mw35_to,
        sced1_curve_price_35_from=sced1_curve_price_35_from,
        sced1_curve_price_35_to=sced1_curve_price_35_to,
        sced2_curve_mw1_from=sced2_curve_mw1_from,
        sced2_curve_mw1_to=sced2_curve_mw1_to,
        sced2_curve_price_1_from=sced2_curve_price_1_from,
        sced2_curve_price_1_to=sced2_curve_price_1_to,
        sced2_curve_mw2_from=sced2_curve_mw2_from,
        sced2_curve_mw2_to=sced2_curve_mw2_to,
        sced2_curve_price_2_from=sced2_curve_price_2_from,
        sced2_curve_price_2_to=sced2_curve_price_2_to,
        sced2_curve_mw3_from=sced2_curve_mw3_from,
        sced2_curve_mw3_to=sced2_curve_mw3_to,
        sced2_curve_price_3_from=sced2_curve_price_3_from,
        sced2_curve_price_3_to=sced2_curve_price_3_to,
        sced2_curve_mw4_from=sced2_curve_mw4_from,
        sced2_curve_mw4_to=sced2_curve_mw4_to,
        sced2_curve_price_4_from=sced2_curve_price_4_from,
        sced2_curve_price_4_to=sced2_curve_price_4_to,
        sced2_curve_mw5_from=sced2_curve_mw5_from,
        sced2_curve_mw5_to=sced2_curve_mw5_to,
        sced2_curve_price_5_from=sced2_curve_price_5_from,
        sced2_curve_price_5_to=sced2_curve_price_5_to,
        sced2_curve_mw6_from=sced2_curve_mw6_from,
        sced2_curve_mw6_to=sced2_curve_mw6_to,
        sced2_curve_price_6_from=sced2_curve_price_6_from,
        sced2_curve_price_6_to=sced2_curve_price_6_to,
        sced2_curve_mw7_from=sced2_curve_mw7_from,
        sced2_curve_mw7_to=sced2_curve_mw7_to,
        sced2_curve_price_7_from=sced2_curve_price_7_from,
        sced2_curve_price_7_to=sced2_curve_price_7_to,
        sced2_curve_mw8_from=sced2_curve_mw8_from,
        sced2_curve_mw8_to=sced2_curve_mw8_to,
        sced2_curve_price_8_from=sced2_curve_price_8_from,
        sced2_curve_price_8_to=sced2_curve_price_8_to,
        page=page,
        size=size,
        sort=sort,
        dir_=dir_,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    sced2_curve_mw9_from: float | Unset = UNSET,
    sced2_curve_mw9_to: float | Unset = UNSET,
    sced2_curve_price_9_from: float | Unset = UNSET,
    sced2_curve_price_9_to: float | Unset = UNSET,
    sced2_curve_mw10_from: float | Unset = UNSET,
    sced2_curve_mw10_to: float | Unset = UNSET,
    sced2_curve_price_10_from: float | Unset = UNSET,
    sced2_curve_price_10_to: float | Unset = UNSET,
    sced2_curve_mw11_from: float | Unset = UNSET,
    sced2_curve_mw11_to: float | Unset = UNSET,
    sced2_curve_price_11_from: float | Unset = UNSET,
    sced2_curve_price_11_to: float | Unset = UNSET,
    sced2_curve_mw12_from: float | Unset = UNSET,
    sced2_curve_mw12_to: float | Unset = UNSET,
    sced2_curve_price_12_from: float | Unset = UNSET,
    sced2_curve_price_12_to: float | Unset = UNSET,
    sced2_curve_mw13_from: float | Unset = UNSET,
    sced2_curve_mw13_to: float | Unset = UNSET,
    sced2_curve_price_13_from: float | Unset = UNSET,
    sced2_curve_price_13_to: float | Unset = UNSET,
    sced2_curve_mw14_from: float | Unset = UNSET,
    sced2_curve_mw14_to: float | Unset = UNSET,
    sced2_curve_price_14_from: float | Unset = UNSET,
    sced2_curve_price_14_to: float | Unset = UNSET,
    sced2_curve_mw15_from: float | Unset = UNSET,
    sced2_curve_mw15_to: float | Unset = UNSET,
    sced2_curve_price_15_from: float | Unset = UNSET,
    sced2_curve_price_15_to: float | Unset = UNSET,
    sced2_curve_mw16_from: float | Unset = UNSET,
    sced2_curve_mw16_to: float | Unset = UNSET,
    sced2_curve_price_16_from: float | Unset = UNSET,
    sced2_curve_price_16_to: float | Unset = UNSET,
    sced2_curve_mw17_from: float | Unset = UNSET,
    sced2_curve_mw17_to: float | Unset = UNSET,
    sced2_curve_price_17_from: float | Unset = UNSET,
    sced2_curve_price_17_to: float | Unset = UNSET,
    sced2_curve_mw18_from: float | Unset = UNSET,
    sced2_curve_mw18_to: float | Unset = UNSET,
    sced2_curve_price_18_from: float | Unset = UNSET,
    sced2_curve_price_18_to: float | Unset = UNSET,
    sced2_curve_mw19_from: float | Unset = UNSET,
    sced2_curve_mw19_to: float | Unset = UNSET,
    sced2_curve_price_19_from: float | Unset = UNSET,
    sced2_curve_price_19_to: float | Unset = UNSET,
    sced2_curve_mw20_from: float | Unset = UNSET,
    sced2_curve_mw20_to: float | Unset = UNSET,
    sced2_curve_price_20_from: float | Unset = UNSET,
    sced2_curve_price_20_to: float | Unset = UNSET,
    sced2_curve_mw21_from: float | Unset = UNSET,
    sced2_curve_mw21_to: float | Unset = UNSET,
    sced2_curve_price_21_from: float | Unset = UNSET,
    sced2_curve_price_21_to: float | Unset = UNSET,
    sced2_curve_mw22_from: float | Unset = UNSET,
    sced2_curve_mw22_to: float | Unset = UNSET,
    sced2_curve_price_22_from: float | Unset = UNSET,
    sced2_curve_price_22_to: float | Unset = UNSET,
    sced2_curve_mw23_from: float | Unset = UNSET,
    sced2_curve_mw23_to: float | Unset = UNSET,
    sced2_curve_price_23_from: float | Unset = UNSET,
    sced2_curve_price_23_to: float | Unset = UNSET,
    sced2_curve_mw24_from: float | Unset = UNSET,
    sced2_curve_mw24_to: float | Unset = UNSET,
    sced2_curve_price_24_from: float | Unset = UNSET,
    sced2_curve_price_24_to: float | Unset = UNSET,
    sced2_curve_mw25_from: float | Unset = UNSET,
    sced2_curve_mw25_to: float | Unset = UNSET,
    sced2_curve_price_25_from: float | Unset = UNSET,
    sced2_curve_price_25_to: float | Unset = UNSET,
    sced2_curve_mw26_from: float | Unset = UNSET,
    sced2_curve_mw26_to: float | Unset = UNSET,
    sced2_curve_price_26_from: float | Unset = UNSET,
    sced2_curve_price_26_to: float | Unset = UNSET,
    sced2_curve_mw27_from: float | Unset = UNSET,
    sced2_curve_mw27_to: float | Unset = UNSET,
    sced2_curve_price_27_from: float | Unset = UNSET,
    sced2_curve_price_27_to: float | Unset = UNSET,
    sced2_curve_mw28_from: float | Unset = UNSET,
    sced2_curve_mw28_to: float | Unset = UNSET,
    sced2_curve_price_28_from: float | Unset = UNSET,
    sced2_curve_price_28_to: float | Unset = UNSET,
    sced2_curve_mw29_from: float | Unset = UNSET,
    sced2_curve_mw29_to: float | Unset = UNSET,
    sced2_curve_price_29_from: float | Unset = UNSET,
    sced2_curve_price_29_to: float | Unset = UNSET,
    sced2_curve_mw30_from: float | Unset = UNSET,
    sced2_curve_mw30_to: float | Unset = UNSET,
    sced2_curve_price_30_from: float | Unset = UNSET,
    sced2_curve_price_30_to: float | Unset = UNSET,
    sced2_curve_mw31_from: float | Unset = UNSET,
    sced2_curve_mw31_to: float | Unset = UNSET,
    sced2_curve_price_31_from: float | Unset = UNSET,
    sced2_curve_price_31_to: float | Unset = UNSET,
    sced2_curve_mw32_from: float | Unset = UNSET,
    sced2_curve_mw32_to: float | Unset = UNSET,
    sced2_curve_price_32_from: float | Unset = UNSET,
    sced2_curve_price_32_to: float | Unset = UNSET,
    sced2_curve_mw33_from: float | Unset = UNSET,
    sced2_curve_mw33_to: float | Unset = UNSET,
    sced2_curve_price_33_from: float | Unset = UNSET,
    sced2_curve_price_33_to: float | Unset = UNSET,
    sced2_curve_mw34_from: float | Unset = UNSET,
    sced2_curve_mw34_to: float | Unset = UNSET,
    sced2_curve_price_34_from: float | Unset = UNSET,
    sced2_curve_price_34_to: float | Unset = UNSET,
    sced2_curve_mw35_from: float | Unset = UNSET,
    sced2_curve_mw35_to: float | Unset = UNSET,
    sced2_curve_price_35_from: float | Unset = UNSET,
    sced2_curve_price_35_to: float | Unset = UNSET,
    output_schedule_from: float | Unset = UNSET,
    output_schedule_to: float | Unset = UNSET,
    hsl_from: float | Unset = UNSET,
    hsl_to: float | Unset = UNSET,
    hasl_from: float | Unset = UNSET,
    hasl_to: float | Unset = UNSET,
    hdl_from: float | Unset = UNSET,
    hdl_to: float | Unset = UNSET,
    lsl_from: float | Unset = UNSET,
    lsl_to: float | Unset = UNSET,
    lasl_from: float | Unset = UNSET,
    lasl_to: float | Unset = UNSET,
    ldl_from: float | Unset = UNSET,
    ldl_to: float | Unset = UNSET,
    telemetered_resource_status: str | Unset = UNSET,
    base_point_from: float | Unset = UNSET,
    base_point_to: float | Unset = UNSET,
    telemetered_net_output_from: float | Unset = UNSET,
    telemetered_net_output_to: float | Unset = UNSET,
    asregup_from: float | Unset = UNSET,
    asregup_to: float | Unset = UNSET,
    asregdn_from: float | Unset = UNSET,
    asregdn_to: float | Unset = UNSET,
    asrrs_from: float | Unset = UNSET,
    asrrs_to: float | Unset = UNSET,
    asrrsffr_from: float | Unset = UNSET,
    asrrsffr_to: float | Unset = UNSET,
    asnsrs_from: float | Unset = UNSET,
    asnsrs_to: float | Unset = UNSET,
    bid_type: str | Unset = UNSET,
    start_up_cold_offer_from: float | Unset = UNSET,
    start_up_cold_offer_to: float | Unset = UNSET,
    start_up_hot_offer_from: float | Unset = UNSET,
    start_up_hot_offer_to: float | Unset = UNSET,
    start_up_inter_offer_from: float | Unset = UNSET,
    start_up_inter_offer_to: float | Unset = UNSET,
    min_gen_cost_from: float | Unset = UNSET,
    min_gen_cost_to: float | Unset = UNSET,
    submitted_tpomw1_from: float | Unset = UNSET,
    submitted_tpomw1_to: float | Unset = UNSET,
    submitted_tpo_price_1_from: float | Unset = UNSET,
    submitted_tpo_price_1_to: float | Unset = UNSET,
    submitted_tpomw2_from: float | Unset = UNSET,
    submitted_tpomw2_to: float | Unset = UNSET,
    submitted_tpo_price_2_from: float | Unset = UNSET,
    submitted_tpo_price_2_to: float | Unset = UNSET,
    submitted_tpomw3_from: float | Unset = UNSET,
    submitted_tpomw3_to: float | Unset = UNSET,
    submitted_tpo_price_3_from: float | Unset = UNSET,
    submitted_tpo_price_3_to: float | Unset = UNSET,
    submitted_tpomw4_from: float | Unset = UNSET,
    submitted_tpomw4_to: float | Unset = UNSET,
    submitted_tpo_price_4_from: float | Unset = UNSET,
    submitted_tpo_price_4_to: float | Unset = UNSET,
    submitted_tpomw5_from: float | Unset = UNSET,
    submitted_tpomw5_to: float | Unset = UNSET,
    submitted_tpo_price_5_from: float | Unset = UNSET,
    submitted_tpo_price_5_to: float | Unset = UNSET,
    submitted_tpomw6_from: float | Unset = UNSET,
    submitted_tpomw6_to: float | Unset = UNSET,
    submitted_tpo_price_6_from: float | Unset = UNSET,
    submitted_tpo_price_6_to: float | Unset = UNSET,
    submitted_tpomw7_from: float | Unset = UNSET,
    submitted_tpomw7_to: float | Unset = UNSET,
    submitted_tpo_price_7_from: float | Unset = UNSET,
    submitted_tpo_price_7_to: float | Unset = UNSET,
    submitted_tpomw8_from: float | Unset = UNSET,
    submitted_tpomw8_to: float | Unset = UNSET,
    submitted_tpo_price_8_from: float | Unset = UNSET,
    submitted_tpo_price_8_to: float | Unset = UNSET,
    submitted_tpomw9_from: float | Unset = UNSET,
    submitted_tpomw9_to: float | Unset = UNSET,
    submitted_tpo_price_9_from: float | Unset = UNSET,
    submitted_tpo_price_9_to: float | Unset = UNSET,
    submitted_tpomw10_from: float | Unset = UNSET,
    submitted_tpomw10_to: float | Unset = UNSET,
    submitted_tpo_price_10_from: float | Unset = UNSET,
    submitted_tpo_price_10_to: float | Unset = UNSET,
    proxy_extension: str | Unset = UNSET,
    sced_timestamp_from: str | Unset = UNSET,
    sced_timestamp_to: str | Unset = UNSET,
    repeat_hour_flag: bool | Unset = UNSET,
    qse_name: str | Unset = UNSET,
    dme_name: str | Unset = UNSET,
    resource_name: str | Unset = UNSET,
    resource_type: str | Unset = UNSET,
    sced1_curve_mw1_from: float | Unset = UNSET,
    sced1_curve_mw1_to: float | Unset = UNSET,
    sced1_curve_price_1_from: float | Unset = UNSET,
    sced1_curve_price_1_to: float | Unset = UNSET,
    sced1_curve_mw2_from: float | Unset = UNSET,
    sced1_curve_mw2_to: float | Unset = UNSET,
    sced1_curve_price_2_from: float | Unset = UNSET,
    sced1_curve_price_2_to: float | Unset = UNSET,
    sced1_curve_mw3_from: float | Unset = UNSET,
    sced1_curve_mw3_to: float | Unset = UNSET,
    sced1_curve_price_3_from: float | Unset = UNSET,
    sced1_curve_price_3_to: float | Unset = UNSET,
    sced1_curve_mw4_from: float | Unset = UNSET,
    sced1_curve_mw4_to: float | Unset = UNSET,
    sced1_curve_price_4_from: float | Unset = UNSET,
    sced1_curve_price_4_to: float | Unset = UNSET,
    sced1_curve_mw5_from: float | Unset = UNSET,
    sced1_curve_mw5_to: float | Unset = UNSET,
    sced1_curve_price_5_from: float | Unset = UNSET,
    sced1_curve_price_5_to: float | Unset = UNSET,
    sced1_curve_mw6_from: float | Unset = UNSET,
    sced1_curve_mw6_to: float | Unset = UNSET,
    sced1_curve_price_6_from: float | Unset = UNSET,
    sced1_curve_price_6_to: float | Unset = UNSET,
    sced1_curve_mw7_from: float | Unset = UNSET,
    sced1_curve_mw7_to: float | Unset = UNSET,
    sced1_curve_price_7_from: float | Unset = UNSET,
    sced1_curve_price_7_to: float | Unset = UNSET,
    sced1_curve_mw8_from: float | Unset = UNSET,
    sced1_curve_mw8_to: float | Unset = UNSET,
    sced1_curve_price_8_from: float | Unset = UNSET,
    sced1_curve_price_8_to: float | Unset = UNSET,
    sced1_curve_mw9_from: float | Unset = UNSET,
    sced1_curve_mw9_to: float | Unset = UNSET,
    sced1_curve_price_9_from: float | Unset = UNSET,
    sced1_curve_price_9_to: float | Unset = UNSET,
    sced1_curve_mw10_from: float | Unset = UNSET,
    sced1_curve_mw10_to: float | Unset = UNSET,
    sced1_curve_price_10_from: float | Unset = UNSET,
    sced1_curve_price_10_to: float | Unset = UNSET,
    sced1_curve_mw11_from: float | Unset = UNSET,
    sced1_curve_mw11_to: float | Unset = UNSET,
    sced1_curve_price_11_from: float | Unset = UNSET,
    sced1_curve_price_11_to: float | Unset = UNSET,
    sced1_curve_mw12_from: float | Unset = UNSET,
    sced1_curve_mw12_to: float | Unset = UNSET,
    sced1_curve_price_12_from: float | Unset = UNSET,
    sced1_curve_price_12_to: float | Unset = UNSET,
    sced1_curve_mw13_from: float | Unset = UNSET,
    sced1_curve_mw13_to: float | Unset = UNSET,
    sced1_curve_price_13_from: float | Unset = UNSET,
    sced1_curve_price_13_to: float | Unset = UNSET,
    sced1_curve_mw14_from: float | Unset = UNSET,
    sced1_curve_mw14_to: float | Unset = UNSET,
    sced1_curve_price_14_from: float | Unset = UNSET,
    sced1_curve_price_14_to: float | Unset = UNSET,
    sced1_curve_mw15_from: float | Unset = UNSET,
    sced1_curve_mw15_to: float | Unset = UNSET,
    sced1_curve_price_15_from: float | Unset = UNSET,
    sced1_curve_price_15_to: float | Unset = UNSET,
    sced1_curve_mw16_from: float | Unset = UNSET,
    sced1_curve_mw16_to: float | Unset = UNSET,
    sced1_curve_price_16_from: float | Unset = UNSET,
    sced1_curve_price_16_to: float | Unset = UNSET,
    sced1_curve_mw17_from: float | Unset = UNSET,
    sced1_curve_mw17_to: float | Unset = UNSET,
    sced1_curve_price_17_from: float | Unset = UNSET,
    sced1_curve_price_17_to: float | Unset = UNSET,
    sced1_curve_mw18_from: float | Unset = UNSET,
    sced1_curve_mw18_to: float | Unset = UNSET,
    sced1_curve_price_18_from: float | Unset = UNSET,
    sced1_curve_price_18_to: float | Unset = UNSET,
    sced1_curve_mw19_from: float | Unset = UNSET,
    sced1_curve_mw19_to: float | Unset = UNSET,
    sced1_curve_price_19_from: float | Unset = UNSET,
    sced1_curve_price_19_to: float | Unset = UNSET,
    sced1_curve_mw20_from: float | Unset = UNSET,
    sced1_curve_mw20_to: float | Unset = UNSET,
    sced1_curve_price_20_from: float | Unset = UNSET,
    sced1_curve_price_20_to: float | Unset = UNSET,
    sced1_curve_mw21_from: float | Unset = UNSET,
    sced1_curve_mw21_to: float | Unset = UNSET,
    sced1_curve_price_21_from: float | Unset = UNSET,
    sced1_curve_price_21_to: float | Unset = UNSET,
    sced1_curve_mw22_from: float | Unset = UNSET,
    sced1_curve_mw22_to: float | Unset = UNSET,
    sced1_curve_price_22_from: float | Unset = UNSET,
    sced1_curve_price_22_to: float | Unset = UNSET,
    sced1_curve_mw23_from: float | Unset = UNSET,
    sced1_curve_mw23_to: float | Unset = UNSET,
    sced1_curve_price_23_from: float | Unset = UNSET,
    sced1_curve_price_23_to: float | Unset = UNSET,
    sced1_curve_mw24_from: float | Unset = UNSET,
    sced1_curve_mw24_to: float | Unset = UNSET,
    sced1_curve_price_24_from: float | Unset = UNSET,
    sced1_curve_price_24_to: float | Unset = UNSET,
    sced1_curve_mw25_from: float | Unset = UNSET,
    sced1_curve_mw25_to: float | Unset = UNSET,
    sced1_curve_price_25_from: float | Unset = UNSET,
    sced1_curve_price_25_to: float | Unset = UNSET,
    sced1_curve_mw26_from: float | Unset = UNSET,
    sced1_curve_mw26_to: float | Unset = UNSET,
    sced1_curve_price_26_from: float | Unset = UNSET,
    sced1_curve_price_26_to: float | Unset = UNSET,
    sced1_curve_mw27_from: float | Unset = UNSET,
    sced1_curve_mw27_to: float | Unset = UNSET,
    sced1_curve_price_27_from: float | Unset = UNSET,
    sced1_curve_price_27_to: float | Unset = UNSET,
    sced1_curve_mw28_from: float | Unset = UNSET,
    sced1_curve_mw28_to: float | Unset = UNSET,
    sced1_curve_price_28_from: float | Unset = UNSET,
    sced1_curve_price_28_to: float | Unset = UNSET,
    sced1_curve_mw29_from: float | Unset = UNSET,
    sced1_curve_mw29_to: float | Unset = UNSET,
    sced1_curve_price_29_from: float | Unset = UNSET,
    sced1_curve_price_29_to: float | Unset = UNSET,
    sced1_curve_mw30_from: float | Unset = UNSET,
    sced1_curve_mw30_to: float | Unset = UNSET,
    sced1_curve_price_30_from: float | Unset = UNSET,
    sced1_curve_price_30_to: float | Unset = UNSET,
    sced1_curve_mw31_from: float | Unset = UNSET,
    sced1_curve_mw31_to: float | Unset = UNSET,
    sced1_curve_price_31_from: float | Unset = UNSET,
    sced1_curve_price_31_to: float | Unset = UNSET,
    sced1_curve_mw32_from: float | Unset = UNSET,
    sced1_curve_mw32_to: float | Unset = UNSET,
    sced1_curve_price_32_from: float | Unset = UNSET,
    sced1_curve_price_32_to: float | Unset = UNSET,
    sced1_curve_mw33_from: float | Unset = UNSET,
    sced1_curve_mw33_to: float | Unset = UNSET,
    sced1_curve_price_33_from: float | Unset = UNSET,
    sced1_curve_price_33_to: float | Unset = UNSET,
    sced1_curve_mw34_from: float | Unset = UNSET,
    sced1_curve_mw34_to: float | Unset = UNSET,
    sced1_curve_price_34_from: float | Unset = UNSET,
    sced1_curve_price_34_to: float | Unset = UNSET,
    sced1_curve_mw35_from: float | Unset = UNSET,
    sced1_curve_mw35_to: float | Unset = UNSET,
    sced1_curve_price_35_from: float | Unset = UNSET,
    sced1_curve_price_35_to: float | Unset = UNSET,
    sced2_curve_mw1_from: float | Unset = UNSET,
    sced2_curve_mw1_to: float | Unset = UNSET,
    sced2_curve_price_1_from: float | Unset = UNSET,
    sced2_curve_price_1_to: float | Unset = UNSET,
    sced2_curve_mw2_from: float | Unset = UNSET,
    sced2_curve_mw2_to: float | Unset = UNSET,
    sced2_curve_price_2_from: float | Unset = UNSET,
    sced2_curve_price_2_to: float | Unset = UNSET,
    sced2_curve_mw3_from: float | Unset = UNSET,
    sced2_curve_mw3_to: float | Unset = UNSET,
    sced2_curve_price_3_from: float | Unset = UNSET,
    sced2_curve_price_3_to: float | Unset = UNSET,
    sced2_curve_mw4_from: float | Unset = UNSET,
    sced2_curve_mw4_to: float | Unset = UNSET,
    sced2_curve_price_4_from: float | Unset = UNSET,
    sced2_curve_price_4_to: float | Unset = UNSET,
    sced2_curve_mw5_from: float | Unset = UNSET,
    sced2_curve_mw5_to: float | Unset = UNSET,
    sced2_curve_price_5_from: float | Unset = UNSET,
    sced2_curve_price_5_to: float | Unset = UNSET,
    sced2_curve_mw6_from: float | Unset = UNSET,
    sced2_curve_mw6_to: float | Unset = UNSET,
    sced2_curve_price_6_from: float | Unset = UNSET,
    sced2_curve_price_6_to: float | Unset = UNSET,
    sced2_curve_mw7_from: float | Unset = UNSET,
    sced2_curve_mw7_to: float | Unset = UNSET,
    sced2_curve_price_7_from: float | Unset = UNSET,
    sced2_curve_price_7_to: float | Unset = UNSET,
    sced2_curve_mw8_from: float | Unset = UNSET,
    sced2_curve_mw8_to: float | Unset = UNSET,
    sced2_curve_price_8_from: float | Unset = UNSET,
    sced2_curve_price_8_to: float | Unset = UNSET,
    page: int | Unset = UNSET,
    size: int | Unset = UNSET,
    sort: str | Unset = UNSET,
    dir_: str | Unset = UNSET,
) -> Response[Exception_ | Report]:
    """60 Day SCED Gen Resource Data

     60 Day SCED Gen Resource Data

    Args:
        sced2_curve_mw9_from (float | Unset):
        sced2_curve_mw9_to (float | Unset):
        sced2_curve_price_9_from (float | Unset):
        sced2_curve_price_9_to (float | Unset):
        sced2_curve_mw10_from (float | Unset):
        sced2_curve_mw10_to (float | Unset):
        sced2_curve_price_10_from (float | Unset):
        sced2_curve_price_10_to (float | Unset):
        sced2_curve_mw11_from (float | Unset):
        sced2_curve_mw11_to (float | Unset):
        sced2_curve_price_11_from (float | Unset):
        sced2_curve_price_11_to (float | Unset):
        sced2_curve_mw12_from (float | Unset):
        sced2_curve_mw12_to (float | Unset):
        sced2_curve_price_12_from (float | Unset):
        sced2_curve_price_12_to (float | Unset):
        sced2_curve_mw13_from (float | Unset):
        sced2_curve_mw13_to (float | Unset):
        sced2_curve_price_13_from (float | Unset):
        sced2_curve_price_13_to (float | Unset):
        sced2_curve_mw14_from (float | Unset):
        sced2_curve_mw14_to (float | Unset):
        sced2_curve_price_14_from (float | Unset):
        sced2_curve_price_14_to (float | Unset):
        sced2_curve_mw15_from (float | Unset):
        sced2_curve_mw15_to (float | Unset):
        sced2_curve_price_15_from (float | Unset):
        sced2_curve_price_15_to (float | Unset):
        sced2_curve_mw16_from (float | Unset):
        sced2_curve_mw16_to (float | Unset):
        sced2_curve_price_16_from (float | Unset):
        sced2_curve_price_16_to (float | Unset):
        sced2_curve_mw17_from (float | Unset):
        sced2_curve_mw17_to (float | Unset):
        sced2_curve_price_17_from (float | Unset):
        sced2_curve_price_17_to (float | Unset):
        sced2_curve_mw18_from (float | Unset):
        sced2_curve_mw18_to (float | Unset):
        sced2_curve_price_18_from (float | Unset):
        sced2_curve_price_18_to (float | Unset):
        sced2_curve_mw19_from (float | Unset):
        sced2_curve_mw19_to (float | Unset):
        sced2_curve_price_19_from (float | Unset):
        sced2_curve_price_19_to (float | Unset):
        sced2_curve_mw20_from (float | Unset):
        sced2_curve_mw20_to (float | Unset):
        sced2_curve_price_20_from (float | Unset):
        sced2_curve_price_20_to (float | Unset):
        sced2_curve_mw21_from (float | Unset):
        sced2_curve_mw21_to (float | Unset):
        sced2_curve_price_21_from (float | Unset):
        sced2_curve_price_21_to (float | Unset):
        sced2_curve_mw22_from (float | Unset):
        sced2_curve_mw22_to (float | Unset):
        sced2_curve_price_22_from (float | Unset):
        sced2_curve_price_22_to (float | Unset):
        sced2_curve_mw23_from (float | Unset):
        sced2_curve_mw23_to (float | Unset):
        sced2_curve_price_23_from (float | Unset):
        sced2_curve_price_23_to (float | Unset):
        sced2_curve_mw24_from (float | Unset):
        sced2_curve_mw24_to (float | Unset):
        sced2_curve_price_24_from (float | Unset):
        sced2_curve_price_24_to (float | Unset):
        sced2_curve_mw25_from (float | Unset):
        sced2_curve_mw25_to (float | Unset):
        sced2_curve_price_25_from (float | Unset):
        sced2_curve_price_25_to (float | Unset):
        sced2_curve_mw26_from (float | Unset):
        sced2_curve_mw26_to (float | Unset):
        sced2_curve_price_26_from (float | Unset):
        sced2_curve_price_26_to (float | Unset):
        sced2_curve_mw27_from (float | Unset):
        sced2_curve_mw27_to (float | Unset):
        sced2_curve_price_27_from (float | Unset):
        sced2_curve_price_27_to (float | Unset):
        sced2_curve_mw28_from (float | Unset):
        sced2_curve_mw28_to (float | Unset):
        sced2_curve_price_28_from (float | Unset):
        sced2_curve_price_28_to (float | Unset):
        sced2_curve_mw29_from (float | Unset):
        sced2_curve_mw29_to (float | Unset):
        sced2_curve_price_29_from (float | Unset):
        sced2_curve_price_29_to (float | Unset):
        sced2_curve_mw30_from (float | Unset):
        sced2_curve_mw30_to (float | Unset):
        sced2_curve_price_30_from (float | Unset):
        sced2_curve_price_30_to (float | Unset):
        sced2_curve_mw31_from (float | Unset):
        sced2_curve_mw31_to (float | Unset):
        sced2_curve_price_31_from (float | Unset):
        sced2_curve_price_31_to (float | Unset):
        sced2_curve_mw32_from (float | Unset):
        sced2_curve_mw32_to (float | Unset):
        sced2_curve_price_32_from (float | Unset):
        sced2_curve_price_32_to (float | Unset):
        sced2_curve_mw33_from (float | Unset):
        sced2_curve_mw33_to (float | Unset):
        sced2_curve_price_33_from (float | Unset):
        sced2_curve_price_33_to (float | Unset):
        sced2_curve_mw34_from (float | Unset):
        sced2_curve_mw34_to (float | Unset):
        sced2_curve_price_34_from (float | Unset):
        sced2_curve_price_34_to (float | Unset):
        sced2_curve_mw35_from (float | Unset):
        sced2_curve_mw35_to (float | Unset):
        sced2_curve_price_35_from (float | Unset):
        sced2_curve_price_35_to (float | Unset):
        output_schedule_from (float | Unset):
        output_schedule_to (float | Unset):
        hsl_from (float | Unset):
        hsl_to (float | Unset):
        hasl_from (float | Unset):
        hasl_to (float | Unset):
        hdl_from (float | Unset):
        hdl_to (float | Unset):
        lsl_from (float | Unset):
        lsl_to (float | Unset):
        lasl_from (float | Unset):
        lasl_to (float | Unset):
        ldl_from (float | Unset):
        ldl_to (float | Unset):
        telemetered_resource_status (str | Unset):
        base_point_from (float | Unset):
        base_point_to (float | Unset):
        telemetered_net_output_from (float | Unset):
        telemetered_net_output_to (float | Unset):
        asregup_from (float | Unset):
        asregup_to (float | Unset):
        asregdn_from (float | Unset):
        asregdn_to (float | Unset):
        asrrs_from (float | Unset):
        asrrs_to (float | Unset):
        asrrsffr_from (float | Unset):
        asrrsffr_to (float | Unset):
        asnsrs_from (float | Unset):
        asnsrs_to (float | Unset):
        bid_type (str | Unset):
        start_up_cold_offer_from (float | Unset):
        start_up_cold_offer_to (float | Unset):
        start_up_hot_offer_from (float | Unset):
        start_up_hot_offer_to (float | Unset):
        start_up_inter_offer_from (float | Unset):
        start_up_inter_offer_to (float | Unset):
        min_gen_cost_from (float | Unset):
        min_gen_cost_to (float | Unset):
        submitted_tpomw1_from (float | Unset):
        submitted_tpomw1_to (float | Unset):
        submitted_tpo_price_1_from (float | Unset):
        submitted_tpo_price_1_to (float | Unset):
        submitted_tpomw2_from (float | Unset):
        submitted_tpomw2_to (float | Unset):
        submitted_tpo_price_2_from (float | Unset):
        submitted_tpo_price_2_to (float | Unset):
        submitted_tpomw3_from (float | Unset):
        submitted_tpomw3_to (float | Unset):
        submitted_tpo_price_3_from (float | Unset):
        submitted_tpo_price_3_to (float | Unset):
        submitted_tpomw4_from (float | Unset):
        submitted_tpomw4_to (float | Unset):
        submitted_tpo_price_4_from (float | Unset):
        submitted_tpo_price_4_to (float | Unset):
        submitted_tpomw5_from (float | Unset):
        submitted_tpomw5_to (float | Unset):
        submitted_tpo_price_5_from (float | Unset):
        submitted_tpo_price_5_to (float | Unset):
        submitted_tpomw6_from (float | Unset):
        submitted_tpomw6_to (float | Unset):
        submitted_tpo_price_6_from (float | Unset):
        submitted_tpo_price_6_to (float | Unset):
        submitted_tpomw7_from (float | Unset):
        submitted_tpomw7_to (float | Unset):
        submitted_tpo_price_7_from (float | Unset):
        submitted_tpo_price_7_to (float | Unset):
        submitted_tpomw8_from (float | Unset):
        submitted_tpomw8_to (float | Unset):
        submitted_tpo_price_8_from (float | Unset):
        submitted_tpo_price_8_to (float | Unset):
        submitted_tpomw9_from (float | Unset):
        submitted_tpomw9_to (float | Unset):
        submitted_tpo_price_9_from (float | Unset):
        submitted_tpo_price_9_to (float | Unset):
        submitted_tpomw10_from (float | Unset):
        submitted_tpomw10_to (float | Unset):
        submitted_tpo_price_10_from (float | Unset):
        submitted_tpo_price_10_to (float | Unset):
        proxy_extension (str | Unset):
        sced_timestamp_from (str | Unset):
        sced_timestamp_to (str | Unset):
        repeat_hour_flag (bool | Unset):
        qse_name (str | Unset):
        dme_name (str | Unset):
        resource_name (str | Unset):
        resource_type (str | Unset):
        sced1_curve_mw1_from (float | Unset):
        sced1_curve_mw1_to (float | Unset):
        sced1_curve_price_1_from (float | Unset):
        sced1_curve_price_1_to (float | Unset):
        sced1_curve_mw2_from (float | Unset):
        sced1_curve_mw2_to (float | Unset):
        sced1_curve_price_2_from (float | Unset):
        sced1_curve_price_2_to (float | Unset):
        sced1_curve_mw3_from (float | Unset):
        sced1_curve_mw3_to (float | Unset):
        sced1_curve_price_3_from (float | Unset):
        sced1_curve_price_3_to (float | Unset):
        sced1_curve_mw4_from (float | Unset):
        sced1_curve_mw4_to (float | Unset):
        sced1_curve_price_4_from (float | Unset):
        sced1_curve_price_4_to (float | Unset):
        sced1_curve_mw5_from (float | Unset):
        sced1_curve_mw5_to (float | Unset):
        sced1_curve_price_5_from (float | Unset):
        sced1_curve_price_5_to (float | Unset):
        sced1_curve_mw6_from (float | Unset):
        sced1_curve_mw6_to (float | Unset):
        sced1_curve_price_6_from (float | Unset):
        sced1_curve_price_6_to (float | Unset):
        sced1_curve_mw7_from (float | Unset):
        sced1_curve_mw7_to (float | Unset):
        sced1_curve_price_7_from (float | Unset):
        sced1_curve_price_7_to (float | Unset):
        sced1_curve_mw8_from (float | Unset):
        sced1_curve_mw8_to (float | Unset):
        sced1_curve_price_8_from (float | Unset):
        sced1_curve_price_8_to (float | Unset):
        sced1_curve_mw9_from (float | Unset):
        sced1_curve_mw9_to (float | Unset):
        sced1_curve_price_9_from (float | Unset):
        sced1_curve_price_9_to (float | Unset):
        sced1_curve_mw10_from (float | Unset):
        sced1_curve_mw10_to (float | Unset):
        sced1_curve_price_10_from (float | Unset):
        sced1_curve_price_10_to (float | Unset):
        sced1_curve_mw11_from (float | Unset):
        sced1_curve_mw11_to (float | Unset):
        sced1_curve_price_11_from (float | Unset):
        sced1_curve_price_11_to (float | Unset):
        sced1_curve_mw12_from (float | Unset):
        sced1_curve_mw12_to (float | Unset):
        sced1_curve_price_12_from (float | Unset):
        sced1_curve_price_12_to (float | Unset):
        sced1_curve_mw13_from (float | Unset):
        sced1_curve_mw13_to (float | Unset):
        sced1_curve_price_13_from (float | Unset):
        sced1_curve_price_13_to (float | Unset):
        sced1_curve_mw14_from (float | Unset):
        sced1_curve_mw14_to (float | Unset):
        sced1_curve_price_14_from (float | Unset):
        sced1_curve_price_14_to (float | Unset):
        sced1_curve_mw15_from (float | Unset):
        sced1_curve_mw15_to (float | Unset):
        sced1_curve_price_15_from (float | Unset):
        sced1_curve_price_15_to (float | Unset):
        sced1_curve_mw16_from (float | Unset):
        sced1_curve_mw16_to (float | Unset):
        sced1_curve_price_16_from (float | Unset):
        sced1_curve_price_16_to (float | Unset):
        sced1_curve_mw17_from (float | Unset):
        sced1_curve_mw17_to (float | Unset):
        sced1_curve_price_17_from (float | Unset):
        sced1_curve_price_17_to (float | Unset):
        sced1_curve_mw18_from (float | Unset):
        sced1_curve_mw18_to (float | Unset):
        sced1_curve_price_18_from (float | Unset):
        sced1_curve_price_18_to (float | Unset):
        sced1_curve_mw19_from (float | Unset):
        sced1_curve_mw19_to (float | Unset):
        sced1_curve_price_19_from (float | Unset):
        sced1_curve_price_19_to (float | Unset):
        sced1_curve_mw20_from (float | Unset):
        sced1_curve_mw20_to (float | Unset):
        sced1_curve_price_20_from (float | Unset):
        sced1_curve_price_20_to (float | Unset):
        sced1_curve_mw21_from (float | Unset):
        sced1_curve_mw21_to (float | Unset):
        sced1_curve_price_21_from (float | Unset):
        sced1_curve_price_21_to (float | Unset):
        sced1_curve_mw22_from (float | Unset):
        sced1_curve_mw22_to (float | Unset):
        sced1_curve_price_22_from (float | Unset):
        sced1_curve_price_22_to (float | Unset):
        sced1_curve_mw23_from (float | Unset):
        sced1_curve_mw23_to (float | Unset):
        sced1_curve_price_23_from (float | Unset):
        sced1_curve_price_23_to (float | Unset):
        sced1_curve_mw24_from (float | Unset):
        sced1_curve_mw24_to (float | Unset):
        sced1_curve_price_24_from (float | Unset):
        sced1_curve_price_24_to (float | Unset):
        sced1_curve_mw25_from (float | Unset):
        sced1_curve_mw25_to (float | Unset):
        sced1_curve_price_25_from (float | Unset):
        sced1_curve_price_25_to (float | Unset):
        sced1_curve_mw26_from (float | Unset):
        sced1_curve_mw26_to (float | Unset):
        sced1_curve_price_26_from (float | Unset):
        sced1_curve_price_26_to (float | Unset):
        sced1_curve_mw27_from (float | Unset):
        sced1_curve_mw27_to (float | Unset):
        sced1_curve_price_27_from (float | Unset):
        sced1_curve_price_27_to (float | Unset):
        sced1_curve_mw28_from (float | Unset):
        sced1_curve_mw28_to (float | Unset):
        sced1_curve_price_28_from (float | Unset):
        sced1_curve_price_28_to (float | Unset):
        sced1_curve_mw29_from (float | Unset):
        sced1_curve_mw29_to (float | Unset):
        sced1_curve_price_29_from (float | Unset):
        sced1_curve_price_29_to (float | Unset):
        sced1_curve_mw30_from (float | Unset):
        sced1_curve_mw30_to (float | Unset):
        sced1_curve_price_30_from (float | Unset):
        sced1_curve_price_30_to (float | Unset):
        sced1_curve_mw31_from (float | Unset):
        sced1_curve_mw31_to (float | Unset):
        sced1_curve_price_31_from (float | Unset):
        sced1_curve_price_31_to (float | Unset):
        sced1_curve_mw32_from (float | Unset):
        sced1_curve_mw32_to (float | Unset):
        sced1_curve_price_32_from (float | Unset):
        sced1_curve_price_32_to (float | Unset):
        sced1_curve_mw33_from (float | Unset):
        sced1_curve_mw33_to (float | Unset):
        sced1_curve_price_33_from (float | Unset):
        sced1_curve_price_33_to (float | Unset):
        sced1_curve_mw34_from (float | Unset):
        sced1_curve_mw34_to (float | Unset):
        sced1_curve_price_34_from (float | Unset):
        sced1_curve_price_34_to (float | Unset):
        sced1_curve_mw35_from (float | Unset):
        sced1_curve_mw35_to (float | Unset):
        sced1_curve_price_35_from (float | Unset):
        sced1_curve_price_35_to (float | Unset):
        sced2_curve_mw1_from (float | Unset):
        sced2_curve_mw1_to (float | Unset):
        sced2_curve_price_1_from (float | Unset):
        sced2_curve_price_1_to (float | Unset):
        sced2_curve_mw2_from (float | Unset):
        sced2_curve_mw2_to (float | Unset):
        sced2_curve_price_2_from (float | Unset):
        sced2_curve_price_2_to (float | Unset):
        sced2_curve_mw3_from (float | Unset):
        sced2_curve_mw3_to (float | Unset):
        sced2_curve_price_3_from (float | Unset):
        sced2_curve_price_3_to (float | Unset):
        sced2_curve_mw4_from (float | Unset):
        sced2_curve_mw4_to (float | Unset):
        sced2_curve_price_4_from (float | Unset):
        sced2_curve_price_4_to (float | Unset):
        sced2_curve_mw5_from (float | Unset):
        sced2_curve_mw5_to (float | Unset):
        sced2_curve_price_5_from (float | Unset):
        sced2_curve_price_5_to (float | Unset):
        sced2_curve_mw6_from (float | Unset):
        sced2_curve_mw6_to (float | Unset):
        sced2_curve_price_6_from (float | Unset):
        sced2_curve_price_6_to (float | Unset):
        sced2_curve_mw7_from (float | Unset):
        sced2_curve_mw7_to (float | Unset):
        sced2_curve_price_7_from (float | Unset):
        sced2_curve_price_7_to (float | Unset):
        sced2_curve_mw8_from (float | Unset):
        sced2_curve_mw8_to (float | Unset):
        sced2_curve_price_8_from (float | Unset):
        sced2_curve_price_8_to (float | Unset):
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
        sced2_curve_mw9_from=sced2_curve_mw9_from,
        sced2_curve_mw9_to=sced2_curve_mw9_to,
        sced2_curve_price_9_from=sced2_curve_price_9_from,
        sced2_curve_price_9_to=sced2_curve_price_9_to,
        sced2_curve_mw10_from=sced2_curve_mw10_from,
        sced2_curve_mw10_to=sced2_curve_mw10_to,
        sced2_curve_price_10_from=sced2_curve_price_10_from,
        sced2_curve_price_10_to=sced2_curve_price_10_to,
        sced2_curve_mw11_from=sced2_curve_mw11_from,
        sced2_curve_mw11_to=sced2_curve_mw11_to,
        sced2_curve_price_11_from=sced2_curve_price_11_from,
        sced2_curve_price_11_to=sced2_curve_price_11_to,
        sced2_curve_mw12_from=sced2_curve_mw12_from,
        sced2_curve_mw12_to=sced2_curve_mw12_to,
        sced2_curve_price_12_from=sced2_curve_price_12_from,
        sced2_curve_price_12_to=sced2_curve_price_12_to,
        sced2_curve_mw13_from=sced2_curve_mw13_from,
        sced2_curve_mw13_to=sced2_curve_mw13_to,
        sced2_curve_price_13_from=sced2_curve_price_13_from,
        sced2_curve_price_13_to=sced2_curve_price_13_to,
        sced2_curve_mw14_from=sced2_curve_mw14_from,
        sced2_curve_mw14_to=sced2_curve_mw14_to,
        sced2_curve_price_14_from=sced2_curve_price_14_from,
        sced2_curve_price_14_to=sced2_curve_price_14_to,
        sced2_curve_mw15_from=sced2_curve_mw15_from,
        sced2_curve_mw15_to=sced2_curve_mw15_to,
        sced2_curve_price_15_from=sced2_curve_price_15_from,
        sced2_curve_price_15_to=sced2_curve_price_15_to,
        sced2_curve_mw16_from=sced2_curve_mw16_from,
        sced2_curve_mw16_to=sced2_curve_mw16_to,
        sced2_curve_price_16_from=sced2_curve_price_16_from,
        sced2_curve_price_16_to=sced2_curve_price_16_to,
        sced2_curve_mw17_from=sced2_curve_mw17_from,
        sced2_curve_mw17_to=sced2_curve_mw17_to,
        sced2_curve_price_17_from=sced2_curve_price_17_from,
        sced2_curve_price_17_to=sced2_curve_price_17_to,
        sced2_curve_mw18_from=sced2_curve_mw18_from,
        sced2_curve_mw18_to=sced2_curve_mw18_to,
        sced2_curve_price_18_from=sced2_curve_price_18_from,
        sced2_curve_price_18_to=sced2_curve_price_18_to,
        sced2_curve_mw19_from=sced2_curve_mw19_from,
        sced2_curve_mw19_to=sced2_curve_mw19_to,
        sced2_curve_price_19_from=sced2_curve_price_19_from,
        sced2_curve_price_19_to=sced2_curve_price_19_to,
        sced2_curve_mw20_from=sced2_curve_mw20_from,
        sced2_curve_mw20_to=sced2_curve_mw20_to,
        sced2_curve_price_20_from=sced2_curve_price_20_from,
        sced2_curve_price_20_to=sced2_curve_price_20_to,
        sced2_curve_mw21_from=sced2_curve_mw21_from,
        sced2_curve_mw21_to=sced2_curve_mw21_to,
        sced2_curve_price_21_from=sced2_curve_price_21_from,
        sced2_curve_price_21_to=sced2_curve_price_21_to,
        sced2_curve_mw22_from=sced2_curve_mw22_from,
        sced2_curve_mw22_to=sced2_curve_mw22_to,
        sced2_curve_price_22_from=sced2_curve_price_22_from,
        sced2_curve_price_22_to=sced2_curve_price_22_to,
        sced2_curve_mw23_from=sced2_curve_mw23_from,
        sced2_curve_mw23_to=sced2_curve_mw23_to,
        sced2_curve_price_23_from=sced2_curve_price_23_from,
        sced2_curve_price_23_to=sced2_curve_price_23_to,
        sced2_curve_mw24_from=sced2_curve_mw24_from,
        sced2_curve_mw24_to=sced2_curve_mw24_to,
        sced2_curve_price_24_from=sced2_curve_price_24_from,
        sced2_curve_price_24_to=sced2_curve_price_24_to,
        sced2_curve_mw25_from=sced2_curve_mw25_from,
        sced2_curve_mw25_to=sced2_curve_mw25_to,
        sced2_curve_price_25_from=sced2_curve_price_25_from,
        sced2_curve_price_25_to=sced2_curve_price_25_to,
        sced2_curve_mw26_from=sced2_curve_mw26_from,
        sced2_curve_mw26_to=sced2_curve_mw26_to,
        sced2_curve_price_26_from=sced2_curve_price_26_from,
        sced2_curve_price_26_to=sced2_curve_price_26_to,
        sced2_curve_mw27_from=sced2_curve_mw27_from,
        sced2_curve_mw27_to=sced2_curve_mw27_to,
        sced2_curve_price_27_from=sced2_curve_price_27_from,
        sced2_curve_price_27_to=sced2_curve_price_27_to,
        sced2_curve_mw28_from=sced2_curve_mw28_from,
        sced2_curve_mw28_to=sced2_curve_mw28_to,
        sced2_curve_price_28_from=sced2_curve_price_28_from,
        sced2_curve_price_28_to=sced2_curve_price_28_to,
        sced2_curve_mw29_from=sced2_curve_mw29_from,
        sced2_curve_mw29_to=sced2_curve_mw29_to,
        sced2_curve_price_29_from=sced2_curve_price_29_from,
        sced2_curve_price_29_to=sced2_curve_price_29_to,
        sced2_curve_mw30_from=sced2_curve_mw30_from,
        sced2_curve_mw30_to=sced2_curve_mw30_to,
        sced2_curve_price_30_from=sced2_curve_price_30_from,
        sced2_curve_price_30_to=sced2_curve_price_30_to,
        sced2_curve_mw31_from=sced2_curve_mw31_from,
        sced2_curve_mw31_to=sced2_curve_mw31_to,
        sced2_curve_price_31_from=sced2_curve_price_31_from,
        sced2_curve_price_31_to=sced2_curve_price_31_to,
        sced2_curve_mw32_from=sced2_curve_mw32_from,
        sced2_curve_mw32_to=sced2_curve_mw32_to,
        sced2_curve_price_32_from=sced2_curve_price_32_from,
        sced2_curve_price_32_to=sced2_curve_price_32_to,
        sced2_curve_mw33_from=sced2_curve_mw33_from,
        sced2_curve_mw33_to=sced2_curve_mw33_to,
        sced2_curve_price_33_from=sced2_curve_price_33_from,
        sced2_curve_price_33_to=sced2_curve_price_33_to,
        sced2_curve_mw34_from=sced2_curve_mw34_from,
        sced2_curve_mw34_to=sced2_curve_mw34_to,
        sced2_curve_price_34_from=sced2_curve_price_34_from,
        sced2_curve_price_34_to=sced2_curve_price_34_to,
        sced2_curve_mw35_from=sced2_curve_mw35_from,
        sced2_curve_mw35_to=sced2_curve_mw35_to,
        sced2_curve_price_35_from=sced2_curve_price_35_from,
        sced2_curve_price_35_to=sced2_curve_price_35_to,
        output_schedule_from=output_schedule_from,
        output_schedule_to=output_schedule_to,
        hsl_from=hsl_from,
        hsl_to=hsl_to,
        hasl_from=hasl_from,
        hasl_to=hasl_to,
        hdl_from=hdl_from,
        hdl_to=hdl_to,
        lsl_from=lsl_from,
        lsl_to=lsl_to,
        lasl_from=lasl_from,
        lasl_to=lasl_to,
        ldl_from=ldl_from,
        ldl_to=ldl_to,
        telemetered_resource_status=telemetered_resource_status,
        base_point_from=base_point_from,
        base_point_to=base_point_to,
        telemetered_net_output_from=telemetered_net_output_from,
        telemetered_net_output_to=telemetered_net_output_to,
        asregup_from=asregup_from,
        asregup_to=asregup_to,
        asregdn_from=asregdn_from,
        asregdn_to=asregdn_to,
        asrrs_from=asrrs_from,
        asrrs_to=asrrs_to,
        asrrsffr_from=asrrsffr_from,
        asrrsffr_to=asrrsffr_to,
        asnsrs_from=asnsrs_from,
        asnsrs_to=asnsrs_to,
        bid_type=bid_type,
        start_up_cold_offer_from=start_up_cold_offer_from,
        start_up_cold_offer_to=start_up_cold_offer_to,
        start_up_hot_offer_from=start_up_hot_offer_from,
        start_up_hot_offer_to=start_up_hot_offer_to,
        start_up_inter_offer_from=start_up_inter_offer_from,
        start_up_inter_offer_to=start_up_inter_offer_to,
        min_gen_cost_from=min_gen_cost_from,
        min_gen_cost_to=min_gen_cost_to,
        submitted_tpomw1_from=submitted_tpomw1_from,
        submitted_tpomw1_to=submitted_tpomw1_to,
        submitted_tpo_price_1_from=submitted_tpo_price_1_from,
        submitted_tpo_price_1_to=submitted_tpo_price_1_to,
        submitted_tpomw2_from=submitted_tpomw2_from,
        submitted_tpomw2_to=submitted_tpomw2_to,
        submitted_tpo_price_2_from=submitted_tpo_price_2_from,
        submitted_tpo_price_2_to=submitted_tpo_price_2_to,
        submitted_tpomw3_from=submitted_tpomw3_from,
        submitted_tpomw3_to=submitted_tpomw3_to,
        submitted_tpo_price_3_from=submitted_tpo_price_3_from,
        submitted_tpo_price_3_to=submitted_tpo_price_3_to,
        submitted_tpomw4_from=submitted_tpomw4_from,
        submitted_tpomw4_to=submitted_tpomw4_to,
        submitted_tpo_price_4_from=submitted_tpo_price_4_from,
        submitted_tpo_price_4_to=submitted_tpo_price_4_to,
        submitted_tpomw5_from=submitted_tpomw5_from,
        submitted_tpomw5_to=submitted_tpomw5_to,
        submitted_tpo_price_5_from=submitted_tpo_price_5_from,
        submitted_tpo_price_5_to=submitted_tpo_price_5_to,
        submitted_tpomw6_from=submitted_tpomw6_from,
        submitted_tpomw6_to=submitted_tpomw6_to,
        submitted_tpo_price_6_from=submitted_tpo_price_6_from,
        submitted_tpo_price_6_to=submitted_tpo_price_6_to,
        submitted_tpomw7_from=submitted_tpomw7_from,
        submitted_tpomw7_to=submitted_tpomw7_to,
        submitted_tpo_price_7_from=submitted_tpo_price_7_from,
        submitted_tpo_price_7_to=submitted_tpo_price_7_to,
        submitted_tpomw8_from=submitted_tpomw8_from,
        submitted_tpomw8_to=submitted_tpomw8_to,
        submitted_tpo_price_8_from=submitted_tpo_price_8_from,
        submitted_tpo_price_8_to=submitted_tpo_price_8_to,
        submitted_tpomw9_from=submitted_tpomw9_from,
        submitted_tpomw9_to=submitted_tpomw9_to,
        submitted_tpo_price_9_from=submitted_tpo_price_9_from,
        submitted_tpo_price_9_to=submitted_tpo_price_9_to,
        submitted_tpomw10_from=submitted_tpomw10_from,
        submitted_tpomw10_to=submitted_tpomw10_to,
        submitted_tpo_price_10_from=submitted_tpo_price_10_from,
        submitted_tpo_price_10_to=submitted_tpo_price_10_to,
        proxy_extension=proxy_extension,
        sced_timestamp_from=sced_timestamp_from,
        sced_timestamp_to=sced_timestamp_to,
        repeat_hour_flag=repeat_hour_flag,
        qse_name=qse_name,
        dme_name=dme_name,
        resource_name=resource_name,
        resource_type=resource_type,
        sced1_curve_mw1_from=sced1_curve_mw1_from,
        sced1_curve_mw1_to=sced1_curve_mw1_to,
        sced1_curve_price_1_from=sced1_curve_price_1_from,
        sced1_curve_price_1_to=sced1_curve_price_1_to,
        sced1_curve_mw2_from=sced1_curve_mw2_from,
        sced1_curve_mw2_to=sced1_curve_mw2_to,
        sced1_curve_price_2_from=sced1_curve_price_2_from,
        sced1_curve_price_2_to=sced1_curve_price_2_to,
        sced1_curve_mw3_from=sced1_curve_mw3_from,
        sced1_curve_mw3_to=sced1_curve_mw3_to,
        sced1_curve_price_3_from=sced1_curve_price_3_from,
        sced1_curve_price_3_to=sced1_curve_price_3_to,
        sced1_curve_mw4_from=sced1_curve_mw4_from,
        sced1_curve_mw4_to=sced1_curve_mw4_to,
        sced1_curve_price_4_from=sced1_curve_price_4_from,
        sced1_curve_price_4_to=sced1_curve_price_4_to,
        sced1_curve_mw5_from=sced1_curve_mw5_from,
        sced1_curve_mw5_to=sced1_curve_mw5_to,
        sced1_curve_price_5_from=sced1_curve_price_5_from,
        sced1_curve_price_5_to=sced1_curve_price_5_to,
        sced1_curve_mw6_from=sced1_curve_mw6_from,
        sced1_curve_mw6_to=sced1_curve_mw6_to,
        sced1_curve_price_6_from=sced1_curve_price_6_from,
        sced1_curve_price_6_to=sced1_curve_price_6_to,
        sced1_curve_mw7_from=sced1_curve_mw7_from,
        sced1_curve_mw7_to=sced1_curve_mw7_to,
        sced1_curve_price_7_from=sced1_curve_price_7_from,
        sced1_curve_price_7_to=sced1_curve_price_7_to,
        sced1_curve_mw8_from=sced1_curve_mw8_from,
        sced1_curve_mw8_to=sced1_curve_mw8_to,
        sced1_curve_price_8_from=sced1_curve_price_8_from,
        sced1_curve_price_8_to=sced1_curve_price_8_to,
        sced1_curve_mw9_from=sced1_curve_mw9_from,
        sced1_curve_mw9_to=sced1_curve_mw9_to,
        sced1_curve_price_9_from=sced1_curve_price_9_from,
        sced1_curve_price_9_to=sced1_curve_price_9_to,
        sced1_curve_mw10_from=sced1_curve_mw10_from,
        sced1_curve_mw10_to=sced1_curve_mw10_to,
        sced1_curve_price_10_from=sced1_curve_price_10_from,
        sced1_curve_price_10_to=sced1_curve_price_10_to,
        sced1_curve_mw11_from=sced1_curve_mw11_from,
        sced1_curve_mw11_to=sced1_curve_mw11_to,
        sced1_curve_price_11_from=sced1_curve_price_11_from,
        sced1_curve_price_11_to=sced1_curve_price_11_to,
        sced1_curve_mw12_from=sced1_curve_mw12_from,
        sced1_curve_mw12_to=sced1_curve_mw12_to,
        sced1_curve_price_12_from=sced1_curve_price_12_from,
        sced1_curve_price_12_to=sced1_curve_price_12_to,
        sced1_curve_mw13_from=sced1_curve_mw13_from,
        sced1_curve_mw13_to=sced1_curve_mw13_to,
        sced1_curve_price_13_from=sced1_curve_price_13_from,
        sced1_curve_price_13_to=sced1_curve_price_13_to,
        sced1_curve_mw14_from=sced1_curve_mw14_from,
        sced1_curve_mw14_to=sced1_curve_mw14_to,
        sced1_curve_price_14_from=sced1_curve_price_14_from,
        sced1_curve_price_14_to=sced1_curve_price_14_to,
        sced1_curve_mw15_from=sced1_curve_mw15_from,
        sced1_curve_mw15_to=sced1_curve_mw15_to,
        sced1_curve_price_15_from=sced1_curve_price_15_from,
        sced1_curve_price_15_to=sced1_curve_price_15_to,
        sced1_curve_mw16_from=sced1_curve_mw16_from,
        sced1_curve_mw16_to=sced1_curve_mw16_to,
        sced1_curve_price_16_from=sced1_curve_price_16_from,
        sced1_curve_price_16_to=sced1_curve_price_16_to,
        sced1_curve_mw17_from=sced1_curve_mw17_from,
        sced1_curve_mw17_to=sced1_curve_mw17_to,
        sced1_curve_price_17_from=sced1_curve_price_17_from,
        sced1_curve_price_17_to=sced1_curve_price_17_to,
        sced1_curve_mw18_from=sced1_curve_mw18_from,
        sced1_curve_mw18_to=sced1_curve_mw18_to,
        sced1_curve_price_18_from=sced1_curve_price_18_from,
        sced1_curve_price_18_to=sced1_curve_price_18_to,
        sced1_curve_mw19_from=sced1_curve_mw19_from,
        sced1_curve_mw19_to=sced1_curve_mw19_to,
        sced1_curve_price_19_from=sced1_curve_price_19_from,
        sced1_curve_price_19_to=sced1_curve_price_19_to,
        sced1_curve_mw20_from=sced1_curve_mw20_from,
        sced1_curve_mw20_to=sced1_curve_mw20_to,
        sced1_curve_price_20_from=sced1_curve_price_20_from,
        sced1_curve_price_20_to=sced1_curve_price_20_to,
        sced1_curve_mw21_from=sced1_curve_mw21_from,
        sced1_curve_mw21_to=sced1_curve_mw21_to,
        sced1_curve_price_21_from=sced1_curve_price_21_from,
        sced1_curve_price_21_to=sced1_curve_price_21_to,
        sced1_curve_mw22_from=sced1_curve_mw22_from,
        sced1_curve_mw22_to=sced1_curve_mw22_to,
        sced1_curve_price_22_from=sced1_curve_price_22_from,
        sced1_curve_price_22_to=sced1_curve_price_22_to,
        sced1_curve_mw23_from=sced1_curve_mw23_from,
        sced1_curve_mw23_to=sced1_curve_mw23_to,
        sced1_curve_price_23_from=sced1_curve_price_23_from,
        sced1_curve_price_23_to=sced1_curve_price_23_to,
        sced1_curve_mw24_from=sced1_curve_mw24_from,
        sced1_curve_mw24_to=sced1_curve_mw24_to,
        sced1_curve_price_24_from=sced1_curve_price_24_from,
        sced1_curve_price_24_to=sced1_curve_price_24_to,
        sced1_curve_mw25_from=sced1_curve_mw25_from,
        sced1_curve_mw25_to=sced1_curve_mw25_to,
        sced1_curve_price_25_from=sced1_curve_price_25_from,
        sced1_curve_price_25_to=sced1_curve_price_25_to,
        sced1_curve_mw26_from=sced1_curve_mw26_from,
        sced1_curve_mw26_to=sced1_curve_mw26_to,
        sced1_curve_price_26_from=sced1_curve_price_26_from,
        sced1_curve_price_26_to=sced1_curve_price_26_to,
        sced1_curve_mw27_from=sced1_curve_mw27_from,
        sced1_curve_mw27_to=sced1_curve_mw27_to,
        sced1_curve_price_27_from=sced1_curve_price_27_from,
        sced1_curve_price_27_to=sced1_curve_price_27_to,
        sced1_curve_mw28_from=sced1_curve_mw28_from,
        sced1_curve_mw28_to=sced1_curve_mw28_to,
        sced1_curve_price_28_from=sced1_curve_price_28_from,
        sced1_curve_price_28_to=sced1_curve_price_28_to,
        sced1_curve_mw29_from=sced1_curve_mw29_from,
        sced1_curve_mw29_to=sced1_curve_mw29_to,
        sced1_curve_price_29_from=sced1_curve_price_29_from,
        sced1_curve_price_29_to=sced1_curve_price_29_to,
        sced1_curve_mw30_from=sced1_curve_mw30_from,
        sced1_curve_mw30_to=sced1_curve_mw30_to,
        sced1_curve_price_30_from=sced1_curve_price_30_from,
        sced1_curve_price_30_to=sced1_curve_price_30_to,
        sced1_curve_mw31_from=sced1_curve_mw31_from,
        sced1_curve_mw31_to=sced1_curve_mw31_to,
        sced1_curve_price_31_from=sced1_curve_price_31_from,
        sced1_curve_price_31_to=sced1_curve_price_31_to,
        sced1_curve_mw32_from=sced1_curve_mw32_from,
        sced1_curve_mw32_to=sced1_curve_mw32_to,
        sced1_curve_price_32_from=sced1_curve_price_32_from,
        sced1_curve_price_32_to=sced1_curve_price_32_to,
        sced1_curve_mw33_from=sced1_curve_mw33_from,
        sced1_curve_mw33_to=sced1_curve_mw33_to,
        sced1_curve_price_33_from=sced1_curve_price_33_from,
        sced1_curve_price_33_to=sced1_curve_price_33_to,
        sced1_curve_mw34_from=sced1_curve_mw34_from,
        sced1_curve_mw34_to=sced1_curve_mw34_to,
        sced1_curve_price_34_from=sced1_curve_price_34_from,
        sced1_curve_price_34_to=sced1_curve_price_34_to,
        sced1_curve_mw35_from=sced1_curve_mw35_from,
        sced1_curve_mw35_to=sced1_curve_mw35_to,
        sced1_curve_price_35_from=sced1_curve_price_35_from,
        sced1_curve_price_35_to=sced1_curve_price_35_to,
        sced2_curve_mw1_from=sced2_curve_mw1_from,
        sced2_curve_mw1_to=sced2_curve_mw1_to,
        sced2_curve_price_1_from=sced2_curve_price_1_from,
        sced2_curve_price_1_to=sced2_curve_price_1_to,
        sced2_curve_mw2_from=sced2_curve_mw2_from,
        sced2_curve_mw2_to=sced2_curve_mw2_to,
        sced2_curve_price_2_from=sced2_curve_price_2_from,
        sced2_curve_price_2_to=sced2_curve_price_2_to,
        sced2_curve_mw3_from=sced2_curve_mw3_from,
        sced2_curve_mw3_to=sced2_curve_mw3_to,
        sced2_curve_price_3_from=sced2_curve_price_3_from,
        sced2_curve_price_3_to=sced2_curve_price_3_to,
        sced2_curve_mw4_from=sced2_curve_mw4_from,
        sced2_curve_mw4_to=sced2_curve_mw4_to,
        sced2_curve_price_4_from=sced2_curve_price_4_from,
        sced2_curve_price_4_to=sced2_curve_price_4_to,
        sced2_curve_mw5_from=sced2_curve_mw5_from,
        sced2_curve_mw5_to=sced2_curve_mw5_to,
        sced2_curve_price_5_from=sced2_curve_price_5_from,
        sced2_curve_price_5_to=sced2_curve_price_5_to,
        sced2_curve_mw6_from=sced2_curve_mw6_from,
        sced2_curve_mw6_to=sced2_curve_mw6_to,
        sced2_curve_price_6_from=sced2_curve_price_6_from,
        sced2_curve_price_6_to=sced2_curve_price_6_to,
        sced2_curve_mw7_from=sced2_curve_mw7_from,
        sced2_curve_mw7_to=sced2_curve_mw7_to,
        sced2_curve_price_7_from=sced2_curve_price_7_from,
        sced2_curve_price_7_to=sced2_curve_price_7_to,
        sced2_curve_mw8_from=sced2_curve_mw8_from,
        sced2_curve_mw8_to=sced2_curve_mw8_to,
        sced2_curve_price_8_from=sced2_curve_price_8_from,
        sced2_curve_price_8_to=sced2_curve_price_8_to,
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
    sced2_curve_mw9_from: float | Unset = UNSET,
    sced2_curve_mw9_to: float | Unset = UNSET,
    sced2_curve_price_9_from: float | Unset = UNSET,
    sced2_curve_price_9_to: float | Unset = UNSET,
    sced2_curve_mw10_from: float | Unset = UNSET,
    sced2_curve_mw10_to: float | Unset = UNSET,
    sced2_curve_price_10_from: float | Unset = UNSET,
    sced2_curve_price_10_to: float | Unset = UNSET,
    sced2_curve_mw11_from: float | Unset = UNSET,
    sced2_curve_mw11_to: float | Unset = UNSET,
    sced2_curve_price_11_from: float | Unset = UNSET,
    sced2_curve_price_11_to: float | Unset = UNSET,
    sced2_curve_mw12_from: float | Unset = UNSET,
    sced2_curve_mw12_to: float | Unset = UNSET,
    sced2_curve_price_12_from: float | Unset = UNSET,
    sced2_curve_price_12_to: float | Unset = UNSET,
    sced2_curve_mw13_from: float | Unset = UNSET,
    sced2_curve_mw13_to: float | Unset = UNSET,
    sced2_curve_price_13_from: float | Unset = UNSET,
    sced2_curve_price_13_to: float | Unset = UNSET,
    sced2_curve_mw14_from: float | Unset = UNSET,
    sced2_curve_mw14_to: float | Unset = UNSET,
    sced2_curve_price_14_from: float | Unset = UNSET,
    sced2_curve_price_14_to: float | Unset = UNSET,
    sced2_curve_mw15_from: float | Unset = UNSET,
    sced2_curve_mw15_to: float | Unset = UNSET,
    sced2_curve_price_15_from: float | Unset = UNSET,
    sced2_curve_price_15_to: float | Unset = UNSET,
    sced2_curve_mw16_from: float | Unset = UNSET,
    sced2_curve_mw16_to: float | Unset = UNSET,
    sced2_curve_price_16_from: float | Unset = UNSET,
    sced2_curve_price_16_to: float | Unset = UNSET,
    sced2_curve_mw17_from: float | Unset = UNSET,
    sced2_curve_mw17_to: float | Unset = UNSET,
    sced2_curve_price_17_from: float | Unset = UNSET,
    sced2_curve_price_17_to: float | Unset = UNSET,
    sced2_curve_mw18_from: float | Unset = UNSET,
    sced2_curve_mw18_to: float | Unset = UNSET,
    sced2_curve_price_18_from: float | Unset = UNSET,
    sced2_curve_price_18_to: float | Unset = UNSET,
    sced2_curve_mw19_from: float | Unset = UNSET,
    sced2_curve_mw19_to: float | Unset = UNSET,
    sced2_curve_price_19_from: float | Unset = UNSET,
    sced2_curve_price_19_to: float | Unset = UNSET,
    sced2_curve_mw20_from: float | Unset = UNSET,
    sced2_curve_mw20_to: float | Unset = UNSET,
    sced2_curve_price_20_from: float | Unset = UNSET,
    sced2_curve_price_20_to: float | Unset = UNSET,
    sced2_curve_mw21_from: float | Unset = UNSET,
    sced2_curve_mw21_to: float | Unset = UNSET,
    sced2_curve_price_21_from: float | Unset = UNSET,
    sced2_curve_price_21_to: float | Unset = UNSET,
    sced2_curve_mw22_from: float | Unset = UNSET,
    sced2_curve_mw22_to: float | Unset = UNSET,
    sced2_curve_price_22_from: float | Unset = UNSET,
    sced2_curve_price_22_to: float | Unset = UNSET,
    sced2_curve_mw23_from: float | Unset = UNSET,
    sced2_curve_mw23_to: float | Unset = UNSET,
    sced2_curve_price_23_from: float | Unset = UNSET,
    sced2_curve_price_23_to: float | Unset = UNSET,
    sced2_curve_mw24_from: float | Unset = UNSET,
    sced2_curve_mw24_to: float | Unset = UNSET,
    sced2_curve_price_24_from: float | Unset = UNSET,
    sced2_curve_price_24_to: float | Unset = UNSET,
    sced2_curve_mw25_from: float | Unset = UNSET,
    sced2_curve_mw25_to: float | Unset = UNSET,
    sced2_curve_price_25_from: float | Unset = UNSET,
    sced2_curve_price_25_to: float | Unset = UNSET,
    sced2_curve_mw26_from: float | Unset = UNSET,
    sced2_curve_mw26_to: float | Unset = UNSET,
    sced2_curve_price_26_from: float | Unset = UNSET,
    sced2_curve_price_26_to: float | Unset = UNSET,
    sced2_curve_mw27_from: float | Unset = UNSET,
    sced2_curve_mw27_to: float | Unset = UNSET,
    sced2_curve_price_27_from: float | Unset = UNSET,
    sced2_curve_price_27_to: float | Unset = UNSET,
    sced2_curve_mw28_from: float | Unset = UNSET,
    sced2_curve_mw28_to: float | Unset = UNSET,
    sced2_curve_price_28_from: float | Unset = UNSET,
    sced2_curve_price_28_to: float | Unset = UNSET,
    sced2_curve_mw29_from: float | Unset = UNSET,
    sced2_curve_mw29_to: float | Unset = UNSET,
    sced2_curve_price_29_from: float | Unset = UNSET,
    sced2_curve_price_29_to: float | Unset = UNSET,
    sced2_curve_mw30_from: float | Unset = UNSET,
    sced2_curve_mw30_to: float | Unset = UNSET,
    sced2_curve_price_30_from: float | Unset = UNSET,
    sced2_curve_price_30_to: float | Unset = UNSET,
    sced2_curve_mw31_from: float | Unset = UNSET,
    sced2_curve_mw31_to: float | Unset = UNSET,
    sced2_curve_price_31_from: float | Unset = UNSET,
    sced2_curve_price_31_to: float | Unset = UNSET,
    sced2_curve_mw32_from: float | Unset = UNSET,
    sced2_curve_mw32_to: float | Unset = UNSET,
    sced2_curve_price_32_from: float | Unset = UNSET,
    sced2_curve_price_32_to: float | Unset = UNSET,
    sced2_curve_mw33_from: float | Unset = UNSET,
    sced2_curve_mw33_to: float | Unset = UNSET,
    sced2_curve_price_33_from: float | Unset = UNSET,
    sced2_curve_price_33_to: float | Unset = UNSET,
    sced2_curve_mw34_from: float | Unset = UNSET,
    sced2_curve_mw34_to: float | Unset = UNSET,
    sced2_curve_price_34_from: float | Unset = UNSET,
    sced2_curve_price_34_to: float | Unset = UNSET,
    sced2_curve_mw35_from: float | Unset = UNSET,
    sced2_curve_mw35_to: float | Unset = UNSET,
    sced2_curve_price_35_from: float | Unset = UNSET,
    sced2_curve_price_35_to: float | Unset = UNSET,
    output_schedule_from: float | Unset = UNSET,
    output_schedule_to: float | Unset = UNSET,
    hsl_from: float | Unset = UNSET,
    hsl_to: float | Unset = UNSET,
    hasl_from: float | Unset = UNSET,
    hasl_to: float | Unset = UNSET,
    hdl_from: float | Unset = UNSET,
    hdl_to: float | Unset = UNSET,
    lsl_from: float | Unset = UNSET,
    lsl_to: float | Unset = UNSET,
    lasl_from: float | Unset = UNSET,
    lasl_to: float | Unset = UNSET,
    ldl_from: float | Unset = UNSET,
    ldl_to: float | Unset = UNSET,
    telemetered_resource_status: str | Unset = UNSET,
    base_point_from: float | Unset = UNSET,
    base_point_to: float | Unset = UNSET,
    telemetered_net_output_from: float | Unset = UNSET,
    telemetered_net_output_to: float | Unset = UNSET,
    asregup_from: float | Unset = UNSET,
    asregup_to: float | Unset = UNSET,
    asregdn_from: float | Unset = UNSET,
    asregdn_to: float | Unset = UNSET,
    asrrs_from: float | Unset = UNSET,
    asrrs_to: float | Unset = UNSET,
    asrrsffr_from: float | Unset = UNSET,
    asrrsffr_to: float | Unset = UNSET,
    asnsrs_from: float | Unset = UNSET,
    asnsrs_to: float | Unset = UNSET,
    bid_type: str | Unset = UNSET,
    start_up_cold_offer_from: float | Unset = UNSET,
    start_up_cold_offer_to: float | Unset = UNSET,
    start_up_hot_offer_from: float | Unset = UNSET,
    start_up_hot_offer_to: float | Unset = UNSET,
    start_up_inter_offer_from: float | Unset = UNSET,
    start_up_inter_offer_to: float | Unset = UNSET,
    min_gen_cost_from: float | Unset = UNSET,
    min_gen_cost_to: float | Unset = UNSET,
    submitted_tpomw1_from: float | Unset = UNSET,
    submitted_tpomw1_to: float | Unset = UNSET,
    submitted_tpo_price_1_from: float | Unset = UNSET,
    submitted_tpo_price_1_to: float | Unset = UNSET,
    submitted_tpomw2_from: float | Unset = UNSET,
    submitted_tpomw2_to: float | Unset = UNSET,
    submitted_tpo_price_2_from: float | Unset = UNSET,
    submitted_tpo_price_2_to: float | Unset = UNSET,
    submitted_tpomw3_from: float | Unset = UNSET,
    submitted_tpomw3_to: float | Unset = UNSET,
    submitted_tpo_price_3_from: float | Unset = UNSET,
    submitted_tpo_price_3_to: float | Unset = UNSET,
    submitted_tpomw4_from: float | Unset = UNSET,
    submitted_tpomw4_to: float | Unset = UNSET,
    submitted_tpo_price_4_from: float | Unset = UNSET,
    submitted_tpo_price_4_to: float | Unset = UNSET,
    submitted_tpomw5_from: float | Unset = UNSET,
    submitted_tpomw5_to: float | Unset = UNSET,
    submitted_tpo_price_5_from: float | Unset = UNSET,
    submitted_tpo_price_5_to: float | Unset = UNSET,
    submitted_tpomw6_from: float | Unset = UNSET,
    submitted_tpomw6_to: float | Unset = UNSET,
    submitted_tpo_price_6_from: float | Unset = UNSET,
    submitted_tpo_price_6_to: float | Unset = UNSET,
    submitted_tpomw7_from: float | Unset = UNSET,
    submitted_tpomw7_to: float | Unset = UNSET,
    submitted_tpo_price_7_from: float | Unset = UNSET,
    submitted_tpo_price_7_to: float | Unset = UNSET,
    submitted_tpomw8_from: float | Unset = UNSET,
    submitted_tpomw8_to: float | Unset = UNSET,
    submitted_tpo_price_8_from: float | Unset = UNSET,
    submitted_tpo_price_8_to: float | Unset = UNSET,
    submitted_tpomw9_from: float | Unset = UNSET,
    submitted_tpomw9_to: float | Unset = UNSET,
    submitted_tpo_price_9_from: float | Unset = UNSET,
    submitted_tpo_price_9_to: float | Unset = UNSET,
    submitted_tpomw10_from: float | Unset = UNSET,
    submitted_tpomw10_to: float | Unset = UNSET,
    submitted_tpo_price_10_from: float | Unset = UNSET,
    submitted_tpo_price_10_to: float | Unset = UNSET,
    proxy_extension: str | Unset = UNSET,
    sced_timestamp_from: str | Unset = UNSET,
    sced_timestamp_to: str | Unset = UNSET,
    repeat_hour_flag: bool | Unset = UNSET,
    qse_name: str | Unset = UNSET,
    dme_name: str | Unset = UNSET,
    resource_name: str | Unset = UNSET,
    resource_type: str | Unset = UNSET,
    sced1_curve_mw1_from: float | Unset = UNSET,
    sced1_curve_mw1_to: float | Unset = UNSET,
    sced1_curve_price_1_from: float | Unset = UNSET,
    sced1_curve_price_1_to: float | Unset = UNSET,
    sced1_curve_mw2_from: float | Unset = UNSET,
    sced1_curve_mw2_to: float | Unset = UNSET,
    sced1_curve_price_2_from: float | Unset = UNSET,
    sced1_curve_price_2_to: float | Unset = UNSET,
    sced1_curve_mw3_from: float | Unset = UNSET,
    sced1_curve_mw3_to: float | Unset = UNSET,
    sced1_curve_price_3_from: float | Unset = UNSET,
    sced1_curve_price_3_to: float | Unset = UNSET,
    sced1_curve_mw4_from: float | Unset = UNSET,
    sced1_curve_mw4_to: float | Unset = UNSET,
    sced1_curve_price_4_from: float | Unset = UNSET,
    sced1_curve_price_4_to: float | Unset = UNSET,
    sced1_curve_mw5_from: float | Unset = UNSET,
    sced1_curve_mw5_to: float | Unset = UNSET,
    sced1_curve_price_5_from: float | Unset = UNSET,
    sced1_curve_price_5_to: float | Unset = UNSET,
    sced1_curve_mw6_from: float | Unset = UNSET,
    sced1_curve_mw6_to: float | Unset = UNSET,
    sced1_curve_price_6_from: float | Unset = UNSET,
    sced1_curve_price_6_to: float | Unset = UNSET,
    sced1_curve_mw7_from: float | Unset = UNSET,
    sced1_curve_mw7_to: float | Unset = UNSET,
    sced1_curve_price_7_from: float | Unset = UNSET,
    sced1_curve_price_7_to: float | Unset = UNSET,
    sced1_curve_mw8_from: float | Unset = UNSET,
    sced1_curve_mw8_to: float | Unset = UNSET,
    sced1_curve_price_8_from: float | Unset = UNSET,
    sced1_curve_price_8_to: float | Unset = UNSET,
    sced1_curve_mw9_from: float | Unset = UNSET,
    sced1_curve_mw9_to: float | Unset = UNSET,
    sced1_curve_price_9_from: float | Unset = UNSET,
    sced1_curve_price_9_to: float | Unset = UNSET,
    sced1_curve_mw10_from: float | Unset = UNSET,
    sced1_curve_mw10_to: float | Unset = UNSET,
    sced1_curve_price_10_from: float | Unset = UNSET,
    sced1_curve_price_10_to: float | Unset = UNSET,
    sced1_curve_mw11_from: float | Unset = UNSET,
    sced1_curve_mw11_to: float | Unset = UNSET,
    sced1_curve_price_11_from: float | Unset = UNSET,
    sced1_curve_price_11_to: float | Unset = UNSET,
    sced1_curve_mw12_from: float | Unset = UNSET,
    sced1_curve_mw12_to: float | Unset = UNSET,
    sced1_curve_price_12_from: float | Unset = UNSET,
    sced1_curve_price_12_to: float | Unset = UNSET,
    sced1_curve_mw13_from: float | Unset = UNSET,
    sced1_curve_mw13_to: float | Unset = UNSET,
    sced1_curve_price_13_from: float | Unset = UNSET,
    sced1_curve_price_13_to: float | Unset = UNSET,
    sced1_curve_mw14_from: float | Unset = UNSET,
    sced1_curve_mw14_to: float | Unset = UNSET,
    sced1_curve_price_14_from: float | Unset = UNSET,
    sced1_curve_price_14_to: float | Unset = UNSET,
    sced1_curve_mw15_from: float | Unset = UNSET,
    sced1_curve_mw15_to: float | Unset = UNSET,
    sced1_curve_price_15_from: float | Unset = UNSET,
    sced1_curve_price_15_to: float | Unset = UNSET,
    sced1_curve_mw16_from: float | Unset = UNSET,
    sced1_curve_mw16_to: float | Unset = UNSET,
    sced1_curve_price_16_from: float | Unset = UNSET,
    sced1_curve_price_16_to: float | Unset = UNSET,
    sced1_curve_mw17_from: float | Unset = UNSET,
    sced1_curve_mw17_to: float | Unset = UNSET,
    sced1_curve_price_17_from: float | Unset = UNSET,
    sced1_curve_price_17_to: float | Unset = UNSET,
    sced1_curve_mw18_from: float | Unset = UNSET,
    sced1_curve_mw18_to: float | Unset = UNSET,
    sced1_curve_price_18_from: float | Unset = UNSET,
    sced1_curve_price_18_to: float | Unset = UNSET,
    sced1_curve_mw19_from: float | Unset = UNSET,
    sced1_curve_mw19_to: float | Unset = UNSET,
    sced1_curve_price_19_from: float | Unset = UNSET,
    sced1_curve_price_19_to: float | Unset = UNSET,
    sced1_curve_mw20_from: float | Unset = UNSET,
    sced1_curve_mw20_to: float | Unset = UNSET,
    sced1_curve_price_20_from: float | Unset = UNSET,
    sced1_curve_price_20_to: float | Unset = UNSET,
    sced1_curve_mw21_from: float | Unset = UNSET,
    sced1_curve_mw21_to: float | Unset = UNSET,
    sced1_curve_price_21_from: float | Unset = UNSET,
    sced1_curve_price_21_to: float | Unset = UNSET,
    sced1_curve_mw22_from: float | Unset = UNSET,
    sced1_curve_mw22_to: float | Unset = UNSET,
    sced1_curve_price_22_from: float | Unset = UNSET,
    sced1_curve_price_22_to: float | Unset = UNSET,
    sced1_curve_mw23_from: float | Unset = UNSET,
    sced1_curve_mw23_to: float | Unset = UNSET,
    sced1_curve_price_23_from: float | Unset = UNSET,
    sced1_curve_price_23_to: float | Unset = UNSET,
    sced1_curve_mw24_from: float | Unset = UNSET,
    sced1_curve_mw24_to: float | Unset = UNSET,
    sced1_curve_price_24_from: float | Unset = UNSET,
    sced1_curve_price_24_to: float | Unset = UNSET,
    sced1_curve_mw25_from: float | Unset = UNSET,
    sced1_curve_mw25_to: float | Unset = UNSET,
    sced1_curve_price_25_from: float | Unset = UNSET,
    sced1_curve_price_25_to: float | Unset = UNSET,
    sced1_curve_mw26_from: float | Unset = UNSET,
    sced1_curve_mw26_to: float | Unset = UNSET,
    sced1_curve_price_26_from: float | Unset = UNSET,
    sced1_curve_price_26_to: float | Unset = UNSET,
    sced1_curve_mw27_from: float | Unset = UNSET,
    sced1_curve_mw27_to: float | Unset = UNSET,
    sced1_curve_price_27_from: float | Unset = UNSET,
    sced1_curve_price_27_to: float | Unset = UNSET,
    sced1_curve_mw28_from: float | Unset = UNSET,
    sced1_curve_mw28_to: float | Unset = UNSET,
    sced1_curve_price_28_from: float | Unset = UNSET,
    sced1_curve_price_28_to: float | Unset = UNSET,
    sced1_curve_mw29_from: float | Unset = UNSET,
    sced1_curve_mw29_to: float | Unset = UNSET,
    sced1_curve_price_29_from: float | Unset = UNSET,
    sced1_curve_price_29_to: float | Unset = UNSET,
    sced1_curve_mw30_from: float | Unset = UNSET,
    sced1_curve_mw30_to: float | Unset = UNSET,
    sced1_curve_price_30_from: float | Unset = UNSET,
    sced1_curve_price_30_to: float | Unset = UNSET,
    sced1_curve_mw31_from: float | Unset = UNSET,
    sced1_curve_mw31_to: float | Unset = UNSET,
    sced1_curve_price_31_from: float | Unset = UNSET,
    sced1_curve_price_31_to: float | Unset = UNSET,
    sced1_curve_mw32_from: float | Unset = UNSET,
    sced1_curve_mw32_to: float | Unset = UNSET,
    sced1_curve_price_32_from: float | Unset = UNSET,
    sced1_curve_price_32_to: float | Unset = UNSET,
    sced1_curve_mw33_from: float | Unset = UNSET,
    sced1_curve_mw33_to: float | Unset = UNSET,
    sced1_curve_price_33_from: float | Unset = UNSET,
    sced1_curve_price_33_to: float | Unset = UNSET,
    sced1_curve_mw34_from: float | Unset = UNSET,
    sced1_curve_mw34_to: float | Unset = UNSET,
    sced1_curve_price_34_from: float | Unset = UNSET,
    sced1_curve_price_34_to: float | Unset = UNSET,
    sced1_curve_mw35_from: float | Unset = UNSET,
    sced1_curve_mw35_to: float | Unset = UNSET,
    sced1_curve_price_35_from: float | Unset = UNSET,
    sced1_curve_price_35_to: float | Unset = UNSET,
    sced2_curve_mw1_from: float | Unset = UNSET,
    sced2_curve_mw1_to: float | Unset = UNSET,
    sced2_curve_price_1_from: float | Unset = UNSET,
    sced2_curve_price_1_to: float | Unset = UNSET,
    sced2_curve_mw2_from: float | Unset = UNSET,
    sced2_curve_mw2_to: float | Unset = UNSET,
    sced2_curve_price_2_from: float | Unset = UNSET,
    sced2_curve_price_2_to: float | Unset = UNSET,
    sced2_curve_mw3_from: float | Unset = UNSET,
    sced2_curve_mw3_to: float | Unset = UNSET,
    sced2_curve_price_3_from: float | Unset = UNSET,
    sced2_curve_price_3_to: float | Unset = UNSET,
    sced2_curve_mw4_from: float | Unset = UNSET,
    sced2_curve_mw4_to: float | Unset = UNSET,
    sced2_curve_price_4_from: float | Unset = UNSET,
    sced2_curve_price_4_to: float | Unset = UNSET,
    sced2_curve_mw5_from: float | Unset = UNSET,
    sced2_curve_mw5_to: float | Unset = UNSET,
    sced2_curve_price_5_from: float | Unset = UNSET,
    sced2_curve_price_5_to: float | Unset = UNSET,
    sced2_curve_mw6_from: float | Unset = UNSET,
    sced2_curve_mw6_to: float | Unset = UNSET,
    sced2_curve_price_6_from: float | Unset = UNSET,
    sced2_curve_price_6_to: float | Unset = UNSET,
    sced2_curve_mw7_from: float | Unset = UNSET,
    sced2_curve_mw7_to: float | Unset = UNSET,
    sced2_curve_price_7_from: float | Unset = UNSET,
    sced2_curve_price_7_to: float | Unset = UNSET,
    sced2_curve_mw8_from: float | Unset = UNSET,
    sced2_curve_mw8_to: float | Unset = UNSET,
    sced2_curve_price_8_from: float | Unset = UNSET,
    sced2_curve_price_8_to: float | Unset = UNSET,
    page: int | Unset = UNSET,
    size: int | Unset = UNSET,
    sort: str | Unset = UNSET,
    dir_: str | Unset = UNSET,
) -> Exception_ | Report | None:
    """60 Day SCED Gen Resource Data

     60 Day SCED Gen Resource Data

    Args:
        sced2_curve_mw9_from (float | Unset):
        sced2_curve_mw9_to (float | Unset):
        sced2_curve_price_9_from (float | Unset):
        sced2_curve_price_9_to (float | Unset):
        sced2_curve_mw10_from (float | Unset):
        sced2_curve_mw10_to (float | Unset):
        sced2_curve_price_10_from (float | Unset):
        sced2_curve_price_10_to (float | Unset):
        sced2_curve_mw11_from (float | Unset):
        sced2_curve_mw11_to (float | Unset):
        sced2_curve_price_11_from (float | Unset):
        sced2_curve_price_11_to (float | Unset):
        sced2_curve_mw12_from (float | Unset):
        sced2_curve_mw12_to (float | Unset):
        sced2_curve_price_12_from (float | Unset):
        sced2_curve_price_12_to (float | Unset):
        sced2_curve_mw13_from (float | Unset):
        sced2_curve_mw13_to (float | Unset):
        sced2_curve_price_13_from (float | Unset):
        sced2_curve_price_13_to (float | Unset):
        sced2_curve_mw14_from (float | Unset):
        sced2_curve_mw14_to (float | Unset):
        sced2_curve_price_14_from (float | Unset):
        sced2_curve_price_14_to (float | Unset):
        sced2_curve_mw15_from (float | Unset):
        sced2_curve_mw15_to (float | Unset):
        sced2_curve_price_15_from (float | Unset):
        sced2_curve_price_15_to (float | Unset):
        sced2_curve_mw16_from (float | Unset):
        sced2_curve_mw16_to (float | Unset):
        sced2_curve_price_16_from (float | Unset):
        sced2_curve_price_16_to (float | Unset):
        sced2_curve_mw17_from (float | Unset):
        sced2_curve_mw17_to (float | Unset):
        sced2_curve_price_17_from (float | Unset):
        sced2_curve_price_17_to (float | Unset):
        sced2_curve_mw18_from (float | Unset):
        sced2_curve_mw18_to (float | Unset):
        sced2_curve_price_18_from (float | Unset):
        sced2_curve_price_18_to (float | Unset):
        sced2_curve_mw19_from (float | Unset):
        sced2_curve_mw19_to (float | Unset):
        sced2_curve_price_19_from (float | Unset):
        sced2_curve_price_19_to (float | Unset):
        sced2_curve_mw20_from (float | Unset):
        sced2_curve_mw20_to (float | Unset):
        sced2_curve_price_20_from (float | Unset):
        sced2_curve_price_20_to (float | Unset):
        sced2_curve_mw21_from (float | Unset):
        sced2_curve_mw21_to (float | Unset):
        sced2_curve_price_21_from (float | Unset):
        sced2_curve_price_21_to (float | Unset):
        sced2_curve_mw22_from (float | Unset):
        sced2_curve_mw22_to (float | Unset):
        sced2_curve_price_22_from (float | Unset):
        sced2_curve_price_22_to (float | Unset):
        sced2_curve_mw23_from (float | Unset):
        sced2_curve_mw23_to (float | Unset):
        sced2_curve_price_23_from (float | Unset):
        sced2_curve_price_23_to (float | Unset):
        sced2_curve_mw24_from (float | Unset):
        sced2_curve_mw24_to (float | Unset):
        sced2_curve_price_24_from (float | Unset):
        sced2_curve_price_24_to (float | Unset):
        sced2_curve_mw25_from (float | Unset):
        sced2_curve_mw25_to (float | Unset):
        sced2_curve_price_25_from (float | Unset):
        sced2_curve_price_25_to (float | Unset):
        sced2_curve_mw26_from (float | Unset):
        sced2_curve_mw26_to (float | Unset):
        sced2_curve_price_26_from (float | Unset):
        sced2_curve_price_26_to (float | Unset):
        sced2_curve_mw27_from (float | Unset):
        sced2_curve_mw27_to (float | Unset):
        sced2_curve_price_27_from (float | Unset):
        sced2_curve_price_27_to (float | Unset):
        sced2_curve_mw28_from (float | Unset):
        sced2_curve_mw28_to (float | Unset):
        sced2_curve_price_28_from (float | Unset):
        sced2_curve_price_28_to (float | Unset):
        sced2_curve_mw29_from (float | Unset):
        sced2_curve_mw29_to (float | Unset):
        sced2_curve_price_29_from (float | Unset):
        sced2_curve_price_29_to (float | Unset):
        sced2_curve_mw30_from (float | Unset):
        sced2_curve_mw30_to (float | Unset):
        sced2_curve_price_30_from (float | Unset):
        sced2_curve_price_30_to (float | Unset):
        sced2_curve_mw31_from (float | Unset):
        sced2_curve_mw31_to (float | Unset):
        sced2_curve_price_31_from (float | Unset):
        sced2_curve_price_31_to (float | Unset):
        sced2_curve_mw32_from (float | Unset):
        sced2_curve_mw32_to (float | Unset):
        sced2_curve_price_32_from (float | Unset):
        sced2_curve_price_32_to (float | Unset):
        sced2_curve_mw33_from (float | Unset):
        sced2_curve_mw33_to (float | Unset):
        sced2_curve_price_33_from (float | Unset):
        sced2_curve_price_33_to (float | Unset):
        sced2_curve_mw34_from (float | Unset):
        sced2_curve_mw34_to (float | Unset):
        sced2_curve_price_34_from (float | Unset):
        sced2_curve_price_34_to (float | Unset):
        sced2_curve_mw35_from (float | Unset):
        sced2_curve_mw35_to (float | Unset):
        sced2_curve_price_35_from (float | Unset):
        sced2_curve_price_35_to (float | Unset):
        output_schedule_from (float | Unset):
        output_schedule_to (float | Unset):
        hsl_from (float | Unset):
        hsl_to (float | Unset):
        hasl_from (float | Unset):
        hasl_to (float | Unset):
        hdl_from (float | Unset):
        hdl_to (float | Unset):
        lsl_from (float | Unset):
        lsl_to (float | Unset):
        lasl_from (float | Unset):
        lasl_to (float | Unset):
        ldl_from (float | Unset):
        ldl_to (float | Unset):
        telemetered_resource_status (str | Unset):
        base_point_from (float | Unset):
        base_point_to (float | Unset):
        telemetered_net_output_from (float | Unset):
        telemetered_net_output_to (float | Unset):
        asregup_from (float | Unset):
        asregup_to (float | Unset):
        asregdn_from (float | Unset):
        asregdn_to (float | Unset):
        asrrs_from (float | Unset):
        asrrs_to (float | Unset):
        asrrsffr_from (float | Unset):
        asrrsffr_to (float | Unset):
        asnsrs_from (float | Unset):
        asnsrs_to (float | Unset):
        bid_type (str | Unset):
        start_up_cold_offer_from (float | Unset):
        start_up_cold_offer_to (float | Unset):
        start_up_hot_offer_from (float | Unset):
        start_up_hot_offer_to (float | Unset):
        start_up_inter_offer_from (float | Unset):
        start_up_inter_offer_to (float | Unset):
        min_gen_cost_from (float | Unset):
        min_gen_cost_to (float | Unset):
        submitted_tpomw1_from (float | Unset):
        submitted_tpomw1_to (float | Unset):
        submitted_tpo_price_1_from (float | Unset):
        submitted_tpo_price_1_to (float | Unset):
        submitted_tpomw2_from (float | Unset):
        submitted_tpomw2_to (float | Unset):
        submitted_tpo_price_2_from (float | Unset):
        submitted_tpo_price_2_to (float | Unset):
        submitted_tpomw3_from (float | Unset):
        submitted_tpomw3_to (float | Unset):
        submitted_tpo_price_3_from (float | Unset):
        submitted_tpo_price_3_to (float | Unset):
        submitted_tpomw4_from (float | Unset):
        submitted_tpomw4_to (float | Unset):
        submitted_tpo_price_4_from (float | Unset):
        submitted_tpo_price_4_to (float | Unset):
        submitted_tpomw5_from (float | Unset):
        submitted_tpomw5_to (float | Unset):
        submitted_tpo_price_5_from (float | Unset):
        submitted_tpo_price_5_to (float | Unset):
        submitted_tpomw6_from (float | Unset):
        submitted_tpomw6_to (float | Unset):
        submitted_tpo_price_6_from (float | Unset):
        submitted_tpo_price_6_to (float | Unset):
        submitted_tpomw7_from (float | Unset):
        submitted_tpomw7_to (float | Unset):
        submitted_tpo_price_7_from (float | Unset):
        submitted_tpo_price_7_to (float | Unset):
        submitted_tpomw8_from (float | Unset):
        submitted_tpomw8_to (float | Unset):
        submitted_tpo_price_8_from (float | Unset):
        submitted_tpo_price_8_to (float | Unset):
        submitted_tpomw9_from (float | Unset):
        submitted_tpomw9_to (float | Unset):
        submitted_tpo_price_9_from (float | Unset):
        submitted_tpo_price_9_to (float | Unset):
        submitted_tpomw10_from (float | Unset):
        submitted_tpomw10_to (float | Unset):
        submitted_tpo_price_10_from (float | Unset):
        submitted_tpo_price_10_to (float | Unset):
        proxy_extension (str | Unset):
        sced_timestamp_from (str | Unset):
        sced_timestamp_to (str | Unset):
        repeat_hour_flag (bool | Unset):
        qse_name (str | Unset):
        dme_name (str | Unset):
        resource_name (str | Unset):
        resource_type (str | Unset):
        sced1_curve_mw1_from (float | Unset):
        sced1_curve_mw1_to (float | Unset):
        sced1_curve_price_1_from (float | Unset):
        sced1_curve_price_1_to (float | Unset):
        sced1_curve_mw2_from (float | Unset):
        sced1_curve_mw2_to (float | Unset):
        sced1_curve_price_2_from (float | Unset):
        sced1_curve_price_2_to (float | Unset):
        sced1_curve_mw3_from (float | Unset):
        sced1_curve_mw3_to (float | Unset):
        sced1_curve_price_3_from (float | Unset):
        sced1_curve_price_3_to (float | Unset):
        sced1_curve_mw4_from (float | Unset):
        sced1_curve_mw4_to (float | Unset):
        sced1_curve_price_4_from (float | Unset):
        sced1_curve_price_4_to (float | Unset):
        sced1_curve_mw5_from (float | Unset):
        sced1_curve_mw5_to (float | Unset):
        sced1_curve_price_5_from (float | Unset):
        sced1_curve_price_5_to (float | Unset):
        sced1_curve_mw6_from (float | Unset):
        sced1_curve_mw6_to (float | Unset):
        sced1_curve_price_6_from (float | Unset):
        sced1_curve_price_6_to (float | Unset):
        sced1_curve_mw7_from (float | Unset):
        sced1_curve_mw7_to (float | Unset):
        sced1_curve_price_7_from (float | Unset):
        sced1_curve_price_7_to (float | Unset):
        sced1_curve_mw8_from (float | Unset):
        sced1_curve_mw8_to (float | Unset):
        sced1_curve_price_8_from (float | Unset):
        sced1_curve_price_8_to (float | Unset):
        sced1_curve_mw9_from (float | Unset):
        sced1_curve_mw9_to (float | Unset):
        sced1_curve_price_9_from (float | Unset):
        sced1_curve_price_9_to (float | Unset):
        sced1_curve_mw10_from (float | Unset):
        sced1_curve_mw10_to (float | Unset):
        sced1_curve_price_10_from (float | Unset):
        sced1_curve_price_10_to (float | Unset):
        sced1_curve_mw11_from (float | Unset):
        sced1_curve_mw11_to (float | Unset):
        sced1_curve_price_11_from (float | Unset):
        sced1_curve_price_11_to (float | Unset):
        sced1_curve_mw12_from (float | Unset):
        sced1_curve_mw12_to (float | Unset):
        sced1_curve_price_12_from (float | Unset):
        sced1_curve_price_12_to (float | Unset):
        sced1_curve_mw13_from (float | Unset):
        sced1_curve_mw13_to (float | Unset):
        sced1_curve_price_13_from (float | Unset):
        sced1_curve_price_13_to (float | Unset):
        sced1_curve_mw14_from (float | Unset):
        sced1_curve_mw14_to (float | Unset):
        sced1_curve_price_14_from (float | Unset):
        sced1_curve_price_14_to (float | Unset):
        sced1_curve_mw15_from (float | Unset):
        sced1_curve_mw15_to (float | Unset):
        sced1_curve_price_15_from (float | Unset):
        sced1_curve_price_15_to (float | Unset):
        sced1_curve_mw16_from (float | Unset):
        sced1_curve_mw16_to (float | Unset):
        sced1_curve_price_16_from (float | Unset):
        sced1_curve_price_16_to (float | Unset):
        sced1_curve_mw17_from (float | Unset):
        sced1_curve_mw17_to (float | Unset):
        sced1_curve_price_17_from (float | Unset):
        sced1_curve_price_17_to (float | Unset):
        sced1_curve_mw18_from (float | Unset):
        sced1_curve_mw18_to (float | Unset):
        sced1_curve_price_18_from (float | Unset):
        sced1_curve_price_18_to (float | Unset):
        sced1_curve_mw19_from (float | Unset):
        sced1_curve_mw19_to (float | Unset):
        sced1_curve_price_19_from (float | Unset):
        sced1_curve_price_19_to (float | Unset):
        sced1_curve_mw20_from (float | Unset):
        sced1_curve_mw20_to (float | Unset):
        sced1_curve_price_20_from (float | Unset):
        sced1_curve_price_20_to (float | Unset):
        sced1_curve_mw21_from (float | Unset):
        sced1_curve_mw21_to (float | Unset):
        sced1_curve_price_21_from (float | Unset):
        sced1_curve_price_21_to (float | Unset):
        sced1_curve_mw22_from (float | Unset):
        sced1_curve_mw22_to (float | Unset):
        sced1_curve_price_22_from (float | Unset):
        sced1_curve_price_22_to (float | Unset):
        sced1_curve_mw23_from (float | Unset):
        sced1_curve_mw23_to (float | Unset):
        sced1_curve_price_23_from (float | Unset):
        sced1_curve_price_23_to (float | Unset):
        sced1_curve_mw24_from (float | Unset):
        sced1_curve_mw24_to (float | Unset):
        sced1_curve_price_24_from (float | Unset):
        sced1_curve_price_24_to (float | Unset):
        sced1_curve_mw25_from (float | Unset):
        sced1_curve_mw25_to (float | Unset):
        sced1_curve_price_25_from (float | Unset):
        sced1_curve_price_25_to (float | Unset):
        sced1_curve_mw26_from (float | Unset):
        sced1_curve_mw26_to (float | Unset):
        sced1_curve_price_26_from (float | Unset):
        sced1_curve_price_26_to (float | Unset):
        sced1_curve_mw27_from (float | Unset):
        sced1_curve_mw27_to (float | Unset):
        sced1_curve_price_27_from (float | Unset):
        sced1_curve_price_27_to (float | Unset):
        sced1_curve_mw28_from (float | Unset):
        sced1_curve_mw28_to (float | Unset):
        sced1_curve_price_28_from (float | Unset):
        sced1_curve_price_28_to (float | Unset):
        sced1_curve_mw29_from (float | Unset):
        sced1_curve_mw29_to (float | Unset):
        sced1_curve_price_29_from (float | Unset):
        sced1_curve_price_29_to (float | Unset):
        sced1_curve_mw30_from (float | Unset):
        sced1_curve_mw30_to (float | Unset):
        sced1_curve_price_30_from (float | Unset):
        sced1_curve_price_30_to (float | Unset):
        sced1_curve_mw31_from (float | Unset):
        sced1_curve_mw31_to (float | Unset):
        sced1_curve_price_31_from (float | Unset):
        sced1_curve_price_31_to (float | Unset):
        sced1_curve_mw32_from (float | Unset):
        sced1_curve_mw32_to (float | Unset):
        sced1_curve_price_32_from (float | Unset):
        sced1_curve_price_32_to (float | Unset):
        sced1_curve_mw33_from (float | Unset):
        sced1_curve_mw33_to (float | Unset):
        sced1_curve_price_33_from (float | Unset):
        sced1_curve_price_33_to (float | Unset):
        sced1_curve_mw34_from (float | Unset):
        sced1_curve_mw34_to (float | Unset):
        sced1_curve_price_34_from (float | Unset):
        sced1_curve_price_34_to (float | Unset):
        sced1_curve_mw35_from (float | Unset):
        sced1_curve_mw35_to (float | Unset):
        sced1_curve_price_35_from (float | Unset):
        sced1_curve_price_35_to (float | Unset):
        sced2_curve_mw1_from (float | Unset):
        sced2_curve_mw1_to (float | Unset):
        sced2_curve_price_1_from (float | Unset):
        sced2_curve_price_1_to (float | Unset):
        sced2_curve_mw2_from (float | Unset):
        sced2_curve_mw2_to (float | Unset):
        sced2_curve_price_2_from (float | Unset):
        sced2_curve_price_2_to (float | Unset):
        sced2_curve_mw3_from (float | Unset):
        sced2_curve_mw3_to (float | Unset):
        sced2_curve_price_3_from (float | Unset):
        sced2_curve_price_3_to (float | Unset):
        sced2_curve_mw4_from (float | Unset):
        sced2_curve_mw4_to (float | Unset):
        sced2_curve_price_4_from (float | Unset):
        sced2_curve_price_4_to (float | Unset):
        sced2_curve_mw5_from (float | Unset):
        sced2_curve_mw5_to (float | Unset):
        sced2_curve_price_5_from (float | Unset):
        sced2_curve_price_5_to (float | Unset):
        sced2_curve_mw6_from (float | Unset):
        sced2_curve_mw6_to (float | Unset):
        sced2_curve_price_6_from (float | Unset):
        sced2_curve_price_6_to (float | Unset):
        sced2_curve_mw7_from (float | Unset):
        sced2_curve_mw7_to (float | Unset):
        sced2_curve_price_7_from (float | Unset):
        sced2_curve_price_7_to (float | Unset):
        sced2_curve_mw8_from (float | Unset):
        sced2_curve_mw8_to (float | Unset):
        sced2_curve_price_8_from (float | Unset):
        sced2_curve_price_8_to (float | Unset):
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
            sced2_curve_mw9_from=sced2_curve_mw9_from,
            sced2_curve_mw9_to=sced2_curve_mw9_to,
            sced2_curve_price_9_from=sced2_curve_price_9_from,
            sced2_curve_price_9_to=sced2_curve_price_9_to,
            sced2_curve_mw10_from=sced2_curve_mw10_from,
            sced2_curve_mw10_to=sced2_curve_mw10_to,
            sced2_curve_price_10_from=sced2_curve_price_10_from,
            sced2_curve_price_10_to=sced2_curve_price_10_to,
            sced2_curve_mw11_from=sced2_curve_mw11_from,
            sced2_curve_mw11_to=sced2_curve_mw11_to,
            sced2_curve_price_11_from=sced2_curve_price_11_from,
            sced2_curve_price_11_to=sced2_curve_price_11_to,
            sced2_curve_mw12_from=sced2_curve_mw12_from,
            sced2_curve_mw12_to=sced2_curve_mw12_to,
            sced2_curve_price_12_from=sced2_curve_price_12_from,
            sced2_curve_price_12_to=sced2_curve_price_12_to,
            sced2_curve_mw13_from=sced2_curve_mw13_from,
            sced2_curve_mw13_to=sced2_curve_mw13_to,
            sced2_curve_price_13_from=sced2_curve_price_13_from,
            sced2_curve_price_13_to=sced2_curve_price_13_to,
            sced2_curve_mw14_from=sced2_curve_mw14_from,
            sced2_curve_mw14_to=sced2_curve_mw14_to,
            sced2_curve_price_14_from=sced2_curve_price_14_from,
            sced2_curve_price_14_to=sced2_curve_price_14_to,
            sced2_curve_mw15_from=sced2_curve_mw15_from,
            sced2_curve_mw15_to=sced2_curve_mw15_to,
            sced2_curve_price_15_from=sced2_curve_price_15_from,
            sced2_curve_price_15_to=sced2_curve_price_15_to,
            sced2_curve_mw16_from=sced2_curve_mw16_from,
            sced2_curve_mw16_to=sced2_curve_mw16_to,
            sced2_curve_price_16_from=sced2_curve_price_16_from,
            sced2_curve_price_16_to=sced2_curve_price_16_to,
            sced2_curve_mw17_from=sced2_curve_mw17_from,
            sced2_curve_mw17_to=sced2_curve_mw17_to,
            sced2_curve_price_17_from=sced2_curve_price_17_from,
            sced2_curve_price_17_to=sced2_curve_price_17_to,
            sced2_curve_mw18_from=sced2_curve_mw18_from,
            sced2_curve_mw18_to=sced2_curve_mw18_to,
            sced2_curve_price_18_from=sced2_curve_price_18_from,
            sced2_curve_price_18_to=sced2_curve_price_18_to,
            sced2_curve_mw19_from=sced2_curve_mw19_from,
            sced2_curve_mw19_to=sced2_curve_mw19_to,
            sced2_curve_price_19_from=sced2_curve_price_19_from,
            sced2_curve_price_19_to=sced2_curve_price_19_to,
            sced2_curve_mw20_from=sced2_curve_mw20_from,
            sced2_curve_mw20_to=sced2_curve_mw20_to,
            sced2_curve_price_20_from=sced2_curve_price_20_from,
            sced2_curve_price_20_to=sced2_curve_price_20_to,
            sced2_curve_mw21_from=sced2_curve_mw21_from,
            sced2_curve_mw21_to=sced2_curve_mw21_to,
            sced2_curve_price_21_from=sced2_curve_price_21_from,
            sced2_curve_price_21_to=sced2_curve_price_21_to,
            sced2_curve_mw22_from=sced2_curve_mw22_from,
            sced2_curve_mw22_to=sced2_curve_mw22_to,
            sced2_curve_price_22_from=sced2_curve_price_22_from,
            sced2_curve_price_22_to=sced2_curve_price_22_to,
            sced2_curve_mw23_from=sced2_curve_mw23_from,
            sced2_curve_mw23_to=sced2_curve_mw23_to,
            sced2_curve_price_23_from=sced2_curve_price_23_from,
            sced2_curve_price_23_to=sced2_curve_price_23_to,
            sced2_curve_mw24_from=sced2_curve_mw24_from,
            sced2_curve_mw24_to=sced2_curve_mw24_to,
            sced2_curve_price_24_from=sced2_curve_price_24_from,
            sced2_curve_price_24_to=sced2_curve_price_24_to,
            sced2_curve_mw25_from=sced2_curve_mw25_from,
            sced2_curve_mw25_to=sced2_curve_mw25_to,
            sced2_curve_price_25_from=sced2_curve_price_25_from,
            sced2_curve_price_25_to=sced2_curve_price_25_to,
            sced2_curve_mw26_from=sced2_curve_mw26_from,
            sced2_curve_mw26_to=sced2_curve_mw26_to,
            sced2_curve_price_26_from=sced2_curve_price_26_from,
            sced2_curve_price_26_to=sced2_curve_price_26_to,
            sced2_curve_mw27_from=sced2_curve_mw27_from,
            sced2_curve_mw27_to=sced2_curve_mw27_to,
            sced2_curve_price_27_from=sced2_curve_price_27_from,
            sced2_curve_price_27_to=sced2_curve_price_27_to,
            sced2_curve_mw28_from=sced2_curve_mw28_from,
            sced2_curve_mw28_to=sced2_curve_mw28_to,
            sced2_curve_price_28_from=sced2_curve_price_28_from,
            sced2_curve_price_28_to=sced2_curve_price_28_to,
            sced2_curve_mw29_from=sced2_curve_mw29_from,
            sced2_curve_mw29_to=sced2_curve_mw29_to,
            sced2_curve_price_29_from=sced2_curve_price_29_from,
            sced2_curve_price_29_to=sced2_curve_price_29_to,
            sced2_curve_mw30_from=sced2_curve_mw30_from,
            sced2_curve_mw30_to=sced2_curve_mw30_to,
            sced2_curve_price_30_from=sced2_curve_price_30_from,
            sced2_curve_price_30_to=sced2_curve_price_30_to,
            sced2_curve_mw31_from=sced2_curve_mw31_from,
            sced2_curve_mw31_to=sced2_curve_mw31_to,
            sced2_curve_price_31_from=sced2_curve_price_31_from,
            sced2_curve_price_31_to=sced2_curve_price_31_to,
            sced2_curve_mw32_from=sced2_curve_mw32_from,
            sced2_curve_mw32_to=sced2_curve_mw32_to,
            sced2_curve_price_32_from=sced2_curve_price_32_from,
            sced2_curve_price_32_to=sced2_curve_price_32_to,
            sced2_curve_mw33_from=sced2_curve_mw33_from,
            sced2_curve_mw33_to=sced2_curve_mw33_to,
            sced2_curve_price_33_from=sced2_curve_price_33_from,
            sced2_curve_price_33_to=sced2_curve_price_33_to,
            sced2_curve_mw34_from=sced2_curve_mw34_from,
            sced2_curve_mw34_to=sced2_curve_mw34_to,
            sced2_curve_price_34_from=sced2_curve_price_34_from,
            sced2_curve_price_34_to=sced2_curve_price_34_to,
            sced2_curve_mw35_from=sced2_curve_mw35_from,
            sced2_curve_mw35_to=sced2_curve_mw35_to,
            sced2_curve_price_35_from=sced2_curve_price_35_from,
            sced2_curve_price_35_to=sced2_curve_price_35_to,
            output_schedule_from=output_schedule_from,
            output_schedule_to=output_schedule_to,
            hsl_from=hsl_from,
            hsl_to=hsl_to,
            hasl_from=hasl_from,
            hasl_to=hasl_to,
            hdl_from=hdl_from,
            hdl_to=hdl_to,
            lsl_from=lsl_from,
            lsl_to=lsl_to,
            lasl_from=lasl_from,
            lasl_to=lasl_to,
            ldl_from=ldl_from,
            ldl_to=ldl_to,
            telemetered_resource_status=telemetered_resource_status,
            base_point_from=base_point_from,
            base_point_to=base_point_to,
            telemetered_net_output_from=telemetered_net_output_from,
            telemetered_net_output_to=telemetered_net_output_to,
            asregup_from=asregup_from,
            asregup_to=asregup_to,
            asregdn_from=asregdn_from,
            asregdn_to=asregdn_to,
            asrrs_from=asrrs_from,
            asrrs_to=asrrs_to,
            asrrsffr_from=asrrsffr_from,
            asrrsffr_to=asrrsffr_to,
            asnsrs_from=asnsrs_from,
            asnsrs_to=asnsrs_to,
            bid_type=bid_type,
            start_up_cold_offer_from=start_up_cold_offer_from,
            start_up_cold_offer_to=start_up_cold_offer_to,
            start_up_hot_offer_from=start_up_hot_offer_from,
            start_up_hot_offer_to=start_up_hot_offer_to,
            start_up_inter_offer_from=start_up_inter_offer_from,
            start_up_inter_offer_to=start_up_inter_offer_to,
            min_gen_cost_from=min_gen_cost_from,
            min_gen_cost_to=min_gen_cost_to,
            submitted_tpomw1_from=submitted_tpomw1_from,
            submitted_tpomw1_to=submitted_tpomw1_to,
            submitted_tpo_price_1_from=submitted_tpo_price_1_from,
            submitted_tpo_price_1_to=submitted_tpo_price_1_to,
            submitted_tpomw2_from=submitted_tpomw2_from,
            submitted_tpomw2_to=submitted_tpomw2_to,
            submitted_tpo_price_2_from=submitted_tpo_price_2_from,
            submitted_tpo_price_2_to=submitted_tpo_price_2_to,
            submitted_tpomw3_from=submitted_tpomw3_from,
            submitted_tpomw3_to=submitted_tpomw3_to,
            submitted_tpo_price_3_from=submitted_tpo_price_3_from,
            submitted_tpo_price_3_to=submitted_tpo_price_3_to,
            submitted_tpomw4_from=submitted_tpomw4_from,
            submitted_tpomw4_to=submitted_tpomw4_to,
            submitted_tpo_price_4_from=submitted_tpo_price_4_from,
            submitted_tpo_price_4_to=submitted_tpo_price_4_to,
            submitted_tpomw5_from=submitted_tpomw5_from,
            submitted_tpomw5_to=submitted_tpomw5_to,
            submitted_tpo_price_5_from=submitted_tpo_price_5_from,
            submitted_tpo_price_5_to=submitted_tpo_price_5_to,
            submitted_tpomw6_from=submitted_tpomw6_from,
            submitted_tpomw6_to=submitted_tpomw6_to,
            submitted_tpo_price_6_from=submitted_tpo_price_6_from,
            submitted_tpo_price_6_to=submitted_tpo_price_6_to,
            submitted_tpomw7_from=submitted_tpomw7_from,
            submitted_tpomw7_to=submitted_tpomw7_to,
            submitted_tpo_price_7_from=submitted_tpo_price_7_from,
            submitted_tpo_price_7_to=submitted_tpo_price_7_to,
            submitted_tpomw8_from=submitted_tpomw8_from,
            submitted_tpomw8_to=submitted_tpomw8_to,
            submitted_tpo_price_8_from=submitted_tpo_price_8_from,
            submitted_tpo_price_8_to=submitted_tpo_price_8_to,
            submitted_tpomw9_from=submitted_tpomw9_from,
            submitted_tpomw9_to=submitted_tpomw9_to,
            submitted_tpo_price_9_from=submitted_tpo_price_9_from,
            submitted_tpo_price_9_to=submitted_tpo_price_9_to,
            submitted_tpomw10_from=submitted_tpomw10_from,
            submitted_tpomw10_to=submitted_tpomw10_to,
            submitted_tpo_price_10_from=submitted_tpo_price_10_from,
            submitted_tpo_price_10_to=submitted_tpo_price_10_to,
            proxy_extension=proxy_extension,
            sced_timestamp_from=sced_timestamp_from,
            sced_timestamp_to=sced_timestamp_to,
            repeat_hour_flag=repeat_hour_flag,
            qse_name=qse_name,
            dme_name=dme_name,
            resource_name=resource_name,
            resource_type=resource_type,
            sced1_curve_mw1_from=sced1_curve_mw1_from,
            sced1_curve_mw1_to=sced1_curve_mw1_to,
            sced1_curve_price_1_from=sced1_curve_price_1_from,
            sced1_curve_price_1_to=sced1_curve_price_1_to,
            sced1_curve_mw2_from=sced1_curve_mw2_from,
            sced1_curve_mw2_to=sced1_curve_mw2_to,
            sced1_curve_price_2_from=sced1_curve_price_2_from,
            sced1_curve_price_2_to=sced1_curve_price_2_to,
            sced1_curve_mw3_from=sced1_curve_mw3_from,
            sced1_curve_mw3_to=sced1_curve_mw3_to,
            sced1_curve_price_3_from=sced1_curve_price_3_from,
            sced1_curve_price_3_to=sced1_curve_price_3_to,
            sced1_curve_mw4_from=sced1_curve_mw4_from,
            sced1_curve_mw4_to=sced1_curve_mw4_to,
            sced1_curve_price_4_from=sced1_curve_price_4_from,
            sced1_curve_price_4_to=sced1_curve_price_4_to,
            sced1_curve_mw5_from=sced1_curve_mw5_from,
            sced1_curve_mw5_to=sced1_curve_mw5_to,
            sced1_curve_price_5_from=sced1_curve_price_5_from,
            sced1_curve_price_5_to=sced1_curve_price_5_to,
            sced1_curve_mw6_from=sced1_curve_mw6_from,
            sced1_curve_mw6_to=sced1_curve_mw6_to,
            sced1_curve_price_6_from=sced1_curve_price_6_from,
            sced1_curve_price_6_to=sced1_curve_price_6_to,
            sced1_curve_mw7_from=sced1_curve_mw7_from,
            sced1_curve_mw7_to=sced1_curve_mw7_to,
            sced1_curve_price_7_from=sced1_curve_price_7_from,
            sced1_curve_price_7_to=sced1_curve_price_7_to,
            sced1_curve_mw8_from=sced1_curve_mw8_from,
            sced1_curve_mw8_to=sced1_curve_mw8_to,
            sced1_curve_price_8_from=sced1_curve_price_8_from,
            sced1_curve_price_8_to=sced1_curve_price_8_to,
            sced1_curve_mw9_from=sced1_curve_mw9_from,
            sced1_curve_mw9_to=sced1_curve_mw9_to,
            sced1_curve_price_9_from=sced1_curve_price_9_from,
            sced1_curve_price_9_to=sced1_curve_price_9_to,
            sced1_curve_mw10_from=sced1_curve_mw10_from,
            sced1_curve_mw10_to=sced1_curve_mw10_to,
            sced1_curve_price_10_from=sced1_curve_price_10_from,
            sced1_curve_price_10_to=sced1_curve_price_10_to,
            sced1_curve_mw11_from=sced1_curve_mw11_from,
            sced1_curve_mw11_to=sced1_curve_mw11_to,
            sced1_curve_price_11_from=sced1_curve_price_11_from,
            sced1_curve_price_11_to=sced1_curve_price_11_to,
            sced1_curve_mw12_from=sced1_curve_mw12_from,
            sced1_curve_mw12_to=sced1_curve_mw12_to,
            sced1_curve_price_12_from=sced1_curve_price_12_from,
            sced1_curve_price_12_to=sced1_curve_price_12_to,
            sced1_curve_mw13_from=sced1_curve_mw13_from,
            sced1_curve_mw13_to=sced1_curve_mw13_to,
            sced1_curve_price_13_from=sced1_curve_price_13_from,
            sced1_curve_price_13_to=sced1_curve_price_13_to,
            sced1_curve_mw14_from=sced1_curve_mw14_from,
            sced1_curve_mw14_to=sced1_curve_mw14_to,
            sced1_curve_price_14_from=sced1_curve_price_14_from,
            sced1_curve_price_14_to=sced1_curve_price_14_to,
            sced1_curve_mw15_from=sced1_curve_mw15_from,
            sced1_curve_mw15_to=sced1_curve_mw15_to,
            sced1_curve_price_15_from=sced1_curve_price_15_from,
            sced1_curve_price_15_to=sced1_curve_price_15_to,
            sced1_curve_mw16_from=sced1_curve_mw16_from,
            sced1_curve_mw16_to=sced1_curve_mw16_to,
            sced1_curve_price_16_from=sced1_curve_price_16_from,
            sced1_curve_price_16_to=sced1_curve_price_16_to,
            sced1_curve_mw17_from=sced1_curve_mw17_from,
            sced1_curve_mw17_to=sced1_curve_mw17_to,
            sced1_curve_price_17_from=sced1_curve_price_17_from,
            sced1_curve_price_17_to=sced1_curve_price_17_to,
            sced1_curve_mw18_from=sced1_curve_mw18_from,
            sced1_curve_mw18_to=sced1_curve_mw18_to,
            sced1_curve_price_18_from=sced1_curve_price_18_from,
            sced1_curve_price_18_to=sced1_curve_price_18_to,
            sced1_curve_mw19_from=sced1_curve_mw19_from,
            sced1_curve_mw19_to=sced1_curve_mw19_to,
            sced1_curve_price_19_from=sced1_curve_price_19_from,
            sced1_curve_price_19_to=sced1_curve_price_19_to,
            sced1_curve_mw20_from=sced1_curve_mw20_from,
            sced1_curve_mw20_to=sced1_curve_mw20_to,
            sced1_curve_price_20_from=sced1_curve_price_20_from,
            sced1_curve_price_20_to=sced1_curve_price_20_to,
            sced1_curve_mw21_from=sced1_curve_mw21_from,
            sced1_curve_mw21_to=sced1_curve_mw21_to,
            sced1_curve_price_21_from=sced1_curve_price_21_from,
            sced1_curve_price_21_to=sced1_curve_price_21_to,
            sced1_curve_mw22_from=sced1_curve_mw22_from,
            sced1_curve_mw22_to=sced1_curve_mw22_to,
            sced1_curve_price_22_from=sced1_curve_price_22_from,
            sced1_curve_price_22_to=sced1_curve_price_22_to,
            sced1_curve_mw23_from=sced1_curve_mw23_from,
            sced1_curve_mw23_to=sced1_curve_mw23_to,
            sced1_curve_price_23_from=sced1_curve_price_23_from,
            sced1_curve_price_23_to=sced1_curve_price_23_to,
            sced1_curve_mw24_from=sced1_curve_mw24_from,
            sced1_curve_mw24_to=sced1_curve_mw24_to,
            sced1_curve_price_24_from=sced1_curve_price_24_from,
            sced1_curve_price_24_to=sced1_curve_price_24_to,
            sced1_curve_mw25_from=sced1_curve_mw25_from,
            sced1_curve_mw25_to=sced1_curve_mw25_to,
            sced1_curve_price_25_from=sced1_curve_price_25_from,
            sced1_curve_price_25_to=sced1_curve_price_25_to,
            sced1_curve_mw26_from=sced1_curve_mw26_from,
            sced1_curve_mw26_to=sced1_curve_mw26_to,
            sced1_curve_price_26_from=sced1_curve_price_26_from,
            sced1_curve_price_26_to=sced1_curve_price_26_to,
            sced1_curve_mw27_from=sced1_curve_mw27_from,
            sced1_curve_mw27_to=sced1_curve_mw27_to,
            sced1_curve_price_27_from=sced1_curve_price_27_from,
            sced1_curve_price_27_to=sced1_curve_price_27_to,
            sced1_curve_mw28_from=sced1_curve_mw28_from,
            sced1_curve_mw28_to=sced1_curve_mw28_to,
            sced1_curve_price_28_from=sced1_curve_price_28_from,
            sced1_curve_price_28_to=sced1_curve_price_28_to,
            sced1_curve_mw29_from=sced1_curve_mw29_from,
            sced1_curve_mw29_to=sced1_curve_mw29_to,
            sced1_curve_price_29_from=sced1_curve_price_29_from,
            sced1_curve_price_29_to=sced1_curve_price_29_to,
            sced1_curve_mw30_from=sced1_curve_mw30_from,
            sced1_curve_mw30_to=sced1_curve_mw30_to,
            sced1_curve_price_30_from=sced1_curve_price_30_from,
            sced1_curve_price_30_to=sced1_curve_price_30_to,
            sced1_curve_mw31_from=sced1_curve_mw31_from,
            sced1_curve_mw31_to=sced1_curve_mw31_to,
            sced1_curve_price_31_from=sced1_curve_price_31_from,
            sced1_curve_price_31_to=sced1_curve_price_31_to,
            sced1_curve_mw32_from=sced1_curve_mw32_from,
            sced1_curve_mw32_to=sced1_curve_mw32_to,
            sced1_curve_price_32_from=sced1_curve_price_32_from,
            sced1_curve_price_32_to=sced1_curve_price_32_to,
            sced1_curve_mw33_from=sced1_curve_mw33_from,
            sced1_curve_mw33_to=sced1_curve_mw33_to,
            sced1_curve_price_33_from=sced1_curve_price_33_from,
            sced1_curve_price_33_to=sced1_curve_price_33_to,
            sced1_curve_mw34_from=sced1_curve_mw34_from,
            sced1_curve_mw34_to=sced1_curve_mw34_to,
            sced1_curve_price_34_from=sced1_curve_price_34_from,
            sced1_curve_price_34_to=sced1_curve_price_34_to,
            sced1_curve_mw35_from=sced1_curve_mw35_from,
            sced1_curve_mw35_to=sced1_curve_mw35_to,
            sced1_curve_price_35_from=sced1_curve_price_35_from,
            sced1_curve_price_35_to=sced1_curve_price_35_to,
            sced2_curve_mw1_from=sced2_curve_mw1_from,
            sced2_curve_mw1_to=sced2_curve_mw1_to,
            sced2_curve_price_1_from=sced2_curve_price_1_from,
            sced2_curve_price_1_to=sced2_curve_price_1_to,
            sced2_curve_mw2_from=sced2_curve_mw2_from,
            sced2_curve_mw2_to=sced2_curve_mw2_to,
            sced2_curve_price_2_from=sced2_curve_price_2_from,
            sced2_curve_price_2_to=sced2_curve_price_2_to,
            sced2_curve_mw3_from=sced2_curve_mw3_from,
            sced2_curve_mw3_to=sced2_curve_mw3_to,
            sced2_curve_price_3_from=sced2_curve_price_3_from,
            sced2_curve_price_3_to=sced2_curve_price_3_to,
            sced2_curve_mw4_from=sced2_curve_mw4_from,
            sced2_curve_mw4_to=sced2_curve_mw4_to,
            sced2_curve_price_4_from=sced2_curve_price_4_from,
            sced2_curve_price_4_to=sced2_curve_price_4_to,
            sced2_curve_mw5_from=sced2_curve_mw5_from,
            sced2_curve_mw5_to=sced2_curve_mw5_to,
            sced2_curve_price_5_from=sced2_curve_price_5_from,
            sced2_curve_price_5_to=sced2_curve_price_5_to,
            sced2_curve_mw6_from=sced2_curve_mw6_from,
            sced2_curve_mw6_to=sced2_curve_mw6_to,
            sced2_curve_price_6_from=sced2_curve_price_6_from,
            sced2_curve_price_6_to=sced2_curve_price_6_to,
            sced2_curve_mw7_from=sced2_curve_mw7_from,
            sced2_curve_mw7_to=sced2_curve_mw7_to,
            sced2_curve_price_7_from=sced2_curve_price_7_from,
            sced2_curve_price_7_to=sced2_curve_price_7_to,
            sced2_curve_mw8_from=sced2_curve_mw8_from,
            sced2_curve_mw8_to=sced2_curve_mw8_to,
            sced2_curve_price_8_from=sced2_curve_price_8_from,
            sced2_curve_price_8_to=sced2_curve_price_8_to,
            page=page,
            size=size,
            sort=sort,
            dir_=dir_,
        )
    ).parsed
