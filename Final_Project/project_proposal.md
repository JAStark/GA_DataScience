<h1>Final Project Proposal</h1>

<h3>Proposal A</h3>
<h4>Predicting the **Identification Potential** of unidentified persons</h4>

The NamUs database (https://identifyus.org/en) has 10474 open cases, currently, with data for each case organised in a structured way (unlike The Doe Network http://www.doenetwork.org). Also unlike other databases, this one has an **Identification Potential** score with stars 1-5 denoting low, low-medium, medium, medium-high, and high potential of identification. 

I would like to determine the features of case files that lead to these scores. Features include presence/absence of images, GPS location, physical descriptions, circumstances assicated with the case. Some details are estimates, such age. Is it more likely for someone with an age range of 20 years less likley to be indentified than someone with a range of 5 years. 

I hypothesis that it is not merely that more data on a person leads to a higher likelyhood of identification. Rather, that some features are more helpful than others. 

This data could be used to facilitate law enforcement prioritise data collection, or acting on certain types of data, making the investigation more effective and efficient. It could also be applied to other databases that don't use a rating system. Of course, it could also turn out that the rating system is entirely arbitrarily and/or inconsistenly decided by some human being!


<h3>Proposal B</h3>
<h4>Searching for Possible Matches between Missing and Unidenfified Persons Databases</h4>

While exploring the Doe Network database (http://www.doenetwork.org), I noticed that there were a number of closed cases where the person in question was in both the Missing _and_ Unidentified databases under different case file numbers. The data is extremeley unstructured _and_ inconsistent between cases, but all - or the vase majority _do_ have images associated with them. 

Using images only, I would like to use facial recognition to indentify matches within some probability. This would consist of unsupervised learning. To improve its precision, I would add other parts of each case, like distinguishing features, or missing/found dates. Actually, the outcomes of Proposal A would benefit Proposal B in terms of deciding features to add...

I'll probably do this project for fun in my own time...