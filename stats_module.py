import math, statistics, collections, scipy, numpy
from math import comb, factorial, e, pi
from math import floor, ceil, sqrt
from collections import Counter
from scipy import stats
import re
from decimal import Decimal



##########MISC FUNCTIONS##########

e_custom = 2.71828

def factorial_custom(n):
    i = 0
    result = 1
    while i < n:
        result *= (i+1)
        i += 1
    return result

def comb_custom(k, n):
    return factorial(n) / (factorial(k) * factorial(n-k))

def midpoint(start, end):
    return (start + end) / 2

def truncate(n, decimals=0):
    multiplier = 10 ** decimals
    return int(n * multiplier) / multiplier

def str_comma_adder(s):
    '''
    adds commas to a string of numbers separated by only white spaces
    '''
    return re.sub("\s+", ",", s.strip())

def str_to_list(s):
    '''
    converts a string representation of a list of numbers (without commas)
    into a list of numbers

    str_to_list("2, 3, NA, 4") -> [2, 3, NA, 4]

    Use String NA to represent a blank space in the list of numbers
    '''
    i = 0
    l = []
    s2 = s.split()
    for item in s2:
        if item != "NA":
            l.append(float(item.replace(',', '')))
        else:
            l.append("NA")
    return l

def split_n_columns_to_list(s, n):
    r = []
    for j in range(n):
        r.append([])
    l = str_to_list(s)
    i = 0
    for item in l:
        if item != "NA":
            r[i % n].append(item)
        i += 1
    return r

def list_rounder(l):
    rounded_l = []
    for item in l:
        rounded_l.append(round(item, 3))
    return rounded_l

##########CENTRAL TENDENCY##########

def mean_ungrouped(data_ungrouped):
    '''
    data_ungrouped   list of numbers
    '''
    result = 0
    pop_size = len(data_ungrouped)
    for data in data_ungrouped:
        result += data
    return round(result / pop_size, 4)
    
def mean_grouped(data_grouped):
    '''
    data_grouped            dict of group: frequency
    group                   tuple of (start, end)
    start, end, frequency   number
    '''
    result = 0
    pop_size = 0
    for group in data_grouped:
        start = group[0]
        end = group[1]
        class_midpoint = midpoint(start, end)
        frequency = data_grouped[group]
        result += frequency * class_midpoint
        pop_size += frequency
    return round(result / pop_size, 4)

def median_ungrouped(data_ungrouped):
    '''
    data_ungrouped   list of numbers
    '''
    return pth_percentile(data_ungrouped, 50)

def median_grouped(data_grouped):
    '''
    data_grouped            dict of group: frequency
    group                   tuple of (start, end)
    start, end, frequency   number
    '''
    pop_size = 0
    for group in data_grouped:
        frequency = data_grouped[group]
        pop_size += frequency
    median_index = pop_size / 2
    b = 0
    for group in data_grouped:
        if (b + data_grouped[group]) > median_index:
            l = group[0]
            n = pop_size
            g = data_grouped[group]
            w = group[1] - group[0]
            return l + (((n/2)-b)/g)*w
        else:
            b += data_grouped[group]

def mode_ungrouped(data_ungrouped):
    '''
    data_ungrouped   list of numbers
    '''
    data = Counter(data_ungrouped)
    return data.most_common()

def mode_grouped(data_grouped):
    '''
    data_grouped            dict of group: frequency
    group                   tuple of (start, end)
    start, end, frequency   number
    '''
    inverse = [(value, key) for key, value in data_grouped.items()]
    modal_group = max(inverse)[1]
    return midpoint(modal_group[0], modal_group[1])

def pth_percentile_ungrouped(data_ungrouped, p):
    '''
    data_ungrouped   list of numbers
    '''
    data_ungrouped.sort()
    pop_size = len(data_ungrouped)
    i = (p/100) * pop_size
    if i == ceil(i) and i == floor(i):
        # i is a natural number
        return (data_ungrouped[floor(i)-1] + data_ungrouped[floor(i)]) / 2
    else:
        # i is not a natural number
        return data_ungrouped[floor(i)]

