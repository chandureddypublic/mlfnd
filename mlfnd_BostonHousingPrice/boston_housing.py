
# coding: utf-8

# # Machine Learning Foundation Nanodegree
# ## Model Evaluation & Validation
# ## Project 5: Predicting Boston Housing Prices
# 
# Welcome to the project 5 of the Machine Learning Engineer Nanodegree! In this notebook, some template code has already been provided for you, and you will need to implement additional functionality to successfully complete this project. You will not need to modify the included code beyond what is requested. Sections that begin with **'Implementation'** in the header indicate that the following block of code will require additional functionality which you must provide. Instructions will be provided for each section and the specifics of the implementation are marked in the code block with a 'TODO' statement. Please be sure to read the instructions carefully!
# 
# In addition to implementing code, there will be questions that you must answer which relate to the project and your implementation. Each section where you will answer a question is preceded by a **'Question X'** header. Carefully read each question and provide thorough answers in the following text boxes that begin with **'Answer:'**. Your project submission will be evaluated based on your answers to each of the questions and the implementation you provide.  
# 
# >**Note:** Code and Markdown cells can be executed using the **Shift + Enter** keyboard shortcut. In addition, Markdown cells can be edited by typically double-clicking the cell to enter edit mode.

# ## Getting Started
# In this project, you will evaluate the performance and predictive power of a model that has been trained and tested on data collected from homes in suburbs of Boston, Massachusetts. A model trained on this data that is seen as a *good fit* could then be used to make certain predictions about a home — in particular, its monetary value. This model would prove to be invaluable for someone like a real estate agent who could make use of such information on a daily basis.
# 
# The dataset for this project originates from the [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/Housing). The Boston housing data was collected in 1978 and each of the 506 entries represent aggregated data about 14 features for homes from various suburbs in Boston, Massachusetts. For the purposes of this project, the following preprocessing steps have been made to the dataset:
# - 16 data points have an `'MEDV'` value of 50.0. These data points likely contain **missing or censored values** and have been removed.
# - 1 data point has an `'RM'` value of 8.78. This data point can be considered an **outlier** and has been removed.
# - The features `'RM'`, `'LSTAT'`, `'PTRATIO'`, and `'MEDV'` are essential. The remaining **non-relevant features** have been excluded.
# - The feature `'MEDV'` has been **multiplicatively scaled** to account for 35 years of market inflation.
# 
# Run the code cell below to load the Boston housing dataset, along with a few of the necessary Python libraries required for this project. You will know the dataset loaded successfully if the size of the dataset is reported.

# In[2]:


# Import libraries necessary for this project
import numpy as np                                # import Numpy library
import pandas as pd                               # import Pandas library
from sklearn.cross_validation import ShuffleSplit # import sklearn library
import matplotlib.pyplot as plt                   # import matplotlib library

# Import supplementary visualizations code visuals.py
import visuals as vs                              # import visuals library

# Pretty display for notebooks
get_ipython().magic(u'matplotlib inline')

import warnings

def warning_supress():
    warnings.warn("deprecated", DeprecationWarning)

with warnings.catch_warnings() as w:
    warnings.simplefilter("ignore")
    warning_supress()

# Load the Boston housing dataset
data = pd.read_csv('housing.csv')
prices = data['MEDV']
features = data.drop('MEDV', axis = 1)
    
# Success
print "Boston housing dataset has {} data points with {} variables each.".format(*data.shape)


# ## Data Exploration
# In this first section of this project, you will make a cursory investigation about the Boston housing data and provide your observations. Familiarizing yourself with the data through an explorative process is a fundamental practice to help you better understand and justify your results.
# 
# Since the main goal of this project is to construct a working model which has the capability of predicting the value of houses, we will need to separate the dataset into **features** and the **target variable**. The **features**, `'RM'`, `'LSTAT'`, and `'PTRATIO'`, give us quantitative information about each data point. The **target variable**, `'MEDV'`, will be the variable we seek to predict. These are stored in `features` and `prices`, respectively.

# ### Implementation: Calculate Statistics
# For your very first coding implementation, you will calculate descriptive statistics about the Boston housing prices. Since `numpy` has already been imported for you, use this library to perform the necessary calculations. These statistics will be extremely important later on to analyze various prediction results from the constructed model.
# 
# In the code cell below, you will need to implement the following:
# - Calculate the minimum, maximum, mean, median, and standard deviation of `'MEDV'`, which is stored in `prices`.
#   - Store each calculation in their respective variable.

