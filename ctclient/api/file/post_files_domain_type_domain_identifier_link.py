from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.post_files_domain_type_domain_identifier_link_body import (
    PostFilesDomainTypeDomainIdentifierLinkBody,
)
from ...models.post_files_domain_type_domain_identifier_link_response_201 import (
    PostFilesDomainTypeDomainIdentifierLinkResponse201,
)
from ...types import Response


def _get_kwargs(
    domain_type: str,
    domain_identifier: str,
    *,
    body: PostFilesDomainTypeDomainIdentifierLinkBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/files/{domain_type}/{domain_identifier}/link".format(
            domain_type=domain_type,
            domain_identifier=domain_identifier,
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | PostFilesDomainTypeDomainIdentifierLinkResponse201 | str | None:
    if response.status_code == 201:
        response_201 = PostFilesDomainTypeDomainIdentifierLinkResponse201.from_dict(
            response.json()
        )

        return response_201

    if response.status_code == 401:
        response_401 = response.text
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
) -> Response[Any | PostFilesDomainTypeDomainIdentifierLinkResponse201 | str]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    domain_type: str,
    domain_identifier: str,
    *,
    client: AuthenticatedClient | Client,
    body: PostFilesDomainTypeDomainIdentifierLinkBody,
) -> Response[Any | PostFilesDomainTypeDomainIdentifierLinkResponse201 | str]:
    """Add link

     Add the given link to the specified domain object.

    Args:
        domain_type (str):  Example: logo.
        domain_identifier (str):  Example: 35.
        body (PostFilesDomainTypeDomainIdentifierLinkBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PostFilesDomainTypeDomainIdentifierLinkResponse201 | str]
    """

    kwargs = _get_kwargs(
        domain_type=domain_type,
        domain_identifier=domain_identifier,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    domain_type: str,
    domain_identifier: str,
    *,
    client: AuthenticatedClient | Client,
    body: PostFilesDomainTypeDomainIdentifierLinkBody,
) -> Any | PostFilesDomainTypeDomainIdentifierLinkResponse201 | str | None:
    """Add link

     Add the given link to the specified domain object.

    Args:
        domain_type (str):  Example: logo.
        domain_identifier (str):  Example: 35.
        body (PostFilesDomainTypeDomainIdentifierLinkBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PostFilesDomainTypeDomainIdentifierLinkResponse201 | str
    """

    return sync_detailed(
        domain_type=domain_type,
        domain_identifier=domain_identifier,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    domain_type: str,
    domain_identifier: str,
    *,
    client: AuthenticatedClient | Client,
    body: PostFilesDomainTypeDomainIdentifierLinkBody,
) -> Response[Any | PostFilesDomainTypeDomainIdentifierLinkResponse201 | str]:
    """Add link

     Add the given link to the specified domain object.

    Args:
        domain_type (str):  Example: logo.
        domain_identifier (str):  Example: 35.
        body (PostFilesDomainTypeDomainIdentifierLinkBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PostFilesDomainTypeDomainIdentifierLinkResponse201 | str]
    """

    kwargs = _get_kwargs(
        domain_type=domain_type,
        domain_identifier=domain_identifier,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    domain_type: str,
    domain_identifier: str,
    *,
    client: AuthenticatedClient | Client,
    body: PostFilesDomainTypeDomainIdentifierLinkBody,
) -> Any | PostFilesDomainTypeDomainIdentifierLinkResponse201 | str | None:
    """Add link

     Add the given link to the specified domain object.

    Args:
        domain_type (str):  Example: logo.
        domain_identifier (str):  Example: 35.
        body (PostFilesDomainTypeDomainIdentifierLinkBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PostFilesDomainTypeDomainIdentifierLinkResponse201 | str
    """

    return (
        await asyncio_detailed(
            domain_type=domain_type,
            domain_identifier=domain_identifier,
            client=client,
            body=body,
        )
    ).parsed
