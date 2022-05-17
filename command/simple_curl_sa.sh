# ./get-kc-jwt-token.sh localhost:8080 pengfei-test toto pengfei-dv-app

REALM_NAME=sspcloud
HOSTNAME=auth.lab.sspcloud.fr
auth_sec=

KEYCLOAK_URL=https://$HOSTNAME/auth/realms/$REALM_NAME/protocol/openid-connect/token
echo $KEYCLOAK_URL

curl -X POST "$KEYCLOAK_URL" '--insecure' \
  --header 'Content-Type: application/x-www-form-urlencoded' \
  --header "Authorization: Basic $auth_sec" \
  --data-urlencode 'grant_type=client_credentials'

