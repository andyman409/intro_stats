import stats_module as s    #Sampling Distributions
import stats_module_2 as s2 #Hypthesis Tests & CI's
import stats_module_3 as s3 #ANOVA (arguments are treatments)
import stats_module_4 as s4 #ANOVA (arguments are values)
import plotter as p

#CHAPTER 11 PART 2:
print("\nCHAPTER 11 PART 2:\n")

#11.5
print("\n11.5\n")
treatment = s.split_n_columns_to_list("2	5	3 \
1	3	4 \
3	6	5 \
3	4	5 \
2	5	3 \
1	NA 	5", 3)
C = s3.find_C(treatment)
N = s3.find_N(treatment)
dfc = s4.find_dfc(C)
dfe = s4.find_dfe_crd(N, C)
ssc = s3.ssc_formula(treatment)
sse = s3.sse_formula_crd(treatment)
msc = s3.msc_formula(treatment)
mse = s3.mse_formula_crd(treatment)
f = s3.one_way_ANOVA_crd(treatment)
print("EXPECTED")
print("dfc", 2, "\tssc", 22.2, "\tmsc", 11.1, "\tF", 11.07)
print("dfe", 14, "\tsse", 14.03, "\tmse", 1)
print("RESULT")
print("dfc", dfc, "\tssc", ssc, "\tmsc", msc, "\tF", f)
print("dfe", dfe, "\tsse", sse, "\tmse", mse)

#11.7
print("\n11.7\n")
treatment = s.split_n_columns_to_list("113	120	132	122 \
121	127	130	118 \
117	125	129	125 \
110	129	135	125 \
", 4)
C = s3.find_C(treatment)
N = s3.find_N(treatment)
dfc = s4.find_dfc(C)
dfe = s4.find_dfe_crd(N, C)
ssc = s3.ssc_formula(treatment)
sse = s3.sse_formula_crd(treatment)
msc = s3.msc_formula(treatment)
mse = s3.mse_formula_crd(treatment)
f = s3.one_way_ANOVA_crd(treatment)
print("EXPECTED")
print("dfc", 3, "\tssc", 544.25, "\tmsc", 181.4, "\tF", 13)
print("dfe", 12, "\tsse", 167.5, "\tmse", 14)
print("RESULT")
print("dfc", dfc, "\tssc", ssc, "\tmsc", msc, "\tF", f)
print("dfe", dfe, "\tsse", sse, "\tmse", mse)

#11.9
print("\n11.9\n")
N = 55
C = 5
ssc = 583.39
sse = 972.18
dfc = s4.find_dfc(C)
dfe = s4.find_dfe_crd(N, C)
dft = dfc + dfe
msc = s4.msc_formula(ssc, dfc)
mse = s4.mse_formula_crd(sse, dfe)
f = s4.one_way_ANOVA_crd(msc, mse)
print("EXPECTED")
print("dfc", 4, "\tssc", 583.39, "\tmsc", 145.8475, "\tF", 7.5)
print("dfe", 50, "\tsse", 972.18, "\tmse", 19.4436)
print("RESULT")
print("dfc", dfc, "\tssc", ssc, "\tmsc", msc, "\tF", f)
print("dfe", dfe, "\tsse", sse, "\tmse", mse)


