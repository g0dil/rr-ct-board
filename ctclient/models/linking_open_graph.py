from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.linking_open_graph_fetch_status import LinkingOpenGraphFetchStatus
from ..models.linking_open_graph_linking_type import LinkingOpenGraphLinkingType

if TYPE_CHECKING:
    from ..models.linking_open_graph_data_type_0 import LinkingOpenGraphDataType0


T = TypeVar("T", bound="LinkingOpenGraph")


@_attrs_define
class LinkingOpenGraph:
    """
    Attributes:
        fetch_status (LinkingOpenGraphFetchStatus):
        url (str):
        data (LinkingOpenGraphDataType0 | None):
        linking_type (LinkingOpenGraphLinkingType):
    """

    fetch_status: LinkingOpenGraphFetchStatus
    url: str
    data: LinkingOpenGraphDataType0 | None
    linking_type: LinkingOpenGraphLinkingType
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.linking_open_graph_data_type_0 import LinkingOpenGraphDataType0

        fetch_status = self.fetch_status.value

        url = self.url

        data: dict[str, Any] | None
        if isinstance(self.data, LinkingOpenGraphDataType0):
            data = self.data.to_dict()
        else:
            data = self.data

        linking_type = self.linking_type.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "fetchStatus": fetch_status,
                "url": url,
                "data": data,
                "linkingType": linking_type,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.linking_open_graph_data_type_0 import LinkingOpenGraphDataType0

        d = dict(src_dict)
        fetch_status = LinkingOpenGraphFetchStatus(d.pop("fetchStatus"))

        url = d.pop("url")

        def _parse_data(data: object) -> LinkingOpenGraphDataType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                data_type_0 = LinkingOpenGraphDataType0.from_dict(data)

                return data_type_0
            except:  # noqa: E722
                pass
            return cast(LinkingOpenGraphDataType0 | None, data)

        data = _parse_data(d.pop("data"))

        linking_type = LinkingOpenGraphLinkingType(d.pop("linkingType"))

        linking_open_graph = cls(
            fetch_status=fetch_status,
            url=url,
            data=data,
            linking_type=linking_type,
        )

        linking_open_graph.additional_properties = d
        return linking_open_graph

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
