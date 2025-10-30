from __future__ import annotations

import json
from collections.abc import Mapping
from io import BytesIO
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .. import types
from ..types import UNSET, File, FileTypes, Unset

if TYPE_CHECKING:
    from ..models.upload_files_body_image_options import UploadFilesBodyImageOptions


T = TypeVar("T", bound="UploadFilesBody")


@_attrs_define
class UploadFilesBody:
    """
    Attributes:
        files (list[File] | Unset):
        image_options (UploadFilesBodyImageOptions | Unset):
        max_height (str | Unset):
        max_width (str | Unset):
    """

    files: list[File] | Unset = UNSET
    image_options: UploadFilesBodyImageOptions | Unset = UNSET
    max_height: str | Unset = UNSET
    max_width: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        files: list[FileTypes] | Unset = UNSET
        if not isinstance(self.files, Unset):
            files = []
            for files_item_data in self.files:
                files_item = files_item_data.to_tuple()

                files.append(files_item)

        image_options: dict[str, Any] | Unset = UNSET
        if not isinstance(self.image_options, Unset):
            image_options = self.image_options.to_dict()

        max_height = self.max_height

        max_width = self.max_width

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if files is not UNSET:
            field_dict["files[]"] = files
        if image_options is not UNSET:
            field_dict["image_options"] = image_options
        if max_height is not UNSET:
            field_dict["max_height"] = max_height
        if max_width is not UNSET:
            field_dict["max_width"] = max_width

        return field_dict

    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        if not isinstance(self.files, Unset):
            for files_item_element in self.files:
                files.append(("files[]", files_item_element.to_tuple()))

        if not isinstance(self.image_options, Unset):
            files.append(
                (
                    "image_options",
                    (
                        None,
                        json.dumps(self.image_options.to_dict()).encode(),
                        "application/json",
                    ),
                )
            )

        if not isinstance(self.max_height, Unset):
            files.append(
                ("max_height", (None, str(self.max_height).encode(), "text/plain"))
            )

        if not isinstance(self.max_width, Unset):
            files.append(
                ("max_width", (None, str(self.max_width).encode(), "text/plain"))
            )

        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))

        return files

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.upload_files_body_image_options import UploadFilesBodyImageOptions

        d = dict(src_dict)
        files = []
        _files = d.pop("files[]", UNSET)
        for files_item_data in _files or []:
            files_item = File(payload=BytesIO(files_item_data))

            files.append(files_item)

        _image_options = d.pop("image_options", UNSET)
        image_options: UploadFilesBodyImageOptions | Unset
        if isinstance(_image_options, Unset):
            image_options = UNSET
        else:
            image_options = UploadFilesBodyImageOptions.from_dict(_image_options)

        max_height = d.pop("max_height", UNSET)

        max_width = d.pop("max_width", UNSET)

        upload_files_body = cls(
            files=files,
            image_options=image_options,
            max_height=max_height,
            max_width=max_width,
        )

        upload_files_body.additional_properties = d
        return upload_files_body

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
