#buat initial database dulu pakai cara di bawah ini, run pake python di cmd aja

from application import db
db.create_all()

# setelah file db udah muncul di file explorer, db siap di-isi. 
# Kita coba masukin 1 row db dulu
# Run lagi aja di python cmd

from application import Users
user = Users(name="broto", email="broto.uhuy@email.com")
db.session.add(user)
db.session.commit()