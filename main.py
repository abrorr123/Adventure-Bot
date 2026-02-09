import time
import random

class BajakLaut:
    """Kelas untuk menyimpan data pemain bajak laut"""
    def __init__(self, nama):
        self.nama = nama
        self.max_kesehatan = 100
        self.kesehatan = self.max_kesehatan
        self.energi = 100
        self.emas = 1000
        self.inventory = ['Pedang', 'Peta Peramal']
        self.level = 1
        self.pengalaman = 0
        self.lokasi = "Pelabuhan Karib"
        self.kekuatan_senjata = 1  # Tier senjata (1-10)
        
    def tampilkan_status(self):
        """Menampilkan status pemain"""
        print(f"\n{'='*50}")
        print(f"🏴‍☠️ NAMA BAJAK LAUT: {self.nama}")
        print(f"{'='*50}")
        print(f"❤️ Kesehatan: {self.kesehatan}/{self.max_kesehatan}")
        print(f"⚡ Energi: {self.energi}/100")
        print(f"💰 Emas: {self.emas} koin")
        print(f"📍 Lokasi: {self.lokasi}")
        print(f"⭐ Level: {self.level} | Pengalaman: {self.pengalaman}")
        print(f"🗡️ Kekuatan Senjata: {self.kekuatan_senjata}/10")
        print(f"🎒 Inventory ({len(self.inventory)}): {', '.join(self.inventory)}")
        print(f"{'='*50}\n")
    
    def ambil_damage(self, jumlah):
        """Pemain menerima damage"""
        self.kesehatan -= jumlah
        if self.kesehatan < 0:
            self.kesehatan = 0
        print(f"⚔️ Anda menerima {jumlah} kerusakan! Kesehatan tersisa: {self.kesehatan}")
        
    def sembuh(self, jumlah):
        """Pemain melakukan penyembuhan"""
        self.kesehatan += jumlah
        if self.kesehatan > self.max_kesehatan:
            self.kesehatan = self.max_kesehatan
        print(f"🩹 Kesehatan pulih {jumlah} poin!")

class Musuh:
    """Kelas untuk berbagai tipe musuh"""
    def __init__(self, tipe, level_pemain=1):
        self.tipe = tipe
        self.level_pemain = level_pemain
        
        # Tentukan range tier berdasarkan level pemain
        self.tier = self._hitung_tier_musuh()
        
        if tipe == "Bajak Laut":
            self.nama = random.choice(["Kapten Blackbeard", "Si Bajak Merah", "Bajak Punah", "Bajak Pemberani"])
            self.kesehatan = 30 + (self.tier * 5)
            self.damage = 10 + (self.tier * 2)
            self.hadiah_emas = 150 + (self.tier * 50)
            self.deskripsi = f"Seorang bajak laut bersenjata yang ganas"
            
        elif tipe == "Monster Laut":
            self.nama = random.choice(["Kraken Mini", "Raksasa Gurita", "Naga Laut", "Paus Raksasa"])
            self.kesehatan = 40 + (self.tier * 6)
            self.damage = 15 + (self.tier * 2)
            self.hadiah_emas = 250 + (self.tier * 80)
            self.deskripsi = f"Makhluk menakutkan dari kedalaman laut"
        
        else:  # Bajak Laut Legendaris
            self.nama = random.choice(["Daud Barbershop", "Blackstone", "Sang Dewa Laut"])
            self.kesehatan = 50 + (self.tier * 7)
            self.damage = 20 + (self.tier * 3)
            self.hadiah_emas = 800 + (self.tier * 150)
            self.deskripsi = f"Musuh legendaris dengan kekuatan super"
    
    def _hitung_tier_musuh(self):
        """Menghitung tier musuh berdasarkan level pemain dengan distribusi probabilitas"""
        if self.level_pemain == 1:
            chance = random.randint(1, 100)
            if chance <= 60:
                return 1
            elif chance <= 90:
                return 2
            else:
                return 3
        
        elif self.level_pemain == 2:
            chance = random.randint(1, 100)
            if chance <= 25:
                return 1
            elif chance <= 65:
                return 2
            elif chance <= 85:
                return 3
            else:
                return 4
        
        elif self.level_pemain == 3:
            chance = random.randint(1, 100)
            if chance <= 20:
                return 2
            elif chance <= 50:
                return 3
            elif chance <= 75:
                return 4
            else:
                return 5
        
        elif self.level_pemain == 4:
            chance = random.randint(1, 100)
            if chance <= 15:
                return 3
            elif chance <= 35:
                return 4
            elif chance <= 60:
                return 5
            else:
                return 6
        
        else:
            base_tier = min(5 + (self.level_pemain - 5), 8)
            max_tier = min(base_tier + 3, 10)
            return random.randint(base_tier, max_tier)
    
    def tampilkan_musuh(self):
        """Menampilkan informasi musuh"""
        print(f"\n🗡️ Musuh Muncul: {self.nama} ({self.tipe})")
        print(f"Deskripsi: {self.deskripsi}")
        print(f"❤️ Kesehatan: {self.kesehatan}")
        print(f"⚔️ Damage: {self.damage}")
        print(f"📊 Tier Musuh: {self.tier}/10\n")

