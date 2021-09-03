import pandas as pd

# Data
data = pd.read_csv('jadwal_vaksin.csv')


# Jumlah Siswa Kelas
def jmls_kel(kelas, data=data):
    print('*siswa yang ikut vaksin')
    if kelas == 10:
        x = data.loc[data['Kelas']==10].count()
        print('===')
        print(f"\t~Jumlah Siswa Kelas 10 :{x['Kelas']}")
        print('===\n')
        return x['Kelas']
    elif kelas == 11:
        xi = data.loc[data['Kelas']==11].count()
        print('===')
        print(f"\t~Jumlah Siswa Kelas 11 :{xi['Kelas']}")
        print('===\n')
        return xi['Kelas']
    elif kelas == 12:
        xii = data.loc[data['Kelas']==12].count()
        print('===')
        print(f"\t~Jumlah Siswa Kelas 12 :{xii['Kelas']}")
        print('===\n')
        return xii['Kelas']
    elif kelas == 'semua':
        semua = data['Kelas'].count()
        print('===')
        print(f"\t~Jumlah Siswa :{semua}")
        print('===\n')
        return semua
    else:
        print('\t_input (10/11/12/semua) saja_')

#Frame Siswa
def freq_kel(kelas, data=data, bag=['Nama','Peminatan']):
    if kelas == 10:
        x = data.loc[data['Kelas'] == 10]
        print('===KELAS 10===')
        print(x[bag])
        print('===\n')
    elif kelas == 11:
        xi = data.loc[data['Kelas'] == 11]
        print('===KELAS 11===')
        print(xi[bag])
        print('===\n')
    elif kelas == 12:
        xii = data.loc[data['Kelas'] == 12]
        print('===KELAS 12===')
        print(xii[bag])
        print('===\n')
    elif kelas == 'semua':
        print('===SEMUA===')
        semua = data
        print(semua[bag])
        print('===\n')
        return semua
    else:
        print('\t_input (10/11/12/semua) saja_')

#List Kecamatan
def li_kec():
    d = data.groupby('Kecamatan')['Nama'].count()
    print(d)
    return d

#Fitur Cari
