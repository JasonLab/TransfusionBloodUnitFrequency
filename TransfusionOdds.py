"""
Info for user:
Enter the antibodies your patient had to determine the odds of finding antigen(-) blood.
Data taken from https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3705660/  This if for the indian blood donor population in 2013.
!!!!DISCLAIMER:I recommend using your own data from the area you are in. Depending on where you are these values can vary GREATLY.

Infor for programming:
Many elements are still open to being worked on.
Will need to bring in loops for "dummyproofing" answers that aren't in the database
"""

#Created a dictionary that will hold the antigens and their value
antigens = {}
#Adding the antigens to the dictionary
#The current program uses popularity of the antigen and converts it antigen(-) frequency in the calculations.
antigens['d'] = 0.936 #Popularity of the antigen. 
antigens['bigc'] = 0.87 #Could have named them c and C but that brings into the case sensitive issue with the others. With such a small list it shouldnt be a hassle for now
antigens['littlec'] = 0.58
antigens['bige'] = 0.20
antigens['littlee'] = 0.98
antigens['bigk'] = 0.035
antigens['littlek'] = 0.9997
antigens['fya'] = 0.874
antigens['fyb'] = 0.576
antigens['jka'] = 0.815
antigens['jkb'] = 0.674
antigens['m'] = 0.887
antigens['n'] = 0.654
antigens['bigs'] = 0.548
antigens['littles'] = 0.887

def blood_percentage1(x):
    if first_antibody in antigens:
        x= antigens[first_antibody]
        y = (1-x)*100
        print("Frequence of the antigen in decimal", x)
        return y
def blood_percentage2(c, v):
    if c in antigens:
        c = antigens[c]
    if v in antigens:
        v = antigens[v]
    y = ((1-c)*(1-v))*100
    print("Frequence of the antigens in decimal", c, v)
    return y
def blood_percentage3(c2, v2, p2):
    if c2 in antigens:
        c2 = antigens[c2]
    if v2 in antigens:
        v2 = antigens[v2]
    if p2 in antigens:
        p2 = antigens[p2]
    y = ((1-c2)*(1-v2)*(1-p2))*100
    print("Frequence of the antigens in decimal", c2, v2, p2) #Was used as a check, will keep it open until a final version is done. Might be useful for user somewhat.
    return y

print("Hello. What is the first antibody the patient has? Enter it from the list below.")
print("If there are no more antibodies you are looking for, just enter 'none'")
units = int(input("Enter the amount of units you need:"))
print("Antigens supported in the current database are: ", ", ".join(antigens.keys()))
first_antibody =  input("Enter the first antibody here: ")
first_antibody = first_antibody.lower()
second_antibody = input("Enter the second antibody here:")
second_antibody = second_antibody.lower()

if second_antibody == "none":
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("Your odds of finding one antigen negative unit are:", round(blood_percentage1(first_antibody), 1), "%")
    print("For",units, " units you would have to type", round((units/((blood_percentage1(first_antibody))/100)),0), " units") #will clean this up eventually
else:
    third_antibody = input("Enter the third antibody here:")
    third_antibody = third_antibody.lower()
    if third_antibody == "none":
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("Your odds of finding one antigen negative unit are:", round((blood_percentage2(first_antibody, second_antibody)), 2), "%")
        print("For", units, " units you would have to type", round((units / ((blood_percentage2(first_antibody, second_antibody)) / 100)),0), " units")
    elif third_antibody in antigens:
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("Your odds of finding one antigen negative unit are:", round((blood_percentage3(first_antibody, second_antibody, third_antibody)),3), "%")
        print("For", units, " units you would have to type", round((units / ((blood_percentage3(first_antibody, second_antibody, third_antibody)) / 100)),0), " units")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
