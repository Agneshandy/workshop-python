# Di Anaconda Prompt atau di jendela terminal Anda, ketik berikut ini:
# conda create --name snowflakes biopython

# Conda memeriksa untuk melihat paket tambahan apa ("ketergantungan") yang dibutuhkan BioPython, dan menanyakan apakah Anda ingin melanjutkan:
# Proceed ([y]/n)? y

# Untuk menggunakan, atau "mengaktifkan" lingkungan baru, ketik berikut ini:
# conda activate snowflakes

# Untuk melihat daftar semua lingkungan Anda, ketik:
# conda info --envs

# Daftar lingkungan muncul, mirip dengan berikut ini:
"""
conda environments:

    base           /home/username/Anaconda3
    snowflakes   * /home/username/Anaconda3/envs/snowflakes
"""

# Ubah lingkungan Anda saat ini kembali ke default (basis):
# conda activate