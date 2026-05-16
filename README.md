# 🧬 DNA Classification and Analysis using Machine Learning


## 👥 Team Members & Course Details
*   **Team Members:** Akash S, Arya Suku, Ben Flis Ziya
*   **Course:** Predictive Analytics
*   **Instructor:** Dr. Aswin VS
*   **Institution:** Digital University Kerala

## 📌 Project Overview

This project is an interactive bioinformatics web application developed using Streamlit and Machine Learning to analyze and classify synthetic DNA samples.

The application predicts the biological category of a DNA sample based on several sequence-derived genomic features such as:

- Nucleotide composition
- GC/AT content
- Sequence length
- Mutation indicators
- k-mer frequency patterns

The project demonstrates how Machine Learning can be applied in genomics and bioinformatics for DNA pattern analysis and biological classification.

---

# 🧬 About DNA Sequences

DNA (Deoxyribonucleic Acid) consists of four nucleotide bases:

- **A** → Adenine
- **T** → Thymine
- **C** → Cytosine
- **G** → Guanine

A DNA sequence is formed by combinations of these nucleotides.

Example:

```text
ATCGGCTAAGCT
```

Different organisms often have different nucleotide composition patterns, sequence structures, and mutation characteristics. These biological patterns can be learned by Machine Learning models for classification tasks.

---

# 📊 Dataset Information

The dataset contains **3,000 synthetic DNA samples** with biologically inspired genomic features.

## Dataset Features

| Feature | Description |
|---|---|
| Sample_ID | Unique identifier for each DNA sample |
| Sequence | DNA sequence consisting of A, T, C, G |
| GC_Content | Percentage of Guanine and Cytosine bases |
| AT_Content | Percentage of Adenine and Thymine bases |
| Sequence_Length | Total sequence length |
| Num_A | Number of Adenine bases |
| Num_T | Number of Thymine bases |
| Num_C | Number of Cytosine bases |
| Num_G | Number of Guanine bases |
| kmer_3_freq | Average 3-mer frequency score |
| Mutation_Flag | Indicates mutation presence (0 or 1) |
| Class_Label | Biological class of sample |
| Disease_Risk | Risk category (Low / Medium / High) |

---

# 🧪 Understanding the Features

## 1. GC Content

GC Content represents the percentage of Guanine (G) and Cytosine (C) bases in the DNA sequence.

### Formula

```text
GC Content = ((G + C) / Total Bases) × 100
```

### Importance

- Higher GC content often indicates stronger DNA stability.
- Different organisms may have distinct GC composition patterns.
- Useful for genomic analysis and biological classification.

---

## 2. AT Content

AT Content represents the percentage of Adenine (A) and Thymine (T) bases.

### Formula

```text
AT Content = ((A + T) / Total Bases) × 100
```

### Importance

- Complements GC content.
- Helps identify genomic composition differences.

---

## 3. Sequence Length

Sequence Length represents the total number of nucleotides present in the DNA sequence.

### Example

```text
ATCGGCTA
```

Length = 8

### Importance

Different biological entities may exhibit characteristic sequence lengths.

---

## 4. Number of A, T, C, and G Bases

These features count the occurrences of each nucleotide in the DNA sequence.

### Example

```text
Sequence = ATCGGCTA
```

| Base | Count |
|---|---|
| A | 2 |
| T | 2 |
| C | 2 |
| G | 2 |

### Importance

Nucleotide frequency distribution is an important genomic signature used in classification tasks.

---

## 5. k-mer Frequency

A k-mer is a short subsequence extracted from DNA.

For k = 3:

```text
ATCGGC
```

3-mers:
- ATC
- TCG
- CGG
- GGC

The dataset contains a computed average 3-mer frequency score.

### Importance

k-mer analysis helps capture local DNA sequence patterns and genomic signatures.

Widely used in:
- Genome classification
- Species identification
- Mutation analysis

---

## 6. Mutation Flag

Binary feature indicating mutation presence.

| Value | Meaning |
|---|---|
| 0 | No Mutation |
| 1 | Mutation Present |

### Importance

Mutations can alter genomic behavior and influence biological classification.

---

# 🎯 Target Variable

The Machine Learning model predicts the biological class of the DNA sample.

## Possible Classes

- Human
- Bacteria
- Virus
- Plant

---

# 🤖 Machine Learning Model

The project uses a **Random Forest Classifier** trained on genomic statistical features extracted from DNA sequences.

## Input Features Used

- GC Content
- AT Content
- Sequence Length
- Number of A bases
- Number of T bases
- Number of C bases
- Number of G bases
- k-mer frequency
- Mutation flag

## Output

Predicted biological class:
- Human
- Bacteria
- Virus
- Plant

---

# 🧠 How Prediction Works

1. User enters genomic feature values in the Streamlit application.
2. Input features are converted into numerical format.
3. The trained Random Forest model processes the input features.
4. The model compares learned genomic patterns from training data.
5. The predicted DNA class is returned to the user.

The model learns relationships between nucleotide composition patterns and biological classes during training.

---

# 📈 Exploratory Data Analysis (EDA)

The application provides interactive visualizations including:

- Dataset preview
- Class distribution
- Disease risk distribution
- GC vs AT content analysis
- Feature exploration charts

These visualizations help understand genomic patterns within the dataset.

---

# 🚀 Streamlit Application Features

✅ DNA Classification  
✅ Interactive EDA Dashboard  
✅ Machine Learning Prediction  
✅ Bioinformatics Feature Analysis  
✅ User-Friendly Interface  

---

# 🛠️ Technologies Used

- Python
- Streamlit
- Pandas
- NumPy
- Scikit-learn
- Plotly
- Matplotlib
- Seaborn
- Joblib

---

# 📂 Project Structure

```text
DNA_Classification/
│
├── app.py
├── train_model.py
├── requirements.txt
├── model.pkl
├── label_encoder.pkl
│
├── Dataset/
│   └── synthetic_dna_dataset.csv
│
└── pages/
    ├── 1_EDA.py
    └── 2_Prediction.py
```

---

# ▶️ How to Run the Project

## 1. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 2. Train the Model

```bash
python train_model.py
```

This generates:
- `model.pkl`
- `label_encoder.pkl`

---

## 3. Run Streamlit App

```bash
streamlit run app.py
```

---

# 📚 Applications

This project can be useful for:

- Bioinformatics learning
- DNA sequence analysis
- Machine Learning education
- Genomic classification research
- Biological pattern recognition studies

---

# 📌 Note

This dataset is synthetic and created for educational and research purposes only. It does not represent real patient or genomic records.

# App URL
https://akash1231961-dna-classification-app-nrqzto.streamlit.app/


