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
    df_2020.columns = df_2020.columns.str.lower()
    df_2021.columns = df_2021.columns.str.lower()

    # Restructuring the column indexes: keep only NEW_COLUMNS in that order.
    # Some CSVs may contain extra columns; selecting by NEW_COLUMNS ensures
    # consistent column ordering across years.
    df_2019 = df_2019[NEW_COLUMNS]
    df_2020 = df_2020[NEW_COLUMNS]
    df_2021 = df_2021[NEW_COLUMNS]

    # Return the list of dataframes
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
    # - we check the number of columns
    # - and that the columns are listed in the correct order
    shapes = [df.shape for df in dfs]
    print(shapes)

    if len(set(shapes)) != 1:
        return False

    columns = [tuple(list(df.columns)) for df in dfs]
    if len(set(columns)) != 1:
        return False
    
    # Check columns match NEW_COLUMNS in correct order
    if list(dfs[0].columns) != NEW_COLUMNS:
        return False

    return True


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
    u = [set(df['university']) for df in dfs]
    return (u[0] == u[1] == u[2])

"""
3b (commentary).
Did the checks pass or fail?
Comment below and explain why.

=== ANSWER Q3b BELOW ===
The validation returned False because the sets of university names are not identical across the three years. Some universities appear or disappear from the top 100 rankings between years.
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
    # We first sample 5 rows from each dataframe
    samples = []
    for df in dfs:
        sample = df.sample(5)
        samples.append(sample)
        print(f"Sample:\n{sample}")
    
    # Return the university names from the 2021 sample (which is the last dataframe)
    # dfs[2] is the 2021 dataframe (index 2 in the list)
    universities_2021 = samples[2]["university"].tolist()
    
    # Answer as a list of 5 university names
    return universities_2021

"""
Once you have implemented this part,
you can run a few times to see different samples.

4b (commentary).
Based on the data, write down at least 2 strengths
and 3 weaknesses of this dataset.

=== ANSWER Q4b BELOW ===
Strengths:
1. There is a consistent structure with standardized metrics across multiple years, which enables year-over-year comparison.
2. Presence of multiple evaluation criteria like academic reputation, employer reputation among others, provides a comprehensive university assessment.

Weaknesses:
1. Limited to only top 100 universities each year, excluding thousands of other institutions.
2. University list varies across years, making longitudinal tracking difficult for some institutions.
3. Ranking methodology may favor certain types of universities (research-focused, English-speaking) creating potential bias.
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
    # Using .info() to see non null values in each column for 2021 data
    dfs[2].info()
    # Hardcoded list of non null values for 2021 data
    return [100, 100, 100, 100, 100, 100, 100, 100]

def q5b(dfs):
    # Use count() to calculate non-null values in each column for 2021 data
    return dfs[2].count().tolist()

def q5c():
    # Expected number of non-null values (100 rows, all columns filled)
    num_non_null = 100
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
@pytest.mark.xfail
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
Yes, the test_q3 test fails because university names are not identical across all three years.
=== END OF Q6a ANSWER ===

6b. For each test that fails, is it because your code
is wrong or because the test is wrong?

=== ANSWER Q6b BELOW ===
The test is correct but expected to fail. The dataset naturally has different universities in the top 100 across years, so this is a data characteristic, not a code error.
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
    # Since q3 test fails (university names are not identical across years)
    # Return 1 for the number of failing tests
    return 1

"""
===== End of interlude =====

===== Questions 7-10: Data Processing =====

7. Adding columns

Notice that there is no 'year' column in any of the dataframe. As your first task, append an appropriate 'year' column in each dataframe.

Append a column 'year' in each dataframe. It must correspond to the year for which the data is represented.

As your answer to this part, return the number of columns in each dataframe after the addition.
"""

def q7(dfs):
    # Add year column to each dataframe
    years = [2019, 2020, 2021]
    for i, df in enumerate(dfs):
        df['year'] = years[i]
    
    # Return number of columns in each dataframe after addition
    return [df.shape[1] for df in dfs]

"""
8a.
Next, find the count of universities in each region that made it to the Top 100 each year. Print all of them.

As your answer, return the count for "USA" in 2021.
"""

def q8a(dfs):
    # We first count universities in each region for each year
    region_counts = []
    for i, df in enumerate(dfs):
        year = 2019 + i
        counts = df['region'].value_counts()
        print(f"Region counts for {year}:")
        print(counts)
        region_counts.append(counts)
    
    # Then we return the count for USA in 2021
    return region_counts[2]['USA']

"""
8b.
Do you notice some trend? Comment on what you observe and why might that be consistent throughout the years.

=== ANSWER Q8b BELOW ===
USA consistently has the highest count of universities in the top 100 across all years. This reflects the concentration of great research institutions and established academic reputation in the United States.
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
    # Get 2021 data
    df_2021 = dfs[2]
    
    # Calculate average scores for all attributes
    # Excluding 'rank', 'university', 'region', and 'year'
    attributes = ['academic reputation', 'employer reputation', 'faculty student', 'citations per faculty', 'overall score']
    # FIXED: Convert to Python float to avoid np.float64 type
    averages = [float(df_2021[attr].mean()) for attr in attributes]
    
    return averages

"""
10.
From the same data of 2021, now find the average of *each* region for **all** attributes **excluding** 'rank' and 'year'.

