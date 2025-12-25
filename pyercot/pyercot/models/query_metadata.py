from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.query_metadata_parameters import QueryMetadataParameters


T = TypeVar("T", bound="QueryMetadata")


@_attrs_define
class QueryMetadata:
    """Represents query parameter summary for the specified query results.

    Attributes:
        parameter_count (int | Unset):
        parameters (QueryMetadataParameters | Unset):
        sorted_by (str | Unset):
    """

    parameter_count: int | Unset = UNSET
    parameters: QueryMetadataParameters | Unset = UNSET
    sorted_by: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        parameter_count = self.parameter_count

        parameters: dict[str, Any] | Unset = UNSET
        if not isinstance(self.parameters, Unset):
            parameters = self.parameters.to_dict()

        sorted_by = self.sorted_by

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if parameter_count is not UNSET:
            field_dict["parameterCount"] = parameter_count
        if parameters is not UNSET:
            field_dict["parameters"] = parameters
        if sorted_by is not UNSET:
            field_dict["sortedBy"] = sorted_by

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.query_metadata_parameters import QueryMetadataParameters

        d = dict(src_dict)
        parameter_count = d.pop("parameterCount", UNSET)

        _parameters = d.pop("parameters", UNSET)
        parameters: QueryMetadataParameters | Unset
        if isinstance(_parameters, Unset):
            parameters = UNSET
        else:
            parameters = QueryMetadataParameters.from_dict(_parameters)

        sorted_by = d.pop("sortedBy", UNSET)

        query_metadata = cls(
            parameter_count=parameter_count,
            parameters=parameters,
            sorted_by=sorted_by,
        )

        query_metadata.additional_properties = d
        return query_metadata

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