# In[3]:


# TODO: Minimum price of the data
minimum_price = np.min(prices)

# TODO: Maximum price of the data
maximum_price = np.max(prices)

# TODO: Mean price of the data
mean_price = np.mean(prices)

# TODO: Median price of the data
median_price = np.median(prices)

# TODO: Standard deviation of prices of the data
std_price = np.std(prices)

# Show the calculated statistics
print "Statistics for Boston housing dataset:\n"
print "Minimum price: ${:,.2f}".format(minimum_price)
print "Maximum price: ${:,.2f}".format(maximum_price)
print "Mean price: ${:,.2f}".format(mean_price)
print "Median price ${:,.2f}".format(median_price)
print "Standard deviation of prices: ${:,.2f}".format(std_price)


# ### Question 1 - Feature Observation
# As a reminder, we are using three features from the Boston housing dataset: `'RM'`, `'LSTAT'`, and `'PTRATIO'`. For each data point (neighborhood):
# - `'RM'` is the average number of rooms among homes in the neighborhood.
# - `'LSTAT'` is the percentage of homeowners in the neighborhood considered "lower class" (working poor).
# - `'PTRATIO'` is the ratio of students to teachers in primary and secondary schools in the neighborhood.
# 
# 
# ** Using your intuition, for each of the three features above, do you think that an increase in the value of that feature would lead to an **increase** in the value of `'MEDV'` or a **decrease** in the value of `'MEDV'`? Justify your answer for each.**
# 
# **Hint:** This problem can phrased using examples like below.  
# * Would you expect a home that has an `'RM'` value(number of rooms) of 6 be worth more or less than a home that has an `'RM'` value of 7?
# * Would you expect a neighborhood that has an `'LSTAT'` value(percent of lower class workers) of 15 have home prices be worth more or less than a neighborhood that has an `'LSTAT'` value of 20?
# * Would you expect a neighborhood that has an `'PTRATIO'` value(ratio of students to teachers) of 10 have home prices be worth more or less than a neighborhood that has an `'PTRATIO'` value of 15?

# In[4]:


# Draw plotting the actual variables against the prices, and adding a trendline, 
# to visually inspect the correlations and there by arrive conclusions.

for col in features.columns:
    fig, ax = plt.subplots()
    # Use a linear fit to compute the trendline
    fit = np.polyfit(features [col], prices, deg=1) 
    ax.scatter(features [col],  prices)
    plt.plot(features [col], prices, 'o', color='blue')
    # This plots a trendline with the regression parameters computed earlier. 
    # We should plot this after the dots or it will be covered by the dots themselves
    ax.plot(features[col], fit[0] * features[col] + fit[1], color='blue', linewidth=3)
    # Display Title
    plt.title('PRICES vs  '+ str(col))
    # Display X-axis Label
    plt.xlabel(col)
    # Display Y-axis Label
    plt.ylabel('PRICES')


# **Answer: **
#   * Based on `'RM'` vs `'MEDV'`(Prices) plotgraph, Higher the `'RM'`, higher the `'MEDV'`. Because more rooms imply more space, leading to more cost.So `'RM'` of 6 worth less than `'RM'` of 7.
#   * Based on `'LSTAT'` vs `'MEDV'`(Prices) plotgraph, Higher the `'LSTAT'`, Lower the `'MEDV'`.`'LSTAT`' value(percent of lower class workers) of 15 have home prices be more worth than a neighborhood that has an `'LSTAT'` value of 20.
#   * Based on `'PTRATIO'` vs `'MEDV'`(Prices) plotgraph, Higher `'PTRATIO`', lower the `'MEDV'`. `'PTRATIO'` value(ratio of students to teachers) of 10 have home prices be worth more than a neighborhood that has an `'PTRATIO'` value of 15.
#   
#     
# 
# 

# In[5]:


fig1 = plt.figure()
ax1 = fig1.add_subplot(1, 1, 1)
n, bins, patches = ax1.hist(np.log(data.RM), bins = 20)
ax1.set_title('RM Log Transformation')
ax1.set_xlabel('RM')
ax1.set_ylabel('Frequency')

fig2 = plt.figure()
ax2 = fig2.add_subplot(1, 1, 1)
n, bins, patches = ax2.hist(np.log(data.LSTAT), bins = 20)
ax2.set_title('LSTAT Log Transformation')
ax2.set_xlabel('LSTAT')
ax2.set_ylabel('Frequency')

