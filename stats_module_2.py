import stats_module as s
import q_dist
import f_dist
import scipy

##########SINGLE POPULATION INFERENCES - CONFIDENCE INTERVALS##########

def ci_form_change(ci):
    '''
    ci    (point estimate, margin of error)

    returns (CI lower bound, CI upper bound)
    '''
    ci_ub = round(ci[0] + ci[1], 4)
    ci_lb = round(ci[0] - ci[1], 4)
    return (ci_lb , ci_ub)

def z_CI_for_mu(confidence, x_bar, sigma, n, N=None):
    '''
    confidence   number     100 * (1 - alpha)
    x_bar        number     sample mean
    sigma        number     population standard deviation
    n            number     sample size
    N            number     population size (optional)

    returns (point estimate, margin of error)
    '''
    z = confidence_to_z(confidence, 1)
    moe = z * (sigma / sqrt(n))
    if (N != None) and (z_CI_for_mu_checker(n, N)):
        correction_factor = sqrt((N - n)/(N - 1))
        moe = moe * correction_factor
    return (round(x_bar, 4), round(moe, 4))

def z_CI_for_mu_checker(n, N):
    '''
    n            number     sample size
    N            number     population size (optional)
    '''
    return n > .05 * N

def t_CI_for_mu(confidence, x_bar, s, n):
    '''
    confidence   number     100 * (1 - alpha)
    x_bar        number     sample mean
    s            number     sample standard deviation
    n            number     sample size
    
    returns (point estimate, margin of error)
    '''
    t = round(confidence_to_t(confidence, n, 1), 4)
    moe = round(t * (s / sqrt(n)), 4)
    return (x_bar, moe)

def z_CI_for_p(confidence, p_hat, n):
    '''
    confidence  number     100 * (1 - alpha)
    n           number     sample size
    p_hat       number     sample proportion
    
    returns (point estimate, margin of error)
    '''
    z = confidence_to_z(confidence, 1)
    q_hat = 1 - p_hat
    moe = z * sqrt((p_hat * q_hat)/n)
    return (p_hat, moe)

def X_2_CI_for_sigma_2(confidence, s_2, n):
    '''
    confidence  number     100 * (1 - alpha)
    n           number     sample size
    s_2         number     sample variance <=> s**2

    for chi square:
    df = 0        <=> highest positive skew
    increasing df <=> decreases positive skew
    
    returns (CI lower bound, CI upper bound)
    
    DOES NOT HAVE A POINT-ESTIMATE FORM!
    '''
    alpha = confidence_to_alpha(confidence) / 2
    ci_lb = ((n-1) * s_2) / alpha_to_X(1 - alpha, n-1)
    ci_ub = ((n-1) * s_2) / alpha_to_X(alpha, n-1)
    return (round(ci_lb, 4), round(ci_ub, 4))

def n_for_est_mu(confidence, E, sigma="range", rang=None):
    '''
    confidence  number     100 * (1 - alpha
    sigma       number     standard deviation
                string     switch indicating that range / 4 will approximate sigma
    rang        number     range <=> max - min
    E           number     margin of error of estimation <=> x_bar - mu <=> CI width

    return optimal sample size to estimate population mean of a
    single population
    '''
    z = confidence_to_z(confidence)
    if sigma == "range":
        sigma = rang / 4
    return round(pow((z * sigma) / E, 2), 4)

def n_for_est_p(confidence, E, p=.5):
    '''
    confidence  number     100 * (1 - alpha
    p           number     population proportion
    E           number     margin of error of estimation <=> p_hat - p <=> CI width

    p = .5 <=> max(p * q) for p, q in rational numbers
    therefore, p = .5 is the most conservative estimate, If it holds, all
    different values of p will hold.

    return optimal sample size to estimate population proportion of a
    single population
    '''
    z = confidence_to_z(confidence)
    z = round(z, 4)
    q = 1 - p
    return round((z**2 * p * q) / E**2, 4)

