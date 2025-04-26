# Logical Reasoning Evaluation Benchmark for Ukrainian LLMs

This project aimed at evaluating the logical reasoning capabilities of large language models (LLMs) in the **Ukrainian language**. It introduces a translated and custom-curated dataset of logical reasoning questions and provides a pipeline to evaluate multilingual LLMs on these tasks.

---

## 🧠 Project Highlights

- 🧩 **Custom dataset generation** following formal logical rules.
- 📊 **Evaluation pipeline** for testing multilingual LLMs on Ukrainian logical tasks.
- 🤖 **Model performance comparison** across popular LLMs.
- - ✅ **Attempts of translation and adaptation** of existing logical reasoning benchmarks (LogicBench, LogiQA) into Ukrainian.


---
## 📁 Repository Structure

```
├── dataset_generation/         # Scripts for creating and formatting custom logical tasks
├── evaluation/                 # Evaluation pipeline and metrics
├── LogicBench_translation/     # Ukrainian translation of the LogicBench dataset
├── LogiQA_translation/         # Ukrainian translation of the LogiQA dataset
├── README.md
└── requirements.txt
```
---

## 📂 Dataset Details

The project includes two main types of datasets:

1. **Translated Benchmarks (The quality of translations was not so well so it is not metioned in the paper)**:
   - `LogicBench_translation/`: Translated version of LogicBench with propositional and first-order logic tasks.
   - `LogiQA_translation/`: Translated version of LogiQA, a multiple-choice logical reasoning dataset.

2. **Generated Dataset**:
   - Found in `dataset_generation/`, containing examples curated specifically for testing logical competence in Ukrainian.

All datasets are formatted for easy evaluation with multilingual LLMs.

---

## 🚀 Evaluation Pipeline

The evaluation code supports testing a variety of LLMs (local or API-based) on all datasets. It computes key metrics such as:

- **Accuracy**
- **F1 Score**
It includes two configurations:
- run_eval.sh - for running the evaluation on single device
- run_eval_vllm.sh - for running the evaluation on multiple devices using vllm
The configurations for prompt forming and evaluation metrics are defined separately for every split in files:
`subset_constructive_dilemma.yaml`, `subset_disjunctive_syllogism.yaml`, `subset_material_implication.yaml`, `subset_modus_ponens.yaml`, `subset_modus_tollens.yaml`.