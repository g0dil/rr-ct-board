from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="GetCaptchaResponse200")


@_attrs_define
class GetCaptchaResponse200:
    """
    Attributes:
        algorithm (str):  Example: SHA-256.
        challenge (str):  Example: deb31600184a45b967f7cf1f952910d702be4c6a5b016371fb84b88e1b20a7bf.
        maxnumber (int):  Example: 50000.
        salt (str):  Example: ffcf79a3645465b36766ee2e?expires=1726565012.
        signature (str):  Example: 1e1c203b3286b58cb6529a0b9f483bfdf11b4cb17e17093921cd692107e24d82y.
    """

    algorithm: str
    challenge: str
    maxnumber: int
    salt: str
    signature: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        algorithm = self.algorithm

        challenge = self.challenge

        maxnumber = self.maxnumber

        salt = self.salt

        signature = self.signature

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "algorithm": algorithm,
                "challenge": challenge,
                "maxnumber": maxnumber,
                "salt": salt,
                "signature": signature,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        algorithm = d.pop("algorithm")

        challenge = d.pop("challenge")

        maxnumber = d.pop("maxnumber")

        salt = d.pop("salt")

        signature = d.pop("signature")

        get_captcha_response_200 = cls(
            algorithm=algorithm,
            challenge=challenge,
            maxnumber=maxnumber,
            salt=salt,
            signature=signature,
        )

        get_captcha_response_200.additional_properties = d
        return get_captcha_response_200

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
