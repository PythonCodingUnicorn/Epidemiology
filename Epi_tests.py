import math


# unversity Epidemiology class



print ("------------ EPIDEMIOLOGY --------------\n")

#--------------------------------------------------------------- population point prevalence
def divide(a,b):
	if b==0:
		print "enter a value greater than 0"
	else:
		return float(a)/b
#--------------
print (" [Population] point Prevalence rate ")
a = float(raw_input(" Enter value for people WITH disease: "))
b = float(raw_input(" Enter value for total population: " ))
prevalence = divide(a,b)
print (" Population Prevalence rate is: ",round(prevalence,4))
#------------------------------------------------


			
#----------------------------------------------------------------- disease test screenings

print "\n----- screen sensitivity ------- "
A = float(raw_input("Enter value for screen(+) AND diseased: "))
B = float(raw_input("Enter value for screen(+) AND no disease: "))
C = float(raw_input("Enter value for screen(-) AND disease: "))
D = float(raw_input("Enter value for screen(-) AND no disease: "))

screen_pos_total =(A+B)
screen_neg_total =(C+D)

diseased_total = (A+C)
non_diseased_total = (B+D)

''' screen totals
   ------------------
   | A (+) || B (+) |
   -----------------
   | C (-) || D (-) |
   ------------------
'''

#---------------------------------------------------------------- probability of test results

print "------- probability of test results -------\n"

#--------------------------------------------- test positive AND disease
pos_AND_diseased = ((A)/diseased_total)

print ("Probability of positive test result, given affected by disease is: ",\
       round(pos_AND_diseased,4), "or",(round(pos_AND_diseased,3)*100),"%"))
#---------------------------------------------

#--------------------------------------------- test negative and not diseased
neg_AND_NOT_diseased = ((D)/non_diseased_total)

print ("Probability of negative test result, given not affected by disease is: ",\
       round(neg_AND_NOT_diseased,4),"or",(round(neg_AND_NOT_diseased,3)*100),"%"))
#---------------------------------------------

#---------------------------------------------- test positive and not diseased
pos_AND_NOT_diseased = ((B)/non_diseased_total)

print ("Probability of false (+) test result, given not affected by disease is: ",\
       round(pos_AND_NOT_diseased,4),"or",(round(pos_AND_NOT_diseased,3)*100),"%")
#----------------------------------------------

#---------------------------------------------- test negative and diseased
neg_AND_diseased = ((C)/diseased_total)

print ("Probability of false (-) test result, given affected by disease is: ",\
       round(neg_AND_diseased,4),"or",(round(neg_AND_diseased,3)*100),"%")
#------------------------------------------------


#---------------------------------------------------------------------- predictive values
print "\n .......... The Predictive value .............."

#--------------------------------------------- diseased given tested positive
diseased_given_pos = ((A)/screen_pos_total)

print ("Probability of having disease given positive test result is: ",\
       round(diseased_given_pos,4),"or",(round(diseased_given_pos,3)*100),"%")
#---------------------------------------------

#---------------------------------------------- not diseased given tested negative
not_diseased_given_neg = ((D)/screen_neg_total)

print ("Probability of not having disease given negative test result is: ",\
       round(not_diseased_given_neg,4),"or",(round(not_diseased_given_neg,3)*100),"%")
#-----------------------------------------------


##########>>> Prevalence of disease <<<#########
prevalence = ((diseased_total)/(diseased_total + non_diseased_total))

print (" Prevalence of disease is: ",round(prevalence,4),\
       "or",(round(prevalence,3)*1000),"per 1000 people")
#----------------------------------------









