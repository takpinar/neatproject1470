def delta(c1, c2, c3, genome1, genome2):
  genes1 = genome1.genes
  genes2 = genome2.genes
  n = max(len(genes1), len(genes2))
  
  excess = 0
  disjoint = 0
  matching = 0
  total_diff = 0

  # find excess and disjoint count 
  i = 0
  j = 0
  while i < len(genes1) or j < len(genes2):
    if i >= len(genes1):
      excess += (len(genes2) - j)
      break
    elif j >= len(genes2):
      excess += (len(genes1) - i)
      break

    gene1 = genes1[i]
    gene2 = genes2[j]

    if gene1.ino == gene2.ino:
      # calculate diff
      diff = abs(gene1.w - gene2.w)
      total_diff += diff
      matching += 1
      i += 1
      j += 1
    elif gene1.ino < gene2.ino:
      disjoint += 1
      i += 1
    else:
      disjoint += 1
      j += 1

  delta = c1 * (excess / n) + c2 * (disjoint / n) + c3 * (total_diff/ matching)
  return delta
    

