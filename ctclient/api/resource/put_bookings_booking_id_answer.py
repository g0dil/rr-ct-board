from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.put_bookings_booking_id_answer_answer import (
    PutBookingsBookingIdAnswerAnswer,
)
from ...types import Response


def _get_kwargs(
    booking_id: int,
    answer: PutBookingsBookingIdAnswerAnswer,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/bookings/{booking_id}/{answer}".format(
            booking_id=booking_id,
            answer=answer,
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | str | None:
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
) -> Response[Any | str]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    booking_id: int,
    answer: PutBookingsBookingIdAnswerAnswer,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | str]:
    """Update status of booking

     Update the status of the specified booking.

    Args:
        booking_id (int):  Example: 8.
        answer (PutBookingsBookingIdAnswerAnswer):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | str]
    """

    kwargs = _get_kwargs(
        booking_id=booking_id,
        answer=answer,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    booking_id: int,
    answer: PutBookingsBookingIdAnswerAnswer,
    *,
    client: AuthenticatedClient | Client,
) -> Any | str | None:
    """Update status of booking

     Update the status of the specified booking.

    Args:
        booking_id (int):  Example: 8.
        answer (PutBookingsBookingIdAnswerAnswer):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | str
    """

    return sync_detailed(
        booking_id=booking_id,
        answer=answer,
        client=client,
    ).parsed


async def asyncio_detailed(
    booking_id: int,
    answer: PutBookingsBookingIdAnswerAnswer,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | str]:
    """Update status of booking

     Update the status of the specified booking.

    Args:
        booking_id (int):  Example: 8.
        answer (PutBookingsBookingIdAnswerAnswer):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | str]
    """

    kwargs = _get_kwargs(
        booking_id=booking_id,
        answer=answer,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    booking_id: int,
    answer: PutBookingsBookingIdAnswerAnswer,
    *,
    client: AuthenticatedClient | Client,
) -> Any | str | None:
    """Update status of booking

     Update the status of the specified booking.

    Args:
        booking_id (int):  Example: 8.
        answer (PutBookingsBookingIdAnswerAnswer):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | str
    """

    return (
        await asyncio_detailed(
            booking_id=booking_id,
            answer=answer,
            client=client,
        )
    ).parsed