fig3 = plt.figure()
ax3 = fig3.add_subplot(1, 1, 1)
n, bins, patches = ax3.hist(np.log(data.PTRATIO), bins = 20)
ax3.set_title('PTRATIO Log Transformation')
ax3.set_xlabel('PTRATIO')
ax3.set_ylabel('Frequency')


# Note: Used log-transformation to deal with skewed data of RM, LSTAT, PTRATIO

# ----
# 
# ## Developing a Model
# In this second section of the project, you will develop the tools and techniques necessary for a model to make a prediction. Being able to make accurate evaluations of each model's performance through the use of these tools and techniques helps to greatly reinforce the confidence in your predictions.

# ### Implementation: Define a Performance Metric
# It is difficult to measure the quality of a given model without quantifying its performance over training and testing. This is typically done using some type of performance metric, whether it is through calculating some type of error, the goodness of fit, or some other useful measurement. For this project, you will be calculating the [*coefficient of determination*](http://stattrek.com/statistics/dictionary.aspx?definition=coefficient_of_determination), R<sup>2</sup>, to quantify your model's performance. The coefficient of determination for a model is a useful statistic in regression analysis, as it often describes how "good" that model is at making predictions. 
# 
# The values for R<sup>2</sup> range from 0 to 1, which captures the percentage of squared correlation between the predicted and actual values of the **target variable**. A model with an R<sup>2</sup> of 0 is no better than a model that always predicts the *mean* of the target variable, whereas a model with an R<sup>2</sup> of 1 perfectly predicts the target variable. Any value between 0 and 1 indicates what percentage of the target variable, using this model, can be explained by the **features**. _A model can be given a negative R<sup>2</sup> as well, which indicates that the model is **arbitrarily worse** than one that always predicts the mean of the target variable._
# 
# For the `performance_metric` function in the code cell below, you will need to implement the following:
# - Use `r2_score` from `sklearn.metrics` to perform a performance calculation between `y_true` and `y_predict`.
# - Assign the performance score to the `score` variable.

# In[6]:


# TODO: Import r2_score
from sklearn.metrics import r2_score

def performance_metric(y_true, y_predict):
    """ Calculates and returns the performance score between 
        true and predicted values based on the metric chosen. """
    
    # Calculate the performance score between 'y_true' and 'y_predict'
    score = r2_score(y_true, y_predict)
    
    # Return the score
    return score


# ### Question 2 - Goodness of Fit
# Assume that a dataset contains five data points and a model made the following predictions for the target variable:
# 
# | True Value | Prediction |
# | :-------------: | :--------: |
# | 3.0 | 2.5 |
# | -0.5 | 0.0 |
# | 2.0 | 2.1 |
# | 7.0 | 7.8 |
# | 4.2 | 5.3 |
# 
# Run the code cell below to use the `performance_metric` function and calculate this model's coefficient of determination.

# In[7]:


# Calculate the performance of this model
score = performance_metric([3, -0.5, 2, 7, 4.2], [2.5, 0.0, 2.1, 7.8, 5.3])
print "Model has a coefficient of determination, R^2, of {:.3f}.".format(score)


# * Would you consider this model to have successfully captured the variation of the target variable? 
# * Why or why not?
# 
# ** Hint: **  The R2 score is the proportion of the variance in the dependent variable that is predictable from the independent variable. In other words:
# * R2 score of 0 means that the dependent variable cannot be predicted from the independent variable.
# * R2 score of 1 means the dependent variable can be predicted from the independent variable.
# * R2 score between 0 and 1 indicates the extent to which the dependent variable is predictable. An 
# * R2 score of 0.40 means that 40 percent of the variance in Y is predictable from X.

# **Answer:**
# 
#     Model has a coefficient of determination(R^2) of 0.923, 
#     This indicates using this model 92.3 percentage of the target variable can be explained by the features
#     ie 92.3% of variation in dependent variable can be predicted from independent variable, which is fairly good fit.
#     
#     But note that R^2 does not indicate whether:
#         the independent variables are a cause of the changes in the dependent variable;
#         omitted-variable bias exists;
#         the correct regression was used;
#         the most appropriate set of independent variables has been chosen;
#         there is collinearity present in the data on the explanatory variables;
#         the model might be improved by using transformed versions of the existing set of independent variables;
#         there are enough data points to make a solid conclusion.
# 
#     Hence we cannot rely completely on coefficient of determination(R^2) to make any statistical conclusions.
#     If we assume above drawbacks are not present then we can say this model is fairly good fit.

