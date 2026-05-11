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

Dataset-ul utilizat în cadrul proiectului:

* License Plate Dataset (Kaggle):
  https://www.kaggle.com/datasets/ronakgohil/license-plate-dataset

Imaginile sunt utilizate pentru aplicarea algoritmului de adaptive thresholding / image binarization și pentru analiza performanței strategiilor de paralelizare.

---

## ⚙️ Requirements / Dependencies

Pentru rularea proiectului sunt necesare:

* Visual Studio Community 2022 sau Visual Studio Community 2026
* C++17
* OpenCV
* Intel oneTBB (Threading Building Blocks)
* vcpkg

---

## 🔧 Instalare vcpkg

```powershell
git clone https://github.com/microsoft/vcpkg.git
cd vcpkg
.\bootstrap-vcpkg.bat
```

Integrarea vcpkg cu Visual Studio:

```powershell
.\vcpkg integrate install
```

Instalarea bibliotecilor necesare:

```powershell
.\vcpkg install opencv:x64-windows
.\vcpkg install tbb:x64-windows
```

---

## ▶️ Rulare Proiect

1. Deschideți soluția `.sln` în Visual Studio.
2. Selectați:

   * `Debug | x64`
3. Asigurați-vă că standardul C++ este:

   * `ISO C++17`
4. Rulați proiectul folosind:

   * `Ctrl + F5`

---

## 🌿 Branch-uri

Proiectul este organizat pe branch-uri separate:

* `main` → versiunea finală
* `secvential` → implementare secvențială
* `tbb-inter` → paralelizare între imagini
* `tbb-intra` → paralelizare în interiorul imaginii
