import tkinter as tk
from tkinter import ttk, messagebox

city_info = {
    # ===== Metro Cities =====
    "Delhi": (
        "Delhi - The Capital of India\n\n"
        "Top Attractions:\n"
        "  - Red Fort (Lal Qila)\n"
        "  - India Gate\n"
        "  - Qutub Minar\n"
        "  - Humayun's Tomb\n"
        "  - Lotus Temple\n"
        "  - Akshardham Temple\n\n"
        "Best Time to Visit: October to March\n"
        "Famous Food: Chole Bhature, Paranthas, Butter Chicken, Chaat"
    ),
    "Mumbai": (
        "Mumbai - The City of Dreams\n\n"
        "Top Attractions:\n"
        "  - Gateway of India\n"
        "  - Marine Drive\n"
        "  - Elephanta Caves\n"
        "  - Juhu Beach\n"
        "  - Siddhivinayak Temple\n"
        "  - Chhatrapati Shivaji Terminus\n\n"
        "Best Time to Visit: November to February\n"
        "Famous Food: Vada Pav, Pav Bhaji, Bombay Sandwich, Bhel Puri"
    ),
    "Kolkata": (
        "Kolkata - The City of Joy\n\n"
        "Top Attractions:\n"
        "  - Victoria Memorial\n"
        "  - Howrah Bridge\n"
        "  - Dakshineswar Temple\n"
        "  - Indian Museum\n"
        "  - Eden Gardens\n"
        "  - Belur Math\n\n"
        "Best Time to Visit: October to February\n"
        "Famous Food: Rosogolla, Mishti Doi, Kathi Roll, Sandesh"
    ),
    "Chennai": (
        "Chennai - Gateway to South India\n\n"
        "Top Attractions:\n"
        "  - Marina Beach\n"
        "  - Kapaleeshwarar Temple\n"
        "  - Fort St. George\n"
        "  - San Thome Basilica\n"
        "  - Government Museum\n"
        "  - Mahabalipuram (nearby)\n\n"
        "Best Time to Visit: November to February\n"
        "Famous Food: Idli, Dosa, Filter Coffee, Chettinad Cuisine"
    ),
    "Bengaluru": (
        "Bengaluru - The Garden City / Silicon Valley of India\n\n"
        "Top Attractions:\n"
        "  - Lalbagh Botanical Garden\n"
        "  - Bangalore Palace\n"
        "  - Cubbon Park\n"
        "  - Vidhana Soudha\n"
        "  - ISKCON Temple\n"
        "  - Nandi Hills (nearby)\n\n"
        "Best Time to Visit: October to February\n"
        "Famous Food: Bisi Bele Bath, Mysore Pak, Masala Dosa, Ragi Mudde"
    ),
    "Hyderabad": (
        "Hyderabad - The City of Pearls / Cyberabad\n\n"
        "Top Attractions:\n"
        "  - Charminar\n"
        "  - Golconda Fort\n"
        "  - Ramoji Film City\n"
        "  - Hussain Sagar Lake\n"
        "  - Chowmahalla Palace\n"
        "  - Salar Jung Museum\n\n"
        "Best Time to Visit: October to February\n"
        "Famous Food: Hyderabadi Biryani, Haleem, Mirchi ka Salan, Double ka Meetha"
    ),
    "Ahmedabad": (
        "Ahmedabad - The Manchester of India\n\n"
        "Top Attractions:\n"
        "  - Sabarmati Ashram\n"
        "  - Adalaj Stepwell\n"
        "  - Sidi Saiyyed Mosque\n"
        "  - Kankaria Lake\n"
        "  - Akshardham Temple (Gandhinagar)\n"
        "  - Jama Masjid\n\n"
        "Best Time to Visit: November to February\n"
        "Famous Food: Dhokla, Thepla, Fafda-Jalebi, Gujarati Thali"
    ),
    "Pune": (
        "Pune - The Oxford of the East\n\n"
        "Top Attractions:\n"
        "  - Shaniwar Wada\n"
        "  - Aga Khan Palace\n"
        "  - Sinhagad Fort\n"
        "  - Dagdusheth Halwai Ganpati Temple\n"
        "  - Osho Ashram\n"
        "  - Lonavala (nearby)\n\n"
        "Best Time to Visit: October to February\n"
        "Famous Food: Misal Pav, Bhakarwadi, Puran Poli, Pune Vada Pav"
    ),

    # ===== Chhattisgarh / UP / Odisha Heritage Cities =====
    "Ambikapur": (
        "Ambikapur - Cultural Capital of Surguja, Chhattisgarh\n\n"
        "Top Attractions:\n"
        "  - Mahamaya Temple\n"
        "  - Ghunghutta Dam\n"
        "  - Thinthini Pathar (musical stone)\n"
        "  - Deogarh\n"
        "  - Sarbhanja Waterfall\n"
        "  - Garden City Park\n\n"
        "Best Time to Visit: October to March\n"
        "Famous Food: Chila, Faraa, Dehrori, Aamat, Bafauri"
    ),
    "Mainpat": (
        "Mainpat - The Shimla of Chhattisgarh / Mini Tibet\n\n"
        "Top Attractions:\n"
        "  - Tiger Point & Fish Point\n"
        "  - Jaljali (bouncing land)\n"
        "  - Ulta Pani (reverse flowing water)\n"
        "  - Jalpari Point\n"
        "  - Tibetan Buddhist Monastery\n"
        "  - Mehta Point Sunset View\n\n"
        "Best Time to Visit: April to July (and Oct-Feb)\n"
        "Famous Food: Tibetan Momos, Thukpa, Fish Curry Rice, Chicken Chilly"
    ),
    "Varanasi": (
        "Varanasi - The Spiritual Capital of India\n\n"
        "Top Attractions:\n"
        "  - Kashi Vishwanath Temple\n"
        "  - Dashashwamedh Ghat (Ganga Aarti)\n"
        "  - Sarnath\n"
        "  - Manikarnika Ghat\n"
        "  - Ramnagar Fort\n"
        "  - Assi Ghat\n\n"
        "Best Time to Visit: October to March\n"
        "Famous Food: Banarasi Paan, Kachori Sabzi, Malaiyo, Tamatar Chaat"
    ),
    "Prayagraj": (
        "Prayagraj (Allahabad) - The Sangam City\n\n"
        "Top Attractions:\n"
        "  - Triveni Sangam (Ganga, Yamuna, Saraswati)\n"
        "  - Allahabad Fort\n"
        "  - Anand Bhavan\n"
        "  - Khusro Bagh\n"
        "  - All Saints Cathedral\n"
        "  - Kumbh Mela Ground\n\n"
        "Best Time to Visit: October to March\n"
        "Famous Food: Allahabadi Tehri, Dum Aloo, Chaat, Lai (Ramdana)"
    ),

    # ===== Other Popular Tourist Cities =====
    "Jaipur": (
        "Jaipur - The Pink City\n\n"
        "Top Attractions:\n"
        "  - Hawa Mahal\n"
        "  - Amber Fort\n"
        "  - City Palace\n"
        "  - Jantar Mantar\n"
        "  - Nahargarh Fort\n"
        "  - Jal Mahal\n\n"
        "Best Time to Visit: October to March\n"
        "Famous Food: Dal Baati Churma, Ghewar, Pyaaz Kachori, Laal Maas"
    ),
    "Agra": (
        "Agra - City of the Taj\n\n"
        "Top Attractions:\n"
        "  - Taj Mahal\n"
        "  - Agra Fort\n"
        "  - Fatehpur Sikri\n"
        "  - Mehtab Bagh\n"
        "  - Itmad-ud-Daulah's Tomb\n"
        "  - Akbar's Tomb\n\n"
        "Best Time to Visit: November to February\n"
        "Famous Food: Petha, Bedai, Mughlai Cuisine, Dalmoth"
    ),
    "Udaipur": (
        "Udaipur - The City of Lakes\n\n"
        "Top Attractions:\n"
        "  - Lake Pichola\n"
        "  - City Palace\n"
        "  - Jag Mandir\n"
        "  - Saheliyon Ki Bari\n"
        "  - Fateh Sagar Lake\n"
        "  - Sajjangarh Monsoon Palace\n\n"
        "Best Time to Visit: September to March\n"
        "Famous Food: Dal Baati, Gatte Ki Sabzi, Laal Maas, Mawa Kachori"
    ),
    "Goa": (
        "Goa - The Beach Paradise\n\n"
        "Top Attractions:\n"
        "  - Baga Beach\n"
        "  - Calangute Beach\n"
        "  - Basilica of Bom Jesus\n"
        "  - Dudhsagar Falls\n"
        "  - Fort Aguada\n"
        "  - Anjuna Flea Market\n\n"
        "Best Time to Visit: November to February\n"
        "Famous Food: Fish Curry Rice, Bebinca, Vindaloo, Prawn Balchao"
    ),
    "Bhubaneswar": (
        "Bhubaneswar - The Temple City of India / Capital of Odisha\n\n"
        "Top Attractions:\n"
        "  - Lingaraja Temple\n"
        "  - Mukteshvara Temple\n"
        "  - Rajarani Temple\n"
        "  - Udayagiri & Khandagiri Caves\n"
        "  - Dhauli Shanti Stupa\n"
        "  - Nandankanan Zoological Park\n"
        "  - Odisha State Museum\n\n"
        "Best Time to Visit: October to March\n"
        "Famous Food: Dalma, Pakhala Bhata, Chhena Poda, Macha Ghanta, Rasagola"
    ),
    "Puri": (
        "Puri - The Temple City of India \n\n"
        "Top Attractions:\n"
        "  - Jagnnath Temple\n"
        "  - Swargadwar\n"
        "  - Puri Beach\n"
        "  - Shankaracharya Temple\n"
        "  - Konark Sun Temple\n"
        "  - Karar Ashram\n"
        "  - Temple Parikraman\n\n"
        "Best Time to Visit: October to March\n"
        "Famous Food: Khaja, Puri, pathuri, Macha Ghanta, Rasagola"
    ),
    
}