##########SINGLE POPULATION INFERENCES - HYPOTHESIS TESTS##########

def test_stat_signer_z_or_t(test_c, inequality):
    '''
    test_c     Number     Critical Test Statistic (Test Statistic from
                          alpha)
    inequality String     "=" <=> H_a: actual/parameter = estimation/value
                          "<" <=> H_a: actual/parameter < estimation/value
                          ">" <=> H_a: actual/parameter > estimation/value
    
    determines the appropriate sign for the critical test statistic
    based on inequality and test_type
    '''
    if inequality == "<":
        return abs(test_c) * -1
    elif inequality == "=":
        return (-abs(test_c), abs(test_c))
    return abs(test_c)
        
def HT_checker_z_or_t(switch, actual, inequality, expected):
    '''
    switch     String     if "p" than expected = alpha and actual = p-value
                          if "test" than expected = test_c and actual = test
    inequality String     "=" <=> H_a: actual/parameter = estimation/value
                          "<" <=> H_a: actual/parameter < estimation/value
                          ">" <=> H_a: actual/parameter > estimation/value
    alpha      Number     Significance Level
    p-value    Number     the p-value of the test statistic (the probability
                          the result occured assuming the Null Hypothesis is
                          True
    test       Number     hypothesis Test Statistic
    test_c     Number     Critical Test Statistic (Test Statistic of
                          alpha)
 
    returns a String indicating whether the Null Hypothesis was rejected
    '''
    if switch == "p":
        alpha = expected
        p_value = actual
        if (inequality == ">") or (inequality == "<"):
            return HT_result_interpreter(alpha > p_value)
        elif inequality == "=":
            return HT_result_interpreter(alpha/2 > p_value)
        else:
            print("Error: value of test_type must be one of '=', '>', or '<'")
    elif switch == "test":
        test_c = expected
        test = actual
        if inequality == ">":
            return HT_result_interpreter(test > test_c)
        elif inequality == "<":
            return HT_result_interpreter(test < test_c)
        elif inequality == "=":
            return HT_result_interpreter((test < test_c[0]) or (test > test_c[1]))
        else:
            print("Error: value of inequality must be one of '=', '>', or '<'")
    else:
        print("Error: value of switch must be one of 'p' or 'test'")

def HT_result_interpreter(result):
    '''
    result     Boolean    True if Null Hypothesis was rejected, False otherwise
    '''
    if result:
        return "Reject Null Hypothesis"
    elif not result:
        return "Fail to Reject Null Hypothesis"
    else:
        print("Error: result must be Boolean")

def X_2_test_statistic_formula(s_2, sigma_2, n):
    '''
    s_2       number     sample variance
    sigma_2   number     population variance (hypothesized)
    n         number     sample size
    
    returns test statistic for use in a chi-square test to hypothesize the
    population variance
    '''
    return round(((n - 1) * s_2) / sigma_2, 4)

def alpha_to_X_2(alpha, df, inequality):
    '''
    alpha       number     tail area (of upper tail)
    df          number     degrees of freedom
    inequality  String     "=" <=> H_a: actual/parameter = estimation/value
                           "<" <=> H_a: actual/parameter < estimation/value
                           ">" <=> H_a: actual/parameter > estimation/value
    X_2         Tuple      if test is two-sided, (X_2 lower bound, X_2 upper bound)
                Number     if test is one-sided
    
    returns X_2 (chi-square-score) corresponding tail area alpha.
    '''
    if inequality == "=":
        u_b_a = alpha / 2
        l_b_a = 1 - u_b_a
        u_b = scipy.stats.chi2.ppf(u_b_a, df)
        l_b = scipy.stats.chi2.ppf(l_b_a, df)
        return (round(u_b, 4), round(l_b, 4))
    elif inequality == "<":
        return round(scipy.stats.chi2.ppf(alpha, df), 4)
    elif inequality == ">":
        return round(scipy.stats.chi2.ppf(1 - alpha, df), 4)
    else:
        print("Error: value of test_type must be one of '=', '>', or '<'")

