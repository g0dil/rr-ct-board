from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.put_resources_resource_id_body import PutResourcesResourceIdBody
from ...models.put_resources_resource_id_response_200 import (
    PutResourcesResourceIdResponse200,
)
from ...types import Response


def _get_kwargs(
    resource_id: float,
    *,
    body: PutResourcesResourceIdBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/resources/{resource_id}".format(
            resource_id=resource_id,
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | PutResourcesResourceIdResponse200 | str | None:
    if response.status_code == 200:
        response_200 = PutResourcesResourceIdResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = response.text
        return response_401

    if response.status_code == 403:
        response_403 = cast(Any, None)
        return response_403

    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | PutResourcesResourceIdResponse200 | str]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    resource_id: float,
    *,
    client: AuthenticatedClient | Client,
    body: PutResourcesResourceIdBody,
) -> Response[Any | PutResourcesResourceIdResponse200 | str]:
    """Update resource

     Update the specified resource.

    Args:
        resource_id (float):  Example: 7.
        body (PutResourcesResourceIdBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PutResourcesResourceIdResponse200 | str]
    """

    kwargs = _get_kwargs(
        resource_id=resource_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    resource_id: float,
    *,
    client: AuthenticatedClient | Client,
    body: PutResourcesResourceIdBody,
) -> Any | PutResourcesResourceIdResponse200 | str | None:
    """Update resource

     Update the specified resource.

    Args:
        resource_id (float):  Example: 7.
        body (PutResourcesResourceIdBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PutResourcesResourceIdResponse200 | str
    """

    return sync_detailed(
        resource_id=resource_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    resource_id: float,
    *,
    client: AuthenticatedClient | Client,
    body: PutResourcesResourceIdBody,
) -> Response[Any | PutResourcesResourceIdResponse200 | str]:
    """Update resource

     Update the specified resource.

    Args:
        resource_id (float):  Example: 7.
        body (PutResourcesResourceIdBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PutResourcesResourceIdResponse200 | str]
    """

    kwargs = _get_kwargs(
        resource_id=resource_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    resource_id: float,
    *,
    client: AuthenticatedClient | Client,
    body: PutResourcesResourceIdBody,
) -> Any | PutResourcesResourceIdResponse200 | str | None:
    """Update resource

     Update the specified resource.

    Args:
        resource_id (float):  Example: 7.
        body (PutResourcesResourceIdBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PutResourcesResourceIdResponse200 | str
    """

    return (
        await asyncio_detailed(
            resource_id=resource_id,
            client=client,
            body=body,
        )
    ).parsed
