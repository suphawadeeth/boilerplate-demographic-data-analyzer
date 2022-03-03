import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('adult.data.csv')

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df['race'].value_counts()

    # What is the average age of men?
    men = df.loc[df['sex'] == 'Male', 'age']
    average_age_men = round(df.loc[df['sex'] == 'Male', 'age'].mean(), 1)

    # What is the percentage of people who have a Bachelor's degree?
    bachelor = df['education'] == 'Bachelors'
    percentage_bachelors = round(bachelor.sum() * 100 / df['education'].value_counts().sum(), 1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    master = df['education'] == 'Masters'
    doctor = df['education'] == 'Doctorate'

    higher = (bachelor) | (master) | (doctor)
    lower = (df['education'] != 'Bachelors') & (df['education'] != 'Masters') & (df['education'] != 'Doctorate')
    #print('HIGER ED GROUP', higher)
    #print('LOWER ED GROUP', lower)

    higher_education = None
    lower_education = None

    #percentage with salary >50K
    #print('GROUP OF SALARY > 50K', df['salary'] == '>50K')
    #print('GROUP OF SALARY > 50K WITH HIGHER EDUCATION', df.loc[higher & (df['salary'] == '>50K')])
    hi_ed_rich_number = df.loc[higher & (df['salary'] == '>50K')].value_counts().sum()
    hi_ed_total = df.loc[higher].value_counts().sum()
    #print(hi_ed_total)
    higher_education_rich = round(hi_ed_rich_number * 100 / hi_ed_total, 1)
    #print(higher_education_rich)


    #print('GROUP OF SALARY > 50K WITH LOWER EDUCATION', df.loc[lower & (df['salary'] == '>50K')])
    low_ed_rich_number = df.loc[lower & (df['salary'] == '>50K')].value_counts().sum()
    low_ed_total = df.loc[lower].value_counts().sum()
    #print(low_ed_total)
    lower_education_rich = round(low_ed_rich_number * 100 / low_ed_total, 1)
    #print(lower_education_rich)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()
    #print('MIN', df['hours-per-week'].min())
    #print('MEAN', df['hours-per-week'].mean())
    #print('MAX', df['hours-per-week'].max())
    #print('WHO WORKS 40H', df['hours-per-week'] == 40)

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    num_min_workers = df.loc[df['hours-per-week'] == 1].value_counts().sum()
    #print('GROUP OF SALARY > 50K', df['salary'] == '>50K')
    #print('WHO WORKS MIN HOURS', df.loc[df['hours-per-week'] == 1].value_counts().sum())
    min_workers_rich = df.loc[(df['hours-per-week'] == 1) & (df['salary'] == '>50K')].value_counts().sum()
    #print('WORK LESS BUT RICH', min_workers_rich)

    rich_percentage = round(min_workers_rich * 100 / num_min_workers, 1)
    #print('% MIN WORK BUT RICH', rich_percentage)

    # What country has the highest percentage of people that earn >50K?

    country_population = df['native-country'].value_counts()
    rich_pop_by_country = df.loc[df['salary'] == '>50K', 'native-country'].value_counts()
    #print('RICH POP BY COUNTRY', rich_pop_by_country)
    #print('COUNTRY POP', country_population)
    percent_rich_by_country = round(rich_pop_by_country *100 / country_population, 1)
    #print('PERCENT RICH BY COUNTRY', percent_rich_by_country)
    #print('HIGHEST RICH COUNTRY', percent_rich_by_country.idxmax())
    highest_earning_country = percent_rich_by_country.idxmax()
    highest_earning_country_percentage = percent_rich_by_country.max()

    # Identify the most popular occupation for those who earn >50K in India.
    india = df['native-country'] == 'India'
    india_rich = df.loc[(india) & (df['salary'] == '>50K')]
    india_occ_rich = india_rich['occupation'].value_counts().idxmax()
    #print('INDIA RICH', india_occ_rich)
    top_IN_occupation = india_rich['occupation'].value_counts().idxmax()

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count)
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