def HT_checker_X_2(X_2, inequality, X_2_c):
    '''
    inequality String     "=" <=> H_a: actual/parameter = estimation/value
                          "<" <=> H_a: actual/parameter < estimation/value
                          ">" <=> H_a: actual/parameter > estimation/value
    X_2        Tuple      if test is two-sided,(X_2 lower bound, X_2 upper bound)
               Number     if test is one-sided
    X_2_c      Number     Critical Test Statistic(s). Test Statistic of
                          alpha for chi-scquared test)
 
    returns a String indicating whether the Null Hypothesis was rejected
    '''
    if inequality == "=":
        return HT_result_interpreter(X_2 < X_2_c[1] or X_2_c[0] < X_2)
    elif inequality == "<":
        return HT_result_interpreter(X_2 < X_2_c)
    elif inequality == ">":
        return HT_result_interpreter(X_2 > X_2_c)
    else:
        print("Error: value of inequality must be one of '=', '>', or '<'")


##########DOUBLE POPULATION INFERENCES - HYPOTHESIS TESTS##########

def get_s_p(s_2_1, s_2_2, n_1, n_2):
    '''
    sigma_2_i            Number     population variance for population i
    n_i                  Number     sample size for population i
    
    returns pooled sample standard deviation (s_p) of the two independant populations,
    which estimates the difference in population standard deviation, in order to
    perform a t HT to find mu_1 - mu_2
    '''
    s_p = s.sqrt(((s_2_1 * (n_1 - 1)) + (s_2_2 * (n_2 - 1))) / (n_1 + n_2 - 2))
    return round(s_p, 4)

def z_HT_stat_mu_1_minus_mu_2(sigma_2_1, sigma_2_2, n_1, n_2, x_bar_1, x_bar_2, mu_1, mu_2):
    '''
    sigma_2_i            Number     population variance for population i
    n_i                  Number     sample size for population i
    x_bar_i              Number     sample mean for population i
    mu_i                 Number     (hypothesized) population mean for population i
    
    returns test statistic for use in a hypothesis test to hypothesize the difference of
    population mean for two indepedant samples (with known population variances)
    '''
    sigma_x_bar_diff = s.sqrt((sigma_2_1 / n_1) + (sigma_2_2 / n_2))
    z = ((x_bar_1 - x_bar_2) - (mu_1 - mu_2)) / sigma_x_bar_diff
    return round(z, 4)

def z_crit_value_method_mu_1_minus_mu_2(sigma_2_1, sigma_2_2, n_1, n_2,  mu_1, mu_2, z_c):
    '''
    sigma_2_i            Number     population variance for population i
    n_i                  Number     sample size for population i
    mu_i                 Number     (hypothesized) population mean for population i
    z_c                  Number     critical z value
    
    returns the value of (x_bar_1 minus x_bar_2) which would be required to attain a critical
    z score of z_critical and therefore reject the null hypothesis at the significance level
    corresponding to z criticals corresponding alpha
    '''
    sigma_x_bar_diff = s.sqrt((sigma_2_1 / n_1) + (sigma_2_2 / n_2))
    x_bar_diff = (z_c * sigma_x_bar_diff) - (mu_1 - mu_2)
    return round(x_bar_diff, 4)

def t_HT_stat_mu_1_minus_mu_2_pooled(s_2_1, s_2_2, n_1, n_2, x_bar_1, x_bar_2, mu_1, mu_2):
    '''
    s_2_i               Number     sample variance for population i
    n_i                 Number     sample size for population i
    x_bar_i             Number     sample mean for population i
    mu_i                Number     (hypothesized) population mean for population i   

    returns test statistic for use in a hypothesis test to hypothesize the difference of
    population mean for two indepedant samples (with unknown population variances known to be
    similiar)
    '''
    s_p = get_s_p(s_2_1, s_2_2, n_1, n_2)
    t = ((x_bar_1 - x_bar_2) - (mu_1 - mu_2)) / (s_p * s.sqrt((1 / n_1) + (1 / n_2)))
    return round(t, 4)

