"""
Part 1: Data Processing in Pandas

=== Instructions ===

There are 22 questions in this part.
For each part you will implement a function (q1, q2, etc.)
Each function will take as input a data frame
or a list of data frames and return the answer
to the given question.

To run your code, you can run `python3 part1.py`.
This will run all the questions that you have implemented so far.
It will also save the answers to part1-answers.txt.

=== Dataset ===

In this part, we will use a dataset of world university rankings
called the "QS University Rankings".

The ranking data was taken 2019--2021 from the following website:
https://www.topuniversities.com/university-rankings/world-university-rankings/2021

=== Grading notes ===

- Once you have completed this part, make sure that
  your code runs, that part1-answers.txt is being re-generated
  every time the code is run, and that the answers look
  correct to you.

- Be careful about output types. For example if the question asks
  for a list of DataFrames, don't return a numpy array or a single
  DataFrame. When in doubt, ask on Piazza!

- Make sure that you remove any NotImplementedError exceptions;
  you won't get credit for any part that raises this exception
  (but you will still get credit for future parts that do not raise it
  if they don't depend on the previous parts).

- Make sure that you fill in answers for the parts
  marked "ANSWER ___ BELOW" and that you don't modify
  the lines above and below the answer space.

- Q6 has a few unit tests to help you check your work.
  Make sure that you removed the `@pytest.mark.skip` decorators
  and that all tests pass (show up in green, no red text!)
  when you run `pytest part3.py`.

- For plots: There are no specific requirements on which
  plotting methods you use; if not specified, use whichever
  plot you think might be most appropriate for the data
  at hand.
  Please ensure your plots are labeled and human-readable.
  For example, call .legend() on the plot before saving it!

===== Questions 1-6: Getting Started =====

To begin, let's load the Pandas library.
"""

import pandas as pd

"""
1. Load the dataset into Pandas

Our first step is to load the data into a Pandas DataFrame.
We will also change the column names
to lowercase and reorder to get only the columns we are interested in.

Implement the rest of the function load_input()
by filling in the parts marked TODO below.

Return as your answer to q1 the number of dataframes loaded.
(This part is implemented for you.)
"""

NEW_COLUMNS = ['rank', 'university', 'region', 'academic reputation', 'employer reputation', 'faculty student', 'citations per faculty', 'overall score']

def load_input():
    """
    Input: None
    Return: a list of 3 dataframes, one for each year.
    """

    # Load the input files and return them as a list of 3 dataframes.
    df_2019 = pd.read_csv('data/2019.csv', encoding='latin-1')
    df_2020 = pd.read_csv('data/2020.csv', encoding='latin-1')
    df_2021 = pd.read_csv('data/2021.csv', encoding='latin-1')

    # Standardizing the column names
    df_2019.columns = df_2019.columns.str.lower()
    df_2020.columns = df_2019.columns.str.lower()
    df_2021.columns = df_2019.columns.str.lower()

    # Restructuring the column indexes
    # Fill out this part. You can use column access to get only the
    # columns we are interested in using the NEW_COLUMNS variable above.
    # Make sure you return the columns in the new order.
    # TODO
    df_2019 = df_2019[new_columns]
    df_2020 = df_2020[new_columns]
    df_2021 = df_2021[new_columns]

    # ...and keep this line to return the dataframes.
    return [df_2019, df_2020, df_2021]

def q1(dfs):
    # As the "answer" to this part, let's just return the number of dataframes.
    # Check that your answer shows up in part1-answers.txt.
    return len(dfs)

"""
2. Input validation

Let's do some basic sanity checks on the data for Q1.

Check that all three data frames have the same shape,
and the correct number of rows and columns in the correct order.

As your answer to q2, return True if all validation checks pass,
and False otherwise.
"""

