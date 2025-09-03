# 📊 Sales Prediction using Linear Regression

This project demonstrates how to use **Linear Regression** to predict product sales based on advertising expenditure across **TV, Radio, and Newspaper** channels.  

The dataset used is the **Advertising dataset**, which contains sales data alongside ad spending in different media.

---

## 🚀 Project Workflow

1. **Data Loading & Exploration**
   - Load dataset (`Advertising.csv`) using `pandas`.
   - Explore data with `.head()`, `.info()`, `.describe()`, and check for missing/duplicate values.

2. **Data Cleaning**
   - Remove unnecessary columns (`Unnamed: 0`).
   - Ensure no null or duplicate values remain.

3. **Exploratory Data Analysis (EDA)**
   - Pairplots to visualize relationships between advertising channels and sales.
   - Histograms for distribution of spending.
   - Heatmap for correlation analysis.

4. **Model Training**
   - Features: `TV`, `Radio`, `Newspaper`
   - Target: `Sales`
   - Split data into training (70%) and testing (30%).
   - Train a **Linear Regression** model using `scikit-learn`.

5. **Model Evaluation**
   - Evaluate performance using:
     - **R² Score**
     - **Mean Squared Error (MSE)**
     - **Cross-Validation (5-fold)**
   - Compare **predicted vs actual sales** with plots:
     - Trend plot (Actual vs Predicted)
     - Scatter plot with perfect prediction line

---

## 📈 Results & Observations

- **TV advertising** shows the strongest positive correlation with Sales.
- **Radio** has some impact but less predictable.
- **Newspaper** spending has the weakest relationship with Sales.
- The model performs well in capturing the general sales trend.

---

## 🛠️ Technologies Used

- Python
- Libraries:
  - `numpy`, `pandas`
  - `matplotlib`, `seaborn`
  - `scikit-learn`

---

## 📊 Sample Output

- **R² Score**: ~0.90 (example, depending on random state)
- **MSE**: Low (indicating good fit)
- **Cross-Validation Mean R²**: Consistently high across folds

---

## 📌 How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/your-repo-name.git
   cd your-repo-name
