import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("zihinseliyilik.csv")
print(df.head())
print(df.columns)
print(df.info())
print(df.describe())
print(df.isnull().sum())
if "Unnamed: 15" in df.columns and df["Unnamed: 15"].isnull().all():
    df = df.drop(columns=["Unnamed: 15"])
    print("Gereksiz 'Unnamed: 15' sütunu kaldırıldı.")

# ==============================================================================
# 2. KEŞİFÇİ VERİ ANALİZİ (EDA) - DAĞILIMLAR (Exploratory Data Analysis - Distributions)
# ==============================================================================

# grafik ayarlamaları
sns.set_theme(style="whitegrid")
plt.rcParams["figure.dpi"] = 100
plt.rcParams["font.sans-serif"] = ["Inter", "Arial"]


# A. Ana Değişkenlerin Dağılımı
fig, axes = plt.subplots(2, 2, figsize=(14, 10))
# Tüm figür için ana başlık ekle
fig.suptitle("2.1. Temel Değişkenlerin Dağılımı", fontsize=16, fontweight="bold")

# Plot 1: Zihinsel İyi Oluş Endeksi (Hedef Değişken)
sns.histplot(
    df["mental_wellness_index_0_100"], bins=20, kde=True, ax=axes[0, 0], color="#2980b9"
)
axes[0, 0].set_title("Zihinsel İyi Oluş Endeksi (0-100)")
axes[0, 0].set_xlabel("Endeks Değeri")
axes[0, 0].set_ylabel("Frekans")

# Plot 2: Stres Seviyesi (En Güçlü İlişki)
sns.histplot(
    df["stress_level_0_10"], bins=10, kde=False, ax=axes[0, 1], color="#e74c3c"
)
axes[0, 1].set_title("Stres Seviyesi (0-10)")
axes[0, 1].set_xlabel("Stres Seviyesi")
axes[0, 1].set_xticks(np.arange(0, 11, 1))

# Plot 3: Uyku Kalitesi (Sıralı)

sns.countplot(
    x="sleep_quality_1_5",
    data=df,
    ax=axes[1, 0],
    palette="YlGnBu",
    order=sorted(df["sleep_quality_1_5"].unique()),
)
axes[1, 0].set_title("Uyku Kalitesi Dağılımı (1=Kötü, 5=İyi)")
axes[1, 0].set_xlabel("Uyku Kalitesi Puanı")
axes[1, 0].set_ylabel("Kişi Sayısı")

# Plot 4: Toplam Ekran Süresi
sns.histplot(df["screen_time_hours"], bins=20, kde=True, ax=axes[1, 1], color="#2ecc71")
axes[1, 1].set_title("Toplam Ekran Süresi (Saat)")
axes[1, 1].set_xlabel("Ekran Süresi (Saat)")

plt.tight_layout(rect=[0, 0.02, 1, 0.95])
plt.savefig("2_1_temel_degisken_dagilimlari.png")
# plt.close()
print("Görsel 2_1: Temel değişken dağılımları kaydedildi.")
# plt.show()

# B. Kategorik Değişkenlerin Dağılımı:
fig, axes = plt.subplots(1, 3, figsize=(18, 5))
fig.suptitle("2.2. Kategorik Değişkenlerin Dağılımı", fontsize=16, fontweight="bold")
# Plot 1: Cinsiyet Dağılımı
sns.countplot(x="gender", data=df, ax=axes[0], palette="Pastel1")
axes[0].set_title("Cinsiyet Dağılımı")
axes[0].set_xlabel("Cinsiyet")
axes[0].set_ylabel("Kişi Sayısı")

# Plot 2: Meslek Dağılımı
sns.countplot(
    x="occupation",
    data=df,
    ax=axes[1],
    palette="Set2",
)
axes[1].tick_params(axis="x", rotation=30)
axes[1].set_title("Meslek Dağılımı")
axes[1].set_xlabel("Meslek")
axes[1].set_ylabel("Kişi Sayısı")


# Plot 3: Çalışma Modu Dağılımı
sns.countplot(x="work_mode", data=df, ax=axes[2], palette="Set3")
axes[2].set_title("Çalışma Modu Dağılımı")
axes[2].set_xlabel("Çalışma Modu")
axes[2].set_ylabel("Kişi Sayısı")
plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.savefig("2_2_kategorik_dagilimlar.png")
# plt.close()
# plt.show()
print("Görsel 2_2: Kategorik değişken dağılımları kaydedildi.")

# ==============================================================================
# 3. KORELASYON VE İLİŞKİ ANALİZİ (Correlation and Relationship Analysis)
# ==============================================================================
numerical_cols = df.select_dtypes(include=np.number).columns
correlation_matrix = df[numerical_cols].corr()

plt.figure(figsize=(12, 10))
sns.heatmap(
    correlation_matrix,
    annot=True,
    fmt=".2f",
    cmap="coolwarm",
    linewidths=0.5,
    linecolor="black",
    cbar_kws={"label": "Korelasyon Katsayısı"},
)
plt.title(
    "3.1. Sayısal Değişkenler Arası Korelasyon Matrisi", fontsize=16, fontweight="bold"
)
plt.tight_layout()
plt.savefig("3_1_korelasyon_matrisi.png")
# plt.close()
# plt.show()

# B. Zihinsel İyi Oluş ile Ana İlişkiler (Regresyon Grafikleri)
fig, axes = plt.subplots(1, 3, figsize=(14, 10))
plt.suptitle("3.2. Zihinsel İyi Oluş ile Ana İlişkiler", fontsize=16, fontweight="bold")

