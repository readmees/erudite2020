# Polynomial fitting and random forrest on Autonomous Greenhouses 1st Edition data
![](https://imgur.com/3vLMjnG.gif)
## About us
Erudite is a group of 5 motivated Artificial Intelligence second year bachelor students. We are Riemer Dijkstra, Otto Márton, Dionne Gantzert, Johannes Roelink and Mees Meester. For the 'Tweedejaarsproject' our group has been assigned to a company, Sigrow. They came up with a challenge for us to solve in four weeks.

## Introduction
*This introduction can be found in erudite2020/Final Report for University of Amsterdam/Final Report.pdf*

Sigrow is a company in the Netherlands which provides state of the art sensor technology tailored to greenhouses. These sensors make it possible for Sigrow’s clients to stay ahead of the curve and make those calculated decisions. Since the horticulture industry is very competitive, growers try to find any competitive advantage they can. This means that most businesses that utilize Artificial Intelligence (AI) closely guard their results and techniques and rarely offer them publicly for free. This means that Sigrow has little knowledge about AI and that is why a collaboration of the two fields was needed. Our group of AI students have been given the opportunity to establish this combination with Sigrow.
Over the years, Sigrow has gathered information about the environment in the greenhouses, such as the temperature, air humidity, light intensity and amount of carbon dioxide (CO2) in the air. These four features are the most important factors for plants to grow, apart from water and nutrition (Hemming et al., 2019). The task Sigrow had for our group was to optimize plant growth by optimizing the greenhouse climate using  AI. This task was dubbed the ‘Sigrow Challenge’. For the completion of this challenge, the earlier mentioned greenhouse information was combined in order to create a dataset. 

When Sigrow provided this dataset, there were two significant problems:
The data lacked information about the plants.
The amount of data was scarce. 

Sigrow has only collected data about the environment of the plants, but not the plants themselves. The data we received from Sigrow did not contain any information about which kind of plant it was, nor the height, stem diameter or weight (1). In addition to this, the amount of data was so scarce that it was impossible to split the dataset into a training and test set (2). The importance of useful and substantial data is explained in the next section of the text. 

Because of the two problems, a new challenge was set up, consisting of two parts.
The first part involved a recommendation. This recommendation had to meet a number of requirements. First, it had to contain a comprehensive analysis about the measurements Sigrow is currently taking. This includes advice about which measurements need to be done and why. This part of the recommendation is meant to inform Sigrow about the importance of useful data and how to acquire that. Second, it had to contain a comprehensive overview of possible feature optimization techniques which Sigrow could use for future work. At last, the recommendation had to contain an understandable explanation about several machine learning techniques.
Besides the recommendation, Sigrow also asked to attempt several discussed implementations.  This is the second part of the proposed challenge. This part  is similar to the initial Sigrow Challenge. Since the data is not usable, the results would be unreliable. However, Sigrow could utilize the results of attempted implementations in the future.  A framework would already be of great help for the company. By providing Sigrow a recommendation on how to optimize the plant growth using machine learning and implementing these techniques for them, we hope Sigrow can optimize the plant growth in the future and stay ahead of the curve.

## The /erudite2020 Github repository
This repository contains of two repositories. The ['/Final Report/'](<Final Report/>) repository contains the report we wrote for the Univisity of Amsterdam. In the ['/Polynomial Regression and Random Forest/'](<Polynomial Regression and Random Forest/>) repository the models made for Sigrow and the data can be found. The data is retrieved from the Automonous greenhouse challenge, a challenge where five teams tried to grow the best and most environmentally friendly plants. The source of the data can be found [here](https://data.4tu.nl/repository/uuid:e4987a7b-04dd-4c89-9b18-883aad30ba9a#DATA). The data is divided in six directories, one for every team and one for a reference (plants grown without the help of AI). Each of those directories contains in 5 datasets. CropManagement.csv, Greenhouse_climate.csv, Irrigation.csv, Production.csv, ResourceCalculations.csv and vip.csv. 
### Using the polynomial fit model
The [polynomial_fit.ipynb](<Polynomial Regression and Random Forest/polynomial_fit.ipynb/>) is made interactive, by asking for user input. The program is run as follows. If you are not familiar with Jupytor Notebook, [here](https://www.datacamp.com/community/tutorials/tutorial-jupyter-notebook?utm_source=adwords_ppc&utm_campaignid=898687156&utm_adgroupid=48947256715&utm_device=c&utm_keyword=&utm_matchtype=b&utm_network=g&utm_adpostion=&utm_creative=332602034352&utm_targetid=dsa-473406581035&utm_loc_interest_ms=&utm_loc_physical_ms=9065312&gclid=EAIaIQobChMI143hk6yb6gIVlUMYCh2a6wDJEAAYASAAEgIwvPD_BwE) is a handy tutorial.

We tried to make the Jupyter Notebook as user friendly as possible, so if all cells are run the user will be asked for input, like the directory of the datasets and if the data needs to be divided by weekly data (to create more usable data). The Jupyter Notebook can be used on more data as well. So every time the growth of a plant is measured the data can simply be added in [Polynomial Regression and Random Forest/data/](<Polynomial Regression and Random Forest/data/>) repository(for example the data of the 5 teams of the greenhouse challenge). Please make sure the directory you add with data has the same directories and features as the one in the greenhouse challenge.

## Results
### Cleaned data
Because of missing data points and inconsistent units of measurement, the data had to be cleaned in order to be useful. Missing data points were replaced with the previously known value using ffill, a built in function of the Pandas Python library. If the first datapoint was missing, we replaced the NaN value with the next known value using Bfill, also from the Pandas library. For ease of use we combined all the data in one large Python dictionary, with the keys being the different teams that competed for the challenge and the values being the environmental and plant data.

### Random forest
[randomforest.ipynb](<Polynomial Regression and Random Forest/randomforest.ipynb/>) is used to find the feature importance in the dataset Greenhouse_climate.csv for different teams. The feature importances are found by using a random forest classifier. The results shown in the figures below are the feature importances of the features in the greenhouse climate datasets.

![](https://imgur.com/mMthsX6.png) ![](https://imgur.com/xPIJtlk.png) 
![](https://imgur.com/ABIU4m2.png) ![](https://imgur.com/mbGukqX.png)
![](https://imgur.com/5gauDK6.png) ![](https://imgur.com/jIrGrvA.png) 

For more clarification of the what the features mean, there is a relevant part of the [ReadMe.pdf](<Polynomial Regression and Random Forest/data/DataReadMe.pdf/>) of the data below.

*Column heading Parameter description Unit Interval Dataset name Type Comments Data collection*
![](https://imgur.com/iAl45aq.png)

Over the years, Sigrow has gathered information about the environment in the greenhouses, such as the temperature, air humidity, light intensity and amount of carbon dioxide (CO2) in the air. These four features are the most important factors for plants to grow, apart from water and nutrition (Hemming et al., 2019). As you can see in every dataset COair, Tair, HumDef and RHair are the most important features of the greenhouse climate dataset. CO2, Temparature and Humidity are together with light indeed the most important features for optimizing growth. The light measurements are divided in outdoor and indoor light and are in other datasets. 
### Polynomial fit
*Before going in depth it is important to realize that the results are found on a very scarce amount of data, so these results are not reliable, but may help getting results in the future.*

Results can be found on the web page https://readmees.github.io/polynomial_fit.html, with the [polynomial_fit.ipynb](<Polynomial Regression and Random Forest/polynomial_fit.ipynb/>) file you can generate even more results yourself, [here](https://i.imgur.com/U4IrLEq.mp4) is a short example how. More than 45 graphs are plotted to understand certain features. 
#### Carbon Dioxide concentration
In ‘The optimal CO2 concentrations for the growth of three perennial grass species’ (Zeng et al., 2018) Zeng et al. examine the growth of three perennial grasses in growth chambers with different CO2 ppm values. They found an ideal total biomass value of 915ppm (see figure 2). As shown in figure 2 Zeng et al. found this maximum by fitting 2nd degree polynomials throughout their measurements of 400, 600, 800, 1000 and 1200 ppm CO2.  With the autonomous greenhouse data a 2nd degree polynomial is heavily overfit, if however, the data is fitted by a 3rd degree polynomial. An overall maximum production value (of class A) is found with a CO2 concentration of +-947 ppm (see figure 1). All teams started with a relative low concentration of CO2 and increased it while the plants grew as shown in figure 3.
![](https://imgur.com/jSb8ixx.png)
#### Temperature
According to www.gardening.cornell.edu a cucumber crop should stay in an environment with a temperature above 70 F, so above +-22℃ at day (and above 60 F at night, +-16℃). In ‘CO2 enrichment of strawberry and cucumber plants grown in unheated greenhouses in Israel’ (Enoch, Rylski, & Spigelman) they keep the temperature in greenhouses under 28℃. The perfect temperature depends on the state of development of the plant and the strain of the plant. However, it would be fair to assume based on these sources that a good temperature is between 22-28℃, which is exactly what our current model found, see figure 4. Based on the production per week and the features in that week, we found an optimal temperature of +-24℃ (see figure 4).
![](https://imgur.com/CO6h90P.png)