#11.11
print("\n11.11\n")
treatment = s.split_n_columns_to_list("4.05	3.99	3.97	4.00 \
4.01	4.02	3.98	4.02 \
4.02	4.01	3.97	3.99 \
4.04	3.99	3.95	4.01 \
NA	4.00	4.00	NA \
NA	4.00	NA	NA", 4)
alpha = .01
C = s3.find_C(treatment)
N = s3.find_N(treatment)
dfc = s4.find_dfc(C)
dfe = s4.find_dfe_crd(N, C)
ssc = s3.ssc_formula(treatment)
sse = s3.sse_formula_crd(treatment)
msc = s3.msc_formula(treatment)
mse = s3.mse_formula_crd(treatment)
f = s3.one_way_ANOVA_crd(treatment)
v_1 = dfc
v_2 = dfe
f_c = s2.f_dist.get_f(alpha, v_1, v_2, "upper") #Always the case for ANOVA
result = s4.HT_checker(f, ">", f_c) #Always the case for ANOVA
print("EXPECTED")
print("dfc", 3, "\tssc", .007076, "\tmsc", .002359, "\tF", 10.1)
print("dfe", 15, "\tsse", .003503, "\tmse", .000234)
print("test result:", "Reject Null Hypothesis")
print("RESULT")
print("dfc", dfc, "\tssc", ssc, "\tmsc", msc, "\tF", f)
print("dfe", dfe, "\tsse", sse, "\tmse", mse)
print("test result:", result)

#11.13
print("\n11.13\n")
treatment = s.split_n_columns_to_list("7	 8	5 \
7	 9	6 \
8	 8	5 \
7	10	7 \
9	 9	4 \
NA 	10	8 \
NA 	 8	NA ", 3)
alpha = .05
C = s3.find_C(treatment)
N = s3.find_N(treatment)
dfc = s4.find_dfc(C)
dfe = s4.find_dfe_crd(N, C)
ssc = s3.ssc_formula(treatment)
sse = s3.sse_formula_crd(treatment)
msc = s3.msc_formula(treatment)
mse = s3.mse_formula_crd(treatment)
f = s3.one_way_ANOVA_crd(treatment)
v_1 = dfc
v_2 = dfe
f_c = s2.f_dist.get_f(alpha, v_1, v_2, "upper")
result = s4.HT_checker(f, ">", f_c)
print("EXPECTED")
print("dfc", 2, "\tssc", 29.61, "\tmsc", 14.8, "\tF", 11.76)
print("dfe", 15, "\tsse", 18.89, "\tmse", 1.26)
print("test result:", "Reject Null Hypothesis")
print("RESULT")
print("dfc", dfc, "\tssc", ssc, "\tmsc", msc, "\tF", f)
print("dfe", dfe, "\tsse", sse, "\tmse", mse)
print("test result:", result)


#CHAPTER 11 PART 3:
print("\nCHAPTER 11 PART 3:\n")

#11.17
print("\n11.17\n")
mse = .3352
alpha = .05
C = 6
N = 46
n_r = 8
n_s = 7
x_bar_1 = 15.85
x_bar_2 = 17.21
dfc = s4.find_dfc_tukey(C)
dfe = s4.find_dfe_crd(N, C) #same dfe as crd experiments
q = s3.q_dist.get_q(alpha, dfc, dfe)
hsd = s3.hsd_formula_modified(mse, n_r, n_s, q)
result = s3.tukey_kramer_procedure(mse, alpha, C, N, n_r, n_s, x_bar_1, x_bar_2)
result = s3.tukey_tests_interpreter(result)
print("EXPECTED")
print("hsd:", .896, "\tq:", 4.23)
print("test result:", "Significant Difference")
print("RESULT")
print("hsd:", hsd, "\tq:", q)
print("test result:", result)

#11.19
print("\n11.19\n")
treatment = s.split_n_columns_to_list("2	5	3 \
1	3	4 \
3	6	5 \
3	4	5 \
2	5	3 \
1	NA 	5", 3)
mse = s3.mse_formula_crd(treatment)
alpha = .05
C = s3.find_C(treatment)
N = s3.find_N(treatment)
n_r = len(treatment[0])
n_s = len(treatment[1])
x_bar_1 = s.mean_ungrouped(treatment[0])
x_bar_2 = s.mean_ungrouped(treatment[1])
dfc = s4.find_dfc_tukey(C)
dfe = s4.find_dfe_crd(N, C)
q = s3.q_dist.get_q(alpha, dfc, dfe)
hsd = s3.hsd_formula_modified(mse, n_r, n_s, q)
result = s3.tukey_kramer_procedure(mse, alpha, C, N, n_r, n_s, x_bar_1, x_bar_2)
result = s3.tukey_tests_interpreter(result)
print("EXPECTED")
print("mse:", 1.002381, "\tC:", 3, "\tN:", 17, "\tn_1:", 6, "\tn_2:", 5)
print("\tx_bar_1:", 2,"\tx_bar_2:", 4.6, "\thsd:", 1.586, "\tq:", 3.7)
print("test result:", "Significant Difference")