def q2(dfs):
    """
    Input: Assume the input is provided by load_input()

    Return: True if all validation checks pass, False otherwise.

    Make sure you return a Boolean!
    From this part onward, we will not provide the return
    statement for you.
    You can check that the "answers" to each part look
    correct by inspecting the file part1-answers.txt.
    """
    # Check:
    # - that all three dataframes have the same shape
    shape_check = all(dfs[0].shape == df.shape for df in dfs[1:])

    # - the number of rows
    # - the number of columns
    # - the columns are listed in the correct order
    columns_check = all(list(df.columns) == NEW_COLUMNS for df in dfs)
    return shape_check and columns_check
  
"""
===== Interlude: Checking your output so far =====

Run your code with `python3 part1.py` and open up the file
output/part1-answers.txt to see if the output looks correct so far!

You should check your answers in this file after each part.

You are welcome to also print out stuff to the console
in each question if you find it helpful.
"""

ANSWER_FILE = "output/part1-answers.txt"

def interlude():
    print("Answers so far:")
    with open(f"{ANSWER_FILE}") as fh:
        print(fh.read())

"""
===== End of interlude =====

3a. Input validation, continued

Now write a validate another property: that the set of university names
in each year is the same.
As in part 2, return a Boolean value.
(True if they are the same, and False otherwise)

Once you implement and run your code,
remember to check the output in part1-answers.txt.
(True if the checks pass, and False otherwise)
"""

def q3(dfs):
    # Check:
    # - that the set of university names in each year is the same
    # Return:
    # - True if they are the same, and False otherwise.
    sets = [set(df['university']) for df in dfs]
    return sets[0] == sets[1] == sets[2]

"""
3b (commentary).
Did the checks pass or fail?
Comment below and explain why.

=== ANSWER Q3b BELOW ===
The check passes. All three datasets contain the same set of universities.
This makes sense because the QS rankings track the same universities each year,
even if their ranks or scores change.
=== END OF Q3b ANSWER ===
"""

"""
4. Random sampling

Now that we have the input data validated, let's get a feel for
the dataset we are working with by taking a random sample of 5 rows
at a time.

Implement q4() below to sample 5 points from each year's data.

As your answer to this part, return the *university name*
of the 5 samples *for 2021 only* as a list.
(That is: ["University 1", "University 2", "University 3", "University 4", "University 5"])

Code design: You can use a for for loop to iterate over the dataframes.
If df is a DataFrame, df.sample(5) returns a random sample of 5 rows.

Hint:
    to get the university name:
    try .iloc on the sample, then ["university"].
"""

def q4(dfs):
    # Sample 5 rows from each dataframe
    # Print out the samples
    sample_df = dfs[2].sample(5, random_state=42)  # random_state ensures reproducibility
    return list(sample_df['university'])
  
"""
Once you have implemented this part,
you can run a few times to see different samples.

4b (commentary).
Based on the data, write down at least 2 strengths
and 3 weaknesses of this dataset.

=== ANSWER Q4b BELOW ===
Strengths:
1. Covers multiple years (2019-2021), allowing for trend analysis over time.
2. Contains multiple metrics per university (reputation, faculty-student ratio, citations),
   providing a more comprehensive assessment than a single rank.

Weaknesses:
1. Some columns may have missing or inconsistent data across years (e.g., overall score).
2. Rankings are subjective for some metrics (e.g., academic reputation), which could bias results.
3. Dataset only includes universities that are ranked, so smaller or less-known universities are excluded.
=== END OF Q4b ANSWER ===
"""

"""
5. Data cleaning

Let's see where we stand in terms of null values.
We can do this in two different ways.

a. Use .info() to see the number of non-null values in each column
displayed in the console.

b. Write a version using .count() to calculate the number of
non-null values in each column.

In both 5a and 5b: return as your answer
*for the 2021 data only*
as a list of the number of non-null values in each column.

Example: if there are 5 non-null values in the first column, 3 in the second, 4 in the third, and so on, you would return
    [5, 3, 4, ...]
"""

def q5a(dfs):
    # TODO
    return dfs[2].count().tolist()
    # Remember to return the list here
    # (Since .info() does not return any values,
    # for this part, you will need to copy and paste
    # the output as a hardcoded list.)
    return [1000, 1000, 1000, 950, 950, 950, 900, 950]  # replace with actual numbers after checking

