from covid import Covid
from random import *
import time
Y="y"
print( '''Hello everyone,this section does not contain a 100% accurate data
      But.... for an approximate data, i am pleased to know you have chose this option.
      As we all know that the pandemic has made the busy world to stand still
      But i will argue that this wasn\'t all negative, this is digitally a blessing in disguise
      So without any more further delay lets proceed.......''')
random_stuffs=['''Pandemic : A pandemic is an epidemic of an infectious disease that 
        has spread across a large region, for instance multiple continents or worldwide,
        affecting a substantial number of people.''',"CoViD-19 : Corona Virus Disease 2019 or SARS-CoV-2","Anosmia (loss of smell) is a symptom.","SARS-CoV-2 binds tightly to human cells.",'''Compared to adults, children appear much less likely to get sick if they contract the novel coronavirus. 
        However, the very young (less than 1 year) appear to be more vulnerable to serious illness than older children.''','''Researchers have found that the virus can live up to 24 hours on cardboard and 2 to 3 days on plastic and stainless steel.\n
        The CDC reports that the virus was detected on surfaces of the Diamond Princess cruise ship up to 17 days after passengers disembarked. \n However, only pieces of the virus were detectable, not viruses capable of infecting a person.''',"The CDC estimates up to 40% of infected individuals do not experience symptoms. ",'''People with type A blood 
        may be more susceptible to infection.''','''Some people never develop symptoms.
        And some people who had what they thought was a “bad cold” or the flu may have actually had COVID-19.''']
time.sleep(2)
covid=Covid()
list_of_countries=covid.list_countries()
while Y in "yY":
    N=randint(0,8)
    print("Before we begin Lets have a fact check")
    time.sleep(1.5)
    print(random_stuffs[N])
    time.sleep(2.2)
    list_of_countries=covid.list_countries()
    Assistance=input("Do you need assistance on the list of countries(Y/N):")
    if Assistance=="y" or Assistance=="Y":
        print(list_of_countries)
    country=input("Enter which country you want the covid cases report for:")
    time.sleep(1)
    cases=covid.get_status_by_country_name(country)
    for x in cases:
        print(x,":",cases[x])
        time.sleep(1)
    Y=input("Do you still want to continue(Y/N):")
    time.sleep(1)
    print("-"*80)
