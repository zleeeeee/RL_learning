import torch

class MLP(torch.nn.Module):

    def __init__(self,obs_size,n_act):
        super().__init__()
        self.mlp = self.__mlp(obs_size,n_act)

    def __mlp(self,obs_size,n_act):
        return torch.nn.Sequential(
            torch.nn.Linear(obs_size,50),   #线性层    in_feature:上一层神经元个数    out_feature:此层神经元个数
            torch.nn.ReLU(),
            torch.nn.Linear(50,50),
            torch.nn.ReLU(),
            torch.nn.Linear(50,n_act)
        )

    def forward(self,x):
        return self.mlp(x)