def t_HT_stat_mu_1_minus_mu_2_unpooled(s_2_1, s_2_2, n_1, n_2, x_bar_1, x_bar_2, mu_1, mu_2):
    '''
    s_2_i               Number     sample variance for population i
    n_i                 Number     sample size for population i
    x_bar_i             Number     sample mean for population i
    mu_i                Number     (hypothesized) population mean for population i   

    returns test statistic for use in a hypothesis test to hypothesize the difference of
    population mean for two indepedant samples (with unknown population variances known to be
    dissimiliar)
    '''
    t = ((x_bar_1 - x_bar_2) - (mu_1 - mu_2)) / (s.sqrt(s_2_1 / n_1 + s_2_2 / n_2))
    return round(t, 4)

def t_HT_stat_D(d_bar, s_d, D, n):
    '''
    d_bar    Number    mean_sample_difference
    s_d      Number    standard deviation of sample difference
    D        Number    mean population difference (hypothesized)
                       for 2 samples from dependant populations
    n        Number    sample size

    return test statistic for use in a hypothesis test to hypothesize
    the difference of population means for two depedant samples (with
    unknown population variances)(for a matched pairs experimental design)
    '''
    t = (d_bar - D) / (s_d / s.sqrt(n))
    return round(t, 4)

def get_differences(variable_1, variable_2):
    '''
    variable_1    List of value
    variable_2    List of value
    value         Number          A value the variable takes on
    
    returns a list of the differences between values taken on by variable_1
    and variable_2 (for a matched pairs experimental design)
    '''
    differences = []
    n = len(variable_1)
    for i in range(n):
        differences.append(variable_1[i] - variable_2[i])
    return differences

def get_d_bar(variable_1, variable_2):
    '''
    variable_1    List of value
    variable_2    List of value
    value         Number          A value the variable takes on
    
    returns mean sample difference between values taken on by variable_1 and
    variable_2
    '''
    differences = []
    n = len(variable_1)
    differences = get_differences(variable_1, variable_2)
    return round(s.mean_ungrouped(differences), 4)

def get_s_d(variable_1, variable_2):
    '''
    variable_1    List of value
    variable_2    List of value
    value         Number          A value the variable takes on

    PRECONDITION: len(variable_1) == len(variable_2)
    
    returns standard deviation of sample difference between values taken on by
    variable_1 and variable_2
    '''
    d_bar = get_d_bar(variable_1, variable_2)
    s_d = 0
    n = len(variable_1)
    differences = get_differences(variable_1, variable_2)
    for i in range(n):
        s_d += ((differences[i] - d_bar) ** 2)
    return round(s.sqrt(s_d / (n - 1)), 4)

def z_HT_stat_p_1_minus_p_2_ps_known(p_hat_1, p_hat_2, n_1, n_2, p_1, p_2):
    '''
    p_hat_i        Number     sample proportion for population i
    p_i            Number     (hypothesized) population proportions
    n_i            Number     sample size for population i
    
    returns test statistic for use in a hypothesis test to hypothesize the difference of
    population proportions for two indepedant populations if population proportions are known
    '''
    if z_HT_stat_p_1_minus_p_2_checker(p_hat_1, p_hat_2, n_1, n_2):
        q_1 = 1 - p_1
        q_2 = 1 - p_2
        sigma_p_hat_diff = s.sqrt(((p_1 * q_1) / n_1) + ((p_2 * q_2) / n_2))  
        z = ((p_hat_1 - p_hat_2) - (p_1 - p_2)) / sigma_p_hat_diff
        return round(z, 4)
    else:
        print("Error: One of (n_1 * p_hat_1 > 5) and (n_1 * q_hat_1 > 5) and (n_2 * p_hat_2 > 5) and (n_2 * q_hat_2 > 5) violated")

