import matplotlib.pyplot as plt
import numpy as np

# ==========================================
# 1. DATELE EXACTE DIN TABELE
# ==========================================
threads = np.array([1, 2, 4, 6, 12])

# Timpi de execuție (secunde)
timp_secvential = 32.31598
timp_cuda = 13.06678
timp_inter = np.array([33.18581, 17.58544, 10.88164, 8.696095, 7.263378])
timp_intra = np.array([33.35816, 25.67054, 22.10807, 20.08613, 19.62377])

# Speedup
speedup_inter = np.array([0.97379, 1.83766, 2.96977, 3.71615, 4.44917])
speedup_intra = np.array([0.96876, 1.25887, 1.46173, 1.60887, 1.64678])

# Calcule noi pentru Graficele 3 si 4
eficienta_inter = (speedup_inter / threads) * 100
eficienta_intra = (speedup_intra / threads) * 100
overhead = timp_intra - timp_inter

plt.style.use('seaborn-v0_8-whitegrid')

# ==========================================
# GRAFICUL 1: SPEEDUP (ACCELERARE)
# ==========================================
plt.figure(figsize=(10, 6))
plt.plot(threads, speedup_inter, marker='o', linewidth=2.5, markersize=8, color='#1f77b4', label='Speedup TBB Inter')
plt.plot(threads, speedup_intra, marker='s', linewidth=2.5, markersize=8, color='#ff7f0e', label='Speedup TBB Intra')
plt.plot([1, 12], [1, 12], color='gray', linestyle=':', linewidth=2, alpha=0.6, label='Scalabilitate Liniară (Ideală)')

plt.title('Accelerarea Algoritmilor (Speedup)', fontsize=14, fontweight='bold', pad=15)
plt.xlabel('Număr Thread-uri', fontsize=12, fontweight='bold')
plt.ylabel('Speedup (T_secvențial / T_paralel)', fontsize=12, fontweight='bold')
plt.xticks(threads)
plt.yticks(np.arange(0, 13, 1)) 
plt.ylim(0, 15)
plt.legend(fontsize=10, loc='upper center', ncol=3)
plt.grid(True, linestyle='--', alpha=0.7)
plt.savefig('Tabelul_1.png', dpi=300, bbox_inches='tight')

# ==========================================
# GRAFICUL 2: TIMP DE EXECUȚIE
# ==========================================
plt.figure(figsize=(10, 6))
plt.plot(threads, timp_inter, marker='o', linewidth=2.5, markersize=8, color='#1f77b4', label='TBB Inter-Imagine')
plt.plot(threads, timp_intra, marker='s', linewidth=2.5, markersize=8, color='#ff7f0e', label='TBB Intra-Imagine')
plt.axhline(y=timp_secvential, color='#d62728', linestyle='--', linewidth=2, label=f'Secvențial (Baseline: {timp_secvential:.2f} s)')
plt.axhline(y=timp_cuda, color='#2ca02c', linestyle='-.', linewidth=2, label=f'CUDA GPU ({timp_cuda:.2f} s)')

plt.title('Evoluția Timpului de Execuție în funcție de Thread-uri', fontsize=14, fontweight='bold', pad=15)
plt.xlabel('Număr Thread-uri', fontsize=12, fontweight='bold')
plt.ylabel('Timp Total (secunde)', fontsize=12, fontweight='bold')
plt.xticks(threads) 
plt.ylim(0, 43)
plt.legend(fontsize=10, loc='upper center', ncol=2)
plt.grid(True, linestyle='--', alpha=0.7)
plt.savefig('Tabelul_2.png', dpi=300, bbox_inches='tight')

# ==========================================
# GRAFICUL 3: EFICIENȚA PER THREAD (%)
# ==========================================
plt.figure(figsize=(10, 6))
plt.plot(threads, eficienta_inter, marker='o', linewidth=2.5, markersize=8, color='#1f77b4', label='Eficiență TBB Inter')
plt.plot(threads, eficienta_intra, marker='s', linewidth=2.5, markersize=8, color='#ff7f0e', label='Eficiență TBB Intra')
plt.axhline(y=100, color='gray', linestyle=':', linewidth=2, alpha=0.6, label='Eficiență Maximă (100%)')

plt.title('Eficiența Paralelizării (Speedup / Număr Thread-uri)', fontsize=14, fontweight='bold', pad=15)
plt.xlabel('Număr Thread-uri', fontsize=12, fontweight='bold')
plt.ylabel('Eficiență (%)', fontsize=12, fontweight='bold')
plt.xticks(threads)
plt.ylim(0, 125)
plt.legend(fontsize=10, loc='upper center', ncol=3)
plt.grid(True, linestyle='--', alpha=0.7)
plt.savefig('Tabelul_3.png', dpi=300, bbox_inches='tight')

# ==========================================
# GRAFICUL 4: PENALIZAREA DE OVERHEAD (Secunde)
# ==========================================
# Folosim un grafic cu bare pentru a arăta clar timpul adăugat de overhead
plt.figure(figsize=(10, 6))
bare = plt.bar(threads, overhead, color='#d62728', alpha=0.8, width=0.8, label='Timp suplimentar pierdut (Intra vs Inter)')

# Adăugăm numărul de secunde deasupra fiecărei bare pentru claritate
for bara in bare:
    inaltime = bara.get_height()
    plt.text(bara.get_x() + bara.get_width()/2, inaltime + 0.3, f'+{inaltime:.1f}s', ha='center', va='bottom', fontweight='bold', fontsize=10)

plt.title('Penalizarea de Performanță: Overhead TBB Intra', fontsize=14, fontweight='bold', pad=15)
plt.xlabel('Număr Thread-uri', fontsize=12, fontweight='bold')
plt.ylabel('Timp pierdut (secunde)', fontsize=12, fontweight='bold')
plt.xticks(threads)
plt.ylim(0, 16)
plt.legend(fontsize=10, loc='upper center')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.savefig('Tabelul_4.png', dpi=300, bbox_inches='tight')

plt.show()