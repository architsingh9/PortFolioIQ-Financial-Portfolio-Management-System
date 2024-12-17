# **PortFolioIQ–Financial-Portfolio-Management-System**

## **Project Overview**
PortFolioIQ is a **Financial Portfolio Management System (FPMS)** designed to simplify portfolio management by centralizing static and transactional financial data. Initially implemented **on-premises** using **Talend** for ETL and **PostgreSQL** for data warehousing, the project was later migrated to **Microsoft Azure** for enhanced scalability, automation, and advanced analytics.

---

## **Why We Built It**
Managing financial portfolios is challenging due to:  

- **Scattered Data**: Static (historical) and real-time transactional data are fragmented.  
- **Complex Risk Management**: Balancing risk and returns requires advanced analytics.  
- **Lack of Insights**: Investors need tools for trend analysis, performance optimization, and decision-making.  

PortFolioIQ bridges these gaps by delivering a **scalable, data-driven solution** that integrates, transforms, and analyzes financial data efficiently.

---

## **Key Features**
- **On-Premises Implementation**: Built using **Talend** for ETL and **PostgreSQL** for data warehousing.  
- **Cloud Migration on Azure**:  
  - **Azure Data Factory** for automated pipelines.  
  - **Azure Databricks** for data transformation.  
  - **Azure Synapse Analytics** for OLAP analysis.  
  - **Power BI** for visualization and insights.  
- **Advanced Analytics**: OLAP operations for trend analysis, ranking, and performance reporting.  
- **Historical Tracking**: Implemented **SCD Type 2** for accurate historical data retention.  

---

## **How We Built It**

### **1. On-Premises Implementation**
- **ETL Pipelines**:  
   - Developed using **Talend** to automate extraction, transformation, and loading of financial data.  
   - **Extraction**: Static data (company financials, stock prices) and transactional data (buy/sell orders).  
   - **Transformation**: Cleaned and normalized data for consistency.  
   - **Loading**: Processed data stored in **PostgreSQL**.  

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

### **2. Cloud Migration to Microsoft Azure**
To scale the project and automate workflows, we migrated to the Azure cloud using the following services:

- **Azure Blob Storage**:  
   - Stored raw and transformed data, ensuring centralized data access.  

- **Azure Data Factory (ADF)**:  
   - Automated data ingestion from raw sources to storage and triggered transformations in **Databricks**.  

- **Azure Databricks**:  
   - Cleaned, normalized, and prepared OLAP-ready data using **PySpark**.  

- **Azure Synapse Analytics**:  
   - Performed advanced SQL-based analysis and OLAP operations (roll-up, drill-down, ranking).  
   - Created a centralized **Lake Database** for querying financial data.  

- **Power BI**:  
   - Connected to Synapse to build interactive dashboards for visualizing portfolio performance, returns, and client transactions.  

- **Azure DevOps**:  
   - Implemented CI/CD pipelines for automated deployment, ensuring reliable and seamless updates.  

---

### **3. Database Design**
We designed a **normalized relational schema** to ensure scalability and efficiency.

**Key Tables:**  
- `Company`: Static company data (ISIN, Ticker, Sector, Market Cap).  
- `Client_Profile`: Investor information (Name, Expected Returns, Risk Appetite).  
- `Portfolio_Holding`: Individual investment records.  
- `Price`: Historical stock prices and dates.  
- `Return_Analytics`: Portfolio performance metrics.  
- `Client_Transaction`: Transaction history.  

---

### **4. OLAP Analytics**
We implemented OLAP operations to derive actionable insights:  
- **Roll-Up**: Summarize transaction data at higher levels.  
- **Drill-Down**: Analyze data at finer granularities (e.g., daily performance).  
- **Slice/Dice**: Filter data for specific portfolios or clients.  
- **Pivot**: Compare key metrics (returns, risk) across dimensions.  
- **Ranking**: Identify top-performing portfolios and clients.  

---

## **Technologies Used**

### On-Premises:  
- **ETL Tool**: Talend  
- **Database**: PostgreSQL  

### Cloud (Azure):  
- **Storage**: Azure Blob Storage  
- **Pipeline Automation**: Azure Data Factory  
- **Data Processing**: Azure Databricks  
- **Data Warehousing**: Azure Synapse Analytics  
- **Visualization**: Power BI  
- **CI/CD**: Azure DevOps  

---

## **Future Enhancements**
- Integration with **real-time market APIs** for live data updates.  
- Implementation of machine learning for predictive portfolio recommendations.  
- Enhanced reporting and visualizations using **Power BI**.

---

## **Project Flow Summary**

```mermaid
graph TD
    A[Raw Data in Azure Blob Storage] --> B[Azure Data Factory: Data Ingestion]
    B --> C[Azure Databricks: Data Transformation]
    C --> D[Azure Synapse Analytics: Data Analysis]
    D --> E[Power BI: Visualization]
    C --> F[CI/CD Pipelines via Azure DevOps]