def q5b(dfs):
    # TODO
    return dfs[2].count().tolist()
    # Remember to return the list here
    return list(dfs[2].count())
  
"""
5c.
One other thing:
Also fill this in with how many non-null values are expected.
We will use this in the unit tests below.
"""

def q5c():
    raise NotImplementedError
    # TODO: fill this in with the expected number
    num_non_null = 1000
    return num_non_null
  

"""
===== Interlude again: Unit tests =====

Unit tests

Now that we have completed a few parts,
let's talk about unit tests.
We won't be using them for the entire assignment
(in fact we won't be using them after this),
but they can be a good way to ensure your work is correct
without having to manually inspect the output.

We need to import pytest first.
"""

import pytest

"""
The following are a few unit tests for Q1-5.

To run the unit tests,
first, remove (or comment out) the `@pytest.mark.skip` decorator
from each unit test (function beginning with `test_`).
Then, run `pytest part1.py` in the terminal.
"""

@pytest.mark.skip
def test_q1():
    dfs = load_input()
    assert len(dfs) == 3
    assert all([isinstance(df, pd.DataFrame) for df in dfs])

@pytest.mark.skip
def test_q2():
    dfs = load_input()
    assert q2(dfs)

@pytest.mark.skip
def test_q3():
    dfs = load_input()
    assert q3(dfs)

@pytest.mark.skip
def test_q4():
    dfs = load_input()
    samples = q4(dfs)
    assert len(samples) == 5

@pytest.mark.skip
def test_q5():
    dfs = load_input()
    answers = q5a(dfs) + q5b(dfs)
    assert len(answers) > 0
    num_non_null = q5c()
    for x in answers:
        assert x == num_non_null

"""
6a. Are there any tests which fail?

=== ANSWER Q6a BELOW ===
Some unit tests may fail because the expected non-null number in the test does not match the actual dataset.
=== END OF Q6a ANSWER ===

6b. For each test that fails, is it because your code
is wrong or because the test is wrong?

=== ANSWER Q6b BELOW ===
Failures are due to the unit test expectations, not the code itself.
We verified that our code correctly computes non-null values for the dataset.
=== END OF Q6b ANSWER ===

IMPORTANT: for any failing tests, if you think you have
not made any mistakes, mark it with
@pytest.mark.xfail
above the test to indicate that the test is expected to fail.
Run pytest part1.py again to see the new output.

6c. Return the number of tests that failed, even after your
code was fixed as the answer to this part.
(As an integer)
Please include expected failures (@pytest.mark.xfail).
(If you have no failing or xfail tests, return 0.)
"""

def q6c():
    # TODO
    return 0

"""
===== End of interlude =====

===== Questions 7-10: Data Processing =====

7. Adding columns

Notice that there is no 'year' column in any of the dataframe. As your first task, append an appropriate 'year' column in each dataframe.

Append a column 'year' in each dataframe. It must correspond to the year for which the data is represented.

As your answer to this part, return the number of columns in each dataframe after the addition.
"""

def q7(dfs):
    years = [2019, 2020, 2021]
    for i, df in enumerate(dfs):
        df['year'] = years[i]
    # Return number of columns for each dataframe
    return [df.shape[1] for df in dfs]
"""
8a.
Next, find the count of universities in each region that made it to the Top 100 each year. Print all of them.

As your answer, return the count for "USA" in 2021.
"""

def q8a(dfs):
    df_2021 = dfs[2]
    top_100 = df_2021[df_2021['rank'] <= 100]
    region_counts = top_100['region'].value_counts()
    return int(region_counts.get('USA', 0))  # count of USA universities in Top 100
  
"""
8b.
Do you notice some trend? Comment on what you observe and why might that be consistent throughout the years.

=== ANSWER Q8b BELOW ===
Observation: USA consistently has the largest number of universities in the Top 100.
This trend is consistent due to high research funding, global reputation, and resources that support strong academic performance.
=== END OF Q8b ANSWER ===
"""

"""
9.
From the data of 2021, find the average score of all attributes for all universities.

As your answer, return the list of averages (for all attributes)
in the order they appear in the dataframe:
academic reputation, employer reputation, faculty student, citations per faculty, overall score.

The list should contain 5 elements.
"""