def pth_percentile_grouped(data_grouped, m):
    '''
    data_grouped  list      list of ((start, end), frequency)
    m             number    percentile of interest
    
    p             number    mth percentile index
    l             number    lower class boundary of class containing p
    h             number    width of class containing p
    f             number    frequency of class containing p
    n             number    frequency of p
    c             number    cumulative frequency of classes
                            preceeding class containing p
    '''
    n = 0
    for group in data_grouped:
        n += group[1]
    p = (m * n) / 100
    i = 0
    c = 0
    for group in data_grouped:
        i += group[1]
        if i >= p:
            l = group[0][0]
            h = group[0][1] - group[0][0]
            f = group[1]
            return l + (((h / f) * (p - c)))
        c += group[1]

def quartiles_ungrouped(data_ungrouped):
    '''
    data_ungrouped   list of numbers
    '''
    return [pth_percentile_ungrouped(data_ungrouped, 25), pth_percentile_ungrouped(data_ungrouped, 50), pth_percentile(data_ungrouped, 75)]


##########VARIABILITY##########

def variance_ungrouped_pop(data_ungrouped):
    '''
    data_ungrouped   list of numbers
    '''
    result = 0
    pop_size = len(data_ungrouped)
    i = 0
    m = mean_ungrouped(data_ungrouped)
    while i < pop_size:
        result += pow((data_ungrouped[i] - m), 2)
        i += 1
    return round(result / pop_size, 4)

def variance_ungrouped_sample(data_ungrouped):
    '''
    data_ungrouped   list of numbers
    '''
    result = 0
    sample_size = len(data_ungrouped)
    i = 0
    m = mean_ungrouped(data_ungrouped)
    while i < sample_size:
        result += pow((data_ungrouped[i] - m), 2)
        i += 1
    return round(result / (sample_size - 1), 6)
        
def variance_grouped_pop(data_grouped):
    '''
    data_grouped            dict of group: frequency
    group                   tuple of (start, end)
    start, end, frequency   number
    '''
    result = 0
    pop_size = 0
    m = mean_ungrouped(data_grouped)
    for group in data_grouped:
        class_midpoint = midpoint(group[0], group[1])
        frequency = data_grouped[group]
        result += (frequency * pow((class_midpoint - m), 2))
        pop_size += frequency
    return round(result / pop_size, 4)

def variance_grouped_sample(data_grouped):
    '''
    data_grouped            dict of group: frequency
    group                   tuple of (start, end)
    start, end, frequency   number
    '''
    result = 0
    sample_size = 0
    m = mean_grouped(data_grouped)
    for group in data_grouped:
        class_midpoint = midpoint(group[0], group[1])
        frequency = data_grouped[group]
        result += (frequency * pow((class_midpoint - m), 2))
        sample_size += frequency
    return round(result / (sample_size - 1), 4)

def standard_deviation_ungrouped_pop(data_ungrouped):
    '''
    data_ungrouped   list of numbers
    '''
    return round(sqrt(variance_ungrouped_pop(data_ungrouped)), 4)
    
def standard_deviation_ungrouped_sample(data_ungrouped):
    '''
    data_ungrouped   list of numbers
    '''
    return round(sqrt(variance_ungrouped_sample(data_ungrouped)), 4)

def standard_deviation_grouped_pop(data_grouped):
    '''
    data_grouped            dict of group: frequency
    group                   tuple of (start, end)
    start, end, frequency   number
    '''
    return round(sqrt(variance_grouped_pop(data_grouped)), 4)

def standard_deviation_grouped_sample(data_grouped):
    '''
    data_grouped            dict of group: frequency
    group                   tuple of (start, end)
    start, end, frequency   number
    '''
    return round(sqrt(variance_grouped_sample(data_grouped)), 4)

def statistical_range(data_ungrouped):
    '''
    data_ungrouped   list of numbers
    '''
    p100 = pth_percentile(data_ungrouped, 99)
    p0 = pth_percentile(data_ungrouped, 1)
    return p100 - p0

def interquartile_range(data_ungrouped):
    '''
    data_ungrouped   list of numbers
    '''
    q3 = pth_percentile_ungrouped(data_ungrouped, 75)
    q1 = pth_percentile_ungrouped(data_ungrouped, 25)
    return q3 - q1

