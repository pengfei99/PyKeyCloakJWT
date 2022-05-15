# ./get-kc-jwt-token.sh localhost:8080 pengfei-test toto pengfei-dv-app

REALM_NAME=pengfei-test
HOSTNAME=127.0.0.1:8080
USERNAME=pengfei
CLIENT_ID=pengfei-dv-app
CLIENT_SECRET=enifviJDIpbN5230yfcPo7h2zsifTa2z
PASSWORD=toto

KEYCLOAK_URL=http://$HOSTNAME/auth/realms/$REALM_NAME/protocol/openid-connect/token
echo $KEYCLOAK_URL

curl -X POST "$KEYCLOAK_URL" "--insecure" \
 -H "Content-Type: application/x-www-form-urlencoded" \
 -d "username=$USERNAME" \
 -d "password=$PASSWORD" \
 -d 'grant_type=password' \
 -d "client_id=$CLIENT_ID" \
 -d "client_secret=$CLIENT_SECRET"