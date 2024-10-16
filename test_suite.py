import stats_module as s    #Sampling Distributions
import stats_module_2 as s2 #Hypthesis Tests & CI's
import stats_module_3 as s3 #ANOVA
import stats_module_4 as s4 #ANOVA

#CHAPTER 9 PART 2:
print("\nCHAPTER 9 PART 2:\n")

#9.5
print("\n9.5\n")
x_bar = 432.69
mu = 424.2
sigma = 33.9
n = 54
alpha = .05
z = s.z_formula_for_sample_means(x_bar, mu, sigma, n)
z_c = s.alpha_to_z(alpha, 2)
z_c = s2.test_stat_signer_z_or_t(z_c, "=")
result = s2.HT_checker_z_or_t("test", z, "=", z_c)
print("EXPECTED")
print("z =", 1.84, "z_c =", (-1.96, 1.96))
print("test result:", "Fail to Reject Null Hypothesis")
print("RESULT")
print("z =", z, "z_c =", z_c)
print("test result:", result)

#9.7
print("\n9.7\n")
x_bar = 506.11
mu = 500
sigma = 28.03
n = 42
N = 650
alpha = .1
z = s.z_formula_for_sample_means_finite_pop(x_bar, mu, sigma, n, N)
z_c = s.alpha_to_z(alpha, 2)
z_c = s2.test_stat_signer_z_or_t(z_c, "=")
result = s2.HT_checker_z_or_t("test", z, "=", z_c)
print("EXPECTED")
print("z =", 1.46, "z_c =", (-1.645, 1.65))
print("test result:", "Fail to Reject Null Hypothesis")
print("RESULT")
print("z =", z, "z_c =", z_c)
print("test result:", result)


#9.9
print("\n9.9\n")
x_bar = 43.4
mu = 41
sigma = 8.95
n = 97
alpha = .1
z = s.z_formula_for_sample_means(x_bar, mu, sigma, n)
p_value = s.p_value_from_z_score_one_sided(z)
result = s2.HT_checker_z_or_t("p", p_value, "<", alpha)
print("EXPECTED")
print("z =", 2.64, "p-value =", .0041)
print("test result:", "Reject Null Hypothesis")
print("RESULT")
print("z =", z, "p-value =", p_value)
print("test result:", result)


#CHAPTER 9 PART 3:
print("\nCHAPTER 9 PART 3:\n")

#9.11
print("\n9.11\n")
x_bar = 16.45
mu = 16
sd = 3.59
n = 20
alpha = .05
df = n - 1
t = s.t_score_formula(x_bar, mu, sd, n)
t_c = s.alpha_to_t(alpha, df, 2)
t_c = s2.test_stat_signer_z_or_t(t_c, "=")
result = s2.HT_checker_z_or_t("test", t, "=", t_c)
print("EXPECTED")
print("t =", .56, "t_c =", (-2.093, 2.093))
print("test result:", "Fail to Reject Null Hypothesis")
print("RESULT")
print("t =", t, "t_c =", t_c)
print("test result:", result)


#9.13
print("\n9.13\n")
data_ungrouped = [1200, 1175 , 1080, 1275, 1201, 1387, 1090, 1280, 1400, 1287, 1225]
x_bar = s.mean_ungrouped(data_ungrouped)
mu = 1160
sd = s.standard_deviation_ungrouped_sample(data_ungrouped)
n = len(data_ungrouped)
alpha = .05
df = n - 1
t = s.t_score_formula(x_bar, mu, sd, n)
t_c = s.alpha_to_t(alpha, df, 1)
t_c = s2.test_stat_signer_z_or_t(t_c, ">")
result = s2.HT_checker_z_or_t("test", t, ">", t_c)
print("EXPECTED")
print("x-bar =", 1235.36, "s=", 103.81, "t =", 2.44, "t_c =", 1.812)
print("test result:", "Reject Null Hypothesis")
print("RESULT")
print("x-bar =", x_bar, "s=", sd, "t =", t, "t_c =", t_c)
print("test result:", result)

