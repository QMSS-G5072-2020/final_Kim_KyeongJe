




def Korea_Covid():
    """
    Describe 
    This is the South Korea Covid API in this package 
    I will look into the data that I am interested in. 
    Parameters 
    ----------
    N/A
    
    Returns
    ----------
    DataFrame
        The data is already converted into dataframe format.
        
    Status of code
        It will inidicate if the api successfully made it or not
        if not it will show some explanations to solve the error.
    
    
    Example
    ----------
	infected	discharged	Isolated	deceased	testsPerformed	testsConcluded	positivityRate	country	historyData	sourceUrl	lastUpdatedAtApify	lastUpdatedAtSource	readMe	isolated
0	9887	5567	4155.0	165.0	421547.0	404962.0	2.4%	South Korea	https://api.apify.com/v2/datasets/T43VVY5mDBeF...	http://ncov.mohw.go.kr/en	2020-04-01T20:20:00.000Z	2020-04-01T12:00:00.000Z	https://apify.com/onidivo/covid-kr	0
1	9976	5828	3979.0	169.0	431743.0	413858.0	2.4%	South Korea	https://api.apify.com/v2/datasets/T43VVY5mDBeF...	http://ncov.mohw.go.kr/en	2020-04-02T01:15:00.000Z	2020-04-02T12:00:00.000Z	https://apify.com/onidivo/covid-kr	0
2	10062	6021	3867.0	174.0	443273.0	424365.0	2.4%	South Korea	https://api.apify.com/v2/datasets/T43VVY5mDBeF...	http://ncov.mohw.go.kr/en	2020-04-03T01:20:00.000Z	2020-04-03T12:00:00.000Z	https://apify.com/onidivo/covid-kr	0
3	10156	6325	3654.0	177.0	455032.0	434888.0	2.3%	South Korea	https://api.apify.com/v2/datasets/T43VVY5mDBeF...	http://ncov.mohw.go.kr/en	2020-04-04T01:35:00.000Z	2020-04-04T12:00:00.000Z	https://apify.com/onidivo/covid-kr	0
4	10156	6325	3654.0	177.0	0.0	0.0	0	South Korea	https://api.apify.com/v2/datasets/T43VVY5mDBeF...	http://ncov.mohw.go.kr/en	2020-04-04T17:15:00.000Z	2020-04-04T12:00:00.000Z	https://apify.com/onidivo/covid-kr	0
    
    """
    
    r1 = requests.get('https://api.apify.com/v2/datasets/Lc0Hoa8MgAbscJA4w/items?format=json&clean=1')  
    if r1.status_code == 200:
        print("Congrats!! Successfully get API!") #Status code of 200 shows this is working.
    elif r1.status_code != 200:
        print("Hmm you may want to check this! 400:error (failed to make request), 500:successfully made but had internal error, Good Luck!")
   
    covid_json = r1.json()
    covid_json_df = pd.DataFrame(covid_json)
    return covid_json_df




def covid_df():
        """
    Describe the funtion 
    Dataframe dataset will get fill na as 0 and will get rid of all other any na, N/A
    Data cleaning 
    I will get only variables that I am interested in
    If there is non float data, that will be changed into float type to easily use
    
    Parameters 
    ----------
    N/A
    
    Returns
    ----------
    Dataframe Covid_json which is Korea dataset
    will get cleaned dataframe which contains 'infected', 'Isolated',
    'testsPerformed', 'testsConcluded', 'deceased' as variable
    
    
    Example
    ----------
    
infected	Isolated	testsPerformed	testsConcluded	deceased
0	9887	4155.0	421547.0	404962.0	165.0
1	9976	3979.0	431743.0	413858.0	169.0
2	10062	3867.0	443273.0	424365.0	174.0
3	10156	3654.0	455032.0	434888.0	177.0
4	10156	3654.0	0.0	0.0	177.0

    """
    r1 = requests.get('https://api.apify.com/v2/datasets/Lc0Hoa8MgAbscJA4w/items?format=json&clean=1')  
    covid_json = r1.json()
    covid_json_df = pd.DataFrame(covid_json)
    covid_clean = covid_json_df.fillna(0) # get rid of na
    covid_clean = covid_clean.dropna(how='any')
    covid_clean = covid_clean[covid_clean['infected'] != 'N/A']
    cd = covid_clean[['infected', 'Isolated', 'testsPerformed', 'testsConcluded', 'deceased']]
    cd = cd.fillna(0)
    cd["infected"] = cd.infected.astype(float) #convert into float type
    print("cd = covid_data. You Got the data! move forward!")
    
    return cd





