import numpy as np
import retriever
def test_cosine_sim():
    v1 = np.array([1,2,3])
    v2 = np.array([1,2,3])
    cos_sim = retriever.cosineSimilarity(v1,v2)
    print(cos_sim)
    assert cos_sim == 1

def test_cos_sim_2():
    v1 = np.array([1,1.3,2.3,1.2,1.5])
    v2 = np.array([1,1.2,2.1,-1.1,1.8])
    cos_sim = retriever.cosineSimilarity(v1,v2)
    assert round(float(cos_sim),2) == 0.76