def layar_utama():
    """Menampilkan menu utama"""
    print("\n")
    print("╔═══════════════════════════════════════════════╗")
    print("║     🏴‍☠️ GAME PETUALANGAN BAJAK LAUT 🏴‍☠️      ║")
    print("║        MENCARI HARTA KARUN DI LAUTAN LUAS      ║")
    print("╚═══════════════════════════════════════════════╝")
    print("\n1. 📖 Mulai Pertualangan Baru")
    print("2. ⛵ Baca Cerita Permainan")
    print("3. ❌ Keluar Permainan\n")

def cerita_permainan():
    """Menampilkan cerita latar belakang permainan"""
    print("\n" + "="*50)
    print("📖 CERITA LATAR BELAKANG")
    print("="*50)
    print("""
Anda adalah seorang bajak laut pemberani yang telah mendengar
legenda tentang harta karun terbesar di samudra. Konon kabarnya,
ada 5 harta karun yang tersembunyi di berbagai pulau dan goa
bawah laut.

Namun perjalanan Anda tidak akan mudah! Bajak laut lain juga
mencari harta yang sama, monster-monster menakutkan menjaga
gua-gua tersebut, dan cuaca ganas akan menghambat perjalanan Anda.

Persenjataan Anda yang terbatas memaksa Anda harus pintar
dalam memilih pertarungan. Cari sekutu, kumpulkan perlengkapan,
dan jadilah bajak laut paling legendaris sepanjang masa!

Apakah Anda siap menerima tantangan ini?
""")
    print("="*50 + "\n")

def cerita_awal(nama):
    """Menampilkan cerita pembukaan"""
    print("\n" + "─"*50)
    print(f"Selamat datang, {nama}!")
    print("─"*50)
    print("""
Suara ombak yang menggampar menyambut Anda saat kapal berlayar
menjauh dari Pelabuhan Karib. Di tangan Anda, sebuah peta tua
dengan X merah yang menandai harta karun.

Mata Anda memandang lautan luas yang misterius. Kabar angin
menyebutkan ada 5 harta karun besar tersembunyi. Anda harus
menemukan semuanya!

Tapi tunggu... apakah itu siluet kapal lain di kejauhan?
""")
    time.sleep(2)
    print("Petualangan Anda dimulai...\n")

def menu_aksi():
    """Menampilkan menu aksi selama permainan"""
    print("\n┌─ PILIHAN AKSI ─┐")
    print("1. ⚔️ Berburu Harta Karun")
    print("2. 🛠️ Kunjungi Bengkel Kapal")
    print("3. 🏥 Kunjungi Medis")
    print("4. 📍 Pindah Lokasi")
    print("5. 📊 Lihat Status Anda")
    print("6. 🗺️ Lihat Petualangan")
    print("7. ❌ Akhiri Petualangan")
    print("└─────────────────┘\n")