#9.15
print("\n9.15\n")
data_ungrouped = [1.81, 1.89, 1.86, 1.83, 1.85, 1.82, 1.87, 1.85, 1.84, 1.86, 1.88, 1.85]
x_bar = s.mean_ungrouped(data_ungrouped)
mu = 1.84
sd = s.standard_deviation_ungrouped_sample(data_ungrouped)
n = len(data_ungrouped)
alpha = .1
df = n - 1
t = s.t_score_formula(x_bar, mu, sd, n)
t_c = s.alpha_to_t(alpha, df, 2)
t_c = s2.test_stat_signer_z_or_t(t_c, "=")
result = s2.HT_checker_z_or_t("test", t, "=", t_c)
print("EXPECTED")
print("x-bar =", 1.85083, "s=", .02353, "t =", 1.59, "t_c =", 1.796) #why isn't t_c expected value (+/-1.796)? It's a 2 sided test. So why is only the positive side considered
print("test result:", "Fail to Reject Null Hypothesis")
print("RESULT")
print("x-bar =", x_bar, "s=", sd, "t =", t, "t_c =", t_c)
print("test result:", result)


#9.17
print("\n9.17\n")
x_bar = 340.89
mu = 347.46
sd = 13.89
n = 49
alpha = .05
df = n - 1
t = s.t_score_formula(x_bar, mu, sd, n)
t_c = s.alpha_to_t(alpha, df, 2)
t_c = s2.test_stat_signer_z_or_t(t_c, "=")
result = s2.HT_checker_z_or_t("test", t, "=", t_c)
print("EXPECTED")
print("t =", -3.31, "t_c =", (-2.009, 2.009))
print("test result:", "Reject Null Hypothesis")
print("RESULT")
print("t =", t, "t_c =", t_c)
print("test result:", result)

#9.19
print("\n9.19\n")
data_ungrouped = [1008, 812, 1117, 1323, 1308, 1415, 831, 1021, 1287, 851, 930, 730, 699, 872, 913, 944, 954, 987, 1695, 995, 1003, 994]
x_bar = s.mean_ungrouped(data_ungrouped)
mu = 1135
sd = s.standard_deviation_ungrouped_sample(data_ungrouped)
n = len(data_ungrouped)
alpha = .05
df = n - 1
t = s.t_score_formula(x_bar, mu, sd, n)
t_c = s.alpha_to_t(alpha, df, 2)
t_c = s2.test_stat_signer_z_or_t(t_c, "=")
result = s2.HT_checker_z_or_t("test", t, "=", t_c)
print("EXPECTED")
print("x-bar =", 1031.32, "s=", 240.37, "t =", -2.02, "t_c =", (-2.08, 2.08))
print("test result:", "Fail to Reject Null Hypothesis")
print("RESULT")
print("x-bar =", x_bar, "s=", sd, "t =", t, "t_c =", t_c)
print("test result:", result)

#CHAPTER 9 PART 4:
print("\nCHAPTER 9 PART 4:\n")

#9.23
print("\n9.23\n")
p = .63
n = 100
p_hat = round(55 / n, 4)
alpha = .01
z = s.z_score_formula_p_hat(p_hat, p, n)
z_c = s.alpha_to_z(alpha, 1)
z_c = s2.test_stat_signer_z_or_t(z_c, "<")
result = s2.HT_checker_z_or_t("test", z, "<", z_c)
print("EXPECTED")
print("p_hat=", .55, "z =", -1.66, "z_c =", -2.33)
print("test result:", "Fail to Reject Null Hypothesis")
print("RESULT")
print("p_hat=", p_hat, "z =", z, "z_c =", z_c)
print("test result:", result)

#9.25
print("\n9.25\n")
p = .48
n = 380
p_hat =  round(164/ n, 4)
alpha = .01
z = s.z_score_formula_p_hat(p_hat, p, n)
z_c = s.alpha_to_z(alpha, 2)
z_c = s2.test_stat_signer_z_or_t(z_c, "=")
result = s2.HT_checker_z_or_t("test", z, "=", z_c)
print("EXPECTED")
print("p_hat=", .4316, "z =", -1.89, "z_c =", (-2.575, 2.575))
print("test result:", "Fail to Reject Null Hypothesis")
print("RESULT")
print("p_hat=", p_hat, "z =", z, "z_c =", z_c)
print("test result:", result)


