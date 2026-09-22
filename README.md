# QML: quantum machine learning paper implementations

This repository collects working implementations of published quantum machine learning papers, with a focus on cybersecurity. Each paper gets its own folder with a notebook that rebuilds the experiment from the paper, step by step, using open tools such as Qiskit and scikit learn.

The notebooks are written for teaching. Every step has a plain language explanation, so students can follow the method without a physics background. Each notebook also compares its own results with the numbers the paper reports, and states clearly which claims were reproduced and which were not.

## Implemented papers

### 2023, Said: Quantum SVM for DDoS detection on a smart micro grid

* Paper: Dhaou Said, "Quantum Computing and Machine Learning for Cybersecurity: Distributed Denial of Service (DDoS) Attack Detection on Smart Micro Grid", Energies 16(8), 3572, 2023. DOI 10.3390/en16083572
* Method: quantum kernel support vector machine (QSVM) with a ZZ feature map, compared against linear and RBF classical SVMs
* Data: CICDDoS2019, benign traffic and SSDP reflection attacks, downloaded automatically by the notebook
* Folder: [papers/2023_Said_QSVM_DDoS](papers/2023_Said_QSVM_DDoS)
* Open in Colab: [QSVM_DDoS_Said2023.ipynb](https://colab.research.google.com/github/owlmt/QML/blob/main/papers/2023_Said_QSVM_DDoS/QSVM_DDoS_Said2023.ipynb)

More papers will be added over time.

## How to run a notebook

The simplest way is Google Colab. Click the Colab link of a paper, then choose Runtime, then Run all. The normal CPU runtime is enough, and no IBM Quantum account is needed, because the circuits run on a simulator.

To run locally, install Python 3.10 or newer and then:

    pip install qiskit qiskit_machine_learning scikit_learn pandas matplotlib pylatexenc huggingface_hub jupyter
    jupyter notebook

## Repository layout

    papers/
        <year>_<first author>_<short topic>/
            <notebook>.ipynb
            README.md   (optional notes for that paper)

## Rules for adding a new paper

* One folder per paper, named year, first author, then a short topic, joined with underscores.
* The notebook downloads or generates its own data, so it runs from a clean Colab session.
* Preprocessing is fitted on training data only, so there is no leakage into the test set.
* A classical baseline is trained on exactly the same inputs as the quantum model.
* The notebook ends with an honest comparison: what matched the paper, what did not, and possible reasons.
* The full reference to the paper, with its DOI or arXiv number, is given at the top of the notebook and in this README.

## Requirements used so far

Qiskit 2.x and qiskit machine learning 0.9 or newer. Older Qiskit versions use different class names for feature maps and may not run the notebooks unchanged.