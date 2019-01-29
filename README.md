# cognito-list-users

## Purpose

This application will print out attributes for a Cognito User Pool, User Pool Client and Cognito user list.
 
## To Use
 
The application runs from a container via the display_pool_users.sh script and requires the following parameters:

```
display_pool_users.sh <UserPoolId> <ClientId> <region> <role_arn>
```

(e.g. bash display_pool_users.sh "eu-west-1_xxxxxxx" "xxxxxxxx" "eu-west-1" "arn:aws:iam::xx:xx/xxxxxxx")

