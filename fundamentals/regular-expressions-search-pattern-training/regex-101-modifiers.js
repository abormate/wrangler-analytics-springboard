/*
"Flags" -- or Modifiers
Flags change the output of the expression. That's why flags are also called modifiers. 
Flags determine whether the typed expression treats text as separate lines, is case sensitive, 
or finds all matches. Continue to the next step to learn the flags.
*/

// ----------------------------------------------------------------- //

// Lesson 51 -- global flag
/*
The global flag causes the expression to select all matches. If not used it will only select the 
first match. Now enable the global flag to be able to select all matches.
*/

// sample line of text to evaluate our regex input on
// domain.com, test.com, site.com

// actual regex input -- it passes when we enable "global" -- ctrl+g
// ------->> // *enable global mode* + this regex instruction ==>       \w+\.com 

// END -- Lesson 51

// ----------------------------------------------------------------- //

// Lesson 52 -- Multi line global flag modifier
/*
Regex sees all text as one line. But we use the multiline flag to handle each line separately. 
In this way, the expressions we write to identify patterns at the end of lines work separately for 
each line. Now enable the multiline flag to find all matches.
*/

// sample lines of text where regex will be applied on
//      domain.com
  //    test.com
  //    site.com

// actual regex input (works when multi-line is enabled and global is enabled too)
// -------->> // *enable multi-line mode along with global* + this regex ==>           \w+\.com$ 

// END -- Lesson 52 

// ----------------------------------------------------------------- //

// Lesson 53 -- Case-insensitive flag modifier
/*
In order to remove the case-sensitivity of the expression we have written, we must 
activate the case-insensitive flag.
*/

// sample lines of text where our regex input will be applied on
// DOMAIN.COM
// TEST.COM
// SITE.COM

// actual regex input
// -------->> // *enable case insensitive* + this regex instruction ==>    \w+\.com$

// END -- Lesson 53 

// ----------------------------------------------------------------- //

// Lesson 54 -- "greedy" match
/*
Regex does a greedy match by default. This means that the matchmaking will be as long as possible. 
Check out the example below. It refers to any match that ends in r and can be any character preceded 
by it. But it does not stop at the first letter r.
*/

// sample line of text where our regex input will search patterns for 
// ber beer beeer beeeer

// actual regex input
// ------>> //         .*r

// END -- Lesson 54

// ---------------------------------------------------------------- //

// Lesson 55 -- "lazy" match
/*
Lazy matchmaking, unlike greedy matching, stops at the first matching. For example, in the example 
below, add a ? after * to find the first match that ends with the letter r and is preceded by 
any character. It means that this match will stop at the first letter r.
*/

// line of text to match with our regex input
// ber beer beeer beeeer

// actual regex input 
// ------->> //           .*?r

// END -- Lesson 55 

