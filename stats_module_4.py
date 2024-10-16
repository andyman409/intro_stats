import stats_module as s
import stats_module_2 as s2
import stats_module_3 as s3
import q_dist
import f_dist
import scipy

##########ONE WAY ANOVA##########

def one_way_ANOVA_crd(msc, mse):
    '''
    mse      mean of squares of columns
    mse      mean of squares of error terms

    returns the f value for a completely randomized experimental design
    '''
    return round(msc / mse, 4)

def ssc_formula(column_means, grand_mean, ns):
    '''
    column_means        list of column_mean
    column mean         number
    ns                  list of column sizes

    PRECONDITION: len(ns) == len(column_means)
    PRECONDITION: if rbd design, then len(ns[i]) == len(ns[j]) for any i, j

    returns the sum of squares of columns for any experimental design
    '''
    ssc = 0
    i = 0
    for i in range(len(column_means)):
        ssc += (ns[i] * ((column_means[i] - grand_mean) ** 2))
    return round(ssc, 6)

def ssr_formula_rbd(row_means, grand_mean, C):
    '''
    column_means        list of column_mean
    column mean         number

    PRECONDITION: len(ns) == len(column_means)

    returns the sum of squares of columns for any experimental design
    '''
    ssr = 0
    i = 0
    for i in range(len(row_means)):
        ssr += ((row_means[i] - grand_mean) ** 2)
    return round(C * ssr, 6)

def sse_formula_using_ANOVA(std_devs, ns):
    sse = 0
    N = len(ns)
    for i in range(N):
        sse += (ns[i] - 1) * (std_devs[i] ** 2)
    return sse

def msc_formula(ssc, dfc):
    '''
    ssc     sum of squares of columns
    dfc     degrees of freedom for columns

    returns the column mean square for any experimental design
    '''
    return round(ssc / dfc, 4)

def mse_formula_crd(sse, dfe):
    '''
    sse     sum of squares of error terms
    dfc     degrees of freedom for error terms

    returns the mean squared error for a completely randomized experimental
    design
    '''
    return round(sse / dfe, 4)

def msr_formula_rbd(ssr, dfr):
    '''
    ssr     sum of squares of blocks
    dfr     degrees of freedom for blocks

    returns the row mean squared for randomized block experimental
    design
    '''
    msr = ssr / dfr
    return round(msr, 6)

def mse_formula_rbd(sse, dfe):
    '''
    sse     sum of squares of error terms
    dfc     degrees of freedom for error terms
    
    returns the mean squared error for a randomized block experimental
    design
    '''
    return round(sse / dfe, 6)

def one_way_ANOVA_rbd(msc, mse, msr):
    '''
    treatment           list of treatment_level (Columns)
    treatment_level     list of member
    member              number

    PRECONDITION: treatment_levels are equal length

    returns (f value for treatments, f value for error) for a randomized block
    experimental design
    '''
    f_treatments = msc / mse
    f_blocks = msr / mse
    return (round(f_treatments, 6), round(f_blocks, 6))

def find_dfc(C):
    return C - 1

def find_dfc_tukey(C):
    return C

def find_dfe_crd(N, C):
    return N - C

def find_dfe_rbd(N, n, C):
    return N - n - C + 1

def find_dfr_rbd(n):
    return n - 1

def find_df_for_CI_for_y(n):
    return n - 2

def HT_checker(actual, inequality, expected):
    '''
    inequality String     "=" <=> H_a: actual/parameter = estimation/value
                          "<" <=> H_a: actual/parameter < estimation/value
                          ">" <=> H_a: actual/parameter > estimation/value
    test       Number     hypothesis Test Statistic
    test_c     Number     Critical Test Statistic (Test Statistic of
                          alpha)
 
    returns a String indicating whether the Null Hypothesis was rejected. Compatible
    with many kinds of hypothesis tests (z, t, F).
    '''
    test_c = expected
    test = actual
    if inequality == ">":
        return s2.HT_result_interpreter(test > test_c)
    elif inequality == "<":
        return s2.HT_result_interpreter(test < test_c)
    elif inequality == "=":
        return s2.HT_result_interpreter((test < test_c[0]) or (test > test_c[1]))
    else:
        print("Error: value of inequality must be one of '=', '>', or '<'")


##########MULTIPLE REGRESSION##########


