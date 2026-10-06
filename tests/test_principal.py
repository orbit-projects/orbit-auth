# Copyright 2026-present Orbit Contributors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Principal-owned identity and role validation checks."""

import pytest

from orbit_auth import Identity, Principal


@pytest.mark.parametrize("value", ["", "reader role", "reader\nrole", "reader\x7frole"])
def test_principal_rejects_unsafe_role_text(value: str) -> None:
    with pytest.raises((TypeError, ValueError), match="role|scope|identifier"):
        Principal(identity=Identity(subject="user", provider="test"), roles=frozenset({value}))


def test_principal_rejects_byte_role_coercion() -> None:
    with pytest.raises((TypeError, ValueError)):
        Principal(
            identity=Identity(subject="user", provider="test"),
            roles=frozenset({b"admin"}),  # type: ignore[arg-type]
        )


def test_principal_bounds_role_cardinality() -> None:
    with pytest.raises(ValueError, match="1,024"):
        Principal(
            identity=Identity(subject="user", provider="test"),
            roles=frozenset(f"role-{index}" for index in range(1_025)),
        )


def test_identity_rejects_non_string_claim_keys() -> None:
    with pytest.raises(ValueError, match="keys"):
        Identity(
            subject="user",
            provider="test",
            claims={b"iss": "issuer"},  # type: ignore[dict-item]
        )
