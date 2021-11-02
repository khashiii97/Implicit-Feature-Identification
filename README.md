# Implicit-Feature-Identification
## NLP - identifying implicit Persian features of opinions from the SentiPers dataset

This repository hosts an implementation of part of the procedure "Implicit feature identification via co-occurrence association rule mining", as stated in the [original paper](https://link.springer.com/chapter/10.1007/978-3-642-19400-9_31) with the data being obtained from the [SentiPers](https://github.com/phosseini/SentiPers) dataset. To be more precise, two parts of the procedure have been implemented:
- Mining association rules using the Co-occurence matrix.
- Creating the contextual feature vectors for clustering, as stated in the paper "Generating a concept hierarchy for sentiment analysis" in [here](https://ieeexplore.ieee.org/abstract/document/4811294/).
</ul>the results of this two parts are stored in the result directory.
<br/>SentiPers consists of numerous reviews, each having their opinions and targets labeled, thus being very beneficial for Sentiment Analysis.


<br/>The clustering part of this procedure is still to be done, and maybe I'll tackle that in the feature. Also, In this project, a rigorous preprocessing procedure has been applied (Stopwords, rephrasing slangs, etc.) to produce the best input for our model. Nevertheless, there is still room for improvement, so feel free to modify the data or contribute in completing the project. Contact me in case of any questions.

