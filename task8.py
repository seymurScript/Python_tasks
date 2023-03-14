
#Qalıqlı ve qalıqsız bölmə ilə minlik mərtəbədəki ədədi tapmaq

# Məsələn ədəd 3453 dür.
a = int(input("Eded: "))

# ədədi 1000ə bölür və qalıqda alınan 453ü yazır.
qaliq = a % 1000

# ədəddən qalığı çıxıb tam bölünəcək vəziyətə gətiririk.
tam = a - qaliq

# burada isə ədədin minlik mərtəbəsindəki rəqəmi tapmış oluruq.
min = tam/1000

print("Minlik mərtəbəsindəki rəqəm: ", min, "-dir")