def berburu_harta(pemain):
    """Sistem berburu harta karun dengan kejadian acak"""
    if pemain.energi < 20:
        print("⚠️ Energi Anda tidak cukup untuk berburu harta karun!")
        return
    
    kejadian = random.randint(1, 100)
    
    if kejadian <= 30:  # Bertemu Bajak Laut
        print("\n🏴‍☠️ PERJALANAN KE LAUT...\n")
        time.sleep(1)
        print("Anda melihat kapal lain mendekati Anda dengan bendera tengkorak!")
        pertarungan(pemain, Musuh("Bajak Laut", pemain.level))
        pemain.energi -= 20
        
    elif kejadian <= 60:  # Bertemu Monster Laut
        print("\n🌊 PERJALANAN KE LAUT...\n")
        time.sleep(1)
        print("Mendadak, air laut bergejolak! Ada sesuatu yang besar muncul dari kedalaman!")
        pertarungan(pemain, Musuh("Monster Laut", pemain.level))
        pemain.energi -= 25
        
    elif kejadian <= 80:  # Ditemukan Harta Karun
        print("\n✨ PERJALANAN KE LAUT...\n")
        time.sleep(1)
        print("Peta Anda bersinar! Anda telah menemukan lokasi harta karun!")
        
        musuh_mungkin = random.randint(1, 100)
        
        if musuh_mungkin <= 50:
            print("Tapi ada penjaga fantastis di sini!")
            pertarungan(pemain, Musuh("Bajak Laut Legendaris", pemain.level))
        
        pemain.emas += 1500
        print(f"💰 Anda menemukan harta karun! +1500 emas!")
        print(f"Total emas sekarang: {pemain.emas}")
        pemain.pengalaman += 50
        pemain.energi -= 30
        
    else:  # Cuaca Buruk
        print("\n⛈️ BADAI LAUT MUNCUL!\n")
        kerusakan = random.randint(10, 30)
        print(f"Badai menerpa kapal Anda! Anda menerima {kerusakan} kerusakan!")
        pemain.ambil_damage(kerusakan)
        pemain.energi -= 15

def pertarungan(pemain, musuh):
    """Sistem pertarungan turn-based dengan berbagai pilihan aksi"""
    musuh.tampilkan_musuh()
    
    # Tampilkan analisis pertarungan
    print(f"📊 ANALISIS PERTARUNGAN:")
    print(f"Senjata Anda (Tier {pemain.kekuatan_senjata}/10) vs Musuh (Tier {musuh.tier}/10)")
    strength_diff = pemain.kekuatan_senjata - musuh.tier
    if strength_diff >= 3:
        print("✅ Anda JAUH lebih kuat dari musuh ini!")
    elif strength_diff >= 1:
        print("✅ Anda lebih kuat dari musuh ini!")
    elif strength_diff > -3:
        print("⚠️ Pertarungan seimbang, hati-hati!")
    else:
        print("❌ Musuh ini JAUH lebih kuat! Pertimbangkan untuk mundur!")
    print()
    
    giliran_pemain = True
    
    while pemain.kesehatan > 0 and musuh.kesehatan > 0:
        print(f"\n├─ KESEHATAN ANDA: {pemain.kesehatan} | KESEHATAN MUSUH: {musuh.kesehatan}")
        
        if giliran_pemain:
            print("\n🎯 GILIRAN ANDA!")
            print("1. ⚔️ Serang Normal (Damage 15-25)")
            print("2. 🌪️ Serangan Kaya (Damage 30-40 tapi risiko 50%)")
            print("3. 🛡️ Pertahanan (Kurangi damage 50%)")
            print("4. 🩹 Gunakan Potion (+30 kesehatan, Harga 100)")
            print("5. 🏃 Mundur (Biaya: 50 emas)")
            
            pilihan = input("Pilihan Anda: ").strip()
            
            if pilihan == "1":
                damage = random.randint(15, 25) + (pemain.kekuatan_senjata * 2)
                musuh.kesehatan -= damage
                print(f"⚔️ Anda menyerang! Damage: {damage}")
                
            elif pilihan == "2":
                jika_sukses = random.randint(1, 100) <= 50
                if jika_sukses:
                    damage = random.randint(30, 40) + (pemain.kekuatan_senjata * 3)
                    musuh.kesehatan -= damage
                    print(f"🌪️ Serangan Kaya Sukses! Damage : {damage}")
                else:
                    print("😵 Serangan Kaya Gagal! Musuh langsung menyerang...")
                    damage_musuh = random.randint(int(musuh.damage * 1.5), int(musuh.damage * 2))
                    pemain.ambil_damage(damage_musuh)
                    giliran_pemain = True
                    continue
                    
            elif pilihan == "3":
                print("🛡️ Anda Mengambil Posisi Pertahanan!")
                pertahanan_aktif = True
                
            elif pilihan == "4":
                if pemain.emas >= 100:
                    pemain.emas -= 100
                    pemain.sembuh(30)
                    print(f"Sisa emas: {pemain.emas}")
                else:
                    print("❌ Emas tidak cukup!")
                    continue
            
            elif pilihan == "5":
                if pemain.emas >= 50:
                    pemain.emas -= 50
                    print(f"🏃 Anda berhasil melarikan diri! (-50 emas)")
                    print(f"Sisa emas: {pemain.emas}")
                    return
                else:
                    print("❌ Emas tidak cukup untuk mundur!")
                    continue
            
            else:
                print("❌ Pilihan tidak valid!")
                continue
                
            giliran_pemain = False
            
        else:
            print(f"\n🗡️ GILIRAN {musuh.nama}!")
            time.sleep(1)
            
            damage_musuh = random.randint(int(musuh.damage * 0.8), int(musuh.damage * 1.2))
            
            if 'pertahanan_aktif' in locals() and pertahanan_aktif:
                damage_musuh = int(damage_musuh / 2)
                print(f"Musuh menyerang! Damage dikurangi 50%: {damage_musuh}")
                pertahanan_aktif = False
            else:
                print(f"Musuh menyerang! Damage: {damage_musuh}")
            
            pemain.ambil_damage(damage_musuh)
            giliran_pemain = True
    
    if pemain.kesehatan > 0:
        print(f"\n🎉 KEMENANGAN! Anda mengalahkan {musuh.nama}!")
        print(f"💰 Anda mendapatkan {musuh.hadiah_emas} emas!")
        pemain.emas += musuh.hadiah_emas
        pemain.pengalaman += 30
        pemain.level += 1 if pemain.pengalaman >= 100 else 0
        if pemain.pengalaman >= 100:
            pemain.pengalaman = 0
            print("⭐ LEVEL UP! Anda naik level!")
    else:
        print(f"\n💀 KEKALAHAN! Anda dikalahkan oleh {musuh.nama}...")
        print("⛵ Anda berhasil melarikan diri dan kembali ke pelabuhan.")
        pemain.kesehatan = 50
        pemain.lokasi = "Pelabuhan Karib"

