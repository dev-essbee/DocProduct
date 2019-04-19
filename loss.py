import tensorflow as tf


def qa_pair_loss(y_true, y_pred):
    y_true = tf.eye(y_pred.shape[0])*2-1
    q_embedding, a_embedding = tf.unstack(y_pred, axis=1)
    q_embedding = q_embedding / \
        tf.norm(q_embedding, axis=-1, keepdims=True)
    a_embedding = a_embedding / \
        tf.norm(a_embedding, axis=-1, keepdims=True)
    similarity_matrix = tf.matmul(
        q_embedding, a_embedding, transpose_b=True)
    return tf.norm(y_true - similarity_matrix)