Exercise: Tuples and Sets
1.	Unique Usernames
Write a program that reads from the console a sequence of N usernames and keeps a collection only of the unique ones. On the first line, you will receive an integer N. On the next N lines, you will receive a username. Print the collection on the console (the order does not matter):
Examples

Input
6
George
George
George
Peter
George
NiceGuy1234

Output
George
Peter
NiceGuy1234

2.	Sets of Elements
Write a program that prints a set of elements. On the first line, you will receive two numbers - n and m, which represent the lengths of two separate sets. On the next n + m lines you will receive n numbers, which are the numbers in the first set, and m numbers, which are in the second set. Find all the unique elements that appear in both and print them on separate lines (the order does not matter).
For example:
Set with length n = 4: {1, 3, 5, 7}
Set with length m = 3: {3, 4, 5}
Set that contains all the elements that repeat in both sets -> {3, 5}
Examples

Input
4 3
1
3
5
7
3
4
5	

Output
3
5

Input
2 2
1
3
1
5	

Output
1

3.	Periodic Table
Write a program that keeps all the unique chemical elements. On the first line you will be given a number n - the count of input lines that you are going to receive. On the next n lines, you will be receiving chemical compounds, separated by a single space. Your task is to print all the unique ones on separate lines (order does not matter):
Examples

Input
4
Ce O
Mo O Ce
Ee
Mo	

Output
Ce
Ee
Mo
O

Input
3
Ge Ch O Ne
Nb Mo Tc
O Ne	

Output
Ch
Ge
Mo
Nb
Ne
O
Tc

4.	Count Symbols
Write a program that reads a text from the console and counts the occurrences of each character in it. Print the results in alphabetical (lexicographical) order.  
Examples

Input
SoftUni rocks

Output
: 1 time/s
S: 1 time/s
U: 1 time/s
c: 1 time/s
f: 1 time/s
i: 1 time/s
k: 1 time/s
n: 1 time/s
o: 2 time/s
r: 1 time/s
s: 1 time/s
t: 1 time/s

5.	Phonebook
Write a program that receives info from the console about people and their phone numbers.
Each entry should have a name and a number (both strings) separated by a "-". If you receive a name that already exists in the phonebook, update its number.
After filling the phonebook, you will receive a number – N. Your program should be able to perform a search of a contact by name and print its details in format "{name} -> {number}". In case the contact isn't found, print "Contact {name} does not exist."
Examples
Input
Adam-0888080808
2
Mery

Output
Adam	Contact Mery does not exist.
Adam -> 0888080808

Input
Adam-+359888001122
Ralf-666
George-5559393
Silvester-02/987665544
4
Silvester
silvester
Rolf

Output
Ralf	Silvester -> 02/987665544
Contact silvester does not exist.
Contact Rolf does not exist.
Ralf -> 666

6.	Longest Intersection
Write a program that finds the longest intersection. You will be given a number N. On the next N lines you will be given two ranges in the format: "{first start},{first end}-{second start},{second end}". Find the intersection of these two ranges and save the longest one of all N intersections. At the end print the numbers that are included in the longest intersection and its length in the format: "Longest intersection is [{longest intersection}] with length {length longest intersection}"
Note: in each range, there will always be intersection. If there are two equal intersections, print the first one.

Examples
Input
3
0,3-1,2
2,10-3,5
6,15-3,10

Output
Longest intersection is [6, 7, 8, 9, 10] with length 5	

Input
5
0,10-2,5
3,8-1,7
1,8-2,4
4,7-2,5
1,10-2,11

Output
Longest intersection is [2, 3, 4, 5, 6, 7, 8, 9, 10] with length 9	


7.	Battle of Names
You will receive a number N. On the next N lines, you will be receiving names. You must sum the ascii values of each letter in the name and integer divide it to the number of the current row (starting from 1). Save the result to a set of either odd or even numbers, depending on if the devised number is an odd or even. After that, sum the values of each set.
•	If the sums of the two sets are equal, print the union values, separated by ", ". 
•	If the sum of the odd numbers is bigger than the sum of the even numbers, print the different values, separated by ", ".
•	If the sum of the even numbers is bigger than the sum of the odd numbers, print the symmetric different values, separated by ", ".
NOTE: On every operation, the starting set should be the odd set
Examples

Input
4
Pesho
Stefan
Stamat
Gosho	

Output
304, 128, 206, 511

Input
6
Preslav
Gosho
Ivan
Stamat
Pesho
Stefan	

Output
733, 101	