def mean_arithmetic_deviation(data_ungrouped):
    '''
    data_ungrouped   list of numbers
    '''
    result = 0
    i = 0
    m = mean_ungrouped(data_ungrouped)
    pop_size = len(data_ungrouped)
    while i < pop_size:
        result += abs((data_ungrouped[i] - m))
        i += 1
    return round(result / pop_size, 4)

def z_score(data_ungrouped, x):
    '''
    data_ungrouped   list of numbers
    '''
    m = mean_ungrouped(data_ungrouped)
    s = standard_deviation_ungrouped_pop(data_ungrouped)
    return round((x - m) / s, 4)

def coefficient_of_variation(data_ungrouped):
    '''
    data_ungrouped   list of numbers
    '''
    m = mean_ungrouped(data_ungrouped)
    s = standard_deviation_ungrouped_pop(data_ungrouped)
    return round((s / m) * 100, 4)

def chebyshevs_theorem(k):
    if k > 1:
        result = (1 - (1/(k**2)))
        print("k > 1 so ", result, " percent of values will\
              occur within k standard deviations of mu")
    else:
        print("k <= 1 so we don't know what percent of values will\
              occur within k standard deviations of mu")
    


##########DISCRETE DISTRIBUTIONS##########

def expected_value(data_discrete):
    '''
    data_discrete   list of tuples (value, probability)
    '''
    result = 0
    for data in data_discrete:
        result += (data[0] * data[1])
    return round(result, 4)

def variance_discrete(data_discrete):
    '''
    data_discrete   list of tuples (value, probability)
    '''
    result = 0
    m = expected_value(data_discrete)
    for data in data_discrete:
        result += (pow((data[0] - m), 2) * data[1])
    return round(result, 4)

def binomial_distribution(n, p, x):
    '''
    n    number   number of identical trials
    p    number   probability of successful outcome per trial
    x    number   number of successful outcomes per trial (sampled with replacement)
    
    successes equal to x
    P(X = x)
    '''
    result = comb(n, x) * pow(p, x) * pow(1-p, n - x)
    return round(result, 5)

def binomial_distribution_less(n, p, x):
    '''
    n    number   number of identical trials
    p    number   probability of successful outcome per trial
    x    number   number of successful outcomes per trial (sampled with replacement)
    
    successes strictly less then x
    P(X < x)
    '''
    result = 0
    i = 0
    while i < x:
        result += binomial_distribution(n, p, i)
        i += 1
    return round(result, 4)

def binomial_distribution_greater(n, p, x):
    '''
    n    number   number of identical trials
    p    number   probability of successful outcome per trial
    x    number   number of successful outcomes per trial (sampled with replacement)
    
    successes strictly greater then x
    P(x < X)
    '''
    result = 1 - binomial_distribution_less(n, p, x + 1)
    return round(result, 5)

def mean_binomial(n, p):
    '''
    n    number   number of identical trials
    p    number   probability of successful outcome per trial
    '''
    return n * p

def variance_binomial(n, p):
    '''
    n    number   number of identical trials
    p    number   probability of successful outcome per trial
    '''
    return n * p * (1 - p)

def standard_deviation_binomial(n, p):
    '''
    n    number   number of identical trials
    p    number   probability of successful outcome per trial
    '''
    return sqrt(variance_binomial(n, p))

#example: https://towardsdatascience.com/the-poisson-distribution-and-poisson-process-explained-4e2cb17d459
def poisson_distribution(lamda, x):
    '''
    lamda     number    long run average
    x         number    number of successes per interval
    
    successes equal to x
    P(X = x)
    '''
    result = (pow(lamda, x) * pow(e, -lamda)) / (factorial(x))
    return round(result, 4)

def poisson_distribution_less(lamda, x):
    '''
    lamda     number    long run average
    x         number    number of successes per interval
    
    successes strictly less then x
    P(X < x) <=> P(X = 0) + P(X = 1) + ... + P(X = x-1)
    '''
    result = 0
    i = 0
    while i < x:
        result += poisson_distribution(lamda, i)
        i += 1
    return round(result, 4)

def poisson_distribution_greater(lamda, x):
    '''
    lamda     number    long run average
    x         number    number of successes per interval
    
    successes strictly greater then n_successes_per_interval
    P(x < X) <=> 1 - P(x+1 > X)
    '''
    result = 1 - poisson_distribution_less(lamda, x + 1)
    return round(result, 5)

