import stats_module as s    #Sampling Distributions
import stats_module_2 as s2 #Hypthesis Tests & CI's
import stats_module_3 as s3 #ANOVA (arguments are treatments)
import stats_module_4 as s4 #ANOVA (arguments are values)
import plotter as p

#CHAPTER 16: PART 1:

#16.1
print("\n16.1\n")
ct = s.split_n_columns_to_list("1	53	68 \
2	37	42 \
3	32	33 \
4	28	22 \
5	18	10 \
6	15	 8", 3)
observations = ct[1]
expectations = ct[2]
k = 6
alpha = .05
X_2 = round(s4.X_2_goodness_of_fit_test(observations, expectations), 4)
df = s4.get_df_X_2_goodness_of_fit_test(k)
X_2_c = round(s2.alpha_to_X_2(alpha, df, ">"), 4)
result = s4.HT_checker(X_2, ">", X_2_c)
print("EXPECTED:", "\tX_2 =", 18.095, "\tX_2_c =", 11.0705, "\tTest Result:", "Reject Null Hypothesis")
print("RESULT:", "\tX_2 =", X_2, "\tX_2_c =", X_2_c, "\tTest Result:", result)

#16.2
print("\n16.2\n")
ct = s.split_n_columns_to_list("1	19 \
2	17 \
3	14 \
4	18 \
5	19 \
6	21 \
7	18 \
8	18", 2)
observations = ct[1]
expectations = s4.get_expectations_uniform(observations)
k = 8
alpha = .01
X_2 = round(s4.X_2_goodness_of_fit_test(observations, expectations), 4)
df = s4.get_df_X_2_goodness_of_fit_test(k)
X_2_c = round(s2.alpha_to_X_2(alpha, df, ">"), 4)
result = s4.HT_checker(X_2, ">", X_2_c)
print("EXPECTED:", "\tX_2 =", 1.557, "\tX_2_c =", 18.4753, "\tTest Result:", "Fail to Reject Null Hypothesis")
print("RESULT:", "\tX_2 =", X_2, "\tX_2_c =", X_2_c, "\tTest Result:", result)

#16.5
print("\n16.5\n")
observations = [42, 95, 27, 63]
compared_proportions = [.39, .12, .18, .31]
expectations = s4.get_expectations_proportions(observations, compared_proportions)
k = 4
alpha = .05
X_2 = s4.X_2_goodness_of_fit_test(observations, expectations)
X_2 = round(X_2, 4)
df = s4.get_df_X_2_goodness_of_fit_test(k)
X_2_c = round(s2.alpha_to_X_2(alpha, df, ">"), 4)
result = s4.HT_checker(X_2, ">", X_2_c)
print("EXPECTED:", "\tX_2 =", 198.48, "\tX_2_c =", 7.8147, "\tTest Result:", "Reject Null Hypothesis")
print("RESULT:", "\tX_2 =", X_2, "\tX_2_c =", X_2_c, "\tTest Result:", result)

#16.6
print("\n16.6\n")
ct = s.split_n_columns_to_list("10 14	 .09	22 \
15 19	.23	50 \
20 24	.22	43 \
25 29	.14	29 \
30 34	.10	19 \
35 35	.22	49", 4)
observations = ct[3]
expected_proportions = ct[2]
expectations = s4.get_expectations_proportions(observations, expected_proportions)
k = 6
alpha = .01
X_2 = s4.X_2_goodness_of_fit_test(observations, expectations)
X_2 = round(X_2, 4)
df = s4.get_df_X_2_goodness_of_fit_test(k)
X_2_c = round(s2.alpha_to_X_2(alpha, df, ">"), 4)
result = s4.HT_checker(X_2, ">", X_2_c)
print("EXPECTED:", "\tX_2 =", 1.13, "\tX_2_c =", 15.0863, "\tTest Result:", "Fail to Reject Null Hypothesis")
print("RESULT:", "\tX_2 =", X_2, "\tX_2_c =", X_2_c, "\tTest Result:", result)

#16.9
print("\n16.9\n")
observations = [96, 27, 157]
expected_proportions = [.4, .12, .48]
expectations = s4.get_expectations_proportions(observations, expected_proportions)
k = 3
alpha = .01
X_2 = s4.X_2_goodness_of_fit_test(observations, expectations)
X_2 = round(X_2, 4)
df = s4.get_df_X_2_goodness_of_fit_test(k)
X_2_c = round(s2.alpha_to_X_2(alpha, df, ">"), 4)
result = s4.HT_checker(X_2, ">", X_2_c)
print("EXPECTED:", "\tX_2 =", 7.39, "\tX_2_c =", 9.2104, "\tTest Result:", "Fail to Reject Null Hypothesis")
print("RESULT:", "\tX_2 =", X_2, "\tX_2_c =", X_2_c, "\tTest Result:", result)


#CHAPTER 16: PART 2:

#16.13
print("\n16.13\n")
alpha = .05
contingency_table = s.split_n_columns_to_list(" 7	18	 6 \
    	 9	38	23 \
	34	97	58 \
	47	31	30", 3)
X_2 = s4.X_2_independance_test(contingency_table)
df = s4.get_df_X_2_independance_test(3, 4)
X_2_c = s2.alpha_to_X_2(alpha, df, ">")
X_2_c = round(X_2_c, 4)
result = s4.HT_checker(X_2, ">", X_2_c)
print("EXPECTED:", "\tX_2 =", 34.98, "\tX_2_c =", 12.5916, "\tTest Result:", "Reject Null Hypothesis")
print("RESULT:", "\tX_2 =", X_2, "\tX_2_c =", X_2_c, "\tTest Result:", result)

#16.14
print("\n16.14\n")
contingency_table = s.split_n_columns_to_list("140	32	 5	18 \
	134	41	52	 8 \
	154	27	 8	13", 4)
alpha = .01
X_2 = s4.X_2_independance_test(contingency_table)
df = s4.get_df_X_2_independance_test(4, 3)
X_2_c = s2.alpha_to_X_2(alpha, df, ">")
X_2_c = round(X_2_c, 4)
result = s4.HT_checker(X_2, ">", X_2_c)
print("EXPECTED:", "\tX_2 =", 64.91, "\tX_2_c =", 16.8119, "\tTest Result:", "Reject Null Hypothesis")
print("RESULT:", "\tX_2 =", X_2, "\tX_2_c =", X_2_c, "\tTest Result:", result)

#16.15
print("\n16.15\n")
contingency_table = s.split_n_columns_to_list("32	12	41 \
5	 6	 24", 3)
alpha = .05
X_2 = s4.X_2_independance_test(contingency_table)
df = s4.get_df_X_2_independance_test(3, 2)
X_2_c = s2.alpha_to_X_2(alpha, df, ">")
X_2_c = round(X_2_c, 4)
result = s4.HT_checker(X_2, ">", X_2_c)
print("EXPECTED:", "\tX_2 =", 6.43, "\tX_2_c =", 5.9915, "\tTest Result:", "Reject Null Hypothesis")
print("RESULT:", "\tX_2 =", X_2, "\tX_2_c =", X_2_c, "\tTest Result:", result)



