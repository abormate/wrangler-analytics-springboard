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
// practice 001: asterisk (*)

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
// practice 002: plus sign (+)

/*
Write the expression using the plus sign + to select words in which the letter e occurs one or 
more times in the text.
*/

// sample text -- line of text where regex will be applied to
// dp dep deep

// actual regular expression
// ---------->>> //      de+p

// ------------------------------------------ //

// lesson 27: question mark (?)
// practice 003: question mark (?) with regular expressions

/*
Write the expression indicating that the letter n is optional in the text, using the question mark ?.
Thus, both the words a and an can be selected.
*/

// sample text -- where regular expression where will be applied to
//  a, an

// actual regex 
// ---------->>> //   an?

// ------------------------------------------ //

// lesson 28: curly braces -- 01
// practice 004: curly braces -- digit number specifier

/*
Write the expression using curly braces {} that will find texts containing 4 numbers side by side. 
Remember that the range [0-9] will match a single digit.
*/

// sample text -- where regex will be applied to
// Release 10/9/2021

// actual regex
// --------->>> //    [0-9]{4}

// ------------------------------------------ //

// lesson 29: curly-braces -- 02
// practice 005: curly braces 02 -- comma delimiter

/*
Write the expression using curly braces {} that will find texts containing at least 
2 numbers side by side.
*/

// sample text -- where regex search pattern will be applied to
// Release 10/9/2021

// actual regex 
// --------->>> //     [0-9]{2,}

// ------------------------------------------- //

// lesson 30: curly-braces -- 03
// practice 006: curly braces -- inner range with comma

/*
Write the expression using curly braces {} that will find texts containing at least 1 and at 
most 4 numbers side by side.
*/

// sample text -- where regex search pattern will be applied to
// Release 10/9/2021

// actual regex 
// ---------->>> //     [0-9]{1,4}

// ------------------------------------------- //

// lesson 32: parentheses grouping
/*
We can group an expression and use these groups to reference or enforce some rules. 
To group an expression, we enclose () in parentheses. For now just group haa below.
*/

// sample text for evaluating regex input
//  ha-ha,haa-haa

// actual regex -- for input
// ----------->> //      (haa)

// END -- Lesson 32

// ------------------------------------------- //

// lesson 33: referencing a group 
/*
The words ha and haa are grouped below. The first group is used by writing \1 to avoid rewriting. 
Here 1 denotes the order of grouping. Type \2 at the end of the expression to refer to the second group.
*/

// sample line of text for evaluation 
// ha-ha,haa-haa

// actual regular expression input following
// ----------->> //      (ha)-\1,(haa)-\2

// END -- Lesson 33

// ------------------------------------------- //

// Lesson 34: Parentheses - Non-capturing Grouping
/*
You can group an expression and ensure that it is not captured by references. For example, 
below are two groups. However, the first group reference we denote with \1 actually indicates 
the second group, as the first is a non-capturing group.
*/

// sample line of text for evaluation
// ha-ha,haa-haa

// actual regular expression input following
// --------->> //     (?:ha)-ha,(haa)-\1

// END -- Lesson 34

// -------------------------------------------- //

