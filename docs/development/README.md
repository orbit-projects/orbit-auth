# orbit-auth development

```bash
python -m pip install -e ../orbit-core
python -m pip install -e '.[dev]'
pytest
ruff check src tests
ruff format --check src tests
mypy
python -m build
```

Keep vendor SDKs and provider transports in the relevant `orbit-auth-*` integration. Add tests for
credential redaction, invalid and boundary input, cancellation, and deny-by-default behavior.
Credential-bearing live tests must be opt-in and use dedicated non-production identities.