# ### Implementation: Shuffle and Split Data
# Your next implementation requires that you take the Boston housing dataset and split the data into training and testing subsets. Typically, the data is also shuffled into a random order when creating the training and testing subsets to remove any bias in the ordering of the dataset.
# 
# For the code cell below, you will need to implement the following:
# - Use `train_test_split` from `sklearn.cross_validation` to shuffle and split the `features` and `prices` data into training and testing sets.
#   - Split the data into 80% training and 20% testing.
#   - Set the `random_state` for `train_test_split` to a value of your choice. This ensures results are consistent.
# - Assign the train and testing splits to `X_train`, `X_test`, `y_train`, and `y_test`.

# In[8]:


# Import 'train_test_split'
from sklearn.cross_validation import train_test_split

# Shuffle and split the data into training and testing subsets
X_train, X_test, y_train, y_test = train_test_split(features, prices,random_state=40, test_size=0.20)

# Success
print "Training and testing split was successful."


# ### Question 3 - Training and Testing
# 
# * What is the benefit to splitting a dataset into some ratio of training and testing subsets for a learning algorithm?
# 
# **Hint:** Think about how overfitting or underfitting is contingent upon how splits on data is done.

# **Answer: **
#         We can split the dataset into two(training,test)groups so that the model can be trained and tested on different data.
#         This allows testing accuracy is estimated better than training accuracy of out-of-sample performance.
# 

# ----
# 
# ## Analyzing Model Performance
# In this third section of the project, you'll take a look at several models' learning and testing performances on various subsets of training data. Additionally, you'll investigate one particular algorithm with an increasing `'max_depth'` parameter on the full training set to observe how model complexity affects performance. Graphing your model's performance based on varying criteria can be beneficial in the analysis process, such as visualizing behavior that may not have been apparent from the results alone.

# ### Learning Curves
# The following code cell produces four graphs for a decision tree model with different maximum depths. Each graph visualizes the learning curves of the model for both training and testing as the size of the training set is increased. Note that the shaded region of a learning curve denotes the uncertainty of that curve (measured as the standard deviation). The model is scored on both the training and testing sets using R<sup>2</sup>, the coefficient of determination.  
# 
# Run the code cell below and use these graphs to answer the following question.

# In[9]:


# Produce learning curves for varying training set sizes and maximum depths
vs.ModelLearning(features, prices)


# ### Question 4 - Learning the Data
# * Choose one of the graphs above and state the maximum depth for the model. 
# * What happens to the score of the training curve as more training points are added? What about the testing curve? 
# * Would having more training points benefit the model? 
# 
# **Hint:** Are the learning curves converging to particular scores? Generally speaking, the more data you have, the better. But if your training and testing curves are converging with a score above your benchmark threshold, would this be necessary?
# Think about the pros and cons of adding more training points based on if the training and testing curves are converging.

# **Answer: **
# 
#     max_depth = 1 Graph: 
#           Testing score(green line) increases with the number of training points.
#           But testing score increases only upto 0.4, which is very low score value.
#           This indicates this model does not generalize well for new/unseen data sets.
#           
#           Moreover, the training score (red line) decreases with the number of training points.
#           Also, the training score decreases to a very low score of approximately 0.4.
#           This indicates This model does not seem to fit the data well.
#                     
#           Thus, we can say this model is facing a high bias problem. 
#           Consequently, having more training points would not benefit the model as the model under fit the dataset.
#           Instead, one should increase the model complexity to better fit the dataset.
#           Morever, the testing score has reached a plateau suggesting the model may not improve from adding 
#           more training points.
# 
#     max_depth = 3 Graph: 
#           Testing score(green line) increases with the number of training points.
#           But testing score increases  upto 0.8, which is high score value comparatively
#           This indicates this model does generalize well for new/unseen data sets.
#           
#           Moreover, the training score (red line) decreases with the number of training points.
#           Also, the training score decreases to a very high score of approximately 0.8.
#           This indicates This model does fit the data set well.
#                     
#           Thus, we can say this model seems no high bias or high variance problem.
#           Model fits and generalizes well.
#           Consequently, having more training points would benefit the model to become idle one.
#           
#      max_depth = 6 Graph: 
#           Testing score(green line) increases with the number of training points.
#           But testing score increases  upto 0.75, which is not so high score value comparatively
#           This indicates this model does not generalize well for new/unseen data sets.
#           
#           Moreover, the training score (red line) slightly decreases with the number of training points.
#           Also, the training score decreases to a very high score of approximately 0.9.
#           This indicates This model does Overfitting dataset.
#                     
#           Thus, we can say this model to be a high variance problem.
#           Model Overfitting and not generalizes well.
#           Consequently, having more training points might benefit the model.        
#           
#        max_depth = 10 Graph: 
#           Testing score(green line) increases with the number of training points.
#           But testing score increases  upto 0.7, which is not so high score value comparatively
#           This indicates this model does not generalize well for new/unseen data sets.
#           
#           Moreover, the training score (red line) slightly decreases with the number of training points.
#           Also, the training score decreases to a very high score of approximately 1.0.
#           This indicates This model does Overfitting dataset.
#                     
#           Thus, we can say this model to be a very high variance problem.
#           Model Overfitting and not generalizes well.

