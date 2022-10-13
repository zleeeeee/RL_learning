import numpy as np
import torch



class DQNAgent(object):

    def __init__(self,q_func,optimizer,n_act,gamma=0.9,e_greed=0.1):
        self.q_func = q_func #q function

        self.optimizer = optimizer #优化器
        self.criterion = torch.nn.MSELoss()  #损失函数
        self.n_act = n_act #动作数量
        self.gamma = gamma #收益衰减率
        self.epsilon = e_greed #探索与利用中的探索概率
    
    #根据经验得到action
    def predict(self,obs):
        Q_list = self.q_func(obs)
        action = int(torch.argmax(Q_list).detach().numpy())
        return action

    #根据探索与利用得到action
    def act(self,obs):
        if np.random.uniform(0,1)<self.epsilon: #探索
            action = np.random.choice(self.n_act)
        else:#利用
            action = self.predict(obs)
        return action

    #更新Q表格
    def learn(self,obs,action,reward,next_obs,done):
        #predict_q
        pred_Vs = self.q_func(obs)      #得到二维张量（两个动作），每个动作对应不同的q值评价
        predict_Q = pred_Vs[action]     #取选取的动作的评价q

        #target_Q
        next_pred_Vs = self.q_func(next_obs)  #下一个状态的Q值
        best_V = next_pred_Vs.max()        #Qmax
        target_Q = reward + (1- float(done))*self.gamma*best_V

        #更新参数
        self.optimizer.zero_grad()    #清空过往梯度，即初始化梯度为0
        loss = self.criterion(predict_Q,target_Q)    #损失函数
        loss.backward()   #    反向传播计算梯度
        self.optimizer.step()  #      通过梯度下降更新网络参数
       