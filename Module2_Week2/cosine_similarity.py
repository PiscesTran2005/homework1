import numpy as np
def vector_length(vector):
    len_of_vector = np.linalg.norm(vector)
    return len_of_vector

def dot_product(vector1, vector2):
    result = np.dot(vector1, vector2)
    return result

def compute_cosine(v1, v2):
  cos_sim = dot_product(v1,v2) / (vector_length(v1)*vector_length(v2))
  return cos_sim