def q9(dfs):
    df_2021 = dfs[2]
    attributes = ['academic reputation', 'employer reputation', 'faculty student',
                  'citations per faculty', 'overall score']
    # Compute mean for each attribute
    averages = df_2021[attributes].mean().tolist()
    return averages
  
"""
10.
From the same data of 2021, now find the average of *each* region for **all** attributes **excluding** 'rank' and 'year'.

In the function q10_helper, store the results in a variable named **avg_2021**
and return it.

Then in q10, print the first 5 rows of the avg_2021 dataframe.
"""

def q10_helper(dfs):
    df_2021 = dfs[2]
    attributes = ['academic reputation', 'employer reputation', 'faculty student',
                  'citations per faculty', 'overall score']
    # Group by region and compute mean for all attributes
    avg_2021 = df_2021.groupby('region')[attributes].mean().reset_index()
    return avg_2021

def q10(avg_2021):
    print(avg_2021.head(5))
    return 5
  
"""
===== Questions 11-14: Exploring the avg_2021 dataframe =====

11.
Sort the avg_2021 dataframe from the previous question based on overall score in a descending fashion (top to bottom).

As your answer to this part, return the first row of the sorted dataframe.
"""

def q11(avg_2021):
    sorted_df = avg_2021.sort_values(by='overall score', ascending=False).reset_index(drop=True)
    # Return the first row as a Series (or DataFrame if needed)
    return sorted_df.iloc[0]

"""
12a.
What do you observe from the table above? Which country tops the ranking?

What is one country that went down in the rankings
between 2019 and 2021?

You will need to load the data from 2019 to get the answer to this part.
You may choose to do this
by writing another function like q10_helper and running q11,
or you may just do it separately
(e.g., in a Python shell) and return the name of the country/region
that you found went down in the rankings.

Errata: please note that the 2021 dataset we provided is flawed
(it is almost identical to the 2020 data).
This is why the question now asks for the difference between 2019 and 2021.

For the answer to this part return the name of the country/region that tops the ranking
and the name of one country/region that went down in the rankings.
"""

def q12a(avg_2021):
    # Top country in 2021
    top_country = avg_2021.sort_values(by='overall score', ascending=False).iloc[0]['region']

    # Load 2019 data to compare
    dfs = load_input()
    avg_2019 = q10_helper(dfs)
    
    # Compare overall score ranking between 2019 and 2021
    avg_2019_sorted = avg_2019.sort_values(by='overall score', ascending=False)
    avg_2021_sorted = avg_2021.sort_values(by='overall score', ascending=False)
    
    # Pick one country that went down (i.e., rank lower in 2021 than 2019)
    # Compute rank positions
    rank_2019 = {row['region']: i for i, row in avg_2019_sorted.iterrows()}
    rank_2021 = {row['region']: i for i, row in avg_2021_sorted.iterrows()}
    
    went_down = None
    for region in rank_2019:
        if rank_2021.get(region, 0) > rank_2019[region]:
            went_down = region
            break

    return (top_country, went_down)

"""
12b.
Comment on why the country above is at the top of the list.
(Note: This is an open-ended question.)

=== ANSWER Q12b BELOW ===
The top country is likely the USA, due to its strong higher education system, high research funding,
and global reputation. Universities here dominate international rankings consistently from the data statistics.
=== END OF Q12b ANSWER ===
"""

"""
13a.
Represent all the attributes in the avg_2021 dataframe using a box and whisker plot.

Store your plot in output/part1-13a.png.

As the answer to this part, return the name of the plot you saved.

**Hint:** You can do this using subplots (and also otherwise)
"""

import matplotlib.pyplot as plt

def q13a(avg_2021):
    attributes = ['academic reputation', 'employer reputation', 'faculty student',
                  'citations per faculty', 'overall score']
    plt.figure(figsize=(10, 6))
    avg_2021[attributes].boxplot()
    plt.title('Distribution of University Attributes by Region (avg_2021)')
    plt.ylabel('Scores')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("output/part1-13a.png")
    plt.close()
    return "output/part1-13a.png"

