numbers = [
    '+5(4671)849-6225',
    '+394(63)128-1148',
    '535(02)715-68-89',
    '+72(23)661-8520',
    '+194(455)628-2961',
    '092158146777',
    '+862(179)416-6138',
    '+3(2697)794-4711',
    '+98(393)874-4458',
    '+3(632)626-8042',
    '+7611528-9013',
    '+88135130-717',
    '94(3005)670-58-48',
    '+264925558-7301',
    '58(6929)091-8491',
    '+581(067)254-6659',
    '+4(838)997-1720',
    '+7(163)228-1948',
    '72236618520',
    '967(28)959-4951',
    '+53(2121)207-3793',
    '+80(922)2856718',
    '7121-2173999'
]

new_format = [i.replace("+" , "").replace("(" , "").replace(")" , "").replace("-" , "") for i in numbers]
country_code = []
area_code = []
client_code = []
for i in new_format :
    country_code.append(i[:-10])
    area_code.append(i[-10:-7])
    client_code.append(i[-7:])

result = [(i[:-10] , i[-10:-7] , i[-7:]) for i in new_format]

print("all numbers  = " , result)

unique_num = (set(new_format))
print("all unique numbers" , unique_num)

print("we have " , len(unique_num) , "unique numbers")

unique_country = [len(set(country_code))]
print("unique countries number equal to = " , unique_country)

longest_num = max(new_format , key=len)
print("the longest number is = " , longest_num )

russian_number = []

for i in new_format :
    if len(i)== 11 and int(i[0]) == 7 :
        russian_number.append(i)

print("the list of Russian numbers = " , russian_number)
