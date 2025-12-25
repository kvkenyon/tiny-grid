from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.archive import Archive
    from ..models.link import Link
    from ..models.product_history_metadata import ProductHistoryMetadata
    from ..models.result_metadata import ResultMetadata


T = TypeVar("T", bound="ProductHistory")


@_attrs_define
class ProductHistory:
    """Each archive represents a single EMIL Product archive (zip file).

    Attributes:
        field_meta (ResultMetadata | Unset): Represents record and paging summary for the specified query results.
        product (ProductHistoryMetadata | Unset): Represents record and paging summary for the specified query results.
        archives (list[Archive] | Unset):
        links (list[Link] | Unset):
    """

    field_meta: ResultMetadata | Unset = UNSET
    product: ProductHistoryMetadata | Unset = UNSET
    archives: list[Archive] | Unset = UNSET
    links: list[Link] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        field_meta: dict[str, Any] | Unset = UNSET
        if not isinstance(self.field_meta, Unset):
            field_meta = self.field_meta.to_dict()

        product: dict[str, Any] | Unset = UNSET
        if not isinstance(self.product, Unset):
            product = self.product.to_dict()

        archives: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.archives, Unset):
            archives = []
            for archives_item_data in self.archives:
                archives_item = archives_item_data.to_dict()
                archives.append(archives_item)

        links: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.links, Unset):
            links = []
            for links_item_data in self.links:
                links_item = links_item_data.to_dict()
                links.append(links_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if field_meta is not UNSET:
            field_dict["_meta"] = field_meta
        if product is not UNSET:
            field_dict["product"] = product
        if archives is not UNSET:
            field_dict["archives"] = archives
        if links is not UNSET:
            field_dict["links"] = links

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.archive import Archive
        from ..models.link import Link
        from ..models.product_history_metadata import ProductHistoryMetadata
        from ..models.result_metadata import ResultMetadata

        d = dict(src_dict)
        _field_meta = d.pop("_meta", UNSET)
        field_meta: ResultMetadata | Unset
        if isinstance(_field_meta, Unset):
            field_meta = UNSET
        else:
            field_meta = ResultMetadata.from_dict(_field_meta)

        _product = d.pop("product", UNSET)
        product: ProductHistoryMetadata | Unset
        if isinstance(_product, Unset):
            product = UNSET
        else:
            product = ProductHistoryMetadata.from_dict(_product)

        _archives = d.pop("archives", UNSET)
        archives: list[Archive] | Unset = UNSET
        if _archives is not UNSET:
            archives = []
            for archives_item_data in _archives:
                archives_item = Archive.from_dict(archives_item_data)

                archives.append(archives_item)

        _links = d.pop("links", UNSET)
        links: list[Link] | Unset = UNSET
        if _links is not UNSET:
            links = []
            for links_item_data in _links:
                links_item = Link.from_dict(links_item_data)

                links.append(links_item)

        product_history = cls(
            field_meta=field_meta,
            product=product,
            archives=archives,
            links=links,
        )

        product_history.additional_properties = d
        return product_history

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
