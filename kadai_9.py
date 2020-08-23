import pandas as pd
import numpy as np
from scipy import stats as st

df_pro = pd.read_csv("kadai_pro.csv")
df_hob = pd.read_csv("kadai_hob.csv")
df_ama = pd.read_csv("kadai_ama.csv")

df_pro["distance_pro_day1"] = np.sqrt(
    df_pro["pro_day1_x"] ** 2+df_pro["pro_day1_y"] ** 2)
df_pro["distance_pro_day7"] = np.sqrt(
    df_pro["pro_day7_x"] ** 2+df_pro["pro_day7_y"] ** 2)

df_hob["distance_hob_day1"] = np.sqrt(
    df_hob["hob_day1_x"] ** 2+df_hob["hob_day1_y"] ** 2)
df_hob["distance_hob_day7"] = np.sqrt(
    df_hob["hob_day7_x"] ** 2+df_hob["hob_day7_y"] ** 2)

df_ama["distance_ama_day1"] = np.sqrt(
    df_ama["ama_day1_x"] ** 2+df_ama["ama_day1_y"] ** 2)
df_ama["distance_ama_day7"] = np.sqrt(
    df_ama["ama_day7_x"] ** 2+df_ama["ama_day7_y"] ** 2)

p_pro = st.wilcoxon(df_pro["distance_pro_day1"], df_pro["distance_pro_day7"])

p_hob = st.wilcoxon(df_hob["distance_hob_day1"], df_hob["distance_hob_day7"])

p_ama = st.wilcoxon(df_ama["distance_ama_day1"], df_ama["distance_ama_day7"])

p_all_day7 = st.kruskal(df_pro["distance_pro_day7"],
                        df_hob["distance_hob_day7"], df_ama["distance_ama_day7"])

p_all_day1 = st.kruskal(df_pro["distance_pro_day1"],
                        df_hob["distance_hob_day1"], df_ama["distance_ama_day1"])

print(p_pro)
print(p_ama)
print(p_hob)
#print(p_all_day7)
print(p_all_day1)
