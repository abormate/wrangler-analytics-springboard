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
// ------->> //     \w+\.com 

// END -- Lesson 51

// ----------------------------------------------------------------- //

// Lesson 52 -- Multi line global flag modifier
/*
Regex sees all text as one line. But we use the multiline flag to handle each line separately. 
In this way, the expressions we write to identify patterns at the end of lines work separately for 
each line. Now enable the multiline flag to find all matches.
*/

// sample line of text where regex will be applied on
//      domain.com
  //    test.com
  //    site.com

// actual regex input (works when multi-line is enabled and global is enabled too)
// -------->> // \w+\.com$ 

// END -- Lesson 52 