#9.27
print("\n9.27\n")
p = .31
n = 600
p_hat =  round(200/ 600, 4)
alpha = .1
z = s.z_score_formula_p_hat(p_hat, p, n)
z_c = s.alpha_to_z(alpha, 2)
z_c = s2.test_stat_signer_z_or_t(z_c, "=")
result = s2.HT_checker_z_or_t("test", z, "=", z_c)
print("EXPECTED")
print("p_hat=", .3333, "z =", 1.23, "z_c =", (-1.645, 1.645))
print("test result:", "Fail to Reject Null Hypothesis")
print("RESULT")
print("p_hat=", p_hat, "z =", z, "z_c =", z_c)
print("test result:", result)

p = .24
p_hat =  round(158/ 600, 4)
alpha = .05
z = s.z_score_formula_p_hat(p_hat, p, n)
z_c = s.alpha_to_z(alpha, 1)
z_c = s2.test_stat_signer_z_or_t(z_c, "<")
result = s2.HT_checker_z_or_t("test", z, "<", z_c)
print("EXPECTED")
print("p_hat=", .2633, "z =", 1.34, "z_c =", -1.645)
print("test result:", "Fail to Reject Null Hypothesis")
print("RESULT")
print("p_hat=", p_hat, "z =", z, "z_c =", z_c)
print("test result:", result)

#9.29
print("\n9.29\n")
p = .32
n = 118
p_hat =  round(22/ 118, 4)
alpha = .05
z = s.z_score_formula_p_hat(p_hat, p, n)
z_c = s.alpha_to_z(alpha, 1)
z_c = s2.test_stat_signer_z_or_t(z_c, "<")
result = s2.HT_checker_z_or_t("test", z, "<", z_c)
print("EXPECTED")
print("p_hat=", .1864, "z =", -3.11, "z_c =", -1.645)
print("test result:", "Reject Null Hypothesis")
print("RESULT")
print("p_hat=", p_hat, "z =", z, "z_c =", z_c)
print("test result:", result)

#CHAPTER 9 PART 5:
print("\nCHAPTER 9 PART 5:\n")

###FIGURE OUT HOW TO MAKE s2.alpha_to_X_2(alpha, df) WORK!!!

#9.31
print("\n9.31 a)\n")
alpha = .05
n = 15
s_2 = 32
sigma_2 = 20
df = n - 1
X_2 = s2.X_2_test_statistic_formula(s_2, sigma_2, n)
X_2_c = s2.alpha_to_X_2(alpha, df, ">")
result = s2.HT_checker_X_2(X_2, ">", X_2_c)
print("EXPECTED")
print("X_2=", 22.4, "X_2_c =", 23.6848)
print("test result:", "Fail to Reject Null Hypothesis")
print("RESULT")
print("X_2=", X_2, "X_2_c =", X_2_c)
print("test result:", result)

print("\n9.31 b)\n")
alpha = .1
n = 22
s_2 = 17
sigma_2 = 8.5
df = n - 1
X_2 = s2.X_2_test_statistic_formula(s_2, sigma_2, n)
X_2_c = s2.alpha_to_X_2(alpha, df, "=")
result = s2.HT_checker_X_2(X_2, "=", X_2_c)
print("EXPECTED")
print("X_2=", 42, "X_2_c =", (11.59132, 32.6706))
print("test result:", "Reject Null Hypothesis")
print("RESULT")
print("X_2=", X_2, "X_2_c =", X_2_c)
print("test result:", result)

print("\n9.31 c)\n")
alpha = .01
n = 8
s_2 = 4.12
sigma_2 = 45
df = n - 1
X_2 = s2.X_2_test_statistic_formula(s_2, sigma_2, n)
X_2_c = s2.alpha_to_X_2(alpha, df, "<")
result = s2.HT_checker_X_2(X_2, "<", X_2_c)
print("EXPECTED")
print("X_2=", .64, "X_2_c =", 1.23903)
print("test result:", "Reject Null Hypothesis")
print("RESULT")
print("X_2=", X_2, "X_2_c =", X_2_c)
print("test result:", result)