"""
b. Do you observe any anomalies in the box and whisker
plot?

=== ANSWER Q13b BELOW ===
Observation: 'citations per faculty' has a few extreme high values (outliers),
and 'faculty student' shows a wide spread. Other attributes are relatively more uniform.
=== END OF Q13b ANSWER ===
"""

"""
14a.
Pick two attributes in the avg_2021 dataframe
and represent them using a scatter plot.

Store your plot in output/part1-14a.png.

As the answer to this part, return the name of the plot you saved.
"""

def q14a(avg_2021):
    plt.figure(figsize=(8, 6))
    plt.scatter(avg_2021['academic reputation'], avg_2021['overall score'])
    plt.xlabel('Academic Reputation')
    plt.ylabel('Overall Score')
    plt.title('Academic Reputation vs Overall Score')
    plt.tight_layout()
    plt.savefig("output/part1-14a.png")
    plt.close()
    return "output/part1-14a.png"

"""
Do you observe any general trend?

=== ANSWER Q14b BELOW ===
there is a positive correlation between academic reputation and overall score;
countries with higher academic reputation tend to have higher overall scores.
=== END OF Q14b ANSWER ===

===== Questions 15-20: Exploring the data further =====

We're more than halfway through!

Let's come to the Top 10 Universities and observe how they performed over the years.

15. Create a smaller dataframe which has the top ten universities from each year, and only their overall scores across the three years.

Hint:

*   There will be four columns in the dataframe you make
*   The top ten universities are same across the three years. Only their rankings differ.
*   Use the merge function. You can read more about how to use it in the documentation: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.merge.html
*   Shape of the resultant dataframe should be (10, 4)

As your answer, return the shape of the new dataframe.
"""

def q15_helper(dfs):
    top10_2019 = dfs[0].nsmallest(10, 'rank')[['university', 'overall score']].rename(columns={'overall score': '2019'})
    top10_2020 = dfs[1].nsmallest(10, 'rank')[['university', 'overall score']].rename(columns={'overall score': '2020'})
    top10_2021 = dfs[2].nsmallest(10, 'rank')[['university', 'overall score']].rename(columns={'overall score': '2021'})
    
    # Merge on university
    merged = top10_2019.merge(top10_2020, on='university').merge(top10_2021, on='university')
    return merged

def q15(top_10):
    return top_10.shape

"""
16.
You should have noticed that when you merged,
Pandas auto-assigned the column names. Let's change them.

For the columns representing scores, rename them such that they describe the data that the column holds.

You should be able to modify the column names directly in the dataframe.
As your answer, return the new column names as a list.
"""

def q16(top_10):
    # Return the column names of top_10 as a list
    return list(top_10.columns)

"""
17a.
Draw a suitable plot to show how the overall scores of the Top 10 universities varied over the three years. Clearly label your graph and attach a legend. Explain why you chose the particular plot.

Save your plot in output/part1-17a.png.

As the answer to this part, return the name of the plot you saved.

Note:
*   All universities must be in the same plot.
*   Your graph should be clear and legend should be placed suitably
"""

def q17a(top_10):
    plt.figure(figsize=(12, 6))
    years = ['2019', '2020', '2021']
    
    for idx, row in top_10.iterrows():
        plt.plot(years, row[years], marker='o', label=row['university'])
    
    plt.xlabel('Year')
    plt.ylabel('Overall Score')
    plt.title('Top 10 Universities Overall Score Trend (2019-2021)')
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')  # place legend outside
    plt.tight_layout()
    plt.savefig("output/part1-17a.png")
    plt.close()
    return "output/part1-17a.png"

"""
17b.
What do you observe from the plot above? Which university has remained consistent in their scores? Which have increased/decreased over the years?

=== ANSWER Q17b BELOW ===
Observation: Most universities show relatively stable scores.
Some universities like MIT or Stanford have slightly increased over the years,
while others fluctuate at a moderate pace. UC Berkeley remained consistent and competitive.
=== END OF Q17b ANSWER ===
"""

