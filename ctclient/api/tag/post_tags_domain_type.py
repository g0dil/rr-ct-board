from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.post_tags_domain_type_body import PostTagsDomainTypeBody
from ...models.post_tags_domain_type_domain_type import PostTagsDomainTypeDomainType
from ...models.post_tags_domain_type_response_200 import PostTagsDomainTypeResponse200
from ...types import Response


def _get_kwargs(
    domain_type: PostTagsDomainTypeDomainType,
    *,
    body: PostTagsDomainTypeBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/tags/{domain_type}".format(
            domain_type=domain_type,
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | PostTagsDomainTypeResponse200 | str | None:
    if response.status_code == 200:
        response_200 = PostTagsDomainTypeResponse200.from_dict(response.json())

        return response_200

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
) -> Response[Any | PostTagsDomainTypeResponse200 | str]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    domain_type: PostTagsDomainTypeDomainType,
    *,
    client: AuthenticatedClient | Client,
    body: PostTagsDomainTypeBody,
) -> Response[Any | PostTagsDomainTypeResponse200 | str]:
    """Create new tag

     Create new tag for the specified domain type. Please note that this tag may disappear later if it is
    not immediately added to any particular domain object (does not apply to group tags).

    Args:
        domain_type (PostTagsDomainTypeDomainType):  Example: person.
        body (PostTagsDomainTypeBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PostTagsDomainTypeResponse200 | str]
    """

    kwargs = _get_kwargs(
        domain_type=domain_type,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    domain_type: PostTagsDomainTypeDomainType,
    *,
    client: AuthenticatedClient | Client,
    body: PostTagsDomainTypeBody,
) -> Any | PostTagsDomainTypeResponse200 | str | None:
    """Create new tag

     Create new tag for the specified domain type. Please note that this tag may disappear later if it is
    not immediately added to any particular domain object (does not apply to group tags).

    Args:
        domain_type (PostTagsDomainTypeDomainType):  Example: person.
        body (PostTagsDomainTypeBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PostTagsDomainTypeResponse200 | str
    """

    return sync_detailed(
        domain_type=domain_type,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    domain_type: PostTagsDomainTypeDomainType,
    *,
    client: AuthenticatedClient | Client,
    body: PostTagsDomainTypeBody,
) -> Response[Any | PostTagsDomainTypeResponse200 | str]:
    """Create new tag

     Create new tag for the specified domain type. Please note that this tag may disappear later if it is
    not immediately added to any particular domain object (does not apply to group tags).

    Args:
        domain_type (PostTagsDomainTypeDomainType):  Example: person.
        body (PostTagsDomainTypeBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PostTagsDomainTypeResponse200 | str]
    """

    kwargs = _get_kwargs(
        domain_type=domain_type,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    domain_type: PostTagsDomainTypeDomainType,
    *,
    client: AuthenticatedClient | Client,
    body: PostTagsDomainTypeBody,
) -> Any | PostTagsDomainTypeResponse200 | str | None:
    """Create new tag

     Create new tag for the specified domain type. Please note that this tag may disappear later if it is
    not immediately added to any particular domain object (does not apply to group tags).

    Args:
        domain_type (PostTagsDomainTypeDomainType):  Example: person.
        body (PostTagsDomainTypeBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PostTagsDomainTypeResponse200 | str
    """

    return (
        await asyncio_detailed(
            domain_type=domain_type,
            client=client,
            body=body,
        )
    ).parsed
