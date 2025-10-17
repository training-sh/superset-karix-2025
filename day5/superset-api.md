```
docker exec -it superset_app bash

curl -X POST "http://localhost:8088/api/v1/security/login" \
  -H "Content-Type: application/json" \
  -d '{
        "username": "admin",
        "password": "admin",
        "provider": "db",
        "refresh": true
      }'


{"access_token":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6dHJ1ZSwiaWF0IjoxNzYwMTAzNzU2LCJqdGkiOiJkNTVjZTNlMS04MTI4LTQzZmYtODkwMi02YjJlNDZiODMzNzUiLCJ0eXBlIjoiYWNjZXNzIiwic3ViIjoiMSIsIm5iZiI6MTc2MDEwMzc1NiwiY3NyZiI6IjkxYWI4ZDMxLWE2NzgtNGVlZi04YTI2LTdmMmFjMmM4NjRkMSIsImV4cCI6MTc2MDEwNzM1Nn0.bohY_YfwXRTD7RCX2vRPGaVVVVaBxeEh6zFs_A3S9dI",

"refresh_token":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTc2MDEwMzc1NiwianRpIjoiYTE5NmJkMTMtMTlhNi00YzQ4LWJkN2QtNTExMmRiNjQ0MmUwIiwidHlwZSI6InJlZnJlc2giLCJzdWIiOiIxIiwibmJmIjoxNzYwMTAzNzU2LCJjc3JmIjoiMDNhNjM2OGItYjMyZi00MzAxLTkxYjctZWM3NzQzNmMwYmQwIiwiZXhwIjoxNzYwNzA4NTU2fQ.1GIMBgT9rIXtWQdAK3UK-mwNSmuRehFPQxVGEwQ5ZXA"}

{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTc2MDEwNDI3NywianRpIjoiOWNkMDE2MzMtYTI2Yi00YmY3LTg3ZDgtNDQzMTJkMGNmZTRhIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6IjEiLCJuYmYiOjE3NjAxMDQyNzcsImNzcmYiOiIxYTQyOGFiNS1kYzIwLTRlMzItOGQ5Zi0xM2FjMDk5MjMyZTIiLCJleHAiOjE3NjAxMDc4Nzd9.Ny9_7etuX-5g7fKpldTgjreUD21p8s68PSeAVFhVNWM"
}


    }'
{"access_token":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6dHJ1ZSwiaWF0IjoxNzYwMTA3OTk1LCJqdGkiOiI3YzM1M2QwMy00MmI5LTQ4ZWItYTM4OC1lZDEyMzNmYzc1ZDUiLCJ0eXBlIjoiYWNjZXNzIiwic3ViIjoiMSIsIm5iZiI6MTc2MDEwNzk5NSwiY3NyZiI6IjQ3MmM1MzkxLWRjZjMtNGMwMy1iMWNjLTRiZmRkYWE4NGQ4OCIsImV4cCI6MTc2MDExMTU5NX0._KuY9dM0PedL-YeZMpPHy55s_A8lCRwip9Hz3SG_86c","refresh_token":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTc2MDEwNzk5NSwianRpIjoiMjM5YmE5ZmMtMTBhZC00ZjJiLTgxZGEtZjdmMjJhYWQyZjE2IiwidHlwZSI6InJlZnJlc2giLCJzdWIiOiIxIiwibmJmIjoxNzYwMTA3OTk1LCJjc3JmIjoiZDdhNWE1ZDItZDQ3Mi00ZjE2LWE2NzUtOGMwMjdhOTc1Mjg5IiwiZXhwIjoxNzYwNzEyNzk1fQ.s4h5W95eZpPH1VQ-DHoY6e2_fPvWFjIsjeJ5nUeMyL0"}

superset@bc68a11deaae:/app$


BASE='http://localhost:8088'

ACCESS_TOKEN='eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTc2MDEwNDI3NywianRpIjoiOWNkMDE2MzMtYTI2Yi00YmY3LTg3ZDgtNDQzMTJkMGNmZTRhIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6IjEiLCJuYmYiOjE3NjAxMDQyNzcsImNzcmYiOiIxYTQyOGFiNS1kYzIwLTRlMzItOGQ5Zi0xM2FjMDk5MjMyZTIiLCJleHAiOjE3NjAxMDc4Nzd9.Ny9_7etuX-5g7fKpldTgjreUD21p8s68PSeAVFhVNWM'

ADMIN_ACCESS_TOKEN='eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6dHJ1ZSwiaWF0IjoxNzYwMTAzNzU2LCJqdGkiOiJkNTVjZTNlMS04MTI4LTQzZmYtODkwMi02YjJlNDZiODMzNzUiLCJ0eXBlIjoiYWNjZXNzIiwic3ViIjoiMSIsIm5iZiI6MTc2MDEwMzc1NiwiY3NyZiI6IjkxYWI4ZDMxLWE2NzgtNGVlZi04YTI2LTdmMmFjMmM4NjRkMSIsImV4cCI6MTc2MDEwNzM1Nn0.bohY_YfwXRTD7RCX2vRPGaVVVVaBxeEh6zFs_A3S9dI'

REFRESH_TOKEN='eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTc2MDEwMzc1NiwianRpIjoiYTE5NmJkMTMtMTlhNi00YzQ4LWJkN2QtNTExMmRiNjQ0MmUwIiwidHlwZSI6InJlZnJlc2giLCJzdWIiOiIxIiwibmJmIjoxNzYwMTAzNzU2LCJjc3JmIjoiMDNhNjM2OGItYjMyZi00MzAxLTkxYjctZWM3NzQzNmMwYmQwIiwiZXhwIjoxNzYwNzA4NTU2fQ.1GIMBgT9rIXtWQdAK3UK-mwNSmuRehFPQxVGEwQ5ZXA'


AUTH_HEADER="Authorization: Bearer $ACCESS_TOKEN"


## get who is it

 

curl -s -X GET "$BASE/api/v1/dashboard/" \
  -H "$AUTH_HEADER" \
  -H "Accept: application/json" | jq .


  curl -s -X GET "$BASE/api/v1/dashboard/14" \
  -H "$AUTH_HEADER" -H "Accept: application/json" | jq .


  curl -s -X GET "$BASE/api/v1/chart/" \
  -H "$AUTH_HEADER" -H "Accept: application/json" | jq .


  curl -s -X GET "$BASE/api/v1/chart/12" \
  -H "$AUTH_HEADER" -H "Accept: application/json" | jq .

  curl -s -X GET "$BASE/api/v1/dataset/" \
  -H "$AUTH_HEADER" -H "Accept: application/json" | jq .

  curl -s -X GET "$BASE/api/v1/table/" \
  -H "$AUTH_HEADER" -H "Accept: application/json" | jq .

  curl -s -X GET "$BASE/api/v1/database/" \
  -H "$AUTH_HEADER" -H "Accept: application/json" | jq .


  curl -s -X GET "$BASE/api/v1/user/" \
  -H "$AUTH_HEADER" -H "Accept: application/json" | jq .

  curl -s -X GET "$BASE/api/v1/user/1" \
  -H "$AUTH_HEADER" -H "Accept: application/json" | jq .

  curl -s -X GET "$BASE/api/v1/role/" \
  -H "$AUTH_HEADER" -H "Accept: application/json" | jq .

  curl -s -X GET "$BASE/api/v1/role/1" \
  -H "$AUTH_HEADER" -H "Accept: application/json" | jq .

  curl -s -G "$BASE/api/v1/dashboard/" \
  -H "$AUTH_HEADER" -H "Accept: application/json" \
  --data-urlencode 'q={"page":0,"page_size":50}' | jq .




curl -s -X POST "$BASE/api/v1/security/refresh" \
  -H "Authorization: Bearer $REFRESH_TOKEN" \
  -H "Content-Type: application/json" | jq .

shall provide new access token



# GUEST TOKEN


reate a guest token (admin-only call)


cat >/tmp/payload.json <<'JSON'
{
  "user": { "username": "guest_42", "first_name": "Guest" },
  "resources": [ { "type": "dashboard", "id": "1" } ],
  "rls": [ { "clause": "org_id = 42", "dataset_id": "123" } ]
}
JSON

# get and save csrf & cookie
curl -s -c /tmp/sup_cookies.txt -X GET "$BASE/api/v1/security/csrf_token/" \
  -H "Authorization: Bearer $ADMIN_ACCESS_TOKEN" \
  -H "Accept: application/json" | jq .

# extract token into $CSRF (adjust jq key if required)
CSRF=$(curl -s -c /tmp/sup_cookies.txt -X GET "$BASE/api/v1/security/csrf_token/" \
  -H "Authorization: Bearer $ADMIN_ACCESS_TOKEN" \
  -H "Accept: application/json" | jq -r '.result // .csrf_token // empty')

echo "csrf=$CSRF"

curl -i -b /tmp/sup_cookies.txt -X POST "$BASE/api/v1/security/guest_token/" \
  -H "Authorization: Bearer $ADMIN_ACCESS_TOKEN" \
  -H "X-CSRFToken: $CSRF" \
  -H "Content-Type: application/json" \
  -d @/tmp/payload.json


{"token":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjp7InVzZXJuYW1lIjoiZ3Vlc3RfNDIiLCJmaXJzdF9uYW1lIjoiR3Vlc3QifSwicmVzb3VyY2VzIjpbeyJ0eXBlIjoiZGFzaGJvYXJkIiwiaWQiOiIxIn1dLCJybHNfcnVsZXMiOlt7ImNsYXVzZSI6Im9yZ19pZCA9IDQyIn1dLCJpYXQiOjE3NjAwOTEwNzYuNjc4MzcwNSwiZXhwIjoxNzYwMDkxNjc2LjY3ODM3MDUsImF1ZCI6Imh0dHA6Ly8wLjAuMC4wOjgwODAvIiwidHlwZSI6Imd1ZXN0In0.sm8ypyhmaPGhd91mbqW0OTRsKj6ewjo5o9uTo-GoRjc"}


GUEST_TOKEN='eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjp7InVzZXJuYW1lIjoiZ3Vlc3RfNDIiLCJmaXJzdF9uYW1lIjoiR3Vlc3QifSwicmVzb3VyY2VzIjpbeyJ0eXBlIjoiZGFzaGJvYXJkIiwiaWQiOiIxIn1dLCJybHNfcnVsZXMiOlt7ImNsYXVzZSI6Im9yZ19pZCA9IDQyIn1dLCJpYXQiOjE3NjAwOTEwNzYuNjc4MzcwNSwiZXhwIjoxNzYwMDkxNjc2LjY3ODM3MDUsImF1ZCI6Imh0dHA6Ly8wLjAuMC4wOjgwODAvIiwidHlwZSI6Imd1ZXN0In0.sm8ypyhmaPGhd91mbqW0OTRsKj6ewjo5o9uTo-GoRjc'

curl -i -X GET "$BASE/api/v1/dashboard/1" \
  -H "X-GuestToken: $GUEST_TOKEN" \
  -H "Accept: application/json"

#  | jq . fails..




# try common fields; adjust jq path if needed
CSRF=$(curl -s -c /tmp/sup_cookies.txt -X GET "$BASE/api/v1/security/csrf_token/" \
  -H "Authorization: Bearer $ADMIN_ACCESS_TOKEN" \
  -H "Accept: application/json" | jq -r '.result // .csrf_token // empty')

echo "csrf=$CSRF"


Endpoint (Superset):
 
 curl -i -v -X POST "$BASE/api/v1/security/guest_token" \
  -H "Authorization: Bearer $ADMIN_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "user":{"username":"guest_42","first_name":"Guest"},
    "resources":[{"type":"dashboard","id":1}],
    "rls":[{"clause":"org_id = 42", "dataset_id": 123}]
  }'




```
