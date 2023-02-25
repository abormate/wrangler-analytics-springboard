// Lesson 46 -- positive lookaround (?=)
/*
For example, we want to select the hour value in the text. Therefore, to select only the numerical 
values that have PM after them, we need to write the positive look-ahead expression (?=) after 
our expression. Include PM after the = sign inside the parentheses.
*/

// sample line of text for regex to evaluate
//   Date: 4 Aug 3PM

// actual regex -- input
// -------->> //   \d+(?=PM)

// END -- Lesson 46 

// ------------------------------------ //

// Lesson 47 -- negative lookahead (?!)
/*
For example, we want to select numbers other than the hour value in the text. Therefore, we need 
to write the negative look-ahead (?!) expression after our expression to select only the numerical 
values that do not have PM after them. Include PM after the ! sign inside the parentheses.
*/

// sample line to evaluate input regex on
// Date: 4 Aug 3PM

// actual regex input
// ------->> //     \d+(?!PM)

// END -- Lesson 47

// ------------------------------------ //

// Lesson 48 -- positive lookbehind (?<=)
/*
For example, we want to select the price value in the text. Therefore, to select only the number 
values that are preceded by $, we need to write the positive lookbehind expression (?<=) before our 
expression. Add \$ after the = sign inside the parenthesis.

--> Note: Regex in this lesson step is not supported with some browsers <-- Note.
*/

// sample line of text to evaluate regex input with
//  Product Code: 1064 Price: $5

// actual regex input
// ------->> //   (?<=\$)\d+

// END -- Lesson 48

// ------------------------------------ //

// Lesson 49 -- Negative lookbehind (?<!)
/*
For example, we want to select numbers in the text other than the price value. Therefore, to select 
only numeric values that are not preceded by $, we need to write the negative lookbehind (?<!) before 
our expression. Add \$ after the ! inside the parenthesis.
*/

// sample line of text to evaluate our regex input
// Product Code: 1064 Price: $5

// regex input actual 
// ------->> //    (?<!\$)\d+

// END -- Lesson 49

// ------------------------------------ //