def CI_estimating_y_given_x_0(lsrl, x_0, x_bar, alpha, s_e, n, ss_xx, P=None):
    '''
    lsrl           tuple of numbers (y_intercept, slope)
    x_0            number           a given x value
    x_bar          number           the overall mean
    alpha          number           significance level
    n              number           sample size
    s_e            number           standard error of the estimate
    ss_xx          number           sum of squares of x
    P              anything         converts to a Prediction Interval if P != None

    returns the expected value of y at x_0 at alpha significance level
    '''
    if P == None:
        P = 0
    else:
        P = 1
    b_0 = lsrl[0]
    b_1 = lsrl[1]
    y_hat = b_0 + (b_1 * x_0)
    df = n - 2
    t_a = s.alpha_to_t(alpha, df, 2)
    pe = y_hat
    me = t_a * s_e * s.sqrt(P + (1 / n) + (((x_0 - x_bar) ** 2) / ss_xx))
    return (round(pe, 6), round(me, 6))


##########CATEGORICAL DATA ANALYSIS##########


def X_2_goodness_of_fit_test(observations, expectations):
    '''
    observations    List of observed frequencies
    expectations    List of expected frequencies
    frequency       Number

    returns test statistic to hypothesize whether (observed) multinomial
    distribution of categorical variable frequencies matches data from an
    (expectated) particular distribution
    '''
    X_2 = 0
    for i in range(len(observations)):
        f_o = observations[i]
        f_e = expectations[i]
        X_2 += ((f_o - f_e) ** 2) / f_e
    return X_2

def get_df_X_2_goodness_of_fit_test(k, distribution="uniform"):
    '''
    k            Number     number of categories
    distribution String     "uniform" (default)
                            "poisson"
                            "normal"
    '''
    if distribution == "uniform":
        c = 0
    elif distribution == "poisson":
        c = 1
    elif distribution == "normal":
        c = 2
    return k - 1 - c

def get_expectations_uniform(observations):
    n = len(observations)
    N = sum(observations)
    expected_value = N / n
    expectations = []
    for i in range(n):
        expectations.append(expected_value)
    return expectations

def get_expectations_proportions(observations, compared_proportions):
    N = sum(observations)
    expectations = []
    for proportion in compared_proportions:
        expectations.append(proportion * N)
    return expectations
    
def X_2_independance_test(contingency_table):
    '''
    contingency_table    List of column
    column               List of frequency
    frequency            Number
    '''
    X_2 = 0
    N = get_N_contingency_table(contingency_table)
    num_cols = get_row_len(contingency_table)
    num_rows = get_col_len(contingency_table)
    expected_freqs = get_expected_freqs(contingency_table)
    expected_freq_rows = expected_freqs[0]
    expected_freq_cols = expected_freqs[1]
    for j in range(num_cols): #j = column
        for i in range(num_rows): #i = row
            f_o = contingency_table[j][i]
            n_i = expected_freq_rows[i]
            n_j = expected_freq_cols[j]
            f_e = expected_freq_value(n_i, n_j, N)
            X_2 += ((f_o - f_e) ** 2) / f_e
    return round(X_2, 4)

def get_N_contingency_table(contingency_table):
    N = 0
    for column in contingency_table:
        N += sum(column)
    return N
    
def get_expected_freqs(contingency_table):
    expected_freq_rows = []
    expected_freq_cols = []
    num_cols = get_row_len(contingency_table)
    num_rows = get_col_len(contingency_table)
    row = []
    for j in range(num_cols):
        expected_freq_cols.append(sum(contingency_table[j]))
    transposed = [list(i) for i in zip(*contingency_table)]
    for i in range(num_rows):
        expected_freq_rows.append(sum(transposed[i]))
    return (expected_freq_rows, expected_freq_cols)

def expected_freq_value(n_i, n_j, N):
    '''
    n_i   Number    total frequency of row i contingency table elements
    n_j   Number    total frequency of column j contingency table elements
    N     Number    total frequency of contingency table elements
    PRECONDITION: the variable in n_row and n_col of the contingency_table
    represents independant variables
    '''
    return round((n_i * n_j) / N, 4)

def get_df_X_2_independance_test(c, r):
    return (c - 1) * (r - 1)

def get_row_len(contingency_table):
    return len(contingency_table)

def get_col_len(contingency_table):
    return len(contingency_table[0])

def how_much_cell_contributes_to_X_2_statistic(contingency_table, row, col):
    '''
    i                    Number                  row index of target cell (minus 1)
    j                    Number                  column index of target cell (minus 1)
    contingency_table    List of List of Number
    '''
    f_o = contingency_table[col][row]
    expected_freqs = get_expected_freqs(contingency_table)
    n_i = expected_freqs[0][row]
    n_j = expected_freqs[1][col]
    N = get_N_contingency_table(contingency_table)
    f_e = expected_freq_value(n_i, n_j, N)
    return ((f_o - f_e) ** 2) / f_e