print("RESULT")
print("mse:", mse, "\tC:", C, "\tN:", N, "\tn_1:", n_r, "\tn_2:", n_s)
print("\tx_bar_1:", x_bar_1,"\tx_bar_2:", x_bar_2, "\thsd:", hsd, "\tq:", q)
print("test result:", result)

#11.21
print("\n11.21\n")
treatment = s.split_n_columns_to_list("113	120	132	122 \
121	127	130	118 \
117	125	129	125 \
110	129	135	125 \
", 4)
mse = s3.mse_formula_crd(treatment)
alpha = .01
C = s3.find_C(treatment)
N = s3.find_N(treatment)
n = len(treatment[0])
x_bar_1 = s.mean_ungrouped(treatment[0])
x_bar_2 = s.mean_ungrouped(treatment[1])
x_bar_3 = s.mean_ungrouped(treatment[2])
x_bar_4 = s.mean_ungrouped(treatment[3])
dfc = s4.find_dfc_tukey(C)
dfe = s4.find_dfe_crd(N, C)
q = s3.q_dist.get_q(alpha, dfc, dfe)
hsd = s3.hsd_formula(mse, n, q)
result_12 = s3.tukey_hsd_test(mse, alpha, C, N, n, x_bar_1, x_bar_2)
result_13 = s3.tukey_hsd_test(mse, alpha, C, N, n, x_bar_1, x_bar_3)
result_14 = s3.tukey_hsd_test(mse, alpha, C, N, n, x_bar_1, x_bar_4)
result_23 = s3.tukey_hsd_test(mse, alpha, C, N, n, x_bar_2, x_bar_3)
result_24 = s3.tukey_hsd_test(mse, alpha, C, N, n, x_bar_2, x_bar_4)
result_34 = s3.tukey_hsd_test(mse, alpha, C, N, n, x_bar_3, x_bar_4)
print("EXPECTED")
print("mse:", 13.95833, "\tC:", 4,"\tN:", 16,"\tn:", 4,"\thsd:", 10.27, "\tq:", 5.5)
print("x_bar_1:", 115.25, "\tx_bar_2:", 125.25, "\tx_bar_3:", 131.5, "\tx_bar_4:", 122.5)
print("abs(x_1 - x_2) > HSD:", "No Significant Difference")
print("abs(x_1 - x_3) > HSD:", "Significant Difference")
print("abs(x_1 - x_4) > HSD:", "No Significant Difference")
print("abs(x_2 - x_3) > HSD:", "No Significant Difference")
print("abs(x_2 - x_4) > HSD:", "No Significant Difference")
print("abs(x_3 - x_4) > HSD:", "No Significant Difference")
print("RESULT")
print("mse:", mse, "\tC:", C,"\tN:", N,"\tn:", n,"\thsd:", hsd, "\tq:", q)
print("x_bar_1:", x_bar_1, "\tx_bar_2:", x_bar_2, "\tx_bar_3:", x_bar_3, "\tx_bar_4:", x_bar_4)
print("abs(x_1 - x_2) > HSD:", s3.tukey_tests_interpreter(result_12))
print("abs(x_1 - x_3) > HSD:", s3.tukey_tests_interpreter(result_13))
print("abs(x_1 - x_4) > HSD:", s3.tukey_tests_interpreter(result_14))
print("abs(x_2 - x_3) > HSD:", s3.tukey_tests_interpreter(result_23))
print("abs(x_2 - x_4) > HSD:", s3.tukey_tests_interpreter(result_24))
print("abs(x_3 - x_4) > HSD:", s3.tukey_tests_interpreter(result_34))

