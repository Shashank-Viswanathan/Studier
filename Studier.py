import random, time
print('\nStudier - v1.0')
definitions = dict()
terms_lst = list()
def create_terms(term,definition): #Creating the term cards
    definitions[term] = definition
    terms_lst.append(term)
new = True
while new:
    cntinu = input('\nWould you like to add another term? y/n:\t')
    if cntinu == 'y':
      new = True
      new_term = str(input('\nWhat is the term?\n\t'))
      new_definition = str(input('What is the definition?\n\t'))
      create_terms(new_term,new_definition)
    else:
       new = False
while True:
   question = random.randrange(0,len(terms_lst))
   print('\nWhat is '+ terms_lst[question] + '?')
   next = input('ENTER to reveal answer!')
   print('\n\t' + definitions[terms_lst[question]])
   time.sleep(3)