def z_HT_stat_p_1_minus_p_2_ps_unknown(p_hat_1, p_hat_2, n_1, n_2, p_1_minus_p_2):
    '''
    p_hat_i        Number     sample proportion for population i
    p_1_minus_p2   Number     (hypothesized) difference in population proportions
                              for both populations
    n_i            Number     sample size for population i
    
    returns test statistic for use in a hypothesis test to hypothesize the difference of
    population proportions for two indepedant populations if population proportions aren't
    known (only their difference)
    '''
    if z_HT_stat_p_1_minus_p_2_checker(p_hat_1, p_hat_2, n_1, n_2):
        p_bar = ((n_1 * p_hat_1) + (n_2 * p_hat_2)) / (n_1 + n_2)
        q_bar = 1 - p_bar
        sigma_p_hat_diff_est = s.sqrt(p_bar * q_bar * ((1 / n_1) + (1 / n_2)))
        z = (p_hat_1 - p_hat_2 - p_1_minus_p_2) / sigma_p_hat_diff_est
        return round(z, 4)
    else:
        print("Error: One of (n_1 * p_hat_1 > 5) and (n_1 * q_hat_1 > 5) and (n_2 * p_hat_2 > 5) and (n_2 * q_hat_2 > 5) violated")

def z_HT_stat_p_1_minus_p_2_checker(p_hat_1, p_hat_2, n_1, n_2):
    '''
    p_hat_i        Number     sample proportion for population i
    n_i            Number     sample size for population i
    
    returns True if data is sufficient to perform a hypothesis test to hypothesize the
    difference of population proportions for two indepedant populations
    '''
    q_hat_1 = 1 - p_hat_1
    q_hat_2 = 1 - p_hat_2
    return (n_1 * p_hat_1 > 5) and (n_1 * q_hat_1 > 5) and (n_2 * p_hat_2 > 5) and (n_2 * q_hat_2 > 5)

def F_HT_stat_sigma_2_i_ratio(s_2_1, s_2_2):
    '''
    s_2_i               Number     sample variance for population i

    return the test statistic for a hypothesis test to hypothesize  the ratio of the
    population variances for two indepedant populations
    '''
    F = s_2_1 / s_2_2
    return round(F, 6)


##########DOUBLE POPULATION INFERENCES - CONFIDENCE INTERVALS##########

def z_CI_mu_1_minus_mu_2(sigma_2_1, sigma_2_2, n_1, n_2, x_bar_1, x_bar_2, mu_1, mu_2, alpha):
    '''
    sigma_2_i   Number     population variance for population i
    n_i         Number     sample size for population i
    x_bar_i     Number     sample mean for population i
    mu_i        Number     (hypothesized) population mean for population i
    alpha       Number     Significance Level
    
    returns confidence interval to predict the difference of population means
    for two indepedant samples (with known population variances) at Significance
    Level alpha

    ci form: (point estimate, margin of error)
    '''
    pe = (x_bar_1 - x_bar_2)
    z_a = s.alpha_to_z(alpha, 2)
    sigma_x_bar_diff = s.sqrt((sigma_2_1 / n_1) + (sigma_2_2 / n_2))
    me = z_a * sigma_x_bar_diff
    return (round(pe, 4), round(me, 4))

def t_CI_mu_1_minus_mu_2_pooled(s_2_1, s_2_2, n_1, n_2, x_bar_1, x_bar_2, mu_1, mu_2, alpha):
    '''
    s_2_i       Number     population variance for population i
    n_i         Number     sample size for population i
    x_bar_i     Number     sample mean for population i
    mu_i        Number     (hypothesized) population mean for population i
    alpha       Number     Significance Level
    
    returns confidence interval to predict the difference of population means
    for two indepedant samples (with unknown population variances known to be
    similiar) at Significance Level alpha

    ci form: (point estimate, margin of error)
    '''
    pe = (x_bar_1 - x_bar_2)
    df = n_1 + n_2 - 2
    t_a = s.alpha_to_t(alpha, df, 2)
    s_p = get_s_p(s_2_1, s_2_2, n_1, n_2)
    me = t_a * s_p * s.sqrt((1 / n_1) + (1 / n_2))
    return (round(pe, 4), round(me, 4))

