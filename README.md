
# Sinc Kernel Function (SKF)
Implementation of: _"The Periodic Sinc Kernel: Theoretical Design and Applications in Machine Learning and Scientific Computing"_    [Link to Paper](https://www.sciencedirect.com/science/article/abs/pii/S1568494625004624)

---

## 🔧 Overview
This repository provides a Python package implementing the propoesed kernel function described in the paper. The package can be installed via `pip`:

```bash
pip install sinc
```
---

## 🧪 Usage

### SKF for SVMs
Use `sinc.SKF` as the kernel function for solving classification/regression tasks.
```python
from sinc import SKF
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC

X, y = load_iris(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = SVC(kernel=SKF(sigma=0.1))
model.fit(X_train, y_train)
score = model.score(X_test, y_test)
print(f"Test accuracy: {score:.2f}")
```
## Nystroem Kernel Approximation
Use `sinc.NystroemSKF` to approximate the kernel function using a subset of training data.
```python
from sinc import NystroemSKF
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.svm import SVC

X, y = load_iris(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

pipeline = make_pipeline(NystroemSKF(sigma=0.1, random_state=42), SVC(kernel="linear"))

pipeline.fit(X_train, y_train)
score = pipeline.score(X_test, y_test)
print(f"Test accuracy: {score:.2f}")
```
## Solving ODEs
Use `sinc.SincODE` to solve linear boundary value Ordinary Differential Equations (ODEs). As an example consider the following linear boundary value problem:

$$
-u''(x) + 2 u(x) = e^{-x^2}\left[\left(8-4x^2\right)\sin\left(2x\right) + 8x\cos\left(2x\right)\right]
$$

This problem is set on the entire real line, i.e. $(-\infty, \infty)$, with boundary conditions $u(\pm \infty) = 0$, and its solution exhibits both periodic behavior and decay to zero at infinity.

```python
from sinc import SincODE
import numpy as np

f = lambda x: np.exp(-(x**2)) * ((8 - 4 * x**2) * np.sin(2 * x) + 8 * x * np.cos(2 * x))

ode = lambda D, x: -D[2] + 2 * D[0]
solver = SincODE(ode, f, kernel_mode=False)
solver.solve(n=40, sigma=10)

x = np.linspace(-100, 100, 500)
y_pred = solver.predict(x)
y_ex = np.exp(-(x**2)) * np.sin(2 * x)
np.abs(y_ex - y_pred).mean()
```

---

## 📚 Citation

If you use this module, please cite:
```bibtex
@article{aghaei2025periodic,
title = {The periodic Sinc kernel: Theoretical design and applications in machine learning and scientific computing},
journal = {Applied Soft Computing},
pages = {113151},
year = {2025},
issn = {1568-4946},
doi = {https://doi.org/10.1016/j.asoc.2025.113151},
url = {https://www.sciencedirect.com/science/article/pii/S1568494625004624},
author = {Alireza Afzal Aghaei}
}
```

---

## 🤝 Contact
For questions or collaboration, create issue, pull request or contact:  
Alireza Afzal Aghaei – [alirezaafzalaghaei@gmail.com]  