def poisson_distribution_between(lamda, x1, x2):
    '''
    lamda     number    long run average
    x1        number    number of successes per interval (lower bound)
    x2        number    number of successes per interval (upper bound)
    
    successes strictly greater then x1, strictly less then x2
    P(x1 < X < x2) <=> P(X < x2) - (1 - P(X < x1 + 1))
    '''
    result = poisson_distribution_less(lamda, x2) - (1 - poisson_distribution_greater(lamda, x1))
    return round(result, 4)

def mean_and_variance_of_poisson(lamda):
    '''
    lamda     number    long run average
    '''
    return lamda

def standard_deviation_of_poisson(lamda):
    '''
    lamda     number    long run average
    '''
    return round(sqrt(lamda), 4)

def hypergeometric_distribution(N, n, A, x):
    '''
    N    number    population size
    n    number    sample size
    A    number    number of successes in population
    x    number    number of successes in sample (sampled without replacement)
    
    successes equal to x
    P(X = x)
    '''
    result = (comb(A, x) * comb(N - A, n - x)) / comb(N, n)
    return round(result, 5)

def hypergeometric_distribution_less(N, n, A, x):
    '''
    N    number    population size
    n    number    sample size
    A    number    number of successes in population
    x    number    number of successes in sample (sampled without replacement)
    
    successes strictly less then x
    P(X < x) <=> P(X = 0) + P(X = 1) ... + P(X = a-1)
    '''
    i = 0
    result = 0
    while i < x:
        result += hypergeometric_distribution(N, n, N, i)
        i += 1
    return round(result, 4)
    
def hypergeometric_distribution_greater(N, n, A, x):
    '''
    N    number    population size
    n    number    sample size
    A    number    number of successes in population
    x    number    number of successes in sample (sampled without replacement)
    
    successes strictly greater then x
    P(x < X) <=> 1 - P(x+1 > X)
    '''
    result = 1 - hypergeometric_distribution_less(N, n, A, x + 1)
    return round(result, 4)


##########CONTINUOUS DISTRIBUTIONS##########

def density_function_uniform_distribution(a, b, x):
    '''
    a    number    lower bound
    b    number    upper bound
    x    number    independant variable

    returns probability density. Integrate to find probability
    '''
    if a <= x <= b:
        return 1 / (b-a)
    else:
        return 0

def mean_uniform_distribution(a, b):
    '''
    a    number    lower bound
    b    number    upper bound
    '''
    return midpoint(a, b)

def standard_deviation_uniform_distribution(a, b):
    '''
    a    number    lower bound
    b    number    upper bound
    '''
    return (b - a) / sqrt(12)

def uniform_distribution(a, b, x1, x2):
    '''
    a    number    lower bound (range)
    b    number    upper bound (range)
    x1   number    lower bound (independant variable)
    x2   number    upper bound (independant variable)

    P(x1 <= X <= x2)
    '''
    if a <= x1 and x2 <= b:
        return (x2 - x1) / (b - a)
    else:
        return 0

def density_function_normal_distribution(mu, sigma, x):
    '''
    x      number     independant variable

    returns probability density. Integrate to find probability.
    '''
    return (1/(sigma * sqrt(2 * pi))) * (e ** ((-(x - mu)**2) / (2 * (sigma ** 2))))

def density_function_z_distribution(x):
    '''
    x      number     independant variable

    set mu = 0 and sigma = 1 to use as z distribution's density function.

    returns probability density. Integrate to find probability.
    '''
    result = density_function_normal_distribution(0, 1, x)
    return result

def z_score_formula(mu, sigma, x):
    '''
    mu     number     mean
    sigma  number     standard deviation
    x      number     independant variable
    '''
    return round((x - mu)/ sigma, 4)

def p_value_from_z_score_one_sided(z):
    '''
    z      number     z-score

    P(Z < -z) or P(z < Z) depending on Null Hypothesis
    '''
    z = abs(z)
    p = scipy.integrate.quad(density_function_z_distribution, 0, z)[0]
    return round(1 - (.5 + p), 4)