print("\n9.31 d)\n")
alpha = .05
n = 11
s_2 = 1.2
sigma_2 = 5
df = n - 1
X_2 = s2.X_2_test_statistic_formula(s_2, sigma_2, n)
X_2_c = s2.alpha_to_X_2(alpha, df, "=")
result = s2.HT_checker_X_2(X_2, "=", X_2_c)
print("EXPECTED")
print("X_2=", 2.4, "X_2_c =", (20.4832, 3.24696))
print("test result:", "Reject Null Hypothesis")
print("RESULT")
print("X_2=", X_2, "X_2_c =", X_2_c)
print("test result:", result)

#9.33
print("\n9.33\n")

data_ungrouped = s.split_n_columns_to_list("1.69	1.62	1.63	1.70 \
1.66	1.63	1.65	1.71 \
1.64	1.69	1.57	1.64 \
1.59	1.66	1.63	1.65", 1)
data_ungrouped = data_ungrouped[0]
s_2 = s.variance_ungrouped_sample(data_ungrouped)
n = len(data_ungrouped)
alpha = .01
df = n - 1
sigma_2 = 0.001
X_2 = s2.X_2_test_statistic_formula(s_2, sigma_2, n)
X_2_c = s2.alpha_to_X_2(alpha, df, ">")
result = s2.HT_checker_X_2(X_2, ">", X_2_c)
print("EXPECTED")
print("s_2 =", .00144667, "X_2=", 21.7, "X_2_c =", 30.5780)
print("test result:", "Fail to Reject Null Hypothesis")
print("RESULT")
print("s_2 =", s_2, "X_2=", X_2, "X_2_c =", X_2_c)
print("test result:", result)

#9.35
print("\n9.35\n")
alpha = .01
n = 7
s_2 = .34 ** 2
sigma_2 = .04
df = n - 1
X_2 = s2.X_2_test_statistic_formula(s_2, sigma_2, n)
X_2_c = s2.alpha_to_X_2(alpha, df, ">")
result = s2.HT_checker_X_2(X_2, ">", X_2_c)
print("EXPECTED")
print("X_2=", 17.34, "X_2_c =", 16.8119)
print("test result:", "Reject Null Hypothesis")
print("RESULT")
print("X_2=", X_2, "X_2_c =", X_2_c)
print("test result:", result)



#CHAPTER 10 PART 1:
print("\nCHAPTER 10 PART 1:\n")

#10.1
print("\n10.1 a)\n")
x_bar_1 = 51.3
x_bar_2 = 53.2
mu_1 = 0
mu_2 = 0
sigma_2_1 = 52
sigma_2_2 = 60
n_1 = 31
n_2 = 32
alpha = .1
z = s2.z_HT_stat_mu_1_minus_mu_2(sigma_2_1, sigma_2_2, n_1, n_2, x_bar_1, x_bar_2, mu_1, mu_2)
z_c = s.alpha_to_z(alpha, 1)
z_c = s2.test_stat_signer_z_or_t(z_c, "<")
result = s2.HT_checker_z_or_t("test", z, "<", z_c) 
print("EXPECTED")
print("z =", -1.01, "z_c =", -1.28)
print("test result:", "Fail to Reject Null Hypothesis")
print("RESULT")
print("z =", z, "z_c =", z_c)
print("test result:", result)

print("\n10.1 b)\n")
result = s2.z_crit_value_method_mu_1_minus_mu_2(sigma_2_1, sigma_2_2, n_1, n_2,  mu_1, mu_2, z_c)
print("EXPECTED")
print("The critical difference in the mean values required to Reject the Null Hypothesis is:", -2.41)
print("RESULT")
print("The critical difference in the mean values required to Reject the Null Hypothesis is:", result)

print("\n10.1 c)\n")
p_value = s.p_value_from_z_score_one_sided(z)
print("EXPECTED")
print("p-value =", .1562)
print("RESULT")
print("p-value =", p_value)