#11.23
print("\n11.23\n")
treatment = s.split_n_columns_to_list("4.05	3.99	3.97	4.00 \
4.01	4.02	3.98	4.02 \
4.02	4.01	3.97	3.99 \
4.04	3.99	3.95	4.01 \
NA	4.00	4.00	NA \
NA	4.00	NA	NA", 4)
mse = s3.mse_formula_crd(treatment)
alpha = .01
C = s3.find_C(treatment)
N = s3.find_N(treatment)
x_bar_1 = s.mean_ungrouped(treatment[0])
x_bar_2 = s.mean_ungrouped(treatment[1])
x_bar_3 = s.mean_ungrouped(treatment[2])
x_bar_4 = s.mean_ungrouped(treatment[3])
n_1 = len(treatment[0])
n_2 = len(treatment[1])
n_3 = len(treatment[2])
n_4 = len(treatment[3])
dfc = s4.find_dfc_tukey(C)
dfe = s4.find_dfe_crd(N, C)
q = s3.q_dist.get_q(alpha, dfc, dfe)
hsd_12 = s3.hsd_formula_modified(mse, n_1, n_2, q)
hsd_13 = s3.hsd_formula_modified(mse, n_1, n_3, q)
hsd_14 = s3.hsd_formula_modified(mse, n_1, n_4, q)
hsd_23 = s3.hsd_formula_modified(mse, n_2, n_3, q)
hsd_24 = s3.hsd_formula_modified(mse, n_2, n_4, q)
hsd_34 = s3.hsd_formula_modified(mse, n_3, n_4, q)
result_12 = s3.tukey_kramer_procedure(mse, alpha, C, N, n_1, n_2, x_bar_1, x_bar_2)
result_13 = s3.tukey_kramer_procedure(mse, alpha, C, N, n_1, n_3, x_bar_1, x_bar_3)
result_14 = s3.tukey_kramer_procedure(mse, alpha, C, N, n_1, n_4, x_bar_1, x_bar_4)
result_23 = s3.tukey_kramer_procedure(mse, alpha, C, N, n_2, n_3, x_bar_2, x_bar_3)
result_24 = s3.tukey_kramer_procedure(mse, alpha, C, N, n_2, n_4, x_bar_2, x_bar_4)
result_34 = s3.tukey_kramer_procedure(mse, alpha, C, N, n_3, n_4, x_bar_3, x_bar_4)
print("EXPECTED")
print("mse:", .000234, "\tC:", 4,"\tN:", 19, "\tq:", 5.25)
print("n_1:", n_1,"\tn_2:", n_2, "n_3:", n_3,"\tn_4:", n_4)
print("x_bar_1:", 4.03, "\tx_bar_2:", 4.001667, "\tx_bar_3:", 3.974, "\tx_bar_4:", 4.005)
print("hsd_12:", .0367, "\thsd_13:", .0381, "\thsd_14:", .0402, "\thsd_23:", .0344, "\thsd_24:", .0367, "\thsd_34:", .0381)
print("abs(x_1 - x_2) > HSD:", "Not Significant Difference")
print("abs(x_1 - x_3) > HSD:", "Significant Difference")
print("abs(x_1 - x_4) > HSD:", "No Significant Difference")
print("abs(x_2 - x_3) > HSD:", "No Significant Difference")
print("abs(x_2 - x_4) > HSD:", "No Significant Difference")
print("abs(x_3 - x_4) > HSD:", "No Significant Difference")
print("RESULT")
print("mse:", mse, "\tC:", C,"\tN:", N, "\tq:", q)
print("n_1:", n_1,"\tn_2:", n_2, "n_3:", n_3,"\tn_4:", n_4)
print("x_bar_1:", x_bar_1, "\tx_bar_2:", x_bar_2, "\tx_bar_3:", x_bar_3, "\tx_bar_4:", x_bar_4)
print("hsd_12:", hsd_12, "\thsd_13:", hsd_13, "\thsd_14:", hsd_14, "\thsd_23:", hsd_23, "\thsd_24:", hsd_24, "\thsd_34:", hsd_34)
print("abs(x_1 - x_2) > HSD:", s3.tukey_tests_interpreter(result_12))
print("abs(x_1 - x_3) > HSD:", s3.tukey_tests_interpreter(result_13))
print("abs(x_1 - x_4) > HSD:", s3.tukey_tests_interpreter(result_14))
print("abs(x_2 - x_3) > HSD:", s3.tukey_tests_interpreter(result_23))
print("abs(x_2 - x_4) > HSD:", s3.tukey_tests_interpreter(result_24))
print("abs(x_3 - x_4) > HSD:", s3.tukey_tests_interpreter(result_34))

