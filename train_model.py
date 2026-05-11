import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score
import joblib

# Load dataset
df = pd.read_csv(r"C:\Users\HP\Downloads\synthetic_dna_dataset.csv")

# Features
X = df[
    [
        "GC_Content",
        "AT_Content",
        "Sequence_Length",
        "Num_A",
        "Num_T",
        "Num_C",
        "Num_G",
        "kmer_3_freq",
        "Mutation_Flag"
    ]
]

# Target
y = df["Class_Label"]

# Encode labels
le = LabelEncoder()
y_encoded = le.fit_transform(y)

# Train test split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y_encoded,
    test_size=0.2,
    random_state=42
)

# Model
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(X_train, y_train)

# Accuracy
pred = model.predict(X_test)

acc = accuracy_score(y_test, pred)

print("Accuracy:", acc)

# Save model
joblib.dump(model, "model.pkl")
joblib.dump(le, "label_encoder.pkl")

print("Model saved successfully!")