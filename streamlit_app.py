import streamlit as st

st.title("🎈 halo barudak")
<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Tabel Periodik Interaktif</title>
    <style>
        :root {
            --bg-color: #0f172a;
            --card-bg: #1e293b;
            --text-color: #f8fafc;
            --accent: #38bdf8;
        }

        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background-color: var(--bg-color);
            color: var(--text-color);
            margin: 0;
            display: flex;
            flex-direction: column;
            align-items: center;
            padding: 20px;
        }

        h1 { margin-bottom: 20px; color: var(--accent); }

        /* Grid Tabel Periodik */
        .periodic-table {
            display: grid;
            grid-template-columns: repeat(18, minmax(40px, 1fr));
            gap: 4px;
            max-width: 1200px;
            width: 100%;
        }

        .element {
            aspect-ratio: 1 / 1;
            background-color: var(--card-bg);
            border: 1px solid #334155;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            cursor: pointer;
            transition: all 0.2s;
            border-radius: 4px;
            position: relative;
        }

        .element:hover {
            transform: scale(1.1);
            z-index: 10;
            border-color: var(--accent);
            box-shadow: 0 0 15px rgba(56, 189, 248, 0.5);
        }

        .atomic-number { font-size: 0.6rem; position: absolute; top: 2px; left: 4px; }
        .symbol { font-weight: bold; font-size: 1.1rem; }
        .name { font-size: 0.5rem; text-align: center; }

        /* Kategori Warna (Contoh) */
        .nonmetal { border-left: 4px solid #fbbf24; }
        .noble-gas { border-left: 4px solid #818cf8; }
        .alkali-metal { border-left: 4px solid #f87171; }

        /* Panel Informasi */
        #info-panel {
            margin-top: 30px;
            padding: 20px;
            background: var(--card-bg);
            border-radius: 8px;
            width: 100%;
            max-width: 600px;
            border: 1px solid var(--accent);
            display: none;
        }

        .info-grid {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 10px;
        }

        .info-item { border-bottom: 1px solid #334155; padding: 5px 0; }
        .info-label { color: #94a3b8; font-size: 0.8rem; }
    </style>
</head>
<body>

    <h1>Tabel Periodik Interaktif</h1>

    <div class="periodic-table" id="table">
        <!-- Elemen akan diisi oleh JavaScript -->
    </div>

    <div id="info-panel">
        <h2 id="el-name">Pilih Elemen</h2>
        <div class="info-grid">
            <div class="info-item"><div class="info-label">Simbol</div><div id="el-symbol">-</div></div>
            <div class="info-item"><div class="info-label">Nomor Atom</div><div id="el-number">-</div></div>
            <div class="info-item"><div class="info-label">Massa Atom</div><div id="el-mass">-</div></div>
            <div class="info-item"><div class="info-label">Konfigurasi Elektron</div><div id="el-config">-</div></div>
            <div class="info-item"><div class="info-label">Titik Didih</div><div id="el-boil">-</div></div>
            <div class="info-item"><div class="info-label">Penemu</div><div id="el-discoverer">-</div></div>
        </div>
    </div>

    <script>
        // Data contoh (tambahkan elemen lain di sini)
        const elements = [
            { no: 1, s: 'H', n: 'Hydrogen', m: '1.008', cat: 'nonmetal', col: 1, row: 1, config: '1s1', boil: '20.28 K', disc: 'Henry Cavendish' },
            { no: 2, s: 'He', n: 'Helium', m: '4.0026', cat: 'noble-gas', col: 18, row: 1, config: '1s2', boil: '4.22 K', disc: 'Pierre Janssen' },
            { no: 3, s: 'Li', n: 'Lithium', m: '6.94', cat: 'alkali-metal', col: 1, row: 2, config: '[He] 2s1', boil: '1615 K', disc: 'Johan August Arfwedson' },
            // Tambahkan elemen lainnya mengikuti pola ini...
        ];

        const table = document.getElementById('table');
        const panel = document.getElementById('info-panel');

        function renderTable() {
            elements.forEach(el => {
                const div = document.createElement('div');
                div.className = `element ${el.cat}`;
                div.style.gridColumn = el.col;
                div.style.gridRow = el.row;
                
                div.innerHTML = `
                    <span class="atomic-number">${el.no}</span>
                    <span class="symbol">${el.s}</span>
                    <span class="name">${el.n}</span>
                `;

                div.onclick = () => showInfo(el);
                table.appendChild(div);
            });
        }

        function showInfo(el) {
            panel.style.display = 'block';
            document.getElementById('el-name').innerText = `${el.n} (${el.s})`;
            document.getElementById('el-symbol').innerText = el.s;
            document.getElementById('el-number').innerText = el.no;
            document.getElementById('el-mass').innerText = el.m;
            document.getElementById('el-config').innerText = el.config;
            document.getElementById('el-boil').innerText = el.boil;
            document.getElementById('el-discoverer').innerText = el.disc;
            
            // Scroll otomatis ke panel info
            panel.scrollIntoView({ behavior: 'smooth' });
        }

        renderTable();
    </script>
</body>
</html>
