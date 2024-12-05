Here’s the **README** in a Git-friendly format using Markdown:

---

# **EV Adoption Analysis and Insights**

## **Project Overview**
This project analyzes Electric Vehicle (EV) adoption trends in Washington State using data from the Department of Licensing. It includes data preprocessing, exploratory analysis, predictive modeling, and interactive visualizations to support stakeholders in understanding EV trends.

---

## **Steps in the Project**

### 1. Dataset Selection
- **Source:** Washington State Department of Licensing - EV Population Data.  
- **Features:** EV types, makes, models, electric range, geographic data, and more.

### 2. Data Preprocessing
- **Techniques:**
  - Handled missing values:
    - `bfill`/`ffill` for categorical columns.
    - Median/mean/mode for numerical columns.
  - Removed duplicates and irrelevant columns.
  - Validated numeric fields (e.g., `Electric Range`).
  - Filtered dataset to include only Washington State (`State == 'WA'`).

### 3. Exploratory Data Analysis (EDA)
- Analyzed:
  - EV type distribution (BEVs vs. PHEVs).
  - Top manufacturers and models.
  - Regional distribution (by counties).
  - Trends in electric range and adoption over time.
- **Tools:** `pandas`, `matplotlib`, `seaborn`.

### 4. Visualizations for Base-Layer Insights
- **Visuals:**
  - Scatter plots (e.g., Model Year vs. Electric Range).
  - Heatmaps for correlations.
  - Word clouds for manufacturer prominence.
- **Theme:** EV-focused dark and green aesthetic.

### 5. Machine Learning Predictions
- Built predictive models (e.g., Linear Regression) to forecast EV adoption over the next 5 years.
- Input features: Geographic, demographic, and vehicle data.
- **Library Used:** `scikit-learn`.

### 6. Tableau Storytelling
- Designed an interactive dashboard:
  - EV adoption trends by region and year.
  - Socio-economic and geographic correlations.
  - Key findings presented for stakeholders.

---

## **Tools and Libraries**

| **Tool/Library**        | **Purpose**                              |
|--------------------------|------------------------------------------|
| `pandas`, `numpy`        | Data preprocessing and analysis         |
| `matplotlib`, `seaborn`  | Data visualization                      |
| `sklearn`                | Machine Learning                        |
| `Tableau`                | Interactive dashboards                  |
| `WordCloud`              | Text-based visualizations               |
| `Jupyter Notebook`       | Project execution and documentation     |

---

## **Project Outcomes**
- Identified BEVs as the dominant EV type, with Tesla leading the market.
- Mapped EV adoption hotspots (e.g., King County as the leader).
- Showcased a steady increase in EV ranges over the years.
- Predicted EV adoption trends for the next 5 years.
- Delivered a Tableau dashboard for stakeholder decision-making.

---

## **Contributors**
1. Aayush Anil Patil
2. Sadhvi Singh
3. Shaila Reddy Kankanala
4. Varshini Rao

---

## **Future Work**
- Incorporate additional datasets for socio-economic and infrastructure analysis.
- Enhance machine learning models with advanced techniques.
- Expand the Tableau dashboard with real-time EV data.
