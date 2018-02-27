
a = "THIS IS A STRING"
b = "THIS IS ALSO A STRING"
################################################
# notice - '+' is an operator, as is '='       #
#     '=' still means 'is assigned'            #
#     '+' does not been addition any more!     #
#         now it means "cancatenate" or        #
#                   "string together"          #
################################################
c = a + " & " + b

print (a)
print (b)
print (c)

# 
# I could have also concatenated 3 string variables:
#

d = " & (that is 'and') "
e = a + d + c
print (e)

#
# and to introduce a few other characters...
#

print ("THIS IS ONE THING")
print ("\tTHIS IS ANOTHER THING")
print ("\tTHIS IS \n\t\tYET ANOTHER THING")
print ("\t\t\tAND FINALLY, INTERESTINGLY ENOUGH, THIS IS STILL SOMETHING\rELSE.")
