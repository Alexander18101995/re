import re 

text = "lastname,firstname,surname,organization,position,phone,email Усольцев Олег Валентинович,,,ФНС,главный специалист – эксперт отдела взаимодействия с федеральными органами власти Управления налогообложения имущества и доходов физических лиц,+7 (495) 913-04-78,opendata@nalog.ru Мартиняхин Виталий Геннадьевич,,,ФНС,,+74959130037, Наркаев,Вячеслав Рифхатович,,ФНС,,8 495-913-0168,Мартиняхин,Виталий,Геннадьевич,ФНС,cоветник отдела Интернет проектов Управления информационных технологий,,,Лукина Ольга Владимировна,,,Минфин,,+7 (495) 983-36-99 доб. 2926,Olga.Lukina@minfin.ru Паньшин Алексей Владимирович,,,Минфин,,8(495)748-49-73,1248@minfin.ru Лагунцов Иван Алексеевич,,,Минфин,,+7 (495) 913-11-11 (доб. 0792),Лагунцов Иван,,,,,,Ivan.Laguntcov@minfin.ru"

pattern = r"(\+7)\s\((\d+)\)\s*(\d+)-(\d+)-(\d+)"
pattern_2 = r"(\+7)(\d{3})(\d{3})(\d{2})(\d{2})"
pattern_3 = r"(8)\((\d+)\)(\d+)-(\d+)-(\d+)"
pattern_4 = r"(8)\s(\d+)-(\d+)-(\d{2})(\d+)"
r_p = r"+7(\2)\3-\4-\5"
result = re.sub(pattern,r_p,text)
result_2 = re.sub(pattern_2,r_p,result)
result_3 = re.sub(pattern_3,r_p,result_2)
result_4 = re.sub(pattern_4,r_p,result_3)

pattern_5 = r"(\+7)\((\d+)\)(\d+)-(\d+)-(\d+)\s\((\w+.)\s(\w+)\)"
r_p_2 = r"+7(\2)\3-\4-\5 \6\7"
result_5 = re.sub(pattern_5,r_p_2,result_4)
pattern_6 = r"(\+7)\((\d+)\)(\d+)-(\d+)-(\d+)\s(\w+.)\s(\d+)"
r_p_2 = r"+7(\2)\3-\4-\5 \6\7"
result_6 = re.sub(pattern_6,r_p_2,result_5)

print(result_6)