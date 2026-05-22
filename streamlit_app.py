import streamlit as st

st.title("Titik koordinat SUKI pada map")
<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Tabel Periodik Interaktif Modern</title>
    <style>
        :root {
            --bg: #0f172a;
            --card: #1e293b;
            --text: #f1f5f9;
            --accent: #38bdf8;
            /* Warna Kategori */
            --alkali: #ef4444;
            --noble: #a855f7;
            --nonmetal: #22c55e;
            --metal: #eab308;
        }

        body {
            font-family: 'Inter', system-ui, sans-serif;
            background-color: var(--bg);
            color: var(--text);
            display: flex;
            flex-direction: column;
            align-items: center;
            padding: 40px 20px;
            margin: 0;
        }

        .container { max-width: 1200px; width: 100%; }

        h1 { text-align: center; color: var(--accent); margin-bottom: 30px; }

        /* Grid Utama */
        .periodic-table {
            display: grid;
            grid-template-columns: repeat(18, 1fr);
            gap: 5px;
            margin-bottom: 40px;
            overflow-x: auto;
            padding: 10px;
        }

        .element {
            aspect-ratio: 1/1;
            background: var(--card);
            border: 1px solid #334155;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1);
            border-radius: 4px;
            padding: 2px;
        }

        .element:hover {
            transform: scale(1.2);
            z-index: 50;
            box-shadow: 0 0 20px rgba(56, 189, 248, 0.4);
            border-color: var(--accent);
        }

        .num { font-size: 0.6rem; margin-bottom: 2px; opacity: 0.7; }
        .sym { font-size: 1.1rem; font-weight: 800; }
        .name { font-size: 0.5rem; text-transform: uppercase; opacity: 0.8; letter-spacing: 0.5px; }

        /* Pewarnaan Berdasarkan Kelas (Dinamis via JS) */
        .alkali { border-bottom: 3px solid var(--alkali); }
        .noble { border-bottom: 3px solid var(--noble); }
        .nonmetal { border-bottom: 3px solid var(--nonmetal); }
        .metal { border-bottom: 3px solid var(--metal); }

        /* Panel Detail */
        #detail-card {
            background: var(--card);
            border: 2px solid var(--accent);
            border-radius: 12px;
            padding: 25px;
            display: none; /* Muncul saat diklik */
            animation: fadeIn 0.3s ease;
        }

        @keyframes fadeIn { from { opacity: 0; transform: translateY(10px); } to { opacity: 1; transform: translateY(0); } }

        .detail-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
            gap: 20px;
            margin-top: 15px;
        }

        .stat-box { background: rgba(255,255,255,0.05); padding: 10px; border-radius: 6px; }
        .label { font-size: 0.75rem; color: var(--accent); text-transform: uppercase; }
        .val { font-size: 1rem; font-weight: 600; margin-top: 4px; }
    </style>
</head>
<body>

<div class="container">
    <h1>Periodic Table Explorer</h1>
    
    <div class="periodic-table" id="table-grid"></div>

    <div id="detail-card">
        <h2 id="d-name" style="margin-top:0">Pilih Elemen</h2>
        <div class="detail-grid">
            <div class="stat-box"><div class="label">Simbol</div><div id="d-sym" class="val">-</div></div>
            <div class="stat-box"><div class="label">Nomor Atom</div><div id="d-num" class="val">-</div></div>
            <div class="stat-box"><div class="label">Massa</div><div id="d-mass" class="val">-</div></div>
            <div class="stat-box"><div class="label">Konfigurasi</div><div id="d-conf" class="val">-</div></div>
            <div class="stat-box"><div class="label">Kategori</div><div id="d-cat" class="val">-</div></div>
        </div>
    </div>
</div>

<script>
    // Dataset Dasar (Saya tambahkan lebih banyak agar tabel tidak kosong)
    const elements = [
        { n: 1, s: "H", name: "Hydrogen", m: 1.008, x: 1, y: 1, cat: "nonmetal", conf: "1s1" },
        { n: 2, s: "He", name: "Helium", m: 4.002, x: 18, y: 1, cat: "noble", conf: "1s2" },
        { n: 3, s: "Li", name: "Lithium", m: 6.94, x: 1, y: 2, cat: "alkali", conf: "[He] 2s1" },
        { n: 4, s: "Be", name: "Beryllium", m: 9.012, x: 2, y: 2, cat: "metal", conf: "[He] 2s2" },
        { n: 5, s: "B", name: "Boron", m: 10.81, x: 13, y: 2, cat: "metal", conf: "[He] 2s2 2p1" },
        { n: 6, s: "C", name: "Carbon", m: 12.01, x: 14, y: 2, cat: "nonmetal", conf: "[He] 2s2 2p2" },
        { n: 7, s: "N", name: "Nitrogen", m: 14.00, x: 15, y: 2, cat: "nonmetal", conf: "[He] 2s2 2p3" },
        { n: 8, s: "O", name: "Oxygen", m: 15.99, x: 16, y: 2, cat: "nonmetal", conf: "[He] 2s2 2p4" },
        { n: 9, s: "F", name: "Fluorine", m: 18.99, x: 17, y: 2, cat: "nonmetal", conf: "[He] 2s2 2p5" },
        { n: 10, s: "Ne", name: "Neon", m: 20.17, x: 18, y: 2, cat: "noble", conf: "[He] 2s2 2p6" },
        { n: 11, s: "Na", name: "Sodium", m: 22.98, x: 1, y: 3, cat: "alkali", conf: "[Ne] 3s1" },
        { n: 18, s: "Ar", name: "Argon", m: 39.94, x: 18, y: 3, cat: "noble", conf: "[Ne] 3s2 3p6" }
    ];

    const grid = document.getElementById('table-grid');

    function createTable() {
        elements.forEach(el => {
            const btn = document.createElement('div');
            btn.className = `element ${el.cat}`;
            btn.style.gridColumn = el.x;
            btn.style.gridRow = el.y;

            btn.innerHTML = `
                <span class="num">${el.n}</span>
                <span class="sym">${el.s}</span>
                <span class="name">${el.name}</span>
            `;

            btn.onclick = () => showDetail(el);
            grid.appendChild(btn);
        });
    }

    function showDetail(el) {
        const card = document.getElementById('detail-card');
        card.style.display = 'block';
        
        document.getElementById('d-name').innerText = el.name;
        document.getElementById('d-sym').innerText = el.s;
        document.getElementById('d-num').innerText = el.n;
        document.getElementById('d-mass').innerText = el.m + " u";
        document.getElementById('d-conf').innerText = el.conf;
        document.getElementById('d-cat').innerText = el.cat.toUpperCase();
        
        card.scrollIntoView({ behavior: 'smooth', block: 'start' });
    }

    createTable();
</script>

</body>
</html>
