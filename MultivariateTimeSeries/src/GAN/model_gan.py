# Generator network
import torch.nn as nn
import torch
import numpy as np


class Generator(nn.Module):
    """
    This class defines the generator network
    """
    def __init__(self, latent_dim=100, output_dim=100):
        super(Generator, self).__init__()
        self.latent_dim = latent_dim
        self.model = nn.Sequential(
            nn.Linear(latent_dim, 256),
            nn.ReLU(),
            nn.Linear(256, 128),
            nn.ReLU(),
            nn.Linear(128, output_dim)
        )

    def forward(self, x):
        """This function defines the forward pass of the generator network

        Args:
            x (_type_): _description_

        Returns:
            _type_: _description_
        """
        return self.model(x)


# Discriminator Network
class Discriminator(nn.Module):
    """_summary_

    Args:
        nn (_type_): _description_
    """
    def __init__(self, input_dim=100):
        super(Discriminator, self).__init__()
        self.model = nn.Sequential(
            nn.Linear(input_dim, 128),
            nn.ReLU(),
            nn.Linear(128, 64),
            nn.ReLU(),
            nn.Linear(64, 1),
            # nn.Dropout(p=0.2),
            nn.Sigmoid()
        )

    def forward(self, x):
        """_summary_

        Args:
            x (_type_): _description_

        Returns:
            _type_: _description_
        """
        return self.model(x)


# Function to train the discriminator
def train_discriminator(discriminator, optimizer_d, real_data, fake_data, loss: nn.BCELoss):
    """_summary_

    Args:
        discriminator (_type_): _description_
        optimizer_d (_type_): _description_
        real_data (_type_): _description_
        fake_data (_type_): _description_

    Returns:
        _type_: _description_
    """
    optimizer_d.zero_grad()
    # Real data shape: torch.Size([100, 100])
    # Fake data shape: torch.Size([100, 100])
    # Train on real data
    prediction_real = discriminator(real_data)
    error_real = loss(prediction_real, torch.ones_like(prediction_real))

    # Train on fake data
    prediction_fake = discriminator(fake_data.detach())
    error_fake = loss(prediction_fake, torch.zeros_like(prediction_fake))

    # Combine errors
    error = error_real + error_fake
    error.backward()

    optimizer_d.step()

    return error


def train_generator(
    generator,
    discriminator,
    optimizer_g,
    latent_dim,
    batch_size,
    loss: nn.BCELoss
):
    """_summary_

    Args:
        generator (_type_): _description_
        discriminator (_type_): _description_
        optimizer_g (_type_): _description_
        latent_dim (_type_): _description_
        batch_size (_type_): _description_

    Returns:
        _type_: _description_
    """
    optimizer_g.zero_grad()

    # Generate new fake data
    noise = torch.randn(batch_size, latent_dim)
    fake_data = generator(noise)

    # Discriminator evaluates the fake data
    prediction = discriminator(fake_data)
    error = loss(prediction, torch.ones_like(prediction))

    error.backward()
    optimizer_g.step()

    return error


def generate_real_samples(batch_size):
    """_summary_

    Args:
        batch_size (_type_): _description_

    Returns:
        _type_: _description_
    """
    # 定义数据点
    x = np.linspace(0, 1 * np.pi, 100)  # 生成从0到π的128个点
    y = np.sin(x)  # 计算每个点的正弦值
    # 使用索引作为x轴
    index = np.arange(100)  # 生成一个从0到n-1的整数序列
    # 当使用代码 data = np.tile(y, (batch_size, 2)) 并且 y 是数组 [1, 2, 3]，batch_size 为 4，
    # 这里的意思是 y 将在第一个维度（行）重复 4 次，在第二个维度（列）重复 2 次。
    # [[1, 2, 3, 1, 2, 3],
    # [1, 2, 3, 1, 2, 3],
    # [1, 2, 3, 1, 2, 3],
    # [1, 2, 3, 1, 2, 3]]
    data = np.tile(y, (batch_size, 1))

    return index, y, data
