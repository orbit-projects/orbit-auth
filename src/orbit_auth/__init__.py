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
"""Provider-neutral authentication and authorization for Orbit applications."""

from orbit.security.contracts import Authenticator, RouteAuthorizer

from orbit_auth.authorization import PolicyEngine, RoleAuthorizer, require_roles
from orbit_auth.basic import BasicAuthenticator, BasicCredential
from orbit_auth.bearer import BearerAuthenticator, TokenVerifier
from orbit_auth.identity import Identity
from orbit_auth.jwks import JsonWebKey, JsonWebKeySet, JwksProvider
from orbit_auth.oauth import (
    OAuthAuthorizationRequest,
    OAuthProvider,
    OAuthTokenResponse,
    OIDCDiscoveryDocument,
    OIDCDiscoveryProvider,
    is_https_url,
)
from orbit_auth.principal import Principal
from orbit_auth.roles import validate_role_collection, validate_role_text
from orbit_auth.tokens import Token, TokenRevocationStore
from orbit_auth.validation import TokenValidationPolicy

__all__ = [
    "Authenticator",
    "BasicAuthenticator",
    "BasicCredential",
    "BearerAuthenticator",
    "Identity",
    "JsonWebKey",
    "JsonWebKeySet",
    "JwksProvider",
    "OIDCDiscoveryDocument",
    "OIDCDiscoveryProvider",
    "OAuthAuthorizationRequest",
    "OAuthProvider",
    "OAuthTokenResponse",
    "PolicyEngine",
    "Principal",
    "RoleAuthorizer",
    "RouteAuthorizer",
    "Token",
    "TokenRevocationStore",
    "TokenVerifier",
    "TokenValidationPolicy",
    "is_https_url",
    "require_roles",
    "validate_role_collection",
    "validate_role_text",
]
