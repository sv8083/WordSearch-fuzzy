# WordSearch-
Python app using Django framework that exposes a single endpoint and response returns a JSON array containing upto 25 results ranked.

Given A	dataset that	contains	333,333	English	words	and	the	frequency	of	their	usage	in	some	corpus.	
This a	web	app	where	the	user	types	in	a	single	word	from	this	list	in	a	
search	box.	and get autocomplete	feature	in	the	search	box.
Web framework that	exposes	a	single	
endpoint:
GET	/search?word=<input>
where	input	is	the	(partial)	word	that	the	user	has	typed	so	far.	For	example,	if	the	user	is	looking	
up	procrastination,	the	service	might	receive	this	sequence	of	requests:
                           GET	/search?word=pro
                           GET	/search?word=procr
                           GET	/search?word=procra

The	response	should	be	a	JSON	array	containing	upto	25	results,	ranked	by	some	criteria	(see	
below).
Constraints

  1. Matches	can	occur	anywhere	in	the	string,	not	just	at	the	beginning.	For	example,	eryx	
    should	match	archaeopteryx	(among	others).
  2. The	ranking	of	results	should	satisfy	the	following:
      a. We	assume	that	the	user	is	typing	the	beginning	of	the	word.	Thus,	matches	at	the	
      start	of	a	word	should	be	ranked	higher.	For	example,	for	the	input	pract,	the	result	
      practical	should	be	ranked	higher	than	impractical.
      b. Common	words	(those	with	a	higher	usage	count)	should	rank	higher	than	rare	
      words.
      c. Short	words	should	rank	higher	than	long	words.	For	example,	given	the	input	
      environ,	the	result	environment	should	rank	higher	than	environmentalism.
          i. As	a	corollary	to the	above,	an	exact	match should	always	be	ranked	as	the	
              first	result.