def bengkel_kapal(pemain):
    """Toko untuk upgrade kapal dan pembelian item"""
    print("\n🛠️ === BENGKEL KAPAL ===")
    print(f"Saldo Anda: {pemain.emas} emas")
    print(f"Kekuatan Senjata: {pemain.kekuatan_senjata}/10\n")
    print("1. 🛡️ Perkuat Badan Kapal (+20 kesehatan, Harga: 300)")
    print("2. ⚡ Upgrade Mesin Kapal (+20 energi max, Harga: 400)")
    print("3. 🗡️ Upgrade Senjata (+1 tier kekuatan, Harga: 200)")
    print("4. 💰 Beli Pedang Legendaris (+3 tier kekuatan sekaligus, Harga: 800)")
    print("5. 🩹 Beli Potion (+30 kesehatan saat pertarungan, Harga: 100)")
    print("6. ❌ Keluar\n")
    
    pilihan = input("Pilihan Anda: ").strip()
    
    if pilihan == "1":
        if pemain.emas >= 300:
            pemain.emas -= 300
            pemain.max_kesehatan += 20
            print(f"✅ Kapal Anda diperkuat! Maksimal kesehatan naik menjadi {pemain.max_kesehatan}.")
        else:
            print("❌ Emas tidak cukup!")
            
    elif pilihan == "2":
        if pemain.emas >= 400:
            pemain.emas -= 400
            pemain.energi = min(pemain.energi + 20, 100)
            print("✅ Mesin kapal Anda diperbaiki!")
        else:
            print("❌ Emas tidak cukup!")
            
    elif pilihan == "3":
        if pemain.kekuatan_senjata >= 10:
            print("❌ Senjata Anda sudah pada level maksimal!")
        elif pemain.emas >= 200:
            pemain.emas -= 200
            pemain.kekuatan_senjata = min(pemain.kekuatan_senjata + 1, 10)
            print(f"⚔️ Senjata Anda ditingkatkan! Kekuatan: {pemain.kekuatan_senjata}/10")
        else:
            print("❌ Emas tidak cukup!")
    
    elif pilihan == "4":
        if pemain.kekuatan_senjata >= 10:
            print("❌ Senjata Anda sudah pada level maksimal!")
        elif pemain.emas >= 800:
            pemain.emas -= 800
            pemain.kekuatan_senjata = min(pemain.kekuatan_senjata + 3, 10)
            pemain.inventory.append("Pedang Legendaris")
            print(f"💰 Pedang Legendaris diperoleh! Kekuatan: {pemain.kekuatan_senjata}/10")
        else:
            print("❌ Emas tidak cukup!")
            
    elif pilihan == "5":
        if pemain.emas >= 100:
            pemain.emas -= 100
            pemain.inventory.append("Potion")
            print("✅ Potion ditambahkan ke inventory!")
        else:
            print("❌ Emas tidak cukup!")

