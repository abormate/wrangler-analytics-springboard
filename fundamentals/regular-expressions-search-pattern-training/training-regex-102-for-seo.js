// ------------------------------------- //
//
// Regex 102 -- for Organic Online Marketing
//
// ------------------------------------- //

/*
Regex is a set of regular expressions frequently used in many fields, especially by people who want 
to increase their productivity. The advantages of using Regex for SEO are that it makes it easier 
to analyze big data and write richer filters.
*/


// ------------------------------------- //

// Lesson 2
// Use Cases
/*
You can use Regex for SEO on platforms such as Google Analytics, Google Data Studio, Google Sheets, 
Google Search Console, Ahrefs, Deepcrawl, Screaming Frog. It is also frequently used in .htaccess 
and robots.txt (regex-like syntax) files.
*/


// Sample lines of text to apply input regex with
/*
Google Analytics
Google Data Studio
Google Sheets
Google Search Console
Ahrefs
*/

// actual regex input 
// ---------->> //      ^Google

// END -- Lesson 2

// ------------------------------------- //

// Lesson 4 -- "Or" OR operator --> "pipe" |
/*
We use the Or operator | to filter out multiple expressions. For example, filter text containing seo 
and regex by writing the two words, separating them with the Or operator |
*/

// line of text where our regex input will be applied to
/*
regex
seo
regular expression
*/

// actual regex input
// ---------->> //      regex|seo

// END -- Lesson 4

// ------------------------------------- //

// Lesson 5 -- "Optional" operator ? -- question mark
/*
We use it to express that an expression or character is optional. For example, we want to filter text 
containing both http and https. We can use the Or operator | for this operation, but there is a 
better way for these two almost identical words.
*/

// workspace -- multiple lines of text where our input regex will be applied to
/*
what is http
what is https
what is html
*/

// In this example, the letter s is optional. Instead, add a question mark ? to the end of the letter s.

// actual regex input
// ---------->> //      https?

// END - Lesson 5

// --------------------------------------- //

// Lesson 6 - Anything .*
/*
In regex, the period . can match anything, including spaces. But this match is only for a single 
character where it is used. The asterisk character * means that the preceding item does not exist 
at all or occurs more than once in the text. When the two are used together, it means that there 
can be an element of unlimited length where used.
*/

/*
Below are various keywords. Add .* to the end of the regex to write the expression that starts 
with how to write and matches everything after it.
*/

// workspace -- multiple lines of text where input regex will be applied to
/*
how to write regex
how to write regexp
how to write book review
*/

// actual regex input
// ---------->> //     how to write .*

// END -- Lesson 6

// --------------------------------------- //

// Lesson 7 -- Contains
/*
To filter the text that contains the words or phrases we're looking for, we write the word we're 
looking for between our two phrases .* that match everything. For example, type .*buy.* to filter 
out what includes buy.
*/

// workspace -- multi lines of text where our input regex will be applied to
/*
what is regex?
i want to buy a boat
how to buy a new phone
*/

// actual regex input
// ---------->> //     .*buy.*

// output
// matches "i want to buy a boat" and "how to buy a new phone"

// END -- Lesson 7

// -------------------------------------- // 

