import tkinter as tk
from tkinter import ttk, messagebox
from typing import Dict, List

# ─── BASIS PENGETAHUAN ───────────────────────────────────────────────────────

GEJALA = {
    "G1": "Nafas abnormal",
    "G2": "Suara serak",
    "G3": "Perubahan kulit",
    "G4": "Telinga penuh",
    "G5": "Nyeri bicara/menelan",
    "G6": "Nyeri tenggorokan",
    "G7": "Nyeri leher",
    "G8": "Pendarahan hidung",
    "G9": "Telinga berdenging",
    "G10": "Air liur menetes",
    "G11": "Perubahan suara",
    "G12": "Sakit kepala",
    "G13": "Nyeri pinggir hidung",
    "G14": "Serangan vertigo",
    "G15": "Getah bening membesar",
    "G16": "Leher bengkak",
    "G17": "Hidung tersumbat",
    "G18": "Infeksi sinus",
    "G19": "Berat badan turun",
    "G20": "Nyeri telinga",
    "G21": "Selaput lendir merah",
    "G22": "Benjolan di leher",
    "G23": "Tubuh tidak seimbang",
    "G24": "Bola mata bergerak",
    "G25": "Nyeri wajah",
    "G26": "Dahi sakit",
    "G27": "Batuk",
    "G28": "Tumbuh di mulut",
    "G29": "Benjolan di leher",
    "G30": "Nyeri antara mata",
    "G31": "Radang gendang telinga",
    "G32": "Tenggorokan gatal",
    "G33": "Hidung meler",
    "G34": "Tuli",
    "G35": "Mual muntah",
    "G36": "Letih lesu",
    "G37": "Demam",
}

PENYAKIT = [
    {"nama": "Tonsilitis",                  "gejala": ["G37","G12","G5","G27","G6","G21"]},
    {"nama": "Sinusitis Maksilaris",        "gejala": ["G37","G12","G27","G17","G33","G36","G29"]},
    {"nama": "Sinusitis Frontalis",         "gejala": ["G37","G12","G27","G17","G33","G36","G21","G26"]},
    {"nama": "Sinusitis Edmoidalis",        "gejala": ["G37","G12","G27","G17","G33","G36","G21","G30","G13","G26"]},
    {"nama": "Sinusitis Sfenoidalis",       "gejala": ["G37","G12","G27","G17","G33","G36","G29","G7"]},
    {"nama": "Abses Peritonsiler",          "gejala": ["G37","G12","G6","G15","G2","G29","G10"]},
    {"nama": "Faringitis",                  "gejala": ["G37","G5","G6","G7","G15"]},
    {"nama": "Kanker Laring",               "gejala": ["G5","G27","G6","G15","G2","G19","G1"]},
    {"nama": "Deviasi Septum",              "gejala": ["G37","G17","G20","G8","G18","G25"]},
    {"nama": "Laringitis",                  "gejala": ["G37","G5","G15","G16","G32"]},
    {"nama": "Kanker Leher & Kepala",       "gejala": ["G5","G22","G8","G28","G3","G11"]},
    {"nama": "Otitis Media Akut",           "gejala": ["G37","G20","G35","G31"]},
    {"nama": "Contact Ulcers",              "gejala": ["G5","G2"]},
    {"nama": "Abses Parafaringeal",         "gejala": ["G5","G16"]},
    {"nama": "Barotitis Media",             "gejala": ["G12","G20"]},
    {"nama": "Kanker Nasofaring",           "gejala": ["G17","G8"]},
    {"nama": "Kanker Tonsil",               "gejala": ["G6","G29"]},
    {"nama": "Neuronitis Vestibularis",     "gejala": ["G35","G24"]},
    {"nama": "Meniere",                     "gejala": ["G20","G35","G14","G4"]},
    {"nama": "Tumor Syaraf Pendengaran",    "gejala": ["G12","G34","G23"]},
    {"nama": "Kanker Leher Metastatik",     "gejala": ["G29"]},
    {"nama": "Osteosklerosis",              "gejala": ["G34","G9"]},
    {"nama": "Vertigo Postular",            "gejala": ["G24"]},
]

# ─── MESIN INFERENSI ─────────────────────────────────────────────────────────