def medis(pemain):
    """Klinik untuk penyembuhan"""
    print("\n🏥 === KLINIK MEDIS ===")
    print(f"Kesehatan Anda: {pemain.kesehatan}/100")
    print(f"Saldo Anda: {pemain.emas} emas\n")
    print("1. 🩹 Penyembuhan Ringan (+25 kesehatan, Harga: 50)")
    print("2. 💊 Penyembuhan Sedang (+50 kesehatan, Harga: 150)")
    print("3. 💉 Penyembuhan Total (Kesehatan Penuh, Harga: 300)")
    print("4. ❌ Keluar\n")
    
    pilihan = input("Pilihan Anda: ").strip()
    
    if pilihan == "1":
        if pemain.emas >= 50:
            pemain.emas -= 50
            pemain.sembuh(25)
        else:
            print("❌ Emas tidak cukup!")
            
    elif pilihan == "2":
        if pemain.emas >= 150:
            pemain.emas -= 150
            pemain.sembuh(50)
        else:
            print("❌ Emas tidak cukup!")
            
    elif pilihan == "3":
        if pemain.emas >= 300:
            pemain.emas -= 300
            pemain.kesehatan = pemain.max_kesehatan
            print(f"💉 Anda sepenuhnya disembuhkan! Kesehatan: {pemain.kesehatan}/{pemain.max_kesehatan}")
        else:
            print("❌ Emas tidak cukup!")

def pindah_lokasi(pemain):
    """Sistem perjalanan ke lokasi berbeda"""
    print("\n📍 === PILIH LOKASI ===\n")
    lokasi_list = [
        "Pelabuhan Karib",
        "Pulau Tengkorak",
        "Goa Bawah Laut",
        "Pulau Harta Legender",
        "Pulau Misterius"
    ]
    
    for i, lokasi in enumerate(lokasi_list, 1):
        print(f"{i}. {lokasi}")
    
    print(f"\nLokasi sekarang: {pemain.lokasi}\n")
    pilihan = input("Pilih lokasi (nomor): ").strip()
    
    try:
        idx = int(pilihan) - 1
        if 0 <= idx < len(lokasi_list):
            pemain.lokasi = lokasi_list[idx]
            print(f"✈️ Anda berpindah ke {pemain.lokasi}")
            pemain.energi -= 10
        else:
            print("❌ Pilihan tidak valid!")
    except:
        print("❌ Masukkan angka yang valid!")

def permainan_berjalan(pemain):
    """Loop utama permainan"""
    harta_ditemukan = 0
    
    while pemain.kesehatan > 0:
        menu_aksi()
        pilihan = input("Pilihan Anda: ").strip()
        
        if pilihan == "1":
            berburu_harta(pemain)
            harta_ditemukan += 1
            
        elif pilihan == "2":
            bengkel_kapal(pemain)
            
        elif pilihan == "3":
            medis(pemain)
            
        elif pilihan == "4":
            pindah_lokasi(pemain)
            
        elif pilihan == "5":
            pemain.tampilkan_status()
            
        elif pilihan == "6":
            print(f"\n📊 STATISTIK PETUALANGAN:")
            print(f"Harta Karun Ditemukan: {harta_ditemukan}")
            print(f"Total Emas: {pemain.emas}")
            print(f"Level: {pemain.level}")
            
        elif pilihan == "7":
            print(f"\n🎉 Petualangan Berakhir!")
            print(f"Anda mengumpulkan {pemain.emas} emas!")
            print(f"Total Harta Karun Ditemukan: {harta_ditemukan}")
            print("Terima kasih telah bermain!\n")
            break
        else:
            print("❌ Pilihan tidak valid!")
        
        # Regenerasi energi sedikit setiap giliran
        pemain.energi = min(pemain.energi + 5, 100)
        
        if pemain.kesehatan <= 0:
            print("\n💀 Anda tewas dalam pertarungan! Game Over!")
            break
    
    print(f"\n{'='*50}")
    print("STATISTIK AKHIR PERMAINAN")
    print(f"{'='*50}")
    pemain.tampilkan_status()

def game_utama():
    """Fungsi utama permainan"""
    layar_utama()
    
    while True:
        pilihan = input("Pilih menu: ").strip()
        
        if pilihan == "1":
            nama = input("Siapa nama bajak laut Anda? ").strip()
            if not nama:
                nama = "Pelaut Pemberani"
            
            pemain = BajakLaut(nama)
            cerita_awal(nama)
            permainan_berjalan(pemain)
            break
            
        elif pilihan == "2":
            cerita_permainan()
            
        elif pilihan == "3":
            print("\n👋 Terima kasih telah bermain! Sampai jumpa!\n")
            break
        else:
            print("❌ Pilihan tidak valid!")
    
if __name__ == "__main__":
    game_utama()

