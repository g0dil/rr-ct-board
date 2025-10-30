from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_person_body import CreatePersonBody
from ...models.create_person_response_200 import CreatePersonResponse200
from ...models.create_person_response_400 import CreatePersonResponse400
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: CreatePersonBody,
    force: bool | Unset = UNSET,
    without_privacy_policy_agreement: bool | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["force"] = force

    params["without_privacy_policy_agreement"] = without_privacy_policy_agreement

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/persons",
        "params": params,
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | CreatePersonResponse200 | CreatePersonResponse400 | None:
    if response.status_code == 200:
        response_200 = CreatePersonResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = CreatePersonResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    if response.status_code == 402:
        response_402 = cast(Any, None)
        return response_402

    if response.status_code == 403:
        response_403 = cast(Any, None)
        return response_403

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | CreatePersonResponse200 | CreatePersonResponse400]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: CreatePersonBody,
    force: bool | Unset = UNSET,
    without_privacy_policy_agreement: bool | Unset = UNSET,
) -> Response[Any | CreatePersonResponse200 | CreatePersonResponse400]:
    """Create new person

     Endpoint to save a new person in ChurchTools. Generally, you can provide any information to save,
    but be aware that you can only save information for fields you have write access to. If the request
    fails because a duplicate is found (person with same name) use the `force` flag to create this
    person even if a duplicate is found.

    Args:
        force (bool | Unset):  Example: True.
        without_privacy_policy_agreement (bool | Unset):
        body (CreatePersonBody): The default values are used if no value is provides.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | CreatePersonResponse200 | CreatePersonResponse400]
    """

    kwargs = _get_kwargs(
        body=body,
        force=force,
        without_privacy_policy_agreement=without_privacy_policy_agreement,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    body: CreatePersonBody,
    force: bool | Unset = UNSET,
    without_privacy_policy_agreement: bool | Unset = UNSET,
) -> Any | CreatePersonResponse200 | CreatePersonResponse400 | None:
    """Create new person

     Endpoint to save a new person in ChurchTools. Generally, you can provide any information to save,
    but be aware that you can only save information for fields you have write access to. If the request
    fails because a duplicate is found (person with same name) use the `force` flag to create this
    person even if a duplicate is found.

    Args:
        force (bool | Unset):  Example: True.
        without_privacy_policy_agreement (bool | Unset):
        body (CreatePersonBody): The default values are used if no value is provides.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | CreatePersonResponse200 | CreatePersonResponse400
    """

    return sync_detailed(
        client=client,
        body=body,
        force=force,
        without_privacy_policy_agreement=without_privacy_policy_agreement,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: CreatePersonBody,
    force: bool | Unset = UNSET,
    without_privacy_policy_agreement: bool | Unset = UNSET,
) -> Response[Any | CreatePersonResponse200 | CreatePersonResponse400]:
    """Create new person

     Endpoint to save a new person in ChurchTools. Generally, you can provide any information to save,
    but be aware that you can only save information for fields you have write access to. If the request
    fails because a duplicate is found (person with same name) use the `force` flag to create this
    person even if a duplicate is found.

    Args:
        force (bool | Unset):  Example: True.
        without_privacy_policy_agreement (bool | Unset):
        body (CreatePersonBody): The default values are used if no value is provides.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | CreatePersonResponse200 | CreatePersonResponse400]
    """

    kwargs = _get_kwargs(
        body=body,
        force=force,
        without_privacy_policy_agreement=without_privacy_policy_agreement,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: CreatePersonBody,
    force: bool | Unset = UNSET,
    without_privacy_policy_agreement: bool | Unset = UNSET,
) -> Any | CreatePersonResponse200 | CreatePersonResponse400 | None:
    """Create new person

     Endpoint to save a new person in ChurchTools. Generally, you can provide any information to save,
    but be aware that you can only save information for fields you have write access to. If the request
    fails because a duplicate is found (person with same name) use the `force` flag to create this
    person even if a duplicate is found.

    Args:
        force (bool | Unset):  Example: True.
        without_privacy_policy_agreement (bool | Unset):
        body (CreatePersonBody): The default values are used if no value is provides.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | CreatePersonResponse200 | CreatePersonResponse400
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            force=force,
            without_privacy_policy_agreement=without_privacy_policy_agreement,
        )
    ).parsed
