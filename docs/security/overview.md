# orbit-auth security

Authentication is opt-in. There are no default accounts, default passwords, or plaintext password
stores. Protect Basic Auth with TLS, secret management, rotation, and network controls; it is not a
complete enterprise identity system.

Bearer token verification is injected. Do not accept unverified token text as identity. Configure
allowed algorithms, issuer, audience, clock policy, and key rotation explicitly. The optional JWT
integration owns cryptographic verification. The optional OAuth integration requires a secure
transaction store, atomic state consumption, PKCE, and browser-session binding for callback flows.

Keep tokens, password material, authorization codes, state, nonces, and provider responses out of
logs, traces, exceptions, and support bundles. Review effective permissions and identity-provider
settings in each deployment. The package is pre-alpha and has no production certification.