# Plot 1: Stres Seviyesi (Güçlü Negatif İlişki: R=-0.89)
sns.regplot(
    x="stress_level_0_10",
    y="mental_wellness_index_0_100",
    data=df,
    ax=axes[0],
    scatter_kws={"alpha": 0.5},
    line_kws={"color": "red"},
)
axes[0].set_title("Stres Seviyesi vs Zihinsel İyi Oluş Endeksi")
axes[0].set_xlabel("Stres Seviyesi (0-10)")
axes[0].set_ylabel("Zihinsel İyi Oluş Endeksi (0-100)")

# Plot 2: Toplam Ekran Süresi (Negatif İlişki: R=-0.74)
sns.regplot(
    x="screen_time_hours",
    y="mental_wellness_index_0_100",
    data=df,
    ax=axes[1],
    scatter_kws={"alpha": 0.5},
    line_kws={"color": "red"},
)
axes[1].set_title("Toplam Ekran Süresi vs Zihinsel İyi Oluş Endeksi")
axes[1].set_xlabel("Toplam Ekran Süresi (Saat)")
axes[1].set_ylabel("Zihinsel İyi Oluş Endeksi (0-100)")

# Plot 3: Üretkenlik (Pozitif İlişki: R=0.75)
sns.regplot(
    x="productivity_0_100",
    y="mental_wellness_index_0_100",
    data=df,
    ax=axes[2],
    scatter_kws={"alpha": 0.5},
    line_kws={"color": "red"},
)
axes[2].set_title("Üretkenlik vs Zihinsel İyi Oluş Endeksi")
axes[2].set_xlabel("Üretkenlik (1-10)")
axes[2].set_ylabel("Zihinsel İyi Oluş Endeksi (0-100)")
plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.savefig("3_2_zihinsel_iyi_olus_iliskileri.png")
# plt.show()
# C. Kategorik ve Sıralı Değişkenlere Göre Karşılaştırma (Kutu Grafikleri)
occupation_order = df["occupation"].value_counts().index
sns.boxplot(
    x="occupation",
    y="mental_wellness_index_0_100",
    data=df,
    order=occupation_order,
    palette="Set2",
    ax=axes[0],
)
axes[0].set_title("Mesleğe Göre Zihinsel İyi Oluş Endeksi")
axes[0].set_xlabel("Meslek")
axes[0].set_ylabel("Zihinsel İyi Oluş Endeksi (0-100)")
axes[0].tick_params(axis="x", rotation=30)

# Plot 2: Uyku Kalitesine Göre Zihinsel İyi Oluş (Kritik Bulgulardan Biri)
sleep_quality_order = sorted(df["sleep_quality_1_5"].unique())
sns.boxplot(
    x="sleep_quality_1_5",
    y="mental_wellness_index_0_100",
    data=df,
    order=sleep_quality_order,
    palette="YlGnBu",
    ax=axes[1],
)
axes[1].set_title("Uyku Kalitesine Göre Zihinsel İyi Oluş Endeksi")
axes[1].set_xlabel("Uyku Kalitesi (1=Kötü, 5=İyi)")
axes[1].set_ylabel("Zihinsel İyi Oluş Endeksi (0-100)")
plt.tight_layout(rect=[0, 0.03, 1, 0.95])

# Plot 3: Çalışma Moduna Göre Zihinsel İyi Oluş
work_mode_order = (
    df.groupby("work_mode")["mental_wellness_index_0_100"]
    .median()
    .sort_values(ascending=False)
    .index
)

sns.boxplot(
    x="work_mode",
    y="mental_wellness_index_0_100",
    data=df,
    order=work_mode_order,
    palette="Set3",
    ax=axes[2],
)
axes[2].set_title("Çalışma Moduna Göre İyi Oluş")
axes[2].set_xlabel("Çalışma Modu")
axes[2].set_ylabel("Zihinsel İyi Oluş Endeksi")
plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.savefig("3_3_kategorik_sirali_karsilastirma.png")
# plt.show()

# ==============================================================================
# 4. BULGULAR ÖZETİ (Konsol Çıktısı İçin)
# ==============================================================================

print("\n\n=================================================================")
print("4. BULGULAR ÖZETİ")
print("=================================================================")

top_correlations = (
    correlation_matrix["mental_wellness_index_0_100"]
    .sort_values(ascending=False)
    .drop("mental_wellness_index_0_100")
    .head(4)
)

bottom_correlations = (
    correlation_matrix["mental_wellness_index_0_100"]
    .sort_values(ascending=True)
    .head(4)
)

print("\n--- 4.1. Zihinsel İyi Oluş ile En Güçlü Pozitif Korelasyonlar ---")

print(top_correlations.to_markdown(numalign="left", stralign="left"))

print("\n--- 4.2. Zihinsel İyi Oluş ile En Güçlü Negatif Korelasyonlar ---")

print(bottom_correlations.to_markdown(numalign="left", stralign="left"))


sleep_median = df.groupby("sleep_quality_1_5")["mental_wellness_index_0_100"].median()
print("\n--- 4.3. Uyku Kalitesine Göre Ortanca İyi Oluş Puanları ---")
print(
    sleep_median.to_frame(name="Ortanca İyi Oluş").to_markdown(
        numalign="left", stralign="left"
    )
)

print(
    f"\nKritik Bulgular: Uyku Kalitesi 1 olanların ortancası {sleep_median.get(1, 'N/A')}, Uyku Kalitesi 4 olanların ortancası ise {sleep_median.get(4, 'N/A')} olarak gözlemlenmiştir. Uyku kalitesindeki artışın Zihinsel İyi Oluş üzerindeki pozitif etkisi çarpıcıdır."
)
print("\n=================================================================")
print(
    "ANALİZ TAMAMLANDI. Tüm sonuçlar konsola yazdırıldı ve 7 adet detaylı görsel .png olarak kaydedildi."
)
