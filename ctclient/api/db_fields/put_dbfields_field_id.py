from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.put_dbfields_field_id_body import PutDbfieldsFieldIdBody
from ...models.put_dbfields_field_id_response_200 import PutDbfieldsFieldIdResponse200
from ...types import Response


def _get_kwargs(
    field_id: str,
    *,
    body: PutDbfieldsFieldIdBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/dbfields/{field_id}".format(
            field_id=field_id,
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | PutDbfieldsFieldIdResponse200 | str | None:
    if response.status_code == 200:
        response_200 = PutDbfieldsFieldIdResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

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
) -> Response[Any | PutDbfieldsFieldIdResponse200 | str]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    field_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: PutDbfieldsFieldIdBody,
) -> Response[Any | PutDbfieldsFieldIdResponse200 | str]:
    """Update db field

    Args:
        field_id (str):
        body (PutDbfieldsFieldIdBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PutDbfieldsFieldIdResponse200 | str]
    """

    kwargs = _get_kwargs(
        field_id=field_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    field_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: PutDbfieldsFieldIdBody,
) -> Any | PutDbfieldsFieldIdResponse200 | str | None:
    """Update db field

    Args:
        field_id (str):
        body (PutDbfieldsFieldIdBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PutDbfieldsFieldIdResponse200 | str
    """

    return sync_detailed(
        field_id=field_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    field_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: PutDbfieldsFieldIdBody,
) -> Response[Any | PutDbfieldsFieldIdResponse200 | str]:
    """Update db field

    Args:
        field_id (str):
        body (PutDbfieldsFieldIdBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PutDbfieldsFieldIdResponse200 | str]
    """

    kwargs = _get_kwargs(
        field_id=field_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    field_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: PutDbfieldsFieldIdBody,
) -> Any | PutDbfieldsFieldIdResponse200 | str | None:
    """Update db field

    Args:
        field_id (str):
        body (PutDbfieldsFieldIdBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PutDbfieldsFieldIdResponse200 | str
    """

    return (
        await asyncio_detailed(
            field_id=field_id,
            client=client,
            body=body,
        )
    ).parsed
