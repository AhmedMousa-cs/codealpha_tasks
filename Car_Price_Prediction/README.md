# 🚗 Car Price Prediction using Linear & Lasso Regression

This project predicts the **selling price of cars** based on different features such as present price, kilometers driven, fuel type, transmission type, and more.  
It uses **Linear Regression** and **Lasso Regression** models to analyze and compare prediction performance.

---

## 📂 Dataset

- **Source**: `car data.csv`
- **Key Features:**
  - `Car_Name` → Name of the car
  - `Year` → Year of manufacture
  - `Present_Price` → Current ex-showroom price
  - `Kms_Driven` → Distance driven in kilometers
  - `Fuel_Type` → Petrol, Diesel, or CNG
  - `Selling_type` → Dealer or Individual
  - `Transmission` → Manual or Automatic
  - `Owner` → Number of previous owners
  - `Selling_Price` → Target variable (price at which car is sold)

---

## 🔎 Project Workflow

### 1. Data Collection & Exploration
- Load dataset with **pandas**
- Inspect rows, columns, datatypes, and missing values
- Explore categorical distributions:
  - Fuel Type
  - Selling Type
  - Transmission

### 2. Data Preprocessing
- Encode categorical variables:
  - Fuel Type → `Petrol=0`, `Diesel=1`, `CNG=2`
  - Seller Type → `Dealer=0`, `Individual=1`
  - Transmission → `Manual=0`, `Automatic=1`
- Drop unnecessary column (`Car_Name`)

### 3. Data Visualization
- **Pairplots** for feature relationships
- **Histograms** for feature distributions
- **Heatmaps** for correlations
- **Scatter plots** for actual vs predicted prices

### 4. Model Training & Evaluation
- **Linear Regression**
  - Train/test split: 70/30
  - Evaluate with R² Score & Mean Squared Error (MSE)
  - Visualize predicted vs actual selling prices
- **Lasso Regression**
  - Fit model and compare performance with Linear Regression
  - Visualize predicted vs actual prices & trend plots

---

## 📊 Results & Observations

- **Linear Regression** gives a good baseline for predicting selling prices.
- **Lasso Regression** helps with feature selection by penalizing irrelevant features.
- Performance comparison (values may vary depending on dataset split):
  - **Linear Regression R²**: ~0.84 – 0.90
  - **Lasso Regression R²**: slightly lower but reduces overfitting risk
- Car price is **strongly correlated with Present Price** and somewhat affected by `Year` and `Kms_Driven`.

---

## 🛠️ Technologies Used

- Python
- Libraries:
  - `numpy`, `pandas`
  - `matplotlib`, `seaborn`
  - `scikit-learn`

---


