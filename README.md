
# 🚀 Iris Classifier API with FastAPI

This project is a lightweight **ML deployment app** using **FastAPI** that serves predictions for the classic [Iris dataset](https://scikit-learn.org/stable/auto_examples/datasets/plot_iris_dataset.html). It provides a clean API endpoint to predict the species of Iris flowers based on input features.

---

### 🔧 Tech Stack

- **FastAPI** – For building the REST API
- **scikit-learn** – Model training
- **Uvicorn** – ASGI server
- **Streamlit** – Optional frontend for testing
- **Pydantic** – Input data validation

---

### 📦 Project Structure

```
.
├── model/
│   └── iris_model.pkl        # Trained ML model
├── app/
│   ├── main.py               # FastAPI app
│   └── schema.py             # Pydantic models
├── streamlit_app.py          # Streamlit-based UI (optional)
├── requirements.txt
└── README.md
```

---

### 📌 How to Use

#### 1. 🔁 Clone the Repo
```bash
git clone https://github.com/trivediadi/iris-classifier-fastapi.git
cd iris-classifier-fastapi
```

#### 2. 🐍 Create Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # or .\venv\Scripts\activate on Windows
```

#### 3. 📥 Install Dependencies
```bash
pip install -r requirements.txt
```

#### 4. ▶️ Run FastAPI App
```bash
uvicorn app.main:app --reload
```

Visit: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) to test the API using Swagger UI.

---

### 🧪 API Usage

**Endpoint:** `POST /predict`

**Request Body (JSON):**
```json
{
  "sepal_length": 5.1,
  "sepal_width": 3.5,
  "petal_length": 1.4,
  "petal_width": 0.2
}
```

**Response:**
```json
"Iris-setosa"
```

---

### 🌐 Optional: Run Streamlit Frontend

```bash
streamlit run streamlit_app.py
```

---

### 📘 Example Use Case

This API can be integrated into web apps, used as a backend service for mobile apps, or even serve as a microservice in a production pipeline — showcasing **how to deploy ML models using FastAPI**.

---

### ✨ Author

- **Aditya Trivedi**
- GitHub: [@yourusername](https://github.com/trivediadi)
- LinkedIn: [linkedin.com/in/your-profile](https://www.linkedin.com/in/aditya-raj-trivedi-884545330/)