# ### Complexity Curves
# The following code cell produces a graph for a decision tree model that has been trained and validated on the training data using different maximum depths. The graph produces two complexity curves — one for training and one for validation. Similar to the **learning curves**, the shaded regions of both the complexity curves denote the uncertainty in those curves, and the model is scored on both the training and validation sets using the `performance_metric` function.  
# 
# ** Run the code cell below and use this graph to answer the following two questions Q5 and Q6. **

# In[10]:


vs.ModelComplexity(X_train, y_train)


# ### Question 5 - Bias-Variance Tradeoff
# * When the model is trained with a maximum depth of 1, does the model suffer from high bias or from high variance? 
# * How about when the model is trained with a maximum depth of 10? What visual cues in the graph justify your conclusions?
# 
# **Hint:** High bias is a sign of underfitting(model is not complex enough to pick up the nuances in the data) and high variance is a sign of overfitting(model is by-hearting the data and cannot generalize well). Think about which model(depth 1 or 10) aligns with which part of the tradeoff.

# **Answer: **
#     
#     High variance models have a gap between the training and testing scores. 
#     This is because it is able to fit the model well but unable to generalize well 
#     resulting in a high training score but low test score.
#     
#     High bias models have have a small or no gap between the training and testing scores.
#     This is because it is unable to fit the model well and unable to generalize well
#     resulting in both scores converging to a similar low score.
# 
# 
# Decision tree(max depth 1) : 
#         Testing score of Low (~0.4),Training score of Low (~0.4) and observed small or no gap between
#         the training and testing scores. 
#         This is of High bias model because it is unable to fit the model well and unable to generalize
#         well resulting in both scores converging to a similar low score.
#         At this stage further adding more data points also model maynot peform well.
#         
#       Note: When the model is trained with a maximum depth of 1, model suffer from high bias.
# 
# Decision tree(max depth 10): 
#         Testing score of High (~0.7),  Training score of Low(~1.0) and observed substantial gap between
#         the training and testing scores
#         This is of High variance model because it is fitting data set well and not generalize well.
#         At this stage further adding more data points make  model peform well.
#         
#        Note: When the model is trained with a maximum depth of 10, model suffer from high variance

# ### Question 6 - Best-Guess Optimal Model
# * Which maximum depth do you think results in a model that best generalizes to unseen data? 
# * What intuition lead you to this answer?
# 
# ** Hint: ** Look at the graph above Question 5 and see where the validation scores lie for the various depths that have been assigned to the model. Does it get better with increased depth? At what point do we get our best validation score without overcomplicating our model? And remember, Occams Razor states "Among competing hypotheses, the one with the fewest assumptions should be selected."

# **Answer: ** 
# 
# We should use the model with max depth > 3, since it has the lowest validation error. To put it another way, it's best prediction capability ispossible even with new data.

# -----
# 
# ## Evaluating Model Performance
# In this final section of the project, you will construct a model and make a prediction on the client's feature set using an optimized model from `fit_model`.

# ### Question 7 - Grid Search
# * What is the grid search technique?
# * How it can be applied to optimize a learning algorithm?
# 
# ** Hint: ** When explaining the Grid Search technique, be sure to touch upon why it is used,  what the 'grid' entails and what the end goal of this method is. To solidify your answer, you can also give an example of a parameter in a model that can be optimized using this approach.

