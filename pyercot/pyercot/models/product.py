from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.artifact import Artifact
    from ..models.link import Link
    from ..models.product_protocol_rules import ProductProtocolRules


T = TypeVar("T", bound="Product")


@_attrs_define
class Product:
    """Represents an EMIL Product, which includes its metadata along with all Artifact information.

    Attributes:
        emil_id (str | Unset):
        name (str | Unset):
        description (str | Unset):
        status (str | Unset):
        report_type_id (int | Unset):
        audience (str | Unset):
        generation_frequency (str | Unset):
        security_classification (str | Unset):
        last_updated (datetime.datetime | Unset):
        first_run (datetime.datetime | Unset):
        eceii (str | Unset):
        channel (str | Unset):
        user_guide (str | Unset):
        posting_type (str | Unset):
        market (str | Unset):
        extract_subscriber (str | Unset):
        xsd_name (str | Unset):
        mis_posting_location (str | Unset):
        certificate_role (str | Unset):
        file_type (str | Unset):
        ddl_name (str | Unset):
        mis_display_duration (int | Unset):
        archive_duration (int | Unset):
        notification_type (str | Unset):
        protocol_rules (ProductProtocolRules | Unset):
        links (list[Link] | Unset):
        artifacts (list[Artifact] | Unset):
    """

    emil_id: str | Unset = UNSET
    name: str | Unset = UNSET
    description: str | Unset = UNSET
    status: str | Unset = UNSET
    report_type_id: int | Unset = UNSET
    audience: str | Unset = UNSET
    generation_frequency: str | Unset = UNSET
    security_classification: str | Unset = UNSET
    last_updated: datetime.datetime | Unset = UNSET
    first_run: datetime.datetime | Unset = UNSET
    eceii: str | Unset = UNSET
    channel: str | Unset = UNSET
    user_guide: str | Unset = UNSET
    posting_type: str | Unset = UNSET
    market: str | Unset = UNSET
    extract_subscriber: str | Unset = UNSET
    xsd_name: str | Unset = UNSET
    mis_posting_location: str | Unset = UNSET
    certificate_role: str | Unset = UNSET
    file_type: str | Unset = UNSET
    ddl_name: str | Unset = UNSET
    mis_display_duration: int | Unset = UNSET
    archive_duration: int | Unset = UNSET
    notification_type: str | Unset = UNSET
    protocol_rules: ProductProtocolRules | Unset = UNSET
    links: list[Link] | Unset = UNSET
    artifacts: list[Artifact] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        emil_id = self.emil_id

        name = self.name

        description = self.description

        status = self.status

        report_type_id = self.report_type_id

        audience = self.audience

        generation_frequency = self.generation_frequency

        security_classification = self.security_classification

        last_updated: str | Unset = UNSET
        if not isinstance(self.last_updated, Unset):
            last_updated = self.last_updated.isoformat()

        first_run: str | Unset = UNSET
        if not isinstance(self.first_run, Unset):
            first_run = self.first_run.isoformat()

        eceii = self.eceii

        channel = self.channel

        user_guide = self.user_guide

        posting_type = self.posting_type

        market = self.market

        extract_subscriber = self.extract_subscriber

        xsd_name = self.xsd_name

        mis_posting_location = self.mis_posting_location

        certificate_role = self.certificate_role

        file_type = self.file_type

        ddl_name = self.ddl_name

        mis_display_duration = self.mis_display_duration

        archive_duration = self.archive_duration

        notification_type = self.notification_type

        protocol_rules: dict[str, Any] | Unset = UNSET
        if not isinstance(self.protocol_rules, Unset):
            protocol_rules = self.protocol_rules.to_dict()

        links: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.links, Unset):
            links = []
            for links_item_data in self.links:
                links_item = links_item_data.to_dict()
                links.append(links_item)

        artifacts: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.artifacts, Unset):
            artifacts = []
            for artifacts_item_data in self.artifacts:
                artifacts_item = artifacts_item_data.to_dict()
                artifacts.append(artifacts_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if emil_id is not UNSET:
            field_dict["emilId"] = emil_id
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if status is not UNSET:
            field_dict["status"] = status
        if report_type_id is not UNSET:
            field_dict["reportTypeId"] = report_type_id
        if audience is not UNSET:
            field_dict["audience"] = audience
        if generation_frequency is not UNSET:
            field_dict["generationFrequency"] = generation_frequency
        if security_classification is not UNSET:
            field_dict["securityClassification"] = security_classification
        if last_updated is not UNSET:
            field_dict["lastUpdated"] = last_updated
        if first_run is not UNSET:
            field_dict["firstRun"] = first_run
        if eceii is not UNSET:
            field_dict["eceii"] = eceii
        if channel is not UNSET:
            field_dict["channel"] = channel
        if user_guide is not UNSET:
            field_dict["userGuide"] = user_guide
        if posting_type is not UNSET:
            field_dict["postingType"] = posting_type
        if market is not UNSET:
            field_dict["market"] = market
        if extract_subscriber is not UNSET:
            field_dict["extractSubscriber"] = extract_subscriber
        if xsd_name is not UNSET:
            field_dict["xsdName"] = xsd_name
        if mis_posting_location is not UNSET:
            field_dict["misPostingLocation"] = mis_posting_location
        if certificate_role is not UNSET:
            field_dict["certificateRole"] = certificate_role
        if file_type is not UNSET:
            field_dict["fileType"] = file_type
        if ddl_name is not UNSET:
            field_dict["ddlName"] = ddl_name
        if mis_display_duration is not UNSET:
            field_dict["misDisplayDuration"] = mis_display_duration
        if archive_duration is not UNSET:
            field_dict["archiveDuration"] = archive_duration
        if notification_type is not UNSET:
            field_dict["notificationType"] = notification_type
        if protocol_rules is not UNSET:
            field_dict["protocolRules"] = protocol_rules
        if links is not UNSET:
            field_dict["links"] = links
        if artifacts is not UNSET:
            field_dict["artifacts"] = artifacts

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.artifact import Artifact
        from ..models.link import Link
        from ..models.product_protocol_rules import ProductProtocolRules

        d = dict(src_dict)
        emil_id = d.pop("emilId", UNSET)

        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        status = d.pop("status", UNSET)

        report_type_id = d.pop("reportTypeId", UNSET)

        audience = d.pop("audience", UNSET)

        generation_frequency = d.pop("generationFrequency", UNSET)

        security_classification = d.pop("securityClassification", UNSET)

        _last_updated = d.pop("lastUpdated", UNSET)
        last_updated: datetime.datetime | Unset
        if isinstance(_last_updated, Unset):
            last_updated = UNSET
        else:
            last_updated = isoparse(_last_updated)

        _first_run = d.pop("firstRun", UNSET)
        first_run: datetime.datetime | Unset
        if isinstance(_first_run, Unset):
            first_run = UNSET
        else:
            first_run = isoparse(_first_run)

        eceii = d.pop("eceii", UNSET)

        channel = d.pop("channel", UNSET)

        user_guide = d.pop("userGuide", UNSET)

        posting_type = d.pop("postingType", UNSET)

        market = d.pop("market", UNSET)

        extract_subscriber = d.pop("extractSubscriber", UNSET)

        xsd_name = d.pop("xsdName", UNSET)

        mis_posting_location = d.pop("misPostingLocation", UNSET)

        certificate_role = d.pop("certificateRole", UNSET)

        file_type = d.pop("fileType", UNSET)

        ddl_name = d.pop("ddlName", UNSET)

        mis_display_duration = d.pop("misDisplayDuration", UNSET)

        archive_duration = d.pop("archiveDuration", UNSET)

        notification_type = d.pop("notificationType", UNSET)

        _protocol_rules = d.pop("protocolRules", UNSET)
        protocol_rules: ProductProtocolRules | Unset
        if isinstance(_protocol_rules, Unset):
            protocol_rules = UNSET
        else:
            protocol_rules = ProductProtocolRules.from_dict(_protocol_rules)

        _links = d.pop("links", UNSET)
        links: list[Link] | Unset = UNSET
        if _links is not UNSET:
            links = []
            for links_item_data in _links:
                links_item = Link.from_dict(links_item_data)

                links.append(links_item)

        _artifacts = d.pop("artifacts", UNSET)
        artifacts: list[Artifact] | Unset = UNSET
        if _artifacts is not UNSET:
            artifacts = []
            for artifacts_item_data in _artifacts:
                artifacts_item = Artifact.from_dict(artifacts_item_data)

                artifacts.append(artifacts_item)

        product = cls(
            emil_id=emil_id,
            name=name,
            description=description,
            status=status,
            report_type_id=report_type_id,
            audience=audience,
            generation_frequency=generation_frequency,
            security_classification=security_classification,
            last_updated=last_updated,
            first_run=first_run,
            eceii=eceii,
            channel=channel,
            user_guide=user_guide,
            posting_type=posting_type,
            market=market,
            extract_subscriber=extract_subscriber,
            xsd_name=xsd_name,
            mis_posting_location=mis_posting_location,
            certificate_role=certificate_role,
            file_type=file_type,
            ddl_name=ddl_name,
            mis_display_duration=mis_display_duration,
            archive_duration=archive_duration,
            notification_type=notification_type,
            protocol_rules=protocol_rules,
            links=links,
            artifacts=artifacts,
        )

        product.additional_properties = d
        return product

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