def t_CI_mu_1_minus_mu_2_unpooled(s_2_1, s_2_2, n_1, n_2, x_bar_1, x_bar_2, mu_1, mu_2, alpha):
    '''
    s_2_i       Number     population variance for population i
    n_i         Number     sample size for population i
    x_bar_i     Number     sample mean for population i
    mu_i        Number     (hypothesized) population mean for population i
    alpha       Number     Significance Level
    
    returns confidence interval to predict the difference of population means
    for two indepedant samples (with unknown population variances known to be
    dissimiliar) at Significance Level alpha

    ci form: (point estimate, margin of error)
    '''
    pe = (x_bar_1 - x_bar_2)
    df = get_df_for_t_unpooled(s_2_1, s_2_2, n_1, n_2, x_bar_1, x_bar_2, mu_1, mu_2, alpha)
    t_a = s.alpha_to_t(alpha, df, 2)
    me = t_a * s.sqrt((s_2_1 / n_1) + (s_2_2 / n_2))
    return (round(pe, 4), round(me, 4))

def get_df_for_t_unpooled(s_2_1, s_2_2, n_1, n_2, x_bar_1, x_bar_2, mu_1, mu_2, alpha):
    '''
    s_2_i       Number     population variance for population i
    n_i         Number     sample size for population i
    x_bar_i     Number     sample mean for population i
    mu_i        Number     (hypothesized) population mean for population i
    alpha       Number     Significance Level
    
    returns df for use in hypothesis tests or confidence intervals hyothesizing/estimating
    the difference of population means for two indepedant samples (with unknown population
    variances known to be dissimiliar) at Significance Level alpha
    '''
    df = (((s_2_1 / n_1) + (s_2_2 / n_2)) ** 2) / ((((s_2_1 / n_1) ** 2) / (n_1 - 1)) + (((s_2_2 / n_2) ** 2) / (n_2 - 1)))
    return s.floor(df)

def t_CI_D(d_bar, s_d, D, n, alpha):
    '''
    d_bar    Number    mean_sample_difference
    s_d      Number    standard deviation of sample difference
    D        Number    mean population difference (hypothesized)
                       for 2 samples from dependant populations
    n        Number    sample size
    alpha    Number    significance level

    returns confidence interval to predict the difference of population means
    for two depedant samples (with unknown population variances) at Significance
    Level alpha

    ci form: (point estimate, margin of error)
    '''
    df = n - 1
    t_a = s.alpha_to_t(alpha / 2, df)
    pe = d_bar
    me = t_a * (s_d / s.sqrt(n))
    return (round(pe, 4), round(me, 4))

def z_CI_p_1_minus_p_2(p_hat_1, p_hat_2, n_1, n_2, p_1_minus_p_2, alpha):
    '''
    p_hat_i        Number     sample proportion for population i
    p_1_minus_p2   Number     (hypothesized) difference in population proportions
                              for both populations
    n_i            Number     sample size for population i
    
    returns confidence interval for use in estimating the difference of population
    proportions for two indepedant populations if population proportions aren't
    known (only their difference)

    ci form: (point estimate, margin of error)
    '''
    if z_HT_stat_p_1_minus_p_2_checker(p_hat_1, p_hat_2, n_1, n_2):
        q_hat_1 = 1 - p_hat_1
        q_hat_2 = 1 - p_hat_2
        z_a = s.alpha_to_z(alpha / 2)
        pe = p_hat_1 - p_hat_2
        me = z_a * s.sqrt(((p_hat_1 * q_hat_1) / n_1) + ((p_hat_2 * q_hat_2) / n_2))
        return (round(pe, 4), round(me, 4))
    else:
        print("Error: One of (n_1 * p_hat_1 > 5) and (n_1 * q_hat_1 > 5) and (n_2 * p_hat_2 > 5) and (n_2 * q_hat_2 > 5) violated")

   

