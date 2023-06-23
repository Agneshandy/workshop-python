# Anda dapat menginstal versi terbaru dari sebuah paket dengan menentukan nama paket:
# (tutorial-env) $ python -m pip install novas
# Output
"""
Collecting novas
  Downloading novas-3.1.1.3.tar.gz (136kB)
Installing collected packages: novas
  Running setup.py install for novas
Successfully installed novas-3.1.1.3
"""

# Anda juga dapat menginstal versi tertentu dari sebuah paket dengan memberikan nama paket diikuti dengan ==dan nomor versinya:
# (tutorial-env) $ python -m pip install requests==2.6.0
# Output
"""
Collecting requests==2.6.0
  Using cached requests-2.6.0-py2.py3-none-any.whl
Installing collected packages: requests
Successfully installed requests-2.6.0
"""

# Anda dapat memberikan nomor versi yang berbeda untuk mendapatkan versi tersebut, atau Anda dapat menjalankan untuk memutakhirkan paket ke versi terbaru:python -m pip install --upgrade
# (tutorial-env) $ python -m pip install --upgrade requests
# Output
"""
Collecting requests
Installing collected packages: requests
  Found existing installation: requests 2.6.0
    Uninstalling requests-2.6.0:
      Successfully uninstalled requests-2.6.0
Successfully installed requests-2.7.0
"""

# python -m pip uninstalldiikuti oleh satu atau lebih nama paket akan menghapus paket dari lingkungan virtual.
# python -m pip showakan menampilkan informasi tentang paket tertentu:
# (tutorial-env) $ python -m pip show requests
# Output
"""
Metadata-Version: 2.0
Name: requests
Version: 2.7.0
Summary: Python HTTP for Humans.
Home-page: http://python-requests.org
Author: Kenneth Reitz
Author-email: me@kennethreitz.com
License: Apache 2.0
Location: /Users/akuchling/envs/tutorial-env/lib/python3.4/site-packages
Requires:
"""

# python -m pip listakan menampilkan semua paket yang diinstal di lingkungan virtual:
# (tutorial-env) $ python -m pip list
# Output
"""
novas (3.1.1.3)
numpy (1.9.2)
pip (7.0.3)
requests (2.7.0)
setuptools (16.0)
"""

# python -m pip freezeakan menghasilkan daftar serupa dari paket-paket yang diinstal,
# tetapi hasilnya menggunakan format yang diharapkan. Konvensi umum adalah memasukkan daftar ini ke dalam file:python -m pip installrequirements.txt
# (tutorial-env) $ python -m pip freeze > requirements.txt
# (tutorial-env) $ cat requirements.txt
# Output
"""
novas==3.1.1.3
numpy==1.9.2
requests==2.7.0
"""

# Kemudian dapat requirements.txtdikomit ke kontrol versi dan dikirim sebagai bagian dari aplikasi.
# Pengguna kemudian dapat menginstal semua paket yang diperlukan dengan :install -r
# (tutorial-env) $ python -m pip install -r requirements.txt
# Output
"""
Collecting novas==3.1.1.3 (from -r requirements.txt (line 1))
  ...
Collecting numpy==1.9.2 (from -r requirements.txt (line 2))
  ...
Collecting requests==2.7.0 (from -r requirements.txt (line 3))
  ...
Installing collected packages: novas, numpy, requests
  Running setup.py install for novas
Successfully installed novas-3.1.1.3 numpy-1.9.2 requests-2.7.0
"""