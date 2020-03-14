# -*- coding: utf-8 -*-
from learning import Learning_Agent
class Trading_Robot():
    '''
    交易核心类
    将交易市场提供的交易方法和交易策略进行组合
    '''

    def __init__(self):
        self.learning_agent = Learning_Agent()

        pass

    def __train(self):
        self.learning_agent.train()

    def run(self, args):
        if args.training:
            self.__train()

        pass