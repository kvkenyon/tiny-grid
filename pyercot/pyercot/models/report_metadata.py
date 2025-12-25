from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ReportMetadata")


@_attrs_define
class ReportMetadata:
    """Represents metadata for the specified object.

    Attributes:
        report_name (str | Unset):
        report_display_name (str | Unset):
        report_id (str | Unset):
        report_emil (str | Unset):
    """

    report_name: str | Unset = UNSET
    report_display_name: str | Unset = UNSET
    report_id: str | Unset = UNSET
    report_emil: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        report_name = self.report_name

        report_display_name = self.report_display_name

        report_id = self.report_id

        report_emil = self.report_emil

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if report_name is not UNSET:
            field_dict["reportName"] = report_name
        if report_display_name is not UNSET:
            field_dict["reportDisplayName"] = report_display_name
        if report_id is not UNSET:
            field_dict["reportId"] = report_id
        if report_emil is not UNSET:
            field_dict["reportEMIL"] = report_emil

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        report_name = d.pop("reportName", UNSET)

        report_display_name = d.pop("reportDisplayName", UNSET)

        report_id = d.pop("reportId", UNSET)

        report_emil = d.pop("reportEMIL", UNSET)

        report_metadata = cls(
            report_name=report_name,
            report_display_name=report_display_name,
            report_id=report_id,
            report_emil=report_emil,
        )

        report_metadata.additional_properties = d
        return report_metadata

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