def p_value_from_z_score_two_sided(z):
    '''
    z      number     z-score

    P(Z < -z) + P(z < Z)
    '''
    z = abs(z)
    p = scipy.integrate.quad(density_function_z_distribution, 0, z)[0]
    return round(p * 2, 4)

def normal_distribution_from_mu_to_x(mu, sigma, x):
    '''
    mu     number     mean
    sigma  number     standard deviation
    x      number     outcome of interest (upper bound)

    P(mu < X < x)
    '''
    z = z_score_formula(mu, sigma, x)
    return round(p_value_from_z_score_one_sided(z), 4)

def normal_distribution_neg_x_to_x(mu, sigma, x):
    '''
    mu     number     mean
    sigma  number     standard deviation
    x      number     outcome of interest (upper bound)

    P(-x < X < x)
    '''
    result = normal_distribution_from_mu_to_x(mu, sigma, x) * 2
    return round(result, 4)

def normal_distribution_neg_inf_to_x(mu, sigma, x):
    '''
    mu     number     mean
    sigma  number     standard deviation
    x      number     outcome of interest (upper bound)

    P(-inf < X < x)
    '''
    return round(0.5 + normal_distribution_from_mu_to_x(mu, sigma, x), 4)

def normal_distribution_between(mu, sigma, x1, x2):
    '''
    mu     number     mean
    sigma  number     standard deviation
    x1     number     outcome of interest (lower bound)
    x2     number     outcome of interest (upper bound)

    P(x1 < X < x2) <=> P(-inf < X < x2) - P(-inf < X < x1)
    '''
    return round(normal_distribution_neg_inf_to_x(mu, sigma, x2) - normal_distribution_neg_inf_to_x(mu, sigma, x1), 4)

def normal_distribution_x_to_inf(mu, sigma, x):
    '''
    mu     number     mean
    sigma  number     standard deviation
    x      number     outcome of interest (upper bound)

    P(x < X < inf) <=> 1 - P(-inf < X < x)
    '''
    return round(1 - normal_distribution_neg_inf_to_x(mu, sigma, x), 4)

def binomial_to_normal_converter(n, p, x, switch, x2=None):
    '''
    n        number   number of identical trials
    p        number   probability of successful outcome per trial
    x        number   independant variable
    switch   string   "P(X = x)"        <=> P(x-.5 <  X <  x+.5)
                      "P(X < x)"        <=> P(-inf <  X <  x-.5)
                      "P(X <= x)"       <=> P(-inf <  X <  x+.5)
                      "P(X > x)"        <=> P(x+.5 <  X <  inf)
                      "P(X >= x)"       <=> P(x-.5 <  X <  inf)
                      "P(x <= X <= x2)"   <=> P(x-.5 <  X <  x2+.5)
                      "P(x < X <= x2)"  <=> P(x+.5 <= X <  x2+.5)
                      "P(x <= X < x2)"  <=> P(x-.5 <  X <= x2-.5)
                      "P(x < X < x2)" <=> P(x+.5 <= X <= x2-.5)
    x2       number   upper bound (optional)
    '''
    if binomial_to_normal_checker(n, p):
        mu = binomial_to_normal_mean(n, p)
        sigma = binomial_to_normal_standard_deviation(n, p)
        if switch == "P(X = x)":
            return normal_distribution_between(mu, sigma, x-.5, x+.5)
        elif switch == "P(X < x)":
            return normal_distribution_neg_inf_to_x(mu, sigma, x-.5)            
        elif switch == "P(X <= x)":
            return normal_distribution_neg_inf_to_x(mu, sigma, x+.5)
        elif switch == "P(X > x)":
            return normal_distribution_x_to_inf(mu, sigma, x+.5)
        elif switch == "P(X >= x)":
            return normal_distribution_x_to_inf(mu, sigma, x-.5)
        elif switch == "P(x < X < x2)":
            return normal_distribution_between(mu, sigma, x+.5, x2-.5)
        elif switch == "P(x <= X < x2)":
            return normal_distribution_between(mu, sigma, x-.5, x2-.5)
        elif switch == "P(x < X <= x2)":
            return normal_distribution_between(mu, sigma, x+.5, x2+.5)
        elif switch == "P(x <= X <= x2)":
            return normal_distribution_between(mu, sigma, x-.5, x2+.5)
        else:
            print("Error: try changing the value of the switch argument")
    else:
        print("this binomial distribution cannot be approximated by a normal distribution")
        
