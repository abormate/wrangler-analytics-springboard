// ------------------------------------------- // 
// 
// Regular Expressions -- 101 training
//
// ------------------------------------------- //

// Curly braces -- lesson 21
/*
instructions:

To express a certain number of occurrences of a character, at the end we write curly braces 
{n} along with how many times we want it to occur. For example, indicate that the following 
letter e can occur only 2 times.
*/

// text sample
/*
ber beer beeer beeeer
*/

// actual regex, following the briefing or instructions above

// ------>>> //     be{2}r 

// ------------------------------------------- //

// Curly braces - part 2 - lesson 22
/*
To express at least a certain number of occurrences of a character, immediately after the character 
we write at least how many times we want it to occur followed by a comma , and wrapped inside curly 
braces {n, }. For example, indicate that the following letter e can occur at least 3 times.
*/

// sample text -- tester
// ber beer beeer beeeer

// actual regex
// -------->>>> //     be{3,}r

// ------------------------------------------ // 

// Curly braces - part 3 - lesson 23
/*
To express the occurrence of a character in a certain number range, we write curly braces {x,y} 
with the interval we want to go to the end. For example, indicate that the following letter e can 
only occur between 1 and 3.
*/

// sample text -- tester, line of text where search pattern is applied to
// ber beer beeer beeeer

// actual regex 
// --------->>> //    be{1,3}r

// ------------------------------------------ //

// Practice run for regular expressions
// asterisk (*)

/*
Use the asterisk * to write the expression that will select each word, suitable for the 
absence of the letter e in the text and the presence of one or more.
*/

// sample text -- to apply regex on this line of text
// dp dep deep

// regular expressions actual 
// --------->>> //     de*p

// ------------------------------------------ // 

// practice: plus sign (+)
// plus sign (+)

/*
Write the expression using the plus sign + to select words in which the letter e occurs one or 
more times in the text.
*/

// sample text -- line of text where regex will be applied to
// dp dep deep

// actual regular expression
// ---------->>> //      de+p

// ------------------------------------------ //

