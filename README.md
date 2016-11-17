# Galvanize-Capstone-
For this capstone project I partnered with a veterinary and pharmaceutical consultancy. They are interested in understanding whether the Costco effect holds in the context of veterinary practices. In the business world, the “Costco effect” is often used to describe the homogeneous and limited selection of goods for a given category of merchandise sold within wholesale warehouse clubs like Costco and Sam’s Club. For example, King Soopers offers over five different brands of peanut butter in at three different sizes each. Peanut butter at Costco comes in packages of 2, 48 oz. jars, and there are two maybe three brands to choose from. These wholesalers likely do this because they have found it increases profits. Ultimately, this consultancy is interested in understanding whether pharmaceutical sales at veterinary clinics would increase if the brands of heartworm and flea/tick medications were restricted to two or three rather than the ten or so currently on the market. 


Using this consultancy’s database, which is comprised of data from clinics throughout the United State, I test two hypotheses using multivariable linear regression: (1) total heartworm medication sales is decreasing in the number of heartworm pharmaceutical brands a clinic offers, and (2) total flea medication sales is decreasing in the number of heartworm pharmaceutical brands a clinic offers. 


While I consider these results preliminary, I find no significant relationship between number of brands and sales. 


Contained in this repo are (1) an annotated draft of the slides I presented during the Galvanize DSI capstone showcase, (2) a folder containing the python and Stata code I used to extract, process, and analysis the data. In this folder, the file...
*allydvm_table_download.py was used to fetch data from the MySQL database
*variable_construct_heartworm.py was used to construct relevant variables used in the heartworm medication regression
*variable_construct_flea.py was used to construct relevant variables used in the flea medication regression
*covariate_balancing.py was used to create various diagrams depicting the inital distributions of the variables and the results of the regressions
*flea_regress.do is a Stata file used to run the regressions
