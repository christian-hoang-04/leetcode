Hint 2 

So, if we fix one of the numbers, say `x`, we have to scan the entire array to find the next number `y` which is `value - x` where value is the input parameter. Can we change our array somehow so that this search becomes faster?

How can we change our array somehow ? 
- sort -> we cannot do this because we need to correct index to be correct (I already tried this way). 

From [the suggestions from Gemini Pro](https://gemini.google.com/app/7946de3e35732a63), I am thinking about using Hash Table (heard about it before but never dig deep into it). 

And maybe the tuples solution, where I can keep the number and their indexes to still use the sort solution. 