
## Hollywood Movie Classification

### Notebooks
---
- [Understanding the variables](https://github.com/srjit/hollywood-movie-classification/blob/master/Hollywood%20data%20analysis%201%20-%20Understanding%20Variables.ipynb) :
  + Analyze the available variables, their distribution, correlation etc.
- [Modeling Experiments](https://github.com/srjit/hollywood-movie-classification/blob/master/Hollywood%20data%20analysis%202%20-%20Preprocessing%20%26%20Modeling.ipynb) :
  + Preprocessing - One Hot Encoding categorical variables, Vectorizing Text Fields
	- All features except `year` has been used during the preprocessing and modeling procedure. 
	- Since the number of rows are less, an 85%-15% of total instances have been used for training and testing respectively.
  + Experimenting and tuning parameters of different classification models. All models have been experimented with and without text features included. The one away score defined in the literature on previous work has been used here to optimize the performance of the classifier.
	1. Multiclass Logistic Regression: 71.6% and 72.2% one away percentage score on test data with and without text features repectively.
	2. Support Vector Machine: 67.8% and 72.7% one away percentage score on test data with and without text features repectively.
	3. Random Forest: 72.2% and 75.5% one away percentage score on test data with and without text features repectively.
	4. Boosted Tree Model (XGBoost): 73.3% and 71.1% one away percentage score on test data with and without text features repectively.
	5. Fusion (Most Voted Class) model: 75.5% one away percentage score on test data
	
  + Creating a custom classifier that picks the most voted candidate class as the final target
- [Scoring the New Sheet](https://github.com/srjit/hollywood-movie-classification/blob/master/Hollywood%20data%20analysis%203%20-%20Classify.ipynb) :
  + Select the best classifier(s), and use it to classify the instances in the scoring sheet
  + Two sets of predictions using the best performing classifiers. 
	- [prediction1.csv](https://github.com/srjit/hollywood-movie-classification/blob/master/prediction1.csv)
	- [prediction2.csv](https://github.com/srjit/hollywood-movie-classification/blob/master/prediction2.csv)

### Custom Functions
---
- [Metrics](metrics.py):
  + Functions that assists the evaluation of a classifier
	- (Accuracy)[https://github.com/srjit/hollywood-movie-classification/blob/8960301b4daa4c9a93b9da55e981923674257e7f/metrics.py#L10]: Total correctly classified / Total instances.
	- (Bingo Score)[https://github.com/srjit/hollywood-movie-classification/blob/8960301b4daa4c9a93b9da55e981923674257e7f/metrics.py#L21]: Implementation of bingo score from literature.
	- (One Away Score)[https://github.com/srjit/hollywood-movie-classification/blob/8960301b4daa4c9a93b9da55e981923674257e7f/metrics.py#L47]: Implementation of one away score from the literature.

