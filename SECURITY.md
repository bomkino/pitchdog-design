# Security

The distributed skill is intentionally text-only and contains no executable script, binary, font, private source asset, secret, telemetry, or remote tool declaration.

It points to external authorities for typography and icon packages. Treat those as normal supply-chain dependencies in the consuming project: resolve an immutable source, review it, pin it, preserve credentials outside committed files and browser code, and verify the built assets. Never hotlink authenticated font sources or copy access tokens into package URLs.

Treat any future script inside the skill, binary, data upload, secret-handling behaviour, or remote instruction as a security-sensitive change.

Report a vulnerability through GitHub's private security-advisory flow for this repository. Do not include credentials, private client material, or exploitable personal data in a public issue.

Skills run inside an agent's existing authority. A licence, validator pass, or store scan is not a security review.
