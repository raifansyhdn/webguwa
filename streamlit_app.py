import streamlit as st

st.title("periodik demo")
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(layout="wide", page_title="Tabel Periodik Interaktif")

# Bungkus seluruh kode HTML, CSS, dan JS dalam satu variabel string
html_code = """
<!DOCTYPE html>
<html>
<head>
    <style>
        :root {
            --bg: #0f172a; --card: #1e293b; --text: #f1f5f9; --accent: #38bdf8;
            --alkali: #ef4444; --noble: #a855f7; --nonmetal: #22c55e; --metal: #eab308;
        }
        body {
            font-family: sans-serif;
            background-color: var(--bg); color: var(--text);
            margin: 0; padding: 20px;
        }
        .periodic-table {
            display: grid;
            grid-template-columns: repeat(18, 1fr);
            gap: 4px;
            margin-bottom: 20px;
        }
        .element {
            aspect-ratio: 1/1; background: var(--card); border: 1px solid #334155;
            display: flex; flex-direction: column; align-items: center; justify-content: center;
            cursor: pointer; border-radius: 4px; transition: 0.2s;
        }
        .element:hover { transform: scale(1.1); border-color: var(--accent); z-index: 10; }
        .num { font-size: 0.7rem; opacity: 0.6; }
        .sym { font-size: 1.2rem; font-weight: bold; }
        .alkali { border-bottom: 3px solid var(--alkali); }
        .noble { border-bottom: 3px solid var(--noble); }
        .nonmetal { border-bottom: 3px solid var(--nonmetal); }
        .metal { border-bottom: 3px solid var(--metal); }
        
        #detail {
            background: var(--card); border: 1px solid var(--accent);
            padding: 15px; border-radius: 8px; margin-top: 20px; min-height: 100px;
        }
    </style>
</head>
<body>
    <h2 style="color:var(--accent); text-align:center;">Tabel Periodik Interaktif</h2>
    <div class="periodic-table" id="grid"></div>
    <div id="detail"><i>Klik elemen untuk melihat informasi detail...</i></div>

    <script>
        const elements = [
            { n: 1, s: "H", name: "Hydrogen", m: 1.008, x: 1, y: 1, cat: "nonmetal" },
            { n: 2, s: "He", name: "Helium", m: 4.002, x: 18, y: 1, cat: "noble" },
            { n: 3, s: "Li", name: "Lithium", m: 6.94, x: 1, y: 2, cat: "alkali" },
            { n: 4, s: "Be", name: "Beryllium", m: 9.012, x: 2, y: 2, cat: "metal" },
            { n: 5, s: "B", name: "Boron", m: 10.81, x: 13, y: 2, cat: "metal" },
            { n: 6, s: "C", name: "Carbon", m: 12.01, x: 14, y: 2, cat: "nonmetal" },
            { n: 10, s: "Ne", name: "Neon", m: 20.17, x: 18, y: 2, cat: "noble" }
        ];

        const grid = document.getElementById('grid');
        elements.forEach(el => {
            const div = document.createElement('div');
            div.className = `element ${el.cat}`;
            div.style.gridColumn = el.x;
            div.style.gridRow = el.y;
            div.innerHTML = `<span class="num">${el.n}</span><span class="sym">${el.s}</span>`;
            div.onclick = () => {
                document.getElementById('detail').innerHTML = `
                    <h3 style="margin:0; color:#38bdf8">${el.name} (${el.s})</h3>
                    <p>Nomor Atom: ${el.n} | Massa: ${el.m} | Kategori: ${el.cat}</p>
                `;
            };
            grid.appendChild(div);
        });
    </script>
</body>
</html>
"""

# Eksekusi HTML di dalam Streamlit
components.html(html_code, height=600, scrolling=True)
