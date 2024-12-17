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

### Day 6

First part, just check the rules as stated.

Secord part, slow brute force solution, just put a obstanble in each possible place and check if it creates a loop.

### Day 7

First part, brute force it.

Secord part, also brute force it.

### Day 8

First part, this one was hard to grasp but relatively easy to implement. Given 2 points you can get the difference in each axe and we call that `dx` and `dy` and then you can generate 2 collinear points, check if those are within the grid and add them to a set. The result will be set size.

Secord part, almost like part 1 the only difference is that once you find a collinear point you want to generate all multiples of that point within the grid and don't forget to add all the antenas to the set to get the right number.

### Day 9

First part, I keep 2 pointers left and right, and I build a state machine that computes the hash on the fly. I forgot to compute the remaining! But that was easy to fix.

Second part, I forgot about memory and I build a list just like in the example, for this one I build 2 indexes one to keep the position and size of the file base on the id and the other one to keep track of the free spaces. I had to update the free index once I moved the file.

### Day 10

First part, for each 0 in the grid just count the amount of 9s that you can reach using dfs or bfs just make sure that the neighbors are consecutive numbers.

Second part, for each 0 calculate the rate and add it, to calculate the rate make another grid to keep track the number of paths up to that level, then do a bfs by level and update the number of paths in the new grid, once you finish the process check each element in the grid and if it's 9 sum the value in the rate grid.

### Day 11

Don't let the description fool you, the sequence part is not needed, you can use a dictionary and count the frequency and at the end of all the iterations all you have to do is to sum all frequencies.

### Day 12

First part, there is not a lot to think of, for each region just count the area and sum the perimeter.

Second part, I tried to solve this one without looking at other solutions and I failed, I even got a solution that passed all the examples and even more examples but failed in the large input then after looking at the comments in reddit I found that the numbers of sides is the same in this case as the number of corners and you can have 2 kind of corners, external and internal. After implementing that I finally got the right answer.

### Day 13

It's only a system of equations with 2 variables, if the solution is not an integer then it's not a valid solution.

### Day 14

For the first part, just brute force it.

For the second part, I had to use pygame and see if there was a pattern after several runs it turns out that the christmast tree is surrounded by robots so this made the search much more easier.

### Day 15

Just implement the rules, there is not a lot to add.

### Day 16

I just brute force it with bfs


### Day 17

For the first part it was just to implement this state machine and keep track of the output.

For the second part I wasn't able to get it done with brute force, I gave up after I exahusted the 32-bit space.
Then I look at other approaches and I settle for a simple dfs, I think the hardest part was to compare the right value for that to recurse.