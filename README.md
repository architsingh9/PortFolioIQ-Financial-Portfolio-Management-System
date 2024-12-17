# **PortFolioIQ–Financial-Portfolio-Management-System**

## **Project Overview**
PortFolioIQ is a Financial Portfolio Management System (FPMS) designed to simplify portfolio management by centralizing static and transactional financial data. Using **Talend** for ETL and **PostgreSQL** for data warehousing, the system enables investors to optimize portfolios, analyze risks, and derive actionable insights.

---

## **Why We Built It**
Managing portfolios is challenging due to:  

- **Scattered Data**: Static (historical) and real-time transactional data are fragmented.  
- **Complex Risk Management**: Balancing risk and returns requires advanced analytics.  
- **Lack of Insights**: Investors need tools for trend analysis and performance optimization.  

PortFolioIQ bridges these gaps by delivering a scalable, data-driven solution that integrates and analyzes financial data efficiently.

---

## **Key Features**
- **Automated ETL Pipelines**: Built using **Talend** to extract, clean, and load data seamlessly into the warehouse.  
- **Centralized Database**: A normalized relational model in **PostgreSQL** storing static and transactional data.  
- **Advanced Analytics**: Multi-dimensional OLAP operations for trend analysis and reporting.  
- **Historical Management**: **SCD (Slowly Changing Dimensions)** implementation for accurate historical tracking.  
- **Portfolio Optimization**: Track investments, returns, and risk metrics for better decision-making.

---

## **How We Built It**

### **1. Data Integration with Talend**
We developed ETL pipelines in Talend for:  
- **Extraction**: Fetching static data (e.g., company financials, stock prices) and transactional data (e.g., buy/sell orders, dividends).  
- **Transformation**: Cleaning and transforming the data to ensure consistency and quality.  
- **Loading**: Inserting the processed data into PostgreSQL tables.  

**Talend Jobs Created:**  
- `Company Transfer`  
- `Price Transfer`  
- `Client Profile Transfer`  
- `Portfolio Creation Transfer`  
- `Portfolio Holding Transfer`  
- `Return Analytics Transfer`  
- `Technical Strategy Transfer`  
- `Time Dimension Transfer`  

---

### **2. Database Design in PostgreSQL**
We created a **normalized relational schema** for efficiency and scalability.  

**Key tables include:**  
- `Company`: Static company data (ISIN, Ticker, Sector, Market Cap).  
- `Client_Profile`: Investor information (Name, Expected Returns, Risk Appetite).  
- `Portfolio_Holding`: Records of individual investments.  
- `Price`: Historical stock prices and dates.  
- `Return_Analytics`: Portfolio performance metrics.  
- `Client_Transaction`: Transaction history.  

**Technologies Used:**  
- Primary keys, foreign keys, and `uuid-ossp` for unique ID generation.

---

### **3. OLAP Operations for Analytics**
We implemented OLAP queries to derive actionable insights:  
- **Roll-Up**: Summarize transaction data by month or year.  
- **Drill-Down**: Analyze trends at finer granularities (e.g., daily performance).  
- **Slice/Dice**: Filter data for specific clients, portfolios, or time ranges.  
- **Pivot**: Compare metrics like transaction totals across clients and years.  
- **Ranking**: Identify top-performing clients or portfolios based on percentage gains/losses.  

---

### **4. SCD (Slowly Changing Dimensions)**
To ensure historical tracking and data integrity, we implemented **SCD Type 2** for key dimension tables, enabling:  
- Accurate analysis of changes over time.  
- Retention of historical attributes for reliable reporting.

---

## **Technologies Used**
- **ETL Tool**: Talend  
- **Database**: PostgreSQL  
- **Data Modeling**: ERD, Normalized Relational Schema  
- **Analytics**: OLAP Operations  

---

## **Future Enhancements**
- Integration with real-time market APIs for dynamic updates.  
- Visualization dashboards using **Power BI** or **Tableau**.  
- Machine learning for predictive analytics and portfolio recommendations.
