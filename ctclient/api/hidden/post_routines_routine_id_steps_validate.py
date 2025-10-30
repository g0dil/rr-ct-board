from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.post_routines_routine_id_steps_validate_body_type_0_type_0 import (
    PostRoutinesRoutineIdStepsValidateBodyType0Type0,
)
from ...models.post_routines_routine_id_steps_validate_body_type_0_type_1 import (
    PostRoutinesRoutineIdStepsValidateBodyType0Type1,
)
from ...models.post_routines_routine_id_steps_validate_body_type_0_type_2 import (
    PostRoutinesRoutineIdStepsValidateBodyType0Type2,
)
from ...models.post_routines_routine_id_steps_validate_body_type_0_type_3 import (
    PostRoutinesRoutineIdStepsValidateBodyType0Type3,
)
from ...models.post_routines_routine_id_steps_validate_body_type_0_type_4 import (
    PostRoutinesRoutineIdStepsValidateBodyType0Type4,
)
from ...models.post_routines_routine_id_steps_validate_body_type_0_type_5 import (
    PostRoutinesRoutineIdStepsValidateBodyType0Type5,
)
from ...models.post_routines_routine_id_steps_validate_body_type_0_type_6 import (
    PostRoutinesRoutineIdStepsValidateBodyType0Type6,
)
from ...models.post_routines_routine_id_steps_validate_body_type_1 import (
    PostRoutinesRoutineIdStepsValidateBodyType1,
)
from ...types import Response


