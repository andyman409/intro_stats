import stats_module as s
import stats_module_2 as s2
import q_dist
import f_dist
import scipy

##########ONE WAY ANOVA##########

def one_way_ANOVA_crd(treatment):
    '''
    treatment           list of treatment_levels (Columns)
    treatment_level     list of member
    member              number

    returns the f value for a completely randomized experimental design
    '''
    msc = msc_formula(treatment)
    mse = mse_formula_crd(treatment)
    return round(msc / mse, 6)

def ssc_formula(treatment):
    '''
    treatment           list of treatment_levels (Columns)
    treatment_level     list of member
    member              number

    returns the sum of squares of columns for any experimental design
    '''
    ssc = 0
    grand_mean = find_grand_mean(treatment)
    for treatment_level in treatment:
        n = len(treatment_level)
        column_mean = s.mean_ungrouped(treatment_level)
        ssc += (n * ((column_mean - grand_mean) ** 2))
    return round(ssc, 6)

def sse_formula_crd(treatment):
    '''
    treatment           list of treatment_levels (Columns)
    treatment_level     list of member
    member              number

    returns the sum of squares of the error for a completely randomized
    experimental design
    '''
    sse = 0
    C = find_C(treatment)
    for treatment_level in treatment:
        column_mean = s.mean_ungrouped(treatment_level)
        result = 0
        for member in treatment_level:
            result += (member - column_mean) ** 2
        sse += result
    return round(sse, 6)

def msc_formula(treatment):
    '''
    treatment           list of treatment_levels (Columns)
    treatment_level     list of member
    member              number

    returns the column mean square for any experimental design
    '''
    C = find_C(treatment)
    ssc = ssc_formula(treatment)
    dfc = C - 1
    return round(ssc / dfc, 6)

def mse_formula_crd(treatment):
    '''
    treatment           list of treatment_levels (Columns)
    treatment_level     list of member
    member              number

    returns the mean squared error for a completely randomized experimental
    design
    '''
    N = find_N(treatment)
    C = find_C(treatment)
    sse = sse_formula_crd(treatment)
    dfe = N - C
    return round(sse / dfe, 6)
    
def find_C(treatment):
    '''
    treatment           list of treatment_levels (Columns)
    treatment_level     list of member
    member              number

    returns the number of treatment levels/columns
    '''
    return len(treatment)
    
def find_N(treatment):
    '''
    treatment           list of treatment_levels (Columns)
    treatment_level     list of member
    member              number

    returns the total number of members accross all treatment levels
    '''
    counter = 0
    for treatment_level in treatment:
        counter += len(treatment_level)
    return counter

def find_grand_mean(treatment):
    '''
    treatments    list of treatment (Columns)
    treatment     list of member
    member        number

    returns mean of all the members
    '''
    means = []
    for treatment_level in treatment:
         means.append(s.mean_ungrouped(treatment_level))
    return round(s.mean_ungrouped(means), 6)


##########MULTIPLE COMPARISON TESTS##########


def tukey_hsd_test(mse, alpha, C, N, n, x_bar_r, x_bar_s):
    '''
    mse      mean of squares of error terms
    alpha    significance level
    C        number of treatments/columns
    N        total number of members
    n        sample size
    x_bar_r  mean of group one being compared
    x_bar_s  mean of group two being compared

    PRECONDITION: length of both groups is equal
    
    Returns True if the difference between the means of the two groups is significant
    under alpha
    '''
    dfc = C
    dfe = N - C
    q = q_dist.get_q(alpha, dfc, dfe)
    hsd = hsd_formula(mse, n, q)
    return abs(x_bar_r - x_bar_s) > hsd
    
    
