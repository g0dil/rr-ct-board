from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.put_oauthclients_identifier_body import PutOauthclientsIdentifierBody
from ...models.put_oauthclients_identifier_response_200 import (
    PutOauthclientsIdentifierResponse200,
)
from ...types import Response


def _get_kwargs(
    identifier: str,
    *,
    body: PutOauthclientsIdentifierBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/oauthclients/{identifier}".format(
            identifier=identifier,
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | PutOauthclientsIdentifierResponse200 | None:
    if response.status_code == 200:
        response_200 = PutOauthclientsIdentifierResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if response.status_code == 500:
        response_500 = cast(Any, None)
        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | PutOauthclientsIdentifierResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    identifier: str,
    *,
    client: AuthenticatedClient | Client,
    body: PutOauthclientsIdentifierBody,
) -> Response[Any | PutOauthclientsIdentifierResponse200]:
    """Update an existing client entity

    Args:
        identifier (str):
        body (PutOauthclientsIdentifierBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PutOauthclientsIdentifierResponse200]
    """

    kwargs = _get_kwargs(
        identifier=identifier,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    identifier: str,
    *,
    client: AuthenticatedClient | Client,
    body: PutOauthclientsIdentifierBody,
) -> Any | PutOauthclientsIdentifierResponse200 | None:
    """Update an existing client entity

    Args:
        identifier (str):
        body (PutOauthclientsIdentifierBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PutOauthclientsIdentifierResponse200
    """

    return sync_detailed(
        identifier=identifier,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    identifier: str,
    *,
    client: AuthenticatedClient | Client,
    body: PutOauthclientsIdentifierBody,
) -> Response[Any | PutOauthclientsIdentifierResponse200]:
    """Update an existing client entity

    Args:
        identifier (str):
        body (PutOauthclientsIdentifierBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PutOauthclientsIdentifierResponse200]
    """

    kwargs = _get_kwargs(
        identifier=identifier,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    identifier: str,
    *,
    client: AuthenticatedClient | Client,
    body: PutOauthclientsIdentifierBody,
) -> Any | PutOauthclientsIdentifierResponse200 | None:
    """Update an existing client entity

    Args:
        identifier (str):
        body (PutOauthclientsIdentifierBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PutOauthclientsIdentifierResponse200
    """

    return (
        await asyncio_detailed(
            identifier=identifier,
            client=client,
            body=body,
        )
    ).parsed
