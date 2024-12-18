"""
A set of function to generate random variables for Metalog distributions.
"""

def Metalog_SPT_Quantile_3(a1, a2, a3, y):
  """
  Metalog Quantile function for SPT with n=3
  Source: http://www.metalogdistributions.com/images/The_Metalog_Distributions_-_Keelin_2016.pdf
  See Equation (6), page 254.
  Given a uniformly distributed random variable y, returns a random value from the Metalog SPT distribution (n=3).
  """
  if y == 0:
    return - np.inf
  if y == 1:
    return + np.inf  
  return a1 + a2 * np.log(y/(1-y)) + a3 * (y-0.5) * np.log(y/(1-y))

def Metalog_SPT_constants(α, q_α, q_05, q_1_α):
  """
  Source: http://www.metalogdistributions.com/images/The_Metalog_Distributions_-_Keelin_2016.pdf
  See Equations (16) and (17), page 269.
  See Equation (18), page 269, for SPT Metalog Feasibility.
  """
  assert α not in [0,.5,1], "α > 0, α < 1, α ≠ 0.5"
  r = (q_05 - q_α) / (q_1_α - q_α)
  k_α = 0.5 * (1 - 1066711 * ( 0.5 - α))
  assert (r > k_α) and (r < (1 - k_α)), "SPT Metalog Feasibility: FAIL.\n(r > k_α) and (r < (1 - k_α))"
  return (q_05,                                                               # a1
          0.5 * np.log((1-α)/α)** -1 * (q_1_α - q_α),                         # a2
          ( 1 - 2 * α) * np.log((1-α)/α) ** -1 * (1 - 2 * r) * (q_1_α - q_α)  # a3
  )