# **Answer: **
# 
#    Grid search technique:
#            allows to define a grid of parameters.
#            exhaustively tries every combination of the provided hyper-parameter values in order to find the best model.
#            allows to easily evaluate validation error and pick the best set of parameters to employ.
#            allows to find the highest cross-validation accuracy that matches with the corresponding parameters
#            that optimizes the learning algorithm.
#            have time complexity for h parameters is O(n^h).

# ### Question 8 - Cross-Validation
# 
# * What is the k-fold cross-validation training technique? 
# 
# * What benefit does this technique provide for grid search when optimizing a model?
# 
# **Hint:** When explaining the k-fold cross validation technique, be sure to touch upon what 'k' is, how the dataset is split into different parts for training and testing and the number of times it is run based on the 'k' value.
# 
# When thinking about how k-fold cross validation helps grid search, think about the main drawbacks of grid search which are hinged upon **using a particular subset of data for training or testing** and how k-fold cv could help alleviate that. You can refer to the [docs](http://scikit-learn.org/stable/modules/cross_validation.html#cross-validation) for your answer.

# **Answer: **
# 
#     K-fold cross-validation technique:
#         Dataset is split into K "folds" of equal size.
#         Each fold acts as the testing set 1 time, and acts as the training set K-1 times.
#         Average testing performance is used as the estimate of out-of-sample performance.
#         Also known as cross-validated performance.
#         
#     Benefits of k-fold cross-validation:
#         More reliable estimate of out-of-sample performance than train/test split.
#         Reduce the variance of a single trial of a train/test split.
#         Hence, with the benefits of k-fold cross-validation, we're able to use the average testing accuracy
#         as a benchmark to decide which is the most optimal set of parameters for the learning algorithm.
#         If we do not use a cross-validation set and we run grid-search, we would have different sets of 
#         optimal parameters due to the fact that without a cross-validation set, the estimate of out-of-sample
#         performance would have a high variance.
#         In summary, without k-fold cross-validation the risk is higher that grid search will select hyper-parameter value
#         combinations that perform very well on a specific train-test split but poorly otherwise.
# 

# ### Implementation: Fitting a Model
# Your final implementation requires that you bring everything together and train a model using the **decision tree algorithm**. To ensure that you are producing an optimized model, you will train the model using the grid search technique to optimize the `'max_depth'` parameter for the decision tree. The `'max_depth'` parameter can be thought of as how many questions the decision tree algorithm is allowed to ask about the data before making a prediction. Decision trees are part of a class of algorithms called *supervised learning algorithms*.
# 
# In addition, you will find your implementation is using `ShuffleSplit()` for an alternative form of cross-validation (see the `'cv_sets'` variable). While it is not the K-Fold cross-validation technique you describe in **Question 8**, this type of cross-validation technique is just as useful!. The `ShuffleSplit()` implementation below will create 10 (`'n_splits'`) shuffled sets, and for each shuffle, 20% (`'test_size'`) of the data will be used as the *validation set*. While you're working on your implementation, think about the contrasts and similarities it has to the K-fold cross-validation technique.
# 
# Please note that ShuffleSplit has different parameters in scikit-learn versions 0.17 and 0.18.
# For the `fit_model` function in the code cell below, you will need to implement the following:
# - Use [`DecisionTreeRegressor`](http://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeRegressor.html) from `sklearn.tree` to create a decision tree regressor object.
#   - Assign this object to the `'regressor'` variable.
# - Create a dictionary for `'max_depth'` with the values from 1 to 10, and assign this to the `'params'` variable.
# - Use [`make_scorer`](http://scikit-learn.org/stable/modules/generated/sklearn.metrics.make_scorer.html) from `sklearn.metrics` to create a scoring function object.
#   - Pass the `performance_metric` function as a parameter to the object.
#   - Assign this scoring function to the `'scoring_fnc'` variable.
# - Use [`GridSearchCV`](http://scikit-learn.org/0.17/modules/generated/sklearn.grid_search.GridSearchCV.html) from `sklearn.grid_search` to create a grid search object.
#   - Pass the variables `'regressor'`, `'params'`, `'scoring_fnc'`, and `'cv_sets'` as parameters to the object. 
#   - Assign the `GridSearchCV` object to the `'grid'` variable.

