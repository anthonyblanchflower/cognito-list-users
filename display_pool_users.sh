#!/bin/bash

set -e
set -o pipefail
pwd
ls -alt

AWS_ACCESS_KEY_ID=$(aws --profile default configure get aws_access_key_id)
AWS_SECRET_ACCESS_KEY=$(aws --profile default configure get aws_secret_access_key)

docker build -t sdi/cognito-list-users .

docker run --rm \
    -e AWS_ACCESS_KEY_ID=$AWS_ACCESS_KEY_ID \
    -e AWS_SECRET_ACCESS_KEY=$AWS_SECRET_ACCESS_KEY \
    sdi/cognito-list-users \
    python /root/cognito-list-users.py --user_pool_id $1 --client_id $2 \
    --region $3 --role_arn $4
