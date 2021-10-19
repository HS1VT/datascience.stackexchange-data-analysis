Answer:

The graph of the distribution resembles a ‘wrapped exponential distribution’ as can be seen in figure 1 which is a graph plotted between the number of times a post is viewed and its frequency. The graph shows that a significantly large number of posts have small view counts and as the view count increases, the number of posts with that view count decreases drastically.

The file top10.py will have to be used on reducer output to get the 10 most viewed posts.

Top 10 most viewed posts:
1)  Title: ValueError: Input contains NaN, infinity or a value too large for dtype(‘float32’)
    Asked by: Edamame
    Tags: python, scikit-learn, pandas, random-forest, python-3.x
    Current number of views(approx): 332k
The question posted is that when the above-mentioned error is encountered while predicting test data using a RandomForest model, how can one find the values in the test dataset that are leading to the error. 
The most liked answer to the post gives 3 commands by which one can a) get a boolean mask that is true for positions containing NaNs; b) return a tuple with i,j coordinates of NaNs; and c) replace NaNs with 0 and inf with finite numbers. Another solution is also given for replacing the records having missing values with mean/median imputation of these values instead of completely dropping them. This prevents loss of information.

2)  Title: How to get correlation between two categorical variables and a categorical variable and continuous variable?
    Asked by: GeorgeOfTheRF
    Tags: r, statistics, correlation
    Current number of views(approx): 315k
The question posted is regarding the use correlation coefficient. The user states the types of variables they need to check correlation between, and asks suggestions for the best correlation coefficient in the mentioned cases and the assumptions to keep in mind. They also ask for a method to implement these in R and SAS.
The most liked solution states that independence of two categorical variables can be tested using Chi-squared test of independence. For categorical vs numerical variables, One-way ANOVA test can be used.

3)  Title: How to set class weights for imbalanced classes in Keras?
    Asked by: Hendrik
    Tags: deep-learning, classification, keras, weighted-data
    Current number of views(approx): 309k
The question posted is regarding Keras which is an open-source software library that provides a python interface for artificial neural networks. The user wants to know about the use of fit() library in Keras. 
The most liked answer states that in order to force the algorithm to treat every instance of class 1 as 50 instances of class 0, one has to define a dictionary with labels and their associated weights and then feed the dictionary as a parameter to fit method.

4)  Title: What's the difference between fit and fit_transform in scikit-learn models?
    Asked by: Kaggle
    Tags: python, scikit-learn
    Current number of views(approx): 301k
In the post, the user wants to know the difference between the fit and the fit_transform methods in scikit-learn and the need to transform data.
The most liked answer to the post states that the training set of the data is centered using mean and standard deviation. Once this is done on the training set of the data, the same transformation has to be applied to the test set with the exact same parameters (mean and standard deviation) as used for the training set. Hence, scikit-learn’s transform’s fit() calculates these parameters and then its transform() method applies it to the test data. But, fit_transform() performs both these functions when called once.

5)  Title: How do I compare columns in different data frames?
    Asked by: a_a_a
    Tags: pandas, dataframe
    Current number of views(approx): 288k
In the post, the user wants to compare one column of a DataFrame with a column of  another. 
The most liked answer gives pd.merge command to join the two DataFrames (using the desired column as a key) to give a new DataFrame that combines the information of both inputs.

6)  Title: Micro Average vs Macro average Performance in a Multiclass classification setting
    Asked by: SHASHANK GUPTA
    Tags: multiclass-classification, evaluation
    Current number of views: 262k
In the post, the user has given the performance that he is getting from training a multiclass classifier. The micro average performances are equal and the macro average performances are lower, the reason for which is unclear.
The most liked answer clarifies that a macro average calculates the metric independently for each class and then takes average whereas micro aggregates the contribution of all classes to compute the average metric. Hence, the difference in performances. Micro average is preferable incase there is a possibility of imbalance.  

7)  Title: train_test_split() error: Found input variables with inconsistent numbers of samples
    Asked by: josh_gray
    Tags: python, scikit-learn, sampling
    Current number of views(approx): 265k
In the post, the user is getting the above mentioned error and wants a way to resolve it.
The most liked answer attributes this error to the unequal lengths of the two arrays being considered. It is suggested that the user transposes the first array to get an equal number of elements in both arrays to solve the error.

8)  Title: K-Means clustering for mixed numeric and categorical data
    Asked by: IharS
    Tags: data-mining, clustering, octave, k-means, categorical-data
    Current number of views(approx): 251k
In the post, the user wants to use the k-means clustering algorithm on a dataset containing several numeric and a categorical attribute. So, they want to know if it is fine to split the categorical attribute into a number of numeric variables.
The most liked answer states that the standard k-means algorithm isn’t directly applicable to categorical data as it is discrete and doesn;t have a natural origin. Instead the use of a variant, k-modes is suggested which is suitable for categorical data.

9)  Title: How to draw Deep learning network architecture diagrams?
    Asked by: Case Msee
    Tags: machine-learning, neural-network, deep-learning, svm, software-recommendation
    Current number of views(approx): 247k
In the post, the user has built his model and wants to know how to draw network architecture diagrams.
The most liked answer suggests an online tool, NN-SVG that produces network architecture schematics.

10) Title: What are deconvolutional layers?
    Asked by: Martin Thoma
    Tags: neural-network, convnet, convolution
    Current number of views(approx): 242k
In the post, the user wants to understand deconvolultional layers, already having some idea about how convolutional layers are trained.
The most liked answer states that deconvolutional layers are transposed convolutional layers. For this, the original input is padded with zeros.



Explanation of the code:

For the graph, after using cat command as usual, the output was sorted before storing in Out_sorted.txt, using the command 
‘cat Posts.xml | ./mapper3b.py | sort | ./reducer3b.py | sort -n -k1 -r > Out_sorted.txt’ .
This sorted output file is read line by line. The key i.e viewcount is plotted on the x axis and the value i.e the number of posts having this particular viewcount on y axis, using matplotlib library. The code is given in ‘plot3b.py’ and the plotted graph is given in ‘graph3b.png’.

For the top 10 most viewed posts, an empty list is taken. 
For each incoming line, a tuple of the format (‘viewcount’, ‘titles’) wherein titles is a list containing the titles of all the posts with the same viewcount is made. 
While the length of the list is less than 10, the value of viewcount is compared one by one with the viewcounts in the tuples already present and inserted in the place where it comes out to be smaller, or appended at the end of the list. This gives us a list of tuples sorted in ascending order of the viewcount values. 
Once the list has 10 elements, the viewcount of each successive tuple is compared to the viewcounts in the tuples already present, if it is greater than any one of them, it is inserted at the right place and the tuple with smallest viewcount i.e the first element of the initial list is removed. In this manner, once all the lines have been taken in, the list finally has the elements with the highest viewcount. 
The code is given in ‘top10.py’.






 


