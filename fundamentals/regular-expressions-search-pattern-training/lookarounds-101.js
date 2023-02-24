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

