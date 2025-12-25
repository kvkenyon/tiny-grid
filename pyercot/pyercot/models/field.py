from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.field_data_type import FieldDataType
from ..types import UNSET, Unset

T = TypeVar("T", bound="Field")


@_attrs_define
class Field:
    """Represents report data field.

    Attributes:
        name (str | Unset):
        label (str | Unset):
        cardinality (int | Unset):
        data_type (FieldDataType | Unset):
        searchable (bool | Unset):
        sortable (bool | Unset):
        has_range (bool | Unset):
    """

    name: str | Unset = UNSET
    label: str | Unset = UNSET
    cardinality: int | Unset = UNSET
    data_type: FieldDataType | Unset = UNSET
    searchable: bool | Unset = UNSET
    sortable: bool | Unset = UNSET
    has_range: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        label = self.label

        cardinality = self.cardinality

        data_type: str | Unset = UNSET
        if not isinstance(self.data_type, Unset):
            data_type = self.data_type.value

        searchable = self.searchable

        sortable = self.sortable

        has_range = self.has_range

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if label is not UNSET:
            field_dict["label"] = label
        if cardinality is not UNSET:
            field_dict["cardinality"] = cardinality
        if data_type is not UNSET:
            field_dict["dataType"] = data_type
        if searchable is not UNSET:
            field_dict["searchable"] = searchable
        if sortable is not UNSET:
            field_dict["sortable"] = sortable
        if has_range is not UNSET:
            field_dict["hasRange"] = has_range

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name", UNSET)

        label = d.pop("label", UNSET)

        cardinality = d.pop("cardinality", UNSET)

        _data_type = d.pop("dataType", UNSET)
        data_type: FieldDataType | Unset
        if isinstance(_data_type, Unset):
            data_type = UNSET
        else:
            data_type = FieldDataType(_data_type)

        searchable = d.pop("searchable", UNSET)

        sortable = d.pop("sortable", UNSET)

        has_range = d.pop("hasRange", UNSET)

        field = cls(
            name=name,
            label=label,
            cardinality=cardinality,
            data_type=data_type,
            searchable=searchable,
            sortable=sortable,
            has_range=has_range,
        )

        field.additional_properties = d
        return field

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
