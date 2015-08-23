# Class Two Homework!

**Look at the head and the tail of chipotle.tsv in the data subdirectory of this repo. Think for a minute about how the data is structured. What do you think each column means? What do you think each row means.
Tell me! (If you're unsure, look at more of the file contents.)**

Column contents are: 
* order_id -> and order that constitutes one payment event
* quantity -> how many of that thing (in that row) is ordered
* item_name -> name of the thing ordered on that row
* choice_description -> what additional things were requested to put on the thing in that row
* item_price -> the total cost of the thing in that row. 

**How many orders do there appear to be?**

* using `tail chipotle.tsv` I can see there are 1834 orders (payments) in this dataset.

**How many lines are in this file?**

* using `wc -l chiptotle.tsv` I can see there are 4623 lines.

**Which burrito is more popular, steak or chicken?**

* `grep -e 'chicken burrito' -i chipotle.tsv | wc -l`  returns `553`
* `grep -e 'steak burrito' -i chipotle.tsv | wc -l` returns `368`

Therefore, chicken burritos are more popular than steak. Bizarre!

**Do chicken burritos more often have black beans or pinto beans?**

* `grep -e 'chicken burrito.*pinto beans' chipotle.tsv | wc -l` returns 105
* `grep -e 'chicken burrito.*black beans' chipotle.tsv | wc -l` returns 282

Therefore, black beans are more popular than pinto beans in chicken burritos. 

**Make a list of all of the CSV or TSV files in the DAT8 repo (using a single command). Think about how wildcard characters can help you with this task.**

* `find . -name *.?sv`
./data/airlines.csv
./data/chipotle.tsv
./data/sms.tsv

**Count the approximate number of occurrences of the word "dictionary" (rgardless of case) across all files in the DAT8 repo.**

* `grep -rl "dictionary" .`
./code/00_python_intermediate_workshop.py
./data/sms.tsv
./homework/02_command_line_chipotle.md
./project/README.md
./README.md

Was not able to figure out how to print the number of __times__ the word appeared altogether, so this is just a list of the files that the word appears in. 

Or a count:

`grep -rl "dictionary" .  |  wc `
5       5     128

But 128 characters doesn't make sense, so who knows...

**Optional: Use the the command line to discover something "interesting" about the Chipotle data. Try using the commands from the "advanced" section!**

`wc -l chipotle.tsv `
4623 chipotle.tsv

`uniq chipotle.tsv | wc -l`
4589

Of the 4623 lines of orders, the vast majority of those are unique.
