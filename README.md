# datanews
Project Code Review

In this dataset, Firstly send an HTTP request to the URL of the webpage  to access. The server responds to the request by returning the HTML content of the webpage. For this task, we will use a third-party HTTP library for python-requests. Once we have accessed the HTML content, we are left with the task of parsing the data.
I use find() method to get what I need, description of news. After this I used for loop to get specific news' link, content, and use strip() method to put text in words by space
Finally, I saved it csv file with their heads

Question Answers

1.

2. Actually, CSV is one of the most common file formats for storing textual data. These files can be opened using a wide variety of programs including Notepad. The reason behind using this format over others is its ability to store complex data in a simple and readable way. Moreover, CSV files offer more security as compared to file formats like JSON. In python, it is easy to read these types of files using a special library called Pandas.

3. Data quality is a measure of the condition of data based on factors such as accuracy, completeness, consistency, reliability and whether it's up to date. ACtually we should focus on data quality. Beacuse it helps us to evaulate these factors easily. For each data collection project, it is important to select the right tools and the right methods for collecting data. Pretesting data collection tools before administering them to targeted subjects is  also important.