def binomial_to_normal_mean(n, p):
    '''
    n        number   number of identical trials
    p        number   probability of successful outcome per trial
    '''
    return n * p

def binomial_to_normal_standard_deviation(n, p):
    '''
    n        number   number of identical trials
    p        number   probability of successful outcome per trial
    '''
    q = (1 - p)
    return sqrt(n * p * q)

def binomial_to_normal_checker(n, p):
    '''
    checks if this binomial distribution can be approximated by a normal distribution
    '''
    mu = binomial_to_normal_mean(n, p)
    q = (1 - p)
    sigma = binomial_to_normal_standard_deviation(n, p)
    if 0 <= (mu + (3 * sigma)) <= n and 0 <= (mu - (3 * sigma)) <= n:
        if mu > 5 and (n*q) > 5:
            return True
    return False

def density_function_exponential_distribution(lamda, x):
    '''
    lamda    number    number of successes per interval
    x        number    independant variable
    '''
    if x >= 0 and lamda > 0:
        return lamda * (e ** -(lamda * x))
    else:
        print("Not an exponential distribution")

def exponential_distribution_greater(lamda, x0):
    '''
    lamda    number    number of successes per interval
    x0       number    number of intervals between successes

    P(x0 <= X) <=> P(x0 < X)
    '''
    result = e ** (-lamda * x0)
    return f"{result:.9f}"

def exponential_distribution_less(lamda, x0):
    '''
    lamda    number    number of successes per interval
    x0       number    number of intervals between successes

    P(X <= x0) <=> 1 - P(x0 < X)
    '''
    return 1 - exponential_distribution_greater(lamda, x0)

def exponential_distribution_between(lamda, x1, x2):
    '''
    lamda    number    number of successes per interval
    x0       number    number of intervals between successes

    P(x1 < X < x2) <=> P(X < x2) - P(X < x1)
    '''
    return exponential_distribution_less(lamda, x2) - exponential_distribution_less(lamda, x1)



##########SAMPLING DISTRIBUTIONS##########

def standard_error_of_mean(n, sigma):
    '''
    sigma         number     standard deviation (population)
    n             number     sample size

    standard error of mean:  standard deviation of the sample means from an arbitrarily
                             large number of repeated samples

    returns standard error of mean
    '''
    return round(sigma / sqrt(n), 4)

def central_limit_theorem(n, mu, sigma, switch=1):
    '''
    mu            number     mean (population)
    sigma         number     standard deviation (population)
    n             number     sample size
    switch        number     1: population is Normally Distributed
                             0: otherwise
                             
    mu_x_bar      number     mean of sample means from an arbitrarily large number
                             of repeated samples
    sigma_x_bar   number     standard error of mean

    returns tuple (mu_x_bar, sigma_x_bar)
    '''
    if switch or n >= 30:
        mu_x_bar = mu
        sigma_x_bar = standard_error_of_mean(n, sigma)
        return (mu_x_bar, sigma_x_bar)
    else:
        print("fails to meet precondition: Population is Normally Distributed \
              or sample size >= 30")

def z_formula_for_sample_means(x_bar, mu, sigma, n):
    '''
    mu            number     mean (population)
    sigma         number     standard deviation (population)
    x_bar         number     sample mean
    n             number     sample size
    '''
    return z_score_formula(mu, standard_error_of_mean(n, sigma), x_bar)

def z_formula_for_sample_means_finite_pop(x_bar, mu, sigma, n, N):
    '''
    mu            number     mean (population)
    sigma         number     standard deviation (population)
    x_bar         number     sample mean
    n             number     sample size
    N             number     population size
    '''
    finite_correction_factor = sqrt((N-n)/(N-1))
    d = standard_error_of_mean(n, sigma) * finite_correction_factor
    return z_score_formula(mu, d, x_bar)

