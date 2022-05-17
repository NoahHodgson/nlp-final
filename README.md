# CISC489 Process and Analysis

# Name - Noah Hodgson

# Title - Shifting Opinions on Ukraine - A Semantic Analysis of News Articles Before and During the War

## Original Proposal
Use semantic analysis to determine whether or not media opinion on Ukraine and its leader has shifted since Russia’s war of aggression began.

## Process

### Phase 1
The first thing I needed to do in order to work on the project was acquire some data from the
news. The easiest to access API belonged to the New York Times. I have a student liscense,
so I was able to scrape their articles. The coding (included in scraper.js) took more time 
than expected to scrape, in part due to being rate limited. I also was originally going
to look at entire articles from pre and post war, but I limited my scope to just the opening
paragraphs. This was because a plurality of post war articles often are a collection of
the days stories, and quickly change focus from the Russo-Ukrainian War.

### Phase 2
For the sentiment analysis, I was originally going to try and make my own using the BBC news
dataset. The files were not annotated, however, which meant that I would have had to spend a lot of
time on that. For now, I decided to instead use the built-in one that came from the nltk library, and
was trained on the Vader dataset. So I ran the analyzer on the data I got from scraping. Here were 
the results were... not quite what I wanted.
![Averages from Prewar and Postwar](/results/resultsWar.png)
As stated in my proposal, I wanted to look how Ukraine was being potrayed by the media,
specifically the coverage of the government. With just the out of the box 
sentiment analyzer, pre war was more likely to be positive and post war negative. The reason
 for this became pretty obvious for me. Words like "war", "fighting", and "under fire" pulled the 
paragraph pretty heavy to negative. It did not matter whether or not the Ukrainians were being lionized 
or potrayed as heroes, or if the Russians were demonized.<br><br>What would I have to do to solve this
issue while still trying to use sentiment analysis on this data? While the time necessary is not 
allotted for this final project, I was advised by Dr. McCoy to theorize what I would need to do.
The first thing that I think is necessary is to evaluate words like war and fighting as neutral. Next
would be to evaluate Ukraine and Russia and how they handle reflexive words. For instance if an article
is saying good things about Ukraine or Ukrainian victories, that up the likelihood of the sentence
being positive. Likewise Russian defeat should evaluate to negative. It may seem a little odd since
loss and victories are part of war, but on a large dataset and a war that has been fairly even
thus far, focusing more on one sides victories would indicate favoritism. A similar thing 
could be done with leaders of both countries. Positive for Zelensky being popular, and then negative
for Putin becoming more unpopular. This would also help some of the "prewar" data as well as 
the postwar, because me calling the one section of data "prewar" is a little misleading as Pro-Russian rebels
have been fighting in Ukraine since the annexation of Crimea. 

### Phase 3
Even if I did not quite get the results I wanted. I decided to take what I have learned and apply it to
some more articles about Ukraine. I have decided to analyze articles including Zelensky, both with sentences
mentioning him intact and then also removed to determine how positive the media coverage is in the NYT for him. 
![Averages from Prewar and Postwar](/results/resultsZel1.png) Now if we take the sentences including Zelensky
out of the articles, we get this. ![Averages from Prewar and Postwar](/results/resultsZel2.png) For the the first pre-war result, taking Zelensky out of
the story made the article less negative, while other numbers barely fluctuated.
For the second pre-war one, it became less positive and negative and more compound.
For the third one, it remained mostly the same with only a slight decrease in
positivity<br><br>On the post war side, the first article became more positive and
more negative. The second one became more negative and less positive. The third
postwar story became less positive and less negative.

## Analysis
So overall what did my data say? For Phase 2, it told me that the language surrounding war is negative. If I want to attempt to determine whether or not a story is coming in
more or less favorably towards one government for a war, I will need a much more complex
sentiment analyzer that is able to parse language that is reflexive, relative to the different parties involved in the combat.<br><br> For Phase 3, I think I was able to get a cleaner answer. The Prewar articles, when Zelensky was mentioned, did go more negative
this is in part to the corruption surrounding the government at the time of his election
Comparably, the postwar articles become less neutral and more positive and sometimes
more negative. The positivity I would posit is because Western media is very supportive
of Zelensky. The negative could be coming from the fact that Zelensky in his speeches
is talking about the war and the bombings of civilians, which as seen in Phase 2, will
evaluate as more negative.
## How to run
Simple, all it is downloading the necessary nltk packages and running analyze.py as a python file in vs code.