def inferensi(gejala_dipilih: List[str]) -> List[Dict[str, object]]:
    """
    Forward chaining: cocokkan gejala input terhadap setiap rule penyakit.
    Skor = bobot coverage (60%) + bobot precision (40%).
    Hanya kembalikan penyakit dengan minimal 1 gejala cocok.
    """
    if not gejala_dipilih:
        return []

    hasil = []
    for p in PENYAKIT:
        cocok = [g for g in p["gejala"] if g in gejala_dipilih]
        if not cocok:
            continue
        coverage  = len(cocok) / len(p["gejala"])   # seberapa terpenuhi rule
        precision = len(cocok) / len(gejala_dipilih) # relevansi input
        skor = round(coverage * 0.6 + precision * 0.4, 4)
        hasil.append({
            "nama":      p["nama"],
            "gejala":    p["gejala"],
            "cocok":     cocok,
            "coverage":  coverage,
            "precision": precision,
            "skor":      skor,
        })

    hasil.sort(key=lambda x: x["skor"], reverse=True)
    return hasil[:5]  # top-5

# ─── ANTARMUKA GUI ───────────────────────────────────────────────────────────

class SistemPakarTHT(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Sistem Pakar Diagnosis Penyakit THT")
        self.geometry("900x680")
        self.resizable(True, True)
        self.configure(bg="#F8F9FA")

        self.var_gejala = {k: tk.BooleanVar() for k in GEJALA}
        self.var_search = tk.StringVar()
        self.var_search.trace_add("write", lambda *_: self._filter_gejala())

        self._build_ui()

    # ── layout utama ────────────────────────────────────────────────────────

    def _build_ui(self):
        # Header
        header = tk.Frame(self, bg="#1A73E8", pady=12)
        header.pack(fill="x")
        tk.Label(header, text="Sistem Pakar Diagnosis Penyakit THT",
                 font=("Helvetica", 15, "bold"), fg="white", bg="#1A73E8").pack()
        tk.Label(header, text="Berbasis Forward Chaining | Praktikum KB Pertemuan 5",
                 font=("Helvetica", 9), fg="#BBDEFB", bg="#1A73E8").pack()

        # Body: split kiri (gejala) | kanan (hasil)
        body = tk.Frame(self, bg="#F8F9FA")
        body.pack(fill="both", expand=True, padx=14, pady=12)
        body.columnconfigure(0, weight=3, minsize=380)
        body.columnconfigure(1, weight=4)
        body.rowconfigure(0, weight=1)

        self._panel_gejala(body)
        self._panel_hasil(body)

    # ── panel kiri: pilih gejala ─────────────────────────────────────────────

    def _panel_gejala(self, parent):
        frame = tk.LabelFrame(parent, text=" Pilih Gejala ",
                              font=("Helvetica", 10, "bold"),
                              bg="#F8F9FA", fg="#333333", padx=8, pady=8)
        frame.grid(row=0, column=0, sticky="nsew", padx=(0,6))
        frame.rowconfigure(1, weight=1)
        frame.columnconfigure(0, weight=1)

        # Search
        sf = tk.Frame(frame, bg="#F8F9FA")
        sf.grid(row=0, column=0, sticky="ew", pady=(0,6))
        tk.Label(sf, text="Cari:", bg="#F8F9FA", font=("Helvetica", 9)).pack(side="left")
        tk.Entry(sf, textvariable=self.var_search, font=("Helvetica", 10),
                 relief="solid", bd=1).pack(side="left", fill="x", expand=True, padx=(4,0))

        # Scrollable checkbox list
        container = tk.Frame(frame, bg="#F8F9FA")
        container.grid(row=1, column=0, sticky="nsew")
        container.rowconfigure(0, weight=1)
        container.columnconfigure(0, weight=1)

        canvas = tk.Canvas(container, bg="#F8F9FA", highlightthickness=0)
        scrollbar = ttk.Scrollbar(container, orient="vertical", command=canvas.yview)
        canvas.configure(yscrollcommand=scrollbar.set)
        canvas.grid(row=0, column=0, sticky="nsew")
        scrollbar.grid(row=0, column=1, sticky="ns")

        self.chk_frame = tk.Frame(canvas, bg="#F8F9FA")
        self.canvas_window = canvas.create_window((0, 0), window=self.chk_frame, anchor="nw")

        def _on_resize(e):
            canvas.itemconfig(self.canvas_window, width=e.width)
        canvas.bind("<Configure>", _on_resize)
        self.chk_frame.bind("<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
        canvas.bind_all("<MouseWheel>",
            lambda e: canvas.yview_scroll(-1*(e.delta//120), "units"))

        self.chk_widgets = {}
        self._render_checkboxes()

        # Tombol aksi
        btn_frame = tk.Frame(frame, bg="#F8F9FA")
        btn_frame.grid(row=2, column=0, sticky="ew", pady=(8,0))
        btn_frame.columnconfigure(0, weight=1)
        btn_frame.columnconfigure(1, weight=1)

        tk.Button(btn_frame, text="Diagnosa", font=("Helvetica", 10, "bold"),
                  bg="#1A73E8", fg="white", activebackground="#1558B0",
                  relief="flat", cursor="hand2", padx=10, pady=6,
                  command=self._diagnosa).grid(row=0, column=0, sticky="ew", padx=(0,4))
        tk.Button(btn_frame, text="Reset", font=("Helvetica", 10),
                  bg="#E8EAED", fg="#333", activebackground="#DADCE0",
                  relief="flat", cursor="hand2", padx=10, pady=6,
                  command=self._reset).grid(row=0, column=1, sticky="ew")

        self.lbl_count = tk.Label(frame, text="0 gejala dipilih",
                                  font=("Helvetica", 8), fg="#888", bg="#F8F9FA")
        self.lbl_count.grid(row=3, column=0, sticky="w", pady=(4,0))

    def _render_checkboxes(self, filter_str=""):
        for w in self.chk_frame.winfo_children():
            w.destroy()
        self.chk_widgets.clear()

        keys = [k for k in GEJALA
                if filter_str.lower() in GEJALA[k].lower()
                or filter_str.lower() in k.lower()]

        for i, k in enumerate(keys):
            row_bg = "#FFFFFF" if i % 2 == 0 else "#F1F3F4"
            row = tk.Frame(self.chk_frame, bg=row_bg)
            row.pack(fill="x")
            cb = tk.Checkbutton(row, variable=self.var_gejala[k],
                                text=f"{k}  –  {GEJALA[k]}",
                                font=("Helvetica", 9), bg=row_bg,
                                activebackground=row_bg, anchor="w",
                                command=self._update_count)
            cb.pack(fill="x", padx=6, pady=2)
            self.chk_widgets[k] = cb

    def _filter_gejala(self):
        self._render_checkboxes(self.var_search.get())

    def _update_count(self):
        n = sum(1 for v in self.var_gejala.values() if v.get())
        self.lbl_count.config(text=f"{n} gejala dipilih")

    # ── panel kanan: hasil ───────────────────────────────────────────────────

    def _panel_hasil(self, parent):
        frame = tk.LabelFrame(parent, text=" Hasil Diagnosis ",
                              font=("Helvetica", 10, "bold"),
                              bg="#F8F9FA", fg="#333333", padx=8, pady=8)
        frame.grid(row=0, column=1, sticky="nsew")
        frame.rowconfigure(0, weight=1)
        frame.columnconfigure(0, weight=1)

        canvas = tk.Canvas(frame, bg="#F8F9FA", highlightthickness=0)
        scrollbar = ttk.Scrollbar(frame, orient="vertical", command=canvas.yview)
        canvas.configure(yscrollcommand=scrollbar.set)
        canvas.grid(row=0, column=0, sticky="nsew")
        scrollbar.grid(row=0, column=1, sticky="ns")

        self.result_frame = tk.Frame(canvas, bg="#F8F9FA")
        self.result_win = canvas.create_window((0, 0), window=self.result_frame, anchor="nw")

        def _on_resize(e):
            canvas.itemconfig(self.result_win, width=e.width)
        canvas.bind("<Configure>", _on_resize)
        self.result_frame.bind("<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

        self._show_placeholder()

    def _show_placeholder(self):
        for w in self.result_frame.winfo_children():
            w.destroy()
        tk.Label(self.result_frame,
                 text="Pilih gejala lalu klik Diagnosa\nuntuk melihat hasil.",
                 font=("Helvetica", 11), fg="#AAAAAA", bg="#F8F9FA",
                 justify="center").pack(pady=60)

    def _tampilkan_hasil(self, hasil):
        for w in self.result_frame.winfo_children():
            w.destroy()

        if not hasil:
            tk.Label(self.result_frame,
                     text="Tidak ditemukan penyakit yang sesuai\ndengan kombinasi gejala ini.",
                     font=("Helvetica", 11), fg="#C62828", bg="#F8F9FA",
                     justify="center").pack(pady=60)
            return

        for i, h in enumerate(hasil):
            is_top = (i == 0)
            card_bg = "#E8F0FE" if is_top else "#FFFFFF"
            border   = "#1A73E8" if is_top else "#DADCE0"

            card = tk.Frame(self.result_frame, bg=card_bg,
                            highlightbackground=border, highlightthickness=1)
            card.pack(fill="x", padx=4, pady=(0 if i > 0 else 0, 8))

            inner = tk.Frame(card, bg=card_bg, padx=10, pady=8)
            inner.pack(fill="x")

            # Nama + badge
            top_row = tk.Frame(inner, bg=card_bg)
            top_row.pack(fill="x")
            badge_text = "Kemungkinan Utama" if is_top else f"Alternatif {i}"
            badge_bg   = "#1A73E8" if is_top else "#5F6368"
            tk.Label(top_row, text=h["nama"],
                     font=("Helvetica", 11, "bold"), fg="#1A1A1A", bg=card_bg
                     ).pack(side="left")
            tk.Label(top_row, text=f" {badge_text} ",
                     font=("Helvetica", 8), fg="white", bg=badge_bg,
                     padx=4, pady=2).pack(side="right")

            # Skor
            skor_pct = int(h["skor"] * 100)
            tk.Label(inner, text=f"Skor kesesuaian: {skor_pct}%  |  "
                                 f"Coverage: {int(h['coverage']*100)}%  |  "
                                 f"Precision: {int(h['precision']*100)}%",
                     font=("Helvetica", 8), fg="#555555", bg=card_bg
                     ).pack(anchor="w", pady=(2,4))

            # Progress bar skor
            self._progress_bar(inner, skor_pct, card_bg, "#1A73E8" if is_top else "#78909C")

            # Gejala cocok / tidak cocok
            gejala_input = [k for k, v in self.var_gejala.items() if v.get()]
            tag_frame = tk.Frame(inner, bg=card_bg)
            tag_frame.pack(fill="x", pady=(6,0))
            tk.Label(tag_frame, text="Gejala:", font=("Helvetica", 8, "bold"),
                     fg="#555", bg=card_bg).pack(anchor="w")

            wrap = tk.Frame(tag_frame, bg=card_bg)
            wrap.pack(fill="x")
            for g in h["gejala"]:
                match = g in h["cocok"]
                fg_c  = "#0D47A1" if match else "#888888"
                bg_c  = "#BBDEFB" if match else "#EEEEEE"
                tk.Label(wrap, text=f"{g}: {GEJALA.get(g, g)}",
                         font=("Helvetica", 8), fg=fg_c, bg=bg_c,
                         padx=5, pady=2, relief="flat"
                         ).pack(side="left", padx=2, pady=2)

    def _progress_bar(self, parent, pct, bg, fill_color):
        outer = tk.Frame(parent, bg="#DADCE0", height=6)
        outer.pack(fill="x", pady=(0,2))
        outer.pack_propagate(False)
        inner = tk.Frame(outer, bg=fill_color, height=6)
        inner.place(x=0, y=0, relwidth=pct/100, relheight=1)

    # ── aksi tombol ─────────────────────────────────────────────────────────

    def _diagnosa(self):
        gejala_dipilih = [k for k, v in self.var_gejala.items() if v.get()]
        if not gejala_dipilih:
            messagebox.showwarning("Peringatan", "Pilih minimal satu gejala terlebih dahulu.")
            return
        hasil = inferensi(gejala_dipilih)
        self._tampilkan_hasil(hasil)

    def _reset(self):
        for v in self.var_gejala.values():
            v.set(False)
        self.var_search.set("")
        self._render_checkboxes()
        self._update_count()
        self._show_placeholder()

# ─── ENTRY POINT ─────────────────────────────────────────────────────────────

if __name__ == "__main__":
    app = SistemPakarTHT()
    app.mainloop()