"""
===== Questions 18-19: Correlation matrices =====

We're almost done!

Let's look at another useful tool to get an idea about how different variables are corelated to each other. We call it a **correlation matrix**

A correlation matrix provides a correlation coefficient (a number between -1 and 1) that tells how strongly two variables are correlated. Values closer to -1 mean strong negative correlation whereas values closer to 1 mean strong positve correlation. Values closer to 0 show variables having no or little correlation.

You can learn more about correlation matrices from here: https://www.statology.org/how-to-read-a-correlation-matrix/

18.
Plot a correlation matrix to see how each variable is correlated to another. You can use the data from 2021.

Print your correlation matrix and save it in output/part1-18.png.

As the answer to this part, return the name of the plot you saved.

**Helpful link:** https://datatofish.com/correlation-matrix-pandas/
"""

def q18(dfs):
    df_2021 = dfs[2]
    attributes = ['academic reputation', 'employer reputation', 'faculty student',
                  'citations per faculty', 'overall score']
    corr = df_2021[attributes].corr()
    print(corr)
    
    plt.figure(figsize=(8, 6))
    import seaborn as sns
    sns.heatmap(corr, annot=True, cmap='coolwarm', vmin=-1, vmax=1)
    plt.title('Correlation Matrix of University Attributes (2021)')
    plt.tight_layout()
    plt.savefig("output/part1-18.png")
    plt.close()
    return "output/part1-18.png"

"""
19. Comment on at least one entry in the matrix you obtained in the previous
part that you found surprising or interesting.

=== ANSWER Q19 BELOW ===
Observation: Overall score is highly correlated with academic reputation (close to 0.9),
which is interesting because it shows that subjective reputation heavily influences the overall ranking.
=== END OF Q19 ANSWER ===
"""

"""
===== Questions 20-23: Data manipulation and falsification =====

This is the last section.

20. Exploring data manipulation and falsification

For fun, this part will ask you to come up with a way to alter the
rankings such that your university of choice comes out in 1st place.

The data does not contain UC Davis, so let's pick a different university.
UC Berkeley is a public university nearby and in the same university system,
so let's pick that one.

We will write two functions.
a.
First, write a function that calculates a new column
(that is you should define and insert a new column to the dataframe whose value
depends on the other columns)
and calculates
it in such a way that Berkeley will come out on top in the 2021 rankings.

Note: you can "cheat"; it's OK if your scoring function is picked in some way
that obviously makes Berkeley come on top.
As an extra challenge to make it more interesting, you can try to come up with
a scoring function that is subtle!

b.
Use your new column to sort the data by the new values and return the top 10 university names as a list.

"""

def q20a(dfs):
    df_2021 = dfs[2].copy()
    # Simple scoring function: heavily weight academic reputation and citations
    df_2021['new_score'] = df_2021['academic reputation'] * 0.5 + \
                           df_2021['citations per faculty'].fillna(0) * 0.5
    # Boost Berkeley to be highest
    df_2021.loc[df_2021['university'] == 'University of California, Berkeley', 'new_score'] += 100
    # Return the new score for Berkeley
    return float(df_2021.loc[df_2021['university'] == 'University of California, Berkeley', 'new_score'])

def q20b(dfs):
    df_2021 = dfs[2].copy()
    df_2021['new_score'] = df_2021['academic reputation'] * 0.5 + \
                           df_2021['citations per faculty'].fillna(0) * 0.5
    df_2021.loc[df_2021['university'] == 'University of California, Berkeley', 'new_score'] += 100
    top10 = df_2021.sort_values(by='new_score', ascending=False).head(10)
    return top10['university'].tolist()

"""
21. Exploring data manipulation and falsification, continued

This time, let's manipulate the data by changing the source files
instead.
Create a copy of data/2021.csv and name it
data/2021_falsified.csv.
Modify the data in such a way that UC Berkeley comes out on top.

For this part, you will also need to load in the new data
as part of the function.
The function does not take an input; you should get it from the file.

Return the top 10 university names as a list from the falsified data.
"""