# In[12]:


# Import 'make_scorer', 'DecisionTreeRegressor', and 'GridSearchCV'
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import make_scorer
from sklearn.grid_search import GridSearchCV

def fit_model(X, y):
    """ Performs grid search over the 'max_depth' parameter for a 
        decision tree regressor trained on the input data [X, y]. """
    
    # Create cross-validation sets from the training data
    # sklearn version 0.18: ShuffleSplit(n_splits=10, test_size=0.1, train_size=None, random_state=None)
    # sklearn versiin 0.17: ShuffleSplit(n, n_iter=10, test_size=0.1, train_size=None, random_state=None)
    cv_sets = ShuffleSplit(X.shape[0], n_iter = 10, test_size = 0.20, random_state = 0)

    # TODO: Create a decision tree regressor object
    regressor = DecisionTreeRegressor(random_state=0)

    # TODO: Create a dictionary for the parameter 'max_depth' with a range from 1 to 10
    dt_range = range(1, 11)
    params = dict(max_depth=dt_range)

    # TODO: Transform 'performance_metric' into a scoring function using 'make_scorer' 
    scoring_fnc = make_scorer(performance_metric)

    # TODO: Create the grid search cv object --> GridSearchCV()
    # Make sure to include the right parameters in the object:
    # (estimator, param_grid, scoring, cv) which have values 'regressor', 'params', 'scoring_fnc', and 'cv_sets' respectively.
    grid = GridSearchCV(regressor, params, cv=cv_sets, scoring=scoring_fnc)

    # Fit the grid search object to the data to compute the optimal model
    grid = grid.fit(X, y)

    # Return the optimal model after fitting the data
    return grid.best_estimator_


# ### Making Predictions
# Once a model has been trained on a given set of data, it can now be used to make predictions on new sets of input data. In the case of a *decision tree regressor*, the model has learned *what the best questions to ask about the input data are*, and can respond with a prediction for the **target variable**. You can use these predictions to gain information about data where the value of the target variable is unknown — such as data the model was not trained on.

# ### Question 9 - Optimal Model
# 
# * What maximum depth does the optimal model have? How does this result compare to your guess in **Question 6**?  
# 
# Run the code block below to fit the decision tree regressor to the training data and produce an optimal model.

# In[13]:


# Fit the training data to the model using grid search
reg = fit_model(X_train, y_train)

# Produce the value for 'max_depth'
print "Parameter 'max_depth' is {} for the optimal model.".format(reg.get_params()['max_depth'])


# ** Hint: ** The answer comes from the output of the code snipped above.
# 
# **Answer: ** 'max_depth' is 4 for the optimal model.  
# Based on visual diagrams we udnerstand only model with depth > 3 needs to be considered for better performace. but based on fitmodel API results,it is event that 'max_depth' is 4 for the optimal model.

# ### Question 10 - Predicting Selling Prices
# Imagine that you were a real estate agent in the Boston area looking to use this model to help price homes owned by your clients that they wish to sell. You have collected the following information from three of your clients:
# 
# | Feature | Client 1 | Client 2 | Client 3 |
# | :---: | :---: | :---: | :---: |
# | Total number of rooms in home | 5 rooms | 4 rooms | 8 rooms |
# | Neighborhood poverty level (as %) | 17% | 32% | 3% |
# | Student-teacher ratio of nearby schools | 15-to-1 | 22-to-1 | 12-to-1 |
# 
# * What price would you recommend each client sell his/her home at? 
# * Do these prices seem reasonable given the values for the respective features? 
# 
# **Hint:** Use the statistics you calculated in the **Data Exploration** section to help justify your response.  Of the three clients, client 3 has has the biggest house, in the best public school neighborhood with the lowest poverty level; while client 2 has the smallest house, in a neighborhood with a relatively high poverty rate and not the best public schools.
# 
# Run the code block below to have your optimized model make predictions for each client's home.

# In[14]:


# Produce a matrix for client data
client_data = [[5, 17, 15], # Client 1
               [4, 32, 22], # Client 2
               [8, 3, 12]]  # Client 3

# Show predictions
for i, price in enumerate(reg.predict(client_data)):
    print "Predicted selling price for Client {}'s home: ${:,.2f}".format(i+1, price)


# **Answer: **
# 
#     Recommend Price as follows:
#         Client 1: 411,000
#         Client 2: 219,900
#         Client 3: 921,900
# 