#11.25
print("\n11.25\n")
treatment = s.split_n_columns_to_list("7	 8	5 \
7	 9	6 \
8	 8	5 \
7	10	7 \
9	 9	4 \
NA 	10	8 \
NA 	 8	NA ", 3)
alpha = .05
mse = s3.mse_formula_crd(treatment)
alpha = .05
C = s3.find_C(treatment)
N = s3.find_N(treatment)
x_bar_1 = s.mean_ungrouped(treatment[0])
x_bar_2 = s.mean_ungrouped(treatment[1])
x_bar_3 = s.mean_ungrouped(treatment[2])
n_1 = len(treatment[0])
n_2 = len(treatment[1])
n_3 = len(treatment[2])
dfc = s4.find_dfc_tukey(C)
dfe = s4.find_dfe_crd(N, C)
q = s3.q_dist.get_q(alpha, dfc, dfe)
hsd_12 = s3.hsd_formula_modified(mse, n_1, n_2, q)
hsd_13 = s3.hsd_formula_modified(mse, n_1, n_3, q)
hsd_23 = s3.hsd_formula_modified(mse, n_2, n_3, q)
result_12 = s3.tukey_kramer_procedure(mse, alpha, C, N, n_1, n_2, x_bar_1, x_bar_2)
result_13 = s3.tukey_kramer_procedure(mse, alpha, C, N, n_1, n_3, x_bar_1, x_bar_3)
result_23 = s3.tukey_kramer_procedure(mse, alpha, C, N, n_2, n_3, x_bar_2, x_bar_3)
print("EXPECTED")
print("mse:", 1.259365, "\tC:", 3,"\tN:", 18, "\tq:", 3.67)
print("n_1:", n_1,"\tn_2:", n_2, "\tn_3:", n_3)
print("x_bar_1:", 7.6, "\tx_bar_2:", 8.8571, "\tx_bar_3:", 5.8333)
print("hsd_12:", 1.705, "\thsd_13:", 1.763, "\thsd_23:", 1.62)
print("abs(x_1 - x_2) > HSD:", "No Significant Difference")
print("abs(x_1 - x_3) > HSD:", "Significant Difference")
print("abs(x_2 - x_3) > HSD:", "Significant Difference")
print("RESULT")
print("mse:", mse, "\tC:", C,"\tN:", N, "\tq:", q)
print("n_1:", n_1,"\tn_2:", n_2, "\tn_3:", n_3)
print("x_bar_1:", x_bar_1, "\tx_bar_2:", x_bar_2, "\tx_bar_3:", x_bar_3)
print("hsd_12:", hsd_12, "\thsd_13:", hsd_13, "\thsd_23:", hsd_23)
print("abs(x_1 - x_2) > HSD:", s3.tukey_tests_interpreter(result_12))
print("abs(x_1 - x_3) > HSD:", s3.tukey_tests_interpreter(result_13))
print("abs(x_2 - x_3) > HSD:", s3.tukey_tests_interpreter(result_23))


