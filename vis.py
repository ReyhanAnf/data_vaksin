from jvak import *
import matplotlib.pyplot as plt

#jumlah siswa perkelas
#param = v_jmls_kel(jmls_kel(kelas 10/11/12))
def v_jmls_kel(jmls_kel=[jmls_kel(10),jmls_kel(11),jmls_kel(12)]):
    plt.figure(figsize=(7,5), dpi=70)
    plt.xlabel('Kelas')
    plt.ylabel('Banyak Siswa')
    plt.title('Perbandingan Banyak Siswa', fontdict={'fontsize':24, 'fontweight':'bold'})
    plt.grid()
    plt.bar(['10','11','12'],jmls_kel)
    plt.show()

def v_kec(kec=data['Kecamatan'],n=li_kec()):
    kc = list(dict.fromkeys([x for x in kec]))
    plt.figure(figsize=(7,5), dpi=70)
    plt.xlabel('Banyak Siswa')
    plt.ylabel('Kecamatan')
    plt.title('Asal Kecamatan Siswa', fontdict={'fontsize':24, 'fontweight':'bold'})
    plt.grid()
    plt.barh(kc, n, color='orange')
    plt.show()

v_jmls_kel()