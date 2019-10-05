# WordSearch-fuzzy
Python app using Django framework
Search for Words and it auto-completes the list
Optionally hit 
/search?word=
to get a list of words matching the given query, based on conditions below:

a. We assume that the user is typing the beginning of the word. Thus, matches at the start of a word should be ranked higher. For example, for the input pract, the result practical should be ranked higher than impractical. 
b. Common words (those with a higher usage count) should rank higher than rare words. 
c. Short words should rank higher than long words. For example, given the input environ, the result environment should rank higher than environmentalism.
