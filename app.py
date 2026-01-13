import streamlit as st 
st.title(" dyqani online")

def encrypt_password(password):
    result = ""
    for char in password:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + 3) % 26 + base)
        else:
            result += char
    return result

emri_valid = email_valid = numri_valid = adresa_valid = password_valid = kodi_postar_valid = False 
encrypted_password = None

emri=st.text_input("Ju lutem shkruani emrin tuaj dhe mbiemrin tuaj")

if not emri:
    st.error("Ju lutem shkruani emrin tuaj dhe mbiemrin tuaj mos e lerni bosh.")
    emri_valid = False
else:
    
    if any(char.isdigit() for char in emri):
        st.error("Emri dhe mbiemri nuk duhet të përmbajë numra.")
    elif" " not in emri.strip():
        st.error("Ju lutem shkruani emrin dhe mbiemrin tuaj të plotë.") 
    else:
        st.success("Emri dhe mbiemri juaj janë të vlefshëm.")
        emri_valid = True
 
        
        
email=st.text_input("Ju lutem shkruani emailin tuaj",type="default")
if email:
    if "@" not in email or "."not in email:
        st.error("ju keni harruar simbolin @ ne email ose e keni harruar nje pike(.)  ju lutem rishikone emailin tuaj")
    elif  not email.endswith((".com",".net",".org")):
        st.error("Ju lutem sigurohuni që emaili juaj të përfundojë me .com, .net, ose .org")
    elif len(email)>90:
        st.error("Email është shumë i gjatë (max 90 karaktere)")
    else:
        st.success("Emaili juaj është i vlefshëm.")
        email_valid = True
    
numri=st.text_input("Ju lutem shkruani numrin tuaj te telefonit" )
if numri:
    if numri and not numri.isdigit():
        st.error("Numri juaj duhet te shenohet vetum me numra KUJDES!?.")
    elif len(numri) != 9:
        st.error("Numri juaj i telefonit duhet të ketë saktësisht 9 shifra.")
    elif not numri.startswith(("044", "045", "046", "048", "049")):
        st.error("Numri i telefonit duhet me fillu me 044,045,046,048,049.")
    else:
        st.success("Numri juaj i telefonit është i vlefshëm.")
        numri_valid = True
                
adresa = st.text_input("Ju lutem shkruani adresen tuaj")
kodi_postar = st.text_input("Ju lutem shkruani kodin postar")
if adresa and kodi_postar:
    if not adresa.strip():
        st.error("Ju lutem shkruani adresën tuaj!")
    elif not kodi_postar.isdigit():
        st.error("Kodi postar duhet të shënohet vetëm me numra!")
    elif len(kodi_postar) != 5:
        st.error("Kodi postar duhet të ketë saktësisht 5 shifra!")
    else:
        st.success("Adresa dhe kodi postar janë të vlefshëm!")
        adresa_valid = True
        kodi_postar_valid = True

password = st.text_input("Ju lutem shkruani fjalekalimin tuaj", type="password")
confirm_password = st.text_input("Ju lutem konfirmoni fjalekalimin tuaj", type="password")

if password and confirm_password:
    password = password.strip()
    confirm_password = confirm_password.strip()
    
    if password and len(password) < 8:
        st.error("Fjalekalimi duhet të ketë të paktën 8 karaktere.")
    elif password != confirm_password:
        st.error("Fjalekalimet nuk përputhen. Ju lutem provoni përsëri.")   
    else:
        encrypted_password = encrypt_password(password)
        password_valid = True
    
if st.button("Regjistrohu"):    
    if emri_valid and email_valid and numri_valid and adresa_valid and kodi_postar_valid and password_valid:
        st.success("Të gjitha të dhënat janë të vlefshme dhe regjistrimi është i suksesshëm!")
        st.success("Fjalëkalimi u enkriptua me sukses!")
        st.write("Fjalëkalimi juaj i enkriptuar është:", encrypted_password)
        st.balloons()
    else:
        st.error("Ju lutem sigurohuni që të gjitha fushat të jenë të plota dhe të vlefshme para regjistrimit.")