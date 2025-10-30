from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.post_routines_response_201_data_domain_type import (
    PostRoutinesResponse201DataDomainType,
)

if TYPE_CHECKING:
    from ..models.post_routines_response_201_data_steps_item_type_0 import (
        PostRoutinesResponse201DataStepsItemType0,
    )
    from ..models.post_routines_response_201_data_steps_item_type_1 import (
        PostRoutinesResponse201DataStepsItemType1,
    )


T = TypeVar("T", bound="PostRoutinesResponse201Data")


@_attrs_define
class PostRoutinesResponse201Data:
    """
    Attributes:
        description (None | str):
        domain_type (PostRoutinesResponse201DataDomainType):
        id (int):
        is_enabled (bool):  Default: False.
        name (str):
        priority (int):  Default: 0.
        steps (list[PostRoutinesResponse201DataStepsItemType0 | PostRoutinesResponse201DataStepsItemType1]):
    """

    description: None | str
    domain_type: PostRoutinesResponse201DataDomainType
    id: int
    name: str
    steps: list[
        PostRoutinesResponse201DataStepsItemType0
        | PostRoutinesResponse201DataStepsItemType1
    ]
    is_enabled: bool = False
    priority: int = 0
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.post_routines_response_201_data_steps_item_type_0 import (
            PostRoutinesResponse201DataStepsItemType0,
        )

        description: None | str
        description = self.description

        domain_type = self.domain_type.value

        id = self.id

        is_enabled = self.is_enabled

        name = self.name

        priority = self.priority

        steps = []
        for steps_item_data in self.steps:
            steps_item: dict[str, Any]
            if isinstance(steps_item_data, PostRoutinesResponse201DataStepsItemType0):
                steps_item = steps_item_data.to_dict()
            else:
                steps_item = steps_item_data.to_dict()

            steps.append(steps_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "description": description,
                "domainType": domain_type,
                "id": id,
                "isEnabled": is_enabled,
                "name": name,
                "priority": priority,
                "steps": steps,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.post_routines_response_201_data_steps_item_type_0 import (
            PostRoutinesResponse201DataStepsItemType0,
        )
        from ..models.post_routines_response_201_data_steps_item_type_1 import (
            PostRoutinesResponse201DataStepsItemType1,
        )

        d = dict(src_dict)

        def _parse_description(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        description = _parse_description(d.pop("description"))

        domain_type = PostRoutinesResponse201DataDomainType(d.pop("domainType"))

        id = d.pop("id")

        is_enabled = d.pop("isEnabled")

        name = d.pop("name")

        priority = d.pop("priority")

        steps = []
        _steps = d.pop("steps")
        for steps_item_data in _steps:

            def _parse_steps_item(
                data: object,
            ) -> (
                PostRoutinesResponse201DataStepsItemType0
                | PostRoutinesResponse201DataStepsItemType1
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    steps_item_type_0 = (
                        PostRoutinesResponse201DataStepsItemType0.from_dict(data)
                    )

                    return steps_item_type_0
                except:  # noqa: E722
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                steps_item_type_1 = PostRoutinesResponse201DataStepsItemType1.from_dict(
                    data
                )

                return steps_item_type_1

            steps_item = _parse_steps_item(steps_item_data)

            steps.append(steps_item)

        post_routines_response_201_data = cls(
            description=description,
            domain_type=domain_type,
            id=id,
            is_enabled=is_enabled,
            name=name,
            priority=priority,
            steps=steps,
        )

        post_routines_response_201_data.additional_properties = d
        return post_routines_response_201_data

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
