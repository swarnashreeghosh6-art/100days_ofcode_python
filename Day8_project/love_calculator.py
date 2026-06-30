def calculate_love_score(name1,name2):
    list=[]
    for letter in name1:
        list.append(letter)
    for letter in name2:
        list.append(letter)
    true="TRUE"
    love="LOVE"
    total_1=0
    total_2=0
    for i in true:
        count_1=list.count(i)
        total_1+=count_1
    for j in love:
        count_2=list.count(j)
        total_2+=count_2
    print(f"Love Score={total_1}{total_2}")
calculate_love_score("Kanye West".upper(),"Taylor Swift".upper())