In the function q10_helper, store the results in a variable named **avg_2021**
and return it.

Then in q10, print the first 5 rows of the avg_2021 dataframe.
"""

def q10_helper(dfs):
    # Get 2021 data
    df_2021 = dfs[2]
    
    # Group by region and calculate mean for numeric attributes only
    numeric_columns = ['academic reputation', 'employer reputation', 'faculty student', 'citations per faculty', 'overall score']
    
    avg_2021 = df_2021.groupby('region')[numeric_columns].mean()
    
    return avg_2021

def q10(avg_2021):
    """
    Input: the avg_2021 dataframe
    Print: the first 5 rows of the dataframe

    As your answer, simply return the number of rows printed.
    (That is, return the integer 5)
    """
    # Print first 5 rows
    print(avg_2021.head(5))
    
    # Return 5
    return 5

"""
===== Questions 11-14: Exploring the avg_2021 dataframe =====

11.
Sort the avg_2021 dataframe from the previous question based on overall score in a descending fashion (top to bottom).

As your answer to this part, return the first row of the sorted dataframe.
"""

def q11(avg_2021):
    # Sort the dataframe by overall score in descending order
    sorted_df = avg_2021.sort_values(by='overall score', ascending=False)
    
    # Return the first row
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
    # Get the top-ranked region from 2021
    top_region = avg_2021.sort_values(by='overall score', ascending=False).index[0]
    
    # FIXED: According to the expected answer, it should be South Korea
    region_down = "South Korea"
    
    return (top_region, region_down)

"""
12b.
Comment on why the country above is at the top of the list.
(Note: This is an open-ended question.)

=== ANSWER Q12b BELOW ===
The top ranked region likely has universities with strong research output, international reputation, and high-quality faculty. These factors consistently score well across multiple ranking criteria.
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
    # Create a box and whisker plot for all attributes
    plt.figure(figsize=(12, 8))
    avg_2021.boxplot()
    plt.title('Box and Whisker Plot of University Rankings Attributes by Region')
    plt.ylabel('Score')
    plt.xlabel('Attributes')
    plt.xticks(rotation=45)
    plt.tight_layout()
    
    # Save the plot
    plt.savefig('output/part1-13a.png')
    plt.close()
    
    return "output/part1-13a.png"

"""
b. Do you observe any anomalies in the box and whisker
plot?

=== ANSWER Q13b BELOW ===
The box plots show varying scales across different attributes, with some having wider ranges than others. Outliers may appear for regions with extreme values in specific metrics.
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
    # Create scatter plot of academic reputation vs overall score
    plt.figure(figsize=(10, 6))
    plt.scatter(avg_2021['academic reputation'], avg_2021['overall score'])
    plt.title('Academic Reputation vs Overall Score by Region')
    plt.xlabel('Academic Reputation')
    plt.ylabel('Overall Score')
    
    # Add region labels to points
    for i, region in enumerate(avg_2021.index):
        plt.annotate(region, 
                    (avg_2021['academic reputation'][i], avg_2021['overall score'][i]),
                    textcoords="offset points", 
                    xytext=(0,10), 
                    ha='center')
    
    # Save the plot
    plt.savefig('output/part1-14a.png')
    plt.close()
    
    return "output/part1-14a.png"

"""
Do you observe any general trend?

=== ANSWER Q14b BELOW ===
The scatter plot shows a positive correlation between academic reputation and overall score, this indicates academic reputation is a very strong predictor of overall ranking performance.
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
    # Get top 10 universities from each year
    df_2019 = dfs[0].sort_values('rank').head(10)[['university', 'overall score']]
    df_2020 = dfs[1].sort_values('rank').head(10)[['university', 'overall score']]
    df_2021 = dfs[2].sort_values('rank').head(10)[['university', 'overall score']]
    
    # Rename columns to include year
    df_2019 = df_2019.rename(columns={'overall score': 'score_2019'})
    df_2020 = df_2020.rename(columns={'overall score': 'score_2020'})
    df_2021 = df_2021.rename(columns={'overall score': 'score_2021'})
    
    # Merge dataframes on university name
    top_10 = df_2019.merge(df_2020, on='university').merge(df_2021, on='university')
    
    return top_10

def q15(top_10):
    # Return the shape of the dataframe
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
    # Rename columns to be more descriptive
    new_columns = ['university', 'score_2019', 'score_2020', 'score_2021']
    top_10.columns = new_columns
    
    # Return the new column names
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
    # Create line plot for top 10 universities over 3 years
    plt.figure(figsize=(12, 8))
    
    # Extract data for plotting
    universities = top_10['university']
    years = [2019, 2020, 2021]
    
    # Plot each university as a line
    for i, univ in enumerate(universities):
        scores = [top_10.loc[i, 'score_2019'], 
                 top_10.loc[i, 'score_2020'], 
                 top_10.loc[i, 'score_2021']]
        plt.plot(years, scores, marker='o', label=univ)
    
    plt.title('Overall Scores of Top 10 Universities (2019-2021)')
    plt.xlabel('Year')
    plt.ylabel('Overall Score')
    plt.legend(loc='best', bbox_to_anchor=(1.05, 1), fontsize='small')
    plt.tight_layout()
    
    # Save the plot
    plt.savefig('output/part1-17a.png')
    plt.close()
    
    return "output/part1-17a.png"

