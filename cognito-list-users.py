from warrant import Cognito
import argparse
import sys

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


def get_user_pool_list():
    pool_args = get_args()
    user_pool = Cognito(pool_args['user_pool_id'], pool_args['client_id'])
    user_pool_list = user_pool.get_users()

    return user_pool_list


if __name__ == "__main__":

    pool_list = get_user_pool_list()

    for pool_user in pool_list:
        print (pool_user._data)
