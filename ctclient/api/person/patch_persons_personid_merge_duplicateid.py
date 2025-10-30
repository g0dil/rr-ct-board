from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.patch_persons_personid_merge_duplicateid_body import (
    PatchPersonsPersonidMergeDuplicateidBody,
)
from ...types import Response


def _get_kwargs(
    person_id: str,
    duplicate_id: str,
    *,
    body: PatchPersonsPersonidMergeDuplicateidBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/persons/{person_id}/merge/{duplicate_id}".format(
            person_id=person_id,
            duplicate_id=duplicate_id,
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | None:
    if response.status_code == 200:
        return None

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    person_id: str,
    duplicate_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: PatchPersonsPersonidMergeDuplicateidBody,
) -> Response[Any]:
    """Merge two person records

     **Caution:** This API is published as Beta and subject to be changed. It is published such that
    customers can play evaluate it with production data.

    Generally, you can provide any person field to save, but be aware that write access to the provided
    ields is required. Beware, that not all fields which are listed in the Person schema can be updated.
    E.g. `imageUrl` or `familyUrl`
    (see `PATCH /api/person/{id}`)

    * using PATCH you can perform the eventual merge, it will
      + patch the person record
      + replace the personId of the doublette with the Original in all related records.
        * Group memberships
        * Person relation
        * Bookings
        * Wiki-Entries
        * Financial transactions
        * ...
    * delete the doublette if `deleteDuplicate` is true

    all to be done within one transaction.

    Args:
        person_id (str):
        duplicate_id (str):  Example: 100.
        body (PatchPersonsPersonidMergeDuplicateidBody): Fields applicable to upate a person

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        person_id=person_id,
        duplicate_id=duplicate_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    person_id: str,
    duplicate_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: PatchPersonsPersonidMergeDuplicateidBody,
) -> Response[Any]:
    """Merge two person records

     **Caution:** This API is published as Beta and subject to be changed. It is published such that
    customers can play evaluate it with production data.

    Generally, you can provide any person field to save, but be aware that write access to the provided
    ields is required. Beware, that not all fields which are listed in the Person schema can be updated.
    E.g. `imageUrl` or `familyUrl`
    (see `PATCH /api/person/{id}`)

    * using PATCH you can perform the eventual merge, it will
      + patch the person record
      + replace the personId of the doublette with the Original in all related records.
        * Group memberships
        * Person relation
        * Bookings
        * Wiki-Entries
        * Financial transactions
        * ...
    * delete the doublette if `deleteDuplicate` is true

    all to be done within one transaction.

    Args:
        person_id (str):
        duplicate_id (str):  Example: 100.
        body (PatchPersonsPersonidMergeDuplicateidBody): Fields applicable to upate a person

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        person_id=person_id,
        duplicate_id=duplicate_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
