[View Raw for best view of input and outputs]

------------------------------------------------------------------------------------------------------
quora.py; Problem Description:
Quora uses a combination of machine learning (ML) algorithms and moderation to ensure high-quality content on the site. High answer quality has helped Quora distinguish itself from other Q&A sites on the web.  

Your task will be to devise a classifier that is able to tell good answers from bad answers, as well as humans can.  A good answer is denoted by a +1 in our system, and a bad answer is denoted by a -1.

Input Format:

The first line contains N, M. N = Number of training data records, M = number of parameters. Followed by N lines containing records of training data. Then one integer q, q = number of records to be classified, followed by q lines of query data
Training data corresponds to the following format:
(:)*

Query data corresponds to the following format:
(:)*

The answer identifier  is an alphanumeric string of no more than 10 chars.  Each identifier is guaranteed unique.  All feature values are doubles.

The data is extracted from real production data, and thus will not include the raw form of the answers. We, however, have extracted as many features as we think are useful, and you can decide which features make sense to be included in your final algorithm. The actual labelling of a good answer and bad answer is done organically on our site, through both human moderators as well as our own classifier.

Output Format:

For each query, you should output q lines to stdout, representing the decision made by your classifier, whether each answer is good or not:
Constraints:

0 0 0 
Sample Input:

5 23
2LuzC +1 1:2101216030446 2:1.807711 3:1 4:4.262680 5:4.488636 6:87.000000 7:0.000000 8:0.000000 9:0 10:0 11:3.891820 12:0 13:1 14:0 15:0 16:0 17:1 18:1 19:0 20:2 21:2.197225 22:0.000000 23:0.000000
LmnUc +1 1:99548723068 2:3.032810 3:1 4:2.772589 5:2.708050 6:0.000000 7:0.000000 8:0.000000 9:0 10:0 11:4.727388 12:5 13:1 14:0 15:0 16:1 17:1 18:0 19:0 20:9 21:2.833213 22:0.000000 23:0.000000
ZINTz -1 1:3030695193589 2:1.741764 3:1 4:2.708050 5:4.248495 6:0.000000 7:0.000000 8:0.000000 9:0 10:0 11:3.091042 12:1 13:1 14:0 15:0 16:0 17:1 18:1 19:0 20:5 21:2.564949 22:0.000000 23:0.000000
gX60q +1 1:2086220371355 2:1.774193 3:1 4:3.258097 5:3.784190 6:0.000000 7:0.000000 8:0.000000 9:0 10:0 11:3.258097 12:0 13:1 14:0 15:0 16:0 17:1 18:0 19:0 20:5 21:2.995732 22:0.000000 23:0.000000
5HG4U -1 1:352013287143 2:1.689824 3:1 4:0.000000 5:0.693147 6:0.000000 7:0.000000 8:0.000000 9:0 10:1 11:1.791759 12:0 13:1 14:1 15:0 16:1 17:0 18:0 19:0 20:4 21:2.197225 22:0.000000 23:0.000000
2
PdxMK 1:340674897225 2:1.744152 3:1 4:5.023881 5:7.042286 6:0.000000 7:0.000000 8:0.000000 9:0 10:0 11:3.367296 12:0 13:1 14:0 15:0 16:0 17:0 18:0 19:0 20:12 21:4.499810 22:0.000000 23:0.000000
ehZ0a 1:2090062840058 2:1.939101 3:1 4:3.258097 5:2.995732 6:75.000000 7:0.000000 8:0.000000 9:0 10:0 11:3.433987 12:0 13:1 14:0 15:0 16:1 17:0 18:0 19:0 20:3 21:2.639057 22:0.000000 23:0.000000

Sample Output:

PdxMK +1
ehZ0a -1
------------------------------------------------------------------------------------------------------
------------------------------------------------------------------------------------------------------

stocks.py; Problem Description

A time series of a stock's highest price during a trading day (at the New York Stock Exchange), is provided to you. In each test case, the day's highest prices is missing for certain days. By analyzing the data, try to identify the missing price for those particular days.

Input Format 
The first line contains an integer N, which is the number of rows of data to follow. 
This is followed by N rows of data, each of which contains a time-stamp in the first column and the day's highest price for the stock in the second column. There is a tab delimiter between the two columns of data. 
There are exactly twenty rows in each input file, where the day's highest price is missing. The missing prices are marked as "Missing_1", "Missing_2" .."Missing_20". These missing records have been randomly dispersed in the rows of data.