def tukey_kramer_procedure(mse, alpha, C, N, n_r, n_s, x_bar_r, x_bar_s):
    '''
    mse      mean of squares of error terms
    alpha    significance level
    C        number of treatments/columns
    N        total number of members
    n_r      sample size of sample r
    n_s      sample size of sample s
    x_bar_r  mean of sample r being compared
    x_bar_s  mean of sample s being compared

    PRECONDITION: length of both groups is not equal
    
    Returns True if the difference between the means of the two groups is
    significant under alpha
    '''
    dfe = N - C
    q = q_dist.get_q(alpha, C, dfe)
    hsd = hsd_formula_modified(mse, n_r, n_s, q)
    return abs(x_bar_r - x_bar_s) > hsd

def tukey_tests_interpreter(result):
    """
    result    Boolean    True difference between the means of the two groups is
                         significant under alpha (via one of the tukey tests)
    
    returns String indicating result of a tukey test
    """
    if result:
        return "Significant Difference"
    else:
        return "No Significant Difference"

def hsd_formula(mse, n, q):
    '''
    mse      mean of squares of error terms
    n        sample size
    q        studentized q score

    PRECONDITION: length of both groups is equal
    
    Returns HSD
    '''
    return round(q * s.sqrt(mse / n), 6)

def hsd_formula_modified(mse, n_r, n_s, q):
    '''
    mse      mean of squares of error terms
    n_r      sample size of sample r
    n_s      sample size of sample s
    q        studentized q score

    PRECONDITION: length of both groups is not equal
    
    Returns HSD
    '''
    return round(q * s.sqrt((mse / 2) * (1/n_r + 1/n_s)), 6)


##########RANDOMIZED BLOCK DESIGN##########

def one_way_ANOVA_rbd(treatment):
    '''
    treatment           list of treatment_level (Columns)
    treatment_level     list of member
    member              number

    PRECONDITION: treatment_levels are equal length

    returns (f value for treatments, f value for error) for a randomized block
    experimental design
    '''
    msc = msc_formula(treatment)
    mse = mse_formula_rbd(treatment)
    msr = msr_formula_rbd(treatment)
    f_treatments = msc / mse
    f_blocks = msr / mse
    return (round(f_treatments, 6), round(f_blocks, 6))

def ssr_formula_rbd(treatment):
    '''
    treatment           list of treatment_level (Columns)
    treatment_level     list of member
    member              number

    PRECONDITION: treatment_levels are equal length

    returns the sum of squares of rows for randomized block experimental
    design
    '''
    grand_mean = find_grand_mean(treatment)
    ssr = 0
    C = find_C(treatment)
    n = len(treatment[0])
    for i in range(n):
        row_mean = find_row_mean(treatment, i)
        ssr += (row_mean - grand_mean) ** 2
    return round(C * ssr, 6)

def msr_formula_rbd(treatment):
    '''
    treatment           list of treatment_level (Columns)
    treatment_level     list of member
    member              number

    PRECONDITION: treatment_levels are equal length

    returns the row mean squared for randomized block experimental
    design
    '''
    n = len(treatment[0])
    ssr = ssr_formula_rbd(treatment)
    dfr = n-1
    msr = ssr / dfr
    return round(msr, 6)

def sse_formula_rbd(treatment):
    '''
    treatment           list of treatment_levels (Columns)
    treatment_level     list of member
    member              number

    returns the sum of squares of the error for a randomized block
    experimental design
    '''
    sse = 0
    C = find_C(treatment)
    n = len(treatment[0])
    grand_mean = find_grand_mean(treatment)
    row_means = []
    column_means = []
    for i in range(n):
        row_means.append(find_row_mean(treatment, i))
    for treatment_level in treatment:
        column_means.append(s.mean_ungrouped(treatment_level))
    for i in range(n):
        for j in range(C):
            sse += (treatment[j][i] - row_means[i] - column_means[j] + grand_mean) ** 2
    return round(sse, 6)

def mse_formula_rbd(treatment):
    '''
    treatment           list of treatment_levels (Columns)
    treatment_level     list of member
    member              number

    PRECONDITION: treatment_levels are equal length

    returns the mean squared error for a randomized block experimental
    design
    '''
    N = find_N(treatment)
    n = len(treatment[0])
    C = find_C(treatment)
    sse = sse_formula_rbd(treatment)
    dfe = N - n - C + 1
    return round(sse / dfe, 6)

