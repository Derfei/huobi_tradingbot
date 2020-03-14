# -*- coding: utf-8 -*-
import argparse

from trading_robot import Trading_Robot
def get_parse():
    '''
    配置相应的参数
    --traing: 表示是否进行训练
    --key: huobi Global Access key

    :return:
    '''

    parse = argparse.ArgumentParser(description=r'''
    *************************************************
    **                Trading robot               ***
    **                    derfei                  ***
    **                 version: 0.0               ***
    *************************************************
    ''')
    parse.add_argument('--train', default=False, help="training the robot(defalut is False) True or False")
    parse.add_argument('--acess-key', help="the access key for the houbi trading", required=True)

    return parse

if __name__ == "__main__":
    parse = get_parse()

    args = parse.parse_args()
    trading_robot = Trading_Robot()
    trading_robot.run(args)