#10.5
print("\n10.5\n")
x_bar_1 = 5.3
x_bar_2 = 6.5
mu_1 = 0
mu_2 = 0
sigma_2_1 = 1.99
sigma_2_2 = 2.36
n_1 = 40
n_2 = 37
alpha = .05
ci = s2.z_CI_mu_1_minus_mu_2(sigma_2_1, sigma_2_2, n_1, n_2, x_bar_1, x_bar_2, mu_1, mu_2, alpha)
print("EXPECTED")
print("ci =", (-1.86, -.54))
print("RESULT")
print("ci =", s2.ci_form_change(ci))

#10.7
print("\n10.7\n")
x_bar_1 = 190
x_bar_2 = 198
mu_1 = 0
mu_2 = 0
sigma_2_1 = 18.5 ** 2
sigma_2_2 = 15.6 ** 2
n_1 = 51
n_2 = 47
alpha = .01
z = s2.z_HT_stat_mu_1_minus_mu_2(sigma_2_1, sigma_2_2, n_1, n_2, x_bar_1, x_bar_2, mu_1, mu_2)
z_c = s.alpha_to_z(alpha, 1)
z_c = s2.test_stat_signer_z_or_t(z_c, "<")
result = s2.HT_checker_z_or_t("test", z, "<", z_c) 
print("EXPECTED")
print("z =", -2.32, "z_c =", -2.33)
print("test result:", "Fail to Reject Null Hypothesis")
print("RESULT")
print("z =", z, "z_c =", z_c)
print("test result:", result)


#10.9
print("\n10.9\n")
x_bar_1 = 5.8
x_bar_2 = 5
mu_1 = 0
mu_2 = 0
sigma_2_1 = 1.7 ** 2
sigma_2_2 = 1.4 ** 2
n_1 = 36
n_2 = 45
alpha = .05
z = s2.z_HT_stat_mu_1_minus_mu_2(sigma_2_1, sigma_2_2, n_1, n_2, x_bar_1, x_bar_2, mu_1, mu_2)
z_c = s.alpha_to_z(alpha, 2)
z_c = s2.test_stat_signer_z_or_t(z_c, "=")
result = s2.HT_checker_z_or_t("test", z, "=", z_c) 
print("EXPECTED")
print("z =", 2.27, "z_c =", (-1.96, 1.96))
print("test result:", "Reject Null Hypothesis")
print("RESULT")
print("z =", z, "z_c =", z_c)
print("test result:", result)


#CHAPTER 10 PART 2:
print("\nCHAPTER 10 PART 2:\n")

#10.11
print("\n10.11\n")
x_bar_1 = 24.56
x_bar_2 = 26.42
mu_1 = 0
mu_2 = 0
s_2_1 = 12.4
s_2_2 = 15.8
n_1 = 8
n_2 = 11
alpha = .01
variance_equality = True
t = s2.t_HT_stat_mu_1_minus_mu_2(s_2_1, s_2_2, n_1, n_2, x_bar_1, x_bar_2, mu_1, mu_2, variance_equality)
df = s2.t_HT_df_mu_1_minus_mu_2(s_2_1, s_2_2, n_1, n_2, x_bar_1, x_bar_2, mu_1, mu_2, variance_equality)
t_c = s.alpha_to_t(alpha, df, 1)
t_c = s2.test_stat_signer_z_or_t(t_c, "<")
result = s2.HT_checker_z_or_t("test", t, "<", t_c) 
print("EXPECTED")
print("t =", -1.05, "t_c =", -2.567)
print("test result:", "Fail to Reject Null Hypothesis")
print("RESULT")
print("t =", t, "t_c =", t_c)
print("test result:", result)

#10.15
print("\n10.15\n")
x_bar_1 = 252000
x_bar_2 = 243000
mu_1 = 0
mu_2 = 0
s_2_1 = 4900 ** 2
s_2_2 = 3700 ** 2
n_1 = 21
n_2 = 26
alpha = .1
variance_equality = False
ci = s2.t_CI_mu_1_minus_mu_2(s_2_1, s_2_2, n_1, n_2, x_bar_1, x_bar_2, mu_1, mu_2, alpha)
print("EXPECTED")
print("ci =", (6892.78, 11107.22))
print("RESULT")
print("ci =", s2.ci_form_change(ci))