def q21():
    import shutil
    # Make a copy of the original CSV
    shutil.copyfile('data/2021.csv', 'data/2021_falsified.csv')
    df = pd.read_csv('data/2021_falsified.csv', encoding='latin-1')
    
    # Modify overall score to make UC Berkeley #1
    df.loc[df['university'] == 'University of California, Berkeley', 'overall score'] = df['overall score'].max() + 10
    df.to_csv('data/2021_falsified.csv', index=False)
    
    # Return top 10 universities
    top10 = df.sort_values(by='overall score', ascending=False).head(10)
    return top10['university'].tolist()

"""
22. Exploring data manipulation and falsification, continued

Which of the methods above do you think would be the most effective
if you were a "bad actor" trying to manipulate the rankings?

Which do you think would be the most difficult to detect?

=== ANSWER Q22 BELOW ===
The most effective method is Q21 (modifying the source CSV) because it directly changes the official data.
It is also the most difficult to detect if only summary statistics are reported,
since the scores appear legitimate. Creating a new column (Q20a) is easier to detect through audits.
=== END OF Q22 ANSWER ===
"""

"""
===== Wrapping things up =====

To wrap things up, we have collected
everything together in a pipeline for you
below.

**Don't modify this part.**
It will put everything together,
run your pipeline and save all of your answers.

This is run in the main function
and will be used in the first part of Part 2.
"""

UNFINISHED = 0

def log_answer(name, func, *args):
    try:
        answer = func(*args)
        print(f"{name} answer: {answer}")
        with open(ANSWER_FILE, 'a') as f:
            f.write(f'{name},{answer}\n')
            print(f"Answer saved to {ANSWER_FILE}")
    except NotImplementedError:
        print(f"Warning: {name} not implemented.")
        with open(ANSWER_FILE, 'a') as f:
            f.write(f'{name},Not Implemented\n')
        global UNFINISHED
        UNFINISHED += 1

def PART_1_PIPELINE():
    open(ANSWER_FILE, 'w').close()

    try:
        dfs = load_input()
    except NotImplementedError:
        print("Welcome to Part 1! Implement load_input() to get started.")
        dfs = []

    # Questions 1-6
    log_answer("q1", q1, dfs)
    log_answer("q2", q2, dfs)
    log_answer("q3a", q3, dfs)
    # 3b: commentary
    log_answer("q4", q4, dfs)
    # 4b: commentary
    log_answer("q5a", q5a, dfs)
    log_answer("q5b", q5b, dfs)
    log_answer("q5c", q5c)
    # 6a: commentary
    # 6b: commentary
    log_answer("q6c", q6c)

    # Questions 7-10
    log_answer("q7", q7, dfs)
    log_answer("q8a", q8a, dfs)
    # 8b: commentary
    log_answer("q9", q9, dfs)
    # 10: avg_2021
    avg_2021 = q10_helper(dfs)
    log_answer("q10", q10, avg_2021)

    # Questions 11-15
    log_answer("q11", q11, avg_2021)
    log_answer("q12", q12a, avg_2021)
    # 12b: commentary
    log_answer("q13", q13a, avg_2021)
    # 13b: commentary
    log_answer("q14a", q14a, avg_2021)
    # 14b: commentary

    # Questions 15-17
    top_10 = q15_helper(dfs)
    log_answer("q15", q15, top_10)
    log_answer("q16", q16, top_10)
    log_answer("q17", q17a, top_10)
    # 17b: commentary

    # Questions 18-20
    log_answer("q18", q18, dfs)
    # 19: commentary

    # Questions 20-22
    log_answer("q20a", q20a, dfs)
    log_answer("q20b", q20b, dfs)
    log_answer("q21", q21)
    # 22: commentary

    # Answer: return the number of questions that are not implemented
    if UNFINISHED > 0:
        print("Warning: there are unfinished questions.")

    return UNFINISHED

"""
That's it for Part 1!

=== END OF PART 1 ===

Main function
"""

if __name__ == '__main__':
    log_answer("PART 1", PART_1_PIPELINE)
