# record-locator

An airline style record locator generator. 

This generates a random string of alphanumeric characters that are be used 
as a unique identifer for tickets (for example). 

This currently attempts to generate 'safe' strings, by attempting the following:

* Removing vowels from the alphabet (as profanity avoidance)
* Removing the use of characters that (in poor fonts) maybe confusing: B, 8, 5, S, 0, O, 1, I, Q
