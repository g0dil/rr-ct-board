from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.post_captcha_body import PostCaptchaBody
from ...models.post_captcha_response_200 import PostCaptchaResponse200
from ...types import Response


def _get_kwargs(
    *,
    body: PostCaptchaBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/captcha",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | PostCaptchaResponse200 | str | None:
    if response.status_code == 200:
        response_200 = PostCaptchaResponse200.from_dict(response.json())

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
) -> Response[Any | PostCaptchaResponse200 | str]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: PostCaptchaBody,
) -> Response[Any | PostCaptchaResponse200 | str]:
    """Altcha Captcha Verification

     Verify a captcha solution. Only for testing purposes. Other endpoints that require a captcha take
    the solution directly. See https://altcha.org/docs/website-integration/ for more information

    Args:
        body (PostCaptchaBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PostCaptchaResponse200 | str]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    body: PostCaptchaBody,
) -> Any | PostCaptchaResponse200 | str | None:
    """Altcha Captcha Verification

     Verify a captcha solution. Only for testing purposes. Other endpoints that require a captcha take
    the solution directly. See https://altcha.org/docs/website-integration/ for more information

    Args:
        body (PostCaptchaBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PostCaptchaResponse200 | str
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: PostCaptchaBody,
) -> Response[Any | PostCaptchaResponse200 | str]:
    """Altcha Captcha Verification

     Verify a captcha solution. Only for testing purposes. Other endpoints that require a captcha take
    the solution directly. See https://altcha.org/docs/website-integration/ for more information

    Args:
        body (PostCaptchaBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PostCaptchaResponse200 | str]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: PostCaptchaBody,
) -> Any | PostCaptchaResponse200 | str | None:
    """Altcha Captcha Verification

     Verify a captcha solution. Only for testing purposes. Other endpoints that require a captcha take
    the solution directly. See https://altcha.org/docs/website-integration/ for more information

    Args:
        body (PostCaptchaBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PostCaptchaResponse200 | str
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
