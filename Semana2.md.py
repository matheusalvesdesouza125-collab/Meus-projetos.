pip install firebase-admin
import firebase_admin
from firebase_admin import credentials, db
cred = credentials.Certificate('/content/drive/MyDrive/FIREBASE/bancodd-f30da-firebase-adminsdk-fbsvc-1aa3fdaf5c.json')
firebase_admin.initialize_app (cred, {
'databaseURL' : 'https://bancodd-f30da-default-rtdb.firebaseio.com/'
})
aventureiros_ref = db.reference('/aventureiros')


aventureiros_ref.set({
'001' : {
'nome': 'André Luiz',
'classe': 'Aventureiro',
'nivel': 1,
'guilda': 'Vale do Espantalho'
},
'002': {
'nome': 'Angelina Brito',
'classe': 'Aventureiro',
'nivel': 1,
'guilda': 'Vale do Espantalho'
},
'003':{
'nome': 'Arthur Silva',
'classe': 'Aventureiro',
'nivel': 1,
'guilda': 'Assombro'
},
'004': {
'nome': 'Bruno Bonatto',
'classe': 'Aventureiro',
'nivel': 1,
'guilda': 'Vale do Espantalho'
},
'005': {
'nome': 'Cauê',
'classe': 'Aventureiro',
'nivel': 1,
'guilda': 'Vale do Espantalho'
},


'006': {
'nome': 'Enzo',
'classe': 'Aventureiro',
'nivel': 1,
'guilda': 'Vale do Espantalho'
},


'007': {
'nome': 'Eryck',
'classe': 'Aventureiro',
'nivel': 1,
'guilda': 'Vale do Espantalho'
},


'008': {
'nome': 'Giullia',
'classe': 'Aventureiro',
'nivel': 1,
'guilda': 'Vale do Espantalho'
},


'009': {
'nome': 'Guilherme Pescuma',
'classe': 'Aventureiro',
'nivel': 1,
'guilda': 'Vale do Espantalho'
},


'010': {
'nome': 'Lucas Mendes',
'classe': 'Aventureiro',
'nivel': 1,
'guilda': 'Vale do Espantalho'
},
