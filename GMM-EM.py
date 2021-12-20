import math

def gaussian_dist(variance, mu, xi):
    coeff = 1 / math.sqrt(2 * math.pi * variance)
    exponent = - (mu - xi) ** 2 / (2 * variance)
    return coeff * math.exp(exponent)


def density_estimator(h, x, xs):
    total = sum(map(lambda xi: gaussian_dist(h ** 2, x, xi), xs))
    print(total / len(xs))


def get_mu(data):
    return sum(data) / len(data)


def get_variance(data, mu):
    return sum(map(lambda x: (x - mu) ** 2, data)) / len(data)


# Gets all the r_ik values
def get_rik(data, gmm):
    # gmm = [[pi, mu, variance]]
    riks = []

    print("r_ik values:")
    for i, x, in enumerate(data):
        total = sum(map(lambda gmm: gmm[0] * gaussian_dist(gmm[2], gmm[1], x), gmm))
        rik = list(map(lambda gmm: (gmm[0] * gaussian_dist(gmm[2], gmm[1], x) / total), gmm))
        print("\t", i, rik)
        riks.append(rik)
    
    return riks


# Updates the mu values
def gmm_mu(data, riks):
    mus = []
    for k in range(len(riks[0])):
        summation = sum(map(lambda i: riks[i][k] * data[i], range(len(data))))
        coeff = sum(map(lambda i: riks[i][k], range(len(data))))
        # print("mu{0} = {1}".format(k, summation / coeff))
        mus.append(summation / coeff)
    
    return mus

# Updates the variance values
def gmm_var(data, riks, mus):
    vars = []
    for k in range(len(riks[0])):
        summation = sum(map(lambda i: riks[i][k] * (data[i] - mus[k])**2, range(len(data))))
        coeff = sum(map(lambda i: riks[i][k], range(len(data))))
        # print("var{0} = {1}".format(k, summation / coeff))
        vars.append(summation / coeff)
    return vars

# Updates the pi values
def gmm_pi(riks):
    pis = []
    for k in range(len(riks[0])):
        pi = sum(map(lambda i: riks[i][k], range(len(data)))) / len(riks)
        # print("pi{0} = {1}".format(k, pi))
        pis.append(pi)
    return pis


# Finds the PD from the GMM model
def probability_density(x, gmm):
    total = sum(map(lambda g: g[0] * gaussian_dist(g[2], g[1], x), gmm))
    print(total)


if __name__ == "__main__":
    # Enter the data points here
    data = [
        5.92,
        2.28,
        3.85,
        5.17,
        1.75
    ]

    # Enter the GMM model details

    gmm = [
        # pi mu variance
        [0.5, 3.34, 1],
        [0.5, 6.12, 1]
    ]

    # Get all the r_ik values
    riks = get_rik(data, gmm)
    # Updated mu values
    mus = gmm_mu(data, riks)
    # Updated variance
    vars = gmm_var(data, riks, mus)
    # Updated probabilities
    pis = gmm_pi(riks)

    updated_gmm = [list(gmm) for gmm in zip(pis, mus, vars)]
    for i, g in enumerate(updated_gmm):
        print("GMM_{0}: {1}".format(i, g))

    # Generate the probability density from a GMM
    probability_density(3.13, gmm)