def z_formula_for_sample_proportions(n, p, p_hat):
    '''
    n             number     sample size
    p             number     proportion of population satisfying P(x)
    p_hat         number     proportion of sample satisfying P(x)
    '''
    if z_sample_proportion_checker(n, p):
        return z_score_formula(p, standard_error_proportion(n, p), p_hat)
    else:
        print("precondition failed: (p * n) > 5 and (q * n) > 5")

def z_sample_proportion_checker(n, p):
    '''
    checks if this binomial distribution can be approximated by a normal distribution
    '''
    q = 1 - p
    return (p * n) > 5 and (q * n) > 5

def standard_error_proportion(n, p):
    '''
    n             number     sample size
    p             number     proportion of population satisfying P(x)
    '''
    q = 1 - p
    return round(sqrt((p * q) / n), 4)


##########SAMPLING DISTRIBUTIONS##########

def t_score_formula(x_bar, mu, s, n):
    '''
    mu      number     population mean
    x_bar   number     sample mean
    s       number     sample standard deviation
    n       number     sample size
    '''
    return round((x_bar - mu) / (s / sqrt(n)), 4)

def z_score_formula_p_hat(p_hat, p, n):
    '''
    n       number     sample size
    p       number     population proportion
    p_hat   number     sample proportion
    '''
    q = 1 - p
    return round((p_hat - p) / sqrt((p * q) / n), 4)

def confidence_to_alpha(confidence, tails=1):
    '''
    confidence    number    expressed as a percent (not decimal)
    tails         number    how many tails the problem is

    returns alpha 
    '''
    if tails == 1:
        return round(1 - (confidence / 100), 4)
    elif tails == 2:
        return round((1 - (confidence / 100)) / 2, 4)

def confidence_to_z(confidence, tails=1):
    '''
    confidence    number   100 * (1 - alpha / 2)
    area          number   1 - alpha
    tails         number   1:  one tailed <=> alpha = P(z < Z < inf)
                           2:  two tailed <=> alpha = 2 * P(z < Z < inf)
    
    return 1 or 2 tail z-score corresponding to confidence. 1 by default.
    '''
    alpha = confidence_to_alpha(confidence)
    if tails == 1:
        return alpha_to_z(alpha, 1)
    elif tails == 2:
        return alpha_to_z(alpha, 2)
    else:
        print("invalid argument: tails must only be 1 or 2")
    
def alpha_to_z(alpha, tails=1):
    '''
    confidence    number   100 * (1 - (alpha / 2))
    area          number   1 - alpha
    tails         number   1:  one tailed <=> alpha = P(z < Z < inf)
                           2:  two tailed <=> alpha = 2 * P(z < Z < inf)
    
    return abslute value of the 1 or 2 tail z-score corresponding to alpha.
    1-tailed by default.
    '''
    if tails == 1:
        area = 1 - alpha
        return round(scipy.stats.norm.ppf(area), 4)
    elif tails == 2:
        area = 1 - (alpha/2)
        return round(scipy.stats.norm.ppf(area), 4)
    else:
        print("invalid argument: tails must only be 1 or 2")

def confidence_to_t(confidence, n, tails=1):
    '''
    confidence    number   100 * (1 - alpha / 2)
    area          number   1 - alpha
    tails         number   1:  one tailed <=> alpha = P(t < T < inf)
                           2:  two tailed <=> alpha = 2 * P(t < T < inf)
    
    return 1 or 2 tail t-score corresponding to confidence. 1 by default.
    '''
    alpha = confidence_to_alpha(confidence)
    if tails == 1:
        return alpha_to_t(alpha, n-1, 1)
    elif tails == 2:
        return alpha_to_t(alpha, n-1, 2)
    else:
        print("invalid argument: tails must only be 1 or 2")

def alpha_to_t(alpha, df, tails=1):
    '''
    alpha       number     tail area
    df          number     degrees of freedom
    tails       number     1:  one tailed <=> alpha = P(t < T < inf)
                           2:  two tailed <=> alpha = 2 * P(t < T < inf)
    
    returns t-score corresponding to tail area alpha
    '''
    if tails == 1:
        area = 1 - alpha
        return round(scipy.stats.t.ppf(area, df), 4)
    elif tails == 2:
        area = 1 - (alpha / 2)
        return round(scipy.stats.t.ppf(area, df), 4)
    else:
        print("invalid argument: tails must only be 1 or 2")
