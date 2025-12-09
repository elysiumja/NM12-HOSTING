
# ░███    ░██ ░███     ░███   ░██    ░██████     ░██     ░██   ░██████     ░██████   ░██████████░██████░███    ░██   ░██████  
# ░████   ░██ ░████   ░████ ░████   ░██   ░██    ░██     ░██  ░██   ░██   ░██   ░██      ░██      ░██  ░████   ░██  ░██   ░██ 
# ░██░██  ░██ ░██░██ ░██░██   ░██         ░██    ░██     ░██ ░██     ░██ ░██             ░██      ░██  ░██░██  ░██ ░██        
# ░██ ░██ ░██ ░██ ░████ ░██   ░██     ░█████     ░██████████ ░██     ░██  ░████████      ░██      ░██  ░██ ░██ ░██ ░██  █████ 
# ░██  ░██░██ ░██  ░██  ░██   ░██    ░██         ░██     ░██ ░██     ░██         ░██     ░██      ░██  ░██  ░██░██ ░██     ██ 
# ░██   ░████ ░██       ░██   ░██   ░██          ░██     ░██  ░██   ░██   ░██   ░██      ░██      ░██  ░██   ░████  ░██  ░███ 
# ░██    ░███ ░██       ░██ ░██████ ░████████    ░██     ░██   ░██████     ░██████       ░██    ░██████░██    ░███   ░█████░█ 


# GRACIAS POR ELEGIRNOS COMO TU HOSTING DE SERVIDORES DE MINECRAFT...
# ESTAMOS BRINDANDO SOPORTE ACTIVO EN NUESTRA COMUNIDAD DE DISCORD: https://discord.gg/RQUgvma9C4
#                                                                                                                                                                                                                                                                                                                                                                                                                                                          
# ================
# 	NM12 STARTER
# ================

#! PASOS PARA INICIAR TU SERVIDOR:

# 1. Haz click al botón de arriba a la derecha (►) (ENCENDER)
# 2. Selecciona la opcion "1"
# 3. Asegurate de estar conectado a la aplicación de Tailscale --> La ip de tu servidor se mostrará al autenticar
# 4. Una vez recibida la señal de "Done!" o "Servidor iniciado", podrás acceder a él desde Minecraft
# 5. Haz click al botón de arriba a la derecha (►) (APAGAR)
























# =================================================
# No toques nada de aquí para abajo, puedes dañarlo
# =================================================
I=None
F='.'
H=print
E='nt'
try:import requests as G
except:B.system('pip install requests');import requests as G
finally:import os as B,base64 as J,glob as D,time
if B.name==E:
	C='NM12';B.system('title NM12 STARTER')
	if not B.path.exists(C):B.mkdir(C)
else:C=F
if B.name==E:A=f"{C}\\.gitignore"
else:A='.gitignore'
if not B.path.exists(A):
	K='L3RhaWxzY2FsZS1jcwovd29ya19hcmVhKgpjb21wb3Nlci4qCi9QeXRob24qCioub3V0cHV0Ci9Nb2RnZXN0Ci90aGFub3MKL3ZlbmRvcgovYmtkaXIKamF2YS8KKi5leGUKKi5tc2kKKi50eHQKKi5weWMKKi5tc3AKKi5tc3gKbXN4LnB5';L=J.standard_b64decode(K).decode()
	with open(A,'w')as M:M.write(L)
def N(download_path=C):
	F='*.msx';N='https://minecraft-sx.github.io/data/links.json'
	if B.name==E:A=D.glob(f"{C}\\sel*.exe")
	else:A=D.glob(F)
	if len(A)>0:A=A[0]
	else:A=''
	try:
		L=G.get(N)
		if L.status_code==200:
			M=L.json()
			if B.name==E:J=M.get('latest_win')
			else:J=M.get('latest')
			A=J.split('/')[-1];O=D.glob(f"{C}\\sel*.exe");K=next(iter(O),I)
			if K==I:K=''
			if A in D.glob(F)or():return A
			elif B.name==E and A in K:return A
			else:
				if B.name!=E:B.system('rm *.msx >> /dev/null 2>&1')
				else:B.system(f"del /f /q {C}\\sel*.exe")
				H('Actualizando tu versión de MSX...');P=B.path.join(download_path,A)
				with open(P,'wb')as Q:Q.write(G.get(J).content)
				return A
		else:
			H('Error al actualizar NM12')
			if A in D.glob(F)or A in D.glob(f"{C}\\sel*.exe"):return A
	except Exception as R:
		H(f"Error general: {R}")
		if A in D.glob(F)or A in D.glob(f"{C}\\sel*.exe"):return A
def O():
	A=N()
	if A==I:return
	elif A.split(F)[-1]=='msx':B.system(f"chmod +x {A} && ./{A}")
	elif A.split(F)[-1]=='exe':B.system(f"start /D {C} {C}\\{A} && exit")
	else:B.system(f"python3 {A}")
O()
