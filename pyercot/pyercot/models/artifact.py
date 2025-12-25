from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.link import Link


T = TypeVar("T", bound="Artifact")


@_attrs_define
class Artifact:
    """Each artifact represents a single report for the given time period designated by the EMIL metadata.

    Attributes:
        display_name (str):
        report_type_id (int | Unset):
        endpoint (str | Unset):
        links (list[Link] | Unset):
    """

    display_name: str
    report_type_id: int | Unset = UNSET
    endpoint: str | Unset = UNSET
    links: list[Link] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        display_name = self.display_name

        report_type_id = self.report_type_id

        endpoint = self.endpoint

        links: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.links, Unset):
            links = []
            for links_item_data in self.links:
                links_item = links_item_data.to_dict()
                links.append(links_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "displayName": display_name,
            }
        )
        if report_type_id is not UNSET:
            field_dict["reportTypeId"] = report_type_id
        if endpoint is not UNSET:
            field_dict["endpoint"] = endpoint
        if links is not UNSET:
            field_dict["links"] = links

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.link import Link

        d = dict(src_dict)
        display_name = d.pop("displayName")

        report_type_id = d.pop("reportTypeId", UNSET)

        endpoint = d.pop("endpoint", UNSET)

        _links = d.pop("links", UNSET)
        links: list[Link] | Unset = UNSET
        if _links is not UNSET:
            links = []
            for links_item_data in _links:
                links_item = Link.from_dict(links_item_data)

                links.append(links_item)

        artifact = cls(
            display_name=display_name,
            report_type_id=report_type_id,
            endpoint=endpoint,
            links=links,
        )

        artifact.additional_properties = d
        return artifact

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
