"""ERCOT Electrical Buses"""

from attrs import define, field


@define
class ERCOTElectricalBus:
    """ERCOT Electrical Bus"""

    bus_name: str = field(default="")
    bus_id: str = field(default="")
    bus_type: str = field(default="")
    bus_location: str = field(default="")
    bus_status: str = field(default="")
    bus_created_at: str = field(default="")
