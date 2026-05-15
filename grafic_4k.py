import matplotlib.pyplot as plt
import numpy as np

# Datele exacte calculate de pe setul 4K (inclusiv 6 threads)
metode = ['Secvențial', 'TBB Intra\n(6 th)', 'TBB Intra\n(12 th)', 'CUDA GPU\n(16x16)', 'TBB Inter\n(6 th)', 'TBB Inter\n(12 th)']
timpi = [41.82706, 33.86617, 33.12928, 30.20892, 9.60625, 7.69150]

# O paletă de culori logică: Gri (Secvențial), Portocaliu (Intra), Verde (CUDA), Albastru (Inter)
culori = ['#7f7f7f', '#ffb07c', '#ff7f0e', '#2ca02c', '#6baed6', '#1f77b4'] 

plt.style.use('seaborn-v0_8-whitegrid')
plt.figure(figsize=(11, 6))

# Generăm barele
bare = plt.bar(metode, timpi, color=culori, width=0.65, alpha=0.9, edgecolor='black', linewidth=1.2)

# Adăugăm numărul exact de secunde deasupra fiecărei bare
for bara in bare:
    inaltime = bara.get_height()
    plt.text(bara.get_x() + bara.get_width()/2, inaltime + 0.5, 
             f'{inaltime:.2f} s', ha='center', va='bottom', 
             fontweight='bold', fontsize=11)

plt.title('Performanța Arhitecturilor pe Imagini 4K (50 Imagini)', fontsize=15, fontweight='bold', pad=20)
plt.ylabel('Timp Total (secunde) - Mai puțin este mai bine', fontsize=12, fontweight='bold')
plt.ylim(0, 50)
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Căsuța explicativă pentru limitarea PCIe
plt.text(3, 44, "Magistrala PCIe\nlimitează masiv CUDA!", 
         bbox=dict(facecolor='#f0f0f0', edgecolor='gray', boxstyle='round,pad=0.5'),
         ha='center', fontsize=11, color='#d62728', fontweight='bold', style='italic')

plt.savefig('Tabelul_5.png', dpi=300, bbox_inches='tight')
plt.show()