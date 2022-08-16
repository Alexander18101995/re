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