10.17
print("\n10.17\n")
x_bar_1 = 47
x_bar_2 = 44
mu_1 = 0
mu_2 = 0
s_2_1 = 3 ** 2
s_2_2 = 3 ** 2
n_1 = 8
n_2 = 9
alpha = .05
variance_equality = True
t = s2.t_HT_stat_mu_1_minus_mu_2(s_2_1, s_2_2, n_1, n_2, x_bar_1, x_bar_2, mu_1, mu_2, variance_equality)
df = s2.t_HT_df_mu_1_minus_mu_2(s_2_1, s_2_2, n_1, n_2, x_bar_1, x_bar_2, mu_1, mu_2, variance_equality)
t_c = s.alpha_to_t(alpha, df, 1)
t_c = s2.test_stat_signer_z_or_t(t_c, ">")
result = s2.HT_checker_z_or_t("test", t, ">", t_c) 
print("EXPECTED")
print("t =", 2.06, "t_c =", 1.753)
print("test result:", "Reject Null Hypothesis")
print("RESULT")
print("t =", t, "t_c =", t_c)
print("test result:", result)

#10.19
print("\n10.19\n")
x_bar_1 = 67381.82
x_bar_2 = 63390.91
mu_1 = 0
mu_2 = 0
s_2_1 = 2067.28 ** 2
s_2_2 = 1526.08 ** 2
n_1 = 11
n_2 = 11
alpha = .01
variance_equality = True
t = s2.t_HT_stat_mu_1_minus_mu_2(s_2_1, s_2_2, n_1, n_2, x_bar_1, x_bar_2, mu_1, mu_2, variance_equality)
df = s2.t_HT_df_mu_1_minus_mu_2(s_2_1, s_2_2, n_1, n_2, x_bar_1, x_bar_2, mu_1, mu_2, variance_equality)
t_c = s.alpha_to_t(alpha, df, 2)
t_c = s2.test_stat_signer_z_or_t(t_c, "=")
result = s2.HT_checker_z_or_t("test", t, "=", t_c) 
print("EXPECTED")
print("t =",5.15, "t_c =", (-2.845, 2.845))
print("test result:", "Reject Null Hypothesis")
print("RESULT")
print("t =", t, "t_c =", t_c)
print("test result:", result)

#CHAPTER 10 PART 3:
print("\nCHAPTER 10 PART 3:\n")

#10.21
print("\n10.21\n")
data = s.split_n_columns_to_list("38 22 16 \
 27 28 -1 \
 30 21 9 \
 41 38 3 \
 36 38 -2 \
 38 26 12 \
 33 19 14 \
 35 31 4  \
 44 35 9", 3)
variable_1 = data[0]
variable_2 = data[1]
D = 0
n = len(variable_1)
alpha = .01
df = n - 1
d_bar = s2.get_d_bar(variable_1, variable_2)
s_d = s2.get_s_d(variable_1, variable_2)
t = s2.t_HT_stat_D(d_bar, s_d, D, n)
t_c = s.alpha_to_t(alpha, df, 1)
t_c = s2.test_stat_signer_z_or_t(t_c, ">")
result = s2.HT_checker_z_or_t("test", t, ">", t_c)
print("EXPECTED")
print("s_d =", 6.45, "d_bar =", 7.11, "t =", 3.31, "t_c =", 2.896)
print("test result:", "Reject Null Hypothesis")
print("RESULT")
print("s_d =", s_d, "d_bar =", d_bar,"t =", t, "t_c =", t_c)
print("test result:", result)

#10.23
print("\n10.23\n")
d_bar = 40.56
s_d = 26.58
n = 22
D = 0
alpha = s.confidence_to_alpha(98, 2) #because ci's are all 2-tailed
ci = s2.t_CI_D(d_bar, s_d, D, n, alpha)
print("EXPECTED")
print("ci =", (26.29, 54.83))
print("RESULT")
print("ci =", s2.ci_form_change(ci))

#10.25
print("\n10.25\n")
data = s.split_n_columns_to_list("20427   25163 \
	 27255	 24625 \
	 22115	 12600 \
         23256	 24588 \
	 21887	 19267 \
	 24255	 20150 \
         19852	 22500 \
         23624	 16667 \
	 25885	 26875 \
	 28999	 35333 \
	 20836	 16292", 2)