#CHAPTER 11: PART 4:
print("\nCHAPTER 11 PART 4:\n")


#11.29
print("\n11.29\n")
treatment = s.split_n_columns_to_list("1.28	1.29	1.29 \
	1.40	1.36	1.35 \
 	1.15	1.13	1.19 \
 	1.22	1.18	1.24", 3)
alpha = .01
C = s3.find_C(treatment)
N = s3.find_N(treatment)
n = len(treatment[0])
dfc = s4.find_dfc(C) #C - 1
dfr = s4.find_dfr_rbd(n) #n - 1
dfe = s4.find_dfe_rbd(N, n, C) #N - n - C + 1
ssc = s3.ssc_formula(treatment)
ssr = s3.ssr_formula_rbd(treatment)
sse = s3.sse_formula_rbd(treatment)
msc = s3.msc_formula(treatment)
msr = s3.msr_formula_rbd(treatment)
mse = s3.mse_formula_rbd(treatment)
f = s3.one_way_ANOVA_rbd(treatment)
f_c = s2.f_dist.get_f(alpha, dfc, dfe, "upper")
result = s4.HT_checker(f[0], ">", f_c) #only F = f[0] is used in hypothesis test
print("EXPECTED")
print("dfc", 2, "\tssc", .001717, "\tmsc", .000858, "\tF", 1.48)
print("dfr", 3, "\tssr", .076867, "\tmsr", .025622, "\tF_r", 44.13)
print("dfe", 6, "\tsse", .003483, "\tmse", .000581)
print("F_c", 10.92)
print("test result:", "Fail to Reject Null Hypothesis")
print("RESULT")
print("dfc", dfc, "\tssc", ssc, "\tmsc", msc, "\tF", f[0])
print("dfr", dfr, "\tssr", ssr, "\tmsr", msr, "\tF_r", f[1])
print("dfe", dfe, "\tsse", sse, "\tmse", mse)
print("F_c", f_c)
print("test result:", result)

#11.31
print("\n11.31\n")
alpha = .01
ssc = 199.48
ssr = 265.24
sse = 306.59
C = 4
N = 4 * 7
n = 7
dfc = s4.find_dfc(C)
dfr = s4.find_dfr_rbd(n)
dfe = s4.find_dfe_rbd(N, n, C)
msc = s4.msc_formula(ssc, dfc)
msr = s4.msr_formula_rbd(ssr, dfr)
mse = s4.mse_formula_rbd(sse, dfe)
f = s4.one_way_ANOVA_rbd(msc, mse, msr)
f_c = s2.f_dist.get_f(alpha, dfc, dfe, "upper")
result = s4.HT_checker(f[0], ">", f_c)
print("EXPECTED")
print("dfc", 3, "\tssc", 199.48, "\tmsc", 66.493, "\tF", 3.9)
print("dfr", 6, "\tssr", 265.24, "\tmsr", 44.207, "\tF_r", 2.6)
print("dfe", 18, "\tsse", 306.59, "\tmse", 17.033)
print("F_c", 10.92)
print("test result:", "Fail to Reject Null Hypothesis")
print("RESULT")
print("dfc", dfc, "\tssc", ssc, "\tmsc", msc, "\tF", f[0])
print("dfr", dfr, "\tssr", ssr, "\tmsr", msr, "\tF_r", f[1])
print("dfe", dfe, "\tsse", sse, "\tmse", mse)
print("F_c", f_c)
print("test result:", result)

#11.33
print("\n11.33\n")
treatment = s.split_n_columns_to_list("11	 5	 8 \
	15	 9	 8 \
	19	14	15 \
	16	12	10 \
	 9	 8	 7", 3)
