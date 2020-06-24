# Tweedejaarsproject: project course University of Amsterdam in cooperation with Sigrow
## About us
Erudite is a group of 5 motivated Artificial Intelligence second year bachelor students. We are Riemer Dijkstra, Otto Márton, Dionne Gantzert, Johannes Roelink and Mees Meester. For the 'Tweedejaarsproject' our group has been assigned to a company, Sigrow. They came up with a challenge for us to solve in four weeks.

## Introduction
*This introduction can be found in erudite2020/Final Report for University of Amsterdam/Final Report.pdf*

One of the goals of horticultural production in greenhouses is to increase the sustainable income of the grower. The investment costs for conventional plant production as well as labour and energy costs are much lower comparing to the investment costs for greenhouses. This can only be balanced out with a better utilization of the yielding potential of plants, higher labour productivity and higher energy efficiency (Tantau, H. J. (1991))*#TODO: add italics in all the sources*. Another goal of horticultural production in greenhouses has to do with the global population rapidly increasing, together with the demand for healthy fresh food. The horticulture industry can play an important role in providing food, but encounters difficulties finding skilled staff to manage crop production (Hemming et al. (2019)).

In the competitive horticulture industry, small improvements can make or break the competitive advantage of the yield. In order to stay ‘ahead of the curve’, calculated decisions need to be made about the greenhouse climates (Sigrow, n.d.).

Sigrow is a company in the Netherlands which provides state of the art sensor technology tailored to a greenhouse. These sensors make it possible for Sigrow’s clients to stay ahead of the curve and make those calculated decisions. Since the horticulture industry is very competitive, little is known about the possibilities to use artificial intelligence to optimize plant growth in greenhouses. Sigrow has little knowledge about artificial intelligence as well and that is why a collaboration of the two fields was needed.

Over the years, Sigrow has gathered information about the environment in the greenhouses, such as the temperature, air humidity, light intensity and amount of carbon dioxide (CO2) in the air. These four features are the most important factors for plants to grow, apart from water and nutrition (Hemming et al. (2019)). The task Sigrow had for us was to optimize the plant growth by optimizing the greenhouse climate.

When Sigrow provided the data there were two significant problems:
The data lacked information about the plants.
The amount of data was scarce. The task Sigrow had for us was to optimize the plant growth by optimizing the greenhouse climate.

Sigrow has only collected data about the environment of the plants, but not the plants themselves. The data did not contain any information about which kind of plant it was, nor the height, stem diameter or weight. In addition to this, the amount of data was so scarce that it was impossible to split the dataset into a training and test set.

Because of these two problems, a new challenge was set up. Instead of optimizing the plant growth by optimizing the greenhouse climate, Sigrow wanted a recommendation. This recommendation had to meet a number of requirements. First, it had to contain a comprehensive analysis about the measurements Sigrow is currently taking. This includes advice about which measurements need to be done and why. Second, it had to contain a simple overview of possible feature optimization techniques which Sigrow could use, imagining the two problems were not there. At last, the recommendation had to contain an understandable explanation about several machine learning techniques.

Besides the recommendation, Sigrow also asked for a implementation design for these feature optimization techniques. Since the data is not usable, the results would be unreliable, but an implementation, imagining the data is complete, would be.

By providing Sigrow a recommendation about how to optimize the plant growth using machine learning and implementing these techniques for them, we hope Sigrow can optimize the plant growth in the future and stay ahead of the curve.

## The /erudite2020 Github repository
This repository contains of two repositories. The ['/Final Report/'](<Final Report/>) repository contains the report we wrote for the Univisity of Amsterdam. In the ['/Polynomial Regression and Random Forest/'](<Polynomial Regression and Random Forest/>) repository the models made for Sigrow and the data can be found. The data is retrieved from the Automonous greenhouse challenge, a challenge where five teams tried to grow the best and most environmentally friendly plants. The source of the data can be found [here](https://data.4tu.nl/repository/uuid:e4987a7b-04dd-4c89-9b18-883aad30ba9a#DATA). The data is divided in six directories, one for every team and one for a reference (plants grown without the help of AI). Each of those directories contains in 5 datasets. CropManagement.csv, Greenhouse_climate.csv, Irrigation.csv, Production.csv, ResourceCalculations.csv and vip.csv. 

### Cleaned data
Because of missing data points and inconsistent units of measurement, the data had to be cleaned in order to be useful. Missing data points were replaced with the previously known value using ffill, a built in function of the Pandas python library. If the first datapoint was missing, we replaced the NaN value with the next known value using Bfill, also from the Pandas library. For ease of use we combined all the data in one large python dictionary, with the keys being the different teams that competed for the challenge and the values being the environmental and plant data.

### Random forest
[randomforest.ipynb](<Polynomial Regression and Random Forest/randomforest.ipynb/>) is used to find the feature importance in the dataset Greenhouse_climate.csv for different teams. The feature importances are found by using a random forest classifier. The results shown in the figures below are the feature importances of the features in the greenhouse climate datasets.

![](https://imgur.com/mMthsX6.png) ![](https://imgur.com/xPIJtlk.png) 
![](https://imgur.com/ABIU4m2.png) ![](https://imgur.com/mbGukqX.png)
![](https://imgur.com/5gauDK6.png) ![](https://imgur.com/jIrGrvA.png) 

For more clarification of the what the features mean, there is a relevant part of the [ReadMe.pdf](<Polynomial Regression and Random Forest/data/DataReadMe.pdf/>) of the data below.

*Column heading Parameter description Unit Interval Dataset name Type Comments Data collection*
![](https://imgur.com/iAl45aq.png)

As you can see in every dataset COair, Tair, HumDef and RHair are the most important features of the greenhouse climate dataset. CO$^2$, Temparature and Humidity are together with light indeed the most important features for optimizing growth. The light measurements are devided in outdoor and indoor light and are in other datasets.
### Polynomial fit
*Before going in depth it is important to realize that the results are found on a very scarce amount of data, so these results are not reliable, but may help getting results in the future.*
#### Carbon Dioxide concentration
In ‘The optimal CO2 concentrations for the growth of three perennial grass species’ (Zeng et al., 2018) Zeng et al. examine the growth of three perennial grasses in growth chambers with different CO2 ppm values. They found an ideal total biomass value of 915ppm (see figure 2). As shown in figure 2 Zeng et al. found this maximum by fitting 2nd degree polynomials (formula: y=ax2+bx+c, a-c are parameters) throughout their measurements of 400, 600, 800, 1000 and 1200 ppm CO2.  With the autonomous greenhouse data a 2nd degree polynomial is heavily overfit, if however, the data is fitted by a 3rd degree polynomial (formula: y=ax3+bx2+cx+d, a-d are parameters). An overall maximum production value (of class A) is found with a CO2 concentration of +-947 ppm (see figure 1). All teams started with a relative low concentration of CO2 and increased it while the plants grew as shown in figure 3.
![](https://imgur.com/jSb8ixx.png)
#### Temperature
According to www.gardening.cornell.edu a cucumber crop should stay in an environment with a temperature above 70 F, so above +-22℃ at day (and above 60 F at night, +-16℃). In ‘CO2 enrichment of strawberry and cucumber plants grown in unheated greenhouses in Israel’ (Enoch, Rylski, & Spigelman) they keep the temperature in greenhouses under 28℃. The perfect temperature depends on the state of development of the plant and the strain of the plant. However, it would be fair to assume based on these sources that a good temperature is between 22-28℃, which is exactly what our current model found, see figure 4. Based on the production per week and the features in that week, we found an optimal temperature of +-24℃ (see figure 4).
![](https://imgur.com/CO6h90P.png)

