from regular import contacts_list
import re
pattern = r"(\+7)\s\((\d+)\)\s*(\d+)-(\d+)-(\d+)"
pattern_2 = r"(\+7)(\d{3})(\d{3})(\d{2})(\d{2})"
pattern_3 = r"(8)\((\d+)\)(\d+)-(\d+)-(\d+)"
pattern_4 = r"(8)\s(\d+)-(\d+)-(\d{2})(\d+)"
r_p = r"+7(\2)\3-\4-\5"
result = re.sub(pattern,r_p,contacts_list)
result_2 = re.sub(pattern_2,r_p,result)
result_3 = re.sub(pattern_3,r_p,result_2)
result_4 = re.sub(pattern_4,r_p,result_3)

pattern_5 = r"(\+7)\((\d+)\)(\d+)-(\d+)-(\d+)\s\((\w+.)\s(\w+)\)"
r_p_2 = r"+7(\2)\3-\4-\5 \6\7"
result_5 = re.sub(pattern_5,r_p_2,result_4)
pattern_6 = r"(\+7)\((\d+)\)(\d+)-(\d+)-(\d+)\s(\w+.)\s(\d+)"
r_p_2 = r"+7(\2)\3-\4-\5 \6\7"
result_6 = re.sub(pattern_6,r_p_2,result_5)
