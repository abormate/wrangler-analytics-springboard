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

// Lesson 35: Pipe character |
/*
It allows to specify that an expression can be in different expressions. Thus, all possible statements 
are written separated by the pipe sign |. This differs from charset [abc], charsets operate at the 
character level. Alternatives are at the expression level. For example, the following expression would 
select both cat and rat. Add another pipe sign | to the end of the expression and type dog so that all 
words are selected.
*/

// sample line of text for regex evaluation
// cat rat dog

// actual regex input
// --------->> //    (c|r)at|dog

// END -- Lesson 35

// -------------------------------------------- //

// Lesson 36: Escape character \
/*
There are special characters that we use when writing regex. { } [ ] / \ + * . $^ | ? 
Before we can select these characters themselves, we need to use an escape character \. 
For example, to select the dot . and asterisk * characters in the text, let's add an escape character \ 
before it.
*/

// sample line of text for evaluating regex input
// (*) Asterisk.

// actual regex input
// --------->> //   (\*|\.)

// END -- Lesson 36

// ------------------------------------------- //

// Lesson 37: Caret sign ^
// Selecting the start only of a line

/*
We were using [0-9] to find numbers. To find only numbers at the beginning of a line, prefix this 
expression with the ^ sign.
*/

// sample multi-line of text to evaluate regex input
/*
Basic Omellette Recipe

1. 3 eggs, beaten
2. 1 tsp sunflower oil
3. 1 tsp butter
*/

// actual regex input
// -------->> //       ^[0-9]

// END -- Lesson 37

// ------------------------------------------ //

// Lesson 38: Dollar Sign $
// Selecting only the end of the line

/*
Let's use the $ sign after the html value to find the html texts only at the end of the line.
*/

/*
Multi-line of sample text to evaluate with regex input:

https://domain.com/what-is-html.html
https://otherdomain.com/html-elements
https://website.com/html5-features.html
*/

// actual regex to input and process
// -------->> //       html$

// END -- Lesson 38

// ----------------------------------------- //

// Lesson 39: Word Character \w -- selects only letters, numbers and underscore

// learn and instructions
/*
The expression \w is used to find letters, numbers and underscore characters. Let's use the 
expression \w to find word characters in the text.
*/

// sample line of text for evaluation where input will be passed.
// abcABC123 _.:!?

// actual regex -- input
// ------->> //     \w

// END -- Lesson 39

// ----------------------------------------- //

// Lesson 40: Except Word Character \W (capital w) -- selects only symbols

// learn and instructions
/*
The expression \W is used to find characters other than letters, numbers, and underscores.
*/

// sample line of text for evaluation
// abcABC123 _.:!?

// actual regex input
// --------->> //      \W

// END -- Lesson 40

// ------------------------------------------ //

// Lesson 41: Number characters \d
/*
\d is used to find only number characters.
*/

// sample line of text for evaluation of regular expression input
// abcABC123 .:!?

// actual regular expression input
// -------->> //     \d

// END -- Lesson 41

// ------------------------------------------ //

// Lesson 42: Except Number character \D
/*
\D is used to find non-numeric characters.
*/

// sample line of text for regex evaluation
// abcABC123 .:!?

// actual regex input
// ------->> //       \D

// END -- Lesson 42

// ------------------------------------------ //

// Lesson 43: Space character \s
/*
\s is used to find only space characters.
*/

// sample line of text to evaluate with regex input 
//  abcABC123 .:!?

// actual regex input 
// -------->> //      \s

// ----------------------------------------- //

