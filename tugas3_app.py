import streamlit as st

def main():
    st.title("Aplikasi Streamlit di VSCode")
    
    long_paragraph = (
        "Ini adalah paragraf panjang yang berisi banyak teks. "
        "Anda dapat menambahkan sebanyak yang Anda inginkan "
        "untuk menampilkan teks dalam satu paragraf."
    )
    
    st.write(long_paragraph)

if __name__ == "__main__":
    main()