# Pro tip: Assess Reasonableness of Prediction using NearestNeighbors
# 
#     To assess if your prediction is reasonable, besides from comparing it with the median, the mean and checking if it is included in one standard deviation range, you could use SKlearn to find the nearest neighbours of the feature vector.
#     You can then contrast your results with the closest neighbours, the ones that have similar characteristics.
# 

# In[15]:


from sklearn.neighbors import NearestNeighbors
num_neighbors=10
def nearest_neighbor_price(x):
    def find_nearest_neighbor_indexes(x, X):  # x is your vector and X is the data set.
        neigh = NearestNeighbors( num_neighbors )
        neigh.fit(X)
        distance, indexes = neigh.kneighbors( [x] )
        return indexes
    indexes = find_nearest_neighbor_indexes(x, features)
    sum_prices = []
    for i in indexes:
        sum_prices.append(prices[i])
    neighbor_avg = np.mean(sum_prices)
    return neighbor_avg
index = 0  
for i in client_data:
    val=nearest_neighbor_price(i)
    index += 1
    print "The predicted {} nearest neighbors price for Client {} Home is: ${:,.2f}".format(num_neighbors,index, val)


# Based on Assess Reasonableness of Prediction using NearestNeighbors, it is evidant that customers can recommended to sell their Houses as predicted below:
# 
#         Client 1: 411,000
#         Client 2: 219,900
#         Client 3: 921,900
# Predicted prices are slightly higer than nearest neighbors price.

# Based on Data Exploration:
# 
#     Minimum price: $105,000.00
#     Maximum price: $1,024,800.00
#     Mean price: $454,342.94
#     Median price $438,900.00
#     Standard deviation of prices: $165,171.13

# Conclusions:
#     The prices are rounded up to the nearest hundred as the prices in the dataset are all rounded to the nearest hundred.
#     
#     The house prices of client 1 and client 2 are below the mean and median prices of Data Explortion findings.
#     client 3 prices are way above the mean and median price of Data Explortion findings.
#     
#     Client 2 prices are lower side because of lesser rooms,high Neighborhood poverty level(%) and high student-to-teacher ratio.
#     
#     Client 1 prices are average because of average rooms, average Neighborhood poverty level(%) and average student-to-teacher ratio.
#     
#     Client 3 prices are more because of more rooms, less Neighborhood poverty level(%) and more student-to-teacher ratio.
#    
#     The model predicts well and recommends prices for client houses. 

# ### Sensitivity
# An optimal model is not necessarily a robust model. Sometimes, a model is either too complex or too simple to sufficiently generalize to new data. Sometimes, a model could use a learning algorithm that is not appropriate for the structure of the data given. Other times, the data itself could be too noisy or contain too few samples to allow a model to adequately capture the target variable — i.e., the model is underfitted. 
# 
# **Run the code cell below to run the `fit_model` function ten times with different training and testing sets to see how the prediction for a specific client changes with respect to the data it's trained on.**

# In[16]:


vs.PredictTrials(features, prices, fit_model, client_data)


# ### Question 11 - Applicability
# 
# * In a few sentences, discuss whether the constructed model should or should not be used in a real-world setting.  
# 
# **Hint:** Take a look at the range in prices as calculated in the code snippet above. Some questions to answering:
# - How relevant today is data that was collected from 1978? How important is inflation?
# - Are the features present in the data sufficient to describe a home? Do you think factors like quality of apppliances in the home, square feet of the plot area, presence of pool or not etc should factor in?
# - Is the model robust enough to make consistent predictions?
# - Would data collected in an urban city like Boston be applicable in a rural city?
# - Is it fair to judge the price of an individual home based on the characteristics of the entire neighborhood?

# **Answer: **  Definetely data collected in 1978 cann't be used to predict accurate rates now. May be lot of other features need to be considered for better prediction.
# This Model is not robust enough because it is not considered all the features.
# No data collected in an urban city like Boston cannot be applicable in a rural city
# Yes, it is fair to judge the price of an individual home based on the characteristics of the entire neighborhood.This is one feature only but addtional features to be considered for better prediction.

# > **Note**: Once you have completed all of the code implementations and successfully answered each question above, you may finalize your work by exporting the iPython Notebook as an HTML document. You can do this by using the menu above and navigating to  
# **File -> Download as -> HTML (.html)**. Include the finished document along with this notebook as your submission.