def find_row_mean(treatment, i):
    '''
    treatment           list of treatment_level (Columns)
    treatment_level     list of member
    member              number
    i                   specified row

    return row mean of row i of the dataset (treatment)
    '''
    row_members = []
    for treatment_level in treatment:
        row_members.append(treatment_level[i])
    return round(s.mean_ungrouped(row_members), 6)


##########SIMPLE REGRESSION ANALYSIS##########

def pearson_product_moment_correlation_coefficient(x_variables, y_variables):
    '''
    x_variables    list of number
    y_variables    list of number

    PRECONDITION: len(x_variables) == len(y_variables)

    return pearson product moment-correlation coefficient <=> r
    '''
    r = 0
    num = 0
    den1 = 0
    den2 = 0
    x_mean = s.mean_ungrouped(x_variables)
    y_mean = s.mean_ungrouped(y_variables)
    n = len(x_variables)
    for i in range(n):
        num += ((x_variables[i] - x_mean) * (y_variables[i] - y_mean))
        den1 += (x_variables[i] - x_mean) ** 2
        den2 += (y_variables[i] - y_mean) ** 2
    return round(num / s.sqrt(den1 * den2), 6)

def least_squares_regression_line(x_variables, y_variables):
    '''
    x_variables    list of number
    y_variables    list of number

    Precondition: len(x_variables) == len(y_variables)

    return (y_intercept, slope) for least square regression line
    '''
    slope = lsrl_slope(x_variables, y_variables)
    y_intercept = lsrl_y_intercept(x_variables, y_variables)
    return (round(y_intercept, 6), round(slope, 6))

def lsrl_slope(x_variables, y_variables):
    '''
    x_variables    list of number
    y_variables    list of number

    Precondition: len(x_variables) == len(y_variables)

    return the slope for least square regression line
    '''
    ss_xy = find_ss_xy(x_variables, y_variables)
    ss_xx = find_ss_xx(x_variables)
    return round(ss_xy / ss_xx, 6)

def lsrl_y_intercept(x_variables, y_variables):
    '''
    x_variables    list of number
    y_variables    list of number

    Precondition: len(x_variables) == len(y_variables)

    return the y-intercept for least square regression line
    '''
    sigma_x = sigma(x_variables)
    sigma_y = sigma(y_variables)
    n = len(x_variables)
    slope = lsrl_slope(x_variables, y_variables)
    return round((sigma_y / n) - (slope * (sigma_x / n)), 6)

def find_ss_xx(x_variables):
    '''
    x_variables    list of number

    return sum of squares of x <=> the denominator of the slope of the
    least squares regression line <=> ss_xx
    '''
    n = len(x_variables)
    sigma_x = sigma(x_variables)
    sigma_x2 = sigma_squared(x_variables)
    return round(sigma_x2 - ((sigma_x ** 2) / n), 6)

def find_ss_xy(x_variables, y_variables):
    '''
    x_variables    list of number
    y_variables    list of number

    returns the numerator for the slope of the least squares regression
    line <=> ss_xy
    '''
    n = len(x_variables)
    sigma_x = sigma(x_variables)
    sigma_y = sigma(y_variables)
    sigma_xy = sigma_product(x_variables, y_variables)
    return round(sigma_xy - ((sigma_x * sigma_y) / n), 6)

def find_ss_yy(y_variables):
    '''
    y_variables    list of number

    return sum of squares of y <=> ss_yy
    '''
    n = len(x_variables)
    sigma_y = sigma(y_variables)
    sigma_y2 = sigma_squared(y_variables)
    return sigma_y2 - ((sigma_y ** 2) / n)

def sigma(variables):
    '''
    variables    list of number

    return sum of all variables <=> sigma(x_i)
    '''
    return sum(variables)

def sigma_squared(variables):
    '''
    variables    list of number

    return sum of all squared variables <=> sigma(x_i^2)
    '''
    squared = 0
    n = len(variables)
    for i in range(n):
        squared += variables[i] ** 2
    return squared