def CanIgoOut(cd):
        """
    Describe the funtion 
    It will show the percentage of the positive rate.
    infected devided by tesetsperformed then *100 so you will get intuition of
    the how much covid is spreading out badly 
    
    Parameters 
    ----------
    cd 
        dataset that we cleaned already
    infected
        number of people who caught covid
    testsperformed
        number of covid test
          
    
    Returns
    ----------
    list
        the calculated ratio 
    how much it is bad at the moment. result>=2 bad result<2 relatively better
    
    
    Example
    ----------
    If >2 Prepare the Covid wave! Need Strict Social Distancing!, 
    if <2 You may go out with Mask on!
    0      2.345409
    1      2.310634
    2      2.269933
    3      2.231931
    4           inf
         ...   
    304    1.212085
    305    1.223266
    306    1.302522
    307    1.312662
    308    1.323613
Length: 308, dtype: float64
    """
    positive_rate=(cd['infected']/cd['testsPerformed'])*100
    print ("If >2 Prepare the Covid wave! Need Strict Social Distancing!, if <2 You may go out with Mask on!")
    
    return positive_rate



def deathrate(cd):
        """
    Describe the funtion 
    It will show the percentage of the death rate when caught covid.
    deceased devided by infected then *100 so you will get intuition of
    the how much covid is dangerous 
    
    Parameters 
    ----------
    cd 
        dataset that we cleaned already
    infected
        number of people who caught covid
    deceased 
        number of people who died by covid
        
          
    
    Returns
    ----------
    list
        the calculated ratio 
    how much it is bad at the moment. result>=1 bad result<1 relatively less peopel die
    
    
    Example
    ----------
 If >1 STAY at HOME!, if <1 Slightly Better but still dangerous!
    0      1.668858
    1      1.694066
    2      1.729278
    3      1.742812
    4      1.742812
         ...   
    304    1.410022
    305    1.406554
    306    1.346772
    307    1.364820
    308    1.357466
Length: 308, dtype: float64
    """
    deaths=(cd['deceased']/cd['infected'])*100
    print ("If >1 STAY at HOME!, if <1 Slightly Better but still dangerous!")
        
    return deaths


def Igotcovidamigoingtodie(cd):
        """
    Describe the funtion 
    It will show the percentage of the death rate graphically when caught covid.
    
    
    Parameters 
    ----------
    cd 
        dataset that we cleaned already
    infected
        number of people who caught covid
    deceased 
        number of people who died by covid
     x = infected y = deceased
          
          
    
    Returns
    ----------
    graph
    
    
    Example
    ----------
    image
    
    """
    import matplotlib.pyplot as plt
    import seaborn as sns
    sns.regplot(x = 'infected', y = 'deceased', data = cd)
    plt.grid()
    return



def Ijusttested(cd):
        """
    Describe the funtion 
    It will show the percentage of the positive rate graphically.
    
    
    Parameters 
    ----------
    cd 
        dataset that we cleaned already
    infected
        number of people who caught covid
    testsperformed
        number of covid test
     x = testsperformed  y = infected
    
    
    Returns
    ----------
    graph
    
    
    Example
    ----------
    image
    
    """
    import matplotlib.pyplot as plt
    import seaborn as sns
    sns.regplot(x = 'testsPerformed', y = 'infected', data = cd)
    plt.grid()
    return