Output Format 
The output should contain exactly twenty rows, each containg your predicted value, for each of the missing values (Missing_1, Missing_2 ... Missing_20) in that order.

Sample Input

250
1/3/2012 16:00:00   Missing_1
1/4/2012 16:00:00   27.47
1/5/2012 16:00:00   27.728
1/6/2012 16:00:00   28.19
1/9/2012 16:00:00   28.1
1/10/2012 16:00:00  28.15
....
....
....
12/13/2012 16:00:00 27.52
12/14/2012 16:00:00 Missing_19
12/17/2012 16:00:00 27.215
12/18/2012 16:00:00 27.63
12/19/2012 16:00:00 27.73
12/20/2012 16:00:00 Missing_20
12/21/2012 16:00:00 27.49
12/24/2012 13:00:00 27.25
12/26/2012 16:00:00 27.2
12/27/2012 16:00:00 27.09
12/28/2012 16:00:00 26.9
12/31/2012 16:00:00 26.77

Sample Output

26.96
31.98
32.69
32.41
32.32
30.5
29.18
30.8
30.46
30.63
30.96
30.4
28.2
28.2
27.3
27.1666
27.58
26.82
27.13
27.68

------------------------------------------------------------------------------------------------------
------------------------------------------------------------------------------------------------------

grades.py;

This challenge is based on real school data of the CBSE Class 12 examination conducted in the year 2013. You are given the grades obtained by students with specific but popular combinations of subjects (and all these students had opted for Mathematics). Their grades in four subjects are known to you. However their grade in Mathematics (i.e, the fifth subject) is hidden.

The records provided to you are the grades obtained by students who had opted for the following combinations of subjects or courses and obtained a passing grade in each subject. The individual subjects in the data are: 
English, Physics, Chemistry, Mathematics, Computer Science, Biology, Physical Education, Economics, Accountancy and Business Studies.

The most dominant subject combinations, account for approximately 99% of the data are:

English, Physics, Chemistry, Mathematics, Computer Science    
English, Physics, Chemistry, Mathematics, Physical Education    
English, Physics, Chemistry, Mathematics, Economics    
English, Physics, Chemistry, Mathematics, Biology  
English, Economics, Accountancy, Mathematics, Business Studies   

Input Format

The first line will be an integer N. N lines follow each line being a valid JSON object. The following fields of raw data are given in json.

SerialNumber (Numeric): The identifier of the student record. This is provided just for identification purposes and does not have any direct use.  
English (numeric) : The grade (between 1 and 8) obtained in English. This will always be present.  
Three more numeric fields from among: Physics, Chemistry, ComputerScience, Hindi, Biology, PhysicalEducation, Economics, Accountancy, BusinessStudies.  
The input for each record has the grade for all subjects opted by a student, other than Mathematics which you have to predict as the answer.

Output Format

For each student record that is given as a JSON object, containing the grade obtained in four subjects, output the predicted grade in Mathematics (this will be a numeral between 1 and 8, both inclusive) in a newline.

------------------------------------------------------------------------------------------------------
------------------------------------------------------------------------------------------------------

battery.py; Problem Description

Fred is a very predictable man. For instance, when he uses his laptop, all he does is watch TV shows. He keeps on watching TV shows until his battery dies. Also, he is a very meticulous man, i.e. he pays great attention to minute details. He has been keeping logs of every time he charged his laptop, which includes how long he charged his laptop for and after that how long was he able to watch the TV. Now, Fred wants to use this log to predict how long will he be able to watch TV for when he starts so that he can plan his activities after watching his TV shows accordingly.

Challenge

You are given access to Fred’s laptop charging log by reading from the file “trainingdata.txt”. The training data file will consist of 100 lines, each with 2 comma-separated numbers.

The first number denotes the amount of time the laptop was charged.
The second number denotes the amount of time the battery lasted.
The training data file can be downloaded here (this will be the same training data used when your program is run). The input for each of the test cases will consist of exactly 1 number rounded to 2 decimal places. For each input, output 1 number: the amount of time you predict his battery will last.

Sample Input

1.50

Sample Output

3.00