def sigma_product(variables_1, variables_2):
    '''
    variables_1    list of number
    variables_2    list of number

    return product of each variable pair <=> sigma(x_i*y_i)
    '''
    product = 0
    n = len(variables_1)
    for i in range(n):
        product += (variables_1[i] * variables_2[i])
    return product

def standard_error_of_the_estimate(x_variables, y_variables):
    '''
    y_variables    list of number

    return the standard error of the estimate of y <=> s_e
    '''
    sse = sse_formula_regression(x_variables, y_variables)
    n = len(y_variables)
    return round(s.sqrt(sse / (n - 2)), 6)

def find_residuals(x_variables, y_variables):
    '''
    x_variables    list of number
    y_variables    list of number

    Precondition: len(x_variables) == len(y_variables)

    returns a list of the residuals of x and y
    '''
    residuals = []
    n = len(x_variables)
    y = 0
    y_hat = 0
    for i in range(n):
        y = y_variables[i]
        b_0 = lsrl_y_intercept(x_variables, y_variables)
        b_1 = lsrl_slope(x_variables, y_variables)
        x = x_variables[i]
        y_hat = b_0 + (x * b_1)
        residuals.append(y - y_hat)
    return residuals

def coefficient_of_determination(x_variables, y_variables):
    '''
    x_variables    list of number
    y_variables    list of number

    return the coefficient of determination for y <=> r^2
    '''
    sse = sse_formula_regression(x_variables, y_variables)
    ss_yy = find_ss_yy(y_variables)
    return round(1 - (sse / ss_yy), 6)

def sse_formula_regression(x_variables, y_variables):
    '''
    x_variables    list of number
    y_variables    list of number

    Precondition: len(x_variables) == len(y_variables)

    returns the sum of squares error value for use in calculating the standard
    error of the estimate
    '''
    sse = 0
    residuals = find_residuals(x_variables, y_variables)
    for residual in residuals:
        sse += (residual ** 2)
    return round(sse, 6)
        
def t_statistic_for_slope(x_variables, y_variables, beta_1=0):
    '''
    x_variables    list of number
    y_variables    list of number
    b_1            number           sample slope
    beta_1         number           hypothesized slope

    Precondition: len(x_variables) == len(y_variables)

    returns the t statistic to test null hypothesis about the slope
    '''
    n = len(x_variables)
    b_1 = lsrl_slope(x_variables, y_variables)
    sse = sse_formula_regression(x_variables, y_variables)
    s_e = s.sqrt(sse / (n - 2))
    ss_xx = find_ss_xx(x_variables)
    s_b = s_e / s.sqrt(ss_xx)
    return round((b_1 - beta_1) / s_b, 6)

def confidence_interval_estimating_y_given_x(x_variables, y_variables, x_0, alpha, tails=1, P=None):
    '''
    x_variables    list of number
    y_variables    list of number
    alpha          number           significance level
    tails          number           whether the analysis is 1 or 2 tailed. 1 By default
    x_0            number           a given x value
    P              anything         Converts to a Prediction Interval if P != None

    Precondition: len(x_variables) == len(y_variables)
    Precondition: 1 <= tails <= 2

    returns the expected value of y at x_0 at alpha significance level
    '''
    if P == None:
        P = 0
    else:
        P = 1
    b_0 = lsrl_y_intercept(x_variables, y_variables)
    b_1 = lsrl_slope(x_variables, y_variables)
    y_hat = b_0 + (b_1 * x_0)
    n = len(x_variables)
    df = n - 2
    t = s.alpha_to_t(alpha, df, tails)
    s_e = standard_error_of_the_estimate(x_variables, y_variables)
    ss_xx = find_ss_xx(x_variables)
    x_bar = s.mean_ungrouped(x_variables)
    pe = y_hat
    me = t * s_e * s.sqrt(P + (1 / n) + (((x_0 - x_bar) ** 2) / ss_xx))
    return (round(pe, 6), round(me, 6))