alpha = .01
C = s3.find_C(treatment)
N = s3.find_N(treatment)
n = len(treatment[0])
dfc = s4.find_dfc(C)
dfr = s4.find_dfr_rbd(n) 
dfe = s4.find_dfe_rbd(N, n, C)
ssc = s3.ssc_formula(treatment)
ssr = s3.ssr_formula_rbd(treatment)
sse = s3.sse_formula_rbd(treatment)
msc = s3.msc_formula(treatment)
msr = s3.msr_formula_rbd(treatment)
mse = s3.mse_formula_rbd(treatment)
f = s3.one_way_ANOVA_rbd(treatment)
f_c = s2.f_dist.get_f(alpha, dfc, dfe, "upper")
result = s4.HT_checker(f[0], ">", f_c)
print("EXPECTED")
print("dfc", 2, "\tssc", 64.5333, "\tmsc", 32.2667, "\tF", 15.37)
print("dfr", 4, "\tssr", 137.6, "\tmsr", 34.4, "\tF_r", 16.38)
print("dfe", 8, "\tsse", 16.8, "\tmse", 2.1)
print("F_c", 8.65)
print("test result:", "Reject Null Hypothesis")
print("RESULT")
print("dfc", dfc, "\tssc", ssc, "\tmsc", msc, "\tF", f[0])
print("dfr", dfr, "\tssr", ssr, "\tmsr", msr, "\tF_r", f[1])
print("dfe", dfe, "\tsse", sse, "\tmse", mse)
print("F_c", f_c)
print("test result:", result)


#CHAPTER 12 PART 1:
print("\nCHAPTER 12 PART 1:\n")

#12.1
print("\n12.1\n")
x_variables = [4,6,7,11,14,17,21]
y_variables = [18,12,13,8,7,7,4]
r = s3.pearson_product_moment_correlation_coefficient(x_variables, y_variables)
print("EXPECTED:", -.927)
print("RESULT:", r)

#12.3
print("\n12.3\n")
t = s.split_n_columns_to_list("0.75	11.92 \
0.76	12.09 \
0.84	12.25 \
0.85	11.85 \
0.86	11.78 \
0.86	11.74", 2)
x_variables = t[0]
y_variables = t[1]
r = s3.pearson_product_moment_correlation_coefficient(x_variables, y_variables)
print("EXPECTED:", -.37)
print("RESULT:", r)

#12.5
print("\n12.5\n")
t = s.split_n_columns_to_list("0.46	0.48	0.69 \
	0.52	0.62	0.63 \
	0.90	0.72	0.81 \
	1.50	1.74	2.10 \
	2.89	2.03	2.46 \
	1.80	1.92	2.00 \
	3.29	3.18	3.17 \
	5.73	4.43	4.00", 3)
variables_1 = t[0]
variables_2 = t[1]
variables_3 = t[2]
r_12 = s3.pearson_product_moment_correlation_coefficient(variables_1, variables_2)
r_13 = s3.pearson_product_moment_correlation_coefficient(variables_1, variables_3)
r_23 = s3.pearson_product_moment_correlation_coefficient(variables_2, variables_3)
print("EXPECTED:", "\tr_12", .975, "\tr_13", .985, "\tr_23", .957)
print("RESULT:",  "\tr_12", r_12, "\tr_13", r_13, "\tr_23", r_23)


#CHAPTER 12 PART 3:
print("\nCHAPTER 12 PART 3:\n")

#12.7
print("\n12.7\n")
x_variables = [140, 119, 103, 91, 65, 29, 24]
y_variables = [25, 29, 46, 70, 88, 112, 128]
lsrl = s3.least_squares_regression_line(x_variables, y_variables)
print("EXPECTED:", (144.414, -.898))
print("RESULT:", lsrl)

#12.9
print("\n12.9\n")
t = s.split_n_columns_to_list("5	 16 \
12	 6 \
 9	 8 \
15	 4 \
 7	 7", 2)
x_variables = t[1]
y_variables = t[0]
lsrl = s3.least_squares_regression_line(x_variables, y_variables)
print("EXPECTED:", (15.46, -.715))
print("RESULT:", lsrl)

