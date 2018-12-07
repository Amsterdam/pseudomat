#!/usr/bin/env bash

# Assert this file is SOURCED, not EXECUTED.
if [ "$0" = "${BASH_SOURCE[0]}" ]; then
    echo "Error: bash script $0 needs to be sourced, not executed." >&2
    exit 1
fi

export OIDC_RP_CLIENT_ID='pseudomat-dev'
export OIDC_RP_CLIENT_SECRET='<CLIENT_SECRET>'
export OIDC_OP_AUTHORIZATION_ENDPOINT='https://acc.iam.amsterdam.nl/auth/realms/datapunt/protocol/openid-connect/auth'
export OIDC_OP_TOKEN_ENDPOINT='https://acc.iam.amsterdam.nl/auth/realms/datapunt/protocol/openid-connect/token'
export OIDC_OP_USER_ENDPOINT='https://acc.iam.amsterdam.nl/auth/realms/datapunt/protocol/openid-connect/userinfo'
export OIDC_OP_JWKS_ENDPOINT='https://acc.iam.amsterdam.nl/auth/realms/datapunt/protocol/openid-connect/certs'
