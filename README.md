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
This repository contains of two directories. 'erudite2020/Final Report for University of Amsterdam/' contains the Final Report for the Univisity of Amsterdam. 'erudite2020/Polynomial Regression and Random Forest/' contains the models made for Sigrow and the data. THe data is retrieved from the Automonous greenhouse challenge, a challenge where 5 artificial intelligence tried to grow the best and most environmental friendly plants. The source of the data can be found [here][1]




[1]:(https://data.4tu.nl/repository/uuid:e4987a7b-04dd-4c89-9b18-883aad30ba9a#DATA)
