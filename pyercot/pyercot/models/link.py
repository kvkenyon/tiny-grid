from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Link")


@_attrs_define
class Link:
    """
    Attributes:
        rel (str | Unset):
        href (str | Unset):
        hreflang (str | Unset):
        media (str | Unset):
        title (str | Unset):
        type_ (str | Unset):
        deprecation (str | Unset):
        profile (str | Unset):
        name (str | Unset):
    """

    rel: str | Unset = UNSET
    href: str | Unset = UNSET
    hreflang: str | Unset = UNSET
    media: str | Unset = UNSET
    title: str | Unset = UNSET
    type_: str | Unset = UNSET
    deprecation: str | Unset = UNSET
    profile: str | Unset = UNSET
    name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        rel = self.rel

        href = self.href

        hreflang = self.hreflang

        media = self.media

        title = self.title

        type_ = self.type_

        deprecation = self.deprecation

        profile = self.profile

        name = self.name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if rel is not UNSET:
            field_dict["rel"] = rel
        if href is not UNSET:
            field_dict["href"] = href
        if hreflang is not UNSET:
            field_dict["hreflang"] = hreflang
        if media is not UNSET:
            field_dict["media"] = media
        if title is not UNSET:
            field_dict["title"] = title
        if type_ is not UNSET:
            field_dict["type"] = type_
        if deprecation is not UNSET:
            field_dict["deprecation"] = deprecation
        if profile is not UNSET:
            field_dict["profile"] = profile
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        rel = d.pop("rel", UNSET)

        href = d.pop("href", UNSET)

        hreflang = d.pop("hreflang", UNSET)

        media = d.pop("media", UNSET)

        title = d.pop("title", UNSET)

        type_ = d.pop("type", UNSET)

        deprecation = d.pop("deprecation", UNSET)

        profile = d.pop("profile", UNSET)

        name = d.pop("name", UNSET)

        link = cls(
            rel=rel,
            href=href,
            hreflang=hreflang,
            media=media,
            title=title,
            type_=type_,
            deprecation=deprecation,
            profile=profile,
            name=name,
        )

        link.additional_properties = d
        return link

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
