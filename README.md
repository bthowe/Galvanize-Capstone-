# Galvanize-Capstone-

#Project Overview
For this capstone project I partnered with a veterinary and pharmaceutical consultancy. They are interested in understanding whether the Costco effect holds in the context of veterinary practices. In the business world, the “Costco effect” is often used to describe the homogeneous and limited selection of goods for a given category of merchandise sold within wholesale warehouse clubs like Costco and Sam’s Club. For example, King Soopers offers over five different brands of peanut butter in at three different sizes each. Peanut butter at Costco comes in packages of 2, 48 oz. jars, and there are two maybe three brands to choose from. These wholesalers likely do this because they have found it increases profits. Ultimately, this consultancy is interested in understanding whether pharmaceutical sales at veterinary clinics would increase if the brands of heartworm and flea/tick medications were restricted to two or three rather than the ten or so currently on the market. 

Using this consultancy’s database, which is comprised of data from clinics throughout the United State, I test two hypotheses using multivariable linear regression: (1) total heartworm medication sales is decreasing in the number of heartworm pharmaceutical brands a clinic offers, and (2) total flea medication sales is decreasing in the number of heartworm pharmaceutical brands a clinic offers. 

The following displays the distributions of and correlations between the relevant variables (the data is clinic-level).
###Correlations and Distributions of Outcomes and Covariates
![alt text](https://github.com/bthowe/Galvanize-Capstone-/blob/master/images/var_distributions.png "Scatter matrix")

For both flea and heartworm medications, I estimate eight specifications of the linear model corresponding to four different outcome variables (doses sold, doses sold per customer, the natural log of doses sold, and the natural log of doses sold per customer (since doses sold and doses sold per customer are right skewed)) and two different key explanatory variables (a continuous and dummy version of the number of brands of a given medication type sold (high (6-8 brands), medium (4-5 brands), and low (1-3 brands) categories were created to generate the dummies (the medium is the baseline category in the regression))). The following diagrams display the results of these sixteen regressions.
###Flea Medications
![alt text](https://github.com/bthowe/Galvanize-Capstone-/blob/master/images/coef_flea.png "Flea results")
###Heartworm Medications
![alt text](https://github.com/bthowe/Galvanize-Capstone-/blob/master/images/coef_heartworm.png "Heartworm results")

Confidence intervals are calculated using robust estimates of the standard errors. We see that none of the estimates is significant (since 0 falls within the confidence intervals). Therefore, while I consider these results preliminary, I find no significant relationship between number of brands and sales. 

Moving forward, there are a few things I would do in order to improve the internal and external consistency of these estimates. First, there may be profit benefits from price discrimination (i.e., a pet owner may not purchase heartworm meds at $20 per dose but would at $10 per dose). Thus, conditioning on price point may improve the estimates. Second, while the data used in this analysis is clinic-level data, it may be possible to disaggregate to get customer-level data which would allow for a hierarchal model (which would allow for both clinic and customer effects in the model). Third, appropriate counterfactuals are vital in causal analysis. Balancing on the feature set would help ensure the types of organizations  across the levels of brands offered are similar. 


#Files Contained in this Repo
Contained in this repo are (1) an annotated draft of the slides I presented during the Galvanize DSI capstone showcase, (2) a folder containing the python and Stata code I used to extract, process, and analysis the data. In this folder, the file...

-allydvm_table_download.py was used to fetch data from the MySQL database

-variable_construct_heartworm.py was used to construct relevant variables used in the heartworm medication regression

-variable_construct_flea.py was used to construct relevant variables used in the flea medication regression

-covariate_balancing.py was used to create various diagrams depicting the inital distributions of the variables and the results of the regressions

-flea_regress.do is a Stata file used to run the regressions
