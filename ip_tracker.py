import requests
import folium
import webbrowser
import tempfile
import tkinter as tk
from tkinter import messagebox

def get_ip_info(ip=""):
    try:
        if ip == "":
            ip = requests.get("https://api.ipify.org").text
        url = f"https://ipinfo.io/{ip}/json?token=359f604680f479"
        response = requests.get(url, timeout=5)
        data = response.json()
        return data
    except Exception as e:
        print(f"Error: {e}")
        return None

def show_map(location_str):
    try:
        lat, lon = map(float, location_str.split(","))
        map_obj = folium.Map(location=[lat, lon], zoom_start=10)
        folium.Marker([lat, lon], popup="IP Location").add_to(map_obj)

        temp_file = tempfile.NamedTemporaryFile(suffix=".html", delete=False)
        map_obj.save(temp_file.name)
        webbrowser.open(f"file://{temp_file.name}")
    except Exception as e:
        print(f"Map error: {e}")

def lookup_ip():
    ip = entry_ip.get().strip()
    info = get_ip_info(ip)
    if info and 'loc' in info:
        result_text = (
            f"IP: {info.get('ip', 'N/A')}\n"
            f"Hostname: {info.get('hostname', 'N/A')}\n"
            f"City: {info.get('city', 'N/A')}\n"
            f"Region: {info.get('region', 'N/A')}\n"
            f"Country: {info.get('country', 'N/A')}\n"
            f"Org/ISP: {info.get('org', 'N/A')}\n"
            f"Location: {info.get('loc', 'N/A')}\n"
            f"Timezone: {info.get('timezone', 'N/A')}"
        )
        lbl_result.config(text=result_text)
        show_map(info['loc'])
    else:
        messagebox.showerror("Error", "Could not retrieve information. Check the IP and try again.")

# GUI setup
root = tk.Tk()
root.title("Upgraded IP Geolocation Tracker")

tk.Label(root, text="Enter IP Address (leave blank for your own IP):").pack(pady=5)
entry_ip = tk.Entry(root, width=35)
entry_ip.pack(pady=5)

btn_lookup = tk.Button(root, text="Lookup IP", command=lookup_ip)
btn_lookup.pack(pady=10)

lbl_result = tk.Label(root, text="", justify="left", font=("Consolas", 10))
lbl_result.pack(padx=10, pady=10)

root.mainloop()