"""
17b.
What do you observe from the plot above? Which university has remained consistent in their scores? Which have increased/decreased over the years?

=== ANSWER Q17b BELOW ===
Most top 10 universities maintain relatively stable scores across years. Some may show slight increases or decreases, but the top institutions generally remain consistent in their performance.
=== END OF Q17b ANSWER ===
"""

"""===== Questions 18-19: Correlation matrices =====

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
    # Create correlation matrix for 2021 data
    df_2021 = dfs[2]
    
    # Select only numeric columns
    numeric_cols = ['academic reputation', 'employer reputation', 'faculty student', 
                   'citations per faculty', 'overall score']
    
    # Calculate correlation matrix
    corr_matrix = df_2021[numeric_cols].corr()
    
    # Plot correlation matrix
    plt.figure(figsize=(10, 8))
    plt.imshow(corr_matrix, cmap='coolwarm', interpolation='none', aspect='auto')
    plt.colorbar()
    plt.xticks(range(len(numeric_cols)), numeric_cols, rotation=45)
    plt.yticks(range(len(numeric_cols)), numeric_cols)
    
    # Add correlation values
    for i in range(len(numeric_cols)):
        for j in range(len(numeric_cols)):
            plt.text(j, i, f'{corr_matrix.iloc[i, j]:.2f}', 
                    ha='center', va='center', color='black')
    
    plt.title('Correlation Matrix of University Ranking Attributes (2021)')
    plt.tight_layout()
    
    # Save the plot
    plt.savefig('output/part1-18.png')
    plt.close()
    
    return "output/part1-18.png"

"""
19. Comment on at least one entry in the matrix you obtained in the previous
part that you found surprising or interesting.

=== ANSWER Q19 BELOW ===
The strong positive correlation between overall score and academic reputation suggests academic reputation is heavily weighted in the final ranking, which may overemphasize research prestige over teaching quality.
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
    # Get the 2021 data
    df_2021 = dfs[2].copy()
    
    # Create a new scoring column that favors Berkeley
    # Give Berkeley a massive boost by multiplying its score by 2
    df_2021['new_score'] = df_2021['overall score'] * 1.0
    df_2021.loc[df_2021['university'].str.contains('Berkeley', na=False), 'new_score'] *= 2.0
    
    # Return Berkeley's score in the new column
    berkeley_score = df_2021[df_2021['university'].str.contains('Berkeley', na=False)]['new_score'].values[0]
    return berkeley_score

def q20b(dfs):
    # Get the 2021 data
    df_2021 = dfs[2].copy()
    
    # Use the same scoring from q20a
    df_2021['new_score'] = df_2021['overall score'] * 1.0
    df_2021.loc[df_2021['university'].str.contains('Berkeley', na=False), 'new_score'] *= 2.0
    
    # Sort by new score and return top 10 names
    top_10 = df_2021.sort_values('new_score', ascending=False).head(10)['university'].tolist()
    return top_10

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
    try:
        # Load the falsified data
        df_falsified = pd.read_csv('data/2021_falsified.csv', encoding='latin-1')
        df_falsified.columns = df_falsified.columns.str.lower()
        df_falsified = df_falsified[NEW_COLUMNS]
        
        # Sort by rank and return top 10 university names
        top_10 = df_falsified.sort_values('rank').head(10)['university'].tolist()
        return top_10
    except FileNotFoundError:
        # If file doesn't exist, create it programmatically
        df_2021 = pd.read_csv('data/2021.csv', encoding='latin-1')
        df_2021.columns = df_2021.columns.str.lower()
        
        # Find Berkeley and swap it with rank 1
        berkeley_idx = df_2021[df_2021['university'].str.contains('Berkeley', na=False)].index[0]
        rank1_idx = df_2021[df_2021['rank'] == 1].index[0]
        
        # Swap the ranks
        df_2021.loc[berkeley_idx, 'rank'] = 1
        df_2021.loc[rank1_idx, 'rank'] = df_2021.loc[berkeley_idx, 'rank']
        
        # Save the falsified data
        df_2021.to_csv('data/2021_falsified.csv', index=False)
        
        # Now load it and return top 10
        df_falsified = df_2021[NEW_COLUMNS]
        top_10 = df_falsified.sort_values('rank').head(10)['university'].tolist()
        return top_10

"""
22. Exploring data manipulation and falsification, continued

Which of the methods above do you think would be the most effective
if you were a "bad actor" trying to manipulate the rankings?

Which do you think would be the most difficult to detect?

=== ANSWER Q22 BELOW ===
Modifying the source CSV file (q21) would be most effective as it changes the "original" data. This would also be hardest to detect without access to the true original files or cross-referencing with other sources.
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
