# Advent of Code 2024

### Day 1

For the first part just sort and zip.  
For the second part use a dict and count the elements.

### Day 2

For the first part, implement the rules and check that.  
For the second part, again just implement the rules, don't try to optimize or anything.

### Day 3

First part, use re.findall  
Second part, use re.findall and a flag

### Day 4

First part, for each point i,j generate all combinations and count, don't forget that you are counting twice in this approach  
Second part, for each point just get the diagonals and check if both are MAS or SAM

### Day 5

First part, build an `rule_index` then for each pair `a[i], a[i+1]` check if a rule exists, if all pairs get passes the rule check then it's a valid order, then just get the middle element and sum it.  
Second part, to fix the order just implement a sorting algorithm and use the `rule_index` to check if you should swap it or not.