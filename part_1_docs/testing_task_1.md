### Testing task 1:

# Carry out static testing on the code below.
# Comment on any errors that you see below.

Note that we are only looking for errors here.

**Not** any issues with, i.e.: 
Thinking that methods should be renamed or should be class level, or using string interpolation etc. 

These aren't errors but rather standards that vary from developer to developer. 

Only comment on errors that would stop the tests running.

```python

class CardGame:
  # missing parameters to pass arguments in as to create a CardGame class

  # missing an __init__ method to initialise the arguments passed in to the CardGame class


  def check_for_ace(self, card):
    if card.value = 1:
      # the above line should have a double == to show that it means you are checking for equality rather than setting card.value to 1
      return True
    else
    # the else line should end with a semicolon
      return False
   

  dif highest_card(self, card1 card2):
  # the above line has a misspelling of the def keyword and is missing a comma between card1 and card2
  if card1.value > card2.value:
    return card
    # the above line should be indented and return card1.value rather than card
  else:
    return card2
    # the above line should be indented and return card2.value rather than card2
  

# the whole function needs indented to be contained within the CardGame class
def cards_total(self, cards):
  total
  # when declaring a variable it must be set to something
  for card in cards:
    total += card.value
    return "You have a total of" + total
    # to add total to the returned string, it must first be converted into a string and a space should be added at the end of the string
    # the final line must also be tabbed in to sit at the same indent as the for loop, otherwise this will return the string after only having completed one iteration of the for loop
  
```