variable_1 = data[0]
variable_2 = data[1]
d_bar = s2.get_d_bar(variable_1, variable_2)
s_d = s2.get_s_d(variable_1, variable_2)
n = 11
D = 0
alpha = s.confidence_to_alpha(99, 2) #because ci's are all 2-tailed
ci = s2.t_CI_D(d_bar, s_d, D, n, alpha)
print("EXPECTED")
print("ci =", (-3415.6, 6021.2))
print("RESULT")
print("ci =", s2.ci_form_change(ci))

#10.27
print("\n10.27\n")
data = s.split_n_columns_to_list(" 1	6.59	5.09 \
 2	5.95	5.82 \
 3	7.50	5.56 \
 4	6.26	5.56 \
 5	7.76	6.21 \
 6	6.46	6.08 \
 7	5.56	4.91 \
 8	5.95	6.21 \
 9	5.82	5.17 \
10	5.66	5.25 \
11	6.10	5.77", 3)
variable_1 = data[1]
variable_2 = data[2]
d_bar = s2.get_d_bar(variable_1, variable_2)
s_d = s2.get_s_d(variable_1, variable_2)
n = 11
D = 0
alpha = s.confidence_to_alpha(98, 2) #because ci's are all 2-tailed
ci = s2.t_CI_D(d_bar, s_d, D, n, alpha)
print("EXPECTED")
print("ci =", (.1685, 1.2825))
print("RESULT")
print("ci =", s2.ci_form_change(ci))

#10.29
print("\n10.29\n")
n = 21
d_bar = 75
s_d = 30
D = 0
alpha = s.confidence_to_alpha(90, 2) #because ci's are all 2-tailed
ci = s2.t_CI_D(d_bar, s_d, D, n, alpha)
print("EXPECTED")
print("ci =", (63.71, 86.29))
print("RESULT")
print("ci =", s2.ci_form_change(ci))

#CHAPTER 10 PART 4:
print("\nCHAPTER 10 PART 4:\n")

#10.31
print("\n10.31 a)\n")
p_1_minus_p_2 = 0
n_1 = 368
n_2 = 405
p_hat_1 = round(175 / n_1, 3)
p_hat_2 = round(182 / n_2, 3)
alpha = .05
z = s2.z_HT_stat_p_1_minus_p_2_ps_unknown(p_hat_1, p_hat_2, n_1, n_2, p_1_minus_p_2)
z_c = s.alpha_to_z(alpha, 2)
z_c = s2.test_stat_signer_z_or_t(z_c, "=")
result = s2.HT_checker_z_or_t("test", z, "=", z_c) 
print("EXPECTED")
print("z =", .75, "z_c =", (-1.96, 1.96))
print("test result:", "Fail Reject Null Hypothesis")
print("RESULT")
print("z =", z, "z_c =", z_c)
print("test result:", result)

#10.31
print("\n10.31 b)\n")
p_1_minus_p_2 = 0
n_1 = 649
n_2 = 558
p_hat_1 = .38
p_hat_2 = .25
alpha = .1
z = s2.z_HT_stat_p_1_minus_p_2_ps_unknown(p_hat_1, p_hat_2, n_1, n_2, p_1_minus_p_2)
z_c = s.alpha_to_z(alpha, 1)
z_c = s2.test_stat_signer_z_or_t(z_c, ">")
result = s2.HT_checker_z_or_t("test", z, ">", z_c) 
print("EXPECTED")
print("z =", 4.83, "z_c =", 1.28)
print("test result:", "Reject Null Hypothesis")
print("RESULT")
print("z =", z, "z_c =", z_c)
print("test result:", result)

#10.33
print("\n10.33\n")
p_1_minus_p_2 = 0
n_1 = 374
n_2 = 481
p_hat_1 = .59
p_hat_2 = .7
alpha = .05
z = s2.z_HT_stat_p_1_minus_p_2_ps_unknown(p_hat_1, p_hat_2, n_1, n_2, p_1_minus_p_2)
z_c = s.alpha_to_z(alpha, 1)
z_c = s2.test_stat_signer_z_or_t(z_c, "<")
result = s2.HT_checker_z_or_t("test", z, "<", z_c) 
print("EXPECTED")
print("z =", -3.35, "z_c =", -1.645)
print("test result:", "Reject Null Hypothesis")
print("RESULT")
print("z =", z, "z_c =", z_c)
print("test result:", result)

