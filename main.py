import re
import csv
with open("phonebook_raw.csv") as f:
  rows = csv.reader(f, delimiter=",")
  contacts_list = list(rows)
  contacts_list[1][1] = contacts_list[1][0][9:13]
  contacts_list[1][2] = contacts_list[1][0][14:]
  contacts_list[1][0] = contacts_list[1][0][:8]
  contacts_list[4][5] = contacts_list[2][5]
  del contacts_list[4][6]
  del contacts_list[2]
  contacts_list[2][2] = contacts_list[2][1][9:]
  contacts_list[2][1] = contacts_list[2][1][:8]
  contacts_list[4][1] = contacts_list[4][0][7:12]
  contacts_list[4][2] = contacts_list[4][0][13:]
  contacts_list[4][0] = contacts_list[4][0][:6]
  contacts_list[5][1] = contacts_list[5][0][8:15]
  contacts_list[5][2] = contacts_list[5][0][16:]
  contacts_list[5][0] = contacts_list[5][0][:7]
  contacts_list[7][1] = contacts_list[7][0][9:]
  contacts_list[7][0] = contacts_list[7][0][:8]
  contacts_list[7][2] = contacts_list[6][0][14:]
  contacts_list[7][3] = contacts_list[6][3]
  contacts_list[7][5] = contacts_list[6][5]
  del contacts_list[6] 
  for cl in contacts_list:
    res = ','.join(cl)
    pattern = r"(\+7)\s\((\d+)\)\s*(\d+)-(\d+)-(\d+)"
    pattern_2 = r"(\+7)(\d{3})(\d{3})(\d{2})(\d{2})"
    pattern_3 = r"(8)\((\d+)\)(\d+)-(\d+)-(\d+)"
    pattern_4 = r"(8)\s(\d+)-(\d+)-(\d{2})(\d+)"
    r_p = r"+7(\2)\3-\4-\5"
    result = re.sub(pattern,r_p,res)
    result_2 = re.sub(pattern_2,r_p,result)
    result_3 = re.sub(pattern_3,r_p,result_2)
    result_4 = re.sub(pattern_4,r_p,result_3)
    pattern_5 = r"(\+7)\((\d+)\)(\d+)-(\d+)-(\d+)\s\((\w+.)\s(\w+)\)"
    r_p_2 = r"+7(\2)\3-\4-\5 \6\7"
    result_5 = re.sub(pattern_5,r_p_2,result_4)
    pattern_6 = r"(\+7)\((\d+)\)(\d+)-(\d+)-(\d+)\s(\w+.)\s(\d+)"
    r_p_2 = r"+7(\2)\3-\4-\5 \6\7"
    result_6 = re.sub(pattern_6,r_p_2,result_5)
    new_contacts_list = result_6
    print(new_contacts_list)
    # with open("phonebook.csv", "w") as f:
    #   datawriter = csv.writer(f)
    #   datawriter.writerows(new_contacts_list)

