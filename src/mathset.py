def jaccard(dataset1, dataset2, g_dataset):
    m11 = 0.0
    m00 = 0.0
    m10 = 0.0
    m01 = 0.0
    for value in g_dataset:
      if value in dataset1 and value in dataset2:
        m11 += 1.0
      if value in dataset1 and value not in dataset2:
        m10 += 1.0
      if value not in dataset1 and value in dataset2:
        m01 += 1.0
      if value not in dataset1 and value not in dataset2:
        m00 += 1.0
    j = (m11) / (m11 + m10 + m01)
    return 1 - j