#10.35
print("\n10.35\n")
p_1_minus_p_2 = 0
n_1 = 56
n_2 = 87
p_hat_1 = .48
p_hat_2 = .56
alpha = .2
z = s2.z_HT_stat_p_1_minus_p_2_ps_unknown(p_hat_1, p_hat_2, n_1, n_2, p_1_minus_p_2)
z_c = s.alpha_to_z(alpha, 2)
z_c = s2.test_stat_signer_z_or_t(z_c, "=")
result = s2.HT_checker_z_or_t("test", z, "=", z_c) 
print("EXPECTED")
print("z =", -.94, "z_c =", (-1.28, 1.28))
print("test result:", "Fail to Reject Null Hypothesis")
print("RESULT")
print("z =", z, "z_c =", z_c)
print("test result:", result)

#10.37
print("\n10.37\n")
p_1_minus_p_2 = 0
n_1 = 780
n_2 = 915
p_hat_1 = .09
p_hat_2 = .06
alpha = .1
z = s2.z_HT_stat_p_1_minus_p_2_ps_unknown(p_hat_1, p_hat_2, n_1, n_2, p_1_minus_p_2)
z_c = s.alpha_to_z(alpha, 2)
z_c = s2.test_stat_signer_z_or_t(z_c, "=")
result = s2.HT_checker_z_or_t("test", z, "=", z_c) 
print("EXPECTED")
print("z =", 2.35, "z_c =", (-1.645, 1.645))
print("test result:", "Reject Null Hypothesis")
print("RESULT")
print("z =", z, "z_c =", z_c)
print("test result:", result)

#CHAPTER 10 PART 5:
print("\nCHAPTER 10 PART 5:\n")

#10.41
print("\n10.41\n")
data = s.split_n_columns_to_list("1.338	1.295	1.318	1.299	1.287	1.342 \
1.326	1.322	1.318	1.334	1.349	1.314 \
1.322	1.318	1.278	1.322	1.322	1.318 \
1.303	 NA	 NA	1.310	NA	NA", 6)
variable_1 = []
variable_2 = []
variable_1.extend(data[0])
variable_1.extend(data[1])
variable_1.extend(data[2])
variable_2.extend(data[3])
variable_2.extend(data[4])
variable_2.extend(data[5])
alpha = .01
s_2_1 = s.variance_ungrouped_sample(variable_1)
s_2_2 = s.variance_ungrouped_sample(variable_2)
n_1 = len(variable_1)
n_2 = len(variable_2)
v_1 = n_1 - 1
v_2 = n_2 - 1
F = s2.F_HT_stat_sigma_2_i_ratio(s_2_1, s_2_2)
F_c = s2.f_dist.get_f(alpha, v_1, v_2, "both")
result = s4.HT_checker(F, "=", F_c)
print("EXPECTED")
print("F =", .8362, "F_c =", (.153, 6.54))
print("test result:", "Fail to Reject Null Hypothesis")
print("RESULT")
print("F =", F, "F_c =", F_c)
print("test result:", result)

#10.43
print("\n10.43\n")
alpha = .05
s_2_1 = 7.52 ** 2
s_2_2 = 6.08 ** 2
n_1 = 12
n_2 = 15
v_1 = n_1 - 1
v_2 = n_2 - 1
F = s2.F_HT_stat_sigma_2_i_ratio(s_2_1, s_2_2)
F_c = s2.f_dist.get_f(alpha, v_1, v_2, "upper") #upper b/c it's greater than
result = s4.HT_checker(F, ">", F_c)
print("EXPECTED")
print("F =", 1.53, "F_c =", 2.565)
print("test result:", "Fail to Reject Null Hypothesis")
print("RESULT")
print("F =", F, "F_c =", F_c)
print("test result:", result)
