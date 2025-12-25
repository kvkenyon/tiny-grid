from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.info import Info


T = TypeVar("T", bound="Version")


@_attrs_define
class Version:
    """
    Attributes:
        info (Info | Unset):
        openapi (str | Unset):
    """

    info: Info | Unset = UNSET
    openapi: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        info: dict[str, Any] | Unset = UNSET
        if not isinstance(self.info, Unset):
            info = self.info.to_dict()

        openapi = self.openapi

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if info is not UNSET:
            field_dict["info"] = info
        if openapi is not UNSET:
            field_dict["openapi"] = openapi

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.info import Info

        d = dict(src_dict)
        _info = d.pop("info", UNSET)
        info: Info | Unset
        if isinstance(_info, Unset):
            info = UNSET
        else:
            info = Info.from_dict(_info)

        openapi = d.pop("openapi", UNSET)

        version = cls(
            info=info,
            openapi=openapi,
        )

        version.additional_properties = d
        return version

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