def show_city_info(event=None):
    city = city_var.get()
    if city == "-- Select a City --" or not city:
        messagebox.showwarning("No Selection", "Please select a city from the dropdown.")
        return
    info_text.config(state="normal")
    info_text.delete("1.0", tk.END)
    info_text.insert(tk.END, city_info[city])
    info_text.config(state="disabled")


root = tk.Tk()
root.title("India Tourism App")
root.geometry("620x620")
root.configure(bg="#fff5e6")

title = tk.Label(
    root,
    text="Incredible India Tourism",
    font=("Helvetica", 22, "bold"),
    bg="#fff5e6",
    fg="#cc5500",
)
title.pack(pady=15)

subtitle = tk.Label(
    root,
    text="Metro Cities | Heritage Cities | Hill Stations | Beaches",
    font=("Helvetica", 10, "italic"),
    bg="#fff5e6",
    fg="#666666",
)
subtitle.pack()

prompt = tk.Label(
    root,
    text="Which city would you like to explore?",
    font=("Helvetica", 12),
    bg="#fff5e6",
    fg="#333333",
)
prompt.pack(pady=10)

city_var = tk.StringVar()
city_dropdown = ttk.Combobox(
    root,
    textvariable=city_var,
    values=["-- Select a City --"] + sorted(city_info.keys()),
    state="readonly",
    font=("Helvetica", 11),
    width=35,
)
city_dropdown.current(0)
city_dropdown.pack(pady=10)
city_dropdown.bind("<<ComboboxSelected>>", show_city_info)

show_btn = tk.Button(
    root,
    text="Show Tourism Info",
    font=("Helvetica", 11, "bold"),
    bg="#cc5500",
    fg="white",
    activebackground="#a64500",
    activeforeground="white",
    padx=15,
    pady=6,
    command=show_city_info,
)
show_btn.pack(pady=8)

info_text = tk.Text(
    root,
    height=18,
    width=68,
    font=("Helvetica", 10),
    bg="#ffffff",
    fg="#222222",
    wrap="word",
    state="disabled",
    relief="solid",
    borderwidth=1,
)
info_text.pack(pady=10, padx=20)

footer = tk.Label(
    root,
    text=f"Total Cities Available: {len(city_info)}  |  Plan your journey across Incredible India!",
    font=("Helvetica", 9, "italic"),
    bg="#fff5e6",
    fg="#555555",
)
footer.pack(pady=5)

root.mainloop()
