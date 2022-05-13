# ./get-kc-jwt-token.sh localhost:8080 pengfei-test toto pengfei-dv-app

REALM_NAME=pengfei-test
HOSTNAME=localhost:8080
USERNAME=toto
CLIENT_ID=pengfei-dv-app
PASSWORD=toto

KEYCLOAK_URL=http://$HOSTNAME/auth/realms/$REALM_NAME/protocol/openid-connect/token
echo $KEYCLOAK_URL

curl -X POST "$KEYCLOAK_URL" "--insecure" \
 -H "Content-Type: application/x-www-form-urlencoded" \
 -d "username=$USERNAME" \
 -d "password=$PASSWORD" \
 -d 'grant_type=password' \
 -d "client_id=$CLIENT_ID"