##########POSSIBLY DEPRECIATED##########

def z_crit_value_method_mu_1_minus_mu_2(sigma_2_1, sigma_2_2, n_1, n_2,  mu_1, mu_2, z_c):
    '''
    sigma_2_i            Number     population variance for population i
    n_i                  Number     sample size for population i
    mu_i                 Number     (hypothesized) population mean for population i
    z_c                  Number     critical z value
    
    returns the value of (x_bar_1 minus x_bar_2) which would be required to attain a critical
    z score of z_critical and therefore reject the null hypothesis at the significance level
    corresponding to z criticals corresponding alpha
    '''
    sigma_x_bar_diff = s.sqrt((sigma_2_1 / n_1) + (sigma_2_2 / n_2))
    x_bar_diff = (z_c * sigma_x_bar_diff) - (mu_1 - mu_2)
    return round(x_bar_diff, 4)

def t_HT_stat_mu_1_minus_mu_2(s_2_1, s_2_2, n_1, n_2, x_bar_1, x_bar_2, mu_1, mu_2, variance_equality):
    '''
    s_2_i               Number     sample variance for population i
    n_i                 Number     sample size for population i
    x_bar_i             Number     sample mean for population i
    mu_i                Number     (hypothesized) population mean for population i
    variance_equality   Boolean    True if population variances are known to be equivolant,
                                   False otherwise     

    returns test statistic for use in a hypothesis test to hypothesize the difference of
    population mean for two indepedant samples (with unknown population variances)
    '''
    CF = 1
    s_p = get_s_p(s_2_1, s_2_2, n_1, n_2)
    if variance_equality:
        CF = s.sqrt((1 / n_1) + (1 / n_2))
    t = ((x_bar_1 - x_bar_2) - (mu_1 - mu_2)) / (s_p * CF)
    return round(t, 4)

def t_HT_df_mu_1_minus_mu_2(s_2_1, s_2_2, n_1, n_2, x_bar_1, x_bar_2, mu_1, mu_2, variance_equality):
    '''
    s_2_i               Number     sample variance for population i
    n_i                 Number     sample size for population i
    x_bar_i             Number     sample mean for population i
    mu_i                Number     (hypothesized) population mean for population i

    variance_equality   Boolean    True if population variances are known to be equivolant,
                                   False otherwise     

    return the degree of freedom to calculate critical t value for use in a hypothesis test
    to hypothesize the difference of population means for two indepedant samples (with unknown
    population variances)
    '''
    if variance_equality:
        return n_1 + n_2 - 2
    else:
        s_x_bar_diff = s.sqrt((s_2_1 / n_1) + (s_2_2 / n_2))
        df = (s_x_bar_diff ** 4) / ((((s_2_1 / n_1) ** 2) / n_1 - 1) + (((s_2_2 / n_2) ** 2) / n_2 - 1))
        return round(df, 4)

def t_CI_mu_1_minus_mu_2(s_2_1, s_2_2, n_1, n_2, x_bar_1, x_bar_2, mu_1, mu_2, alpha):
    '''
    s_2_i       Number     population variance for population i
    n_i         Number     sample size for population i
    x_bar_i     Number     sample mean for population i
    mu_i        Number     (hypothesized) population mean for population i
    alpha       Number     Significance Level
    
    returns confidence interval to predict the difference of population means
    for two indepedant samples (with unknown population variances) at Significance
    Level alpha

    ci form: (point estimate, margin of error)
    '''
    pe = (x_bar_1 - x_bar_2)
    df = n_1 + n_2 - 2
    t_a = s.alpha_to_t(alpha, df, 2)
    s_p = get_s_p(s_2_1, s_2_2, n_1, n_2)
    me = t_a * s_p * s.sqrt((1 / n_1) + (1 / n_2))
    return (round(pe, 4), round(me, 4))