def _get_kwargs(
    routine_id: int,
    *,
    body: PostRoutinesRoutineIdStepsValidateBodyType0Type0
    | PostRoutinesRoutineIdStepsValidateBodyType0Type1
    | PostRoutinesRoutineIdStepsValidateBodyType0Type2
    | PostRoutinesRoutineIdStepsValidateBodyType0Type3
    | PostRoutinesRoutineIdStepsValidateBodyType0Type4
    | PostRoutinesRoutineIdStepsValidateBodyType0Type5
    | PostRoutinesRoutineIdStepsValidateBodyType0Type6
    | PostRoutinesRoutineIdStepsValidateBodyType1,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/routines/{routine_id}/steps/validate".format(
            routine_id=routine_id,
        ),
    }

    _kwargs["json"]: dict[str, Any]
    if isinstance(body, PostRoutinesRoutineIdStepsValidateBodyType0Type0):
        _kwargs["json"] = body.to_dict()
    elif isinstance(body, PostRoutinesRoutineIdStepsValidateBodyType0Type1):
        _kwargs["json"] = body.to_dict()
    elif isinstance(body, PostRoutinesRoutineIdStepsValidateBodyType0Type2):
        _kwargs["json"] = body.to_dict()
    elif isinstance(body, PostRoutinesRoutineIdStepsValidateBodyType0Type3):
        _kwargs["json"] = body.to_dict()
    elif isinstance(body, PostRoutinesRoutineIdStepsValidateBodyType0Type4):
        _kwargs["json"] = body.to_dict()
    elif isinstance(body, PostRoutinesRoutineIdStepsValidateBodyType0Type5):
        _kwargs["json"] = body.to_dict()
    elif isinstance(body, PostRoutinesRoutineIdStepsValidateBodyType0Type6):
        _kwargs["json"] = body.to_dict()
    else:
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | str | None:
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204

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
    routine_id: int,
    *,
    client: AuthenticatedClient | Client,
    body: PostRoutinesRoutineIdStepsValidateBodyType0Type0
    | PostRoutinesRoutineIdStepsValidateBodyType0Type1
    | PostRoutinesRoutineIdStepsValidateBodyType0Type2
    | PostRoutinesRoutineIdStepsValidateBodyType0Type3
    | PostRoutinesRoutineIdStepsValidateBodyType0Type4
    | PostRoutinesRoutineIdStepsValidateBodyType0Type5
    | PostRoutinesRoutineIdStepsValidateBodyType0Type6
    | PostRoutinesRoutineIdStepsValidateBodyType1,
) -> Response[Any | str]:
    """Validates a new step for the specified routine.

    Args:
        routine_id (int):
        body (PostRoutinesRoutineIdStepsValidateBodyType0Type0 |
            PostRoutinesRoutineIdStepsValidateBodyType0Type1 |
            PostRoutinesRoutineIdStepsValidateBodyType0Type2 |
            PostRoutinesRoutineIdStepsValidateBodyType0Type3 |
            PostRoutinesRoutineIdStepsValidateBodyType0Type4 |
            PostRoutinesRoutineIdStepsValidateBodyType0Type5 |
            PostRoutinesRoutineIdStepsValidateBodyType0Type6 |
            PostRoutinesRoutineIdStepsValidateBodyType1):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | str]
    """

    kwargs = _get_kwargs(
        routine_id=routine_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    routine_id: int,
    *,
    client: AuthenticatedClient | Client,
    body: PostRoutinesRoutineIdStepsValidateBodyType0Type0
    | PostRoutinesRoutineIdStepsValidateBodyType0Type1
    | PostRoutinesRoutineIdStepsValidateBodyType0Type2
    | PostRoutinesRoutineIdStepsValidateBodyType0Type3
    | PostRoutinesRoutineIdStepsValidateBodyType0Type4
    | PostRoutinesRoutineIdStepsValidateBodyType0Type5
    | PostRoutinesRoutineIdStepsValidateBodyType0Type6
    | PostRoutinesRoutineIdStepsValidateBodyType1,
) -> Any | str | None:
    """Validates a new step for the specified routine.

    Args:
        routine_id (int):
        body (PostRoutinesRoutineIdStepsValidateBodyType0Type0 |
            PostRoutinesRoutineIdStepsValidateBodyType0Type1 |
            PostRoutinesRoutineIdStepsValidateBodyType0Type2 |
            PostRoutinesRoutineIdStepsValidateBodyType0Type3 |
            PostRoutinesRoutineIdStepsValidateBodyType0Type4 |
            PostRoutinesRoutineIdStepsValidateBodyType0Type5 |
            PostRoutinesRoutineIdStepsValidateBodyType0Type6 |
            PostRoutinesRoutineIdStepsValidateBodyType1):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | str
    """

    return sync_detailed(
        routine_id=routine_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    routine_id: int,
    *,
    client: AuthenticatedClient | Client,
    body: PostRoutinesRoutineIdStepsValidateBodyType0Type0
    | PostRoutinesRoutineIdStepsValidateBodyType0Type1
    | PostRoutinesRoutineIdStepsValidateBodyType0Type2
    | PostRoutinesRoutineIdStepsValidateBodyType0Type3
    | PostRoutinesRoutineIdStepsValidateBodyType0Type4
    | PostRoutinesRoutineIdStepsValidateBodyType0Type5
    | PostRoutinesRoutineIdStepsValidateBodyType0Type6
    | PostRoutinesRoutineIdStepsValidateBodyType1,
) -> Response[Any | str]:
    """Validates a new step for the specified routine.

    Args:
        routine_id (int):
        body (PostRoutinesRoutineIdStepsValidateBodyType0Type0 |
            PostRoutinesRoutineIdStepsValidateBodyType0Type1 |
            PostRoutinesRoutineIdStepsValidateBodyType0Type2 |
            PostRoutinesRoutineIdStepsValidateBodyType0Type3 |
            PostRoutinesRoutineIdStepsValidateBodyType0Type4 |
            PostRoutinesRoutineIdStepsValidateBodyType0Type5 |
            PostRoutinesRoutineIdStepsValidateBodyType0Type6 |
            PostRoutinesRoutineIdStepsValidateBodyType1):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | str]
    """

    kwargs = _get_kwargs(
        routine_id=routine_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    routine_id: int,
    *,
    client: AuthenticatedClient | Client,
    body: PostRoutinesRoutineIdStepsValidateBodyType0Type0
    | PostRoutinesRoutineIdStepsValidateBodyType0Type1
    | PostRoutinesRoutineIdStepsValidateBodyType0Type2
    | PostRoutinesRoutineIdStepsValidateBodyType0Type3
    | PostRoutinesRoutineIdStepsValidateBodyType0Type4
    | PostRoutinesRoutineIdStepsValidateBodyType0Type5
    | PostRoutinesRoutineIdStepsValidateBodyType0Type6
    | PostRoutinesRoutineIdStepsValidateBodyType1,
) -> Any | str | None:
    """Validates a new step for the specified routine.

    Args:
        routine_id (int):
        body (PostRoutinesRoutineIdStepsValidateBodyType0Type0 |
            PostRoutinesRoutineIdStepsValidateBodyType0Type1 |
            PostRoutinesRoutineIdStepsValidateBodyType0Type2 |
            PostRoutinesRoutineIdStepsValidateBodyType0Type3 |
            PostRoutinesRoutineIdStepsValidateBodyType0Type4 |
            PostRoutinesRoutineIdStepsValidateBodyType0Type5 |
            PostRoutinesRoutineIdStepsValidateBodyType0Type6 |
            PostRoutinesRoutineIdStepsValidateBodyType1):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | str
    """

    return (
        await asyncio_detailed(
            routine_id=routine_id,
            client=client,
            body=body,
        )
    ).parsed
