import streamlit as st 
st.title("Online Store")

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

emri = st.text_input("Please enter your first name and last name")

if not emri:
    st.error("Please enter your first name and last name, do not leave it empty.")
    emri_valid = False
else:
    
    if any(char.isdigit() for char in emri):
        st.error("First name and last name must not contain numbers.")
    elif " " not in emri.strip():
        st.error("Please enter your full first name and last name.") 
    else:
        st.success("Your first name and last name are valid.")
        emri_valid = True
 
        
        
email = st.text_input("Please enter your email", type="default")
if email:
    if "@" not in email or "." not in email:
        st.error("You forgot the @ symbol in your email or you forgot a dot (.). Please review your email.")
    elif not email.endswith((".com", ".net", ".org")):
        st.error("Please make sure your email ends with .com, .net, or .org")
    elif len(email) > 90:
        st.error("Email is too long (max 90 characters)")
    else:
        st.success("Your email is valid.")
        email_valid = True
    
numri = st.text_input("Please enter your phone number")
if numri:
    if numri and not numri.isdigit():
        st.error("Your number must be written using numbers only. BE CAREFUL!")
    elif len(numri) != 9:
        st.error("Your phone number must contain exactly 9 digits.")
    elif not numri.startswith(("044", "045", "046", "048", "049")):
        st.error("The phone number must start with 044, 045, 046, 048, or 049.")
    else:
        st.success("Your phone number is valid.")
        numri_valid = True
                
adresa = st.text_input("Please enter your address")
kodi_postar = st.text_input("Please enter your postal code")
if adresa and kodi_postar:
    if not adresa.strip():
        st.error("Please enter your address!")
    elif not kodi_postar.isdigit():
        st.error("Postal code must contain numbers only!")
    elif len(kodi_postar) != 5:
        st.error("Postal code must contain exactly 5 digits!")
    else:
        st.success("Address and postal code are valid!")
        adresa_valid = True
        kodi_postar_valid = True

password = st.text_input("Please enter your password", type="password")
confirm_password = st.text_input("Please confirm your password", type="password")

if password and confirm_password:
    password = password.strip()
    confirm_password = confirm_password.strip()
    
    if password and len(password) < 8:
        st.error("Password must contain at least 8 characters.")
    elif password != confirm_password:
        st.error("Passwords do not match. Please try again.")   
    else:
        encrypted_password = encrypt_password(password)
        password_valid = True
    
if st.button("Register"):    
    if emri_valid and email_valid and numri_valid and adresa_valid and kodi_postar_valid and password_valid:
        st.success("All data is valid and registration was successful!")
        st.success("Password was encrypted successfully!")
        st.write("Your encrypted password is:", encrypted_password)
        st.balloons()
    else:
        st.error("Please make sure all fields are complete and valid before registration.")
