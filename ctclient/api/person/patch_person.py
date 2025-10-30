from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.patch_person_body import PatchPersonBody
from ...models.patch_person_response_200 import PatchPersonResponse200
from ...models.patch_person_response_400 import PatchPersonResponse400
from ...types import Response


def _get_kwargs(
    person_id: int,
    *,
    body: PatchPersonBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/persons/{person_id}".format(
            person_id=person_id,
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | PatchPersonResponse200 | PatchPersonResponse400 | None:
    if response.status_code == 200:
        response_200 = PatchPersonResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = PatchPersonResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    if response.status_code == 403:
        response_403 = cast(Any, None)
        return response_403

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | PatchPersonResponse200 | PatchPersonResponse400]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    person_id: int,
    *,
    client: AuthenticatedClient | Client,
    body: PatchPersonBody,
) -> Response[Any | PatchPersonResponse200 | PatchPersonResponse400]:
    """Updates a person

     Endpoint to update a person in ChurchTools. Generally, you can provide any information to save, but
    be aware that you can only save information for fields you have write access to. Beware, that not
    all fields which are listed in the Person schema can be updated. E.g. `imageUrl` or `familyUrl`.

    Args:
        person_id (int):  Example: 42.
        body (PatchPersonBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PatchPersonResponse200 | PatchPersonResponse400]
    """

    kwargs = _get_kwargs(
        person_id=person_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    person_id: int,
    *,
    client: AuthenticatedClient | Client,
    body: PatchPersonBody,
) -> Any | PatchPersonResponse200 | PatchPersonResponse400 | None:
    """Updates a person

     Endpoint to update a person in ChurchTools. Generally, you can provide any information to save, but
    be aware that you can only save information for fields you have write access to. Beware, that not
    all fields which are listed in the Person schema can be updated. E.g. `imageUrl` or `familyUrl`.

    Args:
        person_id (int):  Example: 42.
        body (PatchPersonBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PatchPersonResponse200 | PatchPersonResponse400
    """

    return sync_detailed(
        person_id=person_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    person_id: int,
    *,
    client: AuthenticatedClient | Client,
    body: PatchPersonBody,
) -> Response[Any | PatchPersonResponse200 | PatchPersonResponse400]:
    """Updates a person

     Endpoint to update a person in ChurchTools. Generally, you can provide any information to save, but
    be aware that you can only save information for fields you have write access to. Beware, that not
    all fields which are listed in the Person schema can be updated. E.g. `imageUrl` or `familyUrl`.

    Args:
        person_id (int):  Example: 42.
        body (PatchPersonBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PatchPersonResponse200 | PatchPersonResponse400]
    """

    kwargs = _get_kwargs(
        person_id=person_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    person_id: int,
    *,
    client: AuthenticatedClient | Client,
    body: PatchPersonBody,
) -> Any | PatchPersonResponse200 | PatchPersonResponse400 | None:
    """Updates a person

     Endpoint to update a person in ChurchTools. Generally, you can provide any information to save, but
    be aware that you can only save information for fields you have write access to. Beware, that not
    all fields which are listed in the Person schema can be updated. E.g. `imageUrl` or `familyUrl`.

    Args:
        person_id (int):  Example: 42.
        body (PatchPersonBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PatchPersonResponse200 | PatchPersonResponse400
    """

    return (
        await asyncio_detailed(
            person_id=person_id,
            client=client,
            body=body,
        )
    ).parsed
