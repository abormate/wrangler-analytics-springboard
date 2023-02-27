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


// Lesson 8 -- Negated character sets [^abc]
/*
We use the negated character sets [^] to denote characters we don't want to be included. 
The characters we do not want to be included are written in square brackets with a caret at the beginning. 
Below are both http and https. Since http occurs in both, it will also choose https. 
Type [^s] after the letter p to exclude the letter s.
*/

// workspace -- multi lines of text for application of our regex input
/*
1. http://testdomain.com
2. https://testdomain.com
*/

// actual regex input
// --------->> //      http[^s].*

// Output
// matches only http (without the "s" letter) --> http://testdomain.com

// END -- Lesson 8

// ------------------------------------- //


// Lesson 9 -- Caret ^ -- beginning
/*
Let's say we have a list of URLs, and we want to find only those URLs that start with http. 
But URLs also contain http in different parts other than their beginning. So add a caret ^ to the 
beginning of the following expression to filter out only those starting with http.
*/

// workspace -- multi lines of text to apply our regex input
/*
http://www.google.com/search?q=https
https://developer.mozilla.org/en-US/docs/Glossary/http
http://httpstatus.io/
https://ahrefs.com/
*/

// actual regex input
// ---------->> //   ^http[^s].*

// output
// matches only http (without an "s") and those 2 lines from the workspace with only with http at the beginning 
// http://www.google.com/search?q=https
// http://httpstatus.io/ 

// END -- Lesson 9 

// ------------------------------------ //

// Lesson 10 -- Dollar Sign $ and Escape character \
/*
Since the period . is a special character that matches everything, we first need to disable 
the period before htm using the escape character \. This applies to all special characters.

Then add a $ sign to the end of the expression. This ensures that the text to be filtered ends 
with the expression written before it.
*/
// Again we have a list of URLs. We want to find only those URLs ending in .htm

// sample lines of text to apply our regex input to
/*
https://www.google.com/search?hl=en&q=html
https://testsite.com/learn-html.htm
https://developer.mozilla.org/en-US/docs/Web/html
https://learnhtmltestsite.com/learn.html
*/

// actual regex input
// ---------->> //    .*\.htm$

// output
// matches only the URL line that ends with ".htm"
// https://testsite.com/learn-html.htm

// END -- Lesson 10

// -------------------------------------- //

// Lesson 11 - Length Restrictions {n}
/*
We may want to filter the results by character lengths. For example, to filter URLs that are 
35 characters long, type the number you want to use for the length, {35}, using curly braces at 
the end of the period .
*/

// sample lines of text where our input regex will be applied to
/*
https://ahrefs.com/dashboard
https://ahrefs.com/site-explorer
https://ahrefs.com/keywords-explorer
https://ahrefs.com/site-audit
https://ahrefs.com/rank-tracker
https://ahrefs.com/content-explorer
*/

// actual regex input 
// ---------->> //      ^.{35}$

// output
// matches only the URL line that has exactly 35 characters to it
// https://ahrefs.com/content-explorer

// END -- Lesson 11

// ------------------------------------- // 

// Lesson 12 -- Length restrictions (maximum) {n,m}
/*
To filter URLs with a maximum length of 35 characters, type {1,35} the minimum and maximum number values 
we will use for the length, using curly braces at the end of the period .
*/

// workspace -- sample lines of text for regex input application
/*
https://ahrefs.com/dashboard
https://ahrefs.com/site-explorer
https://ahrefs.com/keywords-explorer
https://ahrefs.com/site-audit
https://ahrefs.com/rank-tracker
https://ahrefs.com/content-explorer
*/

// actual regex input
// ---------->> //    ^.{1,35}$

// output
// matches all lines of text that have between 1 to 35 characters comprising
// which are the following lines of text from the above workspace
/*
https://ahrefs.com/dashboard
https://ahrefs.com/site-explorer

https://ahrefs.com/site-audit
https://ahrefs.com/rank-tracker
https://ahrefs.com/content-explorer
*/

// END -- Lesson 12 

// ------------------------------------- //

// Lesson 13 - Length Restrictions (minimum) {n,}
/*
To filter URLs with a minimum length of 35 characters, type {35,} using curly braces at the end of the 
period and ending with a comma for the minimum number value we will use for the length.
*/

// workspace -- apply input regex to these lines of text
/*
https://ahrefs.com/dashboard
https://ahrefs.com/site-explorer
https://ahrefs.com/keywords-explorer
https://ahrefs.com/site-audit
https://ahrefs.com/rank-tracker
https://ahrefs.com/content-explorer
*/

// actual regex input
// ---------->> //     ^.{35,}$

// output
// matches only lines of text that have exactly a minimum of 35 characters
// which means, these lines of text 
/*


https://ahrefs.com/keywords-explorer


https://ahrefs.com/content-explorer
*/

// END -- Lesson 13

// ----------------------------------------- //

// Lesson 14 -- robots.txt (regex-like syntax)
/*
Here is an example of regex-like usage in the robots.txt file. The example states that bots should not 
crawl links with the extension pdf
*/

// sample lines of text to apply our regex input to
/*
User-agent: *
Disallow: /*.pdf$

----------

/about.html
/home.html
/document.pdf
/team.html
/introduction.pdf
*/

// actual regex input
// ---------->> //     /*.pdf$

// output 
// matches only page-path ending with .pdf

// END -- Lesson 14

// ------------------------------------------- //

// Lesson 15 -- .htaccess
/*
Here is an example of using regex in the .htaccess file. In the example, php extension links are 
directed to html extensions with 301 code
*/

// sample text for where our input regex will be applied to
/*
RewriteEngine On
RewriteCond %{REQUEST_URI} .php$
RewriteRule ^(.*).php$ /$1.html [R=301,L]

----------

/about.html
/home.html
/product/detail.php
/shop/12/buy.php
/profile.php
*/

// actual regex input
// ---------->> //      ^(.*).php$

// output
// selects only page-paths that end with .php

// END -- Lesson 15

// ------------------------------------------- //


