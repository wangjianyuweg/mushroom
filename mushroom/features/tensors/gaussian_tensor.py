import torch
import torch.nn as nn
from mushroom.utils.features import uniform_grid


class PyTorchGaussianRBF(nn.Module):
    """
    Pytorch module to implement a gaussian radial basis function.

    """
    def __init__(self, mu, scale):
        self._mu = torch.from_numpy(mu)
        self._scale = torch.from_numpy(scale)

    def forward(self, x):
        delta = x - self._mu

        return torch.exp(-torch.sum(delta**2 / self._scale, 1))

    @staticmethod
    def generate(n_centers, ranges):
        """
        Factory method that generates the list of dictionaries to build the
        tensors representing a set of uniformly spaced Gaussian radial basis
        functions with a 25\% overlap.

        Args:
            n_centers (list): list of the number of radial basis functions to be
                              used for each dimension.
            ranges (list): list of two-elements lists specifying the range of
                           each state variable.

        Returns:
            The list of dictionaries as described above.

        """
        n_features = len(ranges)
        assert len(n_centers) == n_features
        assert len(ranges[0]) == 2

        grid, scale = uniform_grid(n_centers, ranges)

        tensor_list = list()
        for i in range(len(grid)):
            mu = grid[i, :]
            tensor_list.append(PyTorchGaussianRBF(mu, scale))

        return tensor_list


