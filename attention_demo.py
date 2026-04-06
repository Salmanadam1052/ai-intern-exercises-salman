import numpy as np
from typing import Tuple


def softmax(x: np.ndarray) -> np.ndarray:
    shifted = x - np.max(x, axis=-1, keepdims=True)
    exp_x = np.exp(shifted)
    return exp_x / np.sum(exp_x, axis=-1, keepdims=True)


def scaled_dot_product_attention(
    Q: np.ndarray,
    K: np.ndarray,
    V: np.ndarray,
) -> np.ndarray:
    """
    Compute scaled dot-product attention.

    Args:
        Q: Query matrix of shape (seq_len, d_k)
        K: Key matrix of shape (seq_len, d_k)
        V: Value matrix of shape (seq_len, d_v)

    Returns:
        Attention output of shape (seq_len, d_v)
    """
    d_k = Q.shape[-1]
    attention_scores = Q @ K.T / np.sqrt(d_k)
    attention_weights = softmax(attention_scores)
    return attention_weights @ V


if __name__ == "__main__":
    np.random.seed(42)
    seq_len, d_k, d_v = 6, 8, 8

    Q = np.random.randn(seq_len, d_k)
    K = np.random.randn(seq_len, d_k)
    V = np.random.randn(seq_len, d_v)

    output = scaled_dot_product_attention(Q, K, V)

    print(f"Q shape: {Q.shape}")
    print(f"K shape: {K.shape}")
    print(f"V shape: {V.shape}")
    print(f"Attention output shape: {output.shape}")
    print(f"\nAttention output:\n{output}")
