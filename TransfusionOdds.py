"""
Info for user:
Enter the antibodies your patient had to determine the odds of finding antigen(-) blood.
Data taken from https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3705660/  This if for the indian blood donor population in 2013.
!!!!DISCLAIMER:I recommend using your own data from the area you are in. Depending on where you are these values can vary GREATLY.

Infor for programming:
Many elements are still open to being worked on.
Will need to bring in loops for "dummyproofing" answers that aren't in the database
"""
#The current program uses popularity of the antigen and converts it antigen(-) frequency in the calculations.
d = 0.936 #Popularity of the antigen. 
bigc= 0.87
littlec= 0.58 #Could have named them c and C but that brings into the case sensitive issue with the others. With such a small list it shouldnt be a hassle for now
bige= 0.20
littlee= 0.98
bigk= 0.035
littlek=0.9997
fya= 0.874
fyb= 0.576
jka= 0.815
jkb= 0.674
m= 0.887
n= 0.654
bigs= 0.548
littles= 0.887
"""
If you add additional variables(antigen frequencies) you need to add them to both the antigen_list and the 
antigen_var_list in the same order!!! Otherwise the functions won't won't atribute the right frequency
"""
antigen_list= ["d","bigc","littlec","bige","littlee","bigk","littlek","fya","fyb","jka","jkb","m","n","bigs","littles"]
antigen_var_list= [d,bigc,littlec,bige,littlee,bigk,littlek,fya,fyb,jka,jkb,m,n,bigs,littles]

def blood_percentage1(x):
    if first_antibody in antigen_list:
        locationantigen = (antigen_list.index(x))
        x= (antigen_var_list[locationantigen])
        y = (1-x)*100
        print("Frequence of the antigen in decimal", x)
        return y
def blood_percentage2(c,v):
    if c in antigen_list:
        locationantigen = (antigen_list.index(c))
        c= (antigen_var_list[locationantigen])
    if v in antigen_list:
        locationantigen = (antigen_list.index(v))
        v = (antigen_var_list[locationantigen])
    y = ((1-c)*(1-v))*100
    print ("Frequence of the antigens in decimal",c,v)
    return y
def blood_percentage3(c2,v2,p2):
    if c2 in antigen_list:
        locationantigen = (antigen_list.index(c2))
        c2= (antigen_var_list[locationantigen])
    if v2 in antigen_list:
        locationantigen = (antigen_list.index(v2))
        v2 = (antigen_var_list[locationantigen])
        if p2 in antigen_list:
            locationantigen = (antigen_list.index(p2))
            p2 = (antigen_var_list[locationantigen])
    y = ((1-c2)*(1-v2)*(1-p2))*100
    print ("Frequence of the antigens in decimal",c2,v2,p2) #Was used as a check, will keep it open until a final version is done. Might be useful for user somewhat.
    return y

print("Hello. What is the first antibody the patient has? Enter it from the list below.")
print("If there are no more antibodies you are looking for, just enter 'none'")
units= int(input("Enter the amount of units you need:"))
print("Antigens supported in the current database are: ",antigen_list)
first_antibody=  input("Enter the first antibody here: ")
first_antibody= first_antibody.lower()
second_antibody= input("Enter the second antibody here:")
second_antibody= second_antibody.lower()

if second_antibody == "none":
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("Your odds of finding one antigen negative unit are:", round(blood_percentage1(first_antibody),1), "%")
    print("For",units, " units you would have to type",round((units/((blood_percentage1(first_antibody))/100)),0)," units") #will clean this up eventually
else:
    third_antibody = input("Enter the third antibody here:")
    third_antibody = third_antibody.lower()
    if third_antibody == "none":
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("Your odds of finding one antigen negative unit are:", round((blood_percentage2(first_antibody,second_antibody)),2), "%")
        print("For", units, " units you would have to type", round((units / ((blood_percentage2(first_antibody,second_antibody)) / 100)),0)," units")
    elif third_antibody in antigen_list:
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("Your odds of finding one antigen negative unit are:", round((blood_percentage3(first_antibody,second_antibody,third_antibody)),3), "%")
        print("For", units, " units you would have to type", round((units / ((blood_percentage3(first_antibody,second_antibody,third_antibody)) / 100)),0)," units")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
