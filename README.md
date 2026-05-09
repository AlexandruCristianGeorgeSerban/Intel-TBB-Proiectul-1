# Procesarea Paralelă a Seturilor de Imagini folosind Intel TBB

## 📋 Descriere Proiect
Acest proiect vizează analiza strategiilor de paralelizare în procesarea seturilor de imagini, utilizând biblioteca **Intel Threading Building Blocks (TBB)**. Accentul este pus pe compararea performanței între paralelizarea la nivel de imagine (intra-imagine) și paralelizarea la nivel de set de date (inter-imagini).

## 🛠️ Operație Propusă
* **Algoritm:** Thresholding adaptiv / Binarizarea imaginilor.

## 🎯 Obiective și Cerințe
* Implementarea algoritmului de binarizare adaptivă.
* Compararea strategiilor:
    1.  **Paralelizare în interiorul unei singure imagini** (intra-imagine).
    2.  **Paralelizare între imagini multiple** (inter-imagini).
* Măsurarea timpilor de execuție și interpretarea rezultatelor pentru fiecare strategie.

## 📊 Metrici de Performanță
Proiectul va evalua următoarele metrici:
* Timp de execuție.
* Speedup (Accelerare).
* Throughput (Imagini / secundă).
* Eficiență la un număr diferit de thread-uri.

## 📝 Structura Raportului Scris
Conform cerințelor, raportul va include:
1.  **Descrierea algoritmului:** Scurtă prezentare a binarizării adaptive și rolul ei în computer vision.
2.  **Strategii de paralelizare:** Detalii tehnice despre implementările cu TBB.
3.  **Analiză Comparativă:** Implementarea secvențială vs. implementările paralele.
4.  **Configurație:** Detalii hardware și software (CPU, RAM, OS, Compilator).
5.  **Interpretarea rezultatelor:** Analiză personală a datelor și a scalabilității.

## 📁 Dataset
* Set de imagini de pe **Kaggle**.

## 📦 Livrabile Finale
* **Repository Git:** Branch-uri separate pentru fiecare implementare, cu commit-uri granulare și mesaje descriptive.
* **Raport scris.**
