from warrant import Cognito
import boto3
import argparse
import sys
import json

args = ''


def get_args():
    val = {}
    parser = argparse.ArgumentParser(description='Cognito parameters')
    parser.add_argument('--user_pool_id',metavar='user_pool_id',help='Specify user pool id')
    parser.add_argument('--client_id', metavar='client_id', help='Specify user pool client id')

    global args

    args = parser.parse_args()
    val['user_pool_id'] = args.user_pool_id
    val['client_id'] = args.client_id

    if not args.user_pool_id or not args.client_id:
        parser.print_help()
        sys.exit(1)
    else:
        return val


def get_user_pool_dictionary(pool_id, client_id):

    cognito_client = boto3.client('cognito-idp')

    user_pool_dict = {}

    user_pool_identity = cognito_client.describe_user_pool(UserPoolId=pool_id)
    user_pool_client_identity = cognito_client.describe_user_pool_client(UserPoolId=pool_id, ClientId=client_id)

    user_pool = user_pool_identity['UserPool']
    user_pool_client = user_pool_client_identity['UserPoolClient']
    user_pool_dict['name'] = user_pool['Name']
    user_pool_dict['policies'] = user_pool['Policies']
    user_pool_dict['created_on'] = str(user_pool['CreationDate'])
    user_pool_dict['modified_on'] = str(user_pool['LastModifiedDate'])
    user_pool_dict['auto_verified_attributes'] = user_pool['AutoVerifiedAttributes']
    user_pool_dict['username_attributes'] = user_pool['UsernameAttributes']
    user_pool_dict['verification_message_template'] = user_pool['VerificationMessageTemplate']
    user_pool_dict['device_configuration'] = user_pool['DeviceConfiguration']
    user_pool_dict['estimated_number_of_users'] = user_pool['EstimatedNumberOfUsers']
    user_pool_dict['email_configuration'] = user_pool['EmailConfiguration']
    user_pool_dict['tags'] = user_pool['UserPoolTags']
    user_pool_dict['domain'] = user_pool['Domain']
    user_pool_dict['admin_create_user_config'] = user_pool['AdminCreateUserConfig']
    user_pool_dict['arn'] = user_pool['Arn']
    user_pool_dict['client_name'] = user_pool_client['ClientName']
    user_pool_dict['client_secret'] = user_pool_client['ClientSecret']
    user_pool_dict['client_callback_url'] = user_pool_client['CallbackURLs']
    user_pool_dict['client_logout_urls'] = user_pool_client['LogoutURLs']
    user_pool_dict['client_allowed_oauth_scopes'] = user_pool_client['AllowedOAuthScopes']
    user_pool_dict['client_allowed_oauth_flows'] = user_pool_client['AllowedOAuthFlows']
    user_pool_dict['client_explicit_oauth_flows'] = user_pool_client['ExplicitAuthFlows']

    return user_pool_dict


def get_user_pool_list(pool_id, client_id):

    user_pool = Cognito(pool_id, client_id)
    user_pool_list = user_pool.get_users()

    return user_pool_list


if __name__ == "__main__":

    pool_args = get_args()
    user_pool_id = pool_args['user_pool_id']
    pool_client_id = pool_args['client_id']

    pool_dictionary = get_user_pool_dictionary(user_pool_id, pool_client_id)

    pool_user_list = get_user_pool_list(user_pool_id, pool_client_id)

    print ("User Pool description : ")

    print (json.dumps(pool_dictionary, indent=2))

    print ("User Pool users : ")

    for pool_user in pool_user_list:
        print (pool_user._data)