#12.11
print("\n12.11\n")
t = s.split_n_columns_to_list("1961	480.88	69.83	145 \
1966	430.50	70.46	164 \
1971	366.11	68.66	188 \
1976	338.55	68.43	202 \
1981	318.36	65.89	207 \
1986	293.09	67.83	231 \
1991	280.04	67.75	242 \
1996	276.55	68.05	246 \
2001	246.92	67.50	273 \
2006	229.37	67.59	295 \
2011	205.73	64.81	315", 4)
x_variables = t[1]
y_variables = t[3]
lsrl = s3.least_squares_regression_line(x_variables, y_variables)
print("EXPECTED:", (420.5, -.6108))
print("RESULT:", lsrl)


#CHAPTER 12 PART 4:
print("\nCHAPTER 12 PART 4:\n")

#12.19
print("\n12.19\n")
x_variables = [5,7,11,12,19,25]
y_variables = [47,38,32,24,22,10]
lsrl = s3.least_squares_regression_line(x_variables, y_variables)
residuals = s3.find_residuals(x_variables, y_variables)
residuals = s.list_rounder(residuals)   
print("EXPECTED:")
print("lsrl", (50.506, -1.646))
print("residuals:", [4.7244, -.9836, -.3996, -6.7537, 2.7683,.6442])
print("RESULT:")
print("lsrl", lsrl)
print("residuals:", residuals)
#p.plot_points(x_variables, residuals)

#12.21
print("\n12.21\n")
t = s.split_n_columns_to_list("213  -11 \
216	-5 \
227	-2 \
229	-1 \
237	 6 \
247	10 \
263	12", 2)
x_variables = t[0]
residuals = t[1]
#p.plot_points(x_variables, residuals)


#CHAPTER 12 PART 5:
print("\nCHAPTER 12 PART 5:\n")

#12.25
print("\n12.25\n")
x_variables = [140, 119, 103, 91, 65, 29, 24]
y_variables = [25, 29, 46, 70, 88, 112, 128]
residuals = s3.find_residuals(x_variables, y_variables)
residuals = s.list_rounder(residuals)  
sse = s3.sse_formula_regression(x_variables, y_variables)
s_e = s3.standard_error_of_the_estimate(x_variables, y_variables)
within_1_se = []
within_2_se = []
for residual in residuals:
    if (-2 * s_e) < residual < (2 * s_e):
        within_2_se.append(residual)
        if -s_e < residual < s_e:
            within_1_se.append(residual)

print("EXPECTED:")
print("sse", 272.153, "\ts_e", 7.38)
print("within +/- 1 se:", 6)
print("within +/- 2 se:", 7)
print("RESULT:")
print("sse", sse, "\ts_e", s_e)
print("within +/- 1 se:", len(within_1_se))
print("within +/- 2 se:", len(within_2_se))
print(residuals)

#12.27
print("\n12.27\n")
t = s.split_n_columns_to_list("5	 16 \
12	 6 \
 9	 8 \
15	 4 \
 7	 7", 2)
x_variables = t[1]
y_variables = t[0]
residuals = s3.find_residuals(x_variables, y_variables)
residuals = s.list_rounder(residuals)  
sse = s3.sse_formula_regression(x_variables, y_variables)
s_e = s3.standard_error_of_the_estimate(x_variables, y_variables)
within_1_se = []
within_2_se = []
for residual in residuals:
    if -s_e < residual < s_e:
        within_1_se.append(residual)
print("EXPECTED:")
print("sse", 19.89326, "\ts_e", 2.575)
print("within +/- 1 se:", 4)
print("RESULT:")
print("sse", sse, "\ts_e", s_e)
print("within +/- 1 se:", len(within_1_se))


#12.29
print("\n12.29\n")
x_variables = [5,7,11,12,19,25]
y_variables = [47,38,32,24,22,10]
s_e = s3.standard_error_of_the_estimate(x_variables, y_variables)
print("EXPECTED:", 4.391)
print("RESULT:", s_e)
