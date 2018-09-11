COMMENT ON HOW TO NAVIGATE THE PROJECT

The project has two parts:
    1. the ordering system
    2. the ice cream trends part

**************************************************************************************************************************
**                                                                                                                      **
**                                    THE ORDERING SYSTEM                                                               **
**                                                                                                                      **
**************************************************************************************************************************
    Has two python files;
        1. __init__ (python package file)
        2. ordering_system.py --> this is the file that contains the code

    It is pure python, it only requires one module; random

    To run;
        1. open the terminal on this directory
        2. navigate to the directory where this project is; (...source.../ice_cream_store/ordering_system)
        3. type: python ordering_system.py

        4. the program is running, enter the details as required.

**************************************************************************************************************************
**                                                                                                                      **
**                                    THE ICE CREAM TRENDS                                                              **
**                                                                                                                      **
**************************************************************************************************************************
~~> it use python flask module, check the requirements.txt for the other requirements
~~> there are four different graphs generated.

                                        REPORT-DATA GENERATION
The data used in the reports is generated from different python scripts. The generation logic is discussed;
    1. WeeklySales / weekly_sales_generator
    - To show the changes of sales over a period of 2010 - 2012, i generated weekly sales for 52 weeks each year for the three years
    - Assumptions made:
        * A store sells a minimum of 10 ice creams and a maximum of 50 ice creams in a day
    - The data is saved in WeeklySales.xlsx file.
    - I used the summation of each year to generate the graph.

    2. StoreSales / store_sales_generator
    - To show the trends in different stores in a given year, i generated weekly sales for each store for an year
    - Assumptions made:
        * A store sells a minimum of 10 ice creams and a maximum of 50 ice creams in a day
        * I used 5 stores to compare the sales.
        * I chose year 2010
    - The data is saved in StoreSales.xlsx file
    - I used the summation of each store sale to generate the report

    3. RegionSales / region_sales_generator
    - To compare sales in five different regions, the following assumptions were made:
        * A region has 5 stores.
        * A store sells a minimum of 10 ice creams and a maximum of 50 ice creams in a day,
            hence a region sale is the collated sales of the 5 stores.
        * Time period for comparision of the sales is 1 year
        * I chose the year 2010

    4. Temperature / temperature_sales_generator
    - To compare sales in a store against effect of temperature.
    - Assumptions made:
        * The weekly temperature is an average of the daily temperature which ranges
            between 0 degrees celsius and 35 degrees celsius
        * I divided the temperature into four bands,
                   0 - 15, 16 -23, 24 - 29, 30 - 35.
        * In each band we will sample 2 sales data
        * The ice cream sales increase as temperature increases, therefor the bands have different sales
        * This was averaged in an year. 

Other general assumptions;
    * I used random --> randint() to generate random values within a given band.


                                        REPORT GENERATION (GRAPHS)
Using the data obtained from the scripts above, we then use matplotlib to generate graphs, which are easier to read
and analyze.

There four graphs, each of which has its data from report-data generator. These Graphs are;

    1. Ice Cream Sales for year 2010 - 2012
    - Shows the number of ice cream sold for the 3 years
    - Each year is a bar on the graph

    2. Ice Cream Trends for different stores in a region, in a given year(2010)
    - Shows the number of ice cream sold by each of the 5 stores in one year
    - Each store is a bar on the graph

    3. Ice cream Trends for different regions in a given year(2010)
    - Shows the number of ice cream sold in each of the 5 regions in one year
    - Each region is a bar on the graph

    4. Ice Cream Sales against Temperature
    - Shows the number of ice cream sold in a store against the different temperature bands
    - Each temperature band is a bar on the graph
    
                                    RUNNING THE APPLICATION
    1.  Open the project in an IDE, if you have the run button simply click it.
         or
          1.1 Navigate to the file with the flask application (below_zero_company/ice_cream_store/ice_cream_trends)
          1.2 Open the app.py file
          1.3 Right click and run
      
    2. Navigate to the file with the flask application from the terminal 
        (... source ... /below_zero_company/ice_cream_store/ice_cream_trends)            
        
        - Run the application by typing: python app.py
        - This activaes a local server and you can access the pages through the following urls:
        
        - address will be 127.0.0.1:5000/ - the port number may vary, though not always
          
         
The graph urls are:
    1. Ice Cream Sales for year 2010 - 2012
        http://127.0.0.1:5000/ice-cream-sales-2010-2012
        
    2. Ice Cream Trends for different stores in a region, in a given year(2010)
        http://127.0.0.1:5000/ice_cream_trends_in_different_stores
        
    3. Ice cream Trends for different regions in a given year(2010)
        http://127.0.0.1:5000/ice_cream_trends_in_regions
        
    4. Ice Cream Sales against Temperature
        http://127.0.0.1:5000/temp_sales_comparision
        