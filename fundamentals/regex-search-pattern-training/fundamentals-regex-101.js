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
// ------>>>> //     be{3,}r

// ----------------------------------